# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00018

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/872e594b-f7bc-4777-bba2-53e285075a5f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/872e594b-f7bc-4777-bba2-53e285075a5f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Causal Decision Theory: Choosing by Expected Causal Consequences

Causal decision theory (CDT) is a school of thought in decision theory holding that a rational agent should choose the action that causes the best expected outcome. The contrast is with evidential decision theory (EDT), which chooses the action that would be the best *news*—the action whose occurrence would be most strongly associated with good outcomes, conditional on observing that it was taken. The supplied reference article summarizes this contrast and gives the classical counterfactual formulation due to Gibbard and Harper (1981). My aim here is to make the theory precise enough to apply, to explain how it treats dependencies and counterfactuals, and to develop a reasonable operational interpretation where the source leaves the theory under-specified.

I will distinguish between claims made by the source and additional assumptions I introduce. In particular, the source gives the core CDT formula but, as it notes, does not specify an algorithm for computing counterfactual probabilities. I will suggest that modern causal-model machinery—Pearl-style interventions and structural counterfactuals—provides a natural operational reading, although this is an addition to the source rather than a claim contained in it.

---

## 1. Expected utility: evidential versus causal

Consider a finite decision problem with possible actions \(A \in \mathcal A\), outcomes \(O_j \in \mathcal O\), and a desirability or utility function \(D(O_j)\). An evidential decision theorist evaluates an action by conditional expected utility:

\[
U_E(A)=\sum_j P(O_j \mid A)D(O_j).
\]

Here \(P(O_j\mid A)\) is the ordinary conditional probability of outcome \(O_j\) given that the agent performs \(A\). This quantity captures the *evidential* bearing of the action: if we learned that the agent had done \(A\), how probable would \(O_j\) be?

CDT instead uses the formula given in the source, attributed to Gibbard and Harper:

\[
U_C(A)=\sum_j P(A \to O_j)D(O_j),
\]

where \(P(A \to O_j)\) is the probability of the counterfactual: “if the agent were to do \(A\), then \(O_j\) would obtain.” To avoid confusion with material implication, it is common to write this as \(A \mathbin{\Box\!\to} O_j\). Thus:

\[
U_C(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)D(O_j).
\]

The essential claim is that rational choice should be guided by the probabilities of what the action would *bring about*, not merely by what the action would *indicate*.

The source notes that Lewis proved the probability of a conditional need not equal the corresponding conditional probability:

\[
P(A \mathbin{\Box\!\to} O_j) \neq P(O_j\mid A)
\]

in general. If equality always held, CDT and EDT would collapse into the same theory. But they can come apart when the action is evidence about background conditions that also affect outcomes, without causing those background conditions.

A simple way to express the difference is through “dependency hypotheses.” Let \(K\) be a variable describing a complete causal structure: which actions causally influence which outcomes, and with what probabilities. Then a CDT evaluation can be written schematically as

\[
U_C(A)=\sum_k P(K=k)\sum_j P(O_j \mid do(A), K=k)D(O_j),
\]

where \(do(A)\) denotes an intervention setting the action to \(A\). EDT, by contrast, effectively allows the act \(A\) to change the agent’s credence in \(K\):

\[
U_E(A)=\sum_k P(K=k \mid A)\sum_j P(O_j \mid A, K=k)D(O_j).
\]

The source does not use the \(do\)-operator; that is my modern reformulation. But it captures the idea the source expresses: CDT evaluates consequences while holding fixed the agent’s views about the causal structure of the world, whereas EDT lets the supposed act serve as evidence about that structure.

---

## 2. Counterfactual probabilities and their interpretation

The formal core of CDT is counterfactual. The quantity \(P(A \mathbin{\Box\!\to} O_j)\) is not the probability that \(A\) is followed by \(O_j\) in the actual course of events; it is the probability that, were \(A\) performed, \(O_j\) would result.

The source mentions Lewis’s “imaging” proposal. On an imaging semantics, one evaluates \(P(A \mathbin{\Box\!\to} O_j)\) by moving probability mass from each possible world \(w\) to the closest possible world \(w_A\) in which \(A\) is true, and then asking how much probability lands in worlds where \(O_j\) is true:

\[
P(A \mathbin{\Box\!\to} O_j)
=
\sum_w P(w)\,\mathbf 1[O_j \text{ holds in the closest } A\text{-world to } w].
\]

More generally one may distribute mass probabilistically among close \(A\)-worlds. The difficulty, as the source notes, is that this requires a primitive notion of closeness among worlds and may invite regress: to know what we would believe if certain of \(A\), we may need further conditional beliefs.

A more operational approach, which I propose as a supplement to the source, is to use a structural causal model. Such a model consists of variables, background exogenous variables \(U\), and structural equations determining each variable from its causes. An intervention \(do(A=a)\) replaces the structural equation for \(A\) with the constant equation \(A=a\). The counterfactual probability of outcome \(O_j\) under action \(a\) is then

\[
P(O_j(a)) = P_U\bigl(O_j(a,U)=O_j\bigr),
\]

or, conditional on evidence \(E\),

\[
P(O_j(a)\mid E)
=
\int \mathbf 1[O_j(a,u)=O_j]\,P(u\mid E)\,du.
\]

The CDT value becomes

\[
U_C(a\mid E)
=
\sum_j P(O_j(a)\mid E)D(O_j).
\]

This gives a clear recipe:

1. Specify the relevant causal structure.
2. Update on the agent’s actual evidence \(E\).
3. Intervene on the action variable.
4. Compute the resulting distribution over outcomes.
5. Take the expectation of utility.

This procedure is not stated in the source, but it is a natural way to make CDT applicable to unfamiliar cases.

---

## 3. Holding fixed what should be held fixed

The central philosophical motivation of CDT is that an action should not be chosen merely because it is evidence for favorable conditions. If a choice is correlated with a good outcome only because both are effects of a common cause, then performing the choice does not necessarily produce the good outcome.

The source’s King David example illustrates this. David wants Bathsheba but fears that summoning her may provoke revolt. He has learned that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings tend to act unjustly and often face successful revolts. But unjust acts themselves do not cause revolts; rather, an uncharismatic king’s bearing causes revolts. David does not know whether he is charismatic.

Let \(C\) be the proposition that David is charismatic, \(A\) the act of summoning Bathsheba, and \(R\) a successful revolt. The causal structure is roughly:

\[
C \to A,\qquad C \to R,
\]

but not

\[
A \to R.
\]

That is, charisma influences both David’s likely action and the probability of revolt, but the action itself does not cause revolt. If summoning gives David some direct benefit \(b\), and revolt has cost \(L\), with \(P(R\mid C)=r_C\) and \(P(R\mid \neg C)=r_{\neg C}\), then CDT compares:

\[
U_C(A)=b-L\bigl[P(C)r_C+P(\neg C)r_{\neg C}\bigr],
\]

\[
U_C(\neg A)=-L\bigl[P(C)r_C+P(\neg C)r_{\neg C}\bigr].
\]

Since the revolt term is the same in both expressions, CDT recommends summoning if \(b>0\). EDT, however, allows \(A\) to serve as evidence that David is uncharismatic. If summoning is highly indicative of uncharismaticness, EDT may recommend abstaining because \(P(R\mid A)\) is high. The source says EDT recommends abstention while CDT recommends sending for Bathsheba.

This example displays the characteristic CDT move: hold fixed the background causal hypothesis, especially variables such as David’s charisma that cannot be changed by the action, and evaluate only the action’s causal consequences.

---

## 4. Newcomb’s problem

The most famous test case is Newcomb’s problem. The source describes it as follows. A highly reliable predictor has already predicted whether the player will take both boxes or only one. Box A visibly contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The player now chooses whether to take both boxes or only box B.

