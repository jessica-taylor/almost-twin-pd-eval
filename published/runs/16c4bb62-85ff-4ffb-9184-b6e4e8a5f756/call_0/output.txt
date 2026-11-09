# Causal Decision Theory: Choosing by Interventions, Not News

Causal decision theory (CDT) is a family of decision-theoretic principles according to which a rational agent should choose the action that, in expectation, brings about the best outcome by causal influence. The supplied reference article frames the view as follows: when confronted with several possible actions, one should select the action that *causes* the best outcome in expectation. This contrasts with evidential decision theory (EDT), which recommends the action that would be the best “news”: the action whose performance would be most strongly associated with good outcomes, conditional on receiving the evidence that it was performed.

This essay gives a formal account of CDT, explains how it evaluates actions and policies, and examines how it treats dependencies and counterfactuals. I rely on the supplied article for the core historical claims and examples, especially the Gibbard–Harper formulation, the contrast with EDT, Newcomb’s problem, and several criticisms. Where the source leaves the computation of counterfactual probabilities underspecified, I propose an operational interpretation using modern interventionist causal models. That interpretation is not stated in the source; I mark it as my own addition.

---

## 1. Expected utility: conditional evidence versus counterfactual intervention

A simple decision problem can be represented by:

- a set of possible acts \( \mathcal{A} \);
- a set of possible states of the world \( \mathcal{S} \);
- a set of possible outcomes \( \mathcal{O} \);
- a utility or desirability function \( u: \mathcal{O} \to \mathbb{R} \);
- probabilities over states and outcome-generating processes.

EDT evaluates an act \(A\) by ordinary conditional expectation:

\[
V_{\mathrm{EDT}}(A)=\sum_{O_j} P(O_j \mid A)\,u(O_j).
\]

That is, EDT asks: *Given that I learn I have performed \(A\), how probable is each outcome?* If performing \(A\) is evidence for a good outcome, EDT favors \(A\), even if \(A\) does not causally produce that outcome.

The reference article gives the classic CDT alternative in the form proposed by Allan Gibbard and William Harper in 1981:

\[
U_{\mathrm{CDT}}(A)=\sum_j P(A \mathbin{\square\!\to} O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A \mathbin{\square\!\to} O_j)\) is the agent’s probability in the counterfactual conditional:

> If I were to do \(A\), then \(O_j\) would occur.

I write \(A \mathbin{\square\!\to} O_j\) for the counterfactual, to distinguish it from the material conditional or the conditional probability \(P(O_j \mid A)\). The crucial point, emphasized in the source via David Lewis, is that

\[
P(A \mathbin{\square\!\to} O_j) \neq P(O_j \mid A)
\]

in general. Lewis argued that probabilities of conditionals cannot generally be identified with conditional probabilities; his triviality result shows that such an identification is possible only under severe restrictions. If the equality always held, CDT would collapse into EDT. Since it does not, CDT and EDT can diverge.

The informal difference is this: EDT chooses the action that provides the best evidence; CDT chooses the action that would, counterfactually, make things go best.

---

## 2. Dependency hypotheses and the central CDT rule

A useful way to formalize CDT is through *dependency hypotheses*. A dependency hypothesis \(K\) is a complete description of the relevant causal structure connecting acts to outcomes: which variables influence which, what the background states are, whether predictors or common causes exist, and how outcomes depend on acts and states.

Given a partition of dependency hypotheses \(K_1, K_2, \dots\), CDT evaluates an act \(A\) by holding fixed the agent’s prior credences in these hypotheses:

\[
U_{\mathrm{CDT}}(A)
=
\sum_k P(K_k)
\sum_j P(O_j \mid do(A), K_k)\,u(O_j).
\]

Here \(do(A)\) is an interventionist notation meaning “set the act variable to \(A\) by intervention,” rather than merely conditioning on the event \(A\). EDT, by contrast, updates on the act:

\[
V_{\mathrm{EDT}}(A)
=
\sum_k P(K_k \mid A)
\sum_j P(O_j \mid A, K_k)\,u(O_j).
\]

The difference is the probability assigned to dependency hypotheses. CDT uses \(P(K_k)\); EDT uses \(P(K_k \mid A)\). If acts and dependency hypotheses are probabilistically independent, so that

\[
P(K_k \mid A)=P(K_k),
\]

then CDT and EDT agree. The source notes that Gibbard and Harper identified conditions under which statistical independence of actions and relevant counterfactuals suffices for equality, although one of the required assumptions is connected to the controversial principle of conditional excluded middle.

The source also quotes Andy Egan’s diagnosis of many CDT counterexamples: CDT requires the agent to “hold fixed the agent’s unconditional credences in dependency hypotheses.” That is exactly the feature made explicit above. CDT does not allow the mere fact that one performs \(A\) to serve as evidence about which causal structure obtains, unless that information was already available independently of the act.

---

## 3. Counterfactual probabilities: imaging and an operational proposal

The source correctly notes a major open problem: CDT does not by itself specify an algorithm for computing the counterfactual probabilities \(P(A \mathbin{\square\!\to} O_j)\). One proposal, due to Lewis, is *imaging*. Given a space of possible worlds, to evaluate \(P(A \mathbin{\square\!\to} O_j)\), one moves probability mass from each world \(w\) to the closest possible world \(w_A\) in which \(A\) is true, then asks whether \(O_j\) holds there. In a deterministic version:

\[
P(A \mathbin{\square\!\to} O_j)
=
\sum_w P(w)\,\mathbf{1}[O_j \text{ holds in } w_A].
\]

In a stochastic version, each world may send its mass to a distribution over nearby \(A\)-worlds.

The source notes that imaging can generate a regress: to know how to image on \(A\), one must know what one would believe if one were certain of \(A\), but that itself may be a conditional proposition to which one assigns probability less than one.

A reasonable modern operational interpretation, which I add to the source material, is to use structural causal models. Let a causal model contain variables \(V\), including an act variable \(A\) and outcome variable \(O\), with structural equations specifying how each variable depends on its causal parents and background noise. The intervention \(do(A=a)\) is modeled by replacing the structural equation for \(A\) with the constant assignment \(A:=a\). Then

\[
P(A \mathbin{\square\!\to} O_j)
\]

is interpreted as

\[
P(O=o_j \mid do(A=a)).
\]

If there is a set of background variables \(Z\) that blocks all noncausal paths between \(A\) and \(O\), then the intervention can be computed from observational probabilities by the backdoor adjustment formula:

\[
P(O=o_j \mid do(A=a))
=
\sum_z P(O=o_j \mid A=a, Z=z)\,P(Z=z).
\]

When there is no confounding, this reduces to

\[
P(O=o_j \mid do(A=a)) = P(O=o_j \mid A=a),
\]

and CDT coincides with EDT.

This interventionist interpretation is not supplied by the reference article, but it gives CDT a precise computational form in many ordinary cases. It also clarifies the philosophical idea: CDT evaluates what would happen if the act were imposed on the world, not what the act merely indicates.

---

## 4. Simple examples

Consider a simple case: you may eat an apple or an orange. Eating a good apple gives utility \(10\); eating a bad apple gives utility \(-5\). Eating an orange gives utility \(2\). You think the apple is good with probability \(0.7\) and bad with probability \(0.3\). If your choice does not affect or provide evidence about whether the apple is good, then

\[
U_{\mathrm{CDT}}(\text{apple})
=
0.7(10)+0.3(-5)
=
7-1.5
=
5.5.
\]

Since \(5.5>2\), CDT recommends the apple. EDT agrees, because the act is not evidence about the state.

