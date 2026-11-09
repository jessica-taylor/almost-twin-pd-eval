# Causal Decision Theory: Choosing as an Intervention

Causal decision theory (CDT) is a school of thought in decision theory which says that a rational agent should choose the action that causes the best outcome in expectation. The supplied reference article summarizes the view in this way: CDT contrasts with evidential decision theory (EDT), which recommends the action that would be the best “news” if one learned that it had been taken. CDT, by contrast, asks which action would bring about the best consequences if the agent intervened to perform it.

That distinction sounds simple, but it becomes subtle once we recognize that actions can be evidence for things they do not cause. My action may be correlated with my character, with another agent’s prediction, or with some hidden state of the world. EDT responds to those correlations by conditionalizing on the action. CDT responds by asking what would happen under an intervention that sets the action. The central formal task of CDT is therefore to represent and evaluate counterfactual or interventionist probabilities.

In this essay I will explain the formal core of CDT, compare it with EDT, and show how it evaluates actions and policies. I will also discuss the main unresolved problem emphasized by the source: CDT does not by itself specify a unique algorithm for computing the relevant counterfactual probabilities. Where the source leaves that question open, I will propose a natural operational interpretation using modern causal-modeling tools. I will mark such proposals as my own.

---

## 1. Expected utility: evidential and causal versions

Let \(\mathcal A\) be a set of possible actions, and let \(\mathcal O\) be a set of possible outcomes. The agent has a desirability function

\[
D : \mathcal O \to \mathbb R,
\]

assigning a numerical value to each outcome. In ordinary expected-utility theory, an action is evaluated by taking a probability-weighted average of the desirabilities of possible outcomes.

Evidential decision theory uses conditional probabilities:

\[
V_{\mathrm{EDT}}(a)
=
\sum_{o \in \mathcal O} P(o \mid a) D(o).
\]

Here \(P(o \mid a)\) is the agent’s conditional credence that outcome \(o\) will occur given that action \(a\) is performed. EDT treats the action as evidence. If performing \(a\) would be good news, EDT favors \(a\).

Causal decision theory replaces the conditional probability with something meant to capture causal consequence. In a 1981 paper, Allan Gibbard and William Harper gave the canonical formulation:

\[
U(a)
=
\sum_j P(a \mathbin{\Box\!\to} O_j) D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(a \mathbin{\Box\!\to} O_j)\) is the probability the agent assigns to the counterfactual claim: “If I were to do \(a\), then \(O_j\) would obtain.” The source uses \(a \to O_j\) for this counterfactual relation; I write \(\Box\!\to\) to distinguish it from a material conditional or an ordinary conditional probability.

The difference matters because, as David Lewis argued, the probability of a counterfactual or conditional need not equal the corresponding conditional probability. If we always had

\[
P(a \mathbin{\Box\!\to} O_j) = P(O_j \mid a),
\]

then CDT would collapse into EDT. Lewis showed that this equality cannot be assumed in general. Thus CDT needs probabilities that are sensitive to causal structure, not merely to evidential association.

The reference article notes that Gibbard and Harper proved a partial equivalence result: under certain axioms, one of which is connected to the controversial principle of conditional excluded middle, statistical independence between the action and the relevant counterfactuals can guarantee equality between counterfactual probabilities and conditional probabilities. In ordinary cases where the action is not correlated with hidden causes of the outcome, CDT and EDT often agree. They diverge in cases involving prediction, common causes, or self-evidence.

---

## 2. A modern operational reading: interventions

The source correctly emphasizes that CDT does not itself specify an algorithm for calculating \(P(a \mathbin{\Box\!\to} O_j)\). One historical proposal, due to Lewis, is “imaging”: to evaluate the probability of \(O\) under the counterfactual supposition \(a\), move the probability mass from each possible world \(w\) to the closest possible world \(w_a\) in which \(a\) is true. The source notes a regress problem: to know what one would believe if certain of \(a\), one may need to evaluate further conditionals.

