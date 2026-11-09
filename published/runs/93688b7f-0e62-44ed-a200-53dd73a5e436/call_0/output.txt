# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a school of thought in decision theory that evaluates actions by their *news value*. The core idea, as summarized in the reference article, is that a rational agent should choose the action that would be the best news to learn she had performed. In a compact slogan: **do what you most want to learn that you will do**. If receiving the news “I did \(A\)” would make you expect better outcomes than receiving the news “I did \(B\),” then EDT recommends \(A\) over \(B\).

This makes EDT contrast sharply with causal decision theory (CDT). CDT asks which action would *bring about* the best outcome, whereas EDT asks which action would be the best *evidence* for a good outcome. The two often agree, but they can diverge in cases involving prediction, duplication, psychological similarity, or other non-causal correlations. The reference article gives the classic examples of Newcomb’s paradox and a twin prisoner’s dilemma, where EDT recommends one-boxing and cooperating, respectively.

This essay develops EDT as a usable decision procedure. I will state the formal definition, explain how it treats dependencies and counterfactuals, work through examples, and discuss some unresolved questions that arise when applying EDT to real or highly reflexive decision problems. Where the source is silent, I will distinguish my own operational proposals from the article’s claims.

---

## 1. The basic formalism

Suppose an agent faces a finite set of possible actions \(\mathcal{A}\). Let \(O_1, O_2, \dots\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). The agent has a probability function \(P\) representing her credences over relevant propositions, including propositions about her own actions.

The reference article gives the central EDT formula, due to Gibbard and Harper:

\[
V(A)=\sum_j P(O_j \mid A)\,D(O_j).
\]

Here \(V(A)\) is the evidential value of action \(A\), \(P(O_j \mid A)\) is the conditional probability of outcome \(O_j\) given that \(A\) is performed, and \(D(O_j)\) is the desirability of that outcome. EDT recommends choosing an action \(A^*\) such that

\[
A^* \in \arg\max_{A \in \mathcal{A}} V(A).
\]

It is usually better to make the agent’s total evidence explicit. If \(E\) is everything else the agent knows, then the formula becomes

\[
V(A)=\sum_j P(O_j \mid A, E)\,D(O_j).
\]

This is important because EDT is not merely about raw statistical correlations; it is about conditional probabilities given the agent’s full epistemic state. If the agent knows the predictor is reliable, knows the payoff matrix, or knows that another agent is her psychological twin, that information belongs in \(E\).

A slightly more explicit formulation uses states of the world. Let \(S_k\) be possible background states, and suppose that if the agent performs action \(A\) and state \(S_k\) obtains, the outcome is \(O(A,S_k)\). Then

\[
V(A)=\sum_k P(S_k \mid A, E)\,D(O(A,S_k)).
\]

This version makes clear that EDT conditions the agent’s beliefs about the world on the proposition that she performs \(A\). If performing \(A\) is evidence that the world is in a favorable state, EDT counts that in favor of \(A\).

The source article’s formula is simple, but applying it requires several interpretive choices. What counts as an “action”? What if actions are policies rather than one-off choices? How should conditional probabilities be defined when the agent is nearly certain what she will do? I will return to these questions later.

---

## 2. Policies, not merely isolated acts

Although the basic formula is written for simple actions, EDT can also evaluate policies. A policy is a rule mapping possible observations or decision situations to actions. For example, “cooperate if the other player has cooperated before, otherwise defect” is a policy. In sequential problems, the object of evaluation may be a whole plan rather than a single immediate action.

Let \(\Pi\) be a set of possible policies. If \(\pi \in \Pi\), EDT can assign a value

\[
V(\pi)=\sum_j P(O_j \mid \Pi=\pi, E)\,D(O_j).
\]

The proposition \(\Pi=\pi\) means: the agent follows policy \(\pi\). The conditional probability \(P(O_j \mid \Pi=\pi, E)\) is the probability of outcome \(O_j\) given the news that the agent is following that policy.

This policy-level formulation is often more natural than evaluating isolated actions. In Newcomb-like cases, for instance, the predictor may be predicting not merely a single physical movement but the agent’s decision procedure or disposition. In twin or multi-agent cases, the relevant proposition may be “I use this decision rule,” and that proposition may be strong evidence that another agent uses the same rule.

The source article does not explicitly develop a policy-based formulation, but it is compatible with the core EDT idea. If EDT says to choose the act that would be best news, then when the available options are policies, EDT should choose the policy that would be best news.

---

## 3. Evidential dependence versus causal dependence