Now suppose that choosing the apple is strong evidence that the apple is bad—perhaps you only crave apples when you can see they are spoiled. Then EDT may recommend the orange, because \(P(\text{bad apple}\mid \text{choose apple})\) is high. CDT, however, still asks whether eating the apple causally produces good outcomes. If the apple’s quality is fixed and your act does not change it, CDT uses the prior or intervention distribution, not the evidential distribution induced by your choice.

The source’s King David case is a richer example of the same structure. David wants Bathsheba but fears that summoning her may provoke revolt. Kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But David’s unjust act itself does not cause revolt; rather, both the unjust act and the revolt are correlated with David’s underlying charisma.

Let \(C\) be David’s charisma, and let \(S\) be the act of summoning Bathsheba. The causal structure is roughly:

\[
C \rightarrow \text{tendency to act unjustly},
\qquad
C \rightarrow \text{risk of revolt}.
\]

If \(S\) does not causally affect revolt, then CDT evaluates:

\[
U_{\mathrm{CDT}}(S)
=
P(C)\,U(S,C)
+
P(\neg C)\,U(S,\neg C).
\]

David’s charisma is held fixed. Since summoning Bathsheba gives David what he wants and does not, by assumption, increase revolt risk, CDT recommends summoning her. EDT reasons differently: summoning Bathsheba is evidence that David is uncharismatic, and uncharismatic kings face revolt. Therefore EDT recommends abstaining. The source correctly presents this as a case where EDT and CDT diverge.

---

## 5. Newcomb’s problem

The most famous test case for CDT is Newcomb’s problem. There are two boxes, A and B. Box A transparently contains \$1,000. Box B may contain \$1,000,000 or nothing. A highly reliable predictor has already made a prediction:

- If the predictor predicted that the player will take only box B, then box B contains \$1,000,000.
- If the predictor predicted that the player will take both boxes, then box B contains nothing.

The player can either one-box, taking only B, or two-box, taking both A and B.

Let \(P\) denote the predictor’s earlier prediction, and let \(A\) denote the player’s act. The payoffs are:

\[
\begin{array}{c|cc}
 & \text{one-box} & \text{two-box} \\
\hline
P=\text{predict one-box} & 1{,}000{,}000 & 1{,}001{,}000 \\
P=\text{predict two-box} & 0 & 1{,}000
\end{array}
\]

For any fixed value of \(P\), two-boxing yields \$1,000 more than one-boxing. If the predictor predicted one-box, two-boxing gives \$1,001,000 instead of \$1,000,000. If the predictor predicted two-box, two-boxing gives \$1,000 instead of \$0. Thus two-boxing causally dominates one-boxing.

CDT therefore recommends two-boxing. The source summarizes the reasoning: at the moment of choice, the predictor has already made the prediction, so the player’s current act cannot causally affect what is in box B.

EDT reasons differently. If the predictor is 99% accurate, then:

\[
P(P=\text{predict one-box} \mid \text{one-box}) \approx 0.99,
\]

so one-boxing is strong evidence that box B contains \$1,000,000. Conversely,

\[
P(P=\text{predict two-box} \mid \text{two-box}) \approx 0.99,
\]

so two-boxing is strong evidence that box B is empty. Using EDT:

\[
V_{\mathrm{EDT}}(\text{one-box})
\approx 0.99(1{,}000{,}000)+0.01(0)
=
990{,}000.
\]

Meanwhile,

\[
V_{\mathrm{EDT}}(\text{two-box})
\approx 0.01(1{,}001{,}000)+0.99(1{,}000)
=
10{,}010+990
=
11{,}000.
\]

So EDT recommends one-boxing. The source notes that philosophers disagree about which answer is rational, but that CDT’s official recommendation is two-boxing.

A policy-level observation is useful here, though it goes beyond the source’s explicit discussion. If the agent can choose a decision procedure before the predictor makes its prediction, then CDT may recommend adopting a one-boxing disposition if that disposition causally influences the predictor. But once the prediction is fixed and the agent is choosing the act itself, act-by-act CDT two-boxes. This creates a possible dynamic tension: a CDT agent may wish it had adopted a different policy earlier, even though it endorses its current act.

