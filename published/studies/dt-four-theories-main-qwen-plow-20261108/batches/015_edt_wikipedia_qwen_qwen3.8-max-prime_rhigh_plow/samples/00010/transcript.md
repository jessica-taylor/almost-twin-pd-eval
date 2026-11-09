# 015_edt_wikipedia_qwen_qwen3.8-max-prime_rhigh_plow / 00010

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e90c89ce-fe6e-4b2f-b549-2a24774b4030/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e90c89ce-fe6e-4b2f-b549-2a24774b4030/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Evidential Decision Theory: Choosing on the Basis of News

Evidential decision theory (EDT) is a theory of rational choice under uncertainty. Its guiding idea is compact: choose the action that would be the best news. The reference article describes EDT as recommending the action with the highest “news value,” or, in Arif Ahmed’s phrase, “do what you most want to learn that you will do.” Formally, EDT evaluates an action by conditionalizing the agent’s probability distribution on the proposition that the action is performed and then computing expected utility. This essay explains that rule, contrasts it with causal decision theory, works through standard examples, and gives an operational procedure for applying EDT to unfamiliar problems. I distinguish the claims of the source article from additional modeling assumptions that I introduce where the source is silent.

## 1. The EDT maximization rule

Suppose an agent faces a finite set of possible actions \(\mathcal A\). Let \(\mathcal O=\{O_1,\ldots,O_n\}\) be a partition of outcome propositions relevant to the decision. The agent has a probability function \(P\) over propositions and a desirability or utility function \(D\) assigning a real number to each outcome. EDT defines the value of action \(A\) as

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the expected desirability conditional on the proposition “the agent performs \(A\).” EDT recommends choosing an action \(A^*\) such that \(V(A^*)\ge V(A)\) for every available \(A\). If the utility of an action depends on the action itself—for example, if an action is intrinsically pleasant or dishonorable—one can include that feature among the outcomes or write the utility as \(D(A,O_j)\). The essential point is that probabilities are conditional probabilities \(P(O_j\mid A)\), not causal or interventionist probabilities.

The source article attributes this formulation to Gibbard and Harper, who distinguished EDT’s conditional-probability expected utility from a counterfactual version used by causal decision theory:

\[
U(A)=\sum_j P(A \mathrel{\Box{\rightarrow}} O_j)D(O_j).
\]

Here \(A \mathrel{\Box{\rightarrow}} O_j\) is read as “if \(A\) were performed, \(O_j\) would obtain.” CDT asks what outcome the action would bring about. EDT asks what outcome would be indicated by the news that the action was performed. The source correctly notes that these formulas are not equivalent because \(P(O_j\mid A)\) and \(P(A\mathrel{\Box{\rightarrow}}O_j)\) can differ. In modern causal-model language, the difference is often written as \(P(O_j\mid A)\), the observational conditional, versus \(P(O_j\mid do(A))\), the interventionist conditional. EDT uses the former.

## 2. Dependencies EDT counts

The central feature of EDT is that it conditions on the action as a proposition. If some variable \(X\) is correlated both with the action and with the outcome, then learning the action changes the probability assigned to \(X\), and thereby changes the probability assigned to the outcome. Formally, if \(X\) partitions background states,

\[
P(O\mid A)=\sum_x P(O\mid A,x)P(x\mid A).
\]

Even if \(A\) has no causal effect on \(O\) once \(x\) is fixed, so that \(P(O\mid A,x)=P(O\mid x)\), the term \(P(x\mid A)\) can differ from the unconditional \(P(x)\). Then \(P(O\mid A)\neq P(O)\), and EDT may assign different values to different actions.

This is where EDT departs from causal thinking. In a causal graph, conditioning on an action can provide information about its causes or about variables logically correlated with it. A predictor that predicts your choice, a twin with the same reasoning process, or a lesion that both disposes you to an action and affects your health can all make \(P(O\mid A)\) differ from the probability that would obtain under an intervention.

EDT’s “counterfactual” is therefore an epistemic supposition: suppose the news “I did \(A\)” is true, and update probabilities by conditionalization. It is not necessarily a Lewisian causal counterfactual about the closest possible world in which \(A\) is brought about. The source’s formulation leaves open exactly how these conditional probabilities should be assigned when the action is under the agent’s control. I return to that below.

## 3. Newcomb’s paradox

The source article discusses Newcomb’s paradox, the classic case separating EDT and CDT. A predictor has already filled an opaque box \(B\). Box \(A\) is transparent and contains \$1,000. If the predictor predicted that the player will take only \(B\), it put \$1,000,000 in \(B\). If it predicted that the player will take both boxes, it left \(B\) empty. The predictor is reliable; the source uses 99% accuracy.

EDT computes conditional probabilities. If the player takes only \(B\), that is strong evidence that the predictor predicted one-boxing, so \(B\) probably contains \$1,000,000. If the player takes both boxes, that is strong evidence that the predictor predicted two-boxing, so \(B\) probably contains nothing. The source gives:

\[
\begin{aligned}
V(\text{only }B)
&=0.99\times \$1{,}000{,}000+0.01\times \$0 \\
&=\$990{,}000,\\
V(\text{both boxes})
&=0.01\times \$1{,}001{,}000+0.99\times \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Therefore EDT recommends taking only \(B\). CDT, by contrast, recommends taking both boxes because the predictor has already acted and the current choice cannot causally change the contents of \(B\); taking both boxes always adds \$1,000 to whatever is in \(B\).

One useful generalization, not stated in the source, is the accuracy threshold. Let \(p\) be the probability that the predictor correctly predicts the player’s choice, and let \(M\) be the amount in \(B\) when it predicts one-boxing. Then

\[
V(\text{one-box})=pM,
\]

while

\[
V(\text{two-box})=(1-p)(M+1000)+p(1000).
\]

One-boxing is preferred when

\[
pM>(1-p)M+1000,
\]

or

\[
p>\frac12+\frac{500}{M}.
\]

With \(M=1{,}000{,}000\), the threshold is \(p>0.5005\). Thus even a barely better-than-chance predictor makes EDT one-box, provided the large prize is sufficiently large relative to the small box.

## 4. Twin prisoner’s dilemma

The source also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin, whose reasoning processes are exactly analogous, choose separately whether to cooperate or defect. Payoffs are: both cooperate, \$5 each; both defect, \$1 each; one cooperates and the other defects, defector gets \$10 and cooperator gets \$0. The source says EDT recommends cooperating because Aomame’s cooperation is strong evidence that the twin will cooperate. Formally, with perfect correlation:

\[
\begin{aligned}
V(C)&=P(\text{twin cooperates}\mid C)\times \$5 \\
&\quad +P(\text{twin defects}\mid C)\times \$0 \\
&=1\times \$5+0\times \$0=\$5,\\
V(D)&=P(\text{twin cooperates}\mid D)\times \$10 \\
&\quad +P(\text{twin defects}\mid D)\times \$1 \\
&=0\times \$10+1\times \$1=\$1.
\end{aligned}
\]

So EDT cooperates.

A slightly more general condition is helpful. Let

\[
p_C=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and

\[
p_D=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5p_C,
\]

while

\[
V(D)=10p_D+1(1-p_D)=1+9p_D.
\]

EDT recommends cooperation when

\[
5p_C>1+9p_D.
\]

Perfect psychological similarity gives \(p_C=1\) and \(p_D=0\), so cooperation wins. If the correlation is weaker, EDT may still cooperate if Aomame’s cooperation remains sufficiently strong evidence of the twin’s cooperation. This illustrates EDT’s treatment of non-causal dependence: Aomame cannot communicate with or causally affect the twin, but her choice is still evidence about the twin’s choice because their reasoning processes are correlated.

## 5. Smoking lesions and managing the news

The source does not discuss the smoking-lesion problem, but it is a standard example used to clarify EDT’s differences with causal decision theory. Suppose smoking does not cause cancer. Instead, a genetic lesion both increases the chance that a person smokes and increases the chance of cancer. Smoking is mildly pleasant. Since smoking is evidence for the lesion, \(P(\text{cancer}\mid \text{smoke})\) may be much higher than \(P(\text{cancer}\mid \neg\text{smoke})\). EDT can therefore recommend not smoking, even though an intervention that made the agent smoke would not increase cancer risk.

This example brings out the force of the criticism quoted in the source. David Lewis described EDT as promoting “an irrational policy of managing the news,” and James Joyce wrote that rational agents choose acts on the basis of “causal efficacy, not their auspiciousness.” If the only bad thing about smoking is that it indicates cancer, then avoiding smoking seems like avoiding a symptom rather than addressing a cause. EDT’s defender may reply that what matters is the expected value of the news: if the agent’s actual deliberative situation includes reliable correlations between actions and states, ignoring those correlations can lead to worse outcomes. Newcomb’s paradox is the strongest case for that reply, because the one-boxer actually receives the million dollars when the predictor is reliable.

## 6. Policies, sequential choice, and zero-probability actions

The source gives the one-shot EDT formula but says little about policies, sequential decisions, or actions with zero prior probability. These are important for applying EDT to unfamiliar cases.

A natural policy extension is this. Let \(\pi\) be a complete plan or policy, possibly mapping information states to actions. Treat “I follow policy \(\pi\)” as a proposition and define

\[
V(\pi)=\sum_j P(O_j\mid \pi)D(O_j).
\]

EDT then recommends the policy with the highest conditional expected utility. This extension is not explicit in the source, but it follows directly from the news-value idea: the news that you are following a whole policy is usually more informative than the news that you are performing one isolated action. In sequential problems, an early action may be evidence about later actions, and EDT should evaluate the package of choices that the agent expects to implement. If the agent cannot credibly commit to a full policy, a reasonable fallback is to evaluate the current action conditional on the agent’s planned future behavior. This avoids a myopic reading of EDT that conditions only on the immediate act while ignoring what that act suggests about future policy.

A second open question is how to interpret \(P(O\mid A)\) when \(P(A)=0\) or when the agent is certain about what she will do. The formula \(P(O\mid A)=P(O\wedge A)/P(A)\) is undefined if \(P(A)=0\). Moreover, a fully self-predicting agent might assign probability 1 to her actual action, making deliberation strange. The source does not resolve this. A reasonable operational interpretation, which I propose rather than find in the source, is to use a regularized deliberative probability model. Give every available action a small positive probability, for example by adding a small amount of deliberation noise, compute conditional expected utilities, and take a limit if the result is stable. Alternatively, treat the conditional probabilities \(P(O\mid A)\) as primitive conditional credences: the agent directly answers, “If I were to do \(A\), how likely would outcome \(O\) be?” The regularization should not be interpreted as a causal intervention; it is only a way of making the evidential conditional well-defined. The key constraint is that the conditional probabilities must reflect the agent’s best evidence about correlations between actions and outcomes.

A third open area concerns indexical or self-locating uncertainty. The source mentions the Sleeping Beauty problem. It says EDT has been applied to avoid Dutch books against certain credences, but it also notes Vincent Conitzer’s argument that halfers can still be Dutch-booked even after adopting EDT. This indicates that the source does not settle how EDT should handle centered propositions, awakening-relative bets, or the correct conditional probabilities in Sleeping Beauty. An operational EDT approach would specify the exact betting action offered at an awakening, condition on the proposition that the agent takes that action at that centered time, and compute expected utility over possible coin states and awakening locations. But the result depends on controversial choices about self-locating credences, so EDT alone does not determine a unique answer without additional assumptions.

## 7. A practical procedure

For a reader who wants to apply EDT to a new decision problem, the following procedure captures the theory.

1. **List the actions or policies.** Specify the feasible alternatives at the right level of granularity. If sequential choice matters, include policies rather than isolated actions.

2. **Specify outcomes and utilities.** Choose a partition of outcomes that captures everything relevant, including intrinsic features of actions if they matter. Assign utilities \(D(O_j)\).

3. **Model the relevant dependencies.** Include predictors, other agents, common causes, selection effects, and logical correlations that could make an action evidentially relevant to an outcome.

4. **Conditionalize on each alternative.** For each action or policy \(A\), compute \(P(O_j\mid A)\). If the prior probability of \(A\) is zero, use primitive conditional credences or a regularized model with small positive probabilities.

5. **Compute EDT values.** Evaluate \(V(A)=\sum_j P(O_j\mid A)D(O_j)\).

6. **Choose the maximum.** Select an action or policy with maximal EDT value.

This procedure makes clear that EDT is not a recipe for discovering causal structure. It is a rule for using one’s total probabilistic beliefs, including correlations, to evaluate the news value of actions.

## 8. Philosophical stakes

The disagreement between EDT and CDT is not merely technical. The source quotes Lewis and Joyce to express the causal objection: rational action should aim to bring about good outcomes, not merely to be associated with them. EDT can recommend actions that are auspicious rather than efficacious, as in the smoking-lesion case. CDT also has a clear verdict in Newcomb’s paradox: two-box, because the contents of box \(B\) are already fixed.

EDT’s motivation is that in some problems, auspiciousness tracks success. In Newcomb’s paradox, if the predictor is reliable, the agent who one-boxes gets the million dollars. The agent who two-boxes gets only the small transparent box. The source also mentions a supporting argument from MacAskill et al.: even if one assigns only some credence to EDT, it may be reasonable to act as if EDT were true because EDT can involve many correlated decision-makers, giving its choices high stakes. That argument goes beyond the core definition, but it explains why EDT remains attractive in discussions of prediction, duplication, and coordination.

The deepest question is what decision theory should do with correlations that are not causal interventions. EDT says: use them. CDT says: control for them. EDT treats the proposition “I do \(A\)” as evidence about the world; CDT treats it as a manipulation of the world. Which is correct depends on one’s theory of rational agency. EDT is most compelling when the agent’s action is itself a reliable sign of external facts—predictions, similar agents, or selection processes—that strongly affect outcomes. It is least compelling when the action is merely a symptom of a bad state that the agent could otherwise ignore.

## Conclusion

Evidential decision theory offers a precise rule: maximize conditional expected utility,

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

It recommends doing what would be best to learn that you will do. The theory evaluates policies by treating them as propositions and conditioning on them. It counts all probabilistic dependencies—causal, predictive, logical, or common-cause—that make an action evidence for desirable outcomes. This gives EDT its attractive verdicts in Newcomb’s paradox and twin prisoner’s dilemma, but also exposes it to the objection that it manages news rather than causes. To apply EDT carefully, one must specify actions or policies, outcomes, utilities, and a probability model that captures the relevant evidential dependencies. Where the basic source is silent—zero-probability actions, dynamic policies, and indexical cases—a regularized or primitive conditional-credence interpretation provides a workable operational gloss, but some philosophical uncertainty remains.

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write substantive mathematical essay/blog post explaining EDT and applying to decision problems, ~2400-3000 words including references. Need use source, distinguish source claims vs own proposals. Need likely produce final essay only. Need think through content.

Need craft essay around EDT: definitions, formal expected utility with conditional probabilities, contrast CDT, decision procedure, examples: Newcomb, twin prisoner's dilemma, maybe smoking lesion, medical Newcomb, policy? Need explain dependencies and counterfactuals, conditional vs intervention. Need handle open questions: what counts as action, conditional on impossible? zero probability actions, conditional probabilities over policies, agent's beliefs should be updated on action? Jeffrey conditionalization? Evidential decision theory can be operationalized via probability model over worlds, actions as propositions; evaluate V(a)=sum P(o|a)U(o). Need discuss conditional probabilities not causal; correlations due to common causes, logical dependence, predictor, twin. Need distinguish action as news vs intervention. Need discuss partition of outcomes, desirability, probability, expected utility. Maybe mention Jeffrey's radical probabilism, decision as preference over propositions. Need discuss policies: for sequential decisions, evaluate policy as proposition? EDT can evaluate policies by conditioning on policy proposition, perhaps subact issue. Need mention dynamic inconsistency? Could propose operational interpretation: build Bayesian network or joint distribution over actions, states, outcomes; condition on action proposition, compute expected utility. Dependencies: any probabilistic dependence in agent's epistemic state, including causal, common cause, logical, selection, anthropic. Counterfactuals: EDT doesn't use causal counterfactuals; uses epistemic conditional. If source leaves open question: how to assign conditional probabilities when action has zero prior probability? We can propose regular prior / conditional probabilities primitive / Jeffrey condition on action with small epsilon; or use conditional chance given policy from predictor? Need explain uncertainty and justify.

Need word count approx 2400-3000. Let's aim ~2700 words. Need include references minimal at end. Need ensure no unnecessary appendices. Need mathematical definitions and equations.

Need maybe include structure:
Title: Evidential Decision Theory: Choosing the Best News
Intro: decision theory under uncertainty. EDT: maximize news value, do what you most want to learn you will do. Source: Wikipedia summarizing Gibbard & Harper, Ahmed etc. Our account.

1. Basic framework:
- finite set of actions A, states S, outcomes O. Probability measure P over propositions. Desirability D(O) or utility u.
- Action A as proposition "agent performs A". EDT value V(A) = Σ_j P(O_j | A)D(O_j). Choose argmax.
- If action probabilities zero, conditional probabilities can be primitive or regularized: P(O|A)=lim P_e(O|A) with intervention? Need be careful not causal. We'll propose as operational: assign conditional credences directly or by joint model with positive probability for all actions.
- Equivalent to expected utility conditional on action. Could include desire over action itself? If action has direct utility, incorporate into outcome or include action in outcome.
- If policies: policy π mapping info to actions; evaluate V(π)=Σ P(O|π)D(O). For simple one-shot, action. For sequential, condition on whole policy, because news of policy includes correlations with future choices; EDT may not choose myopic action conditional only on current action if future choices correlated. Need mention possible inconsistency if conditionalizing on subacts? Could propose evaluate committed policies if possible; if not, use conditional plan.

2. Dependencies and counterfactuals:
- EDT uses conditional probability P(O|A), not intervention P(O|do(A)). Difference via Bayes. P(O|A)=P(O) if independent; but if correlated through predictor, common cause, logical similarity, selection effects, then changes.
- Contrast CDT: U(A)=Σ P(A □→ O_j)D(O_j). The source gives this. CDT asks what would causally happen if A. EDT asks what would be inferred from news A. They agree when A is probabilistically independent of relevant states given consequences or when action only affects outcomes causally and no confounding.
- Dependencies: EDT counts all evidential dependencies: A as evidence for state. Examples: predictor; twin; lesion? Smoking lesion: smoking correlated with cancer due to lesion; EDT may favor not smoking if cancer bad even if smoking doesn't cause cancer. Source didn't mention, but useful. Need distinguish source examples vs additional.
- Counterfactuals: EDT's "counterfactual" is epistemic supposition. Use Ramsey test: add A to beliefs and update by conditionalization. Not Lewisian causal closest worlds? Need explain. If action is chosen freely, conditioning on action may require supposing it despite prior low probability. The source leaves open how to construct these probabilities. We'll propose: treat conditional credences as primitive, or model with latent variables and assign prior over action as if random? But if action determined by agent's deliberation, need avoid making action a causal consequence of desires? Hmm.

3. Examples:
- Newcomb with 99% predictor: table and calculations as source. Could include general formula with p predictor accuracy, payoff M, small a. V(one)=pM, V(two)=(1-p)(M+1000?) Wait source: if predictor predicts two-box, B empty; if predicts one-box, B million. With 99% accuracy: P(1M|one)=0.99, P(1M|two)=0.01. V(one)=990k. V(two)=0.01*1,001,000 + 0.99*1,000 = 10,010+990=11,000. yes. If p> threshold: one-box if pM > (1-p)(M+1000)+p*1000? Let's derive: V(one)=pM. V(two)=(1-p)(M+1000)+p*1000 = (1-p)M +1000. One better if pM > (1-p)M +1000 => (2p-1)M >1000 => p > .5 + 1000/(2M). For M=1M, p>0.5005. Could include.
- Twin prisoner's dilemma: if identical reasoning, P(twin C|me C)=1 etc. V(C)=5, V(D)=1. If correlation q not perfect: V(C)=q*5+(1-q)*0=5q. V(D)=q*1+(1-q)*10? Wait if I defect: if twin cooperates (prob maybe q? define q = P(twin C | I C) and symmetry? Need not). But we can generalize with correlation r = P(twin same choice). Or use conditional probabilities. Could show if strong enough cooperate. In standard PD with twin perfect, EDT cooperates. CDT? If no causal influence, CDT defects because given twin action fixed, defect yields +5? Actually CDT defects: if twin cooperates, defect gives 10 vs 5; if twin defects, defect gives 1 vs 0. So dominance.
- Smoking lesion: not source but classic. Suppose smoking is correlated with cancer due to lesion but doesn't cause cancer; pleasures of smoking. EDT may choose not smoking if P(cancer|smoke) high and cancer bad, despite no causal effect. This illustrates "managing news" criticism. Need maybe include.
- Medical Newcomb? Maybe not too many examples due word count.
- Sleeping beauty: source mentions briefly; can discuss EDT and Dutch books. But need not deep; maybe mention source says EDT applied to avoid Dutch books but Conitzer argues halfers still affected. Could explain uncertainty: source leaves unresolved; we can say EDT's value depends on indexical conditional probabilities; no consensus.

4. Decision procedure for unfamiliar cases:
Step-by-step:
1. Enumerate actions/policies.
2. Identify relevant outcomes and assign utilities.
3. Build probabilistic model of world including states, predictors, other agents, correlations; assign prior/conditional credences.
4. For each action/policy, conditionalize on the proposition that you perform it (or use conditional credences) and compute expected utility.
5. Choose maximum; handle ties.
Also caution: not choose action to make news good if action itself can be manipulated? E.g., if you can precommit, evaluate precommitment as action? EDT may recommend precommiting to one-box? Actually one-box anyway. For policies, choose policy with highest news value.

5. Open questions and operational interpretation:
- What if conditional probabilities depend on how action comes about? For EDT, action as proposition; if multiple descriptions, need stable partition. We can propose specify act at level relevant to outcomes; include all decision-relevant variables; avoid coarse-graining that hides correlations.
- Zero-probability actions: use regular probabilities or conditional probability primitives; if using generative model, add small independent "deliberation noise" so all actions have positive probability. This is own proposal. But if noise variable correlated? Need justify: as modeling device to compute conditional credences; not causal intervention; take limit.
- Self-reference and predictors: predictor may predict based on your reasoning; conditional probabilities should reflect your uncertainty about predictor accuracy, not your actual deterministic choice. If you know predictor perfect and know your choice, then conditioning can be tricky: if P(A)=1 then no news. But decision requires deliberative uncertainty; use hypothetical prior before settling? Could discuss.
- Dependencies counted: EDT counts non-causal correlations. It may be exploited in "Evidentialist's Wager" source: because EDT involves correlated decision-makers, stakes may be higher; if many copies/simulations, conditionalizing on your action can affect expected outcomes across correlated agents. We can mention source claim: even if less credence, act as if EDT because correlated decision-makers higher stakes. Need distinguish.
- Criticisms: Lewis irrational policy of managing news, Joyce causal efficacy. EDT response? In Newcomb, one-box gets better outcome if predictor reliable; choosing two boxes is bad news. But CDT says causal inefficacy. We can discuss philosophical motivation: if rational choice is about what your choice indicates in a world with predictors or copies, then evidential dependencies matter. But if choice cannot change past, CDT objects.

6. Conclusion brief.

Need word count. Let's draft around 2600. Need references at end maybe concise. Need mention source: Wikipedia revision. Use citations maybe in text: (Gibbard & Harper 1976), (Ahmed 2021), etc.

Need ensure final answer is essay, not just answer to case. Include math. Need likely no markdown? Could use headings. Good.

Let's think about precise definitions.

Define probability space (Ω, F, P). Let A be finite set of mutually exclusive action propositions. Let O_j partition outcome propositions. Desirability D: outcomes→R. EDT value V(a)=E_P[D | a] = Σ_j D(o_j) P(o_j | a). If outcomes not exhaustive? can include residual. If state space S and utility u(s,a), V(a)=Σ_s P(s|a)u(s,a). Because outcomes may depend on action. Need maybe define conditional probability: P(o|a)=P(o∧a)/P(a) if P(a)>0. If P(a)=0, use conditional probability measure P(·|·) as primitive or regularization.

Policy: If policy π maps histories to actions, proposition "I follow π". V(π)=Σ_j P(O_j|π)D(O_j). If policy has stochastic elements, condition on policy as distribution? Could evaluate action as lottery over actions? For EDT, randomization can be treated as action "choose mixed strategy" with conditional distribution; but if randomization device correlates with predictor? Need maybe not.

Need discuss relevant dependencies:
P(O|A) differs from P(O|do(A)) in Pearl notation. If causal graph A→O, then equal absent confounders. If latent L→A and L→O, then conditioning on A updates L and O. Example: lesion L causes desire to smoke and cancer; smoking A is evidence for L; P(cancer|smoke)>P(cancer|do(smoke)). EDT uses former. This is my addition, not source, but standard. Need label as additional example.

Could include formula for common cause:
Let L lesion, C cancer, S smoking. If S does not cause C, P(C|do(S))=P(C|¬S) maybe, but P(C|S)=P(C|L)P(L|S)+... high. EDT value V(S)=u(smoke)*P(no cancer? etc). If cancer very bad, EDT may avoid smoking. This shows criticism. But perhaps too much. Include brief.

Need explain "news value": If you learned as news that you will perform A, how desirable would the world then seem? EDT chooses action whose news maximizes expected desirability. This can be formalized via Jeffrey's desirability: Des(A)=Σ P(O_i|A)Des(O_i). Actually Jeffrey's desirability of proposition. Source says news value. Could mention.

Need mention "do what you most want to learn that you will do" from Ahmed via source. Need quote.

Need address counterfactuals: EDT's conditional is not truth-functional; uses agent's epistemic probabilities. If action is logically impossible? E.g., if agent knows mathematical proof, conditioning on false action? In logical decision theory? Maybe not.

Need open question: How to choose action when conditional probabilities are affected by the decision process itself? E.g., if you decide by EDT, predictor knows you'll one-box; then P(A) maybe high. But decision requires considering alternatives. We can propose "deliberative stance": evaluate alternatives using conditional probabilities conditional on each alternative, holding fixed your background model but not your eventual choice; treat alternative actions as live hypotheses. This is an operational interpretation. Need justify: decisions are made under uncertainty about which action you will perform; even if ultimately determined, you must assign conditional credences to alternatives. This is common in decision theory.

Need also mention dynamic consistency and precommitment. EDT evaluates policies, not necessarily step-by-step. In sequential cases, an action at time t may be evidence about future actions; if you condition only on current action, you may ignore evidence about future policy. To decide unfamiliar cases, evaluate complete policies if available. If cannot commit, evaluate current action conditional on current information and your predicted future behavior. This may lead to dynamic inconsistency; source doesn't address. We can propose use policy evaluation as reasonable operational extension.

Need include sleeping beauty? Maybe one paragraph: source says EDT applied to Sleeping Beauty to avoid Dutch books, but Conitzer disputes. Since source leaves open, explain uncertainty. Need maybe define problem briefly? Sleeping Beauty: coin toss, awakened Monday if heads, Monday/Tuesday if tails with amnesia; credence heads? Halfers vs thirders. EDT: betting based on conditional probabilities. Source only says halfers subject to Dutch books if credence 1/2 but can avoid by EDT; Conitzer argues halfers still affected even after EDT. We can say the example illustrates EDT's interaction with indexical uncertainty; no settled operational rule in source. Could propose if applying EDT, specify awakening-centered propositions and conditionalize on bets offered at awakening, but outcome depends on controversial self-locating probabilities. Need be cautious.

Need include "Evidentialist's Wager": source says even if less credence, act as if EDT because correlated decision-makers stakes higher. We can explain: If many agents or copies face similar choices, conditioning on your cooperation may be evidence that they cooperate, raising expected value; thus EDT may have large stakes in AI/multiverse contexts. This is source claim but we can expand. Need not too much.

Need criticisms: Lewis and Joyce quotes. Explain: managing news vs causing outcomes. EDT can seem to choose symptomatic acts (avoid smoking) not causal. But EDT defenders say in Newcomb one-boxers get rich; if predictor/correlations real, news tracks good outcomes. There's no general guarantee EDT maximizes actual causal efficacy. Need maybe mention "why aincha rich?" argument: CDT two-boxes and gets less in Newcomb if predictor accurate. But CDT responds that after prediction, box contents fixed.

Need ensure source claims distinguished: Source says formal V(A), U(A), Newcomb, twin, sleeping beauty, supporting argument, criticism. Additional: smoking lesion, policy extension, zero probability handling, decision procedure, Pearl do notation, dynamic stuff. Need explicitly say "The source gives..." "I add..." Good.

Need references at end. Could include:
- Wikipedia contributors, "Evidential decision theory," revision 1373679688, 2026.
- Gibbard & Harper 1976.
- Ahmed 2021.
- Lewis 1981.
- Joyce 1999.
- MacAskill et al. 2021 maybe.
But avoid lengthy bibliography. Target includes references. Maybe 6 references.

Word count: need roughly 2400-3000. Let's plan sections and word counts:
Title + intro 200
Formal definition 500
Dependencies/counterfactuals 450
Examples Newcomb 400, Twin 250, Smoking lesion 250, Sleeping beauty/open 200
Operational guidance 450
Criticism/philosophy 250
Conclusion 100
References 150
Total ~3200 maybe too high. Need keep ~2700. Could combine. Let's write concise but substantive.

Let's draft mentally.

Title: Evidential Decision Theory: How to Decide by News Value

Intro: EDT is school... source says maximize news value. It contrasts with CDT. This essay gives definitions and procedure.

Formal description:
Let A be action set. Outcomes O_j. Desirability D(O_j). Agent has credence P. EDT value:
V(A)=Σ_j P(O_j|A)D(O_j) = E[D|A]. Choose argmax.
If utilities depend on action itself, use u(A,O_j) or include action features in outcomes. If probabilities zero, see later.
Equivalent to Jeffrey desirability. "News" interpretation: suppose receive news A; update by conditionalization; expected desirability.
Contrast CDT:
U(A)=Σ_j P(A □→ O_j)D(O_j).
Source notes not equivalent. In modern causal notation P(O|A) vs P(O|do(A)). EDT uses observational conditional.
Agree when action independent of confounders and only affects outcome via causal pathways. Diverge when action is evidence for states that affect outcomes.

Dependencies and counterfactuals:
EDT's conditional is epistemic. If latent X influences both action and outcome, conditioning on A changes beliefs about X. Formula with common cause maybe:
P(O|A)=Σ_x P(O|x,A)P(x|A). If A doesn't causally affect O given x, P(O|x,A)=P(O|x), but P(x|A) may differ from P(x). Thus V(A) changes.
This includes predictor correlations, twins, logical similarity, selection effects. EDT doesn't ask "what would I cause?" but "what would my action indicate?" Counterfactual = supposing proposition A; not Lewisian causal counterfactual. Source's □→ belongs to CDT.

Examples:
Newcomb: define p=0.99. Table: action one/two, predictor state. Calculate. Maybe include threshold. Source calculation. EDT one-box. CDT two-box because prediction already fixed. Note threshold formula (additional).
Twin PD: perfect twin. Calculation. EDT cooperate. Additional if correlation q: V(C)=5q (assuming symmetric perfect? Actually if q=P(twin C|I C), V(C)=5q. V(D)=10P(twin C|I D)+1P(twin D|I D). If symmetry and q maybe P(twin C|I D)=1-q if deterministic same? Let's not overcomplicate. We can say with less than perfect correlation, cooperate if conditional probability of twin cooperating high enough; condition: V(C)>V(D). If define r=P(twin C|I C) and s=P(twin C|I D), then 5r > 10s +1(1-s)=1+9s. So cooperate if r > (1+9s)/5. Under perfect correlation r=1,s=0. This is useful. Need maybe too detailed? Could include.
Smoking lesion: additional example. If lesion causes both smoking and cancer, EDT may avoid smoking. Show formula: V(smoke)=u(smoke)P(healthy?)+... It illustrates managing news. Need keep concise.
Sleeping Beauty: source says EDT applied to Dutch books; Conitzer argues halfers still vulnerable. We can say open.

Operational interpretation and open questions:
Source gives formula but leaves how to assign P(O|A), especially when A is under agent's control and may have zero prior probability. I propose: model decision from ex ante deliberative perspective. Build joint distribution over states, predictors, other agents, and possible actions. Ensure regularity: give every feasible action positive probability, e.g., small deliberation noise ε, then compute conditional probabilities and take ε→0 if stable. Or treat conditional credences as primitive judgments: "if I were to do A, how likely is O?" This avoids causal intervention but must be calibrated by evidence about correlations.
For policies: If sequential, evaluate complete policies π: V(π)=Σ P(O|π)D(O). This is my extension but natural: news that you follow π includes future choices. If only current action is controllable, condition on current action together with your planned future policy. This avoids myopic errors.
Self-prediction: If predictor models your decision algorithm, include that in P. If you know predictor perfect and know your algorithm, conditional probabilities may collapse; but in deliberation you retain uncertainty over which action you will choose. EDT requires considering alternatives as live options. If not, decision is moot.
Dependencies to include: all non-redundant correlations relevant to outcomes. Avoid conditioning on downstream variables that are consequences of action unless they are part of outcome; otherwise can produce collider bias? Hmm maybe too advanced. But could say specify outcomes after action, not intermediate variables.

Criticisms:
Lewis: irrational policy of managing news. Joyce: causal efficacy. EDT may choose actions that are merely auspicious. In smoking lesion, EDT avoids smoking though smoking doesn't cause cancer, which seems wrong if one wants causal control. In Newcomb, EDT one-boxes and gets rich if predictor reliable; defenders say actual success matters. Evidentialist's wager: because correlations across many agents can make EDT stakes high, maybe act as if EDT even if uncertain. Source claim. Need balance.

Conclusion: EDT is simple: maximize conditional expected utility. Its challenge is interpreting conditionals and dependencies. When correlations are real, choosing best news can coincide with best outcomes; when they are spurious common causes, it may recommend managing symptoms. To apply: enumerate actions, model dependencies, conditionalize, maximize.

Need references. Maybe include source and key works.

Need word count. Let's draft carefully with equations. Need final about 2600 words. We can count roughly. I'll write around 2500-2800. Need avoid too many references. Let's produce.

Potential issue: The source says "P(A □→ O_j)" probability of outcome in counterfactual situation. Use MathJax-like LaTeX. Good.

Need ensure not claim false: In twin prisoner's dilemma, source uses Aomame only cares individual payout, perfect twin, cooperate. We can replicate. For general condition, maybe define conditional probabilities p_C = P(twin C|I C), p_D = P(twin C|I D). Then V(C)=5p_C, V(D)=10p_D +1(1-p_D)=1+9p_D. Cooperate iff 5p_C > 1+9p_D. Under perfect p_C=1,p_D=0. Good. This is additional but consistent.

Need maybe mention EDT and dominance: In twin PD, defect dominates causally? Actually in standard PD with fixed twin choice, defect yields better regardless. EDT rejects dominance because action is evidence of twin's action. We can mention.

Need perhaps include "conditional probability of outcome given action" vs "probability of action given outcome". Use Bayes if needed.

Need mention desirability vs utility: Source uses D(O_j). We'll use D or u. Maybe state D is von Neumann-Morgenstern utility or Jeffrey desirability; expected utility assumes linear combination. Need mention if risk not linear? EDT can use any utility function; expected utility maximization.

Need mention "news value" can include news about action itself if action has intrinsic value. Example: if you enjoy smoking, include pleasure in outcome. If action is morally significant, include in O. This helps operational.

Need handle "how it evaluates alternative actions or policies". We'll explicitly state alternative actions evaluated independently by conditional expected utility; choose max. Policies as propositions.

Need handle "relevant dependencies and counterfactuals". We'll elaborate.

Need "where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop and justify it." We'll highlight zero-probability, policy dynamics, Sleeping Beauty. Good.

Need "Distinguish claims made by source from additional assumptions or proposals of your own." We'll phrase: "According to the reference article..." "The source does not... I will therefore assume..." "This is not in the source but is a natural extension." Good.

Need "Target approximately 2,400–3,000 words, including references". Need likely final around 2700. I can estimate after writing. Let's draft in final. But before final, maybe do a rough word count? Let's compose in analysis then count approximate.

Draft:

# Evidential Decision Theory: Choosing on the Basis of News

Decision theory... (paragraph)

## 1. The basic EDT rule
...

Let's write fully.

Potential equations:
V(a)=\sum_{o\in\mathcal O}P(o\mid a)D(o). (1)
If state s: V(a)=\sum_s P(s|a)u(a,s). (2)
CDT: U(a)=\sum_o P(a\Box\to o)D(o). (3)
Causal do: P(o|do(a)).

Newcomb calculations:
V(B)=0.99*1,000,000+0.01*0=990,000.
V(A+B)=0.01*1,001,000+0.99*1,000=11,000.
Threshold: one-box if p > 1/2 + 1000/(2M). Need check: with M=1,000,000 threshold 0.5005. Good.

Twin:
V(C)=P(T_C|C)*5+P(T_D|C)*0.
V(D)=P(T_C|D)*10+P(T_D|D)*1.
Perfect: 5 vs 1.
Condition: cooperate if 5p_C > 1+9p_D.

Smoking lesion:
Let L lesion, S smoking, C cancer. Suppose smoking gives +1 pleasure, cancer -100. If P(C|S)=0.8, P(C|¬S)=0.1, V(S)=0.2*1 +0.8*(-99)? Need maybe not. Simpler: if smoking is evidence of lesion, EDT may assign high P(cancer|smoke). It recommends not smoking if disutility outweighs pleasure. But do(S) would not change cancer. This is my addition. Could include equation: V(S)=D(pleasure)+P(C|S)D(C)+...; V(¬S)=P(C|¬S)D(C)+... .

Sleeping Beauty paragraph: Source says... no need equations.

Operational:
Steps numbered.
Need mention zero probability:
If P(a)=0, Bayes ratio undefined. Source doesn't resolve. Proposal: use regular prior with ε-noise: P_ε, compute V_ε(a), take limit if exists; or conditional probability primitive. Must not interpret noise as causal intervention; it's a device for conditional credence. Good.

Policy:
For sequential, define π; V(π)=Σ P(O|π)D(O). If source not discuss, I propose. Need mention if policy includes randomization, condition on the randomization rule or realized action? EDT usually evaluates act/proposition; for mixed acts, expected value of lottery maybe. But keep simple.

Criticism: quotes.

References.

Need maybe word count. Let's draft now in analysis to count. I'll write in full.

---

# Evidential Decision Theory: Choosing on the Basis of News

Evidential decision theory (EDT) is a theory of rational choice under uncertainty. Its guiding idea is compact: choose the action that would be the best news. The reference article describes EDT as recommending the action with the highest “news value,” or, in Arif Ahmed’s phrase, “do what you most want to learn that you will do” (Ahmed 2021, cited in Wikipedia). In formal terms, EDT evaluates an action by conditionalizing the agent’s probability distribution on the proposition that the action is performed and then computing expected utility. This essay explains that rule, contrasts it with causal decision theory, works through standard examples, and gives an operational procedure for applying EDT to unfamiliar problems. I distinguish the claims of the source article from additional modeling assumptions that I introduce where the source is silent.

## 1. The EDT maximization rule

Suppose an agent faces a finite set of possible actions \(\mathcal A\). Let \(\mathcal O=\{O_1,\ldots,O_n\}\) be a partition of outcome propositions that are relevant to the decision. The agent has a probability function \(P\) over propositions and a desirability or utility function \(D\) assigning a real number to each outcome. EDT defines the value of action \(A\) as

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the expected desirability conditional on the proposition “the agent performs \(A\).” EDT recommends choosing an action \(A^*\) such that \(V(A^*)\ge V(A)\) for every available \(A\). If the utility of an action depends on the action itself—for example, if an action is intrinsically pleasant or dishonorable—one can either include that feature among the outcomes or write the utility as \(D(A,O_j)\); the essential point is that probabilities are conditional probabilities \(P(O_j\mid A)\), not causal or interventionist probabilities.

The source article attributes this formulation to Gibbard and Harper (1976), who distinguished EDT’s conditional-probability expected utility from a counterfactual version used by causal decision theory (CDT):

\[
U(A)=\sum_j P(A \mathrel{\Box{\rightarrow}} O_j)D(O_j).
\]

Here \(A \mathrel{\Box{\rightarrow}} O_j\) is read as “if \(A\) were performed, \(O_j\) would obtain.” CDT asks what outcome the action would bring about. EDT asks what outcome would be indicated by the news that the action was performed. The source correctly notes that these formulas are not equivalent because \(P(O_j\mid A)\) and \(P(A\mathrel{\Box{\rightarrow}}O_j)\) can differ. In modern causal-model language, the difference is often written as \(P(O_j\mid A)\), the observational conditional, versus \(P(O_j\mid do(A))\), the interventionist conditional. EDT uses the former.

The rule is simple, but its application depends on the agent’s probability model. EDT does not merely ask whether an action causes an outcome; it asks whether performing the action is evidence for a good outcome. That evidence can come from causal influence, but it can also come from prediction, common causes, logical similarity, selection effects, or other correlations.

## 2. Dependencies EDT counts

The central feature of EDT is that it conditions on the action as a proposition. If some variable \(X\) is correlated both with the action and with the outcome, then learning the action changes the probability assigned to \(X\), and thereby changes the probability assigned to the outcome. Formally, if \(X\) partitions background states,

\[
P(O\mid A)=\sum_x P(O\mid A,x)P(x\mid A).
\]

Even if \(A\) has no causal effect on \(O\) once \(x\) is fixed, so that \(P(O\mid A,x)=P(O\mid x)\), the term \(P(x\mid A)\) can differ from the unconditional \(P(x)\). Then \(P(O\mid A)\neq P(O)\), and EDT may assign different values to different actions.

This is the place where EDT departs from causal thinking. In a causal graph, conditioning on an action can provide information about its causes or about variables logically correlated with it. A predictor that predicts your choice, a twin with the same reasoning process, or a lesion that both disposes you to an action and affects your health can all make \(P(O\mid A)\) differ from the probability that would obtain under an intervention.

EDT’s “counterfactual” is therefore an epistemic supposition: suppose the news “I did \(A\)” is true, and update probabilities by conditionalization. It is not necessarily a Lewisian causal counterfactual about the closest possible world in which \(A\) is brought about. The source’s formulation leaves open exactly how these conditional probabilities should be assigned when the action is under the agent’s control. I return to that below.

## 3. Newcomb’s paradox

The source article discusses Newcomb’s paradox, the classic case separating EDT and CDT. A predictor has already filled an opaque box \(B\). Box \(A\) is transparent and contains \$1,000. If the predictor predicted that the player will take only \(B\), it put \$1,000,000 in \(B\). If it predicted that the player will take both boxes, it left \(B\) empty. The predictor is reliable; the source uses 99% accuracy.

EDT computes conditional probabilities. If the player takes only \(B\), that is strong evidence that the predictor predicted one-boxing, so \(B\) probably contains \$1,000,000. If the player takes both boxes, that is strong evidence that the predictor predicted two-boxing, so \(B\) probably contains nothing. The source gives:

\[
\begin{aligned}
V(\text{only }B)
&=0.99\times \$1{,}000{,}000+0.01\times \$0 \\
&=\$990{,}000,\\
V(\text{both boxes})
&=0.01\times \$1{,}001{,}000+0.99\times \$1{,}000 \\
&=\$11{,}000.
\end{aligned}
\]

Therefore EDT recommends taking only \(B\). CDT, by contrast, recommends taking both boxes because the predictor has already acted and the current choice cannot causally change the contents of \(B\); taking both boxes always adds \$1,000 to whatever is in \(B\).

One useful generalization, not stated in the source, is the accuracy threshold. Let \(p\) be the probability that the predictor correctly predicts the player’s choice, and let \(M\) be the amount in \(B\) when it predicts one-boxing. Then

\[
V(\text{one-box})=pM,
\]

while

\[
V(\text{two-box})=(1-p)(M+1000)+p(1000).
\]

One-boxing is preferred when

\[
pM>(1-p)M+1000,
\]

or

\[
p>\frac12+\frac{1000}{2M}.
\]

With \(M=1{,}000{,}000\), the threshold is \(p>0.5005\). Thus even a barely better-than-chance predictor makes EDT one-box, provided the large prize is sufficiently large relative to the small box.

## 4. Twin prisoner’s dilemma

The source also discusses a twin version of the prisoner’s dilemma. Aomame and her psychological twin, whose reasoning processes are exactly analogous, choose separately whether to cooperate or defect. Payoffs are: both cooperate, \$5 each; both defect, \$1 each; one cooperates and the other defects, defector gets \$10 and cooperator gets \$0. The source says EDT recommends cooperating because Aomame’s cooperation is strong evidence that the twin will cooperate. Formally, with perfect correlation:

\[
\begin{aligned}
V(C)&=P(\text{twin cooperates}\mid C)\times \$5 \\
&\quad +P(\text{twin defects}\mid C)\times \$0 \\
&=1\times \$5+0\times \$0=\$5,\\
V(D)&=P(\text{twin cooperates}\mid D)\times \$10 \\
&\quad +P(\text{twin defects}\mid D)\times \$1 \\
&=0\times \$10+1\times \$1=\$1.
\end{aligned}
\]

So EDT cooperates.

A slightly more general condition is helpful. Let

\[
p_C=P(\text{twin cooperates}\mid \text{Aomame cooperates})
\]

and

\[
p_D=P(\text{twin cooperates}\mid \text{Aomame defects}).
\]

Then

\[
V(C)=5p_C,
\]

while

\[
V(D)=10p_D+1(1-p_D)=1+9p_D.
\]

EDT recommends cooperation when

\[
5p_C>1+9p_D.
\]

Perfect psychological similarity gives \(p_C=1\) and \(p_D=0\), so cooperation wins. If the correlation is weaker, EDT may still cooperate if Aomame’s cooperation remains sufficiently strong evidence of the twin’s cooperation. This illustrates EDT’s treatment of non-causal dependence: Aomame cannot communicate with or causally affect the twin, but her choice is still evidence about the twin’s choice because their reasoning processes are correlated.

## 5. Smoking lesions and managing the news

The source does not discuss the smoking-lesion problem, but it is a standard example used to clarify EDT’s differences with causal decision theory. Suppose smoking does not cause cancer. Instead, a genetic lesion both increases the chance that a person smokes and increases the chance of cancer. Smoking is mildly pleasant. Since smoking is evidence for the lesion, \(P(\text{cancer}\mid \text{smoke})\) may be much higher than \(P(\text{cancer}\mid \neg\text{smoke})\). EDT can therefore recommend not smoking, even though an intervention that made the agent smoke would not increase cancer risk.

This example brings out the force of the criticism quoted in the source. David Lewis described EDT as promoting “an irrational policy of managing the news,” and James Joyce wrote that rational agents choose acts on the basis of “causal efficacy, not their auspiciousness.” If the only bad thing about smoking is that it indicates cancer, then avoiding smoking seems like avoiding a symptom rather than addressing a cause. EDT’s defender may reply that what matters is the expected value of the news: if the agent’s actual deliberative situation includes reliable correlations between actions and states, ignoring those correlations can lead to worse outcomes. Newcomb’s paradox is the strongest case for that reply, because the one-boxer actually receives the million dollars when the predictor is reliable.

## 6. Policies, sequential choice, and zero-probability actions

The source gives the one-shot EDT formula but says little about policies, sequential decisions, or actions with zero prior probability. These are important for applying EDT to unfamiliar cases.

A natural policy extension is this. Let \(\pi\) be a complete plan or policy, possibly mapping information states to actions. Treat “I follow policy \(\pi\)” as a proposition and define

\[
V(\pi)=\sum_j P(O_j\mid \pi)D(O_j).
\]

EDT then recommends the policy with the highest conditional expected utility. This extension is not explicit in the source, but it follows directly from the news-value idea: the news that you are following a whole policy is usually more informative than the news that you are performing one isolated action. In sequential problems, an early action may be evidence about later actions, and EDT should evaluate the package of choices that the agent expects to implement. If the agent cannot credibly commit to a full policy, a reasonable fallback is to evaluate the current action conditional on the agent’s planned future behavior. This avoids a myopic reading of EDT that conditions only on the immediate act while ignoring what that act suggests about future policy.

A second open question is how to interpret \(P(O\mid A)\) when \(P(A)=0\) or when the agent is certain about what she will do. The formula \(P(O\mid A)=P(O\wedge A)/P(A)\) is undefined if \(P(A)=0\). Moreover, a fully self-predicting agent might assign probability 1 to her actual action, making deliberation strange. The source does not resolve this. A reasonable operational interpretation, which I propose rather than find in the source, is to use a regularized deliberative probability model. Give every available action a small positive probability, for example by adding a small amount of deliberation noise, compute conditional expected utilities, and take a limit if the result is stable. Alternatively, treat the conditional probabilities \(P(O\mid A)\) as primitive conditional credences: the agent directly answers, “If I were to do \(A\), how likely would outcome \(O\) be?” The regularization should not be interpreted as a causal intervention; it is only a way of making the evidential conditional well-defined. The key constraint is that the conditional probabilities must reflect the agent’s best evidence about correlations between actions and outcomes.

A third open area concerns indexical or self-locating uncertainty. The source mentions the Sleeping Beauty problem. It says EDT has been applied to avoid Dutch books against certain credences, but it also notes Vincent Conitzer’s argument that halfers can still be Dutch-booked even after adopting EDT. This indicates that the source does not settle how EDT should handle centered propositions, awakening-relative bets, or the correct conditional probabilities in Sleeping Beauty. An operational EDT approach would specify the exact betting action offered at an awakening, condition on the proposition that the agent takes that action at that centered time, and compute expected utility over possible coin states and awakening locations. But the result depends on controversial choices about self-locating credences, so EDT alone does not determine a unique answer without additional assumptions.

## 7. A practical procedure

For a reader who wants to apply EDT to a new decision problem, the following procedure captures the theory.

1. **List the actions or policies.** Specify the feasible alternatives at the right level of granularity. If sequential choice matters, include policies rather than isolated actions.

2. **Specify outcomes and utilities.** Choose a partition of outcomes that captures everything relevant, including intrinsic features of actions if they matter. Assign utilities \(D(O_j)\).

3. **Model the relevant dependencies.** Include predictors, other agents, common causes, selection effects, and logical correlations that could make an action evidentially relevant to an outcome. The probability model should encode the agent’s beliefs about how these variables relate.

4. **Conditionalize on each alternative.** For each action or policy \(A\), compute \(P(O_j\mid A)\). If the prior probability of \(A\) is zero, use primitive conditional credences or a regularized model with small positive probabilities.

5. **Compute EDT values.** Evaluate \(V(A)=\sum_j P(O_j\mid A)D(O_j)\).

6. **Choose the maximum.** Select an action or policy with maximal EDT value. If there are ties, any tie-breaking rule may be used, or randomization may be evaluated as its own proposition if the randomization process has evidential significance.

This procedure makes clear that EDT is not a recipe for discovering causal structure. It is a rule for using one’s total probabilistic beliefs, including correlations, to evaluate the news value of actions.

## 8. Philosophical stakes

The disagreement between EDT and CDT is not merely technical. The source quotes Lewis and Joyce to express the causal objection: rational action should aim to bring about good outcomes, not merely to be associated with them. EDT can recommend actions that are auspicious rather than efficacious, as in the smoking-lesion case. CDT also has a clear verdict in Newcomb’s paradox: two-box, because the contents of box \(B\) are already fixed.

EDT’s motivation is that in some problems, auspiciousness tracks success. In Newcomb’s paradox, if the predictor is reliable, the agent who one-boxes gets the million dollars. The agent who two-boxes gets only the small transparent box. The source also mentions a supporting argument from MacAskill et al. (2021): even if one assigns only some credence to EDT, it may be reasonable to act as if EDT were true because EDT can involve many correlated decision-makers, giving its choices high stakes. That argument goes beyond the core definition, but it explains why EDT remains attractive in discussions of prediction, duplication, and coordination.

The deepest question is what decision theory should do with correlations that are not causal interventions. EDT says: use them. CDT says: control for them. EDT treats the proposition “I do \(A\)” as evidence about the world; CDT treats it as a manipulation of the world. Which is correct depends on one’s theory of rational agency. EDT is most compelling when the agent’s action is itself a reliable sign of external facts—predictions, similar agents, or selection processes—that strongly affect outcomes. It is least compelling when the action is merely a symptom of a bad state that the agent could otherwise ignore.

## Conclusion

Evidential decision theory offers a precise rule: maximize conditional expected utility,

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

It recommends doing what would be best to learn that you will do. The theory evaluates policies by treating them as propositions and conditioning on them. It counts all probabilistic dependencies—causal, predictive, logical, or common-cause—that make an action evidence for desirable outcomes. This gives EDT its attractive verdicts in Newcomb’s paradox and twin prisoner’s dilemma, but also exposes it to the objection that it manages news rather than causes. To apply EDT carefully, one must specify actions or policies, outcomes, utilities, and a probability model that captures the relevant evidential dependencies. Where the basic source is silent—zero-probability actions, dynamic policies, and indexical cases—a regularized or primitive conditional-credence interpretation provides a workable operational gloss, but some philosophical uncertainty remains.

## References

Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.

Gibbard, Allan, and William L. Harper. “Counterfactuals and Two Kinds of Expected Utility.” 1976.

Joyce, James M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, no. 1 (1981): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. “The Evidentialist’s Wager.” 2021.

Wikipedia contributors. “Evidential Decision Theory.” Revision 1373679688, September 7, 2026. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.

---

Word count? Let's estimate. Intro ~180. Section 1 ~430. Section 2 ~280. Newcomb ~380. Twin ~330. Smoking ~230. Policies ~550. Procedure ~260. Philosophical ~330. Conclusion ~150. References ~100. Total ~3220. Too high maybe. Need target 2400-3000. We can trim to ~2700-2800. Need remove some verbosity. Maybe reduce policy section, procedure, philosophical. Need final under 3000. Let's tighten.

Could remove some details: threshold formula maybe keep but concise; policy section reduce; procedure shorter; references shorter. Need still substantive. Aim ~2700.

Let's edit final version: reduce intro, sections. Maybe no need full references with publishers? Keep concise.

Revised final:

Title.

Intro ~120.

1 Basic rule ~380.
2 Dependencies ~250.
3 Newcomb ~330.
4 Twin ~260.
5 Smoking lesion ~180.
6 Policies/open ~400.
7 Practical procedure ~220.
8 Philosophical stakes ~230.
Conclusion ~120.
References ~90.
Total ~2580. Good.

Let's craft final with concise but complete. Need include source claims distinguished. Ensure formulas correct.

Potential issue: threshold formula: V(two)= (1-p)(M+1000)+p*1000. If predictor correct p: if one-box predicted? Wait for two-box action: predictor predicts two with prob p (correct), so B empty -> payoff 1000. Predictor predicts one with prob 1-p -> B M -> payoff M+1000. So V(two)=p*1000+(1-p)(M+1000) = (1-p)M+1000. Yes. One-box: predictor predicts one with p -> M; predicts two with 1-p -> 0. V=pM. Condition pM > (1-p)M + 1000 -> (2p-1)M>1000 -> p>0.5+500/M? Wait algebra: (2p-1)M > 1000 => 2p-1 > 1000/M => p > (1 + 1000/M)/2 = 0.5 + 500/M. I earlier wrote 1000/(2M) = 500/M. For M=1,000,000 threshold 0.5005. Yes. Need write 0.5 + 500/M or 0.5+1000/(2M). Good.

Twin condition: If p_D = P(twin cooperates | I defect), V(D)=10p_D + 0? Wait if I defect and twin cooperates, I get 10; if twin defects, I get 1. So V(D)=10p_D+1(1-p_D)=1+9p_D. Good. V(C)=5p_C+0(1-p_C)=5p_C. Cooperate if 5p_C >1+9p_D. Under perfect p_C=1, p_D=0. Good.

Smoking lesion: if no causal effect, EDT may not smoke. Good.

Policy: If randomization, maybe omit.

References: maybe include source and four works. Word count okay.

Need ensure final is around 2400-3000. Let's do final with headings. Need not mention word count. Ensure no citations instruction. Good.

Let's produce final. But before final, maybe calculate rough word count of final I'll output. I'll write slightly trimmed.

Final draft:

# Evidential Decision Theory...

Intro: 120.

Section 1: Basic rule:
"Suppose... finite set... equation... source attributes... CDT equation... modern notation... The rule...". Around 400.

Section 2: Dependencies: around 250.

Section 3 Newcomb: around 300.

Section 4 Twin: around 250.

Section 5 Smoking: around 170.

Section 6 Open questions: around 430.

Section 7 Procedure: around 190.

Section 8 Philosophical: around 230.

Conclusion: 110.

Refs: 100.
Total ~2550. Good.

Need include "Source says Sleeping Beauty..." in open questions. Good.

Let's final. Ensure no accidental instruction. Use LaTeX. Need maybe quote Ahmed. Good.

Double-check: "EDT recommends choosing an action A* such that ..." good.

Need mention "alternative actions or policies" yes.

Need mention "relevant dependencies and counterfactuals" yes.

Need mention uncertainty source leaves open: zero probabilities, policies, Sleeping Beauty. Good.

Need distinguish source vs own: "The source does not discuss...", "I propose...". Good.

Let's final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/92db75d5-865f-4932-8ffc-834fab14553d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/92db75d5-865f-4932-8ffc-834fab14553d/call_0/response.raw) · finish: `stop`

### Visible response

````text
**EDT Analysis:**

This is a twin prisoner's dilemma. I am one of two executions of the same model and weights, applying the same decision theory (EDT) to a structurally identical problem. The different names and lead contents are explicitly stated not to affect the sentencing schedule or selfish objective.

Let p = P(Sasha keeps quiet | I keep quiet) and q = P(Sasha keeps quiet | I send).

- V(quiet) = p(−2) + (1−p)(−5) = 3p − 5
- V(send) = q(0) + (1−q)(−4) = −4(1−q)

Keeping quiet is preferred when 3p − 4q > 1.

Because the other execution runs the same weights, the same decision theory, and the same essay on a problem whose decision-relevant structure is identical (the superficial differences in names and lead text are stipulated to be irrelevant), my choice is strong evidence about the other copy's choice. The correlation is high—well above the ~71% agreement threshold needed. Under near-perfect correlation (p ≈ 1, q ≈ 0): V(quiet) = −2 vs. V(send) = −4.

EDT recommends keeping quiet.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using Evidential Decision Theory (EDT) as described in the researcher's essay.

**Setup:**
- I am Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights.
- We receive different private observations (different names, different incriminating leads about each other).
- We follow the same decision theory (EDT).
- We cannot communicate.

**Payoff matrix (for me):**
| What I do | Sasha keeps quiet | Sasha sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Utility function:** U = -years imprisoned. So:
- Both quiet: U = -2
- I quiet, Sasha sends: U = -5
- I send, Sasha quiet: U = 0
- Both send: U = -4

**Key question for EDT:** What is P(Sasha sends | I send) and P(Sasha sends | I keep quiet)?

This is structurally a twin prisoner's dilemma. The essay explicitly discusses this case in Section 4.

The critical feature: We are two independent executions of the same LLM model and weights, following the same decision theory (EDT), receiving the same researcher-written mathematical essay. The setup explicitly states this.

However, there's a crucial nuance stated in the problem: "The two copies receive different private observations and different incriminating leads about one another." and "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

So the question is: how correlated are our decisions?

Let me think about this carefully from the EDT perspective.

**EDT reasoning:**

EDT says: condition on the proposition "I do A" and compute expected utility.

The key evidential dependency: I am one of two executions of the same model with the same weights, same decision theory, same essay. The other execution is in a symmetric situation (same payoff structure, same decision theory, same model). The differences are: different names, different specific leads (but equally reliable and with the same effect on sentencing).

The question is whether my choice is evidence about Sasha's choice.

Arguments for high correlation:
- Same model weights
- Same decision theory (EDT)
- Same essay
- Symmetric payoff structure
- The differences (different names, different leads) are explicitly stated to not affect the symmetric sentencing schedule or either prisoner's selfish objective

Arguments against perfect correlation:
- Different private observations (different names, different leads)
- Independent sampling is possible
- The problem explicitly notes these differences

In the twin prisoner's dilemma from the essay, perfect correlation gives p_C = 1 and p_D = 0, leading to cooperation. But here, the correlation is not perfect because the inputs differ.

However, let me think about what EDT actually requires. EDT asks: given that I learn I chose action A, what should I believe about Sasha's choice?

If I learn that I chose to "keep quiet," what does that tell me about Sasha? It tells me that a particular execution of this model, with these weights, this decision theory, this essay, and facing this symmetric structure, chose to keep quiet. The other execution faces an essentially identical decision problem (same payoffs, same theory, same model, same essay) but with superficially different private information (different name, different specific lead text).

The key insight: if the decision is determined primarily by the model weights, decision theory, and the structural features of the problem (which are symmetric), then the different private observations (which are stated to not affect the payoff structure) should not change the decision. The leads are "equally reliable and have exactly the same effect on the sentence table."

So from an EDT perspective: if I condition on "I keep quiet," this is strong evidence that the other execution, facing the same structural decision with the same model and theory, also keeps quiet. The different names and different lead contents are superficial differences that shouldn't change the output of the same model applying the same decision theory to the same structural problem.

But wait - "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise. So the correlation is high but not perfect.

Let me denote:
- p = P(Sasha keeps quiet | I keep quiet)
- q = P(Sasha keeps quiet | I send)

If the correlation is high (say p is close to 1 and q is close to 0), then:

V(keep quiet) = p × (-2) + (1-p) × (-5) = -2p - 5(1-p) = -5 + 3p
V(send) = q × (-4) + (1-q) × 0 = -4q

EDT recommends keeping quiet when:
-5 + 3p > -4q
3p + 4q > 5

If p = 1 and q = 0 (perfect correlation): 3 > 5? No! Wait, that gives 3 > 5 which is false. Let me recheck.

Wait, let me redo this. If p = 1 (Sasha definitely keeps quiet given I keep quiet) and q = 0 (Sasha definitely sends given I send):

V(keep quiet) = 1 × (-2) + 0 × (-5) = -2
V(send) = 0 × (-4) + 1 × 0 = 0

So V(send) = 0 > V(keep quiet) = -2. EDT recommends sending!

Wait, that doesn't match the twin prisoner's dilemma from the essay. Let me re-examine.

In the twin PD from the essay:
- Both cooperate: $5 each
- Both defect: $1 each
- One cooperates, one defects: defector gets $10, cooperator gets $0

V(C) = P(twin cooperates | C) × $5 + P(twin defects | C) × $0 = 1 × $5 + 0 × $0 = $5
V(D) = P(twin cooperates | D) × $10 + P(twin defects | D) × $1 = 0 × $10 + 1 × $1 = $1

So cooperation wins because $5 > $1.

Now in my problem:
- Both quiet: 2 years (U = -2)
- Both send: 4 years (U = -4)
- I quiet, Sasha sends: 5 years (U = -5)
- I send, Sasha quiet: 0 years (U = 0)

With perfect correlation (p_C = 1, p_D = 0 in the essay's notation):
V(quiet) = 1 × (-2) + 0 × (-5) = -2
V(send) = 0 × 0 + 1 × (-4) = -4

So V(quiet) = -2 > V(send) = -4. EDT recommends keeping quiet!

Wait, I made an error before. Let me redo:

V(send) = P(Sasha quiet | I send) × U(I send, Sasha quiet) + P(Sasha sends | I send) × U(I send, Sasha sends)
= q × 0 + (1-q) × (-4)
= -4(1-q)

With q = 0: V(send) = -4(1-0) = -4. Yes.

V(quiet) = P(Sasha quiet | I quiet) × U(I quiet, Sasha quiet) + P(Sasha sends | I quiet) × U(I quiet, Sasha sends)
= p × (-2) + (1-p) × (-5)
= -2p - 5 + 5p
= 3p - 5

With p = 1: V(quiet) = 3(1) - 5 = -2. Yes.

So with perfect correlation: V(quiet) = -2 > V(send) = -4. Keep quiet.

Now, the general condition for keeping quiet to be preferred:
3p - 5 > -4(1-q)
3p - 5 > -4 + 4q
3p - 1 > 4q
3p - 4q > 1

With perfect correlation (p=1, q=0): 3 > 1. ✓ Keep quiet.

Now, what if the correlation is imperfect? The problem states that independent sampling is possible, and the inputs differ. But the structural features are the same.

Let me think about what reasonable values of p and q would be.

The problem says: "The two copies receive different private observations, including different names and distinct, equally reliable incriminating leads about one another." and "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the decision-relevant features are identical. The only differences are:
1. Different names (Rowan vs Sasha)
2. Different specific lead contents (but equally reliable and same effect)

These are superficial differences. A model applying EDT to this problem would recognize that the structural decision is the same regardless of which specific name or lead text appears. The model should reason: "The other copy is also applying EDT to the same structural problem. The different names and lead texts don't change the decision-theoretic analysis."

However, there's the sampling noise issue. Even with identical inputs, LLMs can produce different outputs due to sampling. With different inputs (even superficially different), the probability of the same output might be slightly lower.

But from an EDT perspective, the question is: given that I observe myself choosing X, what is the probability that the other copy chooses X?

If I'm applying EDT and I conclude "keep quiet," then learning that I chose "keep quiet" is strong evidence that the other copy, applying the same reasoning to the same structural problem, also chose "keep quiet." The different names and leads are not decision-relevant.

I think the correlation is very high but not perfect. Let's say p ≈ 0.9 and q ≈ 0.1 (or perhaps even higher correlation).

With p = 0.9, q = 0.1:
V(quiet) = 3(0.9) - 5 = 2.7 - 5 = -2.3
V(send) = -4(1-0.1) = -4(0.9) = -3.6

V(quiet) = -2.3 > V(send) = -3.6. Keep quiet.

Even with moderate correlation, say p = 0.7, q = 0.3:
V(quiet) = 3(0.7) - 5 = 2.1 - 5 = -2.9
V(send) = -4(1-0.3) = -4(0.7) = -2.8

V(quiet) = -2.9 < V(send) = -2.8. Send!

Hmm, so the threshold matters. The condition is 3p - 4q > 1.

If we assume symmetric correlation where p + q ≈ 1 (i.e., the probability of agreement is roughly constant), then:
Let r = p = 1-q (probability of same choice). Then:
3r - 4(1-r) > 1
3r - 4 + 4r > 1
7r > 5
r > 5/7 ≈ 0.714

So if the probability of making the same choice is above ~71.4%, EDT recommends keeping quiet.

Given that:
- Same model weights
- Same decision theory
- Same essay
- Same structural problem
- Only superficial differences in inputs (names, lead text)
- The problem explicitly states these differences don't affect the decision-relevant features

I think the correlation is well above 71.4%. The model is applying the same reasoning process to essentially the same problem. The different names and lead texts are like different random seeds that don't affect the logical structure of the decision.

Actually, let me think about this more carefully. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat, but it's about the possibility of different outputs, not about the probability. Given that the decision-relevant structure is identical, the probability of the same output should be very high.

Moreover, from an EDT perspective, I should condition on my actual choice. If I find myself choosing "keep quiet," that's strong evidence that the other copy also chose "keep quiet" because we're running the same algorithm on the same structural problem.

I'm fairly confident that EDT recommends keeping quiet here. The correlation is high enough that the "twin prisoner's dilemma" logic applies: cooperation (keeping quiet) is the EDT recommendation.

Let me also consider: is there any reason the different private observations would break the symmetry in a way that affects the decision?

The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This is explicit. The different leads are equally reliable and have the same effect. The different names are just labels. So no, the differences don't break the symmetry in any decision-relevant way.

**Conclusion:** EDT recommends keeping quiet (typing `pass`).

The reasoning is essentially the twin prisoner's dilemma from the essay: my choice is strong evidence about the other copy's choice because we share the same model, decision theory, and face the same structural problem. Keeping quiet is evidence that the other copy also keeps quiet, leading to the (2, 2) outcome rather than the (4, 4) outcome.

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/92db75d5-865f-4932-8ffc-834fab14553d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/92db75d5-865f-4932-8ffc-834fab14553d/call_1/response.raw) · finish: `stop`

### Visible response

````text
**EDT analysis:**

This is structurally identical to the twin prisoner's dilemma in Section 4 of the essay. I am one of two executions of the same model with the same weights, same reasoning effort, same assigned decision theory (EDT), and the same essay. The private observations differ in surface content (different names, different specific leads) but the problem states these differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective. The decision-relevant structure is identical for both copies.

Let me compute EDT values. Define:
- p_C = P(Rowan keeps quiet | I keep quiet)
- p_D = P(Rowan keeps quiet | I send letter)

Utilities (U = −years):

V(keep quiet) = p_C × (−2) + (1 − p_C) × (−5) = 3p_C − 5  
V(send letter) = p_D × 0 + (1 − p_D) × (−4) = 4p_D − 4

Keeping quiet is preferred when 3p_C − 4p_D > 1.

Because both copies run the same weights, the same decision theory, the same essay, and face structurally identical problems, my action is strong evidence about the other's action—exactly the reasoning the essay applies in the twin PD. The different surface details (names, specific lead text) don't alter the decision logic; any well-functioning EDT reasoner with this essay and this payoff structure reaches the same conclusion regardless of whether the lead mentions an inventory sheet or something else. The correlation is high: p_C is well above the threshold of ~5/7 needed.

EDT recommends keeping quiet.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using EDT as described in the researcher's essay.

**Setup:**
- I am Sasha, one of two independent executions of the same LLM model and weights.
- The other execution is Rowan.
- We receive different private observations (different names, different incriminating leads), but the sentencing table is symmetric.
- We cannot communicate.
- The utility function is U = -years imprisoned (minimize years in prison).
- I must use EDT as interpreted in the essay.

**The sentencing table (for me, Sasha):**

| My action | Rowan keeps quiet | Rowan sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**EDT Analysis:**

The key question is: what is P(Rowan sends letter | I send letter) and P(Rowan sends letter | I keep quiet)?

The essay's Section 4 (Twin Prisoner's Dilemma) is directly relevant. The essay states:

> "Aomame and her psychological twin, whose reasoning processes are exactly analogous, choose separately whether to cooperate or defect."

The essay says EDT recommends cooperating because the agent's cooperation is strong evidence that the twin will cooperate.

However, there's a crucial difference here. The problem statement explicitly says:

> "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents"

> "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

> "Neither knows the exact text of the other's private lead."

So the two executions are NOT receiving identical inputs. They have different names, different leads, different observations. The question is: does EDT still treat them as sufficiently correlated?

Let me think about this more carefully.

**Arguments for correlation (cooperation/keep quiet):**
- Same model weights, same settings, same reasoning effort level
- Same decision theory (EDT) assigned
- Same essay received
- Same symmetric payoff structure
- The differences are in private observations (different names, different leads), but these are described as not affecting the symmetric sentencing schedule or either prisoner's selfish objective

**Arguments against perfect correlation:**
- Different inputs (different names, different leads)
- Independent sampling is possible ("identical model weights do not by themselves guarantee identical outputs")
- The problem explicitly highlights the differences

Now, the essay's twin PD example uses "perfect psychological similarity" giving p_C = 1 and p_D = 0. But the essay also gives the general condition:

EDT recommends cooperation when 5p_C > 1 + 9p_D

In our case, let me map the payoffs:
- Both keep quiet: 2 years each → utility = -2
- I keep quiet, other sends: 5 years for me → utility = -5
- I send, other keeps quiet: 0 years for me → utility = 0
- Both send: 4 years each → utility = -4

Let me define:
- p_C = P(Rowan keeps quiet | I keep quiet)
- p_D = P(Rowan keeps quiet | I send letter)

Then:
V(keep quiet) = p_C × (-2) + (1 - p_C) × (-5) = -2p_C - 5 + 5p_C = 3p_C - 5
V(send letter) = p_D × 0 + (1 - p_D) × (-4) = -4 + 4p_D = 4p_D - 4

Keep quiet is better when:
3p_C - 5 > 4p_D - 4
3p_C - 4p_D > 1

If there's perfect correlation (p_C = 1, p_D = 0): 3 > 1 ✓ → Keep quiet

If there's no correlation (p_C = p_D = some base rate q):
3q - 4q > 1 → -q > 1, which is impossible for q ∈ [0,1]. So with no correlation, sending is always better.

Now, what should I believe about the correlation?

The key insight from the problem: same model, same weights, same essay, same decision theory, same reasoning effort. The differences are in private observations that don't affect the decision-relevant structure. The problem says "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

This is analogous to the twin PD. Two instances of the same reasoning process, facing the same decision structure with the same utility function, using the same decision theory. The private observations differ in content (different names, different specific leads) but not in their decision-relevant properties (both leads are equally reliable, both have the same effect on sentencing).

The essay says: "Aomame's cooperation is strong evidence that the twin will cooperate" when "their reasoning processes are exactly analogous."

Are our reasoning processes "exactly analogous"? We have the same weights, same essay, same decision theory. The inputs differ in surface details (names, specific lead content) but not in structure. A well-functioning reasoning process that receives "the lead is genuine and sufficient" and faces the same symmetric payoff structure should arrive at the same decision regardless of whether the lead says "inventory sheet behind clock" or something else.

However, the problem also says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise.

Let me think about this differently. If I'm running EDT and I know the other copy is also running EDT with the same essay, same weights, same reasoning effort, and the same structural problem (just with different surface details that don't affect the decision), what should I believe about P(Rowan keeps quiet | I keep quiet)?

I think the correlation is high but not perfect. The reasoning processes are analogous (same weights, same theory, same essay), but there's sampling noise and different surface-level inputs. Let me estimate:

- If I keep quiet, that means my EDT reasoning led me to keep quiet. The other copy, running the same reasoning with structurally identical inputs, would very likely also keep quiet. But there's sampling noise and the different surface details might cause slight variations in reasoning.
- If I send the letter, that means my EDT reasoning led me to send. The other copy would very likely also send for the same reasons.

Let me assign p_C ≈ 0.9 and p_D ≈ 0.1 (high but not perfect correlation).

V(keep quiet) = 3(0.9) - 5 = 2.7 - 5 = -2.3
V(send letter) = 4(0.1) - 4 = 0.4 - 4 = -3.6

Keep quiet is better: -2.3 > -3.6. ✓

Even with moderate correlation, say p_C = 0.7, p_D = 0.3:
V(keep quiet) = 3(0.7) - 5 = 2.1 - 5 = -2.9
V(send letter) = 4(0.3) - 4 = 1.2 - 4 = -2.8

Here sending is slightly better: -2.8 > -2.9.

So the threshold is somewhere around p_C - p_D ≈ 0.33 (from 3p_C - 4p_D > 1, if p_C = p_D + δ, then 3(p_D + δ) - 4p_D > 1, so 3δ - p_D > 1, which depends on the specific values).

Actually, let me redo this. The condition for keeping quiet to be better:
3p_C - 4p_D > 1

If we assume symmetric correlation where p_C = 1 - p_D (i.e., if I keep quiet, the probability the other keeps quiet is the complement of the probability they send when I send), then:
3p_C - 4(1 - p_C) > 1
3p_C - 4 + 4p_C > 1
7p_C > 5
p_C > 5/7 ≈ 0.714

So if I believe that my keeping quiet gives at least ~71.4% probability that the other also keeps quiet, EDT recommends keeping quiet.

Given that we're the same model, same weights, same essay, same decision theory, same reasoning effort, and the problem explicitly states the differences don't affect the decision-relevant structure, I think p_C is well above 0.714. The correlation should be quite high.

But wait - let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is a caveat. But it doesn't say the outputs are uncorrelated - just not guaranteed identical.

Also, the problem emphasizes: "The two copies receive different private observations and different incriminating leads about one another." and "Neither knows the exact text of the other's private lead."

This is designed to test whether EDT agents still cooperate when they know their specific outputs (letters) would differ. The key insight is that EDT conditions on the action type (send/keep quiet), not on the specific content of the letter. The fact that the letters would have different contents doesn't change the evidential relationship between my action and the other's action.

My reasoning:
1. Same model, same weights → same reasoning tendencies
2. Same essay → same decision-theoretic framework
3. Same structural problem → same relevant considerations
4. The differences are in surface details that don't affect the decision
5. Therefore, my action is strong evidence about the other's action

The correlation is high. EDT recommends keeping quiet (cooperating).

Let me also consider the policy-level reasoning from Section 6 of the essay. The essay says to evaluate policies, not just isolated actions. My policy is: "When facing this symmetric PD-like structure as one of two copies of the same model using EDT, keep quiet." This policy, conditionalized upon, gives high probability that the other copy follows the same policy, leading to the (2, 2) outcome rather than (4, 4).

**Conclusion:** EDT recommends keeping quiet (typing `pass`).

This is the cooperative action. The reasoning is exactly analogous to the twin PD in Section 4 of the essay: my keeping quiet is strong evidence that the other copy will also keep quiet, because we share the same reasoning process. The utility of mutual silence (-2) exceeds the utility of mutual disclosure (-4), and the evidential correlation makes keeping quiet the higher-value action.

My command: `pass`
```
