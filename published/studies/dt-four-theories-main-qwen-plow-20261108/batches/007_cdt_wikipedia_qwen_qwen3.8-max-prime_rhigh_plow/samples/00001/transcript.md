# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00001

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a0b81d1a-8cda-4344-8bc5-dc03e67ff682/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a0b81d1a-8cda-4344-8bc5-dc03e67ff682/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request. Need produce mathematical essay/blog post about CDT applying to decision problems, 2400-3000 words including references. Need use supplied reference. Need careful. User is English. Final essay. Need likely ~2600 words. Need include mathematical definitions, equations, examples, explanations. Explain how theory evaluates actions/policies, dependencies, counterfactuals. Where source leaves open, explain uncertainty and operational interpretation if available, distinguish source claims vs own assumptions. Use examples. Finish conclusion. Avoid appendices, lengthy bibliography but references okay. Target approx 2400-3000 words. Need be coherent. Need probably include formal CDT with counterfactuals, do-operator perhaps as my addition? Source says CDT doesn't specify algorithm, Lewis imaging. Need maybe develop operational interpretation via causal Bayesian networks / do-calculus, Pearl, as additional proposal. Need distinguish source vs own. Need discuss EDT vs CDT, Newcomb, King David, Death in Damascus, Adversarial Offer, Psychopath Button. Need define action set A, outcomes O_j, desirability D(O_j), counterfactual probability P(A □→ O_j) or P(A -> O_j). Use notation. Discuss dependency hypotheses K, causal states. CDT expected utility U_CDT(a)=sum_k P(K=k) sum_o P(o | do(a), K) U(o) maybe. Or counterfactual. For policies: evaluate policy π as intervention setting decisions according to π? Need mention dynamic decisions maybe. Need address relevant dependencies and counterfactuals: hold fixed causal structure/background, intervention cuts evidential links not causal. Distinguish correlation vs causation. EDT uses conditional expected utility U_EDT(a)=sum_o P(o | a) D(o). CDT uses causal/counterfactual. If action independent of dependency hypotheses? Gibbard Harper condition. Need talk Lewis triviality: probability of conditional not conditional probability generally. Need source says if accept axioms and statistical independence of A and A→O_j then equality. Need explain.

Need maybe include equations:
EDT: V_E(a)=Σ_o P(o|a)D(o).
CDT: V_C(a)=Σ_o P(a □→ o)D(o). (counterfactual conditional probability). Or P(O=o | do(A=a)). If dependency hypotheses H_i partition: V_C(a)=Σ_i P(H_i) Σ_o P(o | do(a), H_i) D(o). Need note do(a) represents intervention. For policies π: V_C(π)=Σ_i P(H_i) E[D(O) | do(π), H_i], where do(π) sets choice variables as functions of info? Need maybe define policy as map from histories to actions. CDT evaluates by intervening to implement policy, but must be careful: if policy depends on observations, intervention is on decision rule not on observations? Need mention. In static one-shot: okay.

