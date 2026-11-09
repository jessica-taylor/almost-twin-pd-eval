# Evidential Decision Theory: Choosing What You Would Most Like to Learn

Evidential decision theory (EDT) is a school of thought within decision theory that evaluates actions by their *news value*. The reference article summarizes the idea by saying that EDT recommends the action that would be evidence for the best expected outcome: “do what you most want to learn that you will do” (Ahmed 2021, quoted in Wikipedia contributors 2026). If you were to receive a message telling you which action you had chosen, EDT asks what that message would lead you to expect. The rational action, on this view, is the one whose news you would most welcome.

This contrasts with causal decision theory (CDT), which evaluates actions by their expected causal consequences. CDT asks, “If I intervened to bring about this action, what would happen?” EDT asks, “Given that this action is taken, what should I infer about the world?” The two approaches often agree, especially in ordinary cases where actions are causally effective and not strongly correlated with independent states of the world. But they diverge in famous thought experiments involving predictors, twins, copies, and other forms of correlation.

This essay gives a formal account of EDT, explains how to apply it to decision problems, discusses how it treats dependencies and counterfactuals, and examines some unresolved questions. Where I go beyond the supplied reference article, I will say so explicitly.

---

## 1. Formal definition

The reference article attributes to Gibbard and Harper (1976) the following EDT value function:

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

where:

- \(A\) is an available action;
- \(\{O_j\}\) is a partition of possible outcomes;
- \(D(O_j)\) is the desirability, utility, or value of outcome \(O_j\);
- \(P(O_j\mid A)\) is the agent’s conditional probability of outcome \(O_j\) given that action \(A\) is performed.

Equivalently, EDT chooses the action with the highest conditional expected utility:

\[
V(A)=\mathbb{E}[D(O)\mid A].
\]

For continuous outcome spaces, the sum is replaced by an integral.

The EDT decision rule is:

\[
A^* \in \arg\max_A V(A).
\]

If several actions maximize \(V\), EDT permits any of them, or requires a tie-breaking rule supplied by the context.

The article contrasts this with the causal decision-theoretic formula:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) means that outcome \(O_j\) would obtain in the counterfactual situation in which action \(A\) is performed. In modern causal-modeling language, one often writes this as \(P(O_j\mid do(A))\), the probability of \(O_j\) under an intervention setting \(A\) to occur. EDT uses ordinary conditional probabilities \(P(O_j\mid A)\); CDT uses interventionist or counterfactual probabilities \(P(O_j\mid do(A))\) or \(P(A \mathrel{\Box\rightarrow} O_j)\).

The difference is crucial. Conditioning on \(A\) asks what \(A\) tells you about the world. Intervening on \(A\) asks what would happen if \(A\) were produced while holding fixed, in the appropriate way, the causal background conditions.

A useful way to write the EDT calculation is by introducing states of the world. Let \(S\) be a variable representing relevant states: predictor predictions, the actions of correlated agents, medical conditions, social circumstances, and so on. If action \(A\) in state \(s\) produces outcome \(O(A,s)\), then

\[
V(A)=\sum_s P(S=s\mid A)D(O(A,s)).
\]

This formulation is not explicitly in the source, but it is mathematically equivalent to the source’s formula and makes EDT easier to apply. EDT does not use the prior probabilities \(P(S=s)\) when comparing actions; it uses the conditional probabilities \(P(S=s\mid A)\). The action is treated as evidence about the state.

---

## 2. How to apply EDT to a decision problem

A practical EDT analysis can proceed as follows.

1. **Specify the available actions.**  
   Let the agent choose among actions \(A_1,\dots,A_n\). These should be mutually exclusive options at the relevant decision point.

2. **Specify the outcomes.**  
   Identify the possible outcomes \(O_j\) and assign desirabilities \(D(O_j)\). The outcomes should include everything the agent intrinsically cares about: money, welfare, reputational effects, future opportunities, or even facts about what kind of agent she is, if those are valued intrinsically.

3. **Specify the probabilistic model.**  
   EDT requires a joint probability model over actions, states, and outcomes. This is where predictors, correlations, psychological similarity, selection effects, and other dependencies enter.

4. **Compute conditional probabilities.**  
   For each action \(A\), compute \(P(O_j\mid A)\), or equivalently \(P(S=s\mid A)\).

5. **Compare conditional expected utilities.**  
   Choose an action maximizing

   \[
   V(A)=\sum_j P(O_j\mid A)D(O_j).
   \]

One technical caveat is that \(P(O_j\mid A)\) is undefined if \(P(A)=0\). The reference article does not discuss this problem. In many formal treatments, one assumes that all available actions have positive probability, at least for the purpose of deliberation. Later I will suggest an operational way of handling zero-probability actions by using small “trembling” probabilities and taking limits.