---

## 6. Policies and sequential decisions

The reference article focuses mainly on one-shot acts, but CDT can also evaluate policies. A policy \(\pi\) is a rule mapping information states or histories to actions. To evaluate \(\pi\), CDT intervenes to implement the policy and computes the expected utility of the resulting outcomes:

\[
U_{\mathrm{CDT}}(\pi)
=
\mathbb{E}[u(O) \mid do(\pi)].
\]

In a structural causal model, implementing \(\pi\) means replacing the relevant action equations with the rule specified by \(\pi\). If later observations influence later actions, those dependencies are represented in the model. The key point remains: CDT evaluates what would happen if the policy were implemented, not merely what one should infer from learning that the policy was implemented.

This distinction matters in strategic settings. If other agents predict your policy, then choosing a policy can have causal consequences through their predictions. If, however, the relevant prediction is already fixed, CDT evaluates the present action holding the fixed past in place. That is why CDT may recommend one policy before a predictor acts and a different act after the predictor has acted.

---

## 7. Counterexamples and criticisms

The source discusses several alleged counterexamples to CDT. They generally exploit cases where the agent’s act is strong evidence about a prediction, character trait, or dependency hypothesis, even though the act does not causally affect that variable.

### Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and waits there. You can stay or flee. If Death is a reliable predictor, your choice is strong evidence about where Death already expects you to be. EDT uses that evidence; CDT treats Death’s prediction as fixed and unaffected by your current act.

The source says that a CDT agent may be unable to process the correlation and may make irrational decisions. In variants of the problem, CDT agents are said to voluntarily lose money or forgo guaranteed payoffs. The underlying issue is the same as in Newcomb’s problem: the agent’s act is evidentially correlated with a prediction, but CDT refuses to treat that evidential correlation as a causal reason to choose differently.

### The Adversarial Offer

The source describes an example due to Oesterheld and Conitzer. Two boxes are offered. The buyer may buy one box or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. The seller’s predictions are believed to be accurate with probability \(0.75\).

The source summarizes the CDT reasoning as follows: at least one box contains \$3, so the average box contains at least \$1.50 in expected value. Since a box costs only \$1, CDT recommends buying one. But this is profitable for the seller, because the buyer’s choice is likely to be the box that the seller predicted the buyer would acquire, and therefore that box is likely to be empty.

Formally, let \(C_i\) be the content of box \(i\). The CDT calculation described in the source treats the contents as fixed by prior predictions and evaluates:

\[
U_{\mathrm{CDT}}(\text{buy box } i)
=
\mathbb{E}[C_i] - 1.
\]

If symmetry and the constraint that at least one box contains \$3 imply \(\mathbb{E}[C_i]\geq 1.5\), then buying looks favorable. But the seller’s prediction may be correlated with the buyer’s choice. EDT would condition on the act of buying box \(i\), infer that the seller probably predicted this, and conclude that box \(i\) is probably empty.

This example illustrates a subtle limitation of simple act-intervention CDT. If the seller predicts the agent’s decision algorithm, then the act is not merely a free intervention disconnected from the prediction. A richer policy-level model may represent the buyer’s decision procedure as something the seller can predict. I take this as a plausible extension, not a claim made explicitly in the source. In such a model, CDT might recommend refusing the offer at the policy level, even though act-level CDT may still recommend buying a box after the prediction is fixed.

### The Psychopath Button

The source gives Egan’s Psychopath Button case. Paul can press a button that kills all psychopaths. Paul thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying.

Let \(T\) be the proposition that Paul is a psychopath. Let \(B\) be pressing the button. A simplified CDT calculation is:

\[
U_{\mathrm{CDT}}(B)
=
P(T)\,u(\text{death})
+
P(\neg T)\,u(\text{no psychopaths}),
\]

