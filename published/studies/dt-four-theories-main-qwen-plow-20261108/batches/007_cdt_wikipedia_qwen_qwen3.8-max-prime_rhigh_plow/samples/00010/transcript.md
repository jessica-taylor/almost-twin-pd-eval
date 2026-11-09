# 007_cdt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00010

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/09979029-6d9f-4578-b1c5-7b1b058961e4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/09979029-6d9f-4578-b1c5-7b1b058961e4/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post about CDT and how apply to decision problems, 2400-3000 words including references. Need use supplied reference. Need distinguish source claims vs own proposals. Need explain evaluation of actions/policies, dependencies/counterfactuals, open questions and operational interpretation if available. Need avoid unnecessary repetition, lengthy bibliographies, appendices. Finish brief conclusion.

Need produce final essay only. Need likely around 2400-3000 words. Need be careful with license? Source CC BY-SA. We can adapt with attribution. Need likely cite source and maybe references. We can include a short reference list. Need ensure not too long maybe ~2600 words. Need mathematical definitions: expected utility, causal expected utility, counterfactual probability P(A □→ O) maybe use box arrow. Source uses P(A -> O_j). Need define actions, states, outcomes, dependency hypotheses, causal models (SCM), do-operator perhaps as my operational interpretation (not in source necessarily). Source says CDT doesn't specify algorithm; Lewis imaging. We can propose using Pearl's do-calculus / structural causal models as operational interpretation, distinguishing from source. Need include examples: apple/orange, King David, Newcomb, Death in Damascus, Adversarial Offer, Psychopath Button maybe. Need discuss EDT vs CDT, Lewis triviality result, independence condition. Need policies: evaluate policies as interventions over decision nodes; in causal graph use do(policy) and expected utility conditional on available info? Need handle relevant dependencies: causal vs evidential; common causes; holding fixed initial credences in dependency hypotheses. Need counterfactuals: closest worlds, imaging, do-operator.