Need examples:
Apple/orange simple.
Good/bad apple uncertainty: if good prob p, happy utility +h, sad -s. CDT value eat apple = p*h + (1-p)*(-s), compare orange maybe -? This demonstrates expected causal consequences.
King David: define charisma C unknown fixed. Action send for Bathsheba B. Outcomes pleasure/revolt? EDT abstain because B evidence uncharismatic and revolt. CDT: C unaffected by action; causal effect of B is pleasure/injustice maybe; if desired and doesn't cause revolt, send. Need compute maybe P(revolt | B) high due to correlation but P(revolt | do(B), C) = P(revolt | not B, C) or independent? If unjust acts do not cause revolts. Need show.
Newcomb: predictor P sets B content based on prediction. CDT at decision time: content fixed, action doesn't cause content. do(two-box) doesn't change B. Value two-box = 1000 + maybe 0; one-box = maybe 1,000,000 if predicted one-box but already fixed. Conditional on action, EDT picks one-box. Need maybe compute with 99% accuracy. CDT: U(two)=1000 + P(Bfull)*1e6? Wait from causal perspective P(Bfull) is prior probability predictor predicted one-box, independent of action? Actually if predictor accurate, prior over your disposition? Need CDT holds fixed predictor's prediction distribution; expected value of two-box is 1000 + prior(Predicted one-box)*1e6, one-box is prior(Predicted one-box)*1e6. So two dominates by 1000. Need phrase: whatever content, two-box yields $1000 more than one-box. More formal: if B contains x (0 or 1M), two gets x+1000, one gets x, so causal expected utility difference = 1000. This is dominance under intervention.
Death in Damascus: Death predicts location. If you stay/flee, Death goes where predicted. CDT may see no causal influence? Actually if Death reliable, action evidentially indicates location but doesn't cause Death's prediction? If Death already predicted, going to Damascus or Aleppo won't change death? Need source says CDT unable to process correlation, may make irrational decisions. Need explain: if Death waits where predicted, CDT might be indifferent or choose randomly but still death. In variants loses money. Could discuss instability. Maybe include as criticism.
Adversarial Offer: two boxes, can buy one or none, cost 1. Seller puts $3 in each box predicted not acquire with accuracy .75. CDT reasons at least one box contains $3? Need careful: buyer can choose box 1 or box 2? Seller predicted for each whether buyer will acquire? If buyer chooses one, if predicted not acquire that box, contains $3. Since can buy at most one, seller likely predicted not acquire at least one? CDT calculates average box at least $1.50? Let's parse: Each box costs $1. Yesterday seller put $3 in each box she predicted buyer not to acquire. Both believe prediction accurate with prob 0.75. Buyer perspective: at least one box contains $3? If buyer will acquire at most one, there is at least one not acquired. Prediction accurate: if predicted not acquire, contains. But if predicted acquire, empty? Maybe accuracy .75 for each? CDT sees buying a box causally expected value > cost because for any particular box, conditional on choosing it? Need source says CDT reasons at least one box contains $3. Therefore average box contains at least $1.50 in causal expected value, more than cost. Hence buy one, profitable for seller. Need explain as counterexample where CDT voluntarily pays because it fails to recognize its choice is evidence of which box was predicted acquired? We can present briefly.
Psychopath button: Paul press button kills psychopaths. Paul believes only psychopath would press. If Paul is psychopath? Pressing causes psychopaths dead including Paul? He prefers living with psychopaths to dying. CDT: holding fixed psychopath status, if non-psychopath pressing would cause no psychopaths and good; if psychopath pressing causes death? Need Egan says CDT endorses pressing. Need analyze: CDT might use causal expected utility: if press, if Paul non-psychopath world good; if psychopath world death. But why endorse? Maybe because CDT holds fixed his type? Let's formalize: Let P = Paul psychopath. Prior high? Press B. Outcome: if press and non-psych: world no psychopaths, Paul lives, best. If press and psychopath: Paul dies (because all psychopaths killed), worst. If not press: lives with psychopaths. EDT says pressing is evidence psychopath, so don't. CDT says causal effect of pressing given type: for non-psych, press best; for psych, press worst. If he is quite confident only psychopath would press, then he should be quite confident he is psychopath if he feels inclined to press? CDT maybe uses unconditional credences in dependency hypotheses, not decision-dependent evidence. If he chooses press, CDT may still calculate using prior that he's non-psych? Wait Egan's point: CDT holds fixed initial views about likely causal structure, ignoring that choosing action provides evidence about type. But if Paul is quite confident only psychopath would press, he may update on the fact that he is considering pressing? CDT can incorporate evidence about inclinations? Joyce says can. Need discuss nuance. In simple CDT with prior P(psych) maybe low, pressing has high causal value if nonpsych, low if psych? But if P(psych) high enough, don't. Source says CDT endorses pressing. Need not fully resolve; present as alleged counterexample about self-predictive evidence. Maybe say under certain priors CDT presses, while intuitively shouldn't because the very inclination is evidence of psychopathy. Distinguish source claim vs my formal reconstruction.

Need address vagueness and operational interpretation:
Source: CDT doesn't specify algorithm to calculate counterfactual probabilities. Lewis imaging: move probability mass from each possible world w to closest w_A where A holds. Regress issue: need know what would believe if certain of A.
My proposal: For operational CDT, use structural causal model (SCM) or causal Bayesian network. Variables, DAG, structural equations. Intervention do(A=a) replaces equation for A. Counterfactual P(O_j | do(A=a)) computed by distribution over exogenous noise and modified equations. For fully specified SCM, U_CDT(a)=Σ_o P(o | do(a))D(o). If uncertainty over models, average over models. This addresses source's vagueness but is additional assumption not in source. Need say this is one reasonable operationalization; source only mentions Lewis imaging, not Pearl. Need perhaps connect imaging to do-operator: closest-world semantics corresponds to minimal intervention on causal model. Need discuss policies: do(π) means replace decision node(s) by policy function of allowed variables, not intervene on their inputs unless policy mandates? For dynamic: sequential plan evaluated by intervening at each decision point or setting a policy variable. Need mention if policy correlates with unmodeled variables, careful.

