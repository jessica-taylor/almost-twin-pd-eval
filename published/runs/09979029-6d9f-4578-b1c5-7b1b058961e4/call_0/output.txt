# Causal Decision Theory: Choosing by Expected Causal Consequences

Causal decision theory (CDT) is a school of thought in decision theory holding that a rational agent should choose the action that has the best expected *causal* consequences. The contrast is with evidential decision theory (EDT), which chooses the action that would be the best “news”: the action whose occurrence would be most strongly associated with good outcomes. This essay explains the central formal idea of CDT, how it evaluates actions and policies, how it handles probabilistic dependencies and counterfactuals, and where the theory remains under-specified. It draws on the supplied reference article, but also adds an operational interpretation using modern causal-model notation; where I add assumptions beyond the source, I say so explicitly.

## 1. Two ways of computing expected utility

Let \(A\) range over available actions and let \(O_1,\dots,O_n\) be a partition of possible outcomes. Let \(D(O_j)\) be the desirability, or utility, of outcome \(O_j\). EDT evaluates an action \(a\) by conditional probabilities:

\[
U_{\text{EDT}}(a)=\sum_j P(O_j \mid A=a)\,D(O_j).
\]

The probability \(P(O_j \mid A=a)\) is ordinary Bayesian conditional probability: how likely \(O_j\) should be believed, given the news that action \(a\) was taken.

The supplied source gives the classic CDT formula, due to Gibbard and Harper (1981):

\[
U_{\text{CDT}}(A)=\sum_j P(A \mathbin{\Box\!\to} O_j)\,D(O_j),
\]

where \(P(A \mathbin{\Box\!\to} O_j)\) is the probability of the counterfactual: “if \(A\) were performed, \(O_j\) would obtain.” The source describes this as the counterfactual probability that \(A\) implies \(O_j\). In contemporary notation one often writes \(P(O_j \mid do(A))\), meaning the probability of \(O_j\) under an intervention setting the action to \(A\).

A simple example from the source illustrates the basic idea. If eating an apple causes happiness and eating an orange causes sadness, CDT recommends the apple. If the apple may be good or bad, and eating a good apple causes happiness while eating a bad apple causes sadness, the agent should use expected causal effects. If the agent’s credence that the apple is good is \(p\), and the causal effects are deterministic, then

\[
U_{\text{CDT}}(\text{eat apple})
= pD(\text{happy}) + (1-p)D(\text{sad}).
\]

The recommendation depends not merely on the evidence that eating the apple provides, but on the expected causal consequence of eating it.

The source notes an important formal point due to Lewis: the probability of a conditional, or counterfactual, \(P(A \mathbin{\Box\!\to} O_j)\), need not equal the conditional probability \(P(O_j \mid A)\). If they always coincided, CDT would collapse into EDT. Lewis’s triviality result shows that one cannot generally identify probabilities of conditionals with conditional probabilities without making probability assignments trivial. Gibbard and Harper also showed that, under certain axioms, statistical independence between \(A\) and the relevant counterfactuals can make the two calculations agree. The interesting cases are precisely those where action and relevant background conditions are not independent.

## 2. Causal dependence versus evidential dependence

CDT’s central distinction is between causal dependence and mere probabilistic dependence. An action may be evidence for an outcome without causing it. EDT responds to the evidential connection; CDT asks what would happen if the action were intervened upon.

A useful way to state this is to introduce dependency hypotheses \(K\). A dependency hypothesis specifies how outcomes depend causally on actions and background states. For example, \(K\) might encode whether a predictor is reliable, whether a king is charismatic, or whether a button-pressing person is a psychopath. Given a partition of dependency hypotheses, one can write an interventionist version of the CDT formula as

\[
U_{\text{CDT}}(a)
=
\sum_k P(K=k)
\sum_o P(o \mid do(a), K=k)\,D(o).
\]

This is my own operational reconstruction of the source’s counterfactual formula. The source speaks of counterfactual probabilities; I am expressing them using interventionist notation. The crucial feature is that CDT uses the agent’s prior or current non-action-based credence \(P(K=k)\), not the conditional credence \(P(K=k \mid A=a)\). EDT would use the latter whenever the action provides evidence about \(K\).

The King David example from the source illustrates this. David wants Bathsheba but fears that summoning her may provoke revolt. He knows that kings are either charismatic or uncharismatic. Charismatic kings tend to act justly and rarely face successful revolts; uncharismatic kings act unjustly and often face successful revolts. But unjust acts themselves do not cause revolts; the cause is the king’s ignoble bearing. David does not know whether he is charismatic.

