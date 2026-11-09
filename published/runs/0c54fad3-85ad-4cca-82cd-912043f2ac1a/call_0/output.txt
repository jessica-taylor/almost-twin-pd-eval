# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) is a Bayesian approach to rational choice that evaluates actions by their *news value*. According to the reference article, EDT recommends choosing the action that would be the best evidence, in expectation, of a good outcome: “do what you most want to learn that you will do” (Ahmed 2021). If you were to receive the news that you had performed action \(A\), how good should you then expect the world to be? EDT says that a rational agent should choose the action for which that conditional expectation is highest.

This makes EDT formally simple but philosophically provocative. In many ordinary decisions, acting is good news precisely because the action causally produces good outcomes. But in cases involving prediction, correlation, duplicated agents, or logical dependence, an action can be excellent evidence for a good outcome without causally bringing it about. EDT treats those evidential connections as decision-relevant. Causal decision theory (CDT), by contrast, evaluates what an action would *produce* under an intervention or counterfactual supposition. The source article notes that the two theories agree in many cases but diverge in thought experiments such as Newcomb’s problem, where EDT one-boxes and CDT two-boxes.

This essay explains EDT’s central formula, shows how to apply it to concrete decisions, and discusses how it treats dependencies, policies, and counterfactuals. Where the source is silent—especially about policies and zero-probability actions—I will state my own operational interpretation explicitly.

---

## 1. The basic EDT calculation

Let an agent face a finite set of possible actions, represented as mutually exclusive propositions

\[
A_1, A_2, \dots, A_n,
\]

where \(A_i\) means “the agent performs action \(i\).” Let the possible relevant outcomes be another partition

\[
O_1, O_2, \dots, O_m,
\]

where each \(O_j\) represents a complete description of the consequences that matter to the agent. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). Finally, let \(P\) be the agent’s subjective probability function, conditional on all background evidence \(K\). EDT assigns to action \(A_i\) the value

\[
V(A_i \mid K)=\sum_{j=1}^m P(O_j \mid A_i \wedge K)\,D(O_j).
\]

Often the background \(K\) is suppressed, giving the source article’s simpler expression, attributed to Gibbard and Harper:

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

The EDT prescription is then:

\[
\text{Choose } A_i \text{ such that } V(A_i\mid K) \text{ is maximal.}
\]

Equivalently, one can work with states of the world rather than outcomes. Let \(S_1,\dots,S_r\) be states that determine the consequences of actions, and let \(u(A_i,S_k)\) be the utility of performing \(A_i\) when state \(S_k\) obtains. Then

\[
V(A_i)=\sum_{k=1}^r P(S_k \mid A_i)\,u(A_i,S_k).
\]

This state-space form is often the most practical. The central task is to determine the conditional probabilities \(P(S_k\mid A_i)\): given that the agent performs \(A_i\), how likely is each relevant state?

The formula assumes \(P(A_i\mid K)>0\). The source does not discuss what EDT should say if the agent is already certain which action she will take, making some conditional probabilities undefined. A reasonable operational interpretation, which I will use below, is to model deliberation as a situation in which each live option has positive subjective probability, perhaps because of small uncertainty, randomization, or implementation noise. One can then take limits as the noise goes to zero, if the limit exists. This is not explicitly in the source, but it gives EDT a usable procedure.

---

## 2. EDT and CDT: conditional probability versus counterfactual intervention

The source article contrasts EDT with causal decision theory. CDT uses a counterfactual expected utility:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) means something like “if \(A\) were performed, \(O_j\) would obtain.” The probability is over counterfactual situations in which the agent performs \(A\), not merely over evidence that \(A\) has been performed.

In modern causal language, EDT conditions on observing \(A\), while CDT conditions on intervening to make \(A\) happen. If observing that \(A\) occurred is probabilistically equivalent to intervening on \(A\), the two theories agree. They diverge when the action is correlated with relevant states for reasons other than its causal efficacy.

A simple non-decision analogy may help. A falling barometer is evidence of a storm. But breaking the barometer does not cause a storm. EDT is sensitive to the first relation—evidence—while CDT asks about the second—causal production. In decision problems, this distinction becomes crucial when an action is a symptom, a prediction target, or a correlate of another agent’s behavior.

The source article’s examples illustrate exactly this. In Newcomb’s problem, taking only box B is strong evidence that a reliable predictor predicted one-boxing and therefore filled box B with money. In the twin prisoner’s dilemma, cooperating is strong evidence that a psychologically identical twin will also cooperate. EDT counts these evidential connections.

---

## 3. Newcomb’s problem

Newcomb’s problem is the classic test case. There is a predictor and two boxes, A and B. Box A is transparent and contains \$1,000. Box B is opaque and has already been filled according to the predictor’s prediction:

