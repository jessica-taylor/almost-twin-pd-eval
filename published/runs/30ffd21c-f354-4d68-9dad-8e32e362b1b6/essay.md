# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a theory of rational choice that evaluates actions by their *evidential import*: what an action would tell you about the world if you learned that you had performed it. The reference article summarizes the view with the slogan that one should “do what you most want to learn that you will do.” In more technical terms, EDT says that a rational agent should choose the action with the highest expected utility computed by ordinary conditional probabilities. This contrasts with causal decision theory (CDT), which evaluates actions by their expected causal efficacy: what would happen *because* of the action, usually expressed with counterfactual or interventionist probabilities.

The source gives the central EDT formula, the contrast with CDT, and several canonical examples: Newcomb’s paradox, a twin prisoner’s dilemma, and a brief discussion of the Sleeping Beauty problem. In this essay, I restate the formal rule, explain how EDT treats dependencies and counterfactuals, and develop a few operational refinements that the source only hints at. Where I go beyond the source—especially in giving a state-space formulation, a policy formulation, and a practical method for assigning conditional probabilities—I will say so.

---

## 1. The core EDT rule

Suppose an agent faces a finite set of possible actions, denoted \(A_1, A_2, \dots, A_n\). Let \(O_1, O_2, \dots, O_m\) be a partition of relevant outcomes. Let \(D(O_j)\) be the desirability, utility, or value that the agent assigns to outcome \(O_j\). The source attributes to Gibbard and Harper the following EDT value function:

\[
V(A)=\sum_{j} P(O_j \mid A)\,D(O_j).
\]

Here \(P(O_j \mid A)\) is the agent’s conditional probability that outcome \(O_j\) will occur given that the action \(A\) is performed. EDT recommends choosing an action \(A^*\) such that

\[
A^* \in \arg\max_A V(A).
\]

The quantity \(V(A)\) is often called the *news value* of \(A\). The idea is not necessarily that \(A\) causes the best outcome, but that receiving the news “you did \(A\)” would be the most welcome news among the available alternatives.

This formulation treats actions as propositions or events to which probabilities can be assigned. That is a distinctive feature. In many standard presentations of decision theory, an action is not something the agent assigns a probability to; it is something the agent chooses. EDT, however, needs probabilities of acts because it asks: given that act \(A\) occurs, what should I expect?

A useful equivalent formulation, not explicitly in the source but helpful for applying EDT, introduces states of the world. Let \(S\) range over possible states, where a state includes all facts relevant to the outcome besides the action itself: what is in the boxes, what other agents will do, what predictors have predicted, what lesions or dispositions exist, and so on. Let \(f(A,S)\) be the outcome produced by action \(A\) in state \(S\). Then EDT can be written as

\[
V(A)=\sum_S P(S \mid A)\,D(f(A,S)).
\]

This makes clear that EDT evaluates an action by conditioning on the action and then averaging over the states that the action makes probable.

If \(P(A)=0\), the conditional probability \(P(O \mid A)\) is not defined by the elementary ratio formula. The source does not discuss this problem, but it matters in deterministic or highly self-referential cases. A reasonable operational approach is to use a regular conditional probability, or to approximate the case by adding small uncertainty or noise to the agent’s choice. For example, instead of saying that the agent will certainly one-box or two-box, we can model the choice as having a tiny probability of error and then take a limit. This preserves the evidential structure while avoiding division by zero.

---

## 2. EDT and counterfactuals

The source contrasts EDT with causal decision theory using the formula

\[
U(A)=\sum_j P(A \mathrel{\Box\!\rightarrow} O_j)\,D(O_j),
\]

where \(A \mathrel{\Box\!\rightarrow} O_j\) is read as “if \(A\) were performed, \(O_j\) would obtain.” This is a counterfactual probability. CDT asks what would happen in the nearest possible world, or under the appropriate intervention, in which the agent performs \(A\). EDT asks instead what is probable conditional on the proposition that \(A\) is performed.

The difference can be expressed using interventionist notation, although this is my own gloss rather than a claim made directly by the source. Let \(do(A)\) mean that \(A\) is intervened upon, rather than merely observed. CDT often evaluates something like

