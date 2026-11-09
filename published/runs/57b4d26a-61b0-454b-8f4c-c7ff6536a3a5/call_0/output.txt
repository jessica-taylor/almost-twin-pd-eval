# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a school of thought within decision theory that evaluates actions by asking what would be good to learn about oneself. The reference article summarizes the idea by saying that EDT recommends choosing the action with the highest *news value*: the action that would be indicative of the best outcome in expectation if one received the “news” that it had been taken. In a memorable phrase attributed in the article to Arif Ahmed, EDT tells us to “do what you most want to learn that you will do” (Wikipedia contributors, 2026).

This formulation makes EDT sound almost psychological, but it has a precise mathematical core. EDT replaces the causal or interventionist expected utility of an action with an ordinary conditional expected utility. The action is treated as evidence about the world, not necessarily as a causal lever on the world. This small formal change has large philosophical consequences. In famous cases such as Newcomb’s problem and certain prisoner’s dilemma variants, EDT gives recommendations that differ from those of causal decision theory (CDT). The reference article emphasizes exactly this contrast: EDT one-boxes in Newcomb’s problem, while CDT two-boxes.

In this essay I reconstruct EDT as a decision procedure, explain how it treats probabilistic dependencies and counterfactuals, and show how to apply it to unfamiliar problems. I distinguish claims made by the source from additional operational proposals that I introduce where the source is silent.

---

## 1. The basic EDT formula

Suppose an agent faces a finite set of possible actions

\[
\mathcal A=\{A_1,\dots,A_n\}.
\]

The actions are treated as mutually exclusive and jointly exhaustive propositions: exactly one of them will be performed. Let

\[
\{O_1,\dots,O_m\}
\]

be a partition of possible outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The agent has a probability function \(P\) representing her credences over relevant propositions, including propositions about her own possible actions.

The reference article gives the EDT value of an action as

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

where \(P(O_j\mid A)\) is the conditional probability of outcome \(O_j\) given that action \(A\) is performed (Gibbard & Harper, 1976, as cited in Wikipedia contributors, 2026). In expectation notation,

\[
V(A)=\mathbb E[D(O)\mid A].
\]

EDT then recommends choosing an action that maximizes \(V(A)\):

\[
A^\star \in \arg\max_{A\in\mathcal A} V(A).
\]

If the outcome space is continuous, the sum is replaced by an integral:

\[
V(A)=\int D(o)\,dP(o\mid A).
\]

The formula is simple, but its interpretation depends on what the conditional probability \(P(O_j\mid A)\) is supposed to represent. EDT does not ask, “What would happen if I causally intervened to make \(A\) true?” It asks, “What should I expect, conditional on the proposition that \(A\) is true?” The action is used as evidence.

This is why EDT is called *evidential*. The value of an action is the expected desirability of the outcomes that would be indicated by learning that the action was performed.

---

## 2. Conditional probability versus intervention

The mathematical distinction between EDT and CDT can be expressed using conditional probabilities and interventionist probabilities. The reference article contrasts EDT’s formula with the CDT formula

\[
U(A)=\sum_j P(A \mathrel{\Box{\rightarrow}} O_j)D(O_j),
\]

where \(A \mathrel{\Box{\rightarrow}} O_j\) is a counterfactual: roughly, “if \(A\) were performed, \(O_j\) would occur.” CDT uses probabilities over counterfactual worlds in which the action is made true while the causal structure of the world is held fixed in the appropriate way.

EDT instead uses

\[
P(O_j\mid A)=\frac{P(O_j\land A)}{P(A)}.
\]

This is an ordinary Bayesian conditional. It does not sever statistical dependencies between the action and other variables. If the action is correlated with a hidden state, a predictor’s prediction, an agent’s character, a genetic trait, or another agent’s reasoning process, EDT allows that correlation to affect the expected utility of the action.

A useful way to see this is to introduce a hidden state \(S\). Suppose outcomes depend on both the action \(A\) and the state \(S\). Then

\[
P(O\mid A)=\sum_s P(O\mid A,S=s)P(S=s\mid A).
\]

EDT evaluates the action using the posterior distribution \(P(S=s\mid A)\). If performing \(A\) is evidence that \(S\) is good, EDT gives \(A\) extra value. If performing \(A\) is evidence that \(S\) is bad, EDT penalizes \(A\), even if \(A\) does not causally affect \(S\).

In modern causal-graph terminology, EDT conditions on the action node. CDT, by contrast, applies a \(do\)-operator: it asks for \(P(O\mid do(A))\). Conditioning on \(A\) preserves correlations between \(A\) and its causes or common causes; intervening on \(A\) cuts those correlations. EDT is therefore sensitive to what an action indicates, whereas CDT is sensitive to what an action produces.