Let \(C\) be charisma. The causal structure is roughly:

\[
C \rightarrow \text{justice of action}, \qquad
C \rightarrow \text{risk of revolt}.
\]

Summoning Bathsheba is an unjust act and therefore evidence that David is uncharismatic. EDT recommends abstaining, because abstaining is good news about David’s charisma and therefore about revolt risk. CDT says that David’s charisma is already fixed and is not causally affected by the choice. If summoning Bathsheba does not causally increase revolt risk, then CDT recommends summoning her, because the act itself brings about the desired benefit without changing the revolt probability. In intervention notation, if \(C\) is a common cause and summoning has no causal effect on revolt once \(C\) is fixed,

\[
P(\text{revolt} \mid do(\text{summon}))
=
\sum_c P(C=c)P(\text{revolt}\mid C=c),
\]

whereas EDT uses

\[
P(\text{revolt} \mid \text{summon})
=
\sum_c P(C=c \mid \text{summon})P(\text{revolt}\mid C=c).
\]

The difference is that CDT holds fixed the prior distribution over charisma, while EDT conditions on the action as evidence about charisma.

## 3. Counterfactuals and how to compute them

The source correctly points out that CDT by itself does not specify a unique algorithm for computing counterfactual probabilities. One proposal mentioned in the source is Lewis’s “imaging” technique: to evaluate \(P(A \mathbin{\Box\!\to} O)\), move probability mass from each possible world to the closest possible world in which \(A\) is true, and then see how much probability lands in \(O\)-worlds. This captures the idea that counterfactual supposition is not ordinary conditionalization; it revises the probability distribution by making the supposed action true in a minimally disruptive way. But, as the source notes, imaging requires knowing what one would believe if one were certain of \(A\), and that itself may be a conditional belief, creating a potential regress.

Here I propose, as an operational interpretation not supplied by the source, that structural causal models give a clean way to make CDT computable. A structural causal model consists of variables \(V\), exogenous variables \(U\), structural equations \(F\), and a probability distribution \(P(U)\). An action \(A=a\) is represented by an intervention \(do(A=a)\), which replaces the structural equation for \(A\) with the constant assignment \(a\). The counterfactual outcome under action \(a\) is the value that the outcome variable takes after this intervention. Formally, if \(O_a(u)\) is the value of \(O\) under intervention \(do(A=a)\) and exogenous state \(u\), then

\[
P(O=o \mid do(A=a))
=
P(\{u : O_a(u)=o\}).
\]

If the agent has already observed evidence \(e\) that is not itself the action, she should first update her distribution over exogenous variables:

\[
P(u \mid E=e).
\]

Then the causal expected utility of action \(a\) given evidence \(e\) is

\[
U_{\text{CDT}}(a \mid e)
=
\sum_u P(u \mid E=e)\,D(O_a(u)).
\]

If there are several possible causal models \(M_h\), representing uncertainty about the causal structure itself, a natural extension is

\[
U_{\text{CDT}}(a \mid e)
=
\sum_h P(M_h \mid e)
\sum_u P_h(u \mid e)\,D(O_{a,h}(u)).
\]

This is an additional formal proposal, not explicit in the source, but it fits the source’s core idea: evaluate actions by the probabilities of their counterfactual consequences, holding fixed the agent’s views about causal structure except where the intervention changes them.

In graphical causal models, the same idea is often expressed with the \(do\)-operator. If a variable \(C\) is the only common cause of action \(A\) and outcome \(O\), and if there are no unmeasured confounders, then

\[
P(O=o \mid do(A=a))
=
\sum_c P(O=o \mid A=a, C=c)P(C=c).
\]

This is the familiar backdoor adjustment. It shows the difference from EDT in a precise way: EDT conditions on \(A=a\) and therefore may use \(P(C=c \mid A=a)\); CDT intervenes on \(A=a\) and keeps \(P(C=c)\) fixed, unless \(A\) genuinely causes \(C\).

This operationalization solves part of the vagueness problem, but not all of it. CDT still does not tell the agent which causal model to use. The agent must bring causal judgments, scientific knowledge, or assumptions about predictors, dispositions, and common causes. The formal machinery makes the consequences of those assumptions explicit; it does not magically generate the assumptions.

## 4. Evaluating policies, not merely acts

CDT can evaluate policies as well as single acts. A policy \(\pi\) is a rule mapping observations or decision contexts to actions. In a causal model, implementing a policy means intervening on the relevant decision nodes so that they follow \(\pi\). The causal expected utility of a policy is