\[
P(O_j \mid do(A)),
\]

whereas EDT evaluates

\[
P(O_j \mid A).
\]

These coincide when the action is probabilistically independent of relevant background states except through its causal effects. But they can diverge when the action is evidence for something else that affects the outcome.

A simple causal-network way to see the difference is this. If \(S\) represents background states, then EDT computes

\[
P(O \mid A)=\sum_S P(O \mid A,S)P(S \mid A).
\]

An interventionist version, often associated with CDT, computes

\[
P(O \mid do(A))=\sum_S P(O \mid A,S)P(S),
\]

assuming the intervention does not change the prior distribution of background states. The only difference is \(P(S \mid A)\) versus \(P(S)\). EDT lets the action update you about the state; CDT holds the state fixed in the relevant counterfactual or intervention.

Thus EDT is sensitive to any probabilistic dependency between action and outcome, whether that dependency is causal, evidential, logical, or due to common causes. If choosing \(A\) is correlated with a hidden state that affects \(O\), EDT counts that correlation as decision-relevant. CDT usually does not, unless the action causally affects \(O\).

This is the central philosophical disagreement. Critics, as the source notes, accuse EDT of “managing the news.” David Lewis is quoted as calling it an irrational policy of managing the news, and James Joyce is quoted as saying that rational agents choose acts on the basis of causal efficacy, not auspiciousness. EDT’s defenders reply that if your action is genuinely strong evidence for a better outcome, it is rational to choose the action that is evidence for that outcome, even if the evidential link is not causal.

---

## 3. Newcomb’s paradox

The source’s main example is Newcomb’s paradox. A predictor, said to be 99% reliable, has predicted whether the agent will take only box B or both boxes A and B. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The agent chooses after the predictor has already made the prediction.

EDT evaluates the two actions by conditional probabilities. Let “one-box” mean taking only B, and “two-box” mean taking both A and B. If the predictor is 99% accurate, the source gives:

\[
\begin{aligned}
V(\text{one-box})
&= P(\text{\$1M in B} \mid \text{one-box}) \cdot \$1{,}000{,}000 \\
&\quad + P(\text{\$0 in B} \mid \text{one-box}) \cdot \$0 \\
&= 0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0 \\
&= \$990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{two-box})
&= P(\text{\$1M in B} \mid \text{two-box}) \cdot \$1{,}001{,}000 \\
&\quad + P(\text{\$0 in B} \mid \text{two-box}) \cdot \$1{,}000 \\
&= 0.01 \cdot \$1{,}001{,}000 + 0.99 \cdot \$1{,}000 \\
&= \$11{,}000.
\end{aligned}
\]

Since \(\$990{,}000 > \$11{,}000\), EDT recommends one-boxing.

The reason is evidential. Choosing only B is strong evidence that the predictor predicted one-boxing, and therefore strong evidence that B contains the million dollars. Choosing both boxes is strong evidence that the predictor predicted two-boxing, and therefore strong evidence that B is empty.

CDT gives the opposite verdict. The prediction has already been made and the contents of B have already been fixed. The current choice cannot causally change what is in B. Two-boxing always yields \$1,000 more than one-boxing, regardless of whether B contains the million. So CDT recommends two-boxing.

A small extension, not required by the source, helps clarify the EDT calculation. Suppose the predictor is accurate with probability \(p\), where accuracy is symmetric: \(P(\text{predict one-box} \mid \text{one-box})=p\) and \(P(\text{predict two-box} \mid \text{two-box})=p\). Then

\[
V(\text{one-box}) = p \cdot \$1{,}000{,}000,
\]

while

\[
V(\text{two-box})
= (1-p)\cdot \$1{,}001{,}000 + p \cdot \$1{,}000.
\]

One-boxing is better when

\[
p \cdot 1{,}000{,}000
>
(1-p)\cdot 1{,}001{,}000 + p \cdot 1{,}000.
\]

Solving gives

\[
p > 0.5005.
\]

So EDT one-boxes even if the predictor is only slightly better than chance, because the payoff asymmetry is so large. This illustrates a general point: EDT’s recommendation depends on the strength of the evidential correlation and the utilities of the outcomes.