The reference article notes that because \(P(O_j\mid A)\) and \(P(A \mathrel{\Box{\rightarrow}} O_j)\) are not always equal, EDT and CDT are not equivalent. Their disagreement is not merely verbal; it can lead to different choices.

---

## 3. Newcomb’s problem

The standard illustration is Newcomb’s paradox. The reference article describes the setup as follows. A predictor, accurate with probability \(0.99\), has already made a prediction about whether the player will take only box B or both boxes A and B. Box A is transparent and contains \$1,000. Box B is opaque. If the predictor predicted that the player will take only B, it placed \$1,000,000 in B. If the predictor predicted that the player will take both boxes, it left B empty.

The player can choose:

- \(A_1\): take only B;
- \(A_2\): take both A and B.

EDT computes conditional expected values. Taking only B is strong evidence that the predictor predicted one-boxing, so B probably contains \$1,000,000. Taking both boxes is strong evidence that the predictor predicted two-boxing, so B is probably empty.

Using the article’s numbers:

\[
\begin{aligned}
V(\text{take only B})
&=P(\text{\$1M in B}\mid \text{take only B})\cdot \$1{,}000{,}000 \\
&\quad +P(\text{nothing in B}\mid \text{take only B})\cdot \$0 \\
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0 \\
&=\$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{take both boxes})
&=P(\text{\$1M in B}\mid \text{take both boxes})\cdot \$1{,}001{,}000 \\
&\quad +P(\text{nothing in B}\mid \text{take both boxes})\cdot \$1{,}000 \\
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{take only B})>V(\text{take both boxes}),
\]

EDT recommends taking only box B.

The reasoning is purely evidential. The player does not believe that choosing one box now causally causes the predictor to have placed money in the box in the past. Rather, choosing one box is excellent evidence that the predictor already placed money there. EDT treats that evidential connection as decision-relevant.

CDT, according to the source, recommends taking both boxes because the contents of B are already fixed. From a causal perspective, taking both boxes adds \$1,000 to whatever is in B. If B is full, two-boxing yields \$1,001,000; if B is empty, two-boxing yields \$1,000. In either causal state, two-boxing is better by \$1,000. So CDT two-boxes, while EDT one-boxes.

One subtlety is worth adding. The article’s calculation assumes that the conditional probabilities match the predictor’s accuracy in a symmetric way:

\[
P(\text{predict one-box}\mid \text{one-box})=0.99,
\]

and

\[
P(\text{predict two-box}\mid \text{two-box})=0.99.
\]

In a more general model, one would need to specify the predictor’s false-positive and false-negative rates, as well as the prior probability of each action. EDT itself does not determine those probabilities; it takes the agent’s probability model as input.

---

## 4. The twin prisoner’s dilemma

The reference article also discusses a twin prisoner’s dilemma. Aomame and her psychological twin are in separate rooms. They cannot communicate. Their reasoning processes are exactly analogous. The payoff matrix for Aomame is:

- both cooperate: each receives \$5;
- both defect: each receives \$1;
- one cooperates and the other defects: the defector receives \$10, the cooperator receives \$0.

If Aomame’s action were causally independent of her twin’s action, standard decision theory would recommend defecting. But EDT treats Aomame’s choice as evidence about her twin’s choice. Since the twins reason in exactly analogous ways, Aomame’s cooperation is strong evidence that her twin will cooperate, and her defection is strong evidence that her twin will defect.

The article models this as perfect correlation:

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

and

\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then

\[
\begin{aligned}
V(\text{Aomame cooperates})
&=1\cdot \$5+0\cdot \$0 \\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{Aomame defects})
&=0\cdot \$10+1\cdot \$1 \\
&=\$1.
\end{aligned}
\]

Therefore EDT recommends cooperation.

This example shows how EDT can formalize a kind of correlation-based cooperation. The action does not cause the twin’s action. Instead, the action is evidence of the twin’s action because both agents share a reasoning process. EDT counts that evidence.

It is helpful to generalize this slightly, beyond the source’s perfect-correlation example. Let