---

## 3. Newcomb’s problem

The reference article discusses Newcomb’s paradox as a central example. A player faces two boxes:

- Box A is transparent and always contains \$1,000.
- Box B is opaque. Its contents were set earlier by a highly reliable predictor.
  - If the predictor predicted that the player will take only B, then B contains \$1,000,000.
  - If the predictor predicted that the player will take both boxes, then B contains nothing.

The player may either take only box B, called “one-boxing,” or take both boxes A and B, called “two-boxing.” Suppose the predictor is correct with probability \(0.99\). The source gives the following conditional probabilities:

\[
P(\text{1M in B}\mid \text{take only B})=0.99,
\]
\[
P(\text{nothing in B}\mid \text{take only B})=0.01,
\]
\[
P(\text{1M in B}\mid \text{take both boxes})=0.01,
\]
\[
P(\text{nothing in B}\mid \text{take both boxes})=0.99.
\]

The EDT values are:

\[
\begin{aligned}
V(\text{take only B})
&=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0\\
&=\$990{,}000.
\end{aligned}
\]

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

The philosophical interest is that two-boxing appears to dominate one-boxing in a state-by-state sense. If B already contains \$1,000,000, taking both boxes yields \$1,001,000 rather than \$1,000,000. If B is empty, taking both boxes yields \$1,000 rather than \$0. Whatever is already in B, taking both boxes seems to give \$1,000 more. CDT therefore recommends two-boxing, because the predictor’s prediction is already in the past and the player’s current choice does not causally change what is in B.

EDT rejects the assumption that the relevant states are independent of the action. The player’s choice is strong evidence about what the predictor predicted. One-boxing is evidence that B contains \$1,000,000; two-boxing is evidence that B is empty. EDT treats the action not as a causal lever on the past, but as information about the past.

---

## 4. Twin prisoner’s dilemma

The reference article also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin are in separate rooms and cannot communicate. Their reasoning processes are exactly analogous. The payoff structure is:

- If both cooperate, each gets \$5.
- If both defect, each gets \$1.
- If one cooperates and the other defects, the defector gets \$10 and the cooperator gets \$0.

The source assumes perfect psychological symmetry, so:

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]
\[
P(\text{twin defects}\mid \text{Aomame cooperates})=0,
\]
\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0,
\]
\[
P(\text{twin defects}\mid \text{Aomame defects})=1.
\]

Then EDT gives:

\[
\begin{aligned}
V(\text{Aomame cooperates})
&=1\cdot \$5+0\cdot \$0\\
&=\$5,
\end{aligned}
\]

\[
\begin{aligned}
V(\text{Aomame defects})
&=0\cdot \$10+1\cdot \$1\\
&=\$1.
\end{aligned}
\]

So EDT recommends cooperation.

The source gives the perfect-correlation case. A natural generalization, which I add for clarity, is to allow imperfect correlation. Let