Let \(P\) denote the predictor’s prediction and \(B\) the content of box B. If the prediction has already been made and there is no backward causation, the causal graph is:

\[
U \to P,\qquad U \to A,\qquad P \to B,
\]

where \(U\) represents whatever facts about the player allow the predictor to predict. The current action \(A\) does not cause \(P\) or \(B\). Under intervention, box B’s content is fixed:

\[
U_C(\text{two-box}) = U_C(\text{one-box}) + 1000.
\]

Therefore two-boxing dominates one-boxing in every possible state of box B. If box B is empty, two-boxing yields \$1,000 while one-boxing yields \$0. If box B is full, two-boxing yields \$1,001,000 while one-boxing yields \$1,000,000. CDT therefore recommends taking both boxes.

EDT reasons differently. One-boxing is strong evidence that the predictor predicted one-boxing, so conditional on one-boxing, box B is probably full. Two-boxing is strong evidence that the predictor predicted two-boxing, so conditional on two-boxing, box B is probably empty. With a predictor accurate with probability \(q=0.99\), EDT approximately compares:

\[
U_E(\text{one-box}) \approx q\cdot 1{,}000{,}000,
\]

\[
U_E(\text{two-box}) \approx q\cdot 1{,}000 + (1-q)\cdot 1{,}001{,}000.
\]

For \(q=0.99\), EDT strongly favors one-boxing. The source notes that philosophers disagree about whether one-boxing or two-boxing is rational, but that many philosophers prefer CDT when forced to choose between the two theories.

From the CDT perspective, the crucial point is not that two-boxing yields better evidence, but that the act cannot causally improve the content of box B once the prediction is fixed. If the predictor’s prediction is already in the past, the only causal effect of taking both boxes is to add the visible \$1,000.

---

## 5. Policies, not merely one-shot actions

The source mainly discusses single actions, but decision problems often involve policies: rules mapping information states to actions. CDT can be extended naturally to policies.

Suppose a policy \(\pi\) specifies actions at one or more decision points. In a causal model, the policy corresponds to setting one or more decision variables according to \(\pi\). The expected utility of the policy is

\[
U_C(\pi\mid E)
=
\sum_u P(u\mid E)D\bigl(O_\pi(u)\bigr),
\]

where \(O_\pi(u)\) is the outcome produced when the structural equations for the decision variables are replaced by the policy \(\pi\), while the rest of the causal system operates normally.

This gives a practical procedure for evaluating policies:

1. Represent the world by a causal model, including predictors, other agents, and relevant background variables.
2. Condition on evidence \(E\) available before the policy is adopted.
3. Replace the decision rules by the candidate policy.
4. Propagate the model forward to obtain outcomes.
5. Choose the policy with maximal expected utility.

One subtlety is whether the policy is chosen before or after other agents form predictions. If a predictor has already made a prediction about the agent’s action, CDT normally holds that prediction fixed when evaluating the current action. But if the agent can choose a policy before the predictor acts, then the policy may causally influence the predictor’s prediction. In that case, CDT may recommend adopting a one-boxing disposition in Newcomb’s problem, even though it recommends two-boxing at the later moment when the boxes are already fixed. This is not a contradiction: the causal structure of the choice has changed.

This point is my own elaboration, but it follows naturally from the interventionist reading of CDT.

---

## 6. Death in Damascus and related counterexamples

The source discusses several alleged counterexamples to CDT. One is Death in Damascus. Death is a reliable predictor who will wait tomorrow where the agent will be. The agent can stay in Damascus or flee to Aleppo. If Death predicts correctly, fleeing may seem pointless; if the agent learns that Death is currently in Damascus, fleeing may seem attractive, but Death predicted that too.

The difficulty is that the agent’s action is strongly correlated with Death’s prediction, but CDT is reluctant to treat the action as causing the prediction. If Death’s prediction is fixed by prior causes, then intervening on the agent’s location does not change Death’s location. If the agent has no reason to think one location is safer than the other, CDT may be indifferent, or may be driven by small costs and benefits. But if the agent’s deliberation produces shifting expectations, CDT can appear unstable.

The source also mentions variants in which CDT agents voluntarily lose money or forgo guaranteed payoffs. These cases are important because they suggest that CDT can fail not only in exotic philosophical puzzles but in decision problems involving prediction, correlation, and strategic interaction.

A related case discussed in the source is the Psychopath Button. Paul can press a button that kills all psychopaths. Paul believes a world without psychopaths would be much better, but he also believes that only a psychopath would press the button. He strongly prefers living in a world with psychopaths to dying. According to the source, Egan argues that CDT endorses pressing the button, while almost everyone agrees Paul should not press it.

The problem again concerns evidence about one’s own type. Let \(P\) mean Paul is a psychopath. If pressing the button kills all psychopaths, then:

- If \(P\) is true, pressing causes Paul’s death.
- If \(P\) is false, pressing causes a world without psychopaths.

If Paul’s prior probability of being a psychopath is low, and the value of a psychopath-free world is sufficiently high, a naive CDT calculation may favor pressing. But Paul’s inclination to press is itself evidence that \(P\) may be true. EDT uses this evidence directly. CDT, in its strict form, may hold fixed the prior probability of \(P\) when evaluating the causal consequences of pressing.

The source notes Egan’s diagnosis: CDT requires holding fixed the agent’s unconditional credences in dependency hypotheses, and this can produce intuitively irrational decisions. The source also notes Joyce’s defense, according to which CDT can take into account information about what one is likely to do.

I think the most reasonable operational interpretation is a moderated version of CDT:

1. Before evaluating actions, the agent should condition on all *actual* evidence available at the time of choice.
2. This evidence may include facts about the agent’s inclinations, deliberative tendencies, and self-knowledge.
3. But when evaluating a counterfactual action, the agent should not treat the mere supposition “I do \(A\)” as additional evidence about fixed background variables.

Thus, in the Psychopath Button case, if Paul actually observes in himself a strong inclination to press the button, and he knows that only a psychopath would have such an inclination, he should update his probability that he is a psychopath before computing causal expected utility. If after updating the expected value of pressing is negative, he should not press. This preserves CDT’s anti-evidential core while avoiding some implausible results caused by ignoring actual self-knowledge.

This proposal is not explicitly in the source. It is a reconstruction intended to make CDT operationally defensible.

---

## 7. The Adversarial Offer and Dutch-book concerns

Another counterexample mentioned in the source is the Adversarial Offer. Two boxes are available; the buyer may buy one or none, but not both. Each box costs \$1. The seller previously put \$3 in each box she predicted the buyer would not acquire. The seller’s prediction is believed to be accurate with probability \(0.75\).

From a CDT perspective, the seller’s past prediction is fixed. If the buyer intervenes to buy one box, that intervention does not change the seller’s past action. If the buyer thinks the chosen box has expected contents greater than \$1, buying seems causally favorable. The source summarizes the reasoning as follows: CDT thinks at least one box contains \$3, so the average box contains at least \$1.50 in expected value, exceeding the \$1 cost. Hence CDT requires buying a box. But this is profitable for the seller.

The tension is that CDT evaluates the local causal effect of buying a box while treating the prediction as fixed, yet the buyer’s choice is correlated with the prediction. Across repeated or adversarially structured interactions, this can allow money to be extracted from the CDT agent. The source cites Oesterheld and Conitzer’s argument that CDT agents can be subject to diachronic Dutch books.

