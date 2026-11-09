# Causal Decision Theory: Expected Utility as Causal Expectation

Causal decision theory (CDT) is a school of thought within decision theory holding that a rational agent should choose the action that causes the best outcome in expectation. The reference article contrasts CDT with evidential decision theory (EDT): EDT recommends the action that would be the best “news” if one learned that it had been taken, whereas CDT recommends the action with the best expected causal consequences. In ordinary cases the two coincide: if eating an apple tends to cause happiness and eating an orange tends to cause sadness, both theories say to eat the apple. They diverge when an action is merely evidence for a desirable or undesirable state of affairs without causing it.

This essay gives a formal account of CDT, explains how it evaluates actions and policies, and develops a practical way of applying it. The source article supplies the core counterfactual formulation and several examples; where it leaves the computational machinery underspecified, I propose an operational interpretation using causal models and interventions. That interpretation is not itself stated in the source, but it is a natural way to make CDT usable in unfamiliar cases.

---

## 1. Expected utility: evidential and causal versions

A simple decision problem consists of:

- a set of available actions \(\mathcal A\);
- a set of possible outcomes \(\mathcal O\);
- a desirability or utility function \(D : \mathcal O \to \mathbb R\);
- a probability function representing the agent’s uncertainty.

Evidential decision theory evaluates an action \(a\) by conditional expected utility:

\[
V_{\mathrm{EDT}}(a)
=
\sum_{o \in \mathcal O} P(O=o \mid A=a)\,D(o).
\]

Here \(P(O=o \mid A=a)\) is the probability of outcome \(o\) conditional on the proposition that the agent performs \(a\). EDT therefore asks: if I received the news that I had done \(a\), how good would the world look?

This works when the conditional probability reflects causal influence, but it also captures purely evidential correlations. Suppose eating an apple makes you happy if the apple is good and sad if it is bad, but you do not know whether the apple is good. If \(P(\text{good})=0.8\), \(D(\text{happy})=10\), and \(D(\text{sad})=-5\), the expected value of eating the apple is

\[
0.8 \cdot 10 + 0.2 \cdot (-5) = 7.
\]

If eating an orange has expected value \(-2\), choose the apple. So far, nothing distinctively causal is needed. The distinctive claim of CDT appears when the fact that one performs an action is evidence for some background state of the world, but the action does not causally affect that state.

---

## 2. The counterfactual formulation

The source article gives the classic formulation due to Allan Gibbard and William Harper. CDT evaluates an action \(A\) by

\[
U(A)
=
\sum_j P(A \mathbin{\square\!\to} O_j)\,D(O_j),
\]

where \(D(O_j)\) is the desirability of outcome \(O_j\), and \(P(A \mathbin{\square\!\to} O_j)\) is the probability of the counterfactual: if \(A\) were performed, \(O_j\) would obtain. I write \(\square\!\to\) to emphasize that this is not the material conditional and not simply the conditional probability \(P(O_j \mid A)\).

David Lewis showed that probabilities of conditionals are not generally equal to conditional probabilities. If, for all actions and outcomes,

\[
P(A \mathbin{\square\!\to} O) = P(O \mid A),
\]

then CDT would collapse into EDT. But in general they come apart. Gibbard and Harper argued that under certain logical assumptions—including a controversial principle related to conditional excluded middle—and under statistical independence between performing \(A\) and the truth of the counterfactual \(A \mathbin{\square\!\to} O_j\), the two quantities can coincide. The interesting cases are precisely those where this independence fails.

The core idea is that CDT does not ask, “What is likely given that I do \(A\)?” It asks, “What would happen if I did \(A\)?” The second question is counterfactual or interventional, not merely statistical.

---

## 3. A working operationalization: interventions and causal models

The source article notes an important gap: CDT does not by itself specify an algorithm for calculating the counterfactual probabilities \(P(A \mathbin{\square\!\to} O_j)\). One proposal mentioned in the source is Lewis’s “imaging” technique: to evaluate the probability of \(A \mathbin{\square\!\to} O\), move probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) holds. Formally, one might write something like

\[
P_{\text{im}}(A \mathbin{\square\!\to} O)
=
\sum_w P(w)\,\mathbf 1_O(w_A),
\]

where \(w_A\) is the closest \(A\)-world to \(w\). But this requires a similarity ordering over worlds and some account of what one would believe if one were certain of \(A\). The source notes that this can lead to regress.

