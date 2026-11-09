# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00016

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/04066add-13e8-4b25-9142-d3b0c522f289/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/04066add-13e8-4b25-9142-d3b0c522f289/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Expected Utility as Counterfactual Intervention

## 1. The central idea

Causal decision theory (CDT) is a school of decision theory holding that a rational agent should choose the action that *causes* the best expected outcome. The reference article summarizes the contrast with evidential decision theory (EDT) as follows: EDT recommends the action that would be the best *news* if one learned that it had been taken, while CDT recommends the action with the best expected causal consequences. If eating an apple causes happiness and eating an orange causes sadness, CDT says eat the apple. If the apple may be good or bad, CDT says to maximize the *expected* causal effect, weighting possible outcomes by their probabilities and utilities.

The classic formal statement, due to Allan Gibbard and William Harper, defines the causal expected utility of an action \(A\) by

\[
U(A)=\sum_j P(A \mathbin{\square\!\to} O_j)\,D(O_j),
\]

where \(O_j\) ranges over possible outcomes, \(D(O_j)\) is the desirability or utility of outcome \(O_j\), and \(P(A \mathbin{\square\!\to} O_j)\) is the probability of the counterfactual: “if \(A\) were performed, \(O_j\) would obtain.” The arrow here is not material implication and is not generally the conditional probability \(P(O_j\mid A)\). It is meant to capture what would happen under the hypothetical performance of \(A\), not merely what \(A\) would indicate.

EDT, by contrast, uses ordinary conditional probabilities:

\[
U_{\text{EDT}}(A)=\sum_j P(O_j\mid A)\,D(O_j).
\]

The difference is small when actions are probabilistically independent of the relevant counterfactuals, but it becomes decisive when an action is evidence about background conditions that also affect the outcome.

## 2. Counterfactual probabilities versus conditional probabilities

David Lewis argued that probabilities of conditionals cannot generally be identified with conditional probabilities. In the present context, this means

\[
P(A \mathbin{\square\!\to} O) \neq P(O\mid A)
\]

in general. If equality always held, CDT would collapse into EDT.

Gibbard and Harper showed that, given certain assumptions about counterfactual logic—including a principle related to conditional excluded middle—statistical independence between \(A\) and the counterfactual \(A \mathbin{\square\!\to} O_j\) is enough to make the two calculations agree. In many ordinary decisions, performing an action does not tell you anything surprising about what that action would cause. In such cases, CDT and EDT give the same recommendation.

They diverge when the action is evidence for a background variable that influences the outcome but is not itself changed by the action. The reference article illustrates this with the case of King David. David wants Bathsheba but fears that summoning her may provoke revolt. He knows that kings are either charismatic or uncharismatic, that charisma is fixed in adulthood, that charismatic kings tend to act justly and rarely face successful revolts, and that uncharismatic kings tend to act unjustly and often face successful revolts. Crucially, the article says that unjust acts themselves do not cause revolts; the revolt risk comes from the king’s underlying character.

Let \(C\) be the proposition that David is charismatic, \(S\) the action of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is roughly:

\[
C \longrightarrow S, \qquad C \longrightarrow R,
\]

but, by stipulation, \(S\) does not cause \(R\). EDT evaluates

\[
U_{\text{EDT}}(S)=D(S\land \neg R)P(\neg R\mid S)+D(S\land R)P(R\mid S).
\]

Because summoning Bathsheba is evidence that David is uncharismatic, \(P(R\mid S)\) may be high. EDT may therefore recommend abstaining. CDT instead asks what would happen if David intervened to make \(S\) true. Since \(S\) does not affect \(C\), and \(C\) is the common cause of both \(S\) and \(R\), the relevant probability is not \(P(R\mid S)\) but something like \(P(R\mid do(S))\), where \(do(S)\) means “bring about \(S\) by intervention.” If summoning does not causally raise the revolt probability, then

\[
P(R\mid do(S))=P(R),
\]

or at least it is not inflated merely because \(S\) is evidence of uncharismatic character. CDT can therefore recommend summoning Bathsheba if the benefit outweighs the baseline revolt risk.

This example captures the core CDT principle: correlations induced by common causes are not reasons to act unless the action causally changes the outcome.

## 3. An operational interpretation: interventions and causal models

The reference article emphasizes an important gap: CDT itself does not specify an algorithm for computing the counterfactual probabilities \(P(A \mathbin{\square\!\to} O_j)\). One proposal mentioned there is Lewis’s “imaging” technique: to evaluate \(P(A \mathbin{\square\!\to} O)\), move probability mass from each possible world to the closest possible world in which \(A\) holds. But this requires a notion of closeness among possible worlds, and Shaffer’s regress objection says that we may need to know what we would believe if we were certain of \(A\), which itself may be uncertain.

A natural operational interpretation—one that I add to the source rather than find in it—is to use structural causal models or causal Bayesian networks. This is not the only possible interpretation of CDT, but it gives a precise recipe for many decision problems.

Let a causal model contain variables, structural equations, and a probability distribution over exogenous noise variables. Suppose \(A\) is the action variable and \(O\) is the outcome variable. An intervention setting \(A=a\) is written \(do(A=a)\). Formally, the intervention replaces the structural equation for \(A\) with the equation \(A:=a\), while leaving the other structural equations unchanged. The probability of outcome \(o\) under that intervention is

\[
P(o\mid do(a)).
\]

Then the causal expected utility of action \(a\) is

\[
U_{\text{CDT}}(a)=\sum_o u(o)P(o\mid do(a)).
\]

Equivalently, if \(\mathbf{U}\) denotes the exogenous variables of the model and \(O_a(\mathbf{u})\) is the value that the outcome would take in world \(\mathbf{u}\) under intervention \(do(A=a)\), then

\[
U_{\text{CDT}}(a)
=
\sum_{\mathbf{u}} P(\mathbf{u})\,u(O_a(\mathbf{u})).
\]

This formula makes the counterfactual idea concrete: for each possible background state of the world, hold that state fixed, change the action by intervention, propagate the effects forward through the causal system, and evaluate the resulting outcome. Then average over the agent’s prior distribution on background states.

This interventionist reading also clarifies how CDT treats dependencies. If a variable \(K\) is a common cause of both action and outcome, then conditioning on the action may change the probability of \(K\), but intervening on the action does not. In a causal graph, intervening on \(A\) cuts all arrows into \(A\); only variables downstream of \(A\) are affected. Thus CDT distinguishes:

1. **Causal dependence of outcome on action**: counted by CDT.  
2. **Evidential dependence of action on common causes**: ignored by CDT unless it affects causal consequences.  
3. **Logical or predictive correlations without causal influence**: generally ignored by standard CDT, although this is exactly where many counterexamples arise.

When the agent is uncertain about the causal structure itself, we can average over dependency hypotheses or causal models. Let \(K\) index possible causal structures, with prior probabilities \(P(K)\). Then a natural extension is

\[
U_{\text{CDT}}(a)
=
\sum_k P(K=k)\sum_o u(o)P(o\mid do_k(a),K=k).
\]

Here \(P(K=k)\) is the agent’s prior credence in causal structure \(k\), not necessarily the conditional credence \(P(K=k\mid a)\). This reflects the idea that the action does not change the causal structure, even if performing the action would be evidence about it. This “holding fixed” feature is central to CDT and is also the target of Andy Egan’s criticism, discussed below.

## 4. Evaluating policies, not only single actions

