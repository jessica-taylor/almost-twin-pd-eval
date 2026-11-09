# Evidential Decision Theory: Choosing the Best News

Evidential decision theory, or EDT, is a normative theory of choice under uncertainty. Its central instruction is strikingly simple: choose the action that would be the best news to learn you have chosen. The supplied reference article expresses this by saying that EDT recommends the action with the highest “news value,” or, in Arif Ahmed’s phrase, that one should “do what you most want to learn that you will do.”[^1]

This makes EDT sound subjective or even aesthetic: choose the act that looks best as a sign. But the theory can be given a precise probabilistic form. EDT says that an agent should evaluate each available action by the expected desirability of outcomes conditional on that action being performed. The conditional probability here is ordinary Bayesian conditionalization, not an interventionist or explicitly causal notion. That small formal difference produces large philosophical consequences. EDT and causal decision theory often agree, but they diverge in famous cases such as Newcomb’s problem and certain prisoner’s dilemmas involving copies, twins, or highly correlated agents.

This essay explains EDT as a working decision procedure. It gives the formal definition, explains how to apply it to unfamiliar problems, discusses how it treats dependencies and counterfactuals, and identifies places where the theory needs supplementary assumptions, especially for policies, sequential decisions, and self-locating cases. I distinguish the claims of the source article from additional operational proposals that I will introduce where the source is silent.

---

## 1. The formal core of EDT

Suppose an agent faces a finite set of possible actions \( \mathcal{A} \). Let \( O_1, O_2, \ldots \) be a partition of possible outcomes relevant to the decision. The agent has:

1. A probability function \( P \), representing her credences over propositions, including propositions about her own actions and about outcomes.
2. A desirability or utility function \( D(O_j) \), representing how good outcome \( O_j \) is.

The reference article attributes to Allan Gibbard and William Harper the following EDT value function:[^2]

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Here:

- \( A \) is a candidate action.
- \( P(O_j \mid A) \) is the conditional probability of outcome \( O_j \) given that the agent performs \( A \).
- \( D(O_j) \) is the desirability of that outcome.

EDT recommends choosing an action \( A^* \) such that

\[
V(A^*) \geq V(A)
\]

for every available action \( A \). If outcomes are continuous, the sum becomes an integral:

\[
V(A)=\int D(o)\,dP(o \mid A).
\]

The important feature is the conditioning term \( P(O_j \mid A) \). EDT asks: if I learned as news that I had done \( A \), how would that news change my expectations about the outcome? The action is treated as evidence.

The source contrasts this with causal decision theory, or CDT, which uses a counterfactual expected utility:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \( A \mathrel{\Box\rightarrow} O_j \) is read roughly as “if \( A \) were performed, \( O_j \) would obtain.”[^3] In modern causal-model language, CDT is often interpreted as evaluating \( P(O_j \mid do(A)) \), the probability of \( O_j \) under an intervention that sets the action to \( A \), while EDT evaluates the observational conditional \( P(O_j \mid A) \).

The two formulas agree when the observational and interventional probabilities coincide. They differ when an action is probabilistically associated with an outcome for reasons other than the action causally producing that outcome. EDT counts such associations as decision-relevant. CDT typically does not.

---

## 2. How EDT evaluates actions

A practical EDT calculation has three stages.

### Step 1: Specify the probabilistic model

The agent must represent the decision situation with variables describing actions, states of the world, predictors, other agents, and outcomes. For example, in Newcomb’s problem we need variables for the player’s choice, the predictor’s prediction, and the contents of box B. In a twin prisoner’s dilemma we need variables for the agent’s choice and the twin’s choice.

The model should include all propositions that the agent regards as probabilistically relevant. EDT itself does not tell you what probabilities to assign. It takes the agent’s probability function as input and tells her how to use it.

### Step 2: Condition on each candidate action

For each action \( A \), EDT asks the agent to conditionalize on \( A \). This is not the same as physically performing \( A \). It is the hypothetical update expressed by: “Suppose I learned that I did \( A \).”

This update can change the agent’s beliefs about many things: the past, the predictions of others, the choices of correlated agents, the presence of lesions, the state of the economy, or the likely behavior of an algorithm similar to her own.

### Step 3: Compute conditional expected desirability

After conditioning on \( A \), compute the expected value of the outcome distribution:

\[
V(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Then choose the action with the largest \( V \).

This recipe is simple, but it depends on a subtle point: the agent must be able to assign meaningful conditional probabilities to actions she is deliberating about. If the agent is certain she will perform \( A \), then conditioning on an alternative action may be undefined or unstable. A natural operational remedy, which I add to the source rather than finding it stated there, is to require that the agent’s model leave some positive probability for each live option, perhaps by representing deliberation as slightly noisy. Alternatively, one can use regular conditional probabilities or take limits from small positive probabilities. This is a technical convenience, but it matters for applying EDT rigorously.

---

## 3. What counts as a relevant dependence?

EDT is sensitive to any probabilistic dependence between action and outcome, given the agent’s evidence. The dependence may be causal, but it need not be.

EDT treats the following as relevant:

1. **Direct causal influence**: If smoking causes cancer, then \( P(\text{cancer} \mid \text{smoke}) \) differs from \( P(\text{cancer} \mid \text{not smoke}) \). EDT captures this.
2. **Predictive dependence**: If a predictor has already predicted your choice, then your current choice is evidence of that past prediction.
3. **Common-cause dependence**: If some common cause influences both your action and an outcome, your action can be evidence of that outcome.
4. **Correlation between similar agents**: If your choice is correlated with the choice of a twin, copy, or statistically similar decision-maker, your action is evidence about their action.
5. **Logical or algorithmic dependence**: If you believe another agent runs essentially the same reasoning procedure, your choice may be evidence of theirs even without causal interaction.

The source article illustrates predictive dependence with Newcomb’s problem and algorithmic or psychological dependence with the twin prisoner’s dilemma.[^4]

This breadth is EDT’s distinctive feature. EDT does not ask, “Does my action causally influence the outcome?” It asks, “Would learning that I performed this action change my probability distribution over outcomes in a way that matters?” If yes, EDT counts that as relevant.

---

## 4. Newcomb’s problem

The reference article discusses Newcomb’s problem in detail.[^5] There is a predictor, a player, and two boxes, A and B. Box A is transparent and always contains $1,000. Box B is opaque. The predictor has already filled B according to its prediction:

- If it predicted the player will take both boxes, B contains nothing.
- If it predicted the player will take only B, B contains $1,000,000.

The predictor is highly reliable; the source uses 99% accuracy.

The player chooses between:

- \( A_1 \): take only box B;
- \( A_2 \): take both boxes.

EDT evaluates these actions by conditional probabilities.

If the player takes only B, that is strong evidence that the predictor predicted one-boxing, so B probably contains $1,000,000:

\[
V(\text{take only B})
=0.99 \times \$1{,}000{,}000 + 0.01 \times \$0
= \$990{,}000.
\]

If the player takes both boxes, that is strong evidence that the predictor predicted two-boxing, so B probably contains nothing. The player then gets only the $1,000 in box A:

\[
\begin{aligned}
V(\text{take both boxes})
&=0.01 \times \$1{,}001{,}000 + 0.99 \times \$1{,}000 \\
&= \$10{,}010 + \$990 \\
&= \$11{,}000.
\end{aligned}
\]

Since

\[
\$990{,}000 > \$11{,}000,
\]

EDT recommends taking only B.

The source notes that causal decision theory usually recommends taking both boxes, because the predictor has already acted and the player’s current choice cannot causally change what is in B.[^6] CDT focuses on the causal effect of the present action. EDT focuses on the evidential meaning of the action.

We can generalize the Newcomb calculation. Suppose the predictor is correct with probability \( p \), where \( p > 1/2 \). Then

\[
V(\text{one-box}) = p \cdot 1{,}000{,}000,
\]

while

\[
V(\text{two-box}) = (1-p)\cdot 1{,}001{,}000 + p \cdot 1{,}000.
\]

One-boxing is better when

\[
p \cdot 1{,}000{,}000 > (1-p)\cdot 1{,}001{,}000 + p \cdot 1{,}000.
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

Thus, EDT recommends one-boxing whenever the predictor is even slightly better than a coin flip, given these payoffs. This kind of threshold calculation is useful for unfamiliar Newcomb-like cases: identify the conditional probabilities, multiply by outcome values, and compare.

---

## 5. Twin prisoner’s dilemma

The source article also discusses a twin prisoner’s dilemma.[^7] Aomame and her psychological twin are in separate rooms. They cannot communicate. Their reasoning processes are exactly analogous. The payoffs are:

- Both cooperate: each gets $5.
- Both defect: each gets $1.
- One cooperates, one defects: defector gets $10, cooperator gets $0.

The source assumes Aomame cares only about her own payout.

If Aomame cooperates, this is strong evidence that her twin will also cooperate. With perfect psychological similarity:

\[
P(\text{twin cooperates} \mid \text{Aomame cooperates}) = 1.
\]

So

\[
V(\text{cooperate}) = 1 \cdot \$5 + 0 \cdot \$0 = \$5.
\]

If Aomame defects, this is strong evidence that her twin will also defect:

\[
P(\text{twin defects} \mid \text{Aomame defects}) = 1.
\]

So

\[
V(\text{defect}) = 0 \cdot \$10 + 1 \cdot \$1 = \$1.
\]

EDT therefore recommends cooperation.

This example shows how EDT can yield cooperative behavior in cases where ordinary causal decision theory might defect. Aomame cannot causally influence her twin’s choice, since they are separated and cannot communicate. But her choice is evidence of her twin’s choice. EDT treats that evidential connection as reason to cooperate.

We can again generalize. Suppose the correlation is imperfect. Let

\[
q = P(\text{twin cooperates} \mid \text{Aomame cooperates}),
\]

and

\[
r = P(\text{twin cooperates} \mid \text{Aomame defects}).
\]

Then

\[
V(\text{cooperate}) = 5q + 0(1-q) = 5q,
\]

and

\[
V(\text{defect}) = 10r + 1(1-r) = 1 + 9r.
\]

EDT recommends cooperation when

\[
5q > 1 + 9r.
\]

For perfect twins, \( q=1 \) and \( r=0 \), so cooperation wins easily. For weakly correlated agents, EDT may recommend defection. The general lesson is that EDT does not say “always cooperate with copies.” It says: compute the conditional probabilities induced by the correlation, then maximize conditional expected utility.

---

## 6. Noncausal dependencies and the smoking-lesion objection

The source does not discuss the smoking-lesion problem, but it is a standard way to see both the appeal and the danger of EDT. I introduce it here as an illustration, not as a claim drawn directly from the supplied article.

Suppose smoking does not cause cancer. Instead, a genetic lesion causes both cancer and a disposition to smoke. Smoking is mildly pleasant. If an agent knows that smoking is strong evidence that she has the lesion, then EDT may recommend not smoking, because the news “I smoke” is bad news about her health.

Let \( L \) be the lesion, \( C \) cancer, and \( S \) smoking. Suppose the agent’s model gives

\[
P(C \mid S) = 0.9,
\]

and

\[
P(C \mid \neg S) = 0.1.
\]

Let smoking without cancer have utility \(1\), not smoking without cancer have utility \(0\), and cancer have utility \(-100\), regardless of smoking. Then

\[
V(S) = 0.9(-100) + 0.1(1) = -89.9,
\]

while

\[
V(\neg S) = 0.1(-100) + 0.9(0) = -10.
\]

EDT recommends not smoking, because smoking is terrible news. But if smoking does not causally affect cancer, this seems to many philosophers like the wrong answer. The agent should smoke and receive the small pleasure, since her choice does not affect the lesion or the cancer.

This is one route to the criticism quoted in the source article. David Lewis characterized EDT as promoting “an irrational policy of managing the news,” and James Joyce argued that rational agents choose acts based on causal efficacy, not auspiciousness.[^8] On this view, EDT mistakenly treats good signs as good actions.

An EDT defender might respond in several ways. One might argue that real-world cases are rarely so cleanly stripped of causal structure. Or one might argue that if an agent’s action is strongly correlated with bad outcomes because of stable features of the agent, avoiding the action can still be part of a generally successful pattern. But the smoking-lesion style case remains a central reason many philosophers prefer CDT.

---

## 7. Policies, sequences, and dynamic choice

The source article mainly presents EDT as evaluating individual actions. But many decisions are about policies rather than isolated acts. A policy is a function from situations to actions. For example, a policy in a sequential problem might say: “If I see red, choose left; if I see blue, choose right.”

The source does not fully specify how EDT should handle policies. I will propose a natural extension.

Let \( \Pi \) be the set of possible policies. Let \( H \) be a set of possible histories, including observations, states, and actions, and let \( O(h) \) be the outcome of history \( h \). If the agent chooses policy \( \pi \), EDT can evaluate it by conditioning on the proposition that the agent follows \( \pi \):

\[
V(\pi) = \sum_h P(H=h \mid \pi)D(O(h)).
\]

Equivalently, if outcomes are directly associated with policies,

\[
V(\pi)=\sum_o P(O=o \mid \pi)D(o).
\]

This is not a new principle; it is the same EDT idea applied to a richer object. Choosing a policy is also news. If I learn that I have adopted a cooperative policy, that may be evidence that similar agents will cooperate with me. If I learn that I have adopted a one-boxing policy in Newcomb-like situations, that may be evidence that predictors have filled the opaque box with a large reward.

Policy evaluation matters because EDT can otherwise appear vulnerable to dynamic inconsistency. An agent might evaluate a future action differently once she imagines herself at the moment of choice. To avoid this, EDT should often evaluate the whole plan or disposition that the agent is adopting, not merely the isolated act abstracted from its deliberative context. This is my operational proposal for making EDT applicable to sequential problems; the source itself does not settle the issue.

---

## 8. Sleeping Beauty and self-locating uncertainty

The source briefly mentions the Sleeping Beauty problem.[^9] In the classic setup, a fair coin is tossed. If it lands heads, Sleeping Beauty is awakened once. If it lands tails, she is awakened twice, with amnesia between awakenings. Each time she awakens, she is asked for her credence that the coin landed heads.

The source says EDT has been applied to this problem to avoid Dutch book arguments, but that Vincent Conitzer has argued that halfers can still be Dutch-booked even after adopting EDT.[^10] The article therefore leaves the matter unresolved.

The deeper issue is that EDT requires conditional probabilities, but Sleeping Beauty disputes often concern the correct prior probabilities over centered worlds. Should Beauty assign \( P(\text{heads} \mid \text{awake}) = 1/2 \), as halfers say, or \( 1/3 \), as thirders say? EDT by itself does not answer that question. It evaluates acts conditional on probabilities; it does not uniquely determine those probabilities in self-locating cases.

A reasonable operational interpretation, which again I add to the source, is this: when applying EDT to a self-locating problem, the agent should condition on the full centered proposition describing her current decision situation. For example, she should condition not merely on “I am awake,” but on “I am awake now, in this epistemic situation, facing this choice.” The outcome space should include centered outcomes if the agent cares about which person-moment receives a payoff.

With that convention, EDT can evaluate bets or choices once the agent has settled on a credence function. But the halfer/thirder debate remains an input dispute, not something EDT alone resolves. The source’s mention of Dutch books should therefore be read cautiously: EDT may help coordinate probabilities and decisions, but it does not automatically supply the correct self-locating probabilities.

---

## 9. Correlated decision-makers and the evidentialist wager

The source includes an argument that even if one is not fully confident in EDT, it may be reasonable to act as if EDT were true.[^11] The idea is that EDT often involves many correlated decision-makers. If your action is evidence of what many similar agents do, then the stakes of EDT-style reasoning can be large.

For example, in large populations of similar agents facing prisoner’s-dilemma-like choices, EDT may recommend cooperation because one’s own cooperation is evidence of widespread cooperation. If many agents reason this way, the total payoff difference between EDT and CDT can be enormous.

This argument is not a proof that EDT is correct. It is more like a pragmatic or expected-value argument for adopting EDT in contexts where correlation among agents is plausible. It connects EDT to ideas such as superrationality and coordination among similar algorithms. The source lists superrationality among related topics, though it does not develop the connection in detail.[^12]

---

## 10. Criticism and the contrast with causal decision theory

The source presents EDT as a serious theory but also records strong criticisms. Lewis says EDT manages the news rather than acting rationally; Joyce says rational agents act to bring about good results, not merely to be associated with good news.[^13]

The philosophical dispute can be summarized as follows.

EDT says:

> Choose the act that would be the best evidence of a good outcome.

CDT says:

> Choose the act that would causally produce the best outcome.

In many ordinary cases, the best evidence of a good outcome is also the act that causally produces it. If you are deciding whether to carry an umbrella, learning that you carried an umbrella is usually evidence that rain was likely, but carrying the umbrella also causally prevents getting wet. EDT and CDT agree.

They diverge when evidence and causation separate. Newcomb’s problem is the most famous such case. EDT one-boxes because one-boxing is evidence of a filled box. CDT two-boxes because the box contents are already fixed. The twin prisoner’s dilemma is another. EDT cooperates because cooperation is evidence of twin cooperation. CDT may defect because the twin’s action is already fixed.

Which theory is correct depends on what one thinks decision theory is for. If the goal is to select actions that are causally efficacious, CDT looks attractive. If the goal is to select actions that are, from the agent’s epistemic standpoint, most strongly associated with good outcomes, EDT looks attractive. EDT’s defenders can point to cases where one-boxers and cooperators actually do better, at least when predictors and correlations are reliable.

---

## 11. Using EDT in unfamiliar cases

A reader who wants to apply EDT to a new decision problem can use the following checklist.

1. **List the available actions.**  
   For example: cooperate, defect; one-box, two-box; smoke, refrain.

2. **List the relevant outcomes.**  
   Include everything the agent cares about: money, health, consequences for others, perhaps reputational or logical consequences if they enter the utility function.

3. **Assign desirabilities \(D(O_j)\).**  
   These should reflect the agent’s values. EDT is not a theory of value; it assumes utilities are given.

4. **Build a probabilistic model.**  
   Include predictors, common causes, correlated agents, and any information the agent has.

5. **Compute \(P(O_j \mid A)\) for each action.**  
   Condition on the action as news. Do not replace this with an intervention unless you are intentionally switching to CDT.

6. **Compute \(V(A)=\sum_j P(O_j \mid A)D(O_j)\).**

7. **Choose the action with highest \(V(A)\).**

8. **If choosing a policy, condition on the policy as a whole.**  
   This is my suggested operational extension for dynamic cases.

This procedure is precise enough for many thought experiments and real decisions. The hardest part is usually not the EDT formula itself but constructing the probability model: deciding what variables matter, what dependencies exist, and what probabilities are justified.

---

## Conclusion

Evidential decision theory evaluates actions by their conditional expected utility. Its core equation,

\[
V(A)=\sum_j P(O_j \mid A)D(O_j),
\]

captures the idea that rational choice should be guided by what an action indicates, not only by what it causes. In Newcomb’s problem, EDT one-boxes because one-boxing is strong evidence of a large payoff. In the twin prisoner’s dilemma, EDT cooperates because cooperation is evidence of twin cooperation. In cases involving many correlated agents, EDT can recommend cooperative or coordinated behavior even where causal influence is absent.

The theory is elegant and mathematically simple. Its difficulty lies in its permissive treatment of noncausal dependencies. Critics argue that EDT rewards good news rather than good causation. Defenders argue that when predictions, correlations, and similarities are real, evidential connections are exactly what a rational agent should exploit.

At minimum, EDT gives a clear procedure: specify your probabilities, condition on each possible action as if learning it as news, compute expected desirability, and choose the act with the highest value. Whether that is the final word on rational choice depends on deeper disputes about causation, counterfactuals, and the purpose of decision theory. But as a formal framework, EDT is precise enough to guide decisions in unfamiliar cases, provided the agent supplies a well-articulated probabilistic model of the situation.

---

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. Licensed under CC BY-SA 4.0.

[^1]: Wikipedia contributors, “Evidential Decision Theory,” revision 1373679688 (2026), citing Ahmed, *Evidential Decision Theory*, 7.
[^2]: Wikipedia article, citing Gibbard and Harper, “Counterfactuals and Two Kinds of Expected Utility” (1976).
[^3]: Wikipedia article, formal description section.
[^4]: Wikipedia article, “Newcomb’s paradox” and “Twin prisoner’s dilemma” sections.
[^5]: Wikipedia article, “Newcomb’s paradox.”
[^6]: Wikipedia article, “Newcomb’s paradox.”
[^7]: Wikipedia article, “Twin prisoner’s dilemma,” citing Greene and Levinstein.
[^8]: Wikipedia article, “Criticism,” citing Lewis (1981) and Joyce (1999).
[^9]: Wikipedia article, “Sleeping beauty problem.”
[^10]: Wikipedia article, citing Conitzer (2015).
[^11]: Wikipedia article, “Other supporting arguments,” citing MacAskill et al., “The Evidentialist’s Wager.”
[^12]: Wikipedia article, “See also.”
[^13]: Wikipedia article, “Criticism.”