- If the predictor predicted that the player will take both boxes, box B contains \$0.
- If the predictor predicted that the player will take only box B, box B contains \$1,000,000.

The player can either take both boxes or take only box B. Suppose the predictor is accurate with probability \(q=0.99\). The source article models this as

\[
P(\text{predict one-box} \mid \text{one-box}) = 0.99,
\]

and similarly for two-boxing.

The relevant utilities are:

\[
\begin{array}{c|cc}
& \text{B contains \$1M} & \text{B contains \$0} \\
\hline
\text{One-box} & 1{,}000{,}000 & 0 \\
\text{Two-box} & 1{,}001{,}000 & 1{,}000
\end{array}
\]

EDT computes conditional expected values:

\[
\begin{aligned}
V(\text{one-box})
&= P(\text{\$1M in B}\mid \text{one-box})\cdot 1{,}000{,}000 \\
&\quad + P(\text{\$0 in B}\mid \text{one-box})\cdot 0 \\
&= 0.99\cdot 1{,}000{,}000 + 0.01\cdot 0 \\
&= 990{,}000.
\end{aligned}
\]

For two-boxing:

\[
\begin{aligned}
V(\text{two-box})
&= P(\text{\$1M in B}\mid \text{two-box})\cdot 1{,}001{,}000 \\
&\quad + P(\text{\$0 in B}\mid \text{two-box})\cdot 1{,}000 \\
&= 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 \\
&= 10{,}010 + 990 \\
&= 11{,}000.
\end{aligned}
\]

Since \(990{,}000 > 11{,}000\), EDT recommends one-boxing.

More generally, if the predictor matches the player’s choice with probability \(q\), then

\[
V(\text{one-box}) = qM,
\]

where \(M=1{,}000{,}000\), while

\[
V(\text{two-box}) = (1-q)(M+1000)+q(1000)
= (1-q)M + 1000.
\]

EDT one-boxes when

\[
qM > (1-q)M + 1000,
\]

or

\[
(2q-1)M > 1000.
\]

With \(M=1{,}000{,}000\), this requires \(q>0.5005\). Thus even a barely reliable predictor can make one-boxing the EDT recommendation, provided the payoff in box B is large enough.

CDT reasons differently. Once the predictor has made its prediction, the contents of box B are fixed. Relative to either possible state—box B full or empty—taking both boxes yields \$1,000 more than taking only B. So CDT two-boxes. The disagreement is not arithmetical but structural: EDT uses \(P(\text{full}\mid \text{action})\); CDT uses the action’s counterfactual or causal consequences.

---

## 4. The twin prisoner’s dilemma

The source article also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin are separated and cannot communicate. Their reasoning processes are exactly analogous. The payoff matrix for Aomame, depending on both choices, is:

\[
\begin{array}{c|cc}
& \text{Twin cooperates} & \text{Twin defects} \\
\hline
\text{Aomame cooperates} & 5 & 0 \\
\text{Aomame defects} & 10 & 1
\end{array}
\]

If the twins are psychologically identical and reason identically, EDT may assign

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates}) = 1,
\]

and

\[
P(\text{twin defects}\mid \text{Aomame defects}) = 1.
\]

Then

\[
\begin{aligned}
V(\text{cooperate})
&= 1\cdot 5 + 0\cdot 0 = 5,\\
V(\text{defect})
&= 0\cdot 10 + 1\cdot 1 = 1.
\end{aligned}
\]

EDT recommends cooperation.

This example shows how EDT can support cooperation in cases where the other agent’s behavior is strongly correlated with one’s own. In an ordinary one-shot prisoner’s dilemma against an independent opponent, cooperation need not be good news about the opponent’s behavior, so EDT may defect. The decisive question is not the payoff matrix alone but the conditional probabilities linking one’s action to the other agent’s action.

It is useful to generalize slightly, beyond the source’s perfect-correlation case. Suppose Aomame believes her twin will make the same choice with probability \(r\). Then

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=r,
\]

and, by symmetry,

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=1-r.
\]

Then

\[
V(C)=5r,
\]

while

\[
V(D)=10(1-r)+1r=10-9r.
\]

Cooperation is EDT-preferred when

\[
5r > 10-9r,
\]

so

\[
14r>10,
\]

or

\[
r>\frac{5}{7}\approx 0.714.
\]

Thus EDT cooperation does not require certainty of correlation; it requires sufficiently strong evidential connection.

---

## 5. How EDT treats dependencies

EDT’s central commitment is that all decision-relevant information is contained in the conditional probabilities \(P(O_j\mid A_i)\). These conditionals may reflect many different kinds of dependence:

1. **Causal dependence of outcomes on actions.**  
   If exercising improves health, then \(P(\text{good health}\mid \text{exercise})\) may be high because exercise causes good health.

