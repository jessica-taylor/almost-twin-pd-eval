# Evidential Decision Theory: Choosing the Best News About What You Will Do

Evidential decision theory (EDT) is a school of decision theory that evaluates actions by their *news value*: an action is good to the extent that learning you had performed it would be evidence of a good outcome. The reference article summarizes the slogan nicely: EDT recommends “do what you most want to learn that you will do” (Ahmed 2021, as cited in Wikipedia contributors 2026). In ordinary expected-utility language, EDT says that a rational agent should choose the action with the highest expected utility *conditional on that action being taken*.

This sounds close to ordinary Bayesian decision theory, and in many cases it is. The interest of EDT comes from cases where an action is correlated with an outcome without obviously causing it. In such cases, EDT may recommend an action because the action is good evidence, even if the action does not causally bring about the desired result. The standard contrast is causal decision theory (CDT), which evaluates actions by their expected causal efficacy rather than by their evidential implications. The two theories often agree, but they famously diverge in Newcomb’s paradox, in twin prisoner’s dilemma cases, and in some problems involving prediction, coordination, and self-locating uncertainty.

This essay develops EDT as a usable decision procedure. I will state the formal rule, explain how to apply it to actions and policies, clarify how it treats dependence and counterfactuals, and discuss several examples. The core formula and the Newcomb and twin-prisoner examples come from the supplied reference; some elaborations—especially the state-space formulation, the policy rule, and the operational treatment of zero-probability actions—are my own.

---

## 1. The EDT decision rule

Suppose an agent faces a finite set of possible actions \(A_1,\dots,A_n\). Let \(O_1,\dots,O_m\) be a partition of possible outcomes, where each \(O_j\) describes a complete enough specification of what the agent cares about. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). EDT assigns to action \(A\) the value

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the formula given in the reference article, attributed to Gibbard and Harper (1978/1976). The term \(P(O_j\mid A)\) is the ordinary conditional probability of outcome \(O_j\) given that the agent performs action \(A\). EDT then prescribes:

\[
\text{Choose an action } A^* \text{ such that } V(A^*) \ge V(A) \text{ for all available } A.
\]

It is often useful to rewrite the rule in terms of states of the world. Let \(S_1,\dots,S_k\) be states that matter for the outcome. The utility of performing action \(A\) in state \(S_k\) is \(U(A,S_k)\). Then EDT evaluates

\[
V(A)=\sum_k P(S_k\mid A)U(A,S_k).
\]

This state-space version is not explicitly in the source, but it is a standard way to make the dependence structure clearer. The crucial feature is that the probabilities are *conditional on the action*. EDT asks: if I were to learn that I will do \(A\), how should that change my probabilities over the relevant states and outcomes?

For example, if smoking is statistically associated with cancer, then learning that I smoke may raise my probability that I have cancer. If my action set is \(\{\text{smoke},\text{do not smoke}\}\), EDT uses \(P(\text{cancer}\mid\text{smoke})\) and \(P(\text{cancer}\mid\text{do not smoke})\), not merely the unconditional probability of cancer.

A technical caveat: the conditional probability \(P(O\mid A)\) is normally defined as

\[
P(O\mid A)=\frac{P(O\land A)}{P(A)}
\]

when \(P(A)>0\). If the agent assigns zero prior probability to an action, conditionalization is not directly defined. In practice, one may need regular conditional probabilities, limiting procedures, or a model in which the agent retains some uncertainty about which action its own decision procedure will produce. I return to this issue below.

---

## 2. EDT and causal decision theory

The reference article contrasts EDT with CDT using a counterfactual expected-utility formula:

\[
U_{\text{CDT}}(A)=\sum_j P(A\mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A\mathrel{\Box\rightarrow} O_j\) means something like “if \(A\) were performed, \(O_j\) would occur,” interpreted causally or interventionally. The essential difference is that EDT uses ordinary conditional probabilities \(P(O_j\mid A)\), while CDT uses probabilities over counterfactual outcomes under an intervention that brings about \(A\).

These two quantities can differ. An action may be evidence for an outcome without causing it. A medical symptom is evidence for a disease, but producing the symptom does not produce the disease. A predictor’s prediction may be evidence for my choice, but my later choice may not causally change the earlier prediction. A twin’s choice may be evidence for my choice because we share the same reasoning process, even though neither choice causes the other.

EDT treats all such dependencies as decision-relevant. CDT tries to filter out merely evidential dependencies and focus on what the action causally produces.

The two theories agree when the relevant states are probabilistically independent of the action except insofar as the action causally affects them. In many ordinary decisions, this independence assumption is approximately true. If I choose between tea and coffee, and my choice does not provide significant evidence about hidden states of the world, then EDT and CDT will normally give the same recommendation. They become interestingly different when the agent’s action is strongly correlated with some important state of the world through prediction, common causation, logical similarity, selection effects, or self-locating evidence.

---

## 3. What counts as a relevant dependency?

EDT’s central operational question is:

> Given my total evidence, what would the news “I will perform \(A\)” tell me about the world?

The relevant dependencies are therefore all dependencies that make \(P(S_k\mid A)\) differ from \(P(S_k)\), or that otherwise affect the conditional distribution over outcomes.

These dependencies may have several sources.

First, the action may causally affect the outcome. If taking medicine helps cure a disease, then \(P(\text{recovery}\mid\text{take medicine})\) may be high partly because taking medicine causally promotes recovery.

Second, the outcome or a cause of the outcome may influence the action. If a disease causes both a desire to smoke and cancer, then smoking is evidence of the disease. EDT responds to that evidence.

Third, a common cause may influence both the action and the outcome. A predictor may predict my behavior and then arrange the contents of a box. My action and the box’s contents are correlated because the predictor’s prediction is a common cause, or at least an evidential intermediary.

Fourth, logical or algorithmic similarity may create dependence. If another agent reasons in exactly the same way I do, then my choice may be strong evidence of their choice, even if there is no causal interaction.

EDT does not require the agent to distinguish these sources. It simply conditions on the action. That is both its simplicity and its controversy.

One way to express the contrast is this: CDT asks, “What would happen if I intervened to make myself do \(A\)?” EDT asks, “What should I expect if I learned that I will do \(A\)?” The second question is not necessarily a causal question. It is an evidential question about which worlds become more plausible given the news of the action.

---

## 4. Newcomb’s paradox

The reference article discusses Newcomb’s paradox, the classic case favoring EDT. A highly reliable predictor has predicted whether the agent will take only box B or both boxes A and B. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The agent chooses after the predictor has made the prediction and the contents have been fixed. Suppose the predictor is correct with probability 0.99.

EDT computes:

\[
\begin{aligned}
V(\text{take only B})
&=P(\text{1M in B}\mid\text{take only B})\cdot \$1{,}000{,}000 \\
&\quad + P(\text{nothing in B}\mid\text{take only B})\cdot \$0 \\
&=0.99\cdot \$1{,}000{,}000 + 0.01\cdot \$0 \\
&=\$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{take both})
&=P(\text{1M in B}\mid\text{take both})\cdot \$1{,}001{,}000 \\
&\quad + P(\text{nothing in B}\mid\text{take both})\cdot \$1{,}000 \\
&=0.01\cdot \$1{,}001{,}000 + 0.99\cdot \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Since \(\$990{,}000 > \$11{,}000\), EDT recommends taking only box B.

The reasoning is direct: one-boxing is strong evidence that the predictor predicted one-boxing, so it is strong evidence that box B contains the million. Two-boxing is strong evidence that the predictor predicted two-boxing, so it is strong evidence that box B is empty.

CDT, by contrast, reasons that the contents of box B are already fixed. Whether I take both boxes or only one, the million is either there or not. Taking both boxes adds \$1,000 in either state. So CDT recommends two-boxing. The reference article notes this contrast: EDT one-boxes; CDT two-boxes.

One useful elaboration is to ask how accurate the predictor must be for EDT to one-box. Let \(p\) be the probability that the predictor predicts one-boxing if the agent one-boxes, and also the probability that it predicts two-boxing if the agent two-boxes. EDT one-boxes when

\[
p\cdot 1{,}000{,}000 > (1-p)\cdot 1{,}001{,}000 + p\cdot 1{,}000.
\]

This inequality is satisfied once \(p\) is only slightly above \(1/2\). Thus EDT does not need a perfect predictor; even modest predictive reliability can suffice.

---

## 5. Twin prisoner’s dilemma

The reference article also discusses a twin prisoner’s dilemma. Aomame and her psychological twin are in separate rooms. They cannot communicate. Their reasoning processes are exactly analogous. Payoffs are:

- both cooperate: each gets \$5;
- both defect: each gets \$1;
- one cooperates and the other defects: cooperator gets \$0, defector gets \$10.

If Aomame’s decision process is sufficiently similar to her twin’s, then Aomame’s choice is strong evidence about her twin’s choice. In the idealized case where the twins are guaranteed to make the same choice, EDT gives:

\[
\begin{aligned}
V(\text{cooperate})
&=P(\text{twin cooperates}\mid\text{Aomame cooperates})\cdot \$5 \\
&\quad + P(\text{twin defects}\mid\text{Aomame cooperates})\cdot \$0 \\
&=1\cdot \$5 + 0\cdot \$0 \\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{defect})
&=P(\text{twin cooperates}\mid\text{Aomame defects})\cdot \$10 \\
&\quad + P(\text{twin defects}\mid\text{Aomame defects})\cdot \$1 \\
&=0\cdot \$10 + 1\cdot \$1 \\
&=\$1.
\end{aligned}
\]