A more contemporary operational interpretation, which I add to the source’s presentation, is to use a causal model. Let \(M\) be a structural causal model or causal Bayesian network containing variables for actions, background states, and outcomes. An action \(a\) is represented not by merely conditioning on the event \(A=a\), but by an intervention:

\[
\operatorname{do}(A=a).
\]

This intervention replaces the causal equation or incoming arrows for \(A\) with the fixed value \(a\), while leaving the rest of the causal system intact. The causal expected utility of \(a\) is then

\[
V_{\mathrm{CDT}}(a)
=
\sum_o P_{M_{\operatorname{do}(a)}}(o) D(o)
=
\mathbb E_{M_{\operatorname{do}(a)}}[D(O)].
\]

This is not explicitly in the source, but it captures the central CDT idea: evaluate what would happen if the action were imposed on the world, rather than what the action merely indicates.

The distinction can be made very clear with a simple causal graph. Suppose action \(A\) has background causes \(Z\), and outcome \(O\) depends on both \(A\) and \(Z\). EDT evaluates

\[
P(o \mid a)
=
\sum_z P(o \mid a,z) P(z \mid a).
\]

CDT, under the interventionist reading, evaluates

\[
P(o \mid \operatorname{do}(a))
=
\sum_z P(o \mid a,z) P(z),
\]

in the simple case where adjusting for the parents \(Z\) of \(A\) is sufficient. The difference is the distribution over \(Z\): EDT uses \(P(z \mid a)\), because it treats \(a\) as evidence about \(Z\); CDT uses \(P(z)\), because it holds fixed the background causes when intervening on \(A\).

This gives a useful rule of thumb:

- EDT asks: “Given that I do \(a\), what should I infer about the world?”
- CDT asks: “If I intervene to do \(a\), what will the world become?”

CDT does not ignore dependencies. It represents them causally. If \(A\) genuinely causes \(O\), the intervention changes the distribution of \(O\). If \(A\) is merely correlated with \(O\) through a common cause, the intervention on \(A\) need not change that common cause.

---

## 3. Actions, policies, and dependency hypotheses

The source mainly discusses single actions, but decision problems often involve policies. A policy is a rule mapping information or observations to actions. CDT can evaluate policies by extending the interventionist idea.

Suppose a policy \(\pi\) determines actions over time, perhaps depending on observations. Let \(M_{\operatorname{do}(\pi)}\) be the model obtained by setting the agent’s action variables according to \(\pi\). Then the causal expected utility of the policy is

\[
V_{\mathrm{CDT}}(\pi)
=
\mathbb E_{M_{\operatorname{do}(\pi)}}[D].
\]

If the policy is stochastic, the expectation includes the policy’s own randomization. This extension is my own, but it is a natural development of the CDT principle: evaluate the causal consequences of adopting the policy, not merely the evidential significance of the policy.

Another traditional way to formulate CDT uses “dependency hypotheses.” A dependency hypothesis \(K\) is a complete description of how outcomes depend causally on actions. If the agent has credences \(P(K)\) over such hypotheses, then one can write

\[
V_{\mathrm{CDT}}(a)
=
\sum_K P(K)
\sum_o P_K(o \mid \operatorname{do}(a)) D(o).
\]

The crucial point is that CDT holds fixed the agent’s prior credences in the dependency hypotheses when evaluating the action. This is the feature that Andy Egan criticizes, according to the source: CDT’s requirement to hold fixed unconditional credences in dependency hypotheses can, in some cases, produce decisions that seem irrational.

---

## 4. Examples

### 4.1 Apples and ordinary uncertainty

The source gives a simple informal example. Eating an apple causes happiness, while eating an orange causes sadness. Then CDT recommends the apple.

If there is uncertainty, the calculation becomes expected. Suppose the apple may be good or bad. Let \(G\) be the proposition that the apple is good, and \(B\) that it is bad. Let \(D(H)\) be the desirability of happiness and \(D(S)\) the desirability of sadness. If eating the apple is the action \(a\), then a simple CDT evaluation is