2. **Common causes.**  
   An action may be correlated with an outcome because a third factor causes both. For example, a medical condition might cause both a certain behavior and a later health outcome. EDT treats the behavior as evidence of the outcome.

3. **Prediction.**  
   If a reliable predictor has already predicted the agent’s action, then the action is evidence of the prediction and of consequences that depend on the prediction. Newcomb’s problem is of this kind.

4. **Correlated agents.**  
   If two agents share psychology, source code, training, or environment, one agent’s action can be evidence of the other’s action. The twin prisoner’s dilemma is the cleanest example.

5. **Logical or mathematical dependence.**  
   Some EDT-friendly arguments extend the idea to cases where multiple agents run the same computation or face structurally identical decisions. The source does not develop this in detail, but it is a natural extension of the twin case.

EDT does not, by itself, distinguish these sources of correlation. It asks only: if I learned that I had done \(A\), what should I then believe about the outcomes? This is why critics say EDT promotes “managing the news.” The theory is not exclusively interested in what the agent causally brings about; it is interested in what the agent’s action indicates.

For unfamiliar cases, the practical burden is therefore probabilistic. One must construct a probability model that includes the relevant actions, states, predictions, and other agents. The EDT recommendation can change dramatically if the conditional probabilities change. Sensitivity analysis is often wise: if a small change in \(P(S_k\mid A_i)\) reverses the recommendation, the decision depends on fragile evidential assumptions.

---

## 6. Policies, not merely one-shot actions

The source article formulates EDT for actions, not explicitly for policies. A policy is a rule mapping possible observations or histories to actions. Many real decisions are of this kind: one chooses a plan, disposition, algorithm, or strategy, not merely a single immediate act.

A natural EDT extension, which I propose rather than find explicitly in the source, is to treat a policy as a proposition and evaluate its news value. Let \(\Pi\) range over possible policies, and let \(\Pi=\pi\) mean “the agent has, adopts, or implements policy \(\pi\).” Then define

\[
V(\pi\mid K)=\mathbb{E}[D(O)\mid \Pi=\pi \wedge K].
\]

In finite form:

\[
V(\pi\mid K)=\sum_w P(w\mid \Pi=\pi\wedge K)D(w),
\]

where \(w\) ranges over complete possible worlds and \(D(w)\) is the desirability of world \(w\).

This formulation allows EDT to evaluate policies in sequential or multi-agent settings. If a predictor predicts not merely a single action but the agent’s general policy, EDT conditions on the proposition that the agent has that policy. If a twin, copy, or similar agent uses the same policy, news that I use a cooperative policy is evidence that the other uses a cooperative policy.

There is a subtlety, however. In sequential problems, the ex ante value of a policy and the local value of an action at a later history can diverge. Suppose a policy \(\pi\) prescribes action \(a\) at history \(h\). Ex ante, EDT may favor \(\pi\) because news of adopting \(\pi\) correlates with favorable predictions or correlated agents. But once \(h\) occurs, the agent may compute

\[
V(a\mid h,K)=\mathbb{E}[D(O)\mid A=a \wedge H=h \wedge K]
\]

and may prefer to deviate. EDT is not automatically dynamically consistent in such settings. The source does not resolve this.

A reasonable operational rule is:

- If the agent can choose and commit to a policy before later evidence arrives, evaluate policies ex ante by \(V(\pi)\).
- If the agent cannot commit and is genuinely choosing at a later node, evaluate the available local actions by conditional news value given the current history.

This rule does not eliminate all tension, but it gives a workable procedure. It also preserves the core EDT idea: choose what would be the best news, relative to the proposition actually being decided.

The same zero-probability problem arises for policies. If the agent is certain she already has policy \(\pi\), conditioning on alternative policies may be undefined. My proposed interpretation is again to give candidate policies positive subjective probability during deliberation, or to model policy selection with small random perturbations. For example, one might suppose the agent is likely but not certain to follow a given plan, or that implementation has a small error rate. The EDT value is then computed from the resulting conditional distribution and, if appropriate, taken to a limit. This operationalizes EDT but adds modeling assumptions not supplied by the source.

---

## 7. Counterfactuals in EDT

EDT’s relation to counterfactuals is delicate. The source contrasts EDT’s conditional probability formula with CDT’s counterfactual formula. But EDT also uses a kind of counterfactual reasoning: it asks what the agent should expect conditional on the supposition that she performs \(A\). The difference is that this supposition is treated evidentially, not interventionally.

An EDT counterfactual has the form:

> If I were to learn that I had done \(A\), what would I then infer about the world?

A CDT counterfactual has the form:

> If I were to intervene to make \(A\) happen, what would then happen?