\[
U_{\text{CDT}}(\pi \mid e)
=
\sum_u P(u \mid E=e)\,D(Y_{\pi}(u)),
\]

where \(Y_{\pi}(u)\) is the final outcome when the policy \(\pi\) is imposed on the model and the exogenous state is \(u\). If the policy is stochastic, one averages over its random choices as well.

This matters because an action at one time can change what information the agent later receives, what options become available, or what predictions others make. CDT says to compare policies by the causal consequences of implementing them. A single act is just a degenerate policy.

This distinction is important in predictor problems. At the moment of choice in Newcomb’s problem, CDT usually recommends two-boxing because the predictor’s prediction is already in the past. But if the agent can adopt a policy or precommit before the predictor makes the prediction, CDT may recommend a one-boxing policy, because the policy may causally influence the predictor’s prediction. The source does not explicitly discuss this policy-level distinction, but it is a natural consequence of evaluating interventions on decision rules rather than only isolated acts.

## 5. Examples

### Newcomb’s problem

In Newcomb’s problem, a highly reliable predictor has predicted whether the player will take only box B or both boxes A and B. Box A contains \$1,000. Box B contains \$1,000,000 if the predictor predicted one-boxing, and nothing if the predictor predicted two-boxing. The player now chooses.

Let \(K\) be the predictor’s prediction. The payoffs are:

\[
\begin{array}{c|cc}
 & A=\text{one-box} & A=\text{two-box} \\
\hline
K=\text{one-box} & 1{,}000{,}000 & 1{,}001{,}000 \\
K=\text{two-box} & 0 & 1{,}000
\end{array}
\]

CDT reasons by dominance. If \(K=\text{one-box}\), two-boxing yields \$1,000 more than one-boxing. If \(K=\text{two-box}\), two-boxing also yields \$1,000 more than one-boxing. Since the prediction is already fixed and the current action does not causally affect it, CDT recommends two-boxing. Formally, for each \(k\),

\[
D(\text{two-box}, k) = D(\text{one-box}, k)+1000,
\]

so

\[
U_{\text{CDT}}(\text{two-box})
=
U_{\text{CDT}}(\text{one-box})+1000.
\]

EDT gives a different answer. If the predictor is 99% accurate, then taking only box B is strong evidence that the predictor predicted one-boxing:

\[
U_{\text{EDT}}(\text{one-box})
\approx 0.99(1{,}000{,}000)+0.01(0)
=
990{,}000.
\]

Taking both boxes is strong evidence that the predictor predicted two-boxing:

\[
U_{\text{EDT}}(\text{two-box})
\approx 0.99(1{,}000)+0.01(1{,}001{,}000)
=
11{,}000.
\]

So EDT recommends one-boxing. The disagreement arises because the player’s choice is strong evidence of the prediction, even if it does not causally affect the prediction.

### Death in Damascus and adversarial offers

In the “Death in Damascus” scenario, Death predicts where you will be tomorrow and waits there. If Death is a reliable predictor, your choice of location is strong evidence of where Death will be. CDT, however, tends to treat Death’s prediction as already fixed and not causally affected by your current choice. Therefore it may fail to avoid Death, or may make choices that seem irrational once the predictive correlation is taken seriously. The source cites this as a family of counterexamples, including variants where CDT agents voluntarily lose money or forgo guaranteed payoffs.

The Adversarial Offer is one such variant. Two boxes are offered; the buyer may buy one or none, but not both. Each box costs \$1. The seller previously put \$3 in each box that she predicted the buyer would not acquire. Both parties believe the seller’s prediction is accurate with probability 0.75. The source says CDT reasons that at least one box contains \$3, so the average box contains at least \$1.50 in causal expected value, which exceeds the \$1 cost. Hence CDT requires buying one box. But this is profitable for the seller, because the buyer’s actual choice is correlated with the seller’s prediction: the box the buyer chooses is more likely to be one the seller predicted the buyer would acquire, and therefore empty.

The underlying issue is that CDT evaluates the causal effect of buying a box while holding fixed the buyer’s prior views about the seller’s predictions. But the act of choosing a particular box is evidence about what the seller predicted. EDT would treat choosing a box as bad news about its contents and may refuse to buy. CDT can be exploited in such cases because it refuses to use the action itself as evidence about the predictor’s prior state.

### The Psychopath Button

Paul is considering pressing a button that kills all psychopaths. Paul believes a world without psychopaths would be much better, but he is also confident that only a psychopath would press such a button. Paul strongly prefers living in a world with psychopaths to dying.