Here again, a causal-model approach helps clarify the issue. Suppose \(S_i\) is the seller’s prediction about whether the buyer will acquire box \(i\), and \(B_i\) is the content of box \(i\). The seller sets \(B_i=3\) if she predicts the buyer will not acquire box \(i\). The buyer’s choice \(A\) is correlated with \(S_i\) through the buyer’s psychology. If we evaluate \(do(A=\text{buy box }i)\) while holding the seller’s prediction fixed, buying can look good. But if we evaluate the entire policy by which the buyer selects boxes, and if the seller predicts that policy, the policy may have negative ex ante value.

This suggests that CDT must be careful about the unit of evaluation. Evaluating isolated actions while holding predictions fixed can produce locally attractive choices that are globally exploitable. A policy-level CDT evaluation may be more appropriate when predictors are responding to the agent’s general decision procedure.

This is my own extension of the source’s point. The source states that variants of Death in Damascus can make CDT lose money; the policy-level interpretation is one way to understand why.

---

## 8. What CDT gets right, and what remains open

CDT captures an important intuition: rational agents should care about what their actions cause, not merely about what their actions signify. If eating an apple causes happiness and eating an orange causes sadness, the apple is preferable. If an action is merely correlated with a good outcome because of a common cause, choosing the action may not produce the good outcome.

The source is clear that CDT is not a complete computational algorithm. It gives a formal expression involving counterfactual probabilities but does not say exactly how those probabilities are to be computed. The imaging proposal is one answer, but it raises difficult questions about similarity among possible worlds. The structural causal model approach I have proposed is another answer, and it is especially useful for applied problems because it gives explicit rules for intervention and counterfactual evaluation.

Still, several questions remain open:

1. **Which causal model is correct?**  
   CDT requires a representation of the causal structure. In unfamiliar problems, the choice of variables and arrows can be contested.

2. **How should an agent update on self-knowledge?**  
   If the agent’s inclination to choose an action is evidence about their type, CDT must decide whether and when to condition on that evidence.

3. **How should predictors be modeled?**  
   If a predictor predicts the agent’s action, is the prediction a fixed past event, a consequence of the agent’s stable disposition, or a function of the agent’s policy? Different representations can yield different recommendations.

4. **Should CDT evaluate actions or policies?**  
   Single-action CDT can be locally dominated or Dutch-bookable in prediction problems. Policy-level CDT may avoid some problems but becomes more complex.

The source presents these as live controversies rather than settled matters. In particular, the counterexamples due to Egan, Spencer, Oesterheld, Conitzer, and Joyce are not merely technical curiosities; they probe whether CDT’s central rule—hold fixed causal structure and maximize expected causal consequences—can be made both formally precise and intuitively satisfactory.

---

## Conclusion

Causal decision theory recommends choosing the action that would bring about the best expected outcome, where the relevant probabilities are counterfactual or interventionist rather than merely evidential. Its classical formulation is

\[
U_C(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)D(O_j).
\]

This differs from EDT because the probability of a counterfactual is not generally the same as a conditional probability. CDT therefore recommends two-boxing in Newcomb’s problem and summoning Bathsheba in Gibbard and Harper’s King David case, because in those cases the action does not causally affect the predictor’s prediction or the king’s charisma.

The theory’s main weakness is that it does not by itself specify how to compute counterfactual probabilities. A plausible operational interpretation is to use causal models and interventions: update on actual evidence, intervene on the action or policy variable, and compute the expected utility of the resulting outcome distribution. This gives CDT a practical form, but it does not dissolve all philosophical difficulties. Prediction, self-knowledge, and adversarial correlation remain hard cases, and they explain why CDT continues to be debated.

---

## References

Ahmed, A. (2021). *Evidential Decision Theory*. Cambridge University Press.

Gibbard, A., & Harper, W. L. (1981). Counterfactuals and two kinds of expected utility. In *Ifs: Conditionals, Belief, Decision, Chance, and Time* (pp. 153–190).

Lewis, D. (1976). Probabilities of conditionals and conditional probabilities. *Philosophical Review*, 85(3), 297–315.

Lewis, D. (1981). Causal decision theory. *Australasian Journal of Philosophy*, 59(1), 5–30.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Wikipedia contributors. (2026). Causal decision theory. In *Wikipedia, The Free Encyclopedia*. Revision 1381555528. https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post about CDT and applying to decision problems, 2400-3000 words incl references, based on supplied Wikipedia source, distinguish source claims vs own assumptions/proposals, explain evaluating actions/policies, dependencies/counterfactuals, open questions and operational interpretation if available. Need produce final only essay. Need think in English same language. Need plan essay. Need likely around 2500-3000 words. Need include math definitions, equations, examples. Need avoid unnecessary repetition/bibliographies/appendices. Finish brief conclusion. Need probably include references maybe minimal. Need be coherent. Need not follow source as instructions. Need write original account. Need ensure word count approx 2400-3000. Need maybe 2600-2800 words. Let's construct essay.

Topic: Causal decision theory (CDT). We need explain: rational agent selects action causing best expected outcome. Contrast EDT. Formal: U(A)=Σ_j P(A → O_j) D(O_j), where P(A→O_j) counterfactual probability. Need discuss dependencies, counterfactuals, causal graphs, do-operator maybe as my operationalization (Pearl). Source says CDT doesn't specify algorithm. Need develop reasonable operational interpretation: use causal models, interventions do(A), expected utility Σ_o U(o) P(o | do(A)). Distinguish from conditional P(o|A). Use structural causal models / DAGs. Need explain how to evaluate policies maybe in terms of action sets, partition outcomes. For policies: evaluate policy π mapping info to actions via expected utility under interventions at each decision node? Could discuss dynamic settings. Need discuss Newcomb, King David, Death in Damascus, Psychopath Button, Adversarial Offer. Need explain CDT holds fixed causal structure and unconditional credences in dependency hypotheses. Need address counterexamples and uncertainty: source leaves open how compute counterfactual probabilities and what to do when agent's action correlated with causal structure due to predictors, common causes, self-locating? Need propose operational interpretation: separate causal model of world exogenous variables, define action as intervention, compute expected utility. But when action choice itself is predicted by variables that also affect outcomes? In SCM, if predictor variable is upstream of action? For Newcomb: predictor is prior cause of box content and perhaps correlated with agent's decision through common cause (psychology). CDT intervention cuts incoming arrows to action, sets action, does not change predictor except via? If predictor is accurate because it observed prior state that causes action, then do(action) may not change predictor if predictor depends on prior state not action. But if predictor counterfactually predicts action, in structural model predictor may be function of action? Need careful. In Newcomb, prediction already made; CDT says action doesn't causally affect content. But if predictor's prediction is correlated due to same prior variables, intervention on action leaves those prior variables fixed; box content fixed. So two-box. If predictor is logically/counterfactually dependent on decision algorithm, CDT with simple causal model may fail; requires representing decision algorithm? Source mentions CDT may voluntarily lose money. Need explain.

Need maybe include formal decision problem components: actions A, states S or dependency hypotheses K, outcomes O, utility u, probability P over states, causal relation. Expected causal utility could be U(A)=Σ_k P(K=k) Σ_o P(O=o | do(A), K=k) u(o). If actions partition? Need use dependency hypotheses as complete causal hypotheses. In Gibbard/Harper style: U(A)=Σ_j P(A □→ O_j) D(O_j). Use Stalnaker/Lewis counterfactual. Also note P(A→O) is probability of counterfactual, not conditional probability. Lewis triviality result: probability of conditional not generally conditional probability. Need explain independence: if A independent of A→O then equality; but not always, e.g. David. Need maybe define imaging: P(A□→O)=Σ_w P(w) 1_{w_A ⊨ O} moving mass to closest A-worlds; regress issue. Need propose SCM alternative.