In Newcomb’s problem, EDT asks: if I learned that I one-boxed, what would that tell me about the predictor’s earlier prediction? It answers: it would make it very likely that the predictor predicted one-boxing, hence very likely that box B contains \$1,000,000. CDT asks: given the past prediction, what does my current choice causally change? It answers: it adds or does not add the visible \$1,000, but does not change the contents of box B.

This distinction explains why EDT can recommend actions that seem “irrational” from a purely causal perspective. The action is chosen not because it produces the desired outcome but because it is auspicious. The source quotes David Lewis’s criticism that EDT promotes “an irrational policy of managing the news,” and James Joyce’s claim that rational agents choose acts on the basis of “causal efficacy,” not auspiciousness.

An EDT defender might respond that if an agent’s preferences are over total worlds, and if the agent’s action is strongly correlated with better worlds, then choosing that action is a rational expression of those preferences. The dispute is not merely mathematical; it is about what decision theory is for. Is choice a tool for causing outcomes, or is it also a locus of evidence about the world?

---

## 8. Sleeping Beauty, Dutch books, and higher stakes

The source article briefly mentions two further issues.

First, EDT has been applied to the Sleeping Beauty problem. The article says that EDT has been used to avoid Dutch book arguments against certain credences, but it also notes Vincent Conitzer’s argument that halfers can still be Dutch-booked even if they adopt EDT. This indicates that EDT’s relationship to self-locating belief and dynamic consistency remains technically contested.

Second, the source mentions an argument sometimes called the evidentialist’s wager: even if one is not fully convinced by EDT, it may be prudent to act as if EDT is true in contexts involving many correlated decision-makers. If EDT counts correlations that CDT ignores, then the stakes attached to EDT-relevant dependencies may be large. This is a pragmatic supporting argument rather than a derivation of EDT from more basic principles.

Both points are suggestive but not central to the basic EDT recipe. The core algorithm remains: identify the act or policy, condition on it, compute expected utility.

---

## 9. Practical recipe for applying EDT

A reader who wants to apply EDT to an unfamiliar decision problem can proceed as follows.

1. **Specify the options.**  
   List the actions or policies under consideration. Make them mutually exclusive and exhaustive, or refine them until they are.

2. **Specify the outcomes or states.**  
   Identify the uncertain facts that affect the consequences: predictor states, other agents’ choices, medical states, environmental states, etc.

3. **Assign utilities.**  
   Give each outcome or action-state pair a desirability \(D(O_j)\) or \(u(A_i,S_k)\). If money is not linearly valuable, use utility rather than raw monetary payoff.

4. **Assign conditional probabilities.**  
   For each option \(A_i\), estimate \(P(S_k\mid A_i)\) or \(P(O_j\mid A_i)\), conditional on background evidence. Include correlations from prediction, common causes, similarity, or logical dependence.

5. **Compute EDT values.**  
   Use

   \[
   V(A_i)=\sum_k P(S_k\mid A_i)u(A_i,S_k).
   \]

6. **Choose the maximum.**  
   Select the action or policy with the highest EDT value.

7. **Check robustness.**  
   If the recommendation depends on fragile conditional probabilities, investigate how much confidence is justified. EDT is only as good as the agent’s model of evidential dependencies.

This recipe makes clear where EDT differs from naïve expected utility reasoning. Standard expected utility often implicitly assumes that actions are probabilistically independent of states unless the action causes the state. EDT rejects that implicit restriction. It demands explicit conditional probabilities.

---

## 10. Conclusion

Evidential decision theory offers a clean and mathematically simple principle: choose the action or policy that would be the best news. Its formal core is conditional expected utility,

\[
V(A)=\sum_j P(O_j\mid A)D(O_j),
\]

contrasted with causal decision theory’s counterfactual or interventionist expected utility. EDT treats actions as evidence about the world. It therefore gives weight to predictors, twins, correlated agents, common causes, and other noncausal dependencies.

The theory’s strength is also its controversy. By valuing auspiciousness as well as efficacy, EDT can recommend one-boxing in Newcomb’s problem and cooperating in twin prisoner’s dilemmas. But critics argue that rational action should aim to bring about good outcomes, not merely to be correlated with them. Whether one accepts EDT depends partly on formal considerations about probability and partly on deeper views about what choice is for.

For practical purposes, EDT can be applied by explicitly modeling actions, outcomes, utilities, and conditional probabilities. When extended to policies by conditioning on the proposition that a policy is adopted, EDT can address sequential and multi-agent decisions, though questions about dynamic consistency and zero-probability options require additional operational assumptions. With those assumptions stated, EDT becomes a usable decision procedure: ask what you would most want to learn that you had done, and do that.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Conitzer, Vincent. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, no. 9 (2015): 2887–2899.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, 2026. Licensed under CC BY-SA 4.0.