EDT therefore recommends cooperation.

The example is important because it shows that EDT can recommend cooperation in prisoner’s-dilemma-like cases when the agents are correlated. Aomame’s cooperation does not causally force her twin to cooperate. But if they are psychologically identical, or sufficiently similar, her cooperation is excellent evidence that her twin will also cooperate.

A more general version helps clarify how to apply EDT in unfamiliar cases. Let

\[
p=P(\text{twin cooperates}\mid\text{Aomame cooperates})
\]

and

\[
q=P(\text{twin cooperates}\mid\text{Aomame defects}).
\]

Then

\[
V(\text{cooperate})=5p,
\]

and

\[
V(\text{defect})=10q+1(1-q)=1+9q.
\]

EDT recommends cooperation exactly when

\[
5p > 1+9q.
\]

In the perfectly correlated case, \(p=1\) and \(q=0\), so cooperation wins easily. If the twins’ choices are independent, then \(p=q\), and defecting wins, because \(5p < 1+9p\). The example therefore illustrates a general lesson: EDT’s recommendation depends on the strength and structure of the evidential dependence.

---

## 6. A cautionary example: the smoking lesion

The supplied reference does not discuss the smoking lesion problem, but it is a standard illustration of why many philosophers dislike EDT. Suppose smoking does not cause cancer. However, some lesion causes both cancer and a disposition to smoke. Smoking is therefore evidence of cancer.

Imagine the following simplified numbers. Smoking gives \$1 worth of pleasure. Cancer imposes a loss of \$10. Smoking has no causal effect on cancer. But because of the lesion, suppose

\[
P(\text{cancer}\mid\text{smoke})=0.9,
\]

while

\[
P(\text{cancer}\mid\text{do not smoke})=0.1.
\]

Then EDT evaluates smoking as follows:

\[
V(\text{smoke})=0.9(-10+1)+0.1(1)=0.9(-9)+0.1=-8.0.
\]

Not smoking gives:

\[
V(\text{do not smoke})=0.1(-10)+0.9(0)=-1.0.
\]

So EDT recommends not smoking, even though smoking does not cause cancer and brings a small pleasure. CDT, if it accepts that smoking has no causal effect on cancer, recommends smoking because it adds pleasure without worsening the agent’s physical prospects.

This example is not in the source, but it clarifies the philosophical dispute. Critics say EDT recommends avoiding bad news rather than improving the world. Defenders may reply that EDT simply maximizes expected value relative to the agent’s evidence; if the action is strong evidence of a bad state, then the action’s news value is bad. Whether that is a feature or a bug is one of the central debates between EDT and CDT.