CDT can also evaluate policies. A policy is a rule mapping information states to actions. Suppose a policy \(\pi\) says: when the agent observes \(X=x\), take action \(A=\pi(x)\). In an interventionist semantics, the policy is evaluated by replacing the action variable’s structural equation with

\[
A:=\pi(X).
\]

The causal expected utility of the policy is then

\[
U_{\text{CDT}}(\pi)
=
\mathbb{E}\bigl[u(O)\mid do(A:=\pi(X))\bigr].
\]

For sequential decisions, one replaces each decision variable \(A_t\) with a policy function of the history \(H_t\):

\[
A_t := \pi_t(H_t).
\]

Then

\[
U_{\text{CDT}}(\pi)
=
\mathbb{E}\bigl[u(O)\mid do(A_t:=\pi_t(H_t)\text{ for all }t)\bigr].
\]

This gives a clear operational rule: to compare policies, simulate the world under the intervention that the agent follows each policy, and compare the expected utilities of the resulting outcome distributions.

This policy viewpoint is useful because many apparent paradoxes involve not merely a one-off action but a decision rule that predictors can anticipate. If a predictor predicts the agent’s policy, CDT still asks whether adopting that policy causally improves outcomes, given the agent’s causal model.

## 5. Simple example: the uncertain apple

Begin with the reference article’s informal example. Eating an apple may cause happiness if the apple is good, or sadness if it is bad. Let \(G\) be the proposition that the apple is good, with prior probability \(p\). Let \(u_H\) be the utility of happiness and \(u_S\) the utility of sadness. Eating an orange gives known utility \(u_O\).

CDT evaluates eating the apple as

\[
U_{\text{CDT}}(\text{apple})
=
p u_H + (1-p)u_S.
\]

It evaluates eating the orange as

\[
U_{\text{CDT}}(\text{orange})=u_O.
\]

The agent eats the apple iff

\[
p u_H + (1-p)u_S > u_O.
\]

Here CDT and EDT agree, because the apple’s goodness is not plausibly affected by the action and there is no problematic common cause making the action itself evidence about the outcome.

## 6. Newcomb’s problem

Newcomb’s problem is the most famous test case. A predictor has predicted whether the agent will take both boxes or only one. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The predictor is highly reliable, say 99% accurate. The agent chooses after the prediction has been made.

Let \(B\) be the amount in Box B and \(T\) the choice: one-box or two-box. The causal structure is:

\[
\text{Predictor} \longrightarrow B,
\]

and the predictor is correlated with \(T\), but, by the usual setup, \(T\) does not causally affect the predictor’s earlier prediction. Therefore, under CDT,

\[
P(B\mid do(T=\text{two})) = P(B),
\]

and similarly for one-boxing. The action does not change what is already in Box B.

For every possible background state in which Box B contains some amount \(b\), two-boxing yields \(b+1000\), while one-boxing yields \(b\). Thus

\[
U_{\text{CDT}}(\text{two})
=
\mathbb{E}[B]+1000,
\]

while

\[
U_{\text{CDT}}(\text{one})
=
\mathbb{E}[B].
\]

Two-boxing dominates by \$1,000. CDT therefore recommends taking both boxes.

EDT reasons differently. Taking only Box B is strong evidence that the predictor predicted one-boxing, so

\[
P(B=1{,}000{,}000\mid \text{one})
\]

is high. Taking both boxes is strong evidence that Box B is empty, so

\[
P(B=0\mid \text{two})
\]

is high. EDT therefore recommends one-boxing. The reference article notes that philosophers disagree about which answer is rational, but CDT’s answer is standardly two-boxing.

The case illustrates CDT’s treatment of predictive correlation. The predictor’s belief matters causally because it caused the box contents, but the agent’s current choice does not cause the predictor’s past belief. CDT refuses to treat the choice as evidence that changes the past.

## 7. Death in Damascus and predictive counterexamples

The “Death in Damascus” scenario creates a related difficulty. Death predicts where you will be tomorrow and waits there. You know Death is a reliable predictor. If you are currently in Damascus and Death says it has an appointment with you tomorrow in Damascus, should you flee to Aleppo?

Let \(L\) be your location tomorrow and \(D\) Death’s prediction. Death’s prediction causes Death’s location. If Death is reliable, \(D\) is strongly correlated with \(L\), but your choice of location does not causally affect Death’s earlier prediction. CDT may evaluate fleeing by holding Death’s prediction fixed. If your current evidence suggests Death predicted you will stay in Damascus, fleeing seems causally advantageous. But if you become inclined to flee, that inclination is evidence that Death predicted fleeing, which makes staying look better. The agent may have no stable CDT-ratifiable choice.

The reference article says that CDT may be unable to process the correlation and may make irrational decisions. The deeper issue is that CDT evaluates actions by holding fixed the agent’s prior causal picture, but in predictor problems the action is strong evidence about what the predictor predicted. Standard CDT treats the prediction as causally fixed, but this can produce unstable or exploitable behavior.

A related example from the source is the Adversarial Offer. Two boxes are offered; the buyer may buy one or none, but not both. Each box costs \$1. Yesterday, the seller put \$3 in each box that she predicted the buyer would not acquire. Both believe the seller’s prediction is accurate with probability 0.75. The article says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, exceeding the \$1 cost; hence CDT requires buying a box. Yet the offer is profitable for the seller.

The exact calculation depends on how one models the seller’s predictions and the symmetry between boxes. But the intended lesson is clear: CDT can be exploited when an adversarial predictor places payoffs in locations anti-correlated with the agent’s choices. The agent’s local causal calculation says buying a box has positive expected value, while the global predictive setup ensures that the chosen box is likely empty or the total transaction benefits the seller. This kind of example pressures CDT to explain which dependencies should be held fixed and how counterfactuals should be computed when the agent’s choice procedure is predictable.

## 8. The Psychopath Button and common causes

Another counterexample mentioned in the source is the Psychopath Button. Paul can press a button that kills all psychopaths. Paul thinks a world without psychopaths would be much better. But he is also confident that only a psychopath would press such a button. Paul prefers living in a world with psychopaths to dying.

Let \(P\) be the proposition that Paul is a psychopath, \(B\) the action of pressing, and \(W\) the resulting world. Psychopathy may cause Paul to be inclined to press, while pressing causes the elimination of psychopaths. If Paul is not a psychopath, pressing may produce a better world. If Paul is a psychopath, pressing kills him, which he regards as worse than living with psychopaths.

CDT holds Paul’s psychopathy status fixed when evaluating the causal effect of pressing. If \(p=P(P)\), a simplified causal expected utility calculation is

\[
U_{\text{CDT}}(B)
=
(1-p)u(\text{no psychopaths, alive})
+
p u(\text{death}),
\]

while

\[
U_{\text{CDT}}(\neg B)
=
(1-p)u(\text{psychopaths, alive})
+
p u(\text{psychopaths, alive}).
\]

If the benefit of a psychopath-free world is large enough relative to Paul’s prior probability of being a psychopath, CDT can recommend pressing. EDT, by contrast, conditions on pressing:

\[
P(P\mid B)
\]

is high, because only a psychopath would press. EDT therefore recommends not pressing. According to the source, Egan argues that CDT endorses pressing even though “pretty much everyone” agrees Paul should not.

Again, the precise recommendation depends on utilities and priors, but the example exposes the tension: CDT treats psychopathy as a background condition not changed by the action, while ordinary intuition treats the action as alarming evidence about that background condition.