The crucial feature of EDT is that it uses ordinary conditional probabilities rather than explicitly causal or counterfactual probabilities. The source article contrasts EDT’s formula with the causal decision theorist’s counterfactual formula:

\[
U(A)=\sum_j P(A \mathbin{\Box\!\rightarrow} O_j)\,D(O_j),
\]

where \(A \mathbin{\Box\!\rightarrow} O_j\) is a counterfactual such as “if \(A\) were performed, \(O_j\) would occur.” In modern causal-modeling language, CDT often uses an interventionist probability such as \(P(O_j \mid do(A))\), whereas EDT uses the observational conditional \(P(O_j \mid A)\).

These two quantities are not always equal.

A simple way to see the difference is to compare EDT and CDT in a state-based model. Let \(S_k\) be states that are not causally affected by the action. CDT often evaluates an action as

\[
U_{\text{CDT}}(A)=\sum_k P(S_k)\,D(O(A,S_k)),
\]

or, more generally, using probabilities after an intervention that sets \(A\). EDT instead uses

\[
V_{\text{EDT}}(A)=\sum_k P(S_k \mid A, E)\,D(O(A,S_k)).
\]

If the action is probabilistically independent of the relevant states, so that

\[
P(S_k \mid A, E)=P(S_k \mid E),
\]

then EDT and CDT will usually agree. But if the action is evidence about the states, EDT takes that evidence seriously.

This is the heart of EDT’s treatment of dependencies. EDT counts any probabilistic dependency between the action and the outcome, whether that dependency is causal, common-causal, logical, or psychological. If choosing \(A\) is correlated with a good outcome because \(A\) is predicted by a reliable predictor, because \(A\) is performed by agents with a certain disposition, or because \(A\) is logically correlated with another agent’s choice, EDT treats that correlation as decision-relevant.

This is also why EDT is controversial. Critics say that EDT confuses good news with good causal influence. But the EDT response is that if your action is a reliable symptom of a desirable state of the world, then it is rational to care about that symptom, especially when your action reveals something about predictors, copies, or correlated decision-makers.

---

## 4. Newcomb’s paradox

The reference article discusses Newcomb’s paradox, the most famous case where EDT and CDT diverge.

There are two boxes, \(A\) and \(B\). Box \(A\) is transparent and contains \$1,000. Box \(B\) is opaque. A highly reliable predictor has already predicted whether the player will take only box \(B\) or both boxes. If the predictor predicted that the player will take only box \(B\), then box \(B\) contains \$1,000,000. If the predictor predicted that the player will take both boxes, then box \(B\) contains nothing.

The player can choose:

1. Take only box \(B\).
2. Take both boxes \(A\) and \(B\).

Assume the predictor is 99% accurate, and for simplicity treat dollars as utilities. The source gives the EDT calculations:

\[
\begin{aligned}
V(\text{take only } B)
&= P(\text{\$1M in }B \mid \text{take only }B)\cdot \$1{,}000{,}000 \\
&\quad + P(\text{nothing in }B \mid \text{take only }B)\cdot \$0 \\
&= 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0 \\
&= \$990{,}000.
\end{aligned}
\]

For taking both boxes:

\[
\begin{aligned}
V(\text{take both})
&= P(\text{\$1M in }B \mid \text{take both})\cdot \$1{,}001{,}000 \\
&\quad + P(\text{nothing in }B \mid \text{take both})\cdot \$1{,}000 \\
&= 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000 \\
&= \$11{,}000.
\end{aligned}
\]

Since

\[
V(\text{take only }B) > V(\text{take both}),
\]

EDT recommends taking only box \(B\).

The reasoning is straightforward. Choosing only box \(B\) is strong evidence that the predictor predicted one-boxing, which is strong evidence that box \(B\) contains \$1,000,000. Choosing both boxes is strong evidence that the predictor predicted two-boxing, which is strong evidence that box \(B\) is empty.

CDT gives a different verdict. From a causal perspective, the contents of box \(B\) have already been determined. The player’s current action cannot causally change what is in box \(B\). Therefore, if box \(B\) contains \$1,000,000, taking both boxes yields \$1,001,000 instead of \$1,000,000. If box \(B\) contains nothing, taking both boxes yields \$1,000 instead of \$0. In either case, taking both boxes appears causally dominant.

EDT rejects the relevance of this causal dominance reasoning, or at least denies that it is the whole story. The EDT agent does not ask only, “What will this action causally produce?” She asks, “What would the world likely be like if I learned that I performed this action?” In Newcomb’s problem, one-boxing is much better news than two-boxing.

---

## 5. Twin prisoner’s dilemma