---

## 7. Policies, plans, and sequential decisions

The reference article presents EDT as evaluating actions. But many decision problems concern policies: rules for acting over time, or commitments that other agents and predictors may anticipate. A natural extension, which I take to be consistent with EDT’s core idea, is to evaluate a policy \(\pi\) by the expected utility conditional on the agent following \(\pi\):

\[
V(\pi)=\sum_j P(O_j\mid \pi)D(O_j).
\]

Here \(\pi\) might be “always cooperate with agents who use my decision procedure,” “one-box whenever faced with a Newcomb predictor,” or “use a randomized strategy with probability \(r\).” Conditioning on \(\pi\) means asking how good the news would be that I am the kind of agent who follows that policy.

This extension matters because predictors, twin agents, and correlated decision-makers often respond not to an isolated action but to an agent’s general policy. If a predictor can predict my policy, then the news that I have adopted a certain policy may be strong evidence about the state of the world. EDT can therefore recommend choosing or precommitting to a policy with high news value.

Sequential decisions introduce a subtle distinction. If the agent cannot precommit, then at a later decision node it may have to choose an action conditional on the history so far. At history \(h\), EDT would evaluate available actions \(A\) by

\[
V(A\mid h)=\sum_j P(O_j\mid h,A)D(O_j).
\]

But the agent’s future choices may themselves be chosen evidentially, and this should be included in the conditional model. If the agent can bind its future behavior, EDT may recommend selecting the best policy in advance. If it cannot, EDT must evaluate the action available now while accounting for the future decision procedure the agent expects to use. The supplied source does not settle these dynamic questions, so this policy-based formulation should be understood as an operational elaboration rather than a claim explicitly made by the reference.

---

## 8. Open questions and operational interpretation

EDT is formally simple, but applying it carefully raises several questions.

First, what probabilities should be conditioned on? EDT uses the agent’s prior evidence plus the hypothetical news that the action is performed. It should not condition on later observations that the agent would receive only after acting, unless those observations are part of the outcome being evaluated. The relevant conditioning event is “the agent performs \(A\),” not “the agent performs \(A\) and later sees some further evidence,” unless the decision problem explicitly includes that later evidence.

Second, what if the agent assigns probability zero to some action? If the agent is certain it will not take \(A\), then \(P(A)=0\), and \(P(O\mid A)\) is undefined in the elementary ratio definition. A reasonable operational interpretation is to require that all live options have positive probability in the agent’s deliberative state. If the agent is computationally uncertain about what its own reasoning will output, it can assign nonzero probabilities to possible outputs. If the action is logically determined by the agent’s algorithm, EDT may need a theory of logical uncertainty or a regular conditional probability construction. Without some such move, EDT can be underdetermined in cases where the agent is fully certain of its own future action.

Third, how should EDT handle self-locating uncertainty? The reference article mentions the Sleeping Beauty problem. It says EDT has been used to avoid Dutch books against certain positions, but also notes Vincent Conitzer’s argument that halfers may still be vulnerable to Dutch books even after adopting EDT (Conitzer 2015). The issue is unresolved in the source.

An operational EDT approach to Sleeping Beauty would treat Beauty’s choice as occurring at a centered moment: “I am now awake and being offered this action.” One would then compute the expected utility conditional on that centered proposition and on the available action. For example, if Beauty is offered a bet on heads, EDT would ask: conditional on my current awakening and on accepting or rejecting the bet, what is the expected payoff? But the answer depends on how one models the reference class of awakenings, the betting protocol, and whether repeated awakenings create multiple opportunities. The source leaves this disputed, so EDT’s correct application to Sleeping Beauty remains partly a matter of additional modeling assumptions.

Fourth, EDT must decide what counts as an “action.” If actions can be described at different levels of detail, the conditional probabilities may change. For example, “smoke” and “smoke because of a lesion” are not the same proposition. EDT should evaluate the propositions that are genuinely available to the agent’s choice. This is a common issue in decision theory, not unique to EDT, but it is especially important here because EDT is sensitive to how actions are described.

---

