# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a theory of rational choice under uncertainty. Its central idea is simple but philosophically provocative: when choosing among possible actions, an agent should choose the action that would be *best news* to learn that she had chosen. In the words quoted in the reference article, EDT recommends doing “what you most want to learn that you will do” (Ahmed, 2021, p. 7). The theory therefore evaluates actions by their *evidential* bearing on desirable outcomes, not by their alleged causal power to bring those outcomes about.

This essay explains the formal core of EDT, shows how it is applied to decision problems, and discusses how it treats dependencies, policies, and counterfactual reasoning. The reference article supplies the basic expected-utility formula, the contrast with causal decision theory, and the standard examples of Newcomb’s paradox and a twin prisoner’s dilemma. It leaves several operational questions open, including how to treat zero-probability actions, how to evaluate policies rather than one-shot acts, and how to specify the probability model. Where those questions arise, I propose and justify operational interpretations, marking them as additions rather than claims of the source.

---

## 1. The basic formal rule

Suppose an agent faces a finite set of possible actions

\[
\mathcal{A}=\{A_1,\dots,A_n\}.
\]

Let the possible outcomes be a mutually exclusive and exhaustive partition

\[
\{O_1,\dots,O_m\}.
\]

Each outcome has a desirability, or utility,

\[
D(O_j)\in \mathbb{R}.
\]

The agent has a probability function \(P\) representing her credences over propositions involving actions, states of the world, and outcomes. EDT assigns to each action \(A\) its *evidential expected utility* or *news value*:

\[
V(A)=\sum_{j=1}^{m} P(O_j \mid A)\,D(O_j).
\]

The EDT choice rule is:

\[
\text{Choose } A^* \in \arg\max_{A\in\mathcal{A}} V(A).
\]

The expression \(P(O_j\mid A)\) is an ordinary conditional probability: the probability the agent would assign to outcome \(O_j\) upon learning that action \(A\) has been performed. EDT thus asks: if I received the news “I did \(A\),” how much expected value would that news carry?

This is the formula given in the reference article, attributed to Gibbard and Harper (1976):

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

It is useful to compare EDT with the counterfactual expected utility formula associated with causal decision theory (CDT):

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A\mathrel{\Box\rightarrow}O_j\) is read as “if \(A\) were performed, \(O_j\) would obtain.” In modern causal language, one often writes this as something like

\[
U(A)=\sum_j P(O_j\mid do(A))D(O_j),
\]

where \(do(A)\) denotes an intervention that sets the action to \(A\), rather than merely conditioning on the news that \(A\) occurred. The reference article uses the counterfactual notation, and I will follow that distinction: EDT uses conditional probabilities; CDT uses counterfactual or interventionist probabilities.

When the two probability expressions coincide, EDT and CDT agree. They tend to agree in ordinary decisions where the action is not correlated with relevant background states except through the action’s own causal consequences. They diverge when the action is evidence for some outcome-producing state of the world, even if the action does not causally affect that state.

---

## 2. An operational procedure for EDT

The reference article gives the central formula but not a full recipe for applying it to unfamiliar cases. A reasonable operational procedure, which I take to be a straightforward elaboration of the source’s formal description, is the following.

1. **Specify the alternatives.** List the actions or policies under consideration. These should be distinct, well-defined propositions such as “I take both boxes” or “I follow policy \(\pi\).”

2. **Specify outcomes and utilities.** Choose a partition of outcomes over which the agent has desirabilities \(D(O_j)\). If the agent cares about multiple features—money, health, reputation, fairness—these should be incorporated into the outcome description or into the utility function.

3. **Specify the agent’s probability model.** Assign probabilities to the relevant joint propositions involving actions, states, and outcomes. The model should encode the agent’s beliefs about causal structure, predictors, correlations, psychological similarity, and any other dependency she regards as credible.

4. **Compute conditional outcome probabilities.** For each action \(A\), compute

   \[
   P(O_j\mid A)=\frac{P(O_j\land A)}{P(A)}
   \]

   whenever \(P(A)>0\). If there are hidden state variables \(S\), one may compute

   \[
   P(O_j\mid A)=\sum_s P(O_j\mid A,S=s)P(S=s\mid A).
   \]

5. **Compute news value.** Evaluate

   \[
   V(A)=\sum_j P(O_j\mid A)D(O_j).
   \]

6. **Choose an action with maximal news value.** If several actions tie, EDT is indifferent among them unless further tie-breaking criteria are supplied.