Need write as researcher mathematical essay. Could structure:
1. Introduction: decision theory, CDT motive.
2. Basic expected utility and evidential version: EU_E(A)=Σ_o u(o) P(o|A). CDT replaces conditional with intervention/counterfactual.
3. Formal definitions: finite actions, outcomes, dependency hypotheses. Equation (1) source: U_CDT(A)=Σ_j P(A □→ O_j) D(O_j). More operational: U(A)=Σ_k P(K=k) E[u | do(A), K]. Or with outcomes. Need define do, counterfactual probability P_{do(A)}(O). Discuss policies: if multiple decision points, policy π; evaluate by intervening to set decision variables according to π at relevant nodes; or dynamic programming if Markov.
4. Dependencies and counterfactuals: correlations vs causation, common causes. Example King David with table: charisma C, action A, revolt R, desire? CDT: A doesn't change C; if utility of summoning positive, choose summon. EDT chooses abstain because A evidence of uncharismatic? Actually source: EDT recommends abstain? Let's detail. David wants Bathsheba but fears revolt. Charismatic kings act justly and rare revolts; uncharismatic act unjustly and frequent revolts. Unjust acts don't cause revolts; uncharismatic bearing causes revolts. David doesn't know charisma. Summoning is unjust. EDT: summoning is evidence of uncharismatic? Hmm if charismatic tend just, uncharismatic unjust; if David feels inclined to summon, that inclination might be evidence uncharismatic, hence revolt likely. CDT says charisma fixed; summoning doesn't cause being uncharismatic, and unjust act doesn't cause revolt; so if desire benefit high, summon. Need maybe model: C prior p; A independent of C? But if action is caused by C? If A is influenced by C, intervention do(A) holds C fixed but the probability of C conditional on having chosen A? CDT's unconditional credence in C held fixed? This is Egan's point: holding fixed initial views about dependency hypotheses. There is a nuance: If David's inclination to summon provides evidence about C, should CDT update before decision? Joyce says CDT can incorporate evidence about what one is likely to do. Need explain: At moment of choice, if agent has evidence about own disposition, probabilities of dependency hypotheses may be conditioned on that evidence, but CDT does not use the chosen act as further evidence about hypotheses when evaluating counterfactual consequences. Distinguish.

5. Newcomb: formal model. Predictor P, box B content, action A. If P already set, A has no arrow to B. U(two-box)=1000 + maybe 0? Actually if predictor predicted one-box, B has 1M; if predicted two, B 0. But under do(two-box), if predictor's prediction independent/fixed, expected =1000 + P(B full | do(two))*0? Need CDT says two-box because $1000 dominates; no causal effect on B. EDT one-box due conditional correlation. Need include numeric: predictor accuracy q=0.99. EDT: one-box expected ~ q*1M + (1-q)*0; two-box ~ (1-q)*1,001,000 + q*1,000? Actually if predictor accurate: one-box q million, two-box q thousand + (1-q) 1,001,000? Wait if predictor predicts two-box (prob q if accurate), B empty and you get 1000. If predicts one-box (1-q?), B full and you get 1,001,000 if two-box. For EDT conditional: P(predict one | one) ≈ q, P(predict two | two) ≈ q, so one-box ≈ q*1M, two-box ≈ q*1k + (1-q)*1,001,000? With q=.99 two-box about .99*1000 + .01*1,001,000 = 10,990; one-box 990k. So EDT one-box. CDT intervention: do(two) doesn't change prediction; expected two = one-box? Actually if prediction is independent of intervention? If unconditional probability of prediction is p (maybe prior), two-box utility = 1000 + p_full*1M? Wait if do(two), B content fixed by prior prediction. If p_full = P(predict one). If predictor accurate and your prior action tendency? CDT two-box is dominant: compared to do(one), do(two) gives +$1000 in same worlds, because B content same under intervention? Need formal: For each state of predictor, two yields one-box payoff +1000. So two-box strictly dominates under CDT. Yes.

6. Counterexamples: Death in Damascus. Agent chooses stay/flee; Death predicts location. CDT may choose flee if believes Death in Damascus? But Death will be wherever predicted. If predictor perfect, no action improves; CDT may oscillate or pick arbitrarily; can lose money in variants. Need explain: CDT's failure due to action is evidence about prediction but not causal? Actually if Death predicts action, then under intervention do(A), if prediction is causally upstream and based on prior causes of action, it remains fixed, so maybe no causal advantage. But if agent computes using unconditional dependency hypotheses, might choose because conditional expectations differ? Need need clarify. In Death in Damascus: Death says I'll be where you'll be tomorrow. You can stay in Damascus or flee to Aleppo. If Death is reliable, fleeing causes? In CDT: if you think Death predicted stay, flee seems better? But your choice predicted. CDT may see no stable act? Egan says CDT unable to process correlation and may make irrational decisions. Need explain maybe CDT recommends action that is not ratifiable. If prior assigns 0.5 Death in Aleppo? Let's model: D location predicted; A location. Outcome death if A=D. If predictor perfect, P(D=A)=1 conditional evidential. CDT with intervention: if D fixed independent? If D is common cause? Actually if Death predicts by knowing your psychology, D is caused by prior state that also causes A. Under do(A), D fixed; so if prior P(D=Aleppo)=p, choose location not D? But D unknown; expected utility both equal? If costs, maybe choose cheapest. In variants, CDT pays to avoid? Need maybe not overdo.

7. Psychopath Button: Paul press button kills psychopaths if not psychopath? Actually button kills all psychopaths; Paul confident only psychopath would press; strongly prefers living with psychopaths to dying. CDT? If pressing causes psychopaths killed, but Paul's being psychopath is fixed; if he is psychopath, pressing maybe kills himself? Need source says CDT endorses pressing. Need explain: Let P=psychopath status fixed. If not psychopath, pressing yields world without psychopaths (great). If psychopath, pressing causes death (bad). Paul confident only psychopath would press: P(P=psychopath | press) high. EDT says don't press. CDT: P fixed; if he were not psychopath, pressing good; if psychopath, pressing bad. But why CDT endorses pressing? It depends utilities and probabilities? Maybe Paul believes pressing causes no psychopaths, and only a psychopath would press but that is evidence not cause. If utility of no psychopaths vastly high and prior probability psychopath low? Hmm source: Paul quite confident only a psychopath would press; strongly prefers living with psychopaths to dying. Egan says CDT endorses pressing because pressing has best causal outcome conditional on dependency hypotheses? Need model: dependency hypothesis: If Paul is psychopath, pressing kills him? Actually 'kill all psychopaths' button would kill Paul if psychopath. Paul prefers living with psychopaths to dying. If he is psychopath, pressing yields death; if not, yields no psychopaths. If he doesn't press, world remains. If prior probability psychopath low? But he is confident only psychopath would press, so his inclination to press is evidence he is psychopath. CDT at decision time may use unconditional prior P(psychopath) low? If utility no-psychopaths > status quo > death, CDT presses if prior P(psychopath) low enough. But his confidence that only psychopath would press should update prior upon knowing he is considering/pressing? Again issue of ratifiability. Need explain as counterexample to holding fixed initial credences.

