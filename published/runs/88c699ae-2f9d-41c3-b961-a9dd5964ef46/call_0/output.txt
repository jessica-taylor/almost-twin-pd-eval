# Evidential Decision Theory: Choosing the Best News

Evidential decision theory, or EDT, is a proposal about how a rational agent should choose among available actions when the outcomes are uncertain. Its central idea is compact and memorable: choose the action that would be the best news to learn that you had chosen. The reference article summarizes this by saying that EDT recommends selecting the action with the highest *news value*, i.e. the action that would be indicative of the best outcome in expectation if one received the news that it had been taken. In Allan Gibbard and William Harper’s terminology, EDT maximizes expected utility computed with ordinary conditional probabilities rather than with interventionist or counterfactual probabilities.

This essay explains the formal rule, shows how it applies to standard examples such as Newcomb’s problem and the twin prisoner’s dilemma, and discusses how EDT treats dependencies, counterfactuals, and policies. I will also point out places where the source material is incomplete, especially concerning zero-probability actions, sequential policies, and self-locating cases such as Sleeping Beauty. Where useful, I will offer operational interpretations of my own, clearly separated from the claims made in the reference article.

---

## 1. The basic formal rule

Suppose an agent faces a finite set of possible actions

\[
\mathcal A = \{A_1,\dots,A_n\}.
\]