A more explicit operational interpretation—one that I add to the source’s account—is to use a structural causal model and an intervention operator. Let \(M\) be a causal model with variables including an action variable \(A\) and an outcome variable \(O\). The model specifies how variables depend on their causes, for example through structural equations. An intervention \(do(A=a)\) means: set \(A\) to \(a\) by external fiat, leaving the rest of the causal structure intact. Then the CDT value of action \(a\) is

\[
V_{\mathrm{CDT}}(a)
=
\sum_o P_M(O=o \mid do(A=a))\,D(o).
\]

The expression \(P_M(O=o \mid do(A=a))\) is the probability that outcome \(o\) would occur if \(A=a\) were imposed, not merely the probability of \(o\) conditional on observing \(A=a\).

This gives a practical rule:

\[
\text{Choose } a \text{ maximizing } \sum_o P(O=o \mid do(a))D(o).
\]

If the agent is uncertain about which causal model is correct, let \(H\) range over “dependency hypotheses,” each specifying how outcomes depend counterfactually on actions. With prior probability \(p(h)\), a natural CDT extension is

\[
V_{\mathrm{CDT}}(a)
=
\sum_h p(h)
\sum_o P_h(O=o \mid do(a))\,D(o).
\]

The source’s discussion of Andy Egan’s criticism suggests that CDT holds fixed the agent’s prior credences in such dependency hypotheses rather than updating them on the action itself. That is, CDT uses \(p(h)\), not \(p(h \mid a)\), unless the action causally affects the truth of \(h\) or is connected to it through the model. This is one of the theory’s most important and controversial features.

The same approach can evaluate policies. Suppose a policy \(\pi\) maps possible observations or decision nodes to actions. Introduce a policy variable \(\Pi\) whose value determines the agent’s decision rule. Then one can define

\[
V_{\mathrm{CDT}}(\pi)
=
\sum_o P(O=o \mid do(\Pi=\pi))\,D(o).
\]

This policy evaluation is my extension of the source’s action-based formulation. The source mainly discusses individual acts, such as taking both boxes or one box in Newcomb’s problem. But in sequential decisions, it is often useful to treat the adoption of a policy as the relevant intervention. One caution: if the agent will later re-decide locally at each future node, a policy may not be credible unless the agent can precommit. CDT can evaluate precommitment devices as causal interventions that change future behavior, but the source leaves the dynamics of policies largely open.

---

## 4. Examples: King David and Newcomb’s problem

### King David’s dilemma

The source gives an example due to Gibbard and Harper. King David wants Bathsheba but fears that summoning her will provoke revolt. David has learned that kings fall into two personality types: charismatic and uncharismatic. Charisma is fixed by genetics and early childhood. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. However, unjust acts themselves do not cause revolts; the revolts are caused by the king’s uncharismatic bearing. David does not know whether he is charismatic.

Let \(C\) be David’s charisma, \(A\) the action of summoning Bathsheba, and \(R\) the occurrence of revolt. The causal structure is roughly:

\[
C \rightarrow \text{behavior}, \qquad C \rightarrow R.
\]

The action \(A\) may be evidence about \(C\), because an uncharismatic king is more likely to act unjustly. EDT therefore reasons:

\[
P(C=\text{uncharismatic} \mid A=\text{summon})
\]

is high, and uncharismatic kings face revolt, so David should abstain.

CDT reasons differently. Since David’s charisma is fixed, the intervention \(do(A=\text{summon})\) does not change \(C\):

\[
P(C \mid do(A=\text{summon})) = P(C).
\]

Moreover, by hypothesis, summoning Bathsheba does not itself cause revolt. If the direct benefit of summoning outweighs any genuine causal costs, CDT recommends summoning. The example illustrates CDT’s refusal to treat an action as bad merely because it is bad news about one’s own type.

### Newcomb’s problem

In Newcomb’s problem, a highly reliable predictor has already predicted whether the agent will take one box or two. Box A visibly contains \$1,000. Box B contains either \$1,000,000 or nothing. If the predictor predicted one-boxing, it put \$1,000,000 in box B. If it predicted two-boxing, it left box B empty. The agent now chooses between taking only box B or taking both boxes.

Let \(B\) be the content of box B. The standard CDT assumption is that the predictor’s prediction is already in the past and that the current choice does not causally affect it. Thus:

\[
P(B \mid do(\text{two-box})) = P(B).
\]

Given \(B\), two-boxing yields \$1,000 more than one-boxing:

- If \(B = \$1{,}000{,}000\), two-boxing gives \$1,001,000; one-boxing gives \$1,000,000.
- If \(B = \$0\), two-boxing gives \$1,000; one-boxing gives \$0.

So CDT computes:

\[
V_{\mathrm{CDT}}(\text{two-box})
=
P(B=M)(M+1000) + P(B=0)(1000),
\]

\[
V_{\mathrm{CDT}}(\text{one-box})
=
P(B=M)M + P(B=0)0.
\]

The difference is always \$1,000:

\[
V_{\mathrm{CDT}}(\text{two-box}) - V_{\mathrm{CDT}}(\text{one-box}) = 1000.
\]

Therefore CDT recommends two-boxing.

EDT, by contrast, uses conditional probabilities. Because the predictor is reliable, one-boxing is strong evidence that box B contains \$1,000,000, while two-boxing is strong evidence that box B is empty. If the predictor is 99% accurate, EDT gives roughly:

\[
V_{\mathrm{EDT}}(\text{one-box})
\approx 0.99M,
\]

\[
V_{\mathrm{EDT}}(\text{two-box})
\approx 0.01(M+1000) + 0.99(1000).
\]

For large \(M\), EDT recommends one-boxing.

The disagreement is not about arithmetic; it is about which probabilities matter. CDT uses the distribution that would obtain under the intervention of choosing two boxes; EDT uses the evidential conditional distribution.

---

## 5. Which dependencies matter?

CDT treats a dependency as decision-relevant when the outcome counterfactually depends on the action through a causal route. If changing \(A\) by intervention changes the probability of \(O\), then that dependence matters. If \(A\) and \(O\) are correlated only because they share a common cause, CDT generally ignores that correlation for the purpose of evaluating \(A\), unless the action also causally affects the common cause or some downstream variable that affects \(O\).

This is the difference between conditioning and intervening. In a causal graph, conditioning on \(A\) can change probabilities of its causes, because observing \(A\) provides evidence about them. Intervening on \(A\) does not change the distribution of its causes. Thus:

\[
P(C \mid A=a) \neq P(C \mid do(A=a))
\]

when \(C\) is a cause or common cause related to \(A\).

This point explains many CDT verdicts. In King David’s case, charisma is a common cause of both David’s likely action and revolt. In Newcomb’s problem, the predictor’s prediction is a prior cause or correlate of the agent’s choice and of the box contents. CDT says: choose by asking what your action would cause, not by asking what your action indicates.

A useful formulation is in terms of dependency hypotheses. A dependency hypothesis \(h\) specifies, for each action, what outcomes would follow. CDT evaluates:

\[
V_{\mathrm{CDT}}(a)
=
\sum_h p(h)
\sum_o P_h(O=o \mid do(a))D(o).
\]

The source’s summary of Egan’s criticism is that CDT requires “holding fixed the agent’s unconditional credences in dependency hypotheses.” In other words, CDT does not let the fact that you are about to perform \(a\) become evidence about which causal structure obtains, except insofar as that is represented inside the causal model. This is precisely what makes CDT stable in some cases and controversial in others.

---

## 6. Vagueness, imaging, and counterexamples

The source identifies a major difficulty: CDT does not itself say how to compute the counterfactual probabilities. Lewis’s imaging proposal gives one semantic picture, but it requires a notion of similarity between possible worlds and may lead to regress, because one must know what one would believe if one were certain of the action. The structural-causal-model interpretation above avoids some of this vagueness, but only by adding explicit causal assumptions. If those assumptions are wrong or unspecified, CDT may not give a determinate answer.

The source also discusses several alleged counterexamples.

### Death in Damascus

In the “Death in Damascus” scenario, Death predicts where you will be tomorrow and waits for you there. If Death is a reliable predictor, your choice of location is correlated with Death’s prediction. CDT may struggle because your current choice does not causally change Death’s earlier prediction. If staying and fleeing are both predicted with high reliability, CDT may fail to see either action as causally beneficial, even though intuitively one might want to exploit uncertainty or randomize. Critics argue that this shows CDT cannot handle certain predictor correlations.

### The psychopath button

Paul is deciding whether to press a button that kills all psychopaths. He thinks a world without psychopaths would be much better, but he is confident that only a psychopath would press such a button. He strongly prefers living in a world with psychopaths to dying.