## 9. Philosophical motivation and criticism

The philosophical appeal of EDT is that it takes evidence seriously. Rational agents should act on their probabilities and utilities. If an action is strong evidence that desirable outcomes obtain, then conditional expected utility can be high. EDT generalizes the idea that a rational agent should prefer good news to bad news.

The reference article cites David Lewis’s criticism that EDT promotes “an irrational policy of managing the news,” and James Joyce’s claim that rational agents choose acts on the basis of their “causal efficacy,” not their “auspiciousness” (Lewis 1981; Joyce 1999). These objections capture the intuitive worry: if I can make the world better by acting, why should I care whether my action is merely a sign of good things? Why choose an action that is good news but does no good?

EDT’s defenders may respond that in many cases the distinction is less clear than CDT assumes. If my decision procedure is predictable, or if many agents reason similarly, then my action can be evidence about what others will do. In such cases, choosing the action with high news value can coordinate behavior, support cooperation, and produce better outcomes in expectation.

The reference article mentions an argument sometimes called the evidentialist’s wager: even if one is not fully confident in EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, making the stakes potentially higher than under CDT (MacAskill et al. 2021). The idea is that if many agents use similar reasoning, my choice may be evidence about their choices. If cooperation among many agents has enormous value, then the evidential stakes can dominate. This argument is not a proof of EDT, but it gives a practical reason to take EDT seriously in contexts involving large-scale correlation.

Still, the smoking-lesion style objection remains powerful. If EDT tells us not to smoke merely because smoking is evidence of cancer, many people feel that EDT has confused signs with causes. The debate between EDT and CDT is therefore not merely technical; it concerns what decision theory is for. Is decision theory supposed to choose the action that would be best news, or the action that would best manipulate the world?

---

## 10. How to apply EDT in practice

A reader wanting to apply EDT to an unfamiliar case can use the following procedure.

1. **List the available actions or policies.** Make them mutually exclusive and decision-relevant.

2. **Identify the outcomes or states that matter.** Include anything the agent cares about: money, welfare, health, intrinsic features of the action, and effects on others.

3. **Assign utilities.** Let \(D(O_j)\) or \(U(A,S_k)\) represent the desirability of each outcome or action-state pair.

4. **Model the probabilistic dependencies.** Include predictors, correlated agents, common causes, selection effects, and self-locating information. EDT does not require these dependencies to be causal.

5. **Condition on each action or policy.** Compute \(P(O_j\mid A)\), or \(P(S_k\mid A)\), using the agent’s prior probabilities updated on the news that the action is performed.

6. **Compute EDT values.** Use

   \[
   V(A)=\sum_j P(O_j\mid A)D(O_j)
   \]

   or

   \[
   V(A)=\sum_k P(S_k\mid A)U(A,S_k).
   \]

7. **Choose the action or policy with maximal EDT value.** If policies are available and can be adopted, evaluate them by conditioning on the policy as a whole.

This procedure is simple, but its correctness depends heavily on step 4. The hard work in EDT usually lies not in the arithmetic of expected utility, but in constructing a reasonable probability model of the evidential dependencies.

---

## Conclusion

Evidential decision theory says: choose the action that would be the best news about yourself. Its formal core is conditional expected utility:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This rule is easy to state and often easy to apply, but it has controversial implications. In Newcomb’s problem, EDT one-boxes because one-boxing is evidence that the predictor filled the opaque box with a million dollars. In the twin prisoner’s dilemma, EDT cooperates because cooperation is evidence that the twin will cooperate. In smoking-lesion cases, EDT may avoid an action that is merely evidence of a bad outcome, which is why critics accuse EDT of managing the news rather than causing good outcomes.

The theory’s strength is its direct treatment of evidential dependence. Its weakness is that it does not distinguish between causing a good outcome and merely being a sign of one. Whether that distinction should matter is the central divide between evidential and causal decision theory. For the mathematically literate reader, EDT is best understood not as a mere formula but as a commitment: in choice, the evidential significance of an action is not a side effect to be ignored; it is part of the action’s expected value.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, no. 9 (2015): 2887–2899.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976/1978.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026.