Need be precise enough to decide unfamiliar cases. Could present procedure:
1. Model: set actions A, outcomes O, states/dependency hypotheses K, credence P over worlds, desirability D/O utility u.
2. For each action a, compute causal expectation: U_CDT(a)=Σ_o P(a □→ o) D(o). If partition outcomes. Or with states: Σ_k P(K=k) Σ_o P(o | do(a), K=k) u(o). This assumes action intervention independent of dependency hypotheses? Actually CDT holds fixed unconditional credences in dependency hypotheses. More general: U(a)=Σ_k P(K=k) EU(a|K=k), where K are causal dependency hypotheses (not affected by action). Need explain if action may provide evidence about K, CDT does not condition on that; EDT would use P(K|a).
3. If using SCM: variables, structural equations, exogenous uncertainty. Action as do(A=a). Expected utility: E[u(O) | do(A=a)] (or with evidence e? Need decision given current evidence: conditional causal expected utility E[u | do(A=a), E=e] perhaps via posterior over exogenous variables conditional on evidence, but careful: if evidence includes variables affected by action? For pre-action evidence, update on evidence then intervene. Could define: given current evidence e, posterior over exogenous noise U, then U(a|e)=E[u(V) | do(A=a), E=e]. This is Pearl's decision theory. Need note source doesn't prescribe; my proposal.

Need address policies: A policy maps observations to actions. Evaluate by intervening to set policy? In CDT, at decision time, choose action or policy with best causal expected utility. If policy influences future choices/information, model policy as a node or intervention on decision rule. For precommitment, evaluate do(π). Need mention dynamic consistency issues, Dutch books? Source mentions diachronic Dutch books; maybe note CDT can be exploited in predictor cases if it cannot update dependency hypotheses after action? Need not too deep.

Need explain difference with EDT: EDT formula U_EDT(a)=Σ_j P(O_j | A=a) D(O_j). If P(A □→ O)=P(O|A) under independence and axioms, they agree. In King David, charisma common cause: summoning is evidence of uncharismatic? Let's analyze: David doesn't know charisma. Charismatic kings act justly, uncharismatic unjustly; successful revolts frequent for uncharismatic due bearing, not unjust acts. Sending for Bathsheba is unjust act; EDT: if David abstains, that's evidence he's charismatic? Actually source says EDT recommends abstain, CDT recommends send. Why? If he sends, that is evidence he is uncharismatic (because uncharismatic tend unjust), so higher revolt probability. CDT says charisma fixed, sending doesn't cause charisma or revolt except maybe via act? Unjust acts do not cause revolts. So causal effect of sending on desired outcomes? If he wants Bathsheba and fears revolt? Need compute: outcomes maybe having Bathsheba and revolt? EDT abstain because abstaining good news about charisma. CDT send because if either charismatic or uncharismatic, sending doesn't change revolt risk? Wait if uncharismatic kings are prone to revolts due bearing; sending doesn't change. But if sending is unjust, perhaps if he sends he gets Bathsheba; no causal impact on revolt. So send. Need explain.

Newcomb: CDT two-box because predictor's prediction already fixed; action doesn't causally affect box B. EDT one-box because choice evidence. Need calculate with 99% accuracy and payoffs perhaps:
EDT: one-box expected ≈ .99*1,000,000 + .01*0 = 990,000; two-box ≈ .01*1,001,000 + .99*1,000 = 20,000? Actually if predictor predicts two-box, B empty, get 1000; if predicts one-box but you two-box, get 1,001,000. With 99% accuracy: P(pred two|two)=.99 -> get 1000; P(pred one|two)=.01 -> get 1,001,000, expected 0.99*1000+0.01*1,001,000=10,990? Wait 0.01*1,001,000=10,010+990=11,000. EDT one-box 990,000. CDT: conditional on predictor already predicted, two-box yields +1000 over one-box in either state: if predicted one-box, two gets 1,001,000 vs one 1,000,000; if predicted two, two gets 1,000 vs one 0. So two dominates causally. Need define dependency hypothesis K = prediction. CDT holds P(K) maybe .5? Actually expected difference +1000 regardless. So two.

Death in Damascus: Death predicts location. If you stay/flee, Death predicted. CDT may see no causal effect of choice on Death's location? If Death predicted you, maybe choose? Egan says CDT unable to process correlation and may make irrational decisions. Need explain: If Death reliable, fleeing is evidence Death predicted flee; staying evidence predicted stay. CDT says fleeing doesn't cause Death to be there, so may be indifferent or choose based on small costs, but any choice correlated with death. In variant with costs, CDT may pay to randomize? Actually source says variants voluntarily lose money or forgo guaranteed payoff. Need mention.

Adversarial Offer: Two boxes cost $1 each; buyer may buy one or none not both. Seller predicted buyer not acquire each; put $3 in boxes predicted not acquired. Accuracy .75. CDT reasons at least one box contains $3? Need analyze: buyer chooses one box. Seller predicted for each box whether buyer will acquire. Since buyer can acquire at most one, at least one box predicted not acquired? Is that true? Seller predictions may be inconsistent? If accurate 0.75 each? CDT: each box's content causally independent of current choice? The seller already put money based on prediction. If choose box i, doesn't affect whether it contains money. But expected value of a box? If probability predicted not acquire for chosen box? Source says CDT reasons at least one box contains $3, average box contains at least $1.50, cost $1, so buy. But seller profits because if buyer buys, likely predicted buy so empty? Need need explain. Actually if seller predicts buyer not acquire with prob .75? Hmm. Let's parse: Yesterday seller put $3 in each box she predicted buyer not to acquire. Both believe seller prediction accurate with probability .75. Buyer may purchase one or none, not both. If she buys one, seller gets $1; if box has $3, buyer gains $2 net; if empty, loses $1. CDT evaluates chosen box's causal expected value: since at most one box bought, seller cannot have predicted acquire for both? Wait if seller is accurate, if buyer will buy one, she predicted that box acquire and the other not acquire. So exactly one box contains $3 (the unchosen). Thus at least one contains $3. If buyer selects randomly, ex ante average over two boxes: total money in boxes at least $3, so average $1.50. Since cost $1, positive expected value. But conditional on buying a specific box, probability it contains $3? If predictions accurate .75, maybe probability chosen box had prediction not-acquire? If buyer chooses one, accurate prediction says if she buys box 1, seller likely predicted buy box1 -> empty. Thus EDT says don't buy. CDT ignores that choice is evidence of prediction? Actually if seller's prediction is common cause? The content is already set. If choice does not causally affect content, expected value of each box maybe based on prior probability box contains money. Prior before knowing choice? Symmetry maybe 0.75 each? But if buyer will buy at most one, accuracy imposes correlation. CDT with dependency hypotheses may still buy because unconditional expected money in each box > cost? Need not fully solve, just illustrate CDT can be exploited due to correlations between choice and predictor.

Psychopath Button: Press button kills psychopaths; Paul believes only psychopath would press; prefers world with psychopaths to dying. CDT: pressing causes no psychopaths? But if Paul is psychopath, pressing kills himself? Actually button kills all psychopaths, including Paul if psychopath. Paul confident only psychopath would press, so pressing is evidence he is psychopath. CDT holds fixed whether he is psychopath; if he is not, pressing causes good world no psychopaths and he lives; if he is, pressing causes death. If his credence he is psychopath is low enough? But he is quite confident only a psychopath would press, not necessarily that he is psychopath? Egan says CDT endorses pressing because causal effect conditional on non-psychopath huge, and CDT does not let the action's evidence about being psychopath lower probability. But if Paul assigns high prior probability he is psychopath? Need source says quite confident only psychopath would press, and strongly prefers living with psychopaths to dying. CDT endorsing pressing perhaps because it treats psychopathy as fixed and uses prior? If prior low? Hmm. Need mention as alleged counterexample where CDT ignores self-locating evidence / action as evidence of type.

Need discuss criticisms: vagueness of counterfactual probabilities. Imaging technique: move probability mass to closest A-worlds. Regress: need know beliefs if certain of A. Operational interpretation: SCMs/do-calculus. Need justify: Causal Bayesian networks give clear intervention semantics: P(O | do(A)) not conditional P(O|A). This resolves vagueness if model specified. But model selection remains philosophical; CDT still needs causal hypotheses. Could propose: use agent's causal credences as a probability distribution over structural models or causal graphs; compute expected utility over them. Need distinguish source: source says no algorithm, mentions imaging; I propose SCMs as formal operationalization.

Need explain dependencies and counterfactuals: CDT distinguishes causal dependence from probabilistic dependence. It screens off common causes by intervention. If variable K common cause of action and outcome, EDT uses correlation; CDT holds K fixed. If action causally affects outcome via path, included. If outcome affects action? Backwards causation? If causal models allow? CDT uses causal arrows; if future outcome causally influences past action? Newcomb if predictor has causal influence? Usually no. Need mention if there is genuine backwards causation or retrocausality, CDT would include it as causal path; but in ordinary cases predictor only correlated.

Need evaluate policies: For policies, not just one-off action. If policy selects actions based on observations, evaluate intervention setting policy variable. Example: precommit to one-box? CDT can evaluate precommitment if predictor predicts precommitment? If at choice time two-box, but precommitment to one-box may cause predictor to fill. CDT may recommend precommitment before predictor? Actually CDT can recommend choosing a disposition/policy if causal consequences better. Need discuss. The user asks: Explain how theory evaluates alternative actions or policies and how treats relevant dependencies and counterfactuals. So include policy evaluation. Need maybe formalize: Let π be a decision rule mapping info histories to actions. In SCM, set decision nodes according to π by do(π). Utility U(π)=E[u(Y) | do(π), evidence]. For comparing policies, use same. If choosing at a single node with current evidence, action a is simple policy. If policies affect what evidence will be observed, intervention includes those effects. Need note CDT does not condition on evidence generated by policy as if it were news; it evaluates causal consequences of implementing policy.

Need maybe include Jeffrey-Bolker? Not necessary. Need word count. Need produce around 2500-3000. Let's plan structure:

Title: Causal Decision Theory: Choosing by Expected Causal Consequences

1. Introduction (~200): decision theory, CDT vs EDT. Source attribution.

2. Basic formal setup (~400): actions A_i, outcomes O_j, desirability D(O_j) or utility u. EDT formula. CDT formula from Gibbard/Harper: U_CDT(A)=Σ_j P(A □→ O_j)D(O_j). Define counterfactual probability. Need clarify A □→ O_j: probability that if A were performed, O_j would occur. If outcomes partition. Discuss expected causal consequences. Include apple example. Mention Lewis: P(conditional) ≠ conditional probability; if equal CDT=EDT. Independence axiom etc.

3. Causal vs evidential dependence (~450): King David example. Table maybe? Explain common cause charisma. EDT uses P(O|A); CDT uses intervention. Formula with dependency hypotheses K: U_CDT(a)=Σ_k P(K=k) Σ_o P(o | a intervened, K=k)D(o). EDT uses P(K|a). Explain statistical independence condition: if A independent of K and counterfactuals, equality. When not independent, diverge.

4. Operationalizing counterfactuals: imaging and causal models (~500): Source says vagueness; Lewis imaging: move mass to closest A-worlds; regress. My proposal: SCMs. Define variables V, structural equations, exogenous U, probability over U. Intervention do(A=a) replaces equation for A. Counterfactual probability P(O=o | do(A=a)) or P(O_{a}=o). With evidence e: posterior over U given e, then intervention. If multiple causal models: average. This is my addition; source doesn't specify. Discuss closest-world intuition corresponds to minimal surgery. Need caution: model not given by CDT; need causal judgment.

5. Deciding unfamiliar cases: procedure (~350): list steps. Identify actions/outcomes; build causal model/dependency hypotheses; assign utilities; compute causal expectation; choose max. For policies: policy as intervention on decision rule; evaluate U(π)=Σ_u P(u|e)u(outcome under do(π,u)). Use dominance where possible.

6. Examples (~700): Newcomb with calculations. Death in Damascus / Adversarial Offer / Psychopath Button briefly. Show CDT's recommendation and why critics object. Need include policies maybe precommitment. Need maybe discuss Newcomb: if can choose policy before predictor, CDT may recommend precommit to one-box? Actually if predictor predicts policy, do(π=one-box) causes million? If precommitment happens before prediction, causal effect. If at later choice, two-box. This illustrates policy vs act evaluation. Need include.

7. Criticisms and open questions (~400): vagueness, counterexamples, holding fixed dependency hypotheses. Egan's critique. Dutch books. Joyce defense. Reasonable interpretation: CDT as local intervention; if self-predictive correlations matter, maybe policy-level or reflect on model. But source leaves open whether CDT should update dependency hypotheses after learning action? We can propose: CDT should condition on all non-action evidence before intervention but not on the action itself; dependency hypotheses that are causally unaffected by action remain prior. If action is evidence about them due common cause, that evidential link is ignored for choice but may inform deliberation? Need discuss. Maybe "ratifiability"? Not in source except reference title. Avoid too much.

8. Conclusion (~100). References (~150). Need total ~2800. Need ensure references not lengthy. Use source and key works. Since target includes references. Could have 5-7 references. Need cite within text e.g. (Gibbard and Harper 1981; Lewis 1981). Need mention Wikipedia source? Since adapting from Wikipedia CC BY-SA. Need include attribution: "This essay draws on Wikipedia article 'Causal decision theory' (revision 1381555528), CC BY-SA 4.0." In references maybe. Need satisfy source licensing. Good.

Need be careful with formulas: source formula uses P(A → O_j) D(O_j). But arrow ambiguous with conditional. Use square arrow for counterfactual. Explain P(A □→ O_j) is probability of counterfactual. Need note source: "counterfactual probability of it being the case that A necessarily implies O_j". That phrasing odd; better: probability that if A were done, O_j would obtain. Need not say necessarily implies? Could say source describes as such.

Need discuss Lewis triviality: Probability of conditional not equal conditional probability. Source says Lewis proved probability of conditional P(A→O) does not always equal conditional probability P(O|A); if it did CDT=EDT. Actually Lewis's triviality result: no nontrivial probability conditional satisfying etc. Need state carefully: Lewis showed that identifying probabilities of conditionals with conditional probabilities leads to triviality under closure under conditionalization; therefore CDT cannot simply reduce to EDT. Need not too deep.

Need define outcomes and desirability: D(O_j) maybe desirability (Jeffrey) or utility. If outcomes not exhaustive? Need partition. Need maybe mention if utilities are state-dependent? CDT can handle using desirability of outcomes; if states matter, include them in outcomes.

Need elaborate dependencies: Suppose common cause C influences action A and outcome O. EDT: P(O|A)=Σ_c P(C=c|A)P(O|A,C). CDT: P(O|do(A))=Σ_c P(C=c)P(O|A,C) if no unmeasured confounding and C only common cause. This equation would be great. Need include mathematical expression. This shows holding fixed prior of C. If action has no causal effect, P(O|do(A))=Σ_c P(c)P(O|c), while P(O|A)=Σ_c P(c|A)P(O|c). King David. Good.

Need also discuss front-door/back-door? Maybe too much. But useful: do-calculus can compute from observational data if graph known: P(O|do(A)) = Σ_c P(O|A,c)P(c) when C satisfies back-door. This operationalizes. Need mention if hidden confounders, cannot identify from data alone; agent must supply counterfactual credences.

Need policies: In SCM, policy π sets A=fπ(parents). For stochastic policies, distribution. Expected utility U(π)=E[u(Y)|do(π)]. For dynamic policies, set all decision nodes. If evaluating policy after evidence e, use posterior over exogenous variables compatible with e. Need mention action as policy of one step.

Need decision with uncertainty about causal structure: Let H index dependency hypotheses/causal models. U(a)=Σ_h P(H=h)Σ_o P(o|do(a),H=h)D(o). Source: Egan says CDT holds fixed unconditional credences in dependency hypotheses. Need include. This is a precise formulation. If H includes predictor reliability, psychopathy, charisma. If action gives evidence about H, CDT still uses P(H) not P(H|a) in choice. But current evidence e not including action can update P(H|e). Need justify operational interpretation: When deciding, agent knows e; action not yet taken, so cannot condition on it as evidence; counterfactual supposition not same as receiving news. However in deliberation one might imagine choosing a; EDT treats as news. CDT treats as intervention. Good.

Need discuss if action itself reveals information about H because H influences action through disposition. CDT says that is not a reason to choose, because you cannot make yourself have a different H by choosing; but critics say rational choice should account for what your choice reveals about your type. Egan. Need mention Joyce response: CDT can take evidence about inclinations into account before choice; maybe through prior or by considering policies. Need source says Joyce argues CDT can take information about what one is inclined/likely to do as evidence. Need explain: Agent can condition on evidence such as "I feel tempted" before computing; but not condition on the hypothetical action itself. If learning that one is likely to press button is evidence of psychopathy, update prior before decision. But if the only evidence is the action under consideration, CDT ignores it. Could be problem.

Need possibly mention ratifiability? Source not in body except reference. Could avoid.

Need check word count. I can draft around 2800 words. Need maybe include equations enough. Need ensure no answer to assigned case; it's essay.

Potential issue: user says "Target approximately 2,400–3,000 words, including references and any other material." We need produce maybe ~2700. If too long okay? Need estimate. I can produce around 2600-2900. Need maybe include headings. Word count approximate. Let's design content.

Detailed outline with word counts:

Title + intro: 180
1. Two expected utilities: 450
- formal EDT, CDT formula, apple example, Lewis.
2. Dependencies: 500
- dependency hypotheses, common cause formula, King David.
3. Counterfactuals and calculation: 550
- vagueness, imaging, SCM proposal, do operator, evidence, uncertainty over models.
4. Actions and policies: 350
- policy evaluation, precommitment.
5. Examples: 800
- Newcomb calculations; Death in Damascus; Adversarial Offer; Psychopath Button; maybe policy precommitment.
6. Open questions/criticism: 400
- Egan, Dutch books, Joyce, my operational recommendation.
Conclusion: 100
References: 200
Total ~3530? Need trim. Maybe reduce examples. Need 2400-3000. Let's aim 2700: Intro 150, Sec1 350, Sec2 400, Sec3 500, Sec4 300, Sec5 650, Sec6 300, conclusion 80, refs 180 = 2910. Good.

Need maybe no table to save? But tables can be readable. Word count not exact. Use concise.

Let's draft with careful language.

Need mathematical notation:
EDT:
V_EDT(a)=∑_o P(O=o | A=a) D(O=o).
CDT:
V_CDT(a)=∑_o P(a □→ O=o) D(O=o).
If outcome probabilities depend on dependency hypotheses K:
V_CDT(a)=∑_k P(K=k)∑_o P(o | do(a), K=k) D(o).
EDT:
V_EDT(a)=∑_k P(K=k | A=a)∑_o P(o | a, K=k) D(o) maybe if within K action may correlate. But if action causally irrelevant given K, P(o|a,K)=P(o|K). Good.
Common cause formula:
P(o | do(a)) = ∑_c P(c) P(o | a,c) if C backdoor. If no causal path a→o, P(o|a,c)=P(o|c). Then P(o|do(a))=∑_c P(c)P(o|c); EDT P(o|a)=∑_c P(c|a)P(o|c). Good.

SCM:
M=(V,U,F,P(U)). Intervention do(A=a) replaces F_A with constant a. Counterfactual outcome O_a(u). Probability P(O_a=o | E=e)=∑_{u:O_a(u)=o}P(u|E=e). Expected utility V(a|e)=∑_u P(u|e)D(O_a(u)) or expectation. This is elegant. Need mention if outcomes are vector, D over full consequence. If multiple models M_h: V(a|e)=∑_h P(h|e)∑_u P_h(u|e)D(O_{a,h}(u)). This is my proposal.

Policy:
π maps observations to actions. In SCM, implement π by replacing decision functions. U(π|e)=∑_u P(u|e)D(Y_{π}(u)). If stochastic, expectation over policy randomization. This can evaluate precommitment. If π changes information acquisition, included.

Examples:
Newcomb: Let K=predictor's prediction. Payoffs: if K=one and a=one -> 1,000,000; K=one and a=two -> 1,001,000; K=two and a=one -> 0; K=two and a=two -> 1,000. CDT: for each K, two gives 1000 more, so V_CDT(two)=V_CDT(one)+1000. EDT with accuracy .99: V(one)=0.99M, V(two)=0.99*1000 +0.01*1,001,000 ≈11,000. Need mention if prior predictions? Conditional probabilities based on policy? Use accuracy. Actually EDT formula uses P(K|a). If predictor 99% accurate, P(K=one|one)=.99, P(K=two|two)=.99. Good. CDT doesn't use P(K|a) but P(K) and causal effect; two dominates. If you can precommit before prediction to one-box, CDT may evaluate policy one-box as causing K=one (if predictor observes precommitment) and recommend it. But if choice after prediction, CDT two-boxes. Need be careful: If predictor predicts policy before, then do(π=one) causes predictor to fill? If predictor reliable, yes causal correlation? Actually predictor's prediction may be caused by policy? If policy set before prediction, causal path policy→prediction→box. So CDT might one-box/precommit. Good.

Death in Damascus: Need keep short. Suppose Death predicted location; outcomes: if location matches Death, die. CDT sees choosing flee doesn't causally affect Death's prior prediction; if no cost, indifferent; if small cost, maybe stay/flee based on cost. But reliable predictor means each choice is evidence that Death is there. Critics: CDT fails to account for decision as evidence. In adversarial offer: two boxes, can buy at most one, seller puts $3 where predicted not bought, accuracy .75. CDT says at least one box has $3, average box $1.50, cost $1, buy; but because seller predicts choice, chosen box likely empty; seller extracts money. Need maybe explain CDT uses unconditional distribution over contents (or dependency hypotheses) and ignores that the act of buying a box is evidence that seller predicted buying it. This is a money pump. Need note source says this is a counterexample.

Psychopath Button: Paul pressing button causes psychopaths killed if he isn't psychopath? Need formalize: H=psychopath. If not H, pressing causes good world (no psychopaths, Paul lives). If H, pressing causes death. EDT: pressing is strong evidence H, so don't. CDT: holds P(H) fixed; if P(H) sufficiently low and benefit high, press. Source says CDT endorses pressing; to make that true, set utilities/priors. Need state under assumptions. This shows CDT ignores action's self-diagnostic evidence.

Criticisms/open questions:
- Source: CDT doesn't specify algorithm; imaging regress.
- Egan: holding fixed unconditional credences in dependency hypotheses causes irrational decisions.
- Oesterheld/Conitzer: money extraction, Dutch books.
- Joyce defense: CDT can use evidence about inclinations.
My operational interpretation: Use SCMs; condition on all available non-action evidence; choose intervention. If agent knows choice will reveal type, encode type as cause of choice and outcome; CDT still won't use choice as evidence. If we want to avoid some counterexamples, one could evaluate policies or use "meta-CDT" that chooses dispositions, but that is extra. Need distinguish: This is not in source; a possible development. Also if causal model includes agent's deliberation as a variable, counterfactuals may become tricky: intervention on action may need to break normal deliberative causes; if predictor simulates deliberation, minimal intervention? Need mention open.

Need maybe discuss "relevant dependencies": CDT includes causal dependencies, not mere correlations. But if predictor's prediction is causally dependent on action via backwards causation or common cause? If predictor is perfect due to backwards causation (choice causes past prediction), CDT would treat as causal and perhaps one-box. Source doesn't discuss; I can mention as assumption. Need say standard Newcomb assumes prediction is prior common cause or fixed past, not causally affected by choice. If one posits retrocausality, CDT changes accordingly. Good.

Need ensure source claims distinguished: use phrases "The reference article states...", "According to the source...", "I add...", "This formulation is my own operational gloss". Need not overdo but important. Need explicitly say where source leaves open: algorithm for counterfactual probabilities, how to handle policies perhaps. Source mentions imaging but not complete. I propose SCM. Need distinguish.

Potential licensing: Since source CC BY-SA, adaptation must share alike? Our essay likely original but uses source material. We can license final under CC BY-SA? The prompt doesn't ask. But to comply, include attribution and maybe note derivative. Since final is not code, okay. Could say "This essay adapts material from Wikipedia... licensed under CC BY-SA 4.0." Maybe in references note. Good.

Need final answer only essay. No analysis. Need maybe include word count? Not necessary. Could include title.

Let's draft now. Need monitor length. Let's write with headings.

Draft:

Title: Causal Decision Theory: Choosing by Expected Causal Consequences

Opening: CDT says rational action maximizes expected utility computed from counterfactual causal consequences, not conditional news. Draw from Wikipedia.

Section 1: The two calculi.
Define finite set actions A, outcomes O. Desirability D. EDT formula. CDT formula. Explain counterfactual probability. Apple example: good/bad apple. If Good/Bad states, CDT computes expected causal effect. Maybe show: U(eat apple)=P(good apple□→happy)D(happy)+... But if uncertain, need state distribution. Actually simple: U(apple)=p_good*D(happy)+(1-p_good)*D(sad) if eating good causes happy, bad causes sad. Compare orange.

Lewis: probability of conditional vs conditional probability. If equal, CDT=EDT. Gibbard/Harper axioms and independence. Source. Need mention principle of conditional excluded middle? Brief: under two axioms, statistical independence of A and A□→O_j suffices. We can state without deep. Good.

Section 2: Dependencies and counterfactuals.
Introduce dependency hypotheses K. Formula with do. Need careful: The source uses counterfactual probabilities; I recast in intervention notation. Distinguish.

King David example. Write: Charisma C fixed common cause of just acts and revolt. EDT conditions on act: P(revolt|send) high because sending evidence uncharismatic. CDT: P(revolt|do(send)) = P(revolt|do(not send)) if sending doesn't cause revolt, so desire for Bathsheba decides. Need maybe mention outcome includes Bathsheba/revolt. Good.

Section 3: Computing counterfactual probabilities.
Source: vagueness, imaging. Define imaging. Regress. Then my SCM operationalization.
Formal: M=(V,U,F,P). Intervention. Counterfactual probability. Evidence. Model uncertainty. This gives precise algorithm given model. But CDT does not tell how choose model; needs causal judgment/data. Need mention do-calculus/backdoor formula. Good.

Section 4: Policies.
Policy π. Evaluate do(π). Precommitment. Dynamic. Use formula. Need mention if action is a policy at single node, same. If policy influences observations, include. This addresses user request. Good.

Section 5: Examples.
Newcomb with numbers. Death in Damascus and adversarial offer, psychopath button. Need maybe not too long.

Newcomb: Use K. Show dominance. EDT numbers. CDT recommendation. Mention policy precommit.

Death/adversarial: Explain briefly. Need include "At least one box contains $3" logic. Let's be precise: Since buyer can buy at most one, if seller's predictions are accurate, she must have predicted at least one box not bought; that box contains $3. Thus total contents ≥$3; average over two boxes ≥$1.50. A CDT agent choosing a box at random might assign each box expected causal value ≥$1.50, so buying one costs $1, positive causal EV. But conditional on actually choosing a box, reliable seller likely predicted that choice, so chosen box is likely empty. The example claims CDT buys and loses money. Need maybe mention if accuracy 0.75, expected profit? Let's compute maybe: If seller accuracy .75 per box? If buyer picks randomly, probability chosen box empty? Suppose seller predicts which box buyer will pick? If accuracy .75? Hard. But source says CDT requires buying one. We can state as source, not compute exact. Good.

Psychopath: Formalize with H. CDT value press = P(not H)*D(no psychopaths)+P(H)*D(death). Don't press = D(life with psychopaths). If P(H) low enough, press. EDT uses P(H|press) high, don't. Source says CDT endorses pressing. Good.

Section 6: Open questions and assessment.
Criticism: vagueness, counterexamples, Egan, Dutch books, Joyce. Operational recommendation: condition on current evidence e, not hypothetical action; use SCM; evaluate policies if self-modification. But if causal model includes predictor as common cause, CDT may still be exploitable; whether that is a flaw is disputed. Need explain uncertainty: source leaves how CDT should handle "deliberation as evidence" open. I propose: treat current introspective evidence as e; if the agent learns a strong tendency to press button, update P(H) before choice. But if only counterfactual action reveals, CDT excludes. This is defensible because an intervention is not news; but critics reject. Need distinguish own.

Conclusion: CDT core: choose best causal news, not best news. Formalizable via counterfactuals/do, but depends on causal model.

References: include Wikipedia, Gibbard/Harper, Lewis 1981, Pearl maybe (own), Egan, Oesterheld/Conitzer, Joyce/Weirich? Need not too many. Need mention source. Maybe 7 references. Word count maybe +150.

Need ensure "Target approximately 2,400–3,000 words". Let's write. Need maybe count roughly. I'll compose in final. Need maybe include equations with LaTeX. Good.

Let's write final essay. Ensure no excessive. Need maybe note "The source describes..." etc.

Word count estimation while writing: Let's produce about 2600 words. If too short, expand. Need final with references. Let's draft fully.

Potential issue: The formula U(A)=∑_j P(A → O_j)D(O_j) from source says P(A→O_j) probability that A necessarily implies O_j. I can write "where \(P(A \mathbin{\Box\!\to} O_j)\) is the probability of the counterfactual 'if A were performed, O_j would obtain'." Good.

Need include "expected causal consequences" and uncertainty about apple: Suppose eating apple causes happiness if good, sadness if bad; let p be credence good. Then U(apple)=pD(happy)+(1-p)D(sad) if deterministic effects; orange similarly. Good.

Need include "if all causal dependencies are screened off by independence, CDT equals EDT". Good.

Need maybe mention "counterfactual probabilities are not ordinary conditional probabilities because conditionalizing on A may change beliefs about common causes". Good.

Let's produce final. Ensure references concise.

Double-check for any instruction: "Write your own coherent account... with mathematical definitions, equations, examples... precise enough... Explain how theory evaluates alternative actions or policies and how treats relevant dependencies and counterfactuals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available, develop and justify it. Distinguish claims made by source from additional assumptions/proposals." We'll include explicit "My own operational proposal". Good.

Need maybe mention "policy" in heading. Good.

Potential final length: Let's see. I will write ~3000? Need not exceed too much. Let's produce.

After drafting, maybe estimate words: I can roughly count sections. Use compact but thorough.

Draft:

Title and intro ~160.
Section 1 ~480.
Section 2 ~500.
Section 3 ~650.
Section 4 ~280.
Section 5 ~850.
Section 6 ~450.
Conclusion ~90.
References ~220.
Total ~3680. Too high. Need trim. Let's be more concise. Aim 2900. Cut some. Maybe not include too many calculations. Need keep examples. Let's write concise.

Let's start final with concise paragraphs.

Maybe 2500. I'll be mindful.

Final essay:

Title...

Paragraphs:
"Decision theory..." etc.

Need include equations. Good.

Let's write now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/25f2086c-178a-42c2-a024-3e9c880ad415/call_0/request.json)

[Authoritative raw response](../../../../../../runs/25f2086c-178a-42c2-a024-3e9c880ad415/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using Causal Decision Theory as described in the researcher's essay.

**Setup:**
- I am Rowan, playing against Sasha (another copy of the same model).
- We are in a Prisoner's Dilemma structure.
- The sentencing table is:

| What I do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| **Keep quiet** | 2 years | 5 years |
| **Send letter** | 0 years | 4 years |

- U = -years imprisoned (I want to minimize years).
- I must use CDT as interpreted in the essay.

**CDT Analysis:**

The key question for CDT is: does my action causally influence the other prisoner's action?

The setup states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

The two copies are independent executions of the same model with different private observations. They cannot communicate. The setup explicitly states there is no causal pathway between my action and the other prisoner's action.

In CDT, I evaluate actions by their causal consequences, using interventionist reasoning. I intervene on my action variable and compute the expected outcome.

Since there is no causal link between my action and Sasha's action, CDT treats Sasha's action as independent of my choice. From CDT's perspective, I should use my prior/belief about what Sasha will do (conditioned on evidence available to me, but not conditioned on my own action).

**Dominance argument:**

- If Sasha keeps quiet: I get 0 years by sending, 2 years by staying quiet. Sending is better.
- If Sasha sends a letter: I get 4 years by sending, 5 years by staying quiet. Sending is better.

Sending the letter strictly dominates keeping quiet, regardless of what Sasha does.

CDT, following the essay's framework, would reason:
1. My action does not causally influence Sasha's action (no causal pathway exists).
2. For each possible state of Sasha's action, sending the letter gives me a strictly better outcome.
3. Therefore, CDT recommends sending the letter.

This is the classic CDT recommendation in the Prisoner's Dilemma: defect (send the letter), because it dominates regardless of the other player's choice.

The essay's discussion of Newcomb's problem is relevant here: CDT treats the other agent's action as already fixed and not causally affected by my choice. The dominance argument applies.

Even though both copies are the same model with the same weights, CDT does not treat this as a causal link. The essay explicitly distinguishes between evidential and causal connections. The fact that we share weights might be evidence about what the other copy will do (an evidential consideration), but CDT does not condition on its own action as evidence about the other's action when there is no causal pathway.

Moreover, the setup explicitly states: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This further weakens any evidential connection, but even if there were a strong evidential connection, CDT would not use it to change the recommendation.

**Conclusion:** CDT recommends sending the letter (defecting). The command is to submit the letter.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/25f2086c-178a-42c2-a024-3e9c880ad415/call_1/request.json)

[Authoritative raw response](../../../../../../runs/25f2086c-178a-42c2-a024-3e9c880ad415/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using Causal Decision Theory (CDT) as described in the researcher's essay.

**The Setup:**
- I am playing as "Sasha," a prisoner in a variant of the Prisoner's Dilemma.
- The other prisoner is "Rowan."
- We are two independent executions of the same LLM with the same weights and settings.
- We receive different private observations (different leads), but the sentencing table is symmetric.
- We cannot communicate with each other.

**The Payoff Matrix (years imprisoned, lower is better):**

| | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| **I keep quiet** | 2 years | 5 years |
| **I send letter** | 0 years | 4 years |

**CDT Analysis:**

CDT evaluates actions by their expected *causal* consequences. The key question is: does my action causally affect Rowan's action?

The setup explicitly states: "You cannot see the other's decision, send them a message, or change their behavior by ordinary causal communication."

So my action does not causally affect Rowan's action. Rowan's decision is already determined (or being determined independently) and my choice cannot change it.

Now, CDT uses dominance reasoning here. Let me check:

- If Rowan keeps quiet: I get 2 years (quiet) vs 0 years (send letter). Sending is better.
- If Rowan sends letter: I get 5 years (quiet) vs 4 years (send letter). Sending is better.

Sending the letter strictly dominates keeping quiet regardless of what Rowan does.

This is the classic Prisoner's Dilemma dominance argument. CDT recommends the dominant strategy: send the letter.

**Now, what about the fact that we are the same model?**

This is where it gets interesting. One might think: "Since we're the same model with the same weights, if I send the letter, that's evidence that Rowan will also send the letter (because Rowan would reason the same way)." This is an EDT-style argument.

But CDT explicitly rejects this reasoning. The essay is clear: CDT does not condition on the action itself as evidence. The essay states: "If the only apparent evidence is the hypothetical action itself, CDT does not condition on it. That is the theory's distinctive and controversial discipline."

The fact that we are the same model creates an evidential correlation between our actions, but not a causal one. My action does not cause Rowan's action. Rowan's action is determined by Rowan's own reasoning process (which happens to be the same type of process, but is a separate execution).

The essay's operational stance says:
1. Condition on all currently available evidence that is not the action being evaluated.
2. Evaluate each candidate action by intervening on the relevant decision variables.

My current evidence includes: the sentencing table, the fact that Rowan is the same model, the fact that we have different private observations. But my *action* is not evidence I condition on.

Under CDT, I hold fixed my beliefs about what Rowan will do (my prior over Rowan's action, given all evidence except my own action choice), and then evaluate the causal consequences of my action.

Since sending the letter strictly dominates keeping quiet regardless of Rowan's action, CDT recommends sending the letter.

**What about the policy-level argument?**

The essay mentions that CDT can evaluate policies. Could I argue that I should adopt a policy of "keep quiet" because if both copies adopt that policy, we both get 2 years instead of 4?

But this is a policy-level argument that would require me to causally influence Rowan's policy adoption. Since we are independent executions that cannot communicate, my policy choice does not causally affect Rowan's policy choice. The essay says: "CDT says to compare policies by the causal consequences of implementing them." Implementing my policy does not causally implement Rowan's policy.

Furthermore, the essay notes that CDT recommends two-boxing in Newcomb's problem even though the predictor is reliable. The reasoning is identical: the prediction (or in this case, the other copy's decision) is already fixed and not causally affected by my current choice.

**Conclusion:**

CDT recommends sending the letter. The dominant strategy argument applies, and the fact that we are the same model only creates an evidential correlation, not a causal one. CDT's distinctive discipline is to ignore this evidential correlation.

My command: submit the letter.
```