---

## 4. Twin prisoner’s dilemma and correlated agents

The source also discusses a variant of the prisoner’s dilemma involving psychological twins. Aomame and her twin are separated and cannot communicate. Their reasoning processes are exactly analogous. The payoffs are:

- both cooperate: each gets \$5;
- both defect: each gets \$1;
- one cooperates, one defects: cooperator gets \$0, defector gets \$10.

The source assumes perfect correlation: if Aomame cooperates, her twin will certainly cooperate; if Aomame defects, her twin will certainly defect. EDT then gives:

\[
\begin{aligned}
V(\text{Aomame cooperates})
&= P(\text{twin cooperates} \mid \text{Aomame cooperates}) \cdot \$5 \\
&\quad + P(\text{twin defects} \mid \text{Aomame cooperates}) \cdot \$0 \\
&= 1 \cdot \$5 + 0 \cdot \$0 = \$5,
\end{aligned}
\]

and

\[
\begin{aligned}
V(\text{Aomame defects})
&= P(\text{twin cooperates} \mid \text{Aomame defects}) \cdot \$10 \\
&\quad + P(\text{twin defects} \mid \text{Aomame defects}) \cdot \$1 \\
&= 0 \cdot \$10 + 1 \cdot \$1 = \$1.
\end{aligned}
\]

EDT therefore recommends cooperation.

Again, the dependency is not causal. Aomame’s choice does not cause her twin’s choice. But her choice is perfect evidence of her twin’s choice. EDT uses that evidence.

We can generalize this example slightly. Suppose the correlation is imperfect but symmetric. Let

\[
r = P(\text{twin cooperates} \mid \text{Aomame cooperates})
= P(\text{twin defects} \mid \text{Aomame defects}).
\]

Then

\[
V(C)=5r,
\]

while

\[
V(D)=10(1-r)+1r = 10-9r.
\]

Cooperation is EDT-preferred when

\[
5r > 10 - 9r,
\]

so

\[
14r > 10,
\]

or

\[
r > \frac{5}{7} \approx 0.714.
\]

Thus EDT does not say “always cooperate in prisoner’s dilemmas.” It says: cooperate when your action is sufficiently strong evidence that the other party will cooperate. In an ordinary one-shot prisoner’s dilemma with a stranger whose choice is independent of yours, EDT reduces to the standard dominance argument and recommends defection. The distinctive EDT cooperation arises only when there is a relevant evidential dependency.

This point connects to the source’s brief “supporting argument” that EDT may matter especially when many correlated decision-makers are involved. The source cites MacAskill et al.’s “Evidentialist’s Wager”: even if one is not fully convinced by EDT, it may be prudent to act as if EDT is true because if many agents are evidentially correlated with you, the stakes of EDT-style reasoning can be large. This is a claim from the source, though its full defense belongs to the cited paper.

---

## 5. Policies, algorithms, and generalized EDT

The source mainly presents EDT as a theory of individual acts. But many decision problems involve policies: rules, algorithms, or dispositions that map observations to actions. A natural EDT extension, and one I am adding beyond the explicit source, is to evaluate policies in the same evidential way.

Let \(\Pi\) be a policy. Let \(O\) be an outcome. Define

\[
V(\pi)=\sum_o P(O=o \mid \Pi=\pi)\,D(O=o).
\]

Here the event \(\Pi=\pi\) means that the agent implements policy \(\pi\). If multiple agents use similar policies, or if predictors can predict the policy, then conditioning on \(\Pi=\pi\) may carry information about what others do and what outcomes occur.

This is useful for problems involving copies, twins, simulations, or logically correlated agents. Suppose many agents face similar choices and use the same decision procedure. EDT can say that choosing a cooperative policy is valuable not because your individual act causes others to cooperate, but because your use of that policy is evidence that others are using it too. In this way, EDT can resemble Hofstadter-style superrationality, although the source does not develop that connection in detail.

For practical use, I would propose the following EDT procedure:

1. Identify the available actions or policies.
2. Identify the relevant outcomes and assign utilities.
3. Build a probability model over acts, states, predictors, other agents, and outcomes.
4. For each candidate action or policy \(A\), compute \(P(O \mid A)\) by conditionalizing on the proposition that \(A\) is performed or implemented.
5. Compute \(V(A)=\sum_O P(O \mid A)D(O)\).
6. Choose an action or policy with maximal \(V\).

The difficult step is usually step 3. EDT itself does not tell you where the conditional probabilities come from. They must be supplied by the agent’s credences, symmetry considerations, observed frequencies, a causal model plus correlation structure, or assumptions about predictors and similar agents.

---

## 6. Open questions and an operational interpretation

The source leaves several important questions open.

First, it does not fully explain how an EDT agent should assign probabilities to her own actions. In ordinary Bayesian reasoning, one conditionalizes on evidence. But when deciding, the agent does not yet know which action she will perform. EDT nevertheless needs \(P(O \mid A)\) for actions the agent may or may not take. A reasonable operational interpretation is to use a prior or deliberative probability distribution over actions and states, before the agent treats her final choice as settled. The question is not “What do I believe will happen given that I will certainly do what I end up doing?” but rather “If I learned that I had done \(A\), how would my expectations change?”

Second, deterministic decision theories create zero-probability alternatives. If an agent knows she is rational and knows EDT, she might conclude that only one action has positive probability. Then conditioning on the alternatives becomes problematic. My proposed solution is to avoid sharp zero probabilities. One can model the decision process as slightly stochastic, or use conditional probabilities defined by limits. This is not merely a mathematical trick; it reflects the fact that decision-making often involves genuine uncertainty about one’s own future choice, especially in self-referential problems involving predictors or twin agents.

Third, the source mentions the Sleeping Beauty problem but does not resolve it. It says EDT has been applied to avoid Dutch books against certain credences, but also notes Conitzer’s argument that halfers may still be vulnerable even after adopting EDT. The underlying issue is how to handle centered evidence, self-locating uncertainty, and repeated betting opportunities. EDT can be applied, but the correct application depends on how one models awakenings, bets, and conditioning events. The source correctly signals disagreement rather than settling the matter.

Fourth, there is the criticism that EDT confuses evidence with causation. This is not merely a technical objection; it reflects a deep philosophical divide. Consider a case where an action is a symptom of a good outcome but does not cause it. EDT may favor the action because it is good news. CDT will reject the action if it lacks causal efficacy. The source quotes Lewis and Joyce to emphasize this worry. Whether this is a fatal objection depends on whether one thinks rational action is essentially about producing good outcomes or about choosing propositions whose truth is associated with good outcomes.

An operational defense of EDT can be formulated as follows. If the agent’s probability model correctly represents all evidential dependencies, then \(P(O \mid A)\) is exactly the expectation she would have upon learning that she performed \(A\). If she values outcomes according to \(D\), then \(V(A)\) is the value of that news. EDT is therefore coherent as a theory of preference over propositions: choose the act-proposition with highest conditional desirability. Whether this is the best theory of agency is another question, but the formal procedure is clear.

---

## Conclusion

Evidential decision theory recommends the action with the highest expected utility computed by conditional probabilities:

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Its distinctive feature is that it treats an action as evidence about the world. It therefore recommends one-boxing in Newcomb’s problem and cooperating in twin prisoner’s dilemmas when one’s choice is strong evidence of another’s choice. It diverges from causal decision theory because conditional probabilities and counterfactual or interventionist probabilities can differ. EDT counts predictive, logical, and common-cause correlations as decision-relevant; CDT generally does not.

The source gives the central formula and examples. My additions include a state-space formulation, a policy formulation, threshold calculations, and an operational approach to zero-probability actions and self-referential choice. EDT remains philosophically controversial because it can appear to choose good news rather than good causation. But as a formal decision procedure, it is precise: model the evidential dependencies, conditionalize on each possible act or policy, and choose the one whose news is best.

---

## References

Gibbard, Allan, and William L. Harper. 1976. “Counterfactuals and Two Kinds of Expected Utility.”

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.”

Conitzer, Vincent. 2015. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192 (9): 2887–2899.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688. Wikimedia Foundation.