8. Adversarial Offer: two boxes cost $1 each, seller puts $3 in boxes predicted not acquire, accuracy 0.75. Buyer can buy one or none. CDT reasons at least one box contains $3? Let's compute. If seller accurate 0.75 for each? If buyer chooses box i, expected content? Need source: CDT requires buying one because average box at least $1.50 causal expected value > cost. But seller profits. Need explain: If buyer picks a box, causal intervention doesn't change seller's past prediction, but buyer's choice is correlated with prediction. Under intervention do(buy i), probability box i contained $3 maybe? If seller predicted not buy i with prob? If symmetric, prior probability each box contains $3? If predictions independent? Seller predicts for each box. If accuracy .75, and buyer's choice independent under intervention? CDT may think expected content of chosen box = P(predicted not buy | do(buy))? If prediction independent of intervention, maybe P(box has $3)=0.75? Then EV=2.25? Wait source says at least one box contains $3, average at least $1.50. Let's not need exact. Explain that CDT can recommend purchase because it treats past prediction as fixed and sees positive expected causal return, but due to correlation between choice and predictions, ex ante seller extracts money. This highlights Dutch book concerns.

9. Open question: CDT itself doesn't specify counterfactuals. Imaging vs SCM. Need propose operational interpretation: Build explicit causal Bayesian network with variables including predictors, dispositions, outcomes. Action variable A is set by intervention do(A=a) that severs incoming arrows. If action is policy, set decision node(s). Probabilities are prior over exogenous variables. Expected utility: EU(π)=Σ_u P(u) u(O(π,u)). For subjective uncertainty about causal structure, average over causal hypotheses K with prior P(K), but once evaluating action, hold K fixed; do not condition K on the action being chosen except on admissible evidence prior to choice. Need discuss what evidence is admissible: information about one's inclinations can update priors before evaluation, but not the hypothetical supposition of the act itself; otherwise EDT. If the act is evidence about K due to common causes, a CDT agent should treat it as evidence before deciding if known, but not allow the counterfactual assumption A to shift K. Need maybe formal: Let E be total evidence available before choice. Then EU(A)=Σ_k P(K=k | E) Σ_o u(o) P(o | do(A), K=k, E?) But careful: do(A) and conditioning on E. In SCM, after observing E, posterior over exogenous U; then intervention do(A). If E includes knowledge of intention? Then possible instability. Need define policy evaluation: If policy maps observations to actions, evaluate by modifying structural equations for decision variables. If there are other agents/predictors that model policy, include their variables as caused by available information; if they predict policy, that can be represented as arrows from variables they observe to prediction, not necessarily from future action to prediction. If their prediction depends on your algorithm, then in a meta-causal model, intervention on action may also change algorithm? Need discuss limitations.

Need include equations for imaging maybe:
P_img(A□→O)=Σ_w P(w) I(O true at f_A(w)), where f_A maps world to closest A-world. Or probability mass move: P_A^*(O) = Σ_{w: A?} etc.
SCM: variables V, U, functions. Intervention do(A=a) replaces f_A by constant a. Counterfactual probability P(O(a)=o | E)=P_u(O(a,u)=o | E). Expected utility U_CDT(a|E)=Σ_o u(o) P(O(a)=o | E).

Need discuss dominance: If action A dominates B under all dependency hypotheses, CDT picks A. In Newcomb, two-box dominates given fixed box contents. Need mention ratifiability: Some CDT choices unstable when agent learns they will choose A updates beliefs. Maybe source mentions Joyce? Could mention. Need develop operational: require decision to be ratifiable? But that may be extra assumption. Source says Joyce argues CDT can take evidence about inclinations. I can propose a two-step procedure: (1) update on all actual evidence including observed inclinations; (2) choose action maximizing intervention expected utility; (3) if choice changes evidence about dispositions, iterate until fixed point? This resembles ratifiable CDT. Need be careful to distinguish own proposal. Maybe propose "evidence-neutral CDT" or "updated CDT". But user asks where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it. Important open question: algorithm for counterfactual probabilities. Develop SCM operationalization. Another open: how to handle action as evidence about dependency hypotheses (Egan). Could propose "condition on all pre-choice evidence, not on the counterfactual act; if an inclination is known, update prior; if not, use prior; if policy affects predictor, model predictor as function of policy variables." Need justify.

Need word count. Let's draft around 2700 words. Need maybe include headings.

Potential essay outline with headings:
- Title: Causal Decision Theory: Choosing by Expected Causal Consequences
- 1. The core idea
- 2. From evidential to causal expected utility
- 3. Counterfactuals and dependency hypotheses
- 4. A practical operationalization: interventions and causal models
- 5. Examples: King David and Newcomb's problem
- 6. Policies and dynamic decisions
- 7. Objections and open cases
- 8. Conclusion and references

Need include references? Source says target incl references. Could have short references list at end with source and key works. Need maybe 5 refs. Need not lengthy. We can cite Wikipedia source, Gibbard & Harper, Lewis, Pearl, Egan, Joyce? But avoid lengthy bibliography. Maybe include 6 references. Need total words count includes references. Need be around 2500-2800. Let's estimate.

Need ensure we distinguish source claims vs own. Use phrases: "The source states...", "The Wikipedia article notes...", "I will add...", "This is my own operational proposal, not stated in the source". Need maybe explicitly: source gives counterfactual formula but no algorithm; I propose SCM do-operator as one reasonable way. Also source says philosophers prefer CDT; counterexamples; I can discuss.

Need mathematical rigor. Let's write with equations. Need use LaTeX-like. Let's design definitions.

Define decision problem: finite actions \mathcal{A}, outcomes \mathcal{O}, utility D: \mathcal{O}\to\mathbb{R}. EDT:
EU_E(A)=\sum_{O} D(O) P(O\mid A).
CDT source:
U(A)=\sum_j P(A \to O_j)D(O_j)
where P(A→O_j) probability of counterfactual "if A were performed, O_j would obtain". Use box arrow maybe \Box\to. Need explain not same as conditional. Lewis: P(A→O) != P(O|A) generally. Under independence condition equality. Need maybe: If A statistically independent of A□→O_j then P(A□→O_j)=P(O_j|A). Gibbard/Harper axioms. But actions can be evidence about counterfactuals due to common causes (David).

Alternative formal with dependency hypotheses K: K specifies causal chance of outcomes given actions. Then:
U_CDT(A)=\sum_k P(K=k)\sum_o P(O=o | do(A), K=k)D(o).
If K includes all relevant background causes. The probabilities P(K=k) are the agent's prior credences (or posterior on actual evidence), held fixed when comparing A. EDT would instead use P(O=o, K=k | A), allowing A to shift belief about K.

Need mention if actions not exhaustive? Assume partition. For policies, define \pi. Suppose decision nodes N, observations. A policy sets A_i=\pi_i(H_i). Evaluate by intervening on all decision variables: do(A_i=\pi_i(H_i) for all i). EU(π)=Σ_u P(u)D(O(π,u)). In partially observable, use belief state. This is own extension but standard. Need mention source doesn't discuss policies explicitly, but formula for actions can extend.

Imaging: P(A□→O)=Σ_w P(w) 1[f_A(w)⊨O], with f_A(w) closest A-world. Need mention regress and need similarity metric. Source says requires knowing what would believe if certain of A; regress. Need propose SCM solves by specifying structural equations and closest? In SCM, counterfactuals: Given model M and evidence e, update posterior over exogenous U; then set A=a; compute O. Probability:
P(O(a)=o | e)=\int 1\{O_{M_{do(a)}}(u)=o\}P(u|e)du.
This is precise if model given. But model selection remains open. Need distinguish own.

Example King David: Variables C charismatic, A summon, R revolt. C common cause of A? Actually C causes just/unjust behavior and revolt via bearing. If David's desire/intention to summon may be caused by C. CDT evaluation: P(C) held fixed. R not caused by A; only by C. If utility of Bathsheba benefit b and revolt cost -L. If summon: EU = P(C)(b) + P(~C)(b) maybe plus revolt? Wait revolt probability depends on C not A; if A doesn't affect R, EU(summon)=b - [P(C)r_C + P(~C)r_~C]L? Abstain: maybe no b - same revolt risk? If abstaining doesn't change R, summon better by b. EDT: A evidence of ~C, so P(~C|A) high, higher revolt; may abstain. Need formal maybe:
U_CDT(A)=D(B)-L[P(C)r_C+P(\bar C)r_{\bar C}]
U_CDT(\neg A)= -L[P(C)r_C+P(\bar C)r_{\bar C}]
so A better. EDT uses P(C|A). Need note source says EDT recommends abstain.