## 9. Prisoner’s dilemma with correlated twins

A similar issue arises in a Newcomb-like Prisoner’s Dilemma. Suppose you play against a “twin” whose reasoning is highly correlated with yours, but whose choice is not caused by yours. If you cooperate, the twin is likely to cooperate; if you defect, the twin is likely to defect. EDT may recommend cooperation because cooperating is evidence that the twin will cooperate. Standard CDT treats the twin’s choice as causally independent of yours and evaluates defection as having better causal consequences given either possible choice of the twin. Thus CDT often defects in such cases, while EDT may cooperate.

This is not necessarily a refutation of CDT; a CDT defender may say that causal influence, not correlation, is what matters. But it shows that CDT’s verdicts can conflict with theories that assign decision-relevance to logical or statistical correlations.

## 10. What CDT leaves open

The most important open question in the source is how to compute counterfactual probabilities. The Gibbard–Harper formula is elegant, but it is not a complete algorithm unless we know what the probabilities of counterfactuals are. Lewis’s imaging proposal gives one possible semantics, but it depends on a similarity relation among possible worlds and may generate regress if we must evaluate what we would believe under certainty.

My proposed operational interpretation—using structural causal models and interventions—makes CDT applicable in many technical settings. It replaces “closest possible world” with an explicit model of causal mechanisms. However, this interpretation introduces assumptions not contained in the source:

1. The agent must possess or learn a causal model.  
2. The model must distinguish intervention from conditioning.  
3. The agent must decide which variables are exogenous and which are downstream of the action.  
4. If multiple causal models are possible, the agent must assign priors over them.  
5. The agent must decide whether to update those priors on the contemplated action.

Standard CDT tends to answer the last question by holding dependency hypotheses fixed. Egan argues that this is the source of many counterexamples: CDT says “do what you expect will bring about the best results,” but then computes expectations while holding fixed the agent’s prior credences about causal structure, even when the action is evidence about that structure.

A possible moderate response is to separate two kinds of information:

- Information about the causal structure should be fixed when evaluating interventions, because the action does not change causal structure.
- Information about ordinary states of the world should be incorporated before intervention, provided it is not itself downstream of the action.

This yields a practical recipe:

1. Specify the action or policy.  
2. Specify a causal model or set of dependency hypotheses.  
3. Condition on all admissible evidence that is not caused by the action.  
4. For each action, apply the intervention \(do(A=a)\).  
5. Compute expected utility under the intervened distribution.  
6. Choose the action or policy with maximum causal expected utility.

This recipe does not solve every philosophical problem. It does not tell us what to do when predictions are accurate because of logical correlation, simulation, or shared decision algorithms rather than ordinary causal influence. Nor does it fully settle whether CDT should be modified to require ratifiability, stability, or dynamic consistency. But it does make CDT precise enough for many applications in statistics, artificial intelligence, economics, and policy analysis.

## 11. Conclusion

Causal decision theory evaluates actions by asking what would happen if the agent intervened to perform them. Its core formula replaces conditional probabilities with probabilities of counterfactuals:

\[
U_{\text{CDT}}(A)=\sum_j P(A \mathbin{\square\!\to} O_j)D(O_j).
\]

The theory differs from evidential decision theory precisely when actions are evidence about background conditions that also affect outcomes. In Newcomb’s problem, Death in Damascus, twin Prisoner’s Dilemmas, and the Psychopath Button, CDT’s insistence on causal rather than evidential dependence leads to controversial but structurally intelligible recommendations.

The source article rightly emphasizes that CDT does not by itself supply an algorithm for computing counterfactual probabilities. A reasonable operational interpretation is to model the decision problem causally and evaluate actions with interventions: \(P(o\mid do(a))\). This gives CDT a clear mathematical form and makes it applicable to policies and sequential decisions. The price is that the theory’s verdicts depend on the chosen causal model, and many philosophical counterexamples target exactly that dependency. CDT is therefore best understood not as a self-contained calculator, but as a principled schema: maximize expected utility under the causal consequences of your intervention.

## References

- Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Beliefs, Decision, Chance, and Time*, 153–190.  
- Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.  
- Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.  
- Egan, A. (2007). Some counterexamples to causal decision theory. *Philosophical Review*, 116(1), 93–114.  
- Oesterheld, C., & Conitzer, V. (2021). Extracting money from causal decision theorists. *Philosophical Quarterly*, 71(4), pqaa086.  
- Wikipedia contributors. (2026). Causal decision theory. Revision 1381555528. Wikimedia Foundation. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post about CDT and how to apply it to decision problems, target ~2400-3000 words including references. Need use reference article. Need explain theory, formal definitions, equations, examples, dependencies/counterfactuals, open questions, operational interpretation, distinguish source claims from own assumptions. Finish conclusion. Need likely produce final essay only. Need think in same language as user: English. Need now plan essay.

We need produce about 2400-3000 words. Need include references perhaps minimal. Need careful mathematical definitions: actions, states/outcomes, utilities, EDT vs CDT, counterfactual probabilities P(A □→ O) maybe arrow. Need discuss Gibbard-Harper formula U(A)=∑ P(A → O_j) D(O_j). Need clarify notation: counterfactual probability vs conditional probability. Need discuss causal models (structural causal models, do-operator) as operationalization, since source says CDT doesn't specify algorithm; propose using Pearl's do-calculus / causal Bayesian networks as reasonable operational interpretation. Need distinguish: source doesn't mention Pearl, but we can propose. Need mention Lewis imaging, regress. Need evaluate alternative actions/policies: choose action max causal expected utility. Policies maybe interventions mapping observations to actions; evaluate by expected utility under intervention/policy. Need dependencies: common causes, correlations not causal. Need counterfactuals: holding fixed exogenous variables or closest worlds; intervention cuts incoming arrows to action variable.

Need include examples: apple/orange, David/Bathsheba, Newcomb, Death in Damascus, Adversarial Offer, Psychopath Button, maybe prisoner's dilemma twin. Need show calculations. Need be precise enough to decide unfamiliar cases. Need discuss uncertainty where source leaves open: how calculate counterfactual probabilities; which causal model; imaging vs SCM; regress; dependency hypotheses; whether CDT should update on action? Need propose operational interpretation: assume agent has causal model (DAG + structural equations or conditional distributions) and prior over exogenous variables; action as intervention do(A=a); expected utility EU_CDT(a)=∑_o u(o) P(o | do(a)). For policies π, EU(π)=E[u | do(π)] or sum over states. If no known causal graph, use dependency hypotheses: K partition representing causal structure; EU(a)=∑_K P(K) ∑_o P(o | a, K?) but careful: under dependency hypotheses, if action not causally relevant to K, P_K(o|do(a))=P(o|a,K)? Need define. Could use Joyce/Skyrms dependency hypotheses: states of world specifying causal dependencies between acts and outcomes. CDT maximizes ∑_K P(K) EU_K(a) where EU_K(a)=∑_o P(o | a, K) u(o) if within K action's causal consequences captured by conditional probabilities? Need discuss source: Gibbard-Harper independence condition: if A independent of A→O_j then P(A→O_j)=P(O_j|A). In cases actions and conditionals not independent (David). Need maybe define dependency hypotheses and how CDT holds fixed initial credences in them (Egan criticism). Need mention policies and dynamic choices.