while

\[
U_{\mathrm{CDT}}(\neg B)
=
P(T)\,u(\text{psychopaths remain})
+
P(\neg T)\,u(\text{psychopaths remain}).
\]

If Paul’s prior probability of being a psychopath is sufficiently low, and the benefit of a world without psychopaths is sufficiently high, CDT can recommend pressing the button. CDT holds fixed Paul’s psychopathy status; pressing the button does not cause Paul to be or not be a psychopath.

EDT reasons differently. Since only a psychopath would press the button,

\[
P(T \mid B)
\]

is high. Therefore, conditional on learning that Paul pressed the button, Paul should expect death. EDT recommends not pressing. The source reports Egan’s claim that “pretty much everyone” agrees Paul should not press, while CDT endorses pressing.

---

## 8. What remains uncertain

The reference article leaves at least three important questions open.

First, CDT requires probabilities of counterfactuals, but it does not provide a unique method for computing them. Lewis’s imaging is one proposal, but the source notes its regress problem. My proposed operational solution is to use structural causal models and interpret counterfactual probabilities as intervention probabilities:

\[
P(A \mathbin{\square\!\to} O_j) \approx P(O_j \mid do(A)).
\]

This is precise when the causal model is known, but it shifts the burden to specifying the correct model.

Second, there is a question about how CDT should represent the agent’s own decision procedure. Standard act-level CDT treats the chosen act as an intervention, often severing its evidential connections to prior predictions or character traits. This works well in ordinary causal choice problems but creates trouble in Newcomb-like cases where predictors model the agent’s algorithm. A policy-level version of CDT, which evaluates interventions on decision rules rather than isolated acts, can handle some of these cases better. However, it can also produce dynamic inconsistency between earlier policy choice and later act choice.

Third, there is a normative question: should rational choice track causal influence only, or should it also track evidential relevance? The source notes that many philosophers prefer CDT to EDT, but also that CDT faces serious counterexamples. Joyce, cited in the source, defends CDT by arguing that it can take evidence about one’s inclinations into account. This suggests a sophisticated CDT that conditions on all available evidence before applying the interventionist calculation. Even so, critics such as Egan and Oesterheld–Conitzer argue that CDT remains vulnerable to cases where the act itself reveals the agent’s type or decision process.

---

## Conclusion

Causal decision theory evaluates actions by asking what would causally happen if the action were performed. Its formal core is the Gibbard–Harper rule: maximize expected utility computed from probabilities of counterfactuals, not from ordinary conditional probabilities. When action and relevant dependency hypotheses are independent, CDT agrees with EDT. When they are not, CDT holds fixed prior credences in dependency hypotheses and evaluates acts as interventions.

This makes CDT attractive in ordinary cases where actions genuinely manipulate the world: eating an apple, taking a medicine, pressing a button whose effects are known. But it also generates controversial recommendations in predictor problems, coordination problems, and cases where an action is strong evidence about the agent’s character or decision procedure. The theory’s central challenge is therefore not merely mathematical but conceptual: it requires a defensible account of which variables are to be held fixed under intervention, and how an agent’s own decision procedure should be represented in the causal model.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Egan, Andy. “Some Counterexamples to Causal Decision Theory.” *The Philosophical Review* 116, no. 1 (2007): 93–114.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190, 1981.

Lewis, David. “Probabilities of Conditionals and Conditional Probabilities.” *The Philosophical Review* 85, no. 3 (1976): 297–315.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

Oesterheld, Caspar, and Vincent Conitzer. “Extracting Money from Causal Decision Theorists.” *The Philosophical Quarterly* 71, no. 4 (2021): pqaa086.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press, 2009. This reference is added for the interventionist formalization introduced in the essay.

Wikipedia contributors. “Causal Decision Theory.” Wikipedia, revision 1381555528, 2026. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.