Let \(H\) be the hypothesis that Paul is a psychopath. If Paul is not a psychopath, pressing the button may cause a good outcome: psychopaths are eliminated and Paul lives. If Paul is a psychopath, pressing the button causes his death. CDT evaluates:

\[
U_{\text{CDT}}(\text{press})
=
P(\neg H)D(\text{world without psychopaths})
+
P(H)D(\text{death}).
\]

If \(P(H)\) is sufficiently low and the benefit of eliminating psychopaths is sufficiently high, CDT can recommend pressing. EDT, by contrast, conditions on the action:

\[
P(H \mid \text{press})
\]

is high, because only a psychopath would press. EDT therefore recommends not pressing. According to the source, Egan argues that almost everyone agrees Paul should not press, yet CDT endorses pressing. The example highlights CDT’s refusal to treat one’s own action as evidence about one’s own type.

## 6. Open questions and a reasonable operational stance

The source identifies two broad criticisms. First, CDT is vague because it does not specify how to calculate counterfactual probabilities. Lewis’s imaging is one answer, but it creates further questions about how to revise beliefs under hypothetical certainty. Second, CDT faces counterexamples in which its recommendation seems irrational, especially in predictor problems, self-prediction problems, and cases where an action reveals the agent’s type.

Egan’s criticism, as summarized in the source, is that CDT holds fixed the agent’s unconditional credences in dependency hypotheses. This can produce a disconnect between the intuitive rule “do what you expect will bring about the best results” and CDT’s rule “do what has the best expected outcome given your initial causal picture.” Oesterheld and Conitzer argue that CDT agents can be made to voluntarily lose money and can be subject to diachronic Dutch books. Joyce, cited in the source as a prominent defender of CDT, argues that CDT can still take evidence about one’s inclinations into account.

My own view is that the most defensible operational version of CDT is the following:

1. Condition on all currently available evidence \(e\) that is not the action being evaluated.
2. Represent the agent’s causal beliefs using one or more structural causal models.
3. Evaluate each candidate action or policy by intervening on the relevant decision variables.
4. Average over uncertainty about exogenous states and, if necessary, over causal models.
5. Choose the action or policy with highest causal expected utility.

This version makes CDT precise enough for many applications. It also clarifies the philosophical commitment: an action is treated as something done, not as something learned. If the agent has introspective evidence before choosing—say, a strong temptation to press the button—that evidence should be included in \(e\), and it can raise the probability of being a psychopath before the choice. But if the only apparent evidence is the hypothetical action itself, CDT does not condition on it. That is the theory’s distinctive and controversial discipline.

Whether this discipline is correct is the real dispute. If one believes that rational choice should respond to all information, including information provided by one’s own choice, EDT or some hybrid theory may seem better. If one believes that choice should track causal efficacy rather than diagnostic news, CDT remains attractive. The source reports that philosophers usually prefer CDT when forced to choose between CDT and EDT, but the counterexamples show that this preference is not unchallenged.

## Conclusion

Causal decision theory evaluates actions by their expected causal consequences, not by the evidential news they provide. Its core formula replaces conditional probabilities with probabilities of counterfactuals or interventions. This makes CDT recommend two-boxing in Newcomb’s problem, summoning Bathsheba in Gibbard and Harper’s King David case, and sometimes pressing the Psychopath Button. The theory’s strength is that it separates causation from correlation. Its difficulty is that counterfactuals require a causal model, and the theory itself does not fully specify how to obtain one. A structural causal model gives a useful operational interpretation, but the philosophical disputes remain: in cases where choices are strongly predicted or self-diagnostic, ignoring the evidential import of one’s own action can look either admirably causal or stubbornly blind.

## References

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs: Conditionals, Belief, Decision, Chance, and Time*, 153–90.

Lewis, David. 1976. “Probabilities of Conditionals and Conditional Probabilities.” *Philosophical Review* 85 (3): 297–315.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Egan, Andy. 2007. “Some Counterexamples to Causal Decision Theory.” *Philosophical Review* 116 (1): 93–114.

Oesterheld, Caspar, and Vincent Conitzer. 2021. “Extracting Money from Causal Decision Theorists.” *Philosophical Quarterly* 71 (4): pqaa086.

Pearl, Judea. 2009. *Causality: Models, Reasoning, and Inference*. 2nd ed. Cambridge University Press.

Wikipedia contributors. “Causal Decision Theory.” Revision 1381555528. Licensed under CC BY-SA 4.0. This essay adapts material from that article.