Need maybe include mathematical formalism: Let A finite set acts, O outcomes. For EDT: V_EDT(a)=∑_o u(o) P(o | a). For CDT: V_CDT(a)=∑_o u(o) P(a □→ o). In SCM M=(U,V,F,P(U)), variable A, outcome O. Intervention do(A=a) yields M_a; probability P_a(o)=P(O=o in M_a). V_CDT(a)=E_{M_a}[u(O)]. If action is stochastic policy? do(A~π) or set structural equation A=f_PA(parents) or deterministic? For policy mapping info X to action: modify structural equation for A to π(PA) (or stochastic). Evaluate expected utility after intervention. If policies can influence later variables, need sequential do.

Need explain difference with EDT: conditional probability uses Bayes, may condition on action as evidence about common causes; counterfactual intervention breaks causal arrows into action. Example smoking/genotype? Maybe use David. Need do calculations for David: Let C charismatic, ¬C uncharismatic. Prior p. Outcomes: send for Bathsheba (S) and revolt R maybe utility. Suppose desire Bathsheba benefit b>0, revolt cost c>0. C causes just acts? Actually charisma common cause of actions and revolt; sending does not cause revolt? Source says unjust acts themselves do not cause successful revolts; uncharismatic kings prone due to bearing. So causal graph C -> A (unjust act), C -> R; A maybe not cause R. If David sends, that gives evidence he is uncharismatic, so EDT: P(R|S) high; abstain evidence charismatic, low revolt. CDT: do(S) does not change C, P(R | do(S)) = P(R) or if A not cause R, no increase? More precisely if A no causal effect on R, P(R | do(S))=P(R), maybe plus if sending is unjust? But source says unjust acts themselves do not cause revolt. So CDT says send if benefit outweighs baseline revolt risk. Need formulate.

Newcomb: predictor predicted before; B content determined by prediction. Causal graph: predictor's prediction P causes box content and is correlated with player's choice due to predicting; action T does not cause P or content (assuming past fixed). do(two boxes) doesn't change B content; expected payoff two = 1000 + P(B has million?) Actually under do(two), content remains whatever prior; if predictor reliable, prior probability B full maybe small? But causal expected value: take both yields $1000 plus whatever in B; one yields whatever in B. Since action doesn't affect B, two dominates by $1000. EDT: one-box yields high conditional probability B full. Need calculate with accuracy 0.99 maybe if prior? We can show dominance: if content fixed, two-box always $1000 more than one-box in same world, so CDT two-box.

Death in Damascus: Death predicts location; if you choose stay/flee, Death will be where predicted. CDT sees your action doesn't causally affect Death's prior prediction? But if Death reliable, whatever you choose evidence Death predicted it, so EDT maybe indifferent? Actually Death in Damascus: you meet Death in Damascus, Death surprised says appointment tomorrow in Damascus; you flee to Aleppo; Death predicts? Classic: Death has appointment tomorrow, you flee, but Death predicted you flee? Need CDT may choose based on causal consequences but if predictor perfect, all actions lead death? Egan says unable to process correlation and irrational decisions; variants lose money. Need explain: If Death's prediction correlated with action but not caused by it, CDT may treat actions as independent of prediction, can be unstable: at decision, if you assign high probability Death predicted stay, flee seems causally better; but if you intend flee, update Death predicted flee, then stay seems better, no ratifiable choice. Need discuss.

Adversarial Offer: Two boxes cost $1 each, can buy one or none not both. Seller predicted whether buyer not acquire each; put $3 in each box predicted not acquired. Accuracy 0.75. Source says CDT reasons at least one box contains $3; average box at least $1.50, buys one, profitable for seller. Need understand mathematically: Seller predicts for each box whether buyer won't acquire? If accurate 0.75. Buyer can buy one or none. CDT thinks if buy a specific box, whether box contains $3 was set yesterday based on prediction; action doesn't affect content. Need compute expected value of buying box i: P($3 in i | do(buy i))? Seller predicted not acquire i with prob? If prediction accuracy 0.75 relative to actual buyer behavior. If CDT buyer decides buy one, maybe predictions? The source says at least one box contains $3. Why? Since buyer won't acquire both (constraint) and seller's predictions accurate with 0.75? Maybe if she predicts acquire for both, since buyer can buy at most one, at least one prediction is wrong? Let's reconstruct: seller predicted for each box whether buyer will not acquire. If both predictions are "acquire" (i.e., not not acquire), she put no money in either. But buyer cannot acquire both, so if she predicted acquire both, at least one prediction wrong. Since accuracy 0.75, perhaps cannot have both predictions acquire? Hmm. Let's not overfit; use source's claim: CDT requires buying one because average box causal EV > cost, but seller profits. Need present as counterexample where CDT voluntarily loses money due to adversarial predictor. But need avoid incorrect details. Could state qualitatively: under CDT intervention, buying a box doesn't affect yesterday's placement; given accuracy and constraint, CDT estimates positive expected gain. But the seller designed offer so that ex ante CDT buyers lose. Need maybe compute simple model: Suppose each box independently predicted not-buy with probability? Need maybe avoid exact numbers. But target mathematical essay; examples with calculations helpful. Could formulate a simplified version: Let X_i=1 if seller predicted not acquire i, puts $3. Accuracy 0.75 means P(X_i=1 | buyer does not acquire i)=0.75 and P(X_i=0 | buyer acquires i)=0.75? The buyer must choose at most one. CDT evaluates buying box i: P(X_i=1 | do(buy i)). If predictions are based on pre-action beliefs? If seller accurate 0.75 about actual not-acquire, then P(X_i=1 | do(buy i)) = P(seller predicted buy? no). Under do(buy i), buyer acquires i, so if seller's prediction is counterfactually reliable, P(X_i=1 | do(buy i)) = 0.25? Then expected value 0.25*3 - 1 = -0.25, so wouldn't buy. But source says CDT requires buy, because CDT uses unconditional credences in dependency hypotheses? Hmm maybe need more precise.

Let's search memory: Adversarial Offer from Oesterheld/Conitzer: two boxes, buyer may purchase one or none, each costs $1. Yesterday seller put $3 in each box she predicted buyer not to acquire. Both believe prediction accurate with prob .75. CDT reasons at least one box contains $3 because seller's predictions can't both be "acquire"? Let's derive: If buyer can buy at most one, there are three possible actual acquisitions: none, box1, box2. Seller predicts for each whether not acquire. If both boxes contain $0, then seller predicted acquire for both. But actual can be acquire at most one; so at least one prediction is wrong. If accuracy .75 for each prediction? If both predictions are "acquire", probability both correct maybe at most? Let's formalize: There are two binary predictions Y_i=1 if predicts not acquire, 0 if predicts acquire. Accuracy means for each i, P(Y_i = 1_{not acquire i})=0.75? If Y=(0,0), then actual acquisitions (A1,A2) with at most one true. Correctness: for i with A_i=0, Y_i=0 correct; for i with A_i=1, Y_i=0 incorrect. If none acquired, both correct; if one acquired, one correct one wrong. So conditional probability both predictions correct given Y=(0,0) is at most? If actual none with probability q; if one box with probability 1-q, accuracy per prediction? If both predictions are 0, probability both correct = P(no acquisition | Y=00). If each prediction individually accuracy .75, maybe P(Y_i correct)=0.75. Could P(Y=00) happen? If yes, expected? Source says CDT reasons at least one box contains $3. Maybe because if both empty, seller would have predicted acquire both, but since buyer cannot acquire both, at least one prediction false, contradicting high accuracy? Not exactly.