This procedure makes clear that EDT is not a separate probability calculus. It is ordinary Bayesian decision theory using conditional expected utility. The controversial issue is whether conditional probability is the right representation of the decision-relevant “what would happen if I did \(A\)?” question.

---

## 3. What counts as a relevant dependency?

EDT’s distinctive feature is that it allows any probabilistic dependency in the agent’s model to influence the evaluation of an action. If \(A\) is evidence for \(O_j\), then \(P(O_j\mid A)\) differs from the unconditional \(P(O_j)\), and that difference affects \(V(A)\).

The dependency may arise in several ways.

First, \(A\) may cause \(O_j\). If taking medicine causes recovery, then learning that I took the medicine raises the probability of recovery. EDT and CDT will typically agree here.

Second, \(O_j\) or a cause of \(O_j\) may cause or predict \(A\). If a reliable predictor predicted that I would one-box, then the box contains a million dollars; my one-boxing is evidence that the predictor made that prediction. EDT uses this dependency.

Third, \(A\) and \(O_j\) may share a common cause. If a genetic lesion both causes a preference for smoking and causes cancer, then smoking is evidence for the lesion and hence for cancer. EDT may treat smoking as bad news even if smoking does not cause cancer. This kind of case is often used to criticize EDT, though it is not discussed in the supplied source.

Fourth, the dependency may be logical, mathematical, or psychological rather than straightforwardly causal. If another agent is my psychological twin and reasons exactly as I do, then my cooperation is evidence that the twin cooperates. The reference article’s twin prisoner’s dilemma is of this kind.

EDT does not itself ask whether the dependency is causal. It asks only what the agent should expect conditional on the news that a given action was performed. That is why David Lewis criticized EDT as “an irrational policy of managing the news” and why James Joyce says rational agents act on the basis of “causal efficacy, not their auspiciousness” (Lewis, 1981; Joyce, 1999). From EDT’s perspective, however, if an action reliably indicates a good outcome, then choosing it is rational because it is the choice whose occurrence would be most desirable to learn.

---

## 4. Newcomb’s paradox

The reference article’s central example is Newcomb’s paradox. A player faces two boxes:

- Box A is transparent and contains \$1,000.
- Box B is opaque. Its contents were fixed earlier by a highly reliable predictor.
  - If the predictor predicted that the player would take both boxes, B contains nothing.
  - If the predictor predicted that the player would take only B, B contains \$1,000,000.

The player may take both boxes or only box B.

Let \(p=0.99\) be the predictor’s accuracy, interpreted symmetrically. Then EDT assigns:

\[
P(\text{\$1M in B}\mid \text{take only B})=0.99,
\]

and

\[
P(\text{\$1M in B}\mid \text{take both boxes})=0.01.
\]

The EDT values are:

\[
\begin{aligned}
V(\text{take only B})
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0\\
&=\$990{,}000.
\end{aligned}
\]

For taking both boxes, the payoff is \$1,001,000 if B contains the million, and \$1,000 if B is empty:

\[
\begin{aligned}
V(\text{take both boxes})
&=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000\\
&=\$10{,}010+\$990\\
&=\$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{take only B})>V(\text{take both boxes}),
\]

EDT recommends taking only box B.

The reasoning is explicitly evidential. One-boxing does not causally change the past prediction; the contents of box B are already fixed. But one-boxing is strong evidence that the predictor predicted one-boxing. Therefore, conditional on the news that I one-boxed, I should expect B to contain the million. Two-boxing is strong evidence that the predictor predicted two-boxing, so conditional on the news that I two-boxed, I should expect B to be empty.

It is instructive to generalize the calculation. Suppose the predictor is accurate with probability \(p\). Then one-boxing is better when

\[
p\cdot 1{,}000{,}000 > (1-p)\cdot 1{,}001{,}000 + p\cdot 1{,}000.
\]

Simplifying,

\[
1{,}000{,}000p > 1{,}001{,}000 - 1{,}000{,}000p,
\]

so

\[
2{,}000{,}000p > 1{,}001{,}000,
\]

and therefore

\[
p > 0.5005.
\]

Thus, even a predictor only slightly better than chance makes EDT one-box, given the payoff structure. This illustrates how EDT’s recommendation depends on the conditional probabilities encoded in the agent’s model.

---

## 5. Twin prisoner’s dilemma