The reference article also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin are in separate rooms and cannot communicate. Their reasoning processes are exactly analogous. Aomame chooses whether to cooperate or defect. The payoffs to Aomame are:

- If both cooperate, Aomame gets \$5.
- If both defect, Aomame gets \$1.
- If Aomame cooperates while her twin defects, Aomame gets \$0.
- If Aomame defects while her twin cooperates, Aomame gets \$10.

Because the twins are psychologically identical and face the same problem, Aomame’s choice is perfect evidence of her twin’s choice. If Aomame cooperates, that is evidence that her twin cooperates. If Aomame defects, that is evidence that her twin defects.

The source gives:

\[
\begin{aligned}
V(\text{Aomame cooperates})
&= P(\text{twin cooperates} \mid \text{Aomame cooperates})\cdot \$5 \\
&\quad + P(\text{twin defects} \mid \text{Aomame cooperates})\cdot \$0 \\
&= 1\cdot \$5 + 0\cdot \$0 \\
&= \$5.
\end{aligned}
\]

And:

\[
\begin{aligned}
V(\text{Aomame defects})
&= P(\text{twin cooperates} \mid \text{Aomame defects})\cdot \$10 \\
&\quad + P(\text{twin defects} \mid \text{Aomame defects})\cdot \$1 \\
&= 0\cdot \$10 + 1\cdot \$1 \\
&= \$1.
\end{aligned}
\]

Since \$5 > \$1, EDT recommends cooperating.

This example is important because it shows that EDT can recommend cooperation in prisoner’s-dilemma-like cases when the agents are sufficiently correlated. The source’s exact calculation assumes perfect psychological symmetry, but the same reasoning can be generalized.

Suppose the correlation is imperfect. Let

\[
q = P(\text{twin cooperates} \mid \text{Aomame cooperates})
\]

and

\[
r = P(\text{twin defects} \mid \text{Aomame defects}).
\]

Then

\[
V(\text{cooperate}) = 5q,
\]

and

\[
V(\text{defect}) = 10(1-r) + 1r = 10 - 9r.
\]

Aomame should cooperate if

\[
5q > 10 - 9r.
\]

If the situation is symmetric, so that \(q=r=p\), this becomes

\[
5p > 10 - 9p,
\]

which gives

\[
14p > 10,
\]

or

\[
p > \frac{5}{7} \approx 0.714.
\]

Thus, even if the twin is not perfectly predictable, EDT can recommend cooperation if the evidential correlation is strong enough. This extension is not in the source article, but it follows naturally from the EDT formula.

---

## 6. What dependencies count?

EDT’s formalism is simple, but the hard part is constructing the probability model. The conditional probabilities \(P(O_j \mid A, E)\) must reflect all relevant dependencies known to the agent.

At minimum, the agent should consider:

1. **Causal dependencies**: Actions can cause outcomes. If taking medicine causes recovery, then \(P(\text{recovery} \mid \text{take medicine})\) may be high partly because of the causal effect.

2. **Common-cause dependencies**: A common cause may produce both the action and the outcome. If a predictor causes both the box contents and, indirectly, the agent’s choice, then the action and the box contents are correlated even if the action does not causally affect the box contents.

3. **Psychological or algorithmic dependencies**: If two agents use the same reasoning procedure, then one agent’s choice can be evidence of the other’s choice. This is the structure behind the twin prisoner’s dilemma.

4. **Logical dependencies**: In some cases, propositions about one agent’s choice may logically entail or strongly support propositions about another agent’s choice, especially if the agents are identical or if their decisions are outputs of the same algorithm.

5. **Selection effects and indexical dependencies**: In problems involving self-location, repeated awakenings, or observer selection, conditioning on an action may change the agent’s beliefs about which centered situation she is in. The Sleeping Beauty problem is a notable example.

The reference article mentions Sleeping Beauty briefly. It says EDT has been applied to the problem to avoid Dutch book arguments, but also notes that Vincent Conitzer has argued that halfers can still be subject to Dutch books even after adopting EDT. This illustrates that EDT’s application can become uncertain when the relevant probability space involves centered or self-locating propositions. The source does not resolve this issue, and it remains an active area of debate.

A standard example not mentioned in the source, but useful for understanding the dispute, is the “smoking lesion” case. Suppose a genetic lesion causes both a desire to smoke and a higher probability of cancer, but smoking itself does not cause cancer. If smoking is strong evidence of the lesion, then EDT may recommend not smoking, because smoking would be bad news about the agent’s health. CDT would say that since smoking does not causally affect cancer risk, the agent may smoke if she enjoys it. This example captures the philosophical disagreement in a stark form: EDT treats the evidential correlation as relevant; CDT does not.