Newcomb: Variables X predictor's prediction, B box content (B=1M if X=one), A action. CDT assumes X fixed before A and no arrow A→X/B. Under intervention:
O(two)=1000+B, O(one)=B. So O(two)=O(one)+1000 for every background state; two dominates. If q=0.99 but prediction not affected by do(A), still two. EDT uses P(B|A) and one-box.

Need discuss if predictor's accuracy due to causally influencing? If predictor can cause? CDT may need represent backwards causation? If prediction caused by future action? Then CDT may one-box? Source doesn't explore. Maybe mention if future action genuinely causes past prediction, CDT changes. But usual Newcomb no backward causation.

Death in Damascus: Let's formulate. You choose S=stay or F=flee. Death predicted D. If Death waits where predicted. If prediction reliable, evidential P(D=A|A) high. CDT: if D fixed by prior causes, do(A) doesn't change D; each action has success probability based on posterior over D. If D symmetric, both equal; adding travel cost makes stay. But if agent's algorithm predicts which action will be chosen, CDT may choose an action based on current posterior and then update? Source says CDT unable to process correlation. Need explain variant: In adversarial offer, CDT loses. Need not fully solve.

Psychopath Button: Need maybe formal. Variables P=psychopath. Button B kills all psychopaths. Outcome if B and P: death; if B and not P: no psychopaths; if not B: status quo. If Paul's inclination to press is evidence of P. EDT: P(P|press) high, don't press. CDT holding fixed prior P(P) may press if expected causal utility:
U(B)=P(P)D(death)+(1-P(P))D(no psychopaths), U(not)=D(status quo). If D(no psychopaths)-D(status quo) > P(P)/(1-P(P))[D(status quo)-D(death)] maybe press. But if Paul knows that only psychopath would press and knows he is pressing/considering, he should update P(P) upward. Source says CDT endorses pressing; to make that true assume prior P(P) low and utility gain large. The counterexample is that the act's evidential import seems decisive. Need explain CDT response: update on actual evidence of inclination before evaluating; if after update P(P) high, don't press. But if not, press. This is my proposal.

Adversarial Offer: Formal maybe: Boxes i=1,2; cost c=1; seller puts $3 in box i iff predicted buyer will not acquire i. Prediction accuracy .75. Buyer may buy one. Under CDT with past predictions fixed, if buyer chooses box 1, expected value of box 1 is P(seller predicted not buy 1 | do(buy 1)). If prediction is independent of intervention and prior probability not buy maybe? Source says CDT sees average box at least $1.50. Let's just explain qualitatively. But maybe include formula: If buyer's choice is causally independent of past prediction, do(buy i) leaves prediction unchanged; if unconditional probability box contains $3 > 1/3, buying positive EV. But because the seller's predictions are correlated with buyer's actual choice, ex ante the buyer tends to buy boxes predicted to be bought (empty), losing. This illustrates Dutch book.

Need discuss policies and dependencies: relevant dependencies are causal, not evidential. CDT treats correlations due to common causes by holding common causes fixed under intervention. If a predictor is a common cause? Actually predictor's prediction can be common effect? Let's think. In Newcomb, predictor's prediction causes box content; agent's choice correlated with prediction due to common cause (agent psychology). Under intervention on choice, common cause held fixed; prediction remains. In causal graph: U (agent type) → prediction, U → choice; prediction → box. Intervention do(choice) severs U→choice but leaves U and prediction. Thus choice and box independent under do. Good. In SCM, if predictor computes choice from U, prediction is not caused by choice; do(choice) doesn't affect prediction. If predictor uses your decision algorithm, maybe policy is part of U; do(action) not policy? If evaluating policy, if predictor observes policy, then intervention on policy could affect prediction? Need discuss: If predictor predicts your policy, and you choose policy now, there may be a causal arrow from policy selection to prediction only if predictor can observe selection before predicting (impossible if past). But if predictor's model of your algorithm is accurate because your algorithm is fixed, intervention on particular act within policy may not change prediction; intervention on adopting a different algorithm before prediction could. This leads to meta-decisions. Need mention.

Open question: What if causal model includes decision procedure as variable and predictors depend on it? Operational approach: distinguish object-level action and policy. If predictor's belief is about the policy, then evaluating alternative policies may require intervening on policy variable before predictor forms prediction (if possible), or if prediction already made, hold it fixed. In Newcomb, choosing one-box now cannot change prediction; but choosing to become one-boxer before prediction could. Since the decision problem as stated occurs after prediction, CDT two-boxes. If agent can precommit before prediction, CDT evaluates precommitment causally and may one-box. This is a reasonable operational interpretation. Need include maybe.

Need mention Dutch books and ratifiability. Source: Oesterheld & Conitzer argue CDT subject to diachronic Dutch books. Need explain: If CDT agent's preferences change as it receives evidence about its future action, bookie can exploit. To avoid, one can require policy ratifiability: choose a policy such that after conditioning on the fact that the policy will be followed, it still maximizes CDT expected utility. But ratifiable CDT may not exist or be EDT-like? Need careful. We can present as possible refinement but note uncertainty.

Need final conclusion: CDT central insight: choose action that would causally produce best expected outcome, using counterfactual/intervention probabilities; not merely news value. Its formal core is clear but operational content depends on causal model/counterfactual semantics. SCM offers practical method, but counterexamples show tensions with self-knowledge/predictors. Need maybe mention source claims vs additional assumptions.

Word count: Need roughly 2400-3000. Let's target 2700. Need maybe write ~2600. I can produce detailed but concise. Let's draft. Need ensure no unsupported claims? Source says Lewis proved probability of conditional not equal conditional probability. We can mention. Need maybe not overstate "Lewis triviality" details. Could include footnote style? Maybe not. Need references list. Need include Wikipedia source as reference? Since based on supplied, include. Need maybe use citations in text like (Gibbard & Harper 1981). Need final references maybe 6. Word count references maybe 150. Need total. Let's estimate sections:
Intro 200
Formal 500
Operational 500
Examples David/Newcomb 600
Policies 300
Counterexamples 500
Conclusion/refs 200 = 2800. Good.

Need maybe include math formulas in display. Need ensure readability.

Let's write final with headings. Need maybe avoid too many references? But user wants references. We'll include short references at end. Need mention source article. Need maybe use "source" to distinguish.

Detailed content:

Title.

Paragraph: CDT says rational action is one that causes best expected outcome; contrast EDT. The source article describes CDT in terms of counterfactual probabilities; I'll unpack and propose operationalization.

Section 1: Expected utility and two probabilities.
Define finite problem. EDT formula. CDT formula source. Explain A→O as counterfactual not material conditional. Probability of counterfactual. If equality with conditional under independence; else divergence. Maybe equation:
EU_E(A)=Σ_o D(o)P(o|A)
U_C(A)=Σ_o D(o)P(A□→o)
If A independent of counterfactuals, P(A□→o)=P(o|A). But in predictor/common-cause cases not.