\[
q=P(\text{twin cooperates}\mid \text{Aomame cooperates}),
\]
\[
r=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then:

\[
V(\text{cooperate})=5q+0(1-q)=5q,
\]

\[
V(\text{defect})=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when

\[
5q>1+9r.
\]

This inequality is useful for unfamiliar cases. If the twin’s action is independent of Aomame’s action, then \(q=r=p\), where \(p\) is Aomame’s prior probability that the twin cooperates. In that case:

\[
V(\text{cooperate})=5p,
\]
\[
V(\text{defect})=1+9p.
\]

Since

\[
1+9p>5p
\]

for every \(p\in[0,1]\), EDT recommends defection when the twin’s behavior is probabilistically independent of Aomame’s choice. EDT therefore does not recommend cooperation merely because cooperation is morally attractive. It recommends cooperation only when one’s own cooperation is sufficiently strong evidence that the other agent will cooperate.

This point generalizes. EDT can recommend cooperation in prisoner’s dilemma-like cases involving clones, psychological twins, sufficiently similar artificial agents, or correlated decision procedures. But in an ordinary one-shot prisoner’s dilemma with an independent opponent, EDT and CDT usually agree in recommending defection.

---

## 5. Dependencies, counterfactuals, and causal structure

EDT’s distinctive feature is that it cares about evidential dependence, not only causal dependence. An action can be relevant to EDT even if it does not causally influence the outcome. It is enough that the action is probabilistically correlated with something that matters.

Common sources of evidential dependence include:

1. **Prediction.**  
   A predictor has predicted your action before you take it. Your action does not change the past prediction, but it is evidence about that prediction.

2. **Common causes.**  
   Some hidden factor influences both your action and the outcome. Your action is then evidence about that hidden factor.

3. **Psychological or algorithmic similarity.**  
   If another agent reasons like you, your choice may be evidence about their choice.

4. **Selection effects.**  
   The fact that you are making a certain decision may be evidence about which branch, room, awakening, or population you are in.

5. **Logical or mathematical dependence.**  
   If several agents implement the same decision algorithm, the output of one instance can be evidence about the outputs of others.

The contrast with CDT can be expressed using causal Bayes nets. In such a network, ordinary conditioning on \(A\) uses all probabilistic associations represented in the graph. An intervention \(do(A)\), however, cuts the incoming causal arrows to \(A\). It asks what would happen if \(A\) were set from outside the system. EDT evaluates \(P(O\mid A)\); CDT evaluates \(P(O\mid do(A))\). These are equal in randomized experiments or in cases where the action is not confounded, but they can differ sharply otherwise.

Consider a “smoking lesion” case. This example is not in the supplied article, but it is a standard way to illustrate the debate. Suppose smoking does not cause cancer. Instead, a genetic lesion both causes a disposition to smoke and causes cancer. Smoking is therefore evidence of the lesion. If smoking is pleasurable but cancer is bad, EDT may recommend not smoking, because smoking is bad news: it raises the conditional probability that one has the lesion and will get cancer. CDT, by contrast, says that smoking does not causally affect cancer, so if one enjoys smoking, one should smoke. Lewis’s criticism that EDT promotes “an irrational policy of managing the news” is aimed at exactly this sort of case (Lewis 1981, quoted in Wikipedia contributors 2026).

The EDT response is that actions are not merely causal levers; they are also symptoms of the world. If your action reveals something about your type, your environment, or the likely behavior of similar agents, EDT says that evidential information belongs in the decision calculation. Whether this is a virtue or a defect is one of the central philosophical disputes between EDT and CDT.

---

## 6. Policies, precommitments, and dynamic choice

The reference article presents EDT mainly as a theory of individual actions. But many decision problems involve policies: rules that map observations or histories to actions. EDT can be extended naturally to policies, though this extension is my own exposition rather than a detailed claim of the source.

Let \(\Pi\) be a set of possible policies. A policy \(\pi\) might be “one-box in Newcomb’s problem,” “cooperate with agents sufficiently similar to me,” or “bet on heads when awake after a certain coin toss.” EDT can evaluate a policy by conditioning on the proposition that the agent follows that policy:

\[
V(\pi)=\sum_z P(Z=z\mid \pi)D(Z=z),
\]

where \(Z\) ranges over final outcomes.

In a dynamic problem with histories \(h\), one can write:

\[
V(\pi)=\sum_h P(h\mid \pi)D(\text{outcome}(h)).
\]

Here \(P(h\mid \pi)\) is the probability of history \(h\) given that the agent implements policy \(\pi\). The important point is that EDT conditions on the whole policy, not merely on isolated actions abstracted from the rule that produced them.

This matters for precommitment. Suppose an agent can publicly precommit to one-boxing before the predictor makes its prediction. EDT evaluates the precommitment as evidence about future behavior and therefore as evidence about the predictor’s prediction. If precommitting to one-boxing makes it highly probable that the predictor predicted one-boxing, EDT favors the precommitment. The same reasoning can apply to voting, charitable giving, environmental behavior, or coordination among many similar agents: your policy may be evidence about what other agents do.

The reference article briefly mentions a related argument: even if one is not fully confident in EDT, it may be prudent to act as if EDT is true when many correlated decision-makers are involved, because the stakes may be higher than in purely causal reasoning (MacAskill et al. 2021). This is a strategic or wager-like argument rather than a proof of EDT.

---

## 7. Open questions and an operational interpretation

The source gives the core EDT formula and several examples, but it leaves important questions open. I discuss three: act probabilities, self-locating uncertainty, and the boundary between evidential and causal reasoning.

### 7.1 Act probabilities and zero-probability actions

EDT requires conditional probabilities \(P(O_j\mid A)\). These are undefined if \(P(A)=0\). This is not merely a technicality. In deliberation, an agent may become increasingly certain that she will perform the action she judges best. If she assigns probability 1 to that action and probability 0 to the alternatives, EDT’s formula becomes hard to apply.

The reference article does not resolve this. One reasonable operational interpretation, which I propose rather than find in the source, is to use a full-support deliberative prior over available actions. For a small parameter \(\varepsilon>0\), assign every feasible action probability at least \(\varepsilon\), or otherwise ensure that all actions have positive probability. Compute

\[
V_\varepsilon(A)=\sum_j P_\varepsilon(O_j\mid A)D(O_j).
\]

Then take the limit as \(\varepsilon\to 0\), if the limit exists and is stable. This is analogous to “trembling hand” refinements in game theory, where players are assumed to make small mistakes with low probability.

In Newcomb’s problem, for example, small uncertainty about whether the agent will one-box or two-box does not change the EDT recommendation as long as the predictor remains highly reliable. But if a verdict depends sensitively on the chosen limiting process, then the decision problem itself may be underspecified. EDT needs a substantive model of how the agent’s action is related to the relevant states of the world.

### 7.2 Sleeping Beauty and centered evidence

The reference article mentions the Sleeping Beauty problem only briefly. It says EDT has been applied to avoid Dutch book arguments, but it also notes that Conitzer (2015) argues that halfers can still be Dutch booked even after adopting EDT. The article does not settle the underlying debate.

The difficulty is that Sleeping Beauty involves self-locating uncertainty: Beauty must reason about centered propositions such as “I am awake now” rather than only about uncentered propositions such as “the coin landed heads.” EDT’s usual formula applies most cleanly when actions and outcomes are uncentered propositions. When centered evidence matters, one must decide what probability space to condition on.

A cautious operational interpretation, not supplied by the source, is to evaluate betting policies conditional on the agent’s centered situation. For example, instead of asking only for \(P(\text{heads}\mid \text{bet on heads})\), one asks for the probability of heads conditional on being awake and facing a particular betting decision. This preserves the EDT idea—choose the action with the best news—while making explicit that the relevant conditioning event may be a centered proposition. However, this remains philosophically contested.

### 7.3 Which dependencies count?

EDT uses the agent’s probability function, so the verdict can depend on how the agent models the world. If the agent believes that a predictor is reliable, EDT may one-box. If she believes the predictor is unreliable, EDT may two-box. If she believes her action is independent of the other player in a prisoner’s dilemma, EDT defects. If she believes her action is strongly correlated with the other player, EDT may cooperate.

This is not necessarily a flaw. Decision theories must operate relative to the agent’s beliefs. But it means that EDT does not give a single answer unless the probabilistic structure of the problem is specified. The theory tells you how to reason from a model; it does not automatically tell you which model is correct.

---

## 8. Criticism and philosophical significance

The reference article includes two important criticisms. David Lewis characterized EDT as “an irrational policy of managing the news” (Lewis 1981). James M. Joyce wrote that rational agents choose acts on the basis of their “causal efficacy,” not their “auspiciousness”; they act to bring about good results even when doing so might betoken bad news (Joyce 1999).

These criticisms capture the intuitive worry about EDT. In the smoking lesion case, avoiding smoking does not prevent cancer; it merely avoids being evidence of cancer. In Newcomb’s problem, one-boxing does not cause the predictor to have placed money in B; it is merely evidence that the predictor did so. From a causal point of view, this can seem like trying to manipulate the message rather than the world.

EDT’s defenders respond that rational agency cannot always be separated from evidence. If your decision is produced by a physical or computational process, then that process may be predictable, replicated, or correlated with other agents. In such cases, treating your action purely as an intervention may ignore real structure in the world. If a predictor is reliable, one-boxing really is associated with receiving \$1,000,000. If many agents use similar reasoning, your cooperation may be evidence of their cooperation. EDT takes those associations seriously.

The debate between EDT and CDT is therefore not merely technical. It reflects a deeper disagreement about what decision theory is for. Is choice primarily a means of causing outcomes? Or is choice also a piece of evidence about the kind of world one is in and the kind of agent one is? EDT answers that a rational agent should care about the news her action provides.

---

## Conclusion

Evidential decision theory offers a simple but radical rule: choose the action that would be the best news. Formally, it maximizes

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

using conditional probabilities rather than interventionist counterfactuals. In Newcomb’s problem, this leads EDT to one-box, because one-boxing is strong evidence that the predictor placed \$1,000,000 in the opaque box. In twin prisoner’s dilemma cases, EDT can recommend cooperation, because one’s own cooperation is evidence that a sufficiently similar agent will also cooperate.

The theory is easy to state but delicate to apply. One must specify actions, outcomes, utilities, and especially the probabilistic dependencies linking actions to states of the world. EDT is sensitive to prediction, correlation, similarity, selection effects, and self-locating uncertainty. It also faces unresolved questions about act probabilities, zero-probability choices, and centered evidence.

EDT’s great strength is that it takes seriously the evidential significance of action. Its great vulnerability is that it may favor actions that are merely good news rather than good causes. Whether that is a defect or a deeper insight depends on one’s view of rational agency itself.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Conitzer, Vincent. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, no. 9 (2015): 2887–2899.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688. Text licensed under CC BY-SA 4.0.