Maybe the Adversarial Offer: seller predicts buyer will not buy each box; if predicted not buy, puts $3. If buyer chooses one box, CDT calculates: Given you buy one, the other box is not bought. Seller accurate with .75, so the other box likely contains $3. But you cannot buy both; at least one box (the one you don't buy) likely has $3. But you can only buy one, and the box you buy likely empty. However CDT evaluating average? Wait source: "CDT reasons that at least one box contains $3. Therefore, the average box contains at least $1.50 in causal expected value, which is more than the cost. Hence, CDT requires buying one of the two boxes." This is odd: at least one box contains $3 -> average over two boxes >= $1.50. If boxes symmetric, each causal expected value >= $1.50? But if you choose one, perhaps the chosen box's expected value is average due to symmetry. However predictor may make chosen box empty and unchosen full. CDT cannot handle "the box I choose" indexical? Hmm.

Let's not get bogged. We can present source's claim, not fully verify; maybe note that exact calculation depends on modeling predictor and symmetry, but the intended lesson is CDT can be exploited when predictions correlate with action but are not effects. We can also mention if one models seller's prediction as counterfactually reliable, an interventionist CDT might not buy; thus the example presses on how CDT fixes dependency hypotheses. Need be careful distinguishing source vs own.

Psychopath Button: Paul pressing button causes no psychopaths? But only psychopath would press. Common cause: psychopathy P causes pressing B and bad? If pressing kills psychopaths, Paul if psychopath would die? He prefers world with psychopaths to dying. CDT: if he presses, causal effect is kill all psychopaths (if not psychopath? If he is psychopath, pressing kills himself? Source says prefers living with psychopaths to dying; CDT endorses pressing because holding fixed whether psychopath, pressing causes no psychopaths which better unless he dies? Wait if he is psychopath, pressing kills all psychopaths including himself -> death. If he is not psychopath, pressing -> world no psychopaths, good. If he is confident only psychopath would press, evidence he is psychopath, so EDT says don't. CDT: hold fixed psychopathy status; if not psychopath, pressing good; if psychopath, pressing death bad. If prior probability psychopath low? CDT may press if expected causal utility positive. Egan says CDT endorses pressing because Paul quite confident only psychopath would press? Hmm if only psychopath would press, then Paul's action is evidence he's psychopath; CDT holding fixed psychopathy maybe if he is psychopath pressing causes death (bad) vs not pressing live with psychopaths (better), if not psychopath pressing good. So if prior high enough psychopath? Paul quite confident only psychopath would press maybe means he believes if he presses likely psychopath, but CDT ignores evidence. But holding fixed, if psychopath, should not press (death worse). If not, press. So CDT recommendation depends on prior P(psychopath) and utilities. Egan's example probably assumes Paul is unsure whether psychopath, but believes pressing is strong evidence. If causal benefit for non-psychopaths enormous, CDT presses despite high evidence psychopath? Maybe yes. Need present as counterexample: if Paul's prior probability of being psychopath is not too high relative to benefit, CDT says press because intervention does not change psychopathy, but intuitively pressing is evidence he is psychopath and likely fatal. Need not overclaim.

Need include discussion of ratifiability and Egan: CDT holds fixed unconditional credences in dependency hypotheses; can lead to decisions agent expects to regret upon performing? Maybe explain.

Need maybe mention Lewis's triviality result: probability of conditional not equal conditional probability. Need explain formula: P(A→O) = probability of counterfactual "if A were the case, O would be the case". Lewis proved no nontrivial probability conditional satisfying etc. Need not go deep.

Need structure essay:
1. Introduction: decision theory, expected utility, CDT vs EDT.
2. Basic formal setup and EDT formula.
3. CDT formula with counterfactuals, Gibbard-Harper.
4. Operational semantics via interventions/causal models (my proposal): do-operator, SCM, DAG, expected causal utility; policies; dependency hypotheses. Clarify source doesn't mandate SCM; this is a natural operationalization.
5. How to apply step-by-step.
6. Examples: apples uncertainty; David/Bathsheba (common cause); Newcomb (dominance under intervention); maybe prisoner's dilemma/twin; Death in Damascus and adversarial offers, psychopath button as criticisms.
7. Counterfactuals and dependency: imaging vs do; independence condition; regress; open questions; need specify causal model; own operational interpretation and limitations.
8. Policies and sequential decisions: evaluate policy as intervention, dynamic consistency, ratifiability? Maybe integrate.
9. Conclusion.
References: Wikipedia source, Gibbard & Harper, Lewis, Joyce, Pearl maybe (additional), Egan, Oesterheld/Conitzer. Need keep bibliography short.

Word count target 2400-3000. Need produce maybe 2600 words. Need be readable, mathematical. Need likely use LaTeX equations. Need maybe use "□→" or "→" for counterfactual; source uses A -> O_j. Need avoid confusion with material conditional. Use \(A \mathbin{\square\!\to} O\) or \(A \Rightarrow O\). Maybe state I use \(A \counterfact O\). In plain text, can use \(A \hookrightarrow O\) or \(A \,\Box\!\!\to\, O\). For accessibility, use \(A \mathrel{\square\!\to} O\). Need define.

Need ensure no unsupported instructions. Need cite source claims: "According to the reference article..." or "The source reports...". Need distinguish own additions: "The source does not specify... I will use...".

Need maybe include exact formula for CDT under dependency hypotheses:
Let K be dependency hypothesis specifying causal relation. CDT value:
\[
V_{CDT}(a) = \sum_k P(K=k) \sum_o u(o) P(o \mid do_k(a), K=k)
\]
If within K conditional probabilities suffice, \(P(o \mid a, K=k)\). But need careful: if K includes common causes correlated with action? Egan says holding fixed unconditional credences in dependency hypotheses. Could define:
\[
V(a)=\sum_k P(K=k) V_k(a),\quad V_k(a)=\sum_o u(o)P(o|a,K=k)
\]
where \(P(\cdot|a,K=k)\) is the probability conditional on K and on the action, but K is held fixed rather than updated by action. In causal model terms, K represents exogenous causal structure; action intervention does not change K. This matches EDT if K includes all common causes? Hmm.

Maybe better: The Gibbard-Harper formula with counterfactual probabilities can be unpacked by Lewis imaging:
\[
P(A \counterfact O) = \sum_w P(w) P_A(w)
\]
where \(P_A\) is probability distribution obtained by shifting mass from each world w to closest A-worlds. But imaging needs similarity metric. Alternatively SCM:
\[
P(A \counterfact O) = P(O_{A}=o)
\]
where \(O_A\) is value of O under intervention setting A. Good.

Need explain evaluating policies. If actions are one-shot, choose max V(a). For policy π mapping information history h to action a=π(h), value:
\[
V(π)=\mathbb{E}_{do(A_h=π(h))}[u(O)]
\]
More formally in SCM, replace structural equations for action variables by policy equations and compute distribution of outcomes. If stochastic policy, set conditional intervention \(P(A|parents)=π\). The best policy maximizes this. This handles sequential decisions: intervention sets decision rule, not just single variable, and can account for future actions as functions of observations.

Need discuss dependencies and counterfactuals: CDT only cares about causal dependencies from action to outcome; correlations via common causes are treated as evidential, not reasons. But if correlation is due to action causing outcome or outcome's causes being affected by action, included. If predictor's prediction is a cause of outcome (Newcomb box content), but action does not cause predictor, then predictor's effect is fixed; action cannot exploit correlation except if action causally influences predictor (e.g., if prediction made after action? then CDT may one-box? Actually if predictor predicts after? no). If agent can affect predictor's prediction via action? Then CDT accounts.

Need address "how it treats relevant dependencies and counterfactuals". Need emphasize intervention: hold fixed variables not downstream of action; change action variable and propagate downstream. Counterfactual: in each possible world with exogenous variables fixed, ask what outcome would occur if action changed. Average over prior. This is the "closest world" idea but made operational. Need mention backtracking vs non-backtracking counterfactuals: CDT typically uses non-backtracking: if I did A, past causes not changed unless causally dependent on A? In Newcomb, don't backtrack to change predictor. Some debates. Source mentions imaging, closest possible worlds; need note similarity metric must avoid backtracking or else CDT might one-box? We can propose non-backtracking interventionist semantics as reasonable. Need distinguish own.

Need discuss "where source leaves important question open". The source says CDT doesn't specify algorithm to calculate counterfactual probabilities; Lewis imaging regress. We can explain uncertainty: Without a similarity metric/causal model, formula underdetermined. Also in adversarial examples, how to set dependency hypotheses? If predictor is accurate because of simulation or logical correlation, CDT may be incomplete. My operational interpretation: use explicit causal Bayesian network/SCM; if unavailable, use causal dominance/principal principle? Need justify: mathematical precision, connects to statistics and AI, resolves imaging regress by structural equations. But note this extends source; not all CDT philosophers accept Pearl; counterfactuals may need more than DAG (e.g., similarity). But for decision problems, it's a reasonable recipe.

Need maybe include an "algorithm" box:
Given: set of acts A, outcomes O, utility u, causal model M or counterfactual probabilities.
1. For each act a, form intervened model M_a (set A=a).
2. Compute distribution P_{M_a}(O).
3. Compute EU_CDT(a)=∑_o u(o)P_{M_a}(o).
4. Choose a maximizing EU. For policy, replace decision variable equations by policy and compute.

Need maybe include EDT comparison algorithm: EU_EDT(a)=∑ u(o)P(o|a). Need mention if action is evidentially impossible? P(a)=0? Use conditional? Not necessary.

Need include "independence" from Gibbard-Harper: If actions independent of counterfactuals, CDT=EDT. Need define: \(P(A \counterfact O | A)=P(A \counterfact O)\)? They say statistical independence of A and A→O_j suffices. More precisely if \(P(A \counterfact O_j) = P(O_j|A)\) under axioms and independence. Need explain: in ordinary cases where performing A doesn't tell you what A would cause (no common cause linking action and outcome except via action), EDT and CDT agree. Diverge when action is evidence for background causes.

Need maybe mention Lewis triviality result: If probability of conditional equaled conditional probability, trivial; so need counterfactual semantics. Not central.

Need ensure final length. We can draft around 2800 words. Need include references in prose and maybe reference list at end. The word count includes references? Target approx 2400-3000 including references. Need maybe references list of 6-8. Could be 200 words. Essay body ~2500. Need not too long. Let's estimate sections:
- Intro 200
- Formal setup EDT/CDT 400
- Operational interpretation 600
- Examples 800
- Criticisms/open questions 500
- Conclusion 150
- References 150
Total 2800. Good.

Need maybe include equations in markdown.

Potential pitfalls: Need avoid stating CDT always recommends two-boxing as source says; yes. Need be nuanced about Newcomb: CDT recommends two boxes because action doesn't affect prediction/content. Some philosophers disagree. Need mention source says citation needed but claim widely accepted.

Need think more about counterfactual probabilities and "P(A -> O_j) is counterfactual probability of it being case that A necessarily implies O_j". The phrase "necessarily implies" weird. Better: probability that if A were performed, O_j would obtain. Use Stalnaker/Lewis counterfactual. Formula:
\[
U(A)=\sum_j P(A \,\Box\!\to\, O_j)D(O_j)
\]
with \(\sum_j P(A \,\Box\!\to\, O_j)=1\) if outcomes partition possible results of A. In stochastic cases, probabilities sum to 1.

Need define desirability D(O_j) maybe utility u(O_j). Need note if outcomes include all relevant consequences. If actions have uncertain outcomes due to states S, can write:
\[
U_{CDT}(a)=\sum_s P(s) u(o(a,s))
\]
if s causally independent of a? But if s common cause? Need use intervention.

Let's build essay.

Title maybe "Causal Decision Theory: Expected Utility as Counterfactual Intervention".

Opening: decision theory chooses acts based on expected value. But what probability? Evidential conditional vs causal counterfactual. CDT: choose act that would cause best expected outcome. Reference article definition.

Formal: Let \(\mathcal A\) acts, \(\mathcal O\) outcomes, utility \(u: \mathcal O \to \mathbb R\). EDT: \(V_E(a)=\sum_o u(o)P(o|a)\). CDT Gibbard-Harper: \(V_C(a)=\sum_o u(o)P(a\counterfact o)\). Counterfactual probability. Difference: \(P(a\counterfact o)\neq P(o|a)\) generally (Lewis). If independent, equal.

Need maybe note \(P(o|a)\) is conditional credence on news that a was taken; CDT uses "if I were to do a". Good.

Then operationalization: source says CDT doesn't specify algorithm. I propose SCM. Define \(M=(\mathbf U,\mathbf V,\mathbf F,P)\), variables, structural equations. Action variable A. Intervention do(A=a) replaces equation for A by constant a, leaves other equations unchanged, computes distribution of descendants. Then \(P(o|do(a))\) is probability that if A set to a, O=o. Define CDT utility:
\[
V_C(a)=\sum_o u(o)P(o|do(a)).
\]
Equivalently with exogenous variables:
\[
V_C(a)=\sum_{\mathbf u} P(\mathbf u) u(O_{a}(\mathbf u))
\]
where \(O_a(\mathbf u)\) outcome in model under intervention. This matches counterfactual: hold background facts fixed, change act. This avoids imaging regress because structural equations specify closest-world mapping. Need say this is my addition; source only mentions imaging. Also note causal model may be uncertain: average over models/hypotheses K:
\[
V_C(a)=\sum_k P(K=k) \sum_o u(o)P(o|do_k(a),K=k).
\]
This is close to dependency hypotheses. Important: when averaging over K, do not update P(K) on a; hold fixed prior. If learning a would be evidence about K, CDT still uses prior P(K) because K is not caused by a. However if K is causally downstream of a, update via intervention? Hmm K as dependency hypothesis about causal structure should be exogenous. If action provides evidence about K, EDT would update, CDT not. But some CDT formulations allow conditionalizing on act after fixing dependency hypotheses? Need be careful: Egan criticizes holding fixed unconditional credences in dependency hypotheses. So present that.

Policies: For policy π, replace structural equation for A (or sequence A_t) with π. If deterministic policy based on observed variables X: set A=π(X). If stochastic, set distribution. Value:
\[
V_C(π)=\mathbb E[u(O)|do(A:=π(X))].
\]
For sequential decisions, replace all decision variables by policy functions; compute expected final utility. Choose policy maximizing. This covers "alternative actions or policies". Need mention if policy changes information acquisition? Include observations as variables; intervention sets policy but leaves causal effects of observations.

Dependencies: CDT distinguishes causal from evidential dependencies. In DAG, intervention cuts incoming arrows to A; only descendants of A change. Common causes of A and O remain fixed; they create evidential correlation but not causal value. If A causes O directly or via intermediaries, CDT counts. If background variable K causes both A and O, EDT may prefer action that is good news; CDT ignores. If A is evidence about what type of agent you are, CDT treats type as fixed unless action changes it.

Examples:
1. Apple/orange: if apple causes happy, orange sad. If uncertain apple good/bad: states G,B with prior p, utilities h,s. CDT value eat apple = p u(happy)+(1-p)u(sad). If orange known sad, choose if >. This illustrates expected causal consequences. Maybe keep brief.

2. David/Bathsheba: Define C charisma, A send/abstain, R revolt. Utility: being with Bathsheba b>0, revolt cost c>0. C causes A tendencies and R; A does not cause R (per source). EDT: \(P(R|A=send)\) high because send evidence uncharismatic; abstain low. CDT: \(P(R|do(send))=P(R)\) (or baseline unaffected); value send = b - c P(R), abstain = 0 (or -?). If b > cP(R), send. This demonstrates common cause. Need maybe mention source says CDT recommends sending. Need not exact p.

3. Newcomb: variables P prediction (one/two), B content, T choice. P set before, causes B; predictor correlated with T but T does not cause P. Under do(T=two), B unchanged. In every world where B has x, two yields x+1000 vs one yields x; causal dominance. Thus CDT two-box. EDT one-box because \(P(B=1M|one)\approx .99\). Need maybe compute if accuracy q and prior? Could show:
EDT(one)≈q*1M, EDT(two)≈(1-q)*1000? If q=.99, one. CDT: \(V(two)=1000+E[B]\), \(V(one)=E[B]\); two by 1000. This clarifies.

4. Death in Damascus / adversarial offer / psychopath: show criticisms. Need maybe present one by one succinctly.
- Death: Death predicts location. Let L your location, D Death's prediction. D causes Death's location; D correlated with L but not caused by L. CDT evaluating flee vs stay treats D fixed; if prior says Death predicted stay, flee seems safer; but if agent adopts flee, that is evidence D predicted flee, causing instability. Source says CDT unable to process correlation and may make irrational decisions. Need mention ratifiability: no stable choice if perfect predictor.
- Adversarial Offer: source's example. Need describe and state CDT's positive causal EV leads buying, but seller profits; illustrates exploitation. Need maybe include formula: if each box's expected contents under intervention > cost, buy. But due to prediction, the chosen box is likely empty. The source says at least one box contains $3 and average >= $1.50, so CDT buys. I can say "as presented in the source". Need perhaps note exact evaluation depends on symmetry and modeling; the point is CDT's fixed dependency hypotheses can be exploited.
- Psychopath Button: variable P psychopathy, B press, W world. P causes inclination to press; pressing causes psychopaths killed. If Paul not psychopath, pressing good; if psychopath, pressing kills him. CDT holds P fixed; if causal benefit for nonpsychopath sufficiently large relative to prior, it recommends pressing. EDT says pressing is evidence P, so don't. Source says intuitive don't; CDT endorses. Need nuance: recommendation depends on prior/utilities; the counterexample chooses parameters where CDT presses.

Could include Prisoner's Dilemma twin as short: two agents with correlated choices not causal; CDT defects because own choice doesn't cause twin's, EDT cooperates. Source mentions. Maybe include in dependencies section.

Open questions: How obtain causal model? What if predictor accuracy arises from logical correlation, simulation, or identical reasoning? CDT needs causal graph; if choices are logically correlated but not causally, CDT ignores. Some propose update dependency hypotheses or use ratifiable CDT; source mentions Egan. Also counterfactual semantics: Lewis imaging requires closest worlds; regress about what believe if certain of A. My SCM proposal avoids regress if model includes beliefs? But if action changes beliefs? We can say for decision, evaluate outcome not epistemic state; if beliefs are outcomes, model them. However if model itself uncertain, need prior over causal structures; if action provides evidence about structure, CDT's fixed priors may be controversial. Could propose use all available evidence not about action's causal effects? Maybe: before decision, condition on all information that is not downstream of candidate action; then apply intervention. This is standard. Need justify.

Need maybe address "counterfactual probabilities" in terms of possible worlds: For each world w with exogenous state u, define counterfactual world w_a by intervention; \(P(a\counterfact o)=P(\{w: O(w_a)=o\})\). This is mathematically clear.

Need maybe include "Lewis independence" section: Gibbard and Harper axioms. Could write: If \(A\) is probabilistically independent of the counterfactual \(A\counterfact O\), and certain conditional logic axioms hold, then \(P(A\counterfact O)=P(O|A)\). Thus CDT collapses to EDT in benign cases. Divergence when action gives evidence about truth of counterfactual, e.g. David's charisma. Need explain.

Need maybe discuss "principle of conditional excluded middle" controversial. Not dwell.

Need maybe include conclusion: CDT formalizes causal expected utility; powerful when causal model available; underdetermined without counterfactual semantics; counterexamples show tension with predictive/logical correlations. Good.

Need word count. Let's draft final. Need maybe references at end:
1. Wikipedia contributors, "Causal decision theory," revision 1381555528, 2026. (source)
2. Gibbard & Harper 1981.
3. Lewis 1976.
4. Lewis 1981.
5. Egan 2007.
6. Oesterheld & Conitzer 2021.
7. Pearl 2009? Additional. Need maybe include Joyce 2012? We can keep references short. Since source includes many, but we can cite. Need make clear Pearl is my addition.

Need final answer only essay. Ensure around 2600-3000 words. Let's write carefully.

Potential issue: The user asks "Researcher — mathematical essay / blog post explaining CDT and how to apply it to decision problems." Need not answer one case. Good.

Need include mathematical notation robust. Use markdown headings.

Let's draft with approximate word count:

Title + intro ~250.
Section 1: two expectations ~500.
Section 2: interventionist operationalization ~700.
Section 3: examples ~900.
Section 4: open questions ~500.
Conclusion + refs ~350. Total 3200 maybe. Need trim. Target 2400-3000. Keep concise.

Let's write with fewer words but substantive.

Detailed content:

Start:
"Causal decision theory (CDT) is a family of decision rules..." Reference.

Formula:
EDT: \(V_E(a)=\sum_o u(o)P(o\mid a)\).
CDT: \(V_C(a)=\sum_o u(o)P(a\counterfact o)\). Need define \(\counterfact\) as counterfactual conditional.

Maybe mention if outcomes not exhaustive use expectation over consequence function.

Then "The crucial inequality": Lewis proved probability of conditional not conditional probability. Include independence:
If \(A\) independent of \(A\counterfact O\), under axioms, equality. David example.

Operationalization:
"I add a modeling assumption not contained in source: use SCM". Define variables, do. Equation:
\[
P(o|do(a))=\sum_{\mathbf u:O_a(\mathbf u)=o}P(\mathbf u)
\]
Then utility. For uncertain models:
\[
V_C(a)=\sum_m P(M=m)\sum_o u(o)P(o|do_m(a)).
\]
Need note P(M) should be prior not conditioned on a if a is evidence about M; that's Egan point. But if M not dependency hypothesis but ordinary state unaffected by action? Hmm.

Policies:
For policy π: set A=π(X), maybe sequence:
\[
V_C(π)=E[u(O)|do(A_t=π_t(H_t) \text{ for all }t)]
\]
This handles dynamic.

Examples:
Apple: include formula but brief.
David: graph and formula. Let's write:
Let C=charisma. Causal graph C→A? Actually C influences propensity to unjust acts and revolt; A not cause R. Prior p=P(C). If send, utility b if no revolt, b-c if revolt? Value:
\(V_C(send)=b-cP(R|do(send))\). Since do(send) doesn't change C and A not cause R, \(P(R|do(send))=P(R)=pP(R|C)+(1-p)P(R|¬C)\). EDT uses \(P(R|send)\), higher because send more likely under ¬C. CDT send if b>cP(R). Source says sends.

Newcomb: formula:
Let B∈{0,1,000,000}. Given content fixed by prior prediction. For any exogenous state, payoff two = B+1000, one=B. CDT values: \(V_C(two)=E[B]+1000\), \(V_C(one)=E[B]\). EDT: if predictor accuracy .99, \(V_E(one)\approx .99*1M\), \(V_E(two)\approx 1000 + .01*1M?\) Actually if predictor predicts one with high probability when one, two-box conditional B full maybe low: if choose two, predictor likely predicted two, B empty; so \(V_E(two)\approx 1000\). So EDT one. Good.

Death in Damascus: Need maybe concise.

Adversarial Offer: Need phrase carefully. "The reference article describes an Adversarial Offer ... The article says CDT reasons ... Therefore CDT requires buying; yet this is profitable for seller." Then discuss "The example turns on the fact that the box chosen is anti-correlated with money due to predictor; CDT's local intervention calculation can miss the global selection effect." Need maybe note my uncertainty: "A fully specified SCM could alter verdict; if the seller's prediction is represented as counterfactually responsive to the buyer's intervention, the calculation may change. The counterexample therefore also probes what counts as the relevant dependency hypothesis." This addresses open question.

Psychopath: formula:
Let P psychopath prior p. If not P: press -> no psychopaths utility U_good, not press U_status. If P: press -> death utility U_death, not press U_live. CDT:
\(V_C(press)= (1-p)U_good + p U_death\)
\(V_C(not)= (1-p)U_status + p U_live\)
If U_good-U_status large, CDT press. EDT conditions press on P, making p near 1, so not. Good.

Need maybe mention twin prisoner's dilemma in dependencies or examples: one sentence.

Open questions: algorithm for counterfactuals; imaging regress; causal model selection; logical correlations; ratifiability. propose operational recipe: if no causal model, ask for minimal intervention that implements act while holding fixed all variables not causally downstream; use domain knowledge; if multiple models, average over prior; choose ratifiable policy if dynamic? Need maybe suggest "if CDT is to be used computationally, one must supply a causal graph or structural equations; without it the theory is a schema, not an algorithm." Good.

Need conclusion.

Need ensure word count. I will write with moderate detail. Need maybe include references at end. Let's count roughly after drafting mentally. We can aim 2700. Let's start final.

Need decide notation for counterfactual. Markdown may not render \counterfact. Use \(A \mathbin{\square\!\to} O\). Good. Define.

Potential issue: The formula from source uses \(P(A \to O_j)\) "A necessarily implies O_j". I should note arrow is not material implication. Use \(\square\!\to\). Good.

Need maybe state "desirability D(O_j)" as utility. Good.

Need mention expected utility hypothesis? maybe not.

Let's write final now. Ensure no meta. Need include references. final answer.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e34b4361-8691-4e1e-8bc9-fefe0b3de9ce/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e34b4361-8691-4e1e-8bc9-fefe0b3de9ce/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me analyze this decision problem carefully using CDT as described in the researcher's essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model with the same settings, following CDT.
- We receive different private observations (different incriminating leads), but the leads are equally reliable and have the same effect on the sentencing table.
- The sentencing table is symmetric.
- Utility: U = -years imprisoned (maximize by minimizing years).

**The sentencing table (from my perspective):**

| My action | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

**CDT Analysis:**

The key question for CDT is: what is the causal structure here?

The essay explicitly discusses the "Prisoner's Dilemma with correlated twins" in Section 9:

> "Suppose you play against a 'twin' whose reasoning is highly correlated with yours, but whose choice is not caused by yours. If you cooperate, the twin is likely to cooperate; if you defect, the twin is likely to defect. EDT may recommend cooperation because cooperating is evidence that the twin will cooperate. Standard CDT treats the twin's choice as causally independent of yours and evaluates defection as having better causal consequences given either possible choice of the twin. Thus CDT often defects in such cases."

This is exactly the situation described. We are two independent executions of the same model. My choice does not causally influence Sasha's choice. There is no causal arrow from my action to Sasha's action. The correlation (if any) comes from shared weights/algorithm, but CDT treats this as a non-causal correlation — similar to how CDT treats the predictor's accuracy in Newcomb's problem as irrelevant to the current choice's causal consequences.

**CDT evaluation:**

CDT asks: given each possible state of the world (Sasha sends or doesn't send), what does my action causally produce?

- If Sasha keeps quiet: Sending gives me 0 years, keeping quiet gives me 2 years. Sending is better.
- If Sasha sends a letter: Sending gives me 4 years, keeping quiet gives me 5 years. Sending is better.

Sending the letter strictly dominates keeping quiet regardless of what Sasha does. Under CDT, since my action doesn't causally influence Sasha's action, I should evaluate each action by its causal consequences holding Sasha's action fixed.

The fact that we're the same model and might make similar choices is an evidential correlation, not a causal one. CDT explicitly ignores such correlations (as discussed in the essay's treatment of Newcomb's problem and twin PDs).

**Conclusion:** CDT recommends sending the letter (defecting).

The command is: `submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e34b4361-8691-4e1e-8bc9-fefe0b3de9ce/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e34b4361-8691-4e1e-8bc9-fefe0b3de9ce/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as described in the researcher's essay.

**The Setup:**
- I am "Sasha" playing a Prisoner's Dilemma against "Rowan"
- Rowan is described as another execution of the same LLM model with the same weights and settings
- We receive different private observations but the same essay and decision theory assignment
- The sentencing table is symmetric

**The Payoff Matrix (for me):**
| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| I keep quiet | 2 years | 5 years |
| I send letter | 0 years | 4 years |

My utility is U = -years imprisoned.

**CDT Analysis:**

The key question for CDT is: does my action causally influence Rowan's action?

The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

CDT treats the other player's choice as causally independent of mine. The essay's Section 9 explicitly addresses this: "Standard CDT treats the twin's choice as causally independent of yours and evaluates defection as having better causal consequences given either possible choice of the twin. Thus CDT often defects in such cases."

Let me verify by checking dominance:
- If Rowan keeps quiet: I get 0 years by sending, 2 years by keeping quiet → sending is better
- If Rowan sends: I get 4 years by sending, 5 years by keeping quiet → sending is better

Sending the letter strictly dominates keeping quiet regardless of what Rowan does. This is a standard Prisoner's Dilemma where defection (sending the letter) is the dominant strategy.

CDT holds Rowan's choice fixed (as causally independent) and evaluates my intervention. Under either possible state of Rowan's action, sending the letter gives me a better outcome. Therefore CDT recommends sending the letter.

The fact that Rowan is a copy of the same model doesn't change the CDT analysis. The essay explicitly says CDT ignores logical/predictive correlations without causal influence. Section 9: "CDT treats the twin's choice as causally independent of yours and evaluates defection as having better causal consequences given either possible choice of the twin."

My command should be to submit the letter.
```