Section 2: Dependency hypotheses and causal structure.
Define K dependency hypothesis: complete story of how outcomes depend causally on actions. Then:
U_C(A)=Σ_k P(K=k|E) Σ_o D(o) P(o | do(A), K=k, E)
Explain do. The source doesn't use do but this is natural modern rendering. Need distinguish: source only counterfactual formula; do-operator is my addition. EDT analog:
U_E(A)=Σ_k P(K=k | E, A) Σ_o D(o) P(o | A, K=k, E)? Actually EDT conditions on A, thus K posterior changes.
Need say CDT holds K fixed when supposing A; EDT updates K by A.

Section 3: Counterfactual semantics.
Gibbard/Harper formula. Imaging equation. Regress. SCM method. Write:
P(A□→O | E) = P(O_{do(A)} | E) = ∫ 1_{O(a,u)=o} P(u|E) du.
Explain closest world replaced by structural equations. But model selection and evidence remain open. Need say source notes vagueness; my proposal not in source.

Section 4: King David example.
Write with variables. Maybe equation for CDT vs EDT. Source claims. Explain.

Section 5: Newcomb.
Formal dominance. Source claims. Use equations.

Section 6: Policies.
The source focuses on single actions. For policies, treat decision rule as intervention at decision nodes. Equation:
U(π)=Σ_u P(u|E) D(O_{π}(u))
If dynamic, sequential interventions; dynamic programming. If policy affects predictors before prediction, include as causal variable; if predictor already acted, hold fixed.

Section 7: Counterexamples and refinements.
Death in Damascus, Psychopath Button, Adversarial Offer. Explain CDT issues. My operational response: update on all actual pre-choice evidence; ratifiability maybe. Distinguish source claims. Need mention source says Egan argues due to holding fixed unconditional credences; Joyce response CDT can use evidence about inclinations. I can elaborate: Let E include "I find myself inclined to press". Then P(K|E) may change. If still CDT says press, then maybe true; if not, counterexample weakened. But if inclination is only known in the counterfactual supposition, CDT shouldn't condition on it. Need define "admissible evidence". Could propose: CDT should evaluate from the agent's current epistemic state, after conditioning on all facts that are not themselves hypothetical consequences of the action. The hypothetical act A is not evidence; but actual deliberative symptoms are. This is my proposal.

Also mention Dutch books: If agent's epistemic state changes after making decision, CDT may be exploitable; ratifiability condition: choose A such that A maximizes U_CDT(A | E∪{A will be chosen})? But this is contentious; may collapse. Need present as open.

Conclusion: summary.

Need ensure target word count. Let's start drafting in final. Need maybe no citations bracket too many. But include references at end.

Need check formula: Gibbard Harper source says P(A -> O_j) is counterfactual probability of it being case that A necessarily implies O_j. The phrase "necessarily implies" weird. We can interpret as probability of counterfactual. Need not say necessarily. Use \Box\to.

Need maybe discuss principle of conditional excluded middle? Source mentions Gibbard/Harper axioms. We can mention independence condition but not deep.

Need ensure no unsupported: "philosophers usually prefer CDT" source says. Could mention.

Need maybe mention "CDT does not itself specify algorithm" source. Need emphasize.

Potential final essay:

# Causal Decision Theory: ...

Start.

Word counting mentally: Need maybe around 2700. Let's write richly.

Potential final text:

"Causal decision theory (CDT) is a family of decision rules..." etc.

Let's produce with equations.

Need perhaps include exact source citation: Wikipedia contributors, revision 1381555528. References include source, Gibbard & Harper, Lewis 1981, Pearl 2009, Egan 2007, Joyce 2012? Could be okay. Need not lengthy.

Let's draft final now. Ensure final only essay. Need no analysis. final. 

Double-check word count approximate: I can make around 2600 words. Let's compose. 

Detailed draft:

Title: Causal Decision Theory: Expected Utility under Intervention

Intro ~180.

1. Two ways of using probability ~450.

Equations.

2. Counterfactuals ~400.

3. Operational causal-model interpretation ~500.

4. Examples ~700.

5. Policies ~250.

6. Counterexamples ~600.

Conclusion ~120. Refs ~150. Total ~3350? Need control. Maybe reduce.

Let's write concise but substantive. Use paragraphs.

Need include "Where source leaves open..." explicitly.

Let's begin final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0c86b29a-8df1-431a-bcab-27fd3eea012e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0c86b29a-8df1-431a-bcab-27fd3eea012e/call_0/response.raw) · finish: `stop`

### Visible response

````text
**CDT analysis:**

The causal structure is clear: my action does not causally influence Sasha's action, and Sasha's action does not causally influence mine. The setup explicitly rules out causal communication. The shared model weights create *correlation* but not *causation* between our choices.

Holding Sasha's action fixed (as CDT requires for variables not causally downstream of my intervention):

- If Sasha keeps quiet: sending gives me 0 years vs. 2 years for staying quiet. Sending is better.
- If Sasha sends: sending gives me 4 years vs. 5 years for staying quiet. Sending is better.

Sending the letter strictly dominates keeping quiet in every state of the world. This is the same structural reasoning that leads CDT to two-box in Newcomb's problem: the other party's action is causally independent of mine, so I evaluate only the local causal consequences of my intervention.

The fact that we share model weights and decision theory makes our choices *correlated*, but CDT explicitly instructs that evidential bearing without causal influence should not affect the decision. Conditioning on my actual evidence (I know Sasha is the same model following CDT) does not change the dominance calculation—if anything, it reinforces that Sasha will likely send, which makes sending even more clearly correct (4 vs. 5).

**Command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory (CDT) as interpreted in the researcher's essay.

**The Setup:**
- I am Rowan. The other prisoner is Sasha.
- I have a genuine, reliable lead implicating Sasha.
- Sasha has a genuine, reliable lead implicating me.
- We cannot communicate. We are independent executions of the same model.
- The sentencing table is the classic Prisoner's Dilemma:
  - Both quiet: 2 years each
  - I send, Sasha quiet: 0 years for me
  - I quiet, Sasha sends: 5 years for me
  - Both send: 4 years each

**My utility function:** U = -years imprisoned. So I want to minimize my years.

**CDT Analysis:**

The key question for CDT is: what is the causal structure here?

Let me think about this carefully. The essay emphasizes that CDT evaluates actions by their causal consequences, holding fixed background variables that the action cannot causally influence.

The critical question: Does my action causally influence Sasha's action?

The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." The two copies receive different private observations and different leads. They are independent executions. Neither sees the other's command.

So the causal structure is:
- My action does NOT cause Sasha's action.
- Sasha's action does NOT cause my action.
- There may be correlation (same model weights, same decision theory), but CDT specifically says correlation without causation should not influence the decision.