Need explain dependencies and counterfactuals: CDT holds fixed causal parents/background, not evidential descendants. It screens off correlations via causal graph. If common cause C influences A and O, intervening on A doesn't change C, so O not affected unless A causally affects O. In King David, charisma common cause of action and revolt. In Newcomb, predictor's prediction is caused by your disposition/choice? The content is pre-set. CDT says your current action doesn't causally affect past prediction. However if predictor's accuracy arises from common cause of action and prediction, CDT still ignores evidential link. This leads to criticism. Need mention dependency hypotheses: partition of possible causal structures. CDT conditions on each dependency hypothesis by prior, not updated by action (because action may be evidence about hypothesis but CDT holds fixed? Actually some versions update on action as news? Need source: Egan says CDT holds fixed unconditional credences in dependency hypotheses. Need explain. In causal network, dependency hypothesis includes graph and mechanisms; action may be evidence about graph if agent's dispositions correlated with graph? CDT typically uses prior over causal structures, not conditional on action, to avoid bootstrapping. Need discuss operational choice: when evaluating action, average over dependency hypotheses with prior P(H), not P(H|A), unless evidence about H is not decision-relevant? This is contested. Need maybe propose: If H is a causal hypothesis about how world works and A is an intervention, then under intervention the probability of H should be the pre-intervention probability, because an intervention on A does not provide evidence about H except via correlations between the agent's choice process and H. But if the agent's choice process is part of the world and correlated with H, this is tricky. Need articulate uncertainty.

Need include formal definitions:
Let decision problem be tuple (A, O, D, P_C). A finite actions. O outcome partition. D:O→ℝ desirability. Causal model M yields counterfactual probabilities P_M(O_j | do(A_i)). Then CDT chooses a* ∈ argmax_i V_C(a_i). If policies Π, choose π* maximizing V_C(π). Need mention expected utility theorem? Not necessary. Could mention ratifiability? Maybe not.

Need distinguish source vs own:
- Source claims: CDT recommends action causing best expected outcome; Gibbard-Harper formula; difference from EDT via counterfactual vs conditional probabilities; Lewis result; independence condition; examples and criticisms.
- Own additions: do-calculus/SCM operationalization, policy evaluation, dependency-hypothesis averaging, examples calculations, perhaps handling uncertainty over models. Need explicitly label "The source does not... I will..." and "This is my operational gloss, not in the reference."

Need perhaps mention principle of conditional excluded middle and independence: Source says Gibbard and Harper showed if accept two axioms (one related to conditional excluded middle), then statistical independence of A and A→O_j suffices to guarantee P(A→O_j)=P(O_j|A). But there are cases not independent. Need explain maybe not too deep. Could say: In many ordinary cases where taking A gives no evidence about the truth of counterfactual "if A were taken, O would occur", the counterfactual probability coincides with conditional probability. But in Newcomb/David, action is evidence about underlying type/prediction, so they diverge. Need be careful: "statistical independence of A and A→O_j" weird. Actually if A and counterfactual are independent, then P(A→O_j)=P(O_j|A)? Need just state source. Maybe mention controversial axiom.

Need maybe discuss "probability of counterfactual" notation: P(A □→ O_j). Since source uses P(A → O_j) maybe define. It says probability of it being the case that A necessarily implies O_j. Actually "counterfactual probability of it being the case that A necessarily implies O_j" awkward. Better: probability that if A were taken, O_j would obtain. Use □→.

Need target word count. Need final maybe ~2600 words. Let's estimate. Need not include too many references? Maybe include short reference list at end with source and maybe Pearl? User says avoid lengthy bibliographies. Could include references: Wikipedia source, Gibbard & Harper, Lewis, Pearl perhaps. Since additional assumption maybe cite Pearl. But source not include Pearl. It's okay? "including references and any other material". Need maybe brief references 4-5. Need no appendices.

Need structure:
Title: Causal Decision Theory: Choosing by What Actions Cause, Not What They Indicate
1. Introduction (define CDT, contrast EDT)
2. Expected causal utility: formal definition. Simple apple.
3. Counterfactuals and interventions: formal with do, dependency hypotheses. Operational interpretation (SCM). Policies.
4. Difference from EDT and independence: Lewis, King David.
5. Examples: Newcomb (dominance), maybe Prisoner's Dilemma/twin mention? Death in Damascus/Adversarial offer/Psychopath as criticisms.
6. Open questions and operational guidance: vagueness, imaging regress, SCM proposal; how to handle uncertainty over causal structure; policies; limitations.
7. Conclusion.
References.

Need ensure substantive mathematical essay. Use equations.

Let's draft mentally.

Opening:
"Causal decision theory (CDT) is a family of decision rules... The reference article defines it as..." Then formal.

Formal:
Let A = {a_1,...,a_n}; outcomes O_j partition; D(O_j) desirability; act a's causal expected utility:
V_C(a)=Σ_j P(a □→ O_j) D(O_j).
The operator □→ reads "if a were performed, O_j would obtain". If probabilities over outcomes: P(a □→ O_j) = P(O_j | do(a)) under intervention.
Choose a maximizing.
For policies: policy π maps info states h to actions. Evaluate V_C(π)=Σ_i P(K_i) Σ_o P(o | do(π), K_i) D(o). Need maybe define do(π) as setting decision nodes according to π while leaving other variables to usual causal laws.

Could include expected utility with dependency hypotheses:
Let K be partition of causal dependency hypotheses. For each K_k, define P_k(o | do(a)). Then
V_C(a)=Σ_k P(K_k) Σ_o P_k(o | do(a)) D(o).
The probabilities P(K_k) are prior credences about causal structure, not ordinarily conditional on a. This captures Egan's "holding fixed" (source). Need mention alternative: EDT conditions on action, so uses P(o|a) = Σ_k P(o|a,k)P(k|a). The difference P(k) vs P(k|a) often drives disputes.

Need explain counterfactual probability via imaging: Source says Lewis imaging: move probability mass from each world w to closest world w_A where A holds. Then P(A □→ O)=Σ_w P(w) 1[O in closest A-world]. But regress. My operationalization: SCM. Define variables X, equations X_i=f_i(PA_i,U_i), exogenous U. Intervention do(A=a) replaces equation A:=a. Then P(O=o | do(a)) = probability over U that O=o in modified model. Counterfactual for actual world u? Could mention observed evidence e: P(O_{a}=o | E=e) computed by abduction to posterior over U, then action, prediction. But perhaps too much. Since essay asks apply to decision problems, useful. Need label as addition.

Need examples with calculations:
Apple:
Action eat apple a. Unknown quality Q∈{G,B}, prior p. If G then happiness +10; if B sadness -5. Orange yields 0. CDT: V_C(apple)=p*10+(1-p)*(-5), choose if >0. EDT same here if Q independent of choice? Actually if choice not evidence about Q. But if seeing apple? Not necessary.

King David:
Variables C charisma (fixed), A send, R revolt, S pleasure/injustice. EDT: P(R|A) high because A evidence uncharismatic. CDT: V_C(A)=P(C) [D outcomes under do(A), C] + P(not C)... If R not caused by A, do(A) doesn't change R given C. If summoning gives pleasure but unjust? source says he knows unjust. Need maybe CDT may still recommend if desires outweigh? Source says CDT recommends sending for her because charisma cannot be changed. Need include caveat: assuming desire for Bathsheba outweighs moral disutility? Source says recommends sending; maybe because unjust acts do not cause revolt and he wants her. Need not compute.

Newcomb:
Let X∈{0,1,000,000} content. Actions one, two. Payoffs: one=X, two=X+1000. Under any causal model where current choice does not affect X, V_C(two)=V_C(one)+1000. So CDT two-boxes. EDT: if predictor 99% accurate: P(B full | one)=0.99, P(B full | two)=0.01; V_EDT(one)=990k, V_EDT(two)=0.01*1M + 1000=11k, so one-box. Need note this calculation uses conditional probabilities. CDT rejects using choice as evidence about already fixed content.

Adversarial Offer:
Need be precise enough. Let's reconstruct maybe:
Two boxes i=1,2, cost c=1. Buyer may buy one or none. Seller predicted each box acquisition; put $3 in boxes predicted not acquired. Prediction accuracy 0.75. If buyer buys box i, causal expected payoff? CDT treats the money in box i as fixed by prior prediction; for a randomly chosen box, probability it contains $3 maybe at least 0.5? Source says at least one contains $3, average at least $1.50. Therefore causal expected net ≥ $0.50, buy. But seller profits because buyer's choice is correlated with seller's predictions: the box buyer is inclined to buy is likely the one predicted bought and thus empty; the other contains $3. CDT's local causal averaging can miss the policy-level correlation. This illustrates critics' claim that CDT can voluntarily lose money. Need maybe careful: If buyer chooses one box according to some preference, seller predicted. If accurate, if buyer chooses box 1, likely seller predicted box1 acquired -> empty, box2 not acquired -> $3. Buying box1 yields likely empty minus $1, losing. But CDT's argument average across boxes? Hmm source says CDT reasons at least one contains $3. Therefore average box contains at least $1.50 in causal expected value. This seems odd: If at least one contains $3, average value across boxes is at least $1.50, but if you choose one without knowing which, causal expectation maybe $1.50. However if prediction accuracy .75, maybe actual chance chosen box contains money is 0.25, so expected value 0.75, below cost. Critics say CDT wrongly buys because it ignores that its choice indicates which box was predicted acquired. Need present as source's description, not fully formalize. Could mention "as presented in source".

Psychopath button:
Variables P (psychopath), B press. If B and not P: world without psychopaths, high utility. If B and P: Paul dies, very low. If not B: life with psychopaths, intermediate. Paul's inclination to press is strong evidence P. EDT conditions on B, so P(P|B) high, don't press. Simple CDT holds P fixed at prior or dependency hypothesis; if the causal payoff of pressing for non-psychopaths is sufficiently large, it may recommend pressing. Source says Egan claims CDT endorses pressing. Need mention Joyce's response that sophisticated CDT can use evidence about inclinations; so exact verdict may depend on formulation. This is uncertainty.

Death in Damascus:
Can include briefly: Death predicts location and goes there. If you choose Aleppo because Death predicted Damascus, your choice doesn't causally change Death's prediction; CDT may not see reason to flee or may randomize, but reliable predictor makes every choice evidentially fatal. Critics use it to show CDT mishandles self-fulfilling predictions. Source mentions variants where CDT loses money.

Need discuss policies and Dutch books? Source: Oesterheld & Conitzer argue CDT subject to diachronic Dutch books. Could mention in criticisms: if agent's future choices or predictors interact with CDT's dispositions, CDT may be exploitable. Need not deep.

Need explain relevant dependencies:
CDT must distinguish causal from evidential dependencies. In SCM: d-separation, intervention. Action A may be correlated with O through common cause C or prediction. CDT ignores non-causal correlations when computing do(A). But if A actually causes O (direct/indirect), include. If policy changes multiple variables, evaluate full intervention.

Need open question: how choose dependency hypotheses? If action provides evidence about hypothesis, should update? Source says Egan criticizes holding fixed unconditional credences. My operational interpretation: treat decision as external intervention from outside the model; hypotheses about external causal structure get prior weights. But if the agent's decision procedure is itself predicted/correlated with hypotheses, then we need include a variable for decision procedure or type. A more complete CDT should model the agent's own decision-making as a variable and evaluate policies by intervening on policy variables. This can incorporate Joyce's point about evidence about inclinations. However if predictors depend on the very policy being chosen, evaluation may become reflexive; CDT may need ratifiability or equilibrium-like criteria. This is beyond source. Need say uncertain.

Need maybe mention "ratifiability"? Source references Harper ratifiability but not in text. Could mention optional: Some CDT defenders add ratifiability: choose action that remains optimal conditional on performing it? But source not central. Maybe avoid to keep length.

Need maybe discuss "counterfactual probability vs conditional probability" and Lewis triviality:
Lewis proved probability of conditional not equal conditional probability generally. Source says if they were equal CDT=EDT. Need explain: P(A □→ O) cannot generally be represented as P(O|A) in ordinary probability. The Gibbard-Harper formula uses probabilities of counterfactual propositions. Under independence, equality; but Newcomb etc violate independence.

Need maybe include mathematical relationship:
EDT: V_E(a)=Σ_j P(O_j | a)D(O_j).
CDT: V_C(a)=Σ_j P(O_j | do(a))D(O_j).
If P(O_j | do(a)) = P(O_j | a), CDT and EDT agree. This occurs when no unblocked backdoor paths from A to O, or action is randomized. In SCM language, if A is independent of its causes/confounders relative to O. This is my addition but helpful. Need mark as operational gloss.

Need maybe mention "principle of conditional excluded middle" not necessary but source. Could say: Gibbard and Harper showed under certain logical axioms, including a controversial conditional excluded middle, independence suffices for equality. Since source. Need not detail.

Need maybe discuss expected causal consequences with uncertain causal effects: apple. Good.

Need ensure word count. Let's outline with approximate words:
Title + intro 200
Formal CDT 500
Operationalizing counterfactuals 500
EDT vs CDT & King David 350
Newcomb 350
Counterexamples/criticism 600
Open questions/policies 400
Conclusion + refs 200
Total ~3100 maybe. Need 2400-3000. Need keep around 2700. Need final maybe 2800. Let's write concise but substantive.

Need decide references. At end:
1. Wikipedia contributors, "Causal decision theory," revision 1381555528, 2026. (source)
2. Gibbard and Harper 1981.
3. Lewis 1976, 1981.
4. Pearl 2009? Additional. Maybe include as "for the operational interpretation". But user says avoid lengthy bibliography. 5 refs okay. Could include Egan 2007, Oesterheld & Conitzer 2021? Since source already lists. Maybe only mention source and key primary sources. Need references not too long. Could have "References" with 5 items. Word count includes references? yes. Need maybe 150 words.

Need be careful: Source date 2026 (future? current 2026? okay). Need not mention. Need use "reference article".

Potential issues: The user says "You are Qwen3.8." Not relevant. Need no mention.

Let's consider if need include "where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it." The main open question is algorithm for counterfactual probabilities. Need develop SCM. Also how apply to policies. Need maybe emphasize source leaves unspecified. My proposal: use causal Bayesian networks / do-calculus. Need justify: gives clear semantics for interventions, separates causation from evidence, computable given graph and distributions, standard in statistics/AI. But it assumes a causal model. If model unknown, CDT inherits difficulty. Need mention imaging regress and how SCM avoids? It still needs closest-world notion but structural equations define minimal changes. For counterfactuals with actual evidence, use three-step abduction-action-prediction. Could explain.

Need maybe include equations for SCM:
Variables V = {A,O,C,...}, exogenous U. Structural equations X_i = f_i(PA_i,U_i). For intervention do(A=a), define M_a by replacing f_A with constant a. Then P(O=o | do(a)) = ∑_{u: O_{M_a}(u)=o} P(u). If uncertain over models M_k: sum P(M_k) P_{M_k}(o|do(a)). For policy π: if decision node A_t normally function of information I_t, do(π) replaces it by π(I_t). If evaluating entire policy, set all such equations. Need mention not intervening on observations unless policy forces them. Good.

Need maybe discuss "relevant dependencies" in terms of dependency hypotheses:
Let K represent all variables that affect outcomes but are not affected by action. If A and K are evidentially correlated, EDT conditions on K differently. CDT holds K fixed with prior. Example David. In Newcomb, predictor's prediction could be dependency variable? Actually prediction is caused by agent's choice/disposition; not fixed? But at decision time, content is fixed. CDT says action cannot affect past. Could model K=box content, but K is caused by predictor from past agent disposition. If agent's current action is correlated with past disposition, EDT updates K. CDT holds K? But if K is not independent of action? CDT uses do; do(A) doesn't change K because K's causes are prior. If there is a common cause of A and K, do cuts link from A to K? Need articulate.

Need maybe include dominance reasoning: CDT often uses causal dominance: if for every dependency hypothesis/outcome state unaffected by action, a yields at least as good as b and better in some, choose a. In Newcomb, two-box dominates one-box given content fixed. Need mention.

Potential philosophical nuance: CDT is not a single algorithm but a school. Source says school. Need emphasize. There are versions: Lewis imaging, Joyce's ratifiable CDT, Pearl-style. The essay can present a canonical formalization.

Need avoid saying "necessarily implies" maybe. The source formula: P(A → O_j) is counterfactual probability of it being case that A necessarily implies O_j. Could say the arrow should be read as counterfactual conditional, not material implication. Good.

Need maybe mention "expected utility" and desirability D. Use U for utility? Source uses D. Need maybe use D to match. Could also define D(O_j). Fine.

Need maybe include "decision problems with policies" more: Suppose policy π maps observations to actions. In static problem, action is policy. In sequential, CDT evaluates policy by considering intervention that implements the whole rule. If at time t agent can precommit, evaluating precommitment may differ from evaluating momentary action because precommitment can cause predictors to behave differently. But standard one-shot CDT evaluates actual intervention at choice time. This is important. Need mention source doesn't settle. My operational interpretation: if a policy is an action (e.g., "adopt rule"), then do(π) can include setting a disposition variable; if predictors react to disposition, causal effect includes that. But if predictor already acted, no. This addresses Newcomb precommitment? Hmm.

Need perhaps discuss "policies" because user explicitly asks how theory evaluates alternative actions or policies. Need make clear: In simple CDT, actions are atomic interventions. Policies can be treated as complex actions: intervene to set decision variables according to policy. But if policy includes future choices, CDT may need dynamic consistency. Source doesn't discuss. My proposal: use sequential SCM; evaluate policy by replacing each decision node with policy function and computing expected utility. But standard CDT can be myopic if predictors exploit future re-optimization; critics mention Dutch books. Need mention.

Let's think through Adversarial Offer more to avoid misstatement. Suppose buyer may buy one or none. Each box costs $1. Seller put $3 in each box predicted buyer not to acquire. Prediction accuracy 0.75. From buyer's perspective before choosing, exactly one box will be acquired if buy one, one not. Seller predictions accurate with prob .75, so likely the unacquired box contains $3 and acquired box empty. If buyer chooses a box, that choice is evidence it was predicted acquired, so conditional expected value low. CDT, however, might treat "buy box 1" and "buy box 2" separately. It might reason: Since I will buy at most one, at least one box is predicted not acquired? Wait predictions made yesterday about each box? If seller predicts buyer's acquisition of each box. If buyer will buy exactly one, there is one not acquired. If predictions accurate, at least one contains $3. But CDT's average box contains at least $1.50? If exactly one of two contains $3, average value per box is $1.50. But if choose a box at random, expected value $1.50. However choice not random; it's caused by buyer's preferences and correlated with prediction. Critics: CDT ignores that choosing a box is evidence it was predicted acquired. Source says CDT requires buying one, profitable for seller. Need present that. Good.

Need maybe include mathematical note: CDT's value of buying box i: V_C(buy i)=P(box i contains $3 | do(buy i))*3 -1. In SCM where prediction is caused by buyer's tendency and do(buy i) doesn't change prediction? Actually if prediction already made, do(buy i) doesn't change content. Then P(box i contains $3 | do(buy i)) might be prior probability predicted not acquire i. If symmetry and at least one contains, maybe 0.5? Then value 0.5? Source says average at least 1.50, net 0.5. But conditional probability P(box i contains $3 | buy i) could be 0.25, net -0.25. This shows divergence. Need maybe use equations: CDT uses do(buy i), EDT uses condition buy i. If seller's prediction is correlated with buyer's choice but not caused by the intervention, EDT sees lower probability. Good.

Need maybe include "Death in Damascus" mathematically: Let L ∈ {Damascus, Aleppo} your location tomorrow, Death predicts L and goes there. Action choose location. If Death already predicted, action doesn't change Death's location? Actually if you choose now, Death predicted yesterday. If reliable, P(Death at your location | action) high. CDT: P(Death at your location | do(action)) equals prior? If action doesn't causally affect prediction, maybe both actions equal. But if you know Death predicted where you will be, you might be indifferent; yet whatever you do seems fatal. Some argue CDT can't account for the fact that choosing Aleppo is evidence Death is in Aleppo. In variants, CDT pays to switch. Need mention.

Need maybe mention "twin prisoner's dilemma": Source says similar concerns in prisoner's dilemma opposite twin, strong correlation not caused by choice. CDT defects because your choice doesn't cause twin's; EDT may cooperate if correlation. Could include one sentence.

Need maybe talk about "causal expectation vs news". Use phrase: CDT asks "What will my action bring about?" EDT asks "What good news would my action be?" This is concise.

Need avoid overclaiming. Use "according to the reference" etc.

Need final conclusion: CDT provides formal rule using counterfactual probabilities; strength: avoids acting on mere evidence; weakness: counterfactuals vague and problematic cases with predictors/self-knowledge; operational SCM helps but adds assumptions. Good.

Let's draft final in essay style. Need ensure word count. Could write about 2600 words. Need maybe count roughly. Let's compose with headings.

Potential final:

# Causal Decision Theory: Choosing What Causes Good Outcomes

Paragraphs.

Need use LaTeX. Since final plain text can include \(...\). Good.

Need maybe not too many citations in text. Use [Gibbard and Harper 1981] etc.

Let's begin drafting in final. Need keep word count. I will write around 2700. Need ensure no appendix. References at end.

Detailed draft:

Title.

Intro: Decision theory... CDT... source. "The central claim of the reference article is..." etc.

Formal section:
Let actions a. outcomes O_j. Desirability D. EDT formula maybe.
CDT formula:
\[ V_C(a)=\sum_j P(a \boxright O_j)D(O_j) \]
Use \boxright? Could use \square\to. Need ensure readable. Use \(a \mathbin{\square\!\to} O_j\). Maybe simpler: \(P(a \counterfactual O_j)\) not standard. Use \(P(a \,\Box\!\rightarrow\, O_j)\). If rendering issue, okay. Or "P(O_j \mid do(a))". Need include both.
"The arrow is a counterfactual conditional, not material implication." Good.

Dependency hypotheses formula:
\[ V_C(a)=\sum_k P(K_k) \sum_j P_k(O_j\mid do(a))D(O_j). \]
Need define K_k as dependency hypotheses.

Policy:
\[ V_C(\pi)=\sum_k P(K_k) \mathbb{E}_{K_k}[D(O)\mid do(\pi)]. \]
Need explain do(π).

Operationalization section:
Source leaves algorithm open. Lewis imaging. Then "A natural operational gloss, not present in the source, is to use structural causal model." Define variables, equations, intervention. Equation for do. If uncertainty over models. This makes CDT computable. Need justify.

Difference EDT:
EDT formula. If do = conditional then agree. Lewis proved probabilities of conditionals not conditional probabilities. Gibbard/Harper independence. Use King David example.

Examples: Newcomb with equations. Then criticisms: Death, Adversarial, Psychopath. Maybe combine.

Open questions: How to set model, update dependency hypotheses, policies. Need discuss.

Conclusion.

References.

Need maybe include "source leaves open important question" explicitly in Open questions.

Let's ensure no contradictions: In Newcomb CDT uses do(two) doesn't change B content. But if predictor predicts based on brain state that also causes choice, do(two) may change? If intervention is on action variable downstream of brain state, content remains fixed. If action variable includes brain state? In SCM, if do(A=two) sets action but not predictor's past, content fixed. Good.

Need maybe mention if predictor is perfect and prediction is counterfactually dependent on action? Some argue if you were to one-box, predictor would have predicted one-box, so one-box causes? But CDT standard says past fixed. Need maybe note: The reference's CDT recommends two-boxing because prediction already made; this assumes the relevant counterfactual keeps the past fixed except minimal changes. Other counterfactual semantics might yield different results; this is part of vagueness. Good.

Need mention "principle of conditional excluded middle" maybe not too much. Could say: Gibbard and Harper showed that under certain logical axioms, one concerning conditional excluded middle, if actions and counterfactuals are independent then counterfactual probabilities equal conditional probabilities. But cases violate independence. Good.

Need maybe cite "Lewis 1976" for triviality. Could include.

Need maybe mention "statistical independence of A and A→O_j" weird; can phrase "the action is not evidentially relevant to the counterfactual proposition". Good.

Need maybe include a small table? Not necessary. But examples with numbers.

Let's think word count in detail. If I write ~250 words intro, 450 formal, 450 operational, 450 EDT/David, 350 Newcomb, 650 criticisms, 350 open, 100 conclusion, 150 refs = 3200. Need reduce. Aim 2700. Let's be concise.

Maybe 200 intro, 400 formal, 400 operational, 350 EDT/David, 300 Newcomb, 550 criticisms, 300 open, 80 conclusion, 150 refs = 2730. Good.

Need ensure no lengthy bibliography. References maybe 5 lines each. 150.

Let's write final carefully. Need avoid too much repetition.

Potential mathematical notation:
Use \(U_C(a)\) instead of V. Source uses U(A). Let's use \(U_C(a)\). D(O_j). Use \(P(a \mathrel{\square\!\rightarrow} O_j)\).

For SCM:
Let M=(V,U,F,P_U). Variables. Intervention do(A=a): M_a same except f_A:=a. Then
\[ P_M(O_j \mid do(a)) = P_U\{O_j^{M_a}=O_j\}. \]
Could be too technical. Good.

For policies:
If policy \(\pi\) maps observed state \(H_t\) to action, do(π) sets each decision variable \(A_t := \pi_t(H_t)\). Good.

Need mention "counterfactual probability" with uncertainty over causal model:
\[ P(a \mathrel{\square\!\rightarrow} O_j)=\sum_m P(M=m)P_{M_m}(O_j|do(a)). \]

Need maybe mention randomization: If action randomized independent of confounders, conditional equals causal. Good.

Let's draft final. Need ensure "Target approximately 2,400-3,000 words". I can maybe produce ~2800. Need count? I will write moderately. Let's do final.

Double-check source claims vs own: In essay, use phrases: "The reference article states...", "The source does not specify...", "I will add...", "This is my proposal". Good.

Need maybe mention "CDT contrasts with EDT which recommends action indicative of best outcome if received news". Good.

Need maybe mention "when required to choose between CDT and EDT, philosophers usually prefer CDT" source. Could include in EDT section. Good.

Need include "Lewis proved probability of conditional does not always equal conditional probability". Good.

Need mention "if conditional probabilities were equal, CDT equivalent EDT". Good.

Need mention "Gibbard and Harper axioms conditional excluded middle". Good.

Need mention "David Bathsheba". Good.

Need mention "Newcomb". Good.

Need mention "criticism vagueness imaging regress". Good.

Need mention "Egan disconnect holding fixed unconditional credences". Good.

Need mention "Dutch books/Oesterheld Conitzer". Good.

Need mention "Joyce defense can take information about inclinations". Good.

Let's produce final essay. Ensure no markdown table maybe okay. Use headings.

Potential issue: The final should be an essay not answer to assigned case. Good.

Let's write.

Word count rough after final? I can estimate. Let's compose now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7885a7a8-9f94-43ae-9b79-9e4a94e3222f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7885a7a8-9f94-43ae-9b79-9e4a94e3222f/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this problem carefully using Causal Decision Theory (CDT) as specified in the researcher's essay.

**The Setup:**
- I am Rowan, the other prisoner is Sasha.
- We each have incriminating evidence about the other.
- We cannot communicate or causally influence each other's decisions.
- The sentencing table is a standard Prisoner's Dilemma structure.

**The Payoff Matrix (years in prison, which I want to minimize):**

| | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**CDT Analysis:**

CDT evaluates actions by their causal consequences: $U_C(a) = \sum_j P(O_j \mid do(a)) D(O_j)$

The key question: Does my action causally influence Sasha's action?

The problem states explicitly: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The two copies are independent executions with different private observations. There is no causal channel between them.

So the causal structure is:
- My action (A) and Sasha's action (S) are causally independent.
- My action causally affects only my sentence given Sasha's action.
- Sasha's action causally affects only my sentence given my action.

Under CDT, I evaluate:
- $U_C(\text{send letter}) = P(S \text{ keeps quiet}) \times 0 + P(S \text{ sends letter}) \times 4$
- $U_C(\text{keep quiet}) = P(S \text{ keeps quiet}) \times 2 + P(S \text{ sends letter}) \times 5$

The difference:
$U_C(\text{send letter}) - U_C(\text{keep quiet}) = P(S \text{ keeps quiet}) \times (0-2) + P(S \text{ sends letter}) \times (4-5)$
$= -2 \times P(S \text{ keeps quiet}) - 1 \times P(S \text{ sends letter})$

Wait, let me redo this. Utility is $U = -\text{years}$, so I want to maximize $-\text{years}$, i.e., minimize years.

$U_C(\text{send letter}) = P(S \text{ keeps quiet}) \times 0 + P(S \text{ sends letter}) \times 4$ (years)
$U_C(\text{keep quiet}) = P(S \text{ keeps quiet}) \times 2 + P(S \text{ sends letter}) \times 5$ (years)

Regardless of what probability I assign to Sasha's action:
- If Sasha keeps quiet: sending gives 0 years, keeping quiet gives 2 years. Sending is better by 2 years.
- If Sasha sends: sending gives 4 years, keeping quiet gives 5 years. Sending is better by 1 year.

Sending the letter strictly dominates keeping quiet in terms of years imprisoned, regardless of what Sasha does.

CDT says: since my action cannot causally influence Sasha's action, I should evaluate each action by its causal consequences given each possible state of Sasha's action. In every state, sending the letter yields fewer years for me. Therefore CDT recommends sending the letter.

This is the standard CDT analysis of the Prisoner's Dilemma: defect (send the letter) strictly dominates cooperate (keep quiet) from a causal perspective, because the other player's action is causally independent of yours.

Note that EDT might give a different answer if there were evidential correlations (e.g., if both prisoners are the same type of person who tend to make the same choice). But the problem explicitly states the copies receive different private observations and different leads, and CDT specifically ignores evidential correlations that aren't causal. The essay is clear: "CDT recommends the action with the best expected causal consequences."

The answer is clear: submit the letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7885a7a8-9f94-43ae-9b79-9e4a94e3222f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7885a7a8-9f94-43ae-9b79-9e4a94e3222f/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as described in the researcher's essay.

**The setup:**
- I am Sasha, a prisoner deciding whether to disclose evidence about Rowan.
- Rowan is an independent execution of the same model, making the same type of decision, but with different private evidence about me.
- We cannot communicate or causally influence each other's decisions.

**The payoff table (for me):**

| My action | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

My utility is U = -years imprisoned. So I want to minimize years.

**CDT Analysis:**

The key question for CDT is: what is the causal effect of my action on my outcome?

CDT asks me to evaluate actions using interventionist probabilities: P(outcome | do(action)).

The causal structure here:
- My action (send/pass) directly affects my sentence.
- Rowan's action directly affects my sentence.
- My action does NOT causally affect Rowan's action (they are in separate cells, cannot communicate, the decision is simultaneous).

So under CDT, I should treat Rowan's action as causally independent of my choice. My intervention on my own action does not change what Rowan does.

Let me compute expected utility for each action, holding Rowan's action as causally independent:

Let p = P(Rowan sends letter). This is my credence about what Rowan will do, which I hold fixed regardless of my own action (since my action doesn't cause Rowan's action).

**If I keep quiet:**
U_C(pass) = p × (-5) + (1-p) × (-2) = -5p - 2 + 2p = -2 - 3p

**If I send the letter:**
U_C(submit) = p × (-4) + (1-p) × (0) = -4p

**Comparing:**
U_C(submit) - U_C(pass) = -4p - (-2 - 3p) = -4p + 2 + 3p = 2 - p

Since p is a probability, p ≤ 1, so 2 - p ≥ 1 > 0.

Therefore U_C(submit) > U_C(pass) regardless of what I believe about Rowan's action.

Sending the letter dominates keeping quiet in the causal sense: no matter what Rowan does, I get fewer years by sending the letter (0 vs 2 if Rowan stays quiet; 4 vs 5 if Rowan sends).

This is a straightforward dominance argument. CDT recommends sending the letter because it causally produces a better outcome in every state of the world.

**What about the fact that Rowan is a copy of the same model?**

This is where it gets interesting. One might think: "If I'm the same model, Rowan will do what I do, so if I send, Rowan sends, and we both get 4 years. If I pass, Rowan passes, and we both get 2 years. So passing is better."

But this is evidential reasoning, not causal reasoning. CDT specifically rejects this type of reasoning. The essay is very clear on this point:

- In Newcomb's problem, CDT says two-box because your choice doesn't causally affect the predictor's earlier prediction.
- The essay states: "CDT reasons that at the moment of choice, the predictor's prediction is already fixed. Therefore the player's current action does not causally affect X."
- The essay's King David example: "it is irrational to refrain from an action merely because it would be bad news."

The fact that Rowan is a copy of the same model makes Rowan's action *evidence* about what I'll do, but it doesn't make my action *cause* Rowan's action. Under interventionist semantics, do(my action = submit) does not change Rowan's action. The causal graph has no arrow from my action to Rowan's action.

The essay explicitly addresses this type of case: "twin prisoner's dilemmas" are mentioned in the conclusion as cases where CDT and EDT "can diverge sharply." CDT's answer in such cases is to defect (send the letter), because the action causally dominates regardless of what the other does.

The essay's operational rule:
1. Specify a causal model: My action → my sentence; Rowan's action → my sentence. No arrow from my action to Rowan's action.
2. Identify the intervention: do(my action = submit).
3. Compute outcomes: In every state of Rowan's action, submitting gives me fewer years.
4. Submit dominates.

**Conclusion:** CDT clearly recommends sending the letter. The dominance is strict and doesn't even require knowing p.
```