The reference article also discusses a twin prisoner’s dilemma. Aomame and her psychological twin are in separate rooms and cannot communicate. Their reasoning processes are exactly analogous. The payoffs are:

- If both cooperate, each gets \$5.
- If both defect, each gets \$1.
- If one cooperates and the other defects, the defector gets \$10 and the cooperator gets \$0.

Aomame cares only about her own payoff.

If Aomame is exactly psychologically similar to her twin and reasons in the same way, EDT treats her choice as perfect evidence of the twin’s choice:

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then

\[
\begin{aligned}
V(\text{Aomame cooperates})
&=1\cdot \$5+0\cdot \$0\\
&=\$5,
\end{aligned}
\]

while

\[
\begin{aligned}
V(\text{Aomame defects})
&=0\cdot \$10+1\cdot \$1\\
&=\$1.
\end{aligned}
\]

EDT therefore recommends cooperation.

The source’s example uses perfect correlation, but imperfect correlation is often more realistic. Let

\[
p=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and

\[
q=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5p,
\]

while

\[
V(D)=10q+1(1-q)=1+9q.
\]

Cooperation is favored when

\[
5p>1+9q.
\]

This inequality makes explicit the evidential structure EDT exploits. Even if Aomame cannot causally influence her twin, her own choice may be strong evidence of the twin’s choice. EDT treats that evidential connection as decision-relevant.

This case also clarifies the difference between EDT and CDT. CDT asks what would happen if Aomame intervened to defect. If the twin’s choice is already fixed or causally independent of Aomame’s current choice, CDT may recommend defection because defecting yields \$10 instead of \$5 in the relevant counterfactual. EDT instead asks what Aomame should expect upon learning that she defected. If defection is strong evidence that the twin also defected, then the news value of defection is low.

---

## 6. Policies, sequential decisions, and dynamic choice

The reference article presents EDT as a theory evaluating actions. Many real decisions, however, involve policies: plans, rules, algorithms, or strategies mapping observations to actions. The article does not explicitly say how EDT evaluates policies. I propose the following natural extension.

A policy \(\pi\) can be treated as a higher-order action. The proposition “I adopt policy \(\pi\)” is then conditioned on just as an ordinary action is. The news value of \(\pi\) is

\[
V(\pi)=\sum_j P(O_j\mid \pi)D(O_j).
\]

Here \(P(O_j\mid \pi)\) is the probability of outcome \(O_j\) conditional on the news that the agent has adopted, or is following, policy \(\pi\). If policies are chosen in advance and the agent can meaningfully regard herself as uncertain about which policy she will adopt, this formula directly extends EDT to plans, algorithms, and commitments.

For sequential decisions, let \(h\) be the history observed so far. At history \(h\), EDT can evaluate available actions by conditionalizing on both the action and the history:

\[
V_h(a)=\sum_j P(O_j\mid a,h)D(O_j).
\]

The EDT action at \(h\) is then an action maximizing \(V_h(a)\).

There is a subtle question, not addressed in the source, about whether EDT should evaluate a whole policy ex ante or evaluate actions locally at each decision node. These can come apart. An ex ante policy may have high news value, while at some later node the locally best evidential action may differ. A plausible operational interpretation is this:

- If the agent can genuinely choose or precommit to a policy as a single object of choice, evaluate policies by their prior news value \(V(\pi)\).
- If the agent is making a local choice after observing history \(h\), evaluate actions by \(V_h(a)\).
- If the agent wants a dynamically consistent plan, she should prefer policies that she expects to ratify at later nodes, or she should model the choice of policy as including the future decision procedure itself.

This proposal is my own. The reference article does not settle dynamic EDT. But treating policies as actions to be conditioned on is the most direct extension of the theory’s central formula.

---

## 7. Zero-probability actions and hypothetical news

A serious operational difficulty arises when the agent is certain she will not perform some action. If \(P(A)=0\), the ordinary conditional probability \(P(O_j\mid A)\) is undefined. This problem is not unique to EDT, but it is especially important for decision theories because an agent evaluating alternative actions may already know, or strongly believe, what she will do.

The source does not discuss this. A reasonable operational interpretation is to use a regular conditional probability or a limiting procedure. One method is to introduce a small amount of uncertainty about the agent’s action. For example, replace the original probability function \(P\) with a perturbed function \(P_\varepsilon\) under which every available action has at least probability \(\varepsilon>0\). Then define

\[
P(O_j\mid A)=\lim_{\varepsilon\to 0}P_\varepsilon(O_j\mid A),
\]

when the limit exists.

This resembles a “trembling-hand” assumption: even if the agent is nearly certain what she will do, she evaluates alternatives by asking what would be indicated by a small-probability deviation. Another interpretation is that EDT’s conditional is not a conditional on an event with positive prior probability but a hypothetical update: what should I believe if I somehow learned that \(A\) had occurred? Jeffrey conditionalization, imaging, or subjective conditional probability systems can formalize such updates. The key point is that EDT needs a way to assign coherent hypothetical probabilities to alternative actions even when those alternatives are not expected to occur.

Without such a convention, EDT cannot evaluate deterministic agents who are certain of their own choices. With such a convention, EDT can be applied consistently, though the choice of regularization may matter in pathological cases.

---

## 8. What exactly is conditioned on?

Another open question is the proper description of the action proposition on which EDT conditionalizes. Should the agent condition only on the outward behavior, such as “I take box B,” or also on the reasons, intentions, or algorithm that produced the behavior?

The reference article’s examples condition on simple action descriptions: taking only B, taking both boxes, cooperating, defecting. This works when the action description captures all decision-relevant information. But in more complicated cases, the answer may depend on how actions are individuated.

A conservative operational rule is this: condition on the action or policy as it is available to choice, including any features of the decision procedure that the agent regards as uncertain and relevant. If motives or algorithms affect outcomes, they should be included either in the action/policy proposition or in the outcome/state description. One should avoid building the desired conclusion into the action description by conditioning on “I choose A for a good reason” unless that proposition is genuinely part of the alternative being evaluated.

This is not merely a technicality. EDT’s sensitivity to action descriptions is connected to criticisms that it encourages “managing the news.” If an agent can make a bad action look good by associating it with good news, EDT may appear to give perverse advice. Defenders of EDT can respond that rational conditionalization must be based on the agent’s genuine epistemic model, not on arbitrary redescriptions. Still, the source leaves the individuation problem unresolved, and any practical use of EDT needs a disciplined specification of the alternatives.

---

## 9. Counterfactuals in EDT

EDT does not reject counterfactual reasoning, but it interprets the relevant counterfactual evidentially. The question is not:

> What would happen if I intervened to make \(A\) true?

but rather:

> What should I expect if I learned that \(A\) is true?

In possible-world language, EDT considers worlds compatible with the news that \(A\) occurred and weights them by the agent’s conditional credence. In causal-model language, EDT conditions on the variable \(A\) rather than applying a \(do(A)\) intervention.

This difference can be expressed using the distinction between \(P(O\mid A)\) and \(P(O\mid do(A))\). Suppose a predictor’s prediction \(F\) determines the outcome \(O\), and the predictor reliably predicts action \(A\). The causal structure might be:

\[
A \leftarrow F \rightarrow O.
\]

Here \(F\) causes both the prediction and, through the setup of the problem, the outcome. The action \(A\) does not cause \(O\). An intervention \(do(A)\) would not change \(F\), so \(P(O\mid do(A))\) may be low. But ordinary conditionalization gives a high \(P(O\mid A)\), because \(A\) is evidence for \(F\). EDT uses the latter.

This is exactly what happens in Newcomb’s problem. The predictor’s earlier prediction is evidence-linked to the player’s later action. EDT treats the later action as diagnostic of the earlier prediction. CDT denies that this diagnostic relation is decision-relevant once the outcome has already been causally settled.

---

## 10. Sleeping Beauty and Dutch books

The reference article briefly mentions the Sleeping Beauty problem. It says EDT has been applied to Sleeping Beauty in order to avoid Dutch book arguments, but also notes Vincent Conitzer’s claim that halfers can still be Dutch-booked even after adopting EDT (Conitzer, 2015).

The details of Sleeping Beauty are not developed in the source, but the mention is significant because it shows that EDT interacts with problems of self-locating belief and repeated awakenings. In such problems, the agent’s evidence is not only about external states but also about where she is located within a sequence of observations. EDT’s reliance on conditional probability makes it sensitive to how those conditional probabilities are defined. If the agent’s action is evidence about the coin toss, or about which awakening she is experiencing, EDT may give different recommendations depending on the chosen probability model.

Since the source only gestures at this issue, I treat it as an open application rather than a settled part of EDT’s core. It reinforces the general lesson: EDT’s verdicts depend heavily on the agent’s probability model, including her treatment of indexical uncertainty.

---

## 11. The evidentialist’s wager and correlated decision-makers

The reference article mentions an argument that even if one is not fully convinced by EDT, it may be reasonable to act as if EDT were true when many correlated decision-makers are involved. The idea, associated with MacAskill et al. (2021), is that EDT can assign high stakes to actions that are correlated with the actions of many other agents. If my choice is evidence about what many similar agents choose, then the expected value of choosing well may be much larger than a narrowly causal calculation suggests.

This argument is not a proof of EDT. It is more like a pragmatic wager: if EDT is correct, or if the world contains many relevant correlations, then EDT-sensitive decisions may dominate in expected importance. The source presents this as a supporting consideration rather than as part of the formal theory.

The point also helps explain why EDT has attracted interest in contexts involving AI, coordination, and large-scale decision-making. If an agent believes that its decision procedure is similar to the decision procedures of many other agents, then its action may carry strong evidence about outcomes far beyond its local causal reach. EDT takes that evidence seriously.

---

## 12. Criticism and philosophical significance

The strongest objection to EDT is that it confuses good evidence with good control. If smoking is correlated with cancer because of a common cause, EDT may recommend avoiding smoking, even though smoking does not causally affect cancer. If carrying an umbrella is evidence of rain, EDT might seem to recommend avoiding umbrellas simply because umbrella-carrying is bad news. Critics say this is irrational: one should choose actions that bring about good outcomes, not actions that merely make good outcomes likely in the conditional distribution.

Lewis’s phrase “managing the news” captures this criticism. Joyce’s formulation is also sharp: rational agents choose acts on the basis of causal efficacy, not auspiciousness. On this view, EDT can recommend choosing a symptom rather than a cause, thereby mistaking correlation for control.

EDT’s defender can reply in several ways. First, in many cases where an action is evidence for a good outcome, the evidential connection reflects a real decision-relevant dependency, such as a predictor or a twin. Ignoring that dependency seems to leave expected value on the table. Second, if the agent genuinely cannot affect the outcome except through evidence about her own disposition, then choosing the action that indicates the best outcome may be the only rational way to respond to her epistemic situation. Third, EDT can be understood not as a metaphysical theory of causation but as a theory of what an agent should prefer when she thinks of her possible actions as possible versions of herself. From that perspective, choosing the action with highest news value is simply maximizing expected utility over the space of possible self-announcements.

Still, the disagreement with CDT is real. EDT and CDT are not merely different notations. They embody different answers to the question: should rational choice track conditional expectation or counterfactual intervention?

---

## 13. Conclusion

Evidential decision theory evaluates actions by the expected desirability of outcomes conditional on those actions. Its core rule is to maximize

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

choosing the act that would be best news to learn one had performed. This makes EDT especially sensitive to predictors, correlations, psychological similarity, and other non-causal dependencies. In Newcomb’s problem, it recommends one-boxing because one-boxing is evidence that the predictor filled the opaque box. In the twin prisoner’s dilemma, it recommends cooperation because cooperation is evidence that the twin will cooperate.

The theory can be extended to policies by treating a policy as a higher-order action and computing the expected desirability of outcomes conditional on adopting that policy. Sequential versions can condition on histories, though dynamic consistency requires care. The reference article leaves open several operational matters, especially zero-probability actions, action individuation, and policy evaluation. Reasonable operational treatments are available: use regular conditional probabilities or small-probability perturbations; condition on well-specified action or policy propositions; and evaluate policies directly when they are the objects of choice.

EDT’s philosophical appeal is that it takes seriously the evidential meaning of one’s own choices. Its vulnerability is that evidential meaning is not always control. Whether that vulnerability is fatal is the central debate between evidential and causal decision theory. But as a formal procedure, EDT is clear: choose the action whose truth would, by your own lights, bring the best news.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Conitzer, V. (2015). A Dutch book against sleeping beauties who are evidential decision theorists. *Synthese*, 192(9), 2887–2899.

Gibbard, A., & Harper, W. L. (1976). *Counterfactuals and Two Kinds of Expected Utility*.

Greene, P., & Levinstein, B. (2020). Act consequentialism without free rides. *Philosophical Perspectives*, 34(1), 100–101.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.

MacAskill, W., Vallinder, A., Österheld, C., Shulman, C., & Treutlein, J. (2021). *The Evidentialist’s Wager*.

Wikipedia contributors. (2026). Evidential decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1373679688.