Let \(S\) be the proposition that Paul is a psychopath. If Paul is not a psychopath, pressing the button may cause a better world. If Paul is a psychopath, pressing it causes his death. CDT may hold fixed Paul’s prior probability of being a psychopath:

\[
V_{\mathrm{CDT}}(\text{press})
=
P(S)D(\text{death})
+
P(\neg S)D(\text{no psychopaths}).
\]

If \(P(S)\) is small enough and \(D(\text{no psychopaths})\) high enough, CDT can recommend pressing. But intuitively, the fact that Paul is inclined to press is strong evidence that he is a psychopath. EDT would use \(P(S \mid \text{press})\), which may be high, and would recommend not pressing. The source quotes Egan’s claim that “pretty much everyone” agrees Paul should not press, while CDT endorses pressing.

Defenders of CDT, such as Jim Joyce, argue that CDT can incorporate information about one’s inclinations and likely behavior. But the source presents this as disputed. The psychopath button highlights the tension between causal efficacy and self-evidential reasoning.

### The adversarial offer

The source describes a variant involving two boxes, each costing \$1. The buyer may buy one box or none, but not both. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

According to the source, CDT reasons that at least one box probably contains \$3, so the average box has at least \$1.50 in causal expected value. Since a box costs only \$1, CDT requires buying one. But if the seller’s prediction tracks the buyer’s actual choice, the buyer tends to select the box predicted to be acquired, which is likely empty. The seller therefore profits. This kind of case is used to argue that CDT agents can voluntarily lose money and may be subject to Dutch-book-like exploitation.

These counterexamples do not merely dispute particular verdicts. They challenge the central CDT idea that one should hold fixed the causal structure and the agent’s prior view of it while evaluating the act’s causal consequences.

---

## 7. How to apply CDT to an unfamiliar problem

A reasonable operational procedure, combining the source’s counterfactual idea with the interventionist interpretation, is:

1. **List the available actions** \(a \in \mathcal A\) and possible outcomes \(o \in \mathcal O\). Assign utilities \(D(o)\).

2. **Specify the relevant causal structure.** Draw variables and causal arrows. Identify common causes, mediators, and background states.

3. **Identify the action variable** \(A\) on which the agent can intervene.

4. **Replace conditioning with intervention.** For each action \(a\), compute or estimate \(P(O=o \mid do(A=a))\), not merely \(P(O=o \mid A=a)\).

5. **Average over uncertain causal hypotheses.** If the agent is unsure which causal model is correct, use

   \[
   V_{\mathrm{CDT}}(a)
   =
   \sum_h p(h)
   \sum_o P_h(O=o \mid do(a))D(o).
   \]

6. **Evaluate policies by intervening on a policy variable**, if the problem involves rules or sequential choices:

   \[
   V_{\mathrm{CDT}}(\pi)
   =
   \sum_o P(O=o \mid do(\Pi=\pi))D(o).
   \]

7. **Check dynamic consistency.** If a policy requires future actions that the future agent will not locally choose, consider whether precommitment is possible and evaluate the precommitment as an action.

8. **Separate news from causation.** Ask: does doing \(a\) make \(o\) happen, or does doing \(a\) merely indicate that \(o\) is likely?

This procedure makes CDT precise enough for many practical cases, but it also makes clear that CDT’s verdict depends heavily on the assumed causal model.

---

## Conclusion

Causal decision theory says that rational choice should track expected causal consequences, not merely expected news. Its core formula evaluates actions by the probabilities of counterfactuals: if I did \(A\), what would happen? The theory differs from evidential decision theory precisely in cases where actions are correlated with outcomes without causing them, as in King David’s dilemma and Newcomb’s problem. The source article leaves open the exact computation of counterfactual probabilities, but an interventionist causal-model interpretation provides a workable operationalization: evaluate \(P(O \mid do(A))\), average over causal uncertainty, and, for policies, intervene on the policy variable. The price of this precision is that CDT’s verdicts depend on substantive causal assumptions, and several counterexamples suggest that its insistence on holding fixed the agent’s prior causal beliefs may sometimes produce unintuitive or exploitable choices.

---

## References

Wikipedia contributors. “Causal Decision Theory.” Revision 1381555528, October 23, 2026. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190, 1981.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

Pearl, Judea. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press, 2009.