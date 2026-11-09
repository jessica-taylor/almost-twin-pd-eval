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