\[
V_{\mathrm{CDT}}(a)
=
P(G) D(H) + P(B) D(S).
\]

If eating the orange has known effects, compare its expected utility with this value. In this ordinary case, CDT and EDT usually agree, because eating the apple is not usually strong evidence for some hidden cause of happiness or sadness. The distinction between the theories becomes visible only when actions carry evidence that is not causally relevant.

### 4.2 King David and Bathsheba

The source gives an example involving King David. David wants Bathsheba but fears that summoning her may provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But the unjust act itself does not cause revolt; rather, uncharismatic kings have a disposition that both leads to unjust acts and makes revolts more likely. David does not know whether he is charismatic.

Let \(C\) be the proposition that David is charismatic, and \(U\) that he is uncharismatic. Let \(S\) be the action of summoning Bathsheba. EDT evaluates

\[
V_{\mathrm{EDT}}(S)
=
P(C \mid S) D(O_{S,C})
+
P(U \mid S) D(O_{S,U}).
\]

Since summoning Bathsheba is an unjust act, and unjust acts are evidence of uncharismatic character, \(P(U \mid S)\) may be high. EDT may therefore recommend abstaining, because the action is bad news.

CDT instead evaluates something closer to

\[
V_{\mathrm{CDT}}(S)
=
P(C) D(O_{S,C})
+
P(U) D(O_{S,U}),
\]

or, in interventionist notation,

\[
V_{\mathrm{CDT}}(S)
=
\mathbb E_{\operatorname{do}(S)}[D].
\]

David’s charisma is treated as fixed by the intervention. Summoning Bathsheba does not make David uncharismatic. If the benefit of summoning her outweighs the prior risk of revolt, CDT recommends sending for her. The source says exactly this: EDT recommends abstention, while CDT recommends summoning.

The example illustrates the core philosophical motivation for CDT. It seems odd to abstain merely because an action would reveal a bad fixed trait. If the trait cannot be changed, rational choice should focus on what the action causally produces, given the trait.

### 4.3 Newcomb’s problem

Newcomb’s problem is the most famous test case. The source describes it as follows. A predictor has predicted whether the agent will take only box B or both boxes A and B. Box A always contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The predictor is highly reliable, perhaps 99% accurate. The agent chooses after the prediction has been made.

Let \(N_1\) be the proposition that the predictor predicted one-boxing, and \(N_2\) that it predicted two-boxing. Let \(p = P(N_1)\). If the agent’s current choice cannot causally affect the predictor’s earlier prediction, CDT evaluates the options as follows:

\[
V_{\mathrm{CDT}}(\text{one-box})
=
p \cdot 1{,}000{,}000
+
(1-p) \cdot 0.
\]

\[
V_{\mathrm{CDT}}(\text{two-box})
=
p \cdot 1{,}001{,}000
+
(1-p) \cdot 1{,}000.
\]

The difference is

\[
V_{\mathrm{CDT}}(\text{two-box})
-
V_{\mathrm{CDT}}(\text{one-box})
=
1{,}000.
\]

So CDT recommends taking both boxes. This is the standard two-boxing recommendation: given that the contents of box B are already fixed, taking both boxes adds \$1,000 no matter what is in box B.

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so

\[
P(N_1 \mid \text{one-box})
\]

is high. Two-boxing is strong evidence that the predictor predicted two-boxing, so

\[
P(N_2 \mid \text{two-box})
\]

is high. Therefore EDT recommends one-boxing, because one-boxing is good news about the contents of box B.

The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but that many philosophers prefer CDT when forced to choose between CDT and EDT. Newcomb’s problem shows that CDT’s virtue—ignoring merely evidential connections—can also make it appear costly. The CDT agent two-boxes and may end up with only \$1,000, while the EDT agent one-boxes and may receive \$1,000,000.

---

## 5. Counterexamples and unresolved problems