---

## 7. Counterfactuals in EDT

It is sometimes said that EDT does not use counterfactuals. That is not quite right. EDT uses a distinctively *epistemic* or *suppositional* counterfactual. The relevant question is:

> If I were to learn that I performed \(A\), how would my expectations about outcomes change?

This is not the same as the interventionist counterfactual:

> If I intervened to make myself perform \(A\), what would happen?

In many ordinary cases, the two coincide. If I am deciding whether to take an umbrella, learning that I took the umbrella and making myself take the umbrella usually lead to similar expectations about whether I stay dry. But in Newcomb cases and twin cases, they diverge.

EDT’s counterfactual is modeled by conditionalization. To evaluate \(A\), the agent updates her beliefs on the proposition \(A\), then computes expected utility in the resulting probability distribution. CDT instead models the counterfactual by an intervention that changes the action while holding fixed the relevant prior states.

This distinction can be expressed with causal graphs. Suppose a predictor variable \(P\) influences box contents \(B\), and the agent’s decision disposition also influences her action \(A\). If the predictor is accurate, \(A\) and \(B\) become probabilistically correlated through \(P\). EDT conditions on \(A\), so information flows back to \(B\). CDT performs an intervention on \(A\), which severs the usual explanatory link from prior dispositions into \(A\), so \(B\) is held fixed.

Thus, EDT and CDT are not merely using different formulas; they are using different notions of what it means to suppose an action is performed.

---

## 8. A practical procedure for applying EDT

For an unfamiliar decision problem, I would recommend the following procedure. This is partly drawn from the source’s core idea and partly my own operational elaboration.

### Step 1: Identify the feasible actions or policies

Decide whether the relevant options are simple acts, dispositions, or policies. In dynamic or multi-agent problems, policies are often more appropriate.

Let the option set be \(\mathcal{O}\), where each \(o \in \mathcal{O}\) is a proposition such as “I perform action \(A\)” or “I follow policy \(\pi\).”

### Step 2: Specify outcomes and utilities

List the outcomes the agent cares about and assign desirabilities \(D(O_j)\). If the agent cares about other agents’ payoffs, include those in the outcome description. If the agent is risk-averse, use utility rather than money.

### Step 3: Build the joint probability model

Construct a probability model over actions, states, and outcomes. Include known predictors, correlations, common causes, copies, and logical constraints. The model should reflect the agent’s total evidence \(E\).

For example, in a Newcomb problem, the model should include the predictor’s reliability and the fact that the predictor’s prediction influences the box contents. In a twin problem, the model should include the degree of psychological similarity between the agents.

### Step 4: Compute conditional expected values

For each option \(o\), compute

\[
V(o)=\sum_j P(O_j \mid o, E)D(O_j).
\]

If evaluating policies, use

\[
V(\pi)=\sum_j P(O_j \mid \Pi=\pi, E)D(O_j).
\]

### Step 5: Choose the option with maximum evidential value

EDT recommends selecting

\[
o^* \in \arg\max_{o \in \mathcal{O}} V(o).
\]

If several options tie, any of them is EDT-permissible.

---

## 9. The problem of zero-probability actions

One important technical issue is not settled by the source article: how should EDT define \(P(O_j \mid A)\) when the agent assigns probability zero to performing \(A\)? In decision problems, an agent may be practically certain what she will do. Yet EDT still needs to evaluate the alternatives.

If \(P(A)=0\), the ordinary ratio definition

\[
P(O_j \mid A)=\frac{P(O_j \cap A)}{P(A)}
\]

fails. There are several possible responses.

One option is to treat conditional probabilities as primitive. In a Jeffrey-style framework, the agent may have conditional desirabilities or conditional probabilities even for propositions to which she assigns zero unconditional probability. This is mathematically possible but can feel operationally underspecified.

A second option, and the one I find most operationally useful, is to regularize the problem by adding a small amount of uncertainty. Suppose the agent is almost certain to perform some action, but not perfectly certain. Introduce a small \(\varepsilon > 0\) such that every feasible action has positive probability. Compute the EDT values using this perturbed model, and then examine the limit as \(\varepsilon \to 0\). If the limiting values exist and do not depend sensitively on the perturbation, they provide a reasonable EDT evaluation.

For example, instead of assigning probability zero to two-boxing, one might suppose there is a tiny probability that the agent two-boxes because of a momentary error, random noise, or unresolved uncertainty about her own reasoning. Then compute