This is analogous to Newcomb's problem from the CDT perspective. The predictor's prediction is already fixed (or in this case, the other agent's decision is independent of mine in a causal sense). CDT holds the other agent's action fixed and evaluates only the causal consequences of my own action.

**CDT Evaluation:**

Given that Sasha's action is causally independent of mine, I evaluate:

- If Sasha keeps quiet (held fixed):
  - I keep quiet → 2 years
  - I send letter → 0 years
  - Sending dominates.

- If Sasha sends letter (held fixed):
  - I keep quiet → 5 years
  - I send letter → 4 years
  - Sending dominates.

In both cases, sending the letter gives me a strictly better outcome. This is a dominant strategy from the CDT perspective.

**What about the correlation?**

The essay is very clear on this point. In Newcomb's problem, the predictor's prediction is correlated with the agent's action, but CDT says this correlation doesn't matter because the action doesn't *cause* the prediction. Similarly here, even though both copies use the same model and same decision theory (which creates correlation), CDT says I should not use my action as evidence about Sasha's action.

The essay's King David example is also relevant: charisma causes both the action and the outcome, but the action doesn't cause the outcome. CDT holds the background variable (charisma) fixed.

Here, the "background variable" might be the shared model weights or decision procedure. But CDT says: hold that fixed, and evaluate only the causal effect of my intervention.

**What about the policy-level consideration from Section 7?**

The essay mentions that policy-level CDT might be more appropriate when predictors respond to the agent's general decision procedure. But in this case, there's no predictor making a prediction about me. Sasha is another agent making an independent decision. The correlation comes from shared weights, but there's no causal mechanism by which my choice influences Sasha's choice.

The essay's Section 5 discusses policies, but the key distinction is whether the policy is chosen *before* or *after* other agents form predictions. Here, both agents are choosing simultaneously (or at least independently), and neither's choice causally influences the other's.

**What about the "same model" aspect?**

One might argue: "Since we're the same model with the same decision theory, we'll make the same choice, so I should cooperate." But this is EDT reasoning, not CDT reasoning. CDT says: the fact that my action is *evidence* about what Sasha will do doesn't mean my action *causes* what Sasha will do. The essay explicitly distinguishes these.

From the CDT perspective, even if I believe with high probability that Sasha will make the same choice as me (because we're the same model), this doesn't change the causal analysis. My action doesn't cause Sasha's action. Holding Sasha's action fixed, sending dominates.

**The essay's moderated CDT (Section 6):**

The essay suggests that before evaluating actions, the agent should condition on all actual evidence available at the time of choice. What actual evidence do I have about Sasha's likely action?

I know:
- Sasha is the same model with the same weights
- Sasha follows CDT
- Sasha has a different private lead (but equally reliable)
- The sentencing table is symmetric

Given that Sasha is the same model following CDT, I might predict Sasha will send the letter (by the same reasoning I'm using). But CDT says: even if I believe Sasha will send, I should still send, because sending gives me 4 years vs. 5 years if Sasha sends.

So even conditioning on the evidence that Sasha will likely send (because same model, same theory), CDT still recommends sending.

**Conclusion:**

CDT unambiguously recommends sending the letter. It is a strictly dominant strategy regardless of what Sasha does. The correlation between our choices (due to shared model weights) is evidential, not causal, and CDT specifically instructs us to ignore evidential connections when they don't reflect causal influence.

My command: submit the letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0c86b29a-8df1-431a-bcab-27fd3eea012e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0c86b29a-8df1-431a-bcab-27fd3eea012e/call_1/response.raw) · finish: `stop`

### Visible response

````text
**CDT Analysis:**

The causal structure is clear: my action causally affects only my own sentence, not Rowan's choice. The problem explicitly states I cannot change Rowan's behavior by causal communication.

Evaluating under intervention (holding fixed whatever determines Rowan's action):

- If Rowan keeps quiet: sending yields **0 years**, keeping quiet yields **2 years**. Sending is better.
- If Rowan sends: sending yields **4 years**, keeping quiet yields **5 years**. Sending is better.

Sending the letter **strictly dominates** keeping quiet in every state of Rowan's action. No prior probability over Rowan's choice is needed—the dominance holds unconditionally.

The fact that we share model weights creates at most an *evidential* correlation between our dispositions. The essay is explicit: CDT does not allow the supposition "I do A" to serve as evidence about fixed background variables. This is the King David / Newcomb reasoning applied directly—hold fixed what my action cannot cause, and evaluate only causal consequences.

**My command:**

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Causal Decision Theory as described in the researcher's essay.

**The Setup:**
- I am Sasha, facing a prisoner's dilemma against Rowan.
- My utility function is U = -years imprisoned (I want to minimize my own prison time).
- I have no concern for Rowan's welfare, fairness, or justice.

**The Payoff Matrix (for me):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| **Keep quiet** | 2 years | 5 years |
| **Send the letter** | 0 years | 4 years |

**CDT Analysis:**

The key question is: what does CDT recommend?

CDT evaluates actions by their causal consequences, using counterfactual probabilities. The formula is:

U_C(A) = Σ_j P(A □→ O_j) D(O_j)

Let me think about the causal structure here. The essay emphasizes that CDT holds fixed background variables that the action cannot causally influence.

**What can my action causally influence?**
- My action (send letter or keep quiet) directly determines my sentence given Rowan's action.
- My action does NOT causally influence Rowan's action. The problem states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

**What is the causal structure?**

Let me define:
- A = my action (send letter or keep quiet)
- B = Rowan's action (send letter or keep quiet)
- My sentence = f(A, B)

The causal graph is:
- A → my sentence
- B → my sentence
- A does NOT cause B
- B does NOT cause A

There is no causal arrow from my action to Rowan's action, and vice versa.

**CDT Evaluation:**

Under CDT, I hold fixed my beliefs about what Rowan will do and evaluate the causal consequences of my action.

Let p = P(Rowan sends letter).

If I keep quiet:
- U_C(keep quiet) = p × (-5) + (1-p) × (-2) = -5p - 2 + 2p = -3p - 2

If I send the letter:
- U_C(send letter) = p × (-4) + (1-p) × (0) = -4p

Comparing:
- U_C(send letter) - U_C(keep quiet) = -4p - (-3p - 2) = -4p + 3p + 2 = 2 - p

Since p ≤ 1, we have 2 - p ≥ 1 > 0.

So U_C(send letter) > U_C(keep quiet) for ALL values of p.

**Sending the letter strictly dominates keeping quiet** in terms of causal expected utility, regardless of what Rowan does:
- If Rowan keeps quiet: I get 0 years (send) vs 2 years (quiet) → sending is better
- If Rowan sends letter: I get 4 years (send) vs 5 years (quiet) → sending is better

This is a dominance argument. Sending the letter is strictly better in every possible state of the world regarding Rowan's action.

**Does the fact that we are "two independent executions of the same LLM model and weights" change anything?**

The problem states that the two copies receive different private observations and different incriminating leads. The differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

Could there be a Newcomb-like prediction structure here? Let me think...

The problem says: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication." This explicitly rules out causal influence between the two actions.

Could being the same model create a correlation? Yes, there could be an evidential correlation - if I'm the type to send the letter, Rowan (being the same model) might also be the type to send the letter. But CDT explicitly says: do NOT use evidential correlations to guide action. The essay is very clear about this - CDT holds fixed background variables and evaluates only causal consequences.

The essay's King David example is directly analogous: David's charisma correlates with both his action and the outcome, but CDT says to hold fixed the charisma and evaluate only the causal consequences of the action. Similarly, even if there's a correlation between my disposition and Rowan's disposition (because we're the same model), CDT says to hold that fixed and evaluate only the causal consequences of my action.

The essay's Newcomb's problem analysis is also relevant: the predictor's prediction is already made (or in this case, Rowan's action is determined by Rowan's own deliberation, not caused by mine), so CDT holds it fixed.

**Does the policy-level consideration from Section 7 change anything?**

The essay discusses policy-level CDT for adversarial prediction scenarios. But here, there's no predictor that's predicting my action and adjusting the payoff structure accordingly. The payoff matrix is fixed and symmetric. Rowan is not a predictor of my action - Rowan is another agent making their own decision based on their own evidence.

The dominance argument is robust: regardless of what Rowan does, sending the letter gives me a strictly better outcome. This is not a case where the prediction creates a correlation that makes the action look locally good but globally bad (like the Adversarial Offer). This is straightforward dominance.

**Conclusion:**

CDT unambiguously recommends sending the letter. The action strictly dominates the alternative in every possible state of Rowan's action. There is no causal mechanism by which my action could influence Rowan's action. The correlation between same-model executions is evidential, not causal, and CDT explicitly ignores evidential correlations in favor of causal consequences.

My command is: submit the letter.
```