The reference article presents several criticisms of CDT. The most important is that CDT is vague about how to compute counterfactual probabilities. Lewis’s imaging proposal is one answer, but it introduces further difficulties, including a regress concerning what the agent would believe if she were certain of the action.

A second family of criticisms involves alleged counterexamples. These are cases where straightforward CDT appears to recommend a decision that is intuitively bad or self-defeating.

### 5.1 Death in Damascus

In the Death in Damascus scenario, Death predicts where you will be tomorrow and waits there. You are trying to avoid Death. If Death is a reliable predictor, then your choice of location is strongly correlated with Death’s prediction.

A simple CDT model might treat Death’s prediction as fixed when you choose. If you assign prior probability \(p\) to Death predicting Damascus, then staying in Damascus has expected utility proportional to \(1-p\), while fleeing to Aleppo has expected utility proportional to \(p\). CDT may therefore choose the location that it thinks Death is less likely to have predicted.

But if Death is reliable, your choice is evidence about Death’s prediction. The source says that a CDT agent may be unable to process this correlation and may make irrational decisions. The case is closely related to Newcomb’s problem: the agent’s action does not causally affect the predictor’s earlier prediction, but it is strongly correlated with it. CDT’s insistence on treating the prediction as fixed can make the agent neglect the diagnostic value of its own choice.

### 5.2 The Adversarial Offer

The source describes a more recent counterexample called the Adversarial Offer. Two boxes are on offer. The buyer may purchase one box or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both seller and buyer believe the seller’s prediction is accurate with probability \(0.75\).

According to the source, CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value. Since a box costs only \$1, CDT requires buying one. But this is profitable for the seller, meaning that the CDT agent loses money in expectation.

This example is especially interesting because it shows how sensitive CDT can be to the way actions and policies are described. If the action is “buy box 1,” an interventionist model might say that choosing box 1 makes it likely that the seller predicted you would acquire box 1, so box 1 is probably empty. If the action is instead “adopt a policy of buying one randomly selected box,” the evaluation may differ. The source presents the example as a counterexample to CDT; my own view is that it also reveals the importance of specifying the action variable precisely before applying CDT. Without a precise causal model and a clear description of the act or policy, CDT’s recommendation may be indeterminate or misleading.

### 5.3 The Psychopath Button

The source also gives the Psychopath Button example. Paul is considering pressing a button that would kill all psychopaths. He thinks a world without psychopaths would be much better. But he is confident that only a psychopath would press such a button. He strongly prefers living in a world with psychopaths to dying.

According to Egan, almost everyone agrees that Paul should not press the button, yet CDT endorses pressing it. The apparent reason is that CDT focuses on the causal consequence of pressing: psychopaths die. It holds fixed Paul’s psychological type, rather than treating the act as strong evidence that Paul is a psychopath and therefore likely to die. EDT, by contrast, would treat pressing as terrible news about Paul himself.

This case raises a deep question: how should CDT represent facts about the agent’s own character? If Paul’s character causally influences his action, then an intervention on the action may hold character fixed. But if the action is practically inconceivable unless Paul is a psychopath, then holding character fixed may produce a counterfactual that is too distant from the actual decision problem. Critics argue that this is not a mere technical issue but a fundamental flaw in CDT’s treatment of self-knowledge.

### 5.4 Dutch books and money pumps

The source also mentions that Oesterheld and Conitzer have argued that CDT agents can be made to voluntarily lose money in multiple scenarios and can be subject to diachronic Dutch books. A Dutch book is a set of bets or choices that guarantees a loss for the agent because of incoherent probability assignments or decision rules. If CDT agents are systematically exploitable, that is a serious pragmatic objection.

Defenders of CDT, such as James Joyce, argue that CDT can incorporate evidence about one’s own likely actions. Joyce’s position, as summarized in the source, is that CDT can take information about what one is inclined or likely to do as evidence. The dispute is whether this is enough to handle predictor cases, self-revealing actions, and adversarial environments.

---

## 6. A practical procedure for applying CDT