\[
V_\varepsilon(A)=\sum_j P_\varepsilon(O_j \mid A)D(O_j).
\]

If

\[
\lim_{\varepsilon \to 0} V_\varepsilon(A)
\]

is well-defined and stable, use it as the EDT value of \(A\).

This regularization proposal is my own addition to the source material. It is not the only possible interpretation, but it fits the EDT idea: evaluating an action by considering what would be good news upon learning that the action was performed. If the agent was already certain she would not perform the action, we can approximate “learning it” by considering nearby epistemic states where the action remains barely possible.

However, if different regularization methods produce different limiting values, EDT may be indeterminate for that problem. In such cases, the theory does not merely need calculation; it needs a more precise account of the agent’s probability model and of how self-referential action propositions should be represented.

---

## 10. Ratification and dynamic stability

Another subtlety concerns whether EDT recommendations are stable under reflection. An EDT agent chooses the act that maximizes value conditional on performing that act. But after choosing, the agent may update on the fact that she has chosen, and this update could change the values of the alternatives.

A decision is sometimes called *ratifiable* if, conditional on the agent’s choosing it, it still maximizes expected value. EDT can face problems where the recommended action is not ratifiable, especially in reflexive cases where the agent’s beliefs about her own action are influenced by the expected utilities of the actions.

The source article does not discuss ratification. This is another area where EDT may need supplementation if it is to give stable advice in dynamically complex cases. A natural operational approach is to evaluate policies rather than momentary actions and to require that the chosen policy maximize evidential value conditional on the agent’s adopting that policy. This does not solve every problem, but it helps in many sequential and predictive settings.

---

## 11. Criticism and pragmatic support

The reference article mentions two important criticisms of EDT. David Lewis characterized EDT as promoting “an irrational policy of managing the news.” James Joyce argued that rational agents choose acts on the basis of causal efficacy, not auspiciousness; they act to bring about good results even when doing so might betoken bad news.

These criticisms capture the central intuitive objection to EDT. In cases like the smoking lesion, EDT may recommend avoiding an action that is harmless but diagnostically bad. That can seem irrational: why avoid a pleasure just because it is correlated with a disease you cannot cause or avoid?

EDT defenders reply that the cases where EDT diverges from CDT are precisely the cases where actions are not merely causal levers but also evidence about the world. If the world contains reliable predictors, identical copies, or correlated decision-makers, then managing the news may be a rational way of navigating those dependencies.

The source also mentions a pragmatic argument: even if one is not fully confident in EDT, it may be reasonable to act as if EDT were true when many correlated decision-makers are involved. This is associated with what the source calls “The Evidentialist’s Wager.” The idea is that EDT can involve the actions of many correlated agents, so the stakes of EDT-style reasoning may be high. If your action is evidence about what many similar agents do, then EDT may capture coordination benefits that CDT misses.

This argument does not prove EDT is correct. But it suggests that EDT may be practically important in large-scale or multi-agent contexts, especially where agents use similar reasoning procedures.

---

## 12. Conclusion

Evidential decision theory offers a clear and mathematically simple principle: choose the action with the highest expected utility conditional on performing that action. Its core formula,

\[
V(A)=\sum_j P(O_j \mid A)D(O_j),
\]

captures the idea that rational choice should be guided by the expected news value of actions. EDT treats actions as evidence about the world, and it counts non-causal dependencies—prediction, duplication, psychological similarity, and logical correlation—as relevant to decision-making.

In Newcomb’s problem, EDT recommends one-boxing because one-boxing is strong evidence that the predictor filled the opaque box. In the twin prisoner’s dilemma, EDT recommends cooperating because cooperation is evidence that the twin will cooperate. More generally, EDT can be applied by specifying actions or policies, assigning utilities, modeling all relevant probabilistic dependencies, conditioning on each option, and maximizing conditional expected utility.

The main difficulty is not the formula but its interpretation. EDT requires well-defined conditional probabilities for actions, including actions the agent may be nearly certain not to perform. In reflexive, indexical, or zero-probability cases, the theory may need additional operational assumptions. A reasonable approach is to regularize the probability model with small uncertainty and examine stable limits, but this is an interpretive proposal rather than a claim supplied by the source.

EDT remains controversial because it separates good news from causal production. Critics see that as irrational news management; defenders see it as a rational response to a world full of predictors, copies, and correlated agents. Whether one accepts EDT depends partly on one’s view of counterfactuals, agency, and the proper relationship between evidence and action. But as a formal decision procedure, EDT is precise enough to be applied to a wide range of unfamiliar cases, provided the agent carefully specifies the evidential structure of the problem.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.