Let \(O_1,\dots,O_m\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The agent has a subjective probability function \(P\), representing her credences over propositions about actions, states of the world, and outcomes.

The reference article gives the EDT value of an action \(A\) as

\[
V(A)=\sum_{j} P(O_j \mid A) D(O_j),
\]

where \(P(O_j \mid A)\) is the conditional probability of outcome \(O_j\) given that action \(A\) is performed. EDT then recommends choosing an action \(A^*\) such that

\[
A^* \in \arg\max_{A \in \mathcal A} V(A).
\]

Equivalently, EDT says: maximize the conditional expected desirability of the news that you performed \(A\). In expectation notation,

\[
V(A) = \mathbb E_P[D(O) \mid A].
\]

If outcomes are continuous, the sum is replaced by an integral; if the relevant space is more fine-grained, one may use a regular conditional expectation. The essential idea remains the same: the value of an act is the expected utility conditional on the proposition that the act occurs.

A useful alternative formulation uses states of the world. Let \(S_1,\dots,S_k\) be a partition of relevant states, and let \(u(A,S_i)\) be the utility of performing \(A\) in state \(S_i\). Then EDT evaluates

\[
V(A)=\sum_i P(S_i \mid A) u(A,S_i).
\]

By Bayes’ theorem,

\[
P(S_i \mid A)
=
\frac{P(A \mid S_i)P(S_i)}{P(A)},
\]

assuming \(P(A)>0\). This makes clear how EDT uses dependencies: the probability of a state after conditioning on an action depends on how likely that action is in that state. If actions are probabilistically independent of the states, then \(P(S_i \mid A)=P(S_i)\), and EDT reduces to ordinary expected utility with respect to the prior. EDT becomes distinctive precisely when the agent’s action is probabilistically correlated with relevant states of the world.

---

## 2. EDT and counterfactuals

The reference article contrasts EDT with causal decision theory, or CDT. Gibbard and Harper distinguished two expected-utility formulas. EDT uses

\[
V(A)=\sum_j P(O_j \mid A)D(O_j),
\]

whereas CDT uses a counterfactual formula,

\[
U(A)=\sum_j P(A \mathbin{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathbin{\Box\rightarrow} O_j\) means something like “if \(A\) were performed, \(O_j\) would obtain.” In modern causal notation, one might write CDT’s object as something close to

\[
U(A) \approx \mathbb E[D(O) \mid do(A)],
\]

where \(do(A)\) represents an intervention that sets the action to \(A\). EDT instead uses ordinary conditioning:

\[
V(A) = \mathbb E[D(O) \mid A].
\]

The difference is crucial. Conditioning treats the action as evidence about the world. Intervention treats the action as something brought about by choice, while holding fixed the relevant causal background. In graphical terms, conditioning on \(A\) allows information to flow along probabilistic dependencies into and out of \(A\). Intervening on \(A\) cuts the incoming causal arrows: it asks what would happen if \(A\) were imposed from outside.

The source’s slogan “do what you most want to learn that you will do” captures this nicely. EDT does not primarily ask, “Which action would causally produce the best outcome?” It asks, “Which action, regarded as news, is associated with the best expected outcome?”

One can give this a more operational interpretation, though this is an elaboration rather than a detailed claim in the source. Imagine that before acting, the agent receives a reliable message saying, “You will perform \(A\).” If the agent updates by strict conditionalization, her new probability for outcome \(O_j\) becomes \(P(O_j \mid A)\). The expected utility after receiving that message is exactly \(V(A)\). EDT then says to choose the action whose associated message would be most welcome. This “hypothetical news” interpretation is a natural way to understand EDT’s use of conditional probability.

---

## 3. Newcomb’s problem

The reference article discusses Newcomb’s paradox, a classic case where EDT and CDT diverge.

A highly reliable predictor has already made a prediction about whether the agent will take only box B or both boxes A and B. Box A is transparent and contains \$1,000. Box B is opaque. If the predictor predicted that the agent will take only B, it placed \$1,000,000 in B. If it predicted that the agent will take both boxes, it left B empty. The predictor is, say, 99% accurate.

The agent can choose:

1. Take only B.
2. Take both A and B.

EDT computes conditional expected utilities. Using the source’s numbers:

\[
\begin{aligned}
V(\text{take only B})
&= P(\text{\$1M in B} \mid \text{take only B}) \cdot \$1{,}000{,}000 \\
&\quad + P(\text{B empty} \mid \text{take only B}) \cdot \$0 \\
&= 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0 \\
&= \$990{,}000.
\end{aligned}
\]

For taking both boxes:

\[
\begin{aligned}
V(\text{take both})
&= P(\text{\$1M in B} \mid \text{take both}) \cdot \$1{,}001{,}000 \\
&\quad + P(\text{B empty} \mid \text{take both}) \cdot \$1{,}000 \\
&= 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000 \\
&= \$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{take only B}) > V(\text{take both}),
\]

EDT recommends one-boxing.

The reasoning is evidential. Taking only B is strong evidence that the predictor predicted one-boxing, and therefore that B contains \$1,000,000. Taking both boxes is strong evidence that the predictor predicted two-boxing, and therefore that B is empty. EDT does not require the agent’s present choice to causally influence the predictor’s past prediction. It only requires that the choice be good evidence about the prediction.

CDT, by contrast, says that the contents of B are already fixed. Taking both boxes causally adds \$1,000 to whatever is already in B. So CDT recommends two-boxing.

It is useful to generalize the Newcomb calculation. Suppose the predictor’s conditional accuracy is \(p\), so that

\[
P(\text{\$1M in B} \mid \text{one-box}) = p
\]

and

\[
P(\text{B empty} \mid \text{two-box}) = p.
\]

Then

\[
V(\text{one-box}) = p \cdot \$1{,}000{,}000,
\]

while

\[
V(\text{two-box})
=
(1-p)\cdot \$1{,}001{,}000 + p \cdot \$1{,}000.
\]

One-boxing is favored when

\[
p \cdot \$1{,}000{,}000
>
(1-p)\cdot \$1{,}001{,}000 + p \cdot \$1{,}000.
\]

Solving gives

\[
p > \frac{1{,}001{,}000}{2{,}000{,}000}
= 0.5005.
\]

Thus, under these symmetric assumptions, EDT recommends one-boxing whenever the predictor is even slightly better than chance in the relevant conditional sense. This illustrates how EDT can be applied to unfamiliar variants: specify the conditional probabilities, multiply by utilities, and compare.

---

## 4. The twin prisoner’s dilemma

The reference article also discusses a variant of the prisoner’s dilemma involving psychological twins. Aomame and her twin are separated and cannot communicate. Their reasoning processes are exactly analogous. Each chooses cooperation or defection. Payoffs to Aomame are:

- Both cooperate: Aomame gets \$5.
- Both defect: Aomame gets \$1.
- Aomame cooperates, twin defects: Aomame gets \$0.
- Aomame defects, twin cooperates: Aomame gets \$10.

Because the twins reason in exactly the same way, Aomame’s choice is taken to be perfectly correlated with her twin’s choice. The source gives:

\[
P(\text{twin cooperates} \mid \text{Aomame cooperates}) = 1,
\]

and

\[
P(\text{twin defects} \mid \text{Aomame defects}) = 1.
\]

Therefore,

\[
\begin{aligned}
V(\text{Aomame cooperates})
&= 1 \cdot \$5 + 0 \cdot \$0 \\
&= \$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{Aomame defects})
&= 0 \cdot \$10 + 1 \cdot \$1 \\
&= \$1.
\end{aligned}
\]

EDT recommends cooperation.

Again, the point is not that Aomame causally controls her twin’s choice. The point is that her choice is strong evidence about her twin’s choice. If she learns, as it were, that she will cooperate, she should also expect her twin to cooperate. If she learns that she will defect, she should expect her twin to defect.

A more general version helps clarify the evidential structure. Suppose the correlation is imperfect. Let

\[
q = P(\text{twin cooperates} \mid \text{Aomame cooperates})
\]

and, symmetrically,

\[
q = P(\text{twin defects} \mid \text{Aomame defects}).
\]

Then

\[
V(C) = 5q,
\]

and

\[
V(D) = 10(1-q) + 1q = 10 - 9q.
\]

Cooperation is favored when

\[
5q > 10 - 9q,
\]

so

\[
14q > 10,
\]

or

\[
q > \frac{5}{7} \approx 0.714.
\]

Thus EDT recommends cooperation if Aomame’s choice is sufficiently diagnostic of her twin’s choice. In the exact-twin case, \(q=1\), so cooperation is strongly favored.

---

## 5. Dependencies: causal, common-cause, and logical

EDT does not distinguish, at the formal level, between different sources of probabilistic dependence. It uses whatever conditional probabilities the agent assigns. This is both its appeal and the source of many objections.

There are several ways in which an action may be probabilistically correlated with an outcome.

First, the action may causally affect the outcome. In ordinary cases, EDT and CDT often agree. If taking medicine causes recovery, then conditioning on taking medicine will normally raise the probability of recovery, and both EDT and CDT may recommend taking the medicine.

Second, the action may be correlated with an outcome through a common cause. Suppose some underlying condition causes both a certain choice and a certain outcome. Conditioning on the choice then provides evidence about the underlying condition. EDT responds to that evidence; CDT does not, if the choice does not causally affect the outcome.

Third, the dependence may be logical, mathematical, or algorithmic. If two agents run similar decision procedures, one agent’s choice may be evidence about the other’s choice even without causal interaction. The twin prisoner’s dilemma is an example. Some interpretations of Newcomb’s problem also appeal to this kind of dependence: the predictor has modeled the agent’s decision procedure, so the agent’s actual choice is evidence about what the predictor concluded.

To see why critics worry about EDT, consider a case not discussed in the source: a smoking-lesion style example. Suppose a genetic lesion causes both a strong desire to smoke and a high risk of cancer. Smoking itself does not cause cancer, but smoking is evidence of the lesion. Suppose smoking gives one unit of pleasure, while cancer imposes a utility loss of ten units. If the lesion causes cancer regardless of whether one smokes, then smoking is better than not smoking in every causal state: if one has the lesion, smoking gives slightly more utility than not smoking; if one lacks the lesion, smoking also gives slightly more utility than not smoking.

Nevertheless, EDT may recommend not smoking. If

\[
P(\text{lesion} \mid \text{smoke}) = 0.9
\]

and

\[
P(\text{lesion} \mid \text{do not smoke}) = 0.1,
\]

then, using utilities where smoking with lesion gives \(-9\), not smoking with lesion gives \(-10\), smoking without lesion gives \(+1\), and not smoking without lesion gives \(0\), we get

\[
V(\text{smoke}) = 0.9(-9) + 0.1(1) = -8,
\]

while

\[
V(\text{do not smoke}) = 0.9(0) + 0.1(-10) = -1.
\]

EDT says do not smoke, because smoking is bad news. CDT says smoke, because smoking does not cause cancer and gives a small benefit in every state. This example is not in the reference article, but it illustrates the philosophical stakes: EDT can favor an action that is evidentially auspicious even when another action is causally dominant.

---

## 6. Policies, sequential choice, and precommitment

The source mainly presents EDT as a theory of individual acts. But many decision problems ask us to evaluate policies: plans, algorithms, or strategies that specify what to do over time or across circumstances.

A natural EDT extension is to treat a policy \(\pi\) as a proposition: “the agent implements policy \(\pi\).” Then define

\[
V(\pi) = \sum_j P(O_j \mid \pi)D(O_j).
\]

The agent should choose the policy with maximum \(V(\pi)\). This is especially relevant when agents are correlated. If many agents use similar policies, conditioning on your policy may provide evidence about their policies and therefore about the outcome.

In sequential problems, one must be careful. Suppose an agent chooses an action \(a\) at an early history \(h\), and later choices will depend on what happens afterward. If the agent can genuinely choose a full policy in advance, EDT should probably evaluate the full policy rather than each momentary action in isolation. Otherwise, EDT may become dynamically inconsistent: the action that looks best at a later node, conditional on being at that node, may differ from the policy that looked best ex ante.

The reference article does not settle this issue. A reasonable operational interpretation, which I propose rather than find in the source, is this: evaluate the most specific object over which the agent has effective control. If the agent can precommit to a policy, evaluate the policy as a whole. If the agent cannot precommit and will reassess later, evaluate a current action together with the continuation policy the agent expects to follow. Formally, if \(\pi\) is the continuation policy, one might evaluate

\[
V_h(a,\pi)
=
\mathbb E[D(O) \mid h, a, \pi],
\]

rather than merely

\[
\mathbb E[D(O) \mid h, a].
\]

This preserves EDT’s evidential logic while reducing instability over time.

---

## 7. Zero-probability actions and conditional probabilities

Another issue left underdeveloped in the source is the status of conditional probabilities when \(P(A)=0\). The formula

\[
P(O_j \mid A)=\frac{P(O_j \land A)}{P(A)}
\]

requires \(P(A)>0\). But in deliberation, an agent may assign probability zero to some available actions, perhaps because she is psychologically certain she will not perform them. If so, EDT’s value for those actions is undefined under the simplest formula.

One operational response is to restrict EDT to actions with positive subjective probability. A more flexible response is to assign small positive probabilities to all live options, compute conditional expected utilities, and then examine the limiting behavior as those probabilities approach zero. If the ranking of actions is stable, the limiting values can serve as EDT verdicts. If the ranking depends on the path by which the limit is taken, the problem is underdetermined by the simple EDT formula.

A related issue is deliberative feedback. An EDT agent chooses by evaluating \(V(A)\), but her probability distribution may already encode expectations about which action she will choose. In self-referential problems, the probabilities can become endogenous. One possible refinement is to require *ratification*: an action \(A\) is ratifiable if, conditional on performing \(A\), it still has maximal EDT value among the available actions. Ratification is not mentioned in the source, but it is a natural way to handle cases where the agent’s decision rule is itself part of the evidence.

---

## 8. Sleeping Beauty and self-locating evidence

The reference article briefly mentions the Sleeping Beauty problem. It says EDT has been applied there to avoid Dutch-book arguments, but also notes that Vincent Conitzer has argued that halfers can still be Dutch-booked even after adopting EDT.

This is an important caution. EDT tells an agent to condition on actions, but in problems involving indexical uncertainty—uncertainty about who one is, where one is, or when one is—one must first decide how to represent centered propositions and how to assign probabilities over them. In Sleeping Beauty, for example, Beauty must reason about awakenings after a coin toss. Whether she should assign credence \(1/2\) or \(1/3\) to heads depends on disputed principles of self-locating belief. EDT by itself does not settle that dispute. It can only evaluate actions once the relevant conditional probabilities have been specified.

Thus, for self-locating cases, EDT should be treated as a decision rule applied after an account of centered evidence is supplied. The source’s remark about Dutch books should be read as reporting a contested argument, not as a settled theorem that EDT resolves Sleeping Beauty.

---

## 9. The evidentialist’s wager and correlated decision-makers

The source mentions a supporting argument associated with MacAskill, Valliner, Österheld, Shulman, and Treutlein: even if one is not fully confident in EDT, it may be reasonable to act as if EDT were true because EDT can involve the actions of many correlated decision-makers, and therefore its stakes may be higher than those of CDT.

The idea is that if many agents face structurally similar decisions, your choice may be evidence about their choices. If EDT is correct, then choosing an EDT-recommended action may correlate with beneficial behavior by many other agents. If the number of affected agents is large, the expected stakes of EDT-sensitive decisions can be enormous. So even a modest credence in EDT might make it pragmatically attractive to follow EDT in certain high-correlation settings.

This argument is suggestive but controversial. It does not show that EDT is true as a theory of rational choice; it only gives a possible reason to act as if EDT were true under some empirical and decision-theoretic assumptions. I mention it because it illustrates how EDT’s treatment of correlations can have large practical implications beyond single-agent toy cases.

---

## 10. Criticism: managing news versus causing outcomes

The reference article includes two important criticisms. David Lewis characterized EDT as promoting “an irrational policy of managing the news.” James Joyce wrote that rational agents choose acts on the basis of their causal efficacy, not their auspiciousness; they act to bring about good results even when doing so might betoken bad news.

These criticisms identify the central philosophical dispute. EDT treats actions partly as symptoms or signs. If an action is correlated with a good outcome, EDT counts that in the action’s favor. But one might think that rational action should be about control: what will happen because of what I do, not merely what is likely to be true given that I do it.

Defenders of EDT can respond in several ways. In Newcomb’s problem, one-boxing leads to the better outcome if the predictor is reliable, so EDT is practically successful in that case. More broadly, if an agent’s decision procedure is predictable or correlated with others’ decision procedures, evidential correlations may track real structure in the world. Ignoring them, EDT advocates argue, can lead to leaving large benefits on the table.

Critics can reply that EDT succeeds in Newcomb only by accident of the predictor’s setup, while failing in cases like the smoking lesion, where it recommends avoiding an action that is beneficial in every causal state. The debate therefore depends on deeper views about causation, counterfactuals, and the proper role of probability in decision-making.

---

## Conclusion

Evidential decision theory has a simple formal core: choose the action that maximizes conditional expected utility,

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

It treats actions as evidence, not merely as interventions. This leads it to one-box in Newcomb’s problem and to cooperate in twin prisoner’s dilemmas, because in those cases the action is strongly diagnostic of favorable background states or correlated choices. It also leads to controversial recommendations in cases where actions are merely symptomatic of underlying conditions.

To apply EDT to unfamiliar cases, one should specify the actions, outcomes, utilities, and joint probabilities; compute the conditional probabilities of outcomes given each action; and choose the action with the highest conditional expected utility. For policies, one should condition on the policy as a whole. For zero-probability actions and self-locating problems, additional care is needed, and the source leaves significant questions open. Operational remedies—small positive probabilities, regular conditional distributions, ratification, and global policy evaluation—are plausible extensions, but they are not settled by the basic EDT formula alone.

EDT remains philosophically contested because it separates the question “What would be good news?” from the question “What would causally bring about good outcomes?” Whether that separation is a defect or a clarification is the central issue between evidential and causal decision theory.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” *Wikipedia*, revision 1373679688, 2026.