Given the source’s admission that CDT does not itself specify an algorithm for computing counterfactual probabilities, a practical account needs additional structure. The following procedure is my own operational proposal, inspired by modern causal inference.

First, specify the relevant variables. These should include:

1. the available actions or policy variables;
2. background states, such as the agent’s character, other agents’ predictions, or hidden physical states;
3. intermediate causal variables;
4. final outcomes.

Second, specify a causal model. This may be a directed acyclic graph, a system of structural equations, or a set of dependency hypotheses. The model should say which variables causally influence which others.

Third, assign probabilities or distributions to exogenous variables. If the agent is uncertain about the causal model itself, assign probabilities to competing models.

Fourth, for each candidate action \(a\), perform the intervention \(\operatorname{do}(a)\). Compute the resulting distribution over outcomes:

\[
P(o \mid \operatorname{do}(a)).
\]

Fifth, compute causal expected utility:

\[
V_{\mathrm{CDT}}(a)
=
\sum_o P(o \mid \operatorname{do}(a)) D(o).
\]

Sixth, choose an action maximizing this quantity.

For policies, replace step four with an intervention that sets all action variables according to the policy:

\[
V_{\mathrm{CDT}}(\pi)
=
\mathbb E_{M_{\operatorname{do}(\pi)}}[D].
\]

This procedure makes CDT usable in unfamiliar cases, but it also reveals where CDT’s burden lies. The theory does not tell you the correct causal graph. It does not tell you whether a predictor’s prediction should be treated as fixed, as a common effect, as a cause, or as something else. It does not tell you how to individuate actions when the same behavior can be described as “buy box 1,” “buy a box,” or “follow a box-buying policy.” Those modeling choices can affect the recommendation.

In ordinary empirical contexts, this is not a fatal problem. Causal inference always requires a model. But in philosophical cases involving perfect predictors, logical correlation, or agents whose actions reveal their deep character, the required intervention may be controversial. The CDT prescription depends on what counts as the closest world where the action is performed, or on what structural equations are held fixed when the action is surgically imposed.

---

## Conclusion

Causal decision theory says that rational choice is about control, not news. It evaluates actions by the expected desirability of their causal consequences, formally represented by counterfactual probabilities:

\[
U(a)
=
\sum_j P(a \mathbin{\Box\!\to} O_j) D(O_j).
\]

This differs from evidential decision theory, which uses conditional probabilities:

\[
V_{\mathrm{EDT}}(a)
=
\sum_o P(o \mid a) D(o).
\]

The two theories agree when actions are independent of the hidden causes of outcomes, but they diverge in cases involving prediction, common causes, and self-evidence. CDT recommends sending for Bathsheba if charisma is fixed, and two-boxing in Newcomb’s problem if the predictor’s choice is already made. Critics argue that CDT can be vague, unstable, or exploitable in cases such as Death in Damascus, the Adversarial Offer, and the Psychopath Button.

The most defensible way to apply CDT, in my view, is to supplement it with an explicit causal model and evaluate actions or policies using interventions. This makes the theory precise enough for practical use, but it also transfers the difficulty to causal modeling. CDT tells us to choose the action that would cause the best expected outcome; it does not, by itself, tell us how the world causally works. Its strength is a clear normative ideal—choose as an intervener, not as a manager of evidence. Its weakness is that the relevant counterfactuals require a substantive and sometimes disputed representation of causal structure.

---

## References

1. Wikipedia contributors, “Causal decision theory,” revision 1381555528, 2026. Licensed under CC BY-SA 4.0.  
2. Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Belief, Decision, Chance, and Time* (pp. 153–190).  
3. Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.  
4. Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.  
5. Egan, A. (2007). Some counterexamples to causal decision theory. *Philosophical Review*, 116(1), 93–114.  
6. Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *Philosophical Quarterly*, 71(4), pqaa086.  
7. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.  
8. Weirich, P. (2016). Causal decision theory. In E. N. Zalta (ed.), *Stanford Encyclopedia of Philosophy*.