\[
q=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and

\[
r=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5q,
\]

while

\[
V(D)=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when

\[
5q>1+9r.
\]

If the twins are perfectly correlated, \(q=1\) and \(r=0\), so cooperation wins. If Aomame’s action is independent of her twin’s action, then \(q=r\), and defection wins because

\[
1+9q>5q
\]

for every \(q\in[0,1]\). Thus EDT does not recommend cooperation in every prisoner’s dilemma. It recommends cooperation when one’s own cooperative choice is sufficiently strong evidence of the other party’s cooperation.

---

## 5. How to apply EDT to an unfamiliar decision problem

The preceding examples suggest a general procedure.

First, identify the possible actions. EDT requires a set of action propositions that are mutually exclusive and jointly exhaustive relative to the decision.

Second, identify the possible outcomes and assign desirabilities \(D(O_j)\). These desirabilities should reflect everything the agent cares about. If an action has intrinsic psychological value, that value should be included in the outcome evaluation. For example, if one-boxing feels virtuous or two-boxing feels greedy, those feelings can be included in \(D\), provided they are properly represented as parts of outcomes.

Third, specify the agent’s probability model over actions, states, predictions, other agents’ choices, and outcomes. This is the most substantive step. EDT does not tell the agent what probabilities to have; it tells her how to use them.

Fourth, compute

\[
V(A)=\sum_j P(O_j\mid A)D(O_j)
\]

for each action.

Fifth, choose an action with maximal EDT value.

This procedure is straightforward in toy examples, but it raises an important interpretive question. The source does not fully explain how the agent should assign probabilities to her own actions before choosing. The conditional probability \(P(O_j\mid A)\) requires \(P(A)>0\). But if the agent already knows what she will do, then from her perspective the chosen action may have probability 1 and the alternatives probability 0. In that case, conditioning on the unchosen alternatives is undefined or degenerate.

A reasonable operational interpretation, which I add to the source’s presentation, is to evaluate actions from a deliberative standpoint in which the agent has not yet settled which action she will perform. One can imagine a prior probability distribution over possible choices, perhaps generated by a stochastic decision process or by a predictor’s uncertainty. If deterministic deliberation would assign probability zero to some alternative, one can regularize the model by giving every alternative a small positive probability \(\varepsilon\), compute the conditional expected utilities, and then take the limit as \(\varepsilon\to 0\) if needed.

Formally, let \(P_\varepsilon\) be a probability function with full support over actions. Define

\[
V_\varepsilon(A)=\sum_j P_\varepsilon(O_j\mid A)D(O_j).
\]

Then take

\[
V(A)=\lim_{\varepsilon\to 0}V_\varepsilon(A)
\]

when the limit exists. This “trembling-hand” or stochastic-choice interpretation preserves the news-value intuition: EDT asks what would be good to learn, so the alternatives must remain possible objects of news.

This proposal is not explicitly stated in the reference article, but it fits the motivating idea. EDT is not meant to evaluate an action after the agent already knows with certainty that she will perform it. It is meant to compare possible actions as possible pieces of news.

---

## 6. Policies, sequential decisions, and dynamic issues

The source focuses on single acts, but decision problems often involve policies. A policy is a rule mapping information states to actions. For example, a policy might say: “If the predictor’s testimony is ambiguous, take one box; otherwise take two boxes.” EDT can evaluate policies by treating the policy itself as the object of news.

Let \(\Pi\) be a set of possible policies, and let \(\pi\in\Pi\) be a policy. If the agent has a probability distribution over policies and outcomes, EDT can assign

\[
V(\pi)=\sum_o P(O_o\mid \Pi=\pi)D(O_o).
\]

The policy is then evaluated by the expected desirability conditional on learning that the agent will follow \(\pi\). This is a natural extension of EDT, though the reference article does not develop it.

Sequential problems introduce a further complication. Suppose an agent chooses a policy at time \(t_0\), but later faces a local choice at time \(t_1\). EDT may recommend one policy ex ante, while later recommending a different local action once new evidence is available. In other words, EDT can be dynamically inconsistent unless the agent can precommit.

For example, an agent may ex ante prefer a policy of one-boxing because adopting that policy is excellent news about future payoffs. But later, when standing in front of the boxes, local EDT may still one-box in standard Newcomb problems; in other sequential variants, however, the locally best news may differ from the globally best policy. The source does not resolve this issue.

A defensible operational rule is this: if the agent can bind herself to a policy, EDT should evaluate complete policies at the earliest relevant choice point. If she cannot bind herself, she should apply EDT at each information state, while recognizing that the resulting plan may not be the one that was ex ante most desirable. Alternatively, a “resolute” EDT agent might continue to follow the policy whose adoption had the highest ex ante news value, provided that the policy itself remains evidentially relevant. This is an interpretive choice not settled by the source.

The important point is that EDT’s basic object of evaluation can be either an act or a policy. What remains constant is the evidential rule: evaluate the object by the expected value of the outcomes conditional on learning that the object is chosen.

---

## 7. Dependencies, counterfactuals, and the logic of news

EDT’s treatment of dependencies is broad. Any probabilistic dependence between action and outcome can matter, regardless of its source. The dependence may arise from:

1. direct causation;
2. common causes;
3. predictors;
4. psychological similarity;
5. algorithmic or logical correlation;
6. selection effects;
7. self-locating uncertainty.

EDT does not ask whether the dependence is causally productive. It asks whether the action is evidence for the outcome.

This explains why EDT gives distinctive verdicts in Newcomb-type cases. In Newcomb’s problem, the player’s action and the predictor’s prediction are probabilistically dependent. EDT conditions on the action and thereby updates its expectations about the prediction. CDT treats the prediction as causally fixed and asks only what the action adds.

The reference article also mentions the Sleeping Beauty problem. It says EDT has been applied to Sleeping Beauty in order to avoid Dutch book arguments, but that Vincent Conitzer has argued that halfers remain vulnerable to Dutch books even after adopting EDT (Wikipedia contributors, 2026, citing Conitzer, 2015). This illustrates a broader point: EDT is a decision rule, not a complete theory of self-locating credence. In problems involving centered propositions, indexical uncertainty, or repeated awakenings, EDT still needs an account of how probabilities should be assigned over the agent’s possible locations or experiences. The source leaves this territory partly open.

EDT also has a strategic advantage in cases involving many correlated decision-makers. The reference article mentions an argument sometimes called the evidentialist’s wager: even if one places only modest credence in EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, making the stakes higher (MacAskill et al., 2021, as cited in Wikipedia contributors, 2026). This is a source claim, not an independent theorem of EDT. But the intuition is understandable: if many agents reason similarly, then one’s own choice may be evidence about many other choices, amplifying the expected value of cooperative or coordination-friendly actions.

---

## 8. Criticisms and limitations

The most famous criticism of EDT is that it confuses good news with good causation. The reference article quotes David Lewis’s description of EDT as “an irrational policy of managing the news” (Lewis, 1981, as cited in Wikipedia contributors, 2026). James Joyce similarly asserts that rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news (Joyce, 1999, as cited in Wikipedia contributors, 2026).

This criticism points to a real tension. Suppose some harmless action is statistically correlated with a good outcome, not because it causes the outcome, but because people who are already likely to get the good outcome tend to perform that action. EDT may recommend the action because it is good news. A causal decision theorist would say that this is irrational: one should not choose a mere symptom of success if the action does nothing to produce success.

A classic style of example involves medical or genetic correlations. If an action is evidence of an underlying condition that causes bad outcomes, EDT may penalize the action even if the action itself is harmless. Conversely, if an action is evidence of a beneficial condition, EDT may favor it. EDT’s defenders can reply that rational choice should care about expected outcomes, not causal purity. If learning that you will perform an action genuinely raises your expected utility, then there is something right about choosing it. Critics respond that this allows agents to exploit correlations that they cannot actually bring about.

Another limitation concerns probability modeling. EDT’s verdicts depend heavily on the agent’s probability assignments. In Newcomb’s problem, changing the predictor’s accuracy or the prior distribution over actions can change the numerical values, though the qualitative recommendation remains one-boxing for sufficiently reliable predictors. In more complicated cases, reasonable agents may disagree about the correct conditional probabilities. EDT gives a formal rule, but it does not eliminate substantive disagreement about the model.

Finally, EDT’s news-value metaphor can become unstable in reflexive deliberation. If the agent knows that EDT recommends action \(A\), then learning that she will perform \(A\) may partly just mean learning that she is following EDT. The evidential significance of the action can change depending on how the agent models her own decision procedure. This is not unique to EDT, but it is especially sharp because EDT explicitly conditions on the agent’s action as a proposition about the world.

---

## 9. Conclusion

Evidential decision theory offers a clean mathematical rule: choose the action that maximizes expected utility conditional on that action. Its central equation,

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

captures the idea that rational action is guided by the news value of actions. EDT treats actions as evidence about states of the world, predictions, other agents’ behavior, and outcomes. It therefore recommends one-boxing in Newcomb’s problem and cooperating in sufficiently correlated twin prisoner’s dilemmas.

The theory’s strength is that it takes probabilistic dependencies seriously. Its vulnerability is that it may treat mere evidence as if it were efficacy. The reference article presents this as the central divide between EDT and CDT: EDT asks what an action indicates, while CDT asks what an action causes. Where the source leaves questions open—especially concerning zero-probability actions, sequential policies, and self-locating cases—a natural operational approach is to model choices with full-support probability distributions, evaluate policies as objects of news, and take limits where necessary. EDT then becomes not merely a philosophical position but a usable procedure: build a probabilistic model of the decision situation, condition on each possible action or policy, compute the expected desirability of the resulting news, and choose the option with the best news to bring.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, *192*(9), 2887–2899.

Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and two kinds of expected utility*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, *59*(1), 5–30.

MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist’s Wager*.

Wikipedia contributors. (2026). Evidential decision theory (revision 1373679688). Wikipedia. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688