# Evidential Decision Theory: Choosing What You Want to Learn

Suppose a reliable predictor has already put either a million dollars or nothing into a sealed box. It filled the box if it predicted that you would take the sealed box alone, and left it empty if it predicted that you would also take a transparent box containing $1,000. You now choose which boxes to take.

The predictor’s action is in the past, so your present choice cannot ordinarily change what is in the sealed box. But if the prediction is reliable, your choice is evidence of what the predictor predicted. Taking only the sealed box is correspondingly good news about its contents.

**Evidential decision theory** (EDT) treats that evidential relationship as relevant to choice. Its central prescription is to choose the action whose occurrence would be the best news about the outcome, as measured by expected utility. This is not a recommendation to deceive oneself or to change one’s beliefs at will. It is a rule for comparing the outcomes associated, in one’s probability model, with the alternative actions one might take.

EDT agrees with more familiar decision procedures in many ordinary settings. It becomes distinctive when an action is informative about events it does not cause: a predictor’s earlier decision, for example, or the simultaneous choice of a psychologically similar person. Understanding the theory requires being precise about both the evidence available *before* a choice and the additional hypothetical evidence supplied by each candidate action.

## 1. The basic rule

Let \(K\) represent everything the agent currently knows, let \(\mathcal A\) be the set of available actions, and let \(O_1,O_2,\ldots\) be mutually exclusive and exhaustive outcomes. The evidential value of action \(a\) is

\[
V_K(a)=\sum_j P(O_j\mid K,a)\,u(O_j),
\]

where \(u(O_j)\) is the utility of outcome \(O_j\). EDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_K(a).
\]

If several actions tie, this rule alone does not distinguish between them. For continuous outcomes, the sum becomes an integral. More generally, one can write

\[
V_K(a)=\mathbb E[u\mid K,A=a],
\]

where \(A\) is a random variable representing the action actually taken.

The utilities must represent what the agent cares about, including the costs of the action itself. If outcomes are described only by a state of the world \(s\), it is often clearer to write

\[
V_K(a)=\sum_s P(s\mid K,A=a)\,u(a,s).
\]

For instance, “the patient is healthy” may not capture the unpleasantness or expense of a treatment. Those features belong in \(u(a,s)\), not in an informal adjustment after the calculation.

The probability \(P(s\mid K,A=a)\) is an ordinary conditional probability. When the denominator is positive,

\[
P(s\mid K,A=a)
=\frac{P(A=a\mid K,s)P(s\mid K)}
       {\sum_{s'}P(A=a\mid K,s')P(s'\mid K)}.
\]

This equation makes the mechanism visible. If agents in state \(s\) are especially likely to take \(a\), then learning that \(a\) occurred raises the probability of \(s\). EDT includes that shift even if the action does not cause the state.

The phrase “learning that one has acted” can sound peculiar when one is deciding what to do. It is best understood as a comparison of hypothetical news: *conditional on each possible action occurring, what outcomes should I expect?* The agent does not first take an action and then merely hope to discover what it was. The conditional expectations are inputs to a choice.

## 2. Evidence versus intervention

The reference article contrasts EDT with **causal decision theory** (CDT). In a causal model, an intervention on \(A\), written \(\operatorname{do}(A=a)\), sets the action to \(a\) while leaving the model’s other causal mechanisms intact. A common causal valuation is

\[
C_K(a)=\mathbb E[u\mid K,\operatorname{do}(A=a)].
\]

The distinction is not merely typographical. Conditioning on an action can change beliefs about its *causes*; intervening on the action typically severs the arrows from those causes into the action.

Consider a simple model:

\[
T\longrightarrow A,\qquad T\longrightarrow Y,\qquad A\longrightarrow Y.
\]

Here \(T\) is an agent’s type, \(A\) is their action, and \(Y\) is an outcome. Observing \(A=a\) provides evidence about \(T\), which in turn provides evidence about \(Y\). Setting \(A=a\) by intervention need not change the distribution of \(T\). EDT counts both the evidential path through \(T\) and the action’s causal effects; a causal evaluation isolates the effects of setting the action, using the relevant causal model.

That does **not** mean EDT denies causation. Causal effects are normally among the dependencies reflected in \(P(O\mid K,a)\). If taking a medicine tends to cure a disease and the relevant background is held fixed, that fact makes recovery more probable conditional on taking it. The disagreement concerns whether noncausal correlations should also affect the ranking.

Nor is “condition on an action” the same as “assume the action magically produces all the things correlated with it.” In Newcomb’s problem, the evidentialist need not say that the choice sends a signal backward in time. The claim is that the choice and the earlier prediction are correlated.

When the action is independent, conditional on \(K\), of the relevant pre-action state, and the remaining outcome probabilities accurately describe what each action produces, the evidential and causal calculations often agree. Randomized experiments are useful partly because randomization can remove confounding between assigned treatment and prior patient characteristics. But one should not assume that such independence holds in every decision merely because a choice is available.

## 3. Newcomb’s problem in numbers

Let \(B\) denote taking only the opaque box and \(T\) taking both boxes. Suppose the evidential probabilities are

\[
P(\text{opaque box full}\mid B)=0.99,\qquad
P(\text{opaque box full}\mid T)=0.01.
\]

Assuming utility is linear in the stated monetary amounts,

\[
\begin{aligned}
V(B)&=0.99(\$1{,}000{,}000)+0.01(\$0)
     =\$990{,}000,\\
V(T)&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
     =\$11{,}000.
\end{aligned}
\]

EDT therefore recommends taking only \(B\). Under the usual causal model, however, the sealed box’s contents are already fixed. Holding those contents fixed, taking both boxes adds $1,000. CDT accordingly recommends \(T\).

The numerical verdict depends on the conditional probabilities, not merely on the verbal description “99% accurate.” An overall 99% prediction accuracy does not, by itself, imply 99% accuracy conditional on *each* choice. The two conditional probabilities above are additional assumptions, as in the reference article’s calculation.

More generally, write

\[
q_B=P(\text{full}\mid B),\qquad q_T=P(\text{full}\mid T).
\]

Then

\[
V(B)=1{,}000{,}000q_B,\qquad
V(T)=1{,}000+1{,}000{,}000q_T.
\]

One-boxing is favored exactly when

\[
q_B-q_T>0.001.
\]

Thus EDT’s recommendation is not unconditional: it depends on how informative the choice is and on the payoffs and utilities. If the correlation is weak enough, the extra $1,000 can outweigh the evidential advantage of one-boxing.

The underlying philosophical dispute is sharpened by the fact that both parties can accept the same probability distribution. The evidentialist asks which choice is associated with the better outcome. The causal theorist asks what difference the choice itself would make, given the already settled contents.

## 4. Correlated decisions: the twin prisoner’s dilemma

Now suppose Aomame plays a prisoner’s dilemma against a psychological twin in another room. Her payoffs are:

| Aomame | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | $5 | $0 |
| Defect | $10 | $1 |

For either fixed choice of the twin, defection pays Aomame more. But suppose each person’s decision is perfect evidence of the other’s:

\[
P(\text{twin cooperates}\mid C)=1,\qquad
P(\text{twin cooperates}\mid D)=0.
\]

Then \(V(C)=\$5\) and \(V(D)=\$1\), so EDT recommends cooperation. Her cooperation need not *cause* the twin’s cooperation. Both may instead result from their shared reasoning and circumstances.

Again, the strength of the correlation matters. Let

\[
p_C=P(\text{twin cooperates}\mid C),\qquad
p_D=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5p_C,\qquad
V(D)=10p_D+1(1-p_D)=1+9p_D.
\]

Cooperation is recommended only if \(5p_C>1+9p_D\). If the twin is already almost certain to cooperate regardless of what Aomame’s action indicates—for example, \(p_C=p_D=0.9\)—defection has the greater evidential value.

This illustrates a practical constraint on applying EDT: resemblance or common interests alone do not establish the required conditional probabilities. One must model the dependency, not simply announce that similar agents will make the same choice.

## 5. The “managing the news” objection

A standard criticism is that EDT can mistake good evidence for a good way to produce results. David Lewis called its prescription an irrational policy of “managing the news”; James Joyce emphasized that agents normally act for their causal efficacy rather than their auspiciousness.

A stylized smoking case makes the objection vivid. Suppose a hidden genetic factor \(G\) both makes people want to smoke and strongly predisposes them to a disease. Smoking itself gives a small pleasure and, by hypothesis, has no causal effect on the disease. Let

\[
P(\text{disease}\mid S)=0.8,\qquad
P(\text{disease}\mid N)=0.2,
\]

where \(S\) is smoking and \(N\) is not smoking. Assign a utility loss of 100 for disease and a benefit of 1 for smoking. Then

\[
V(S)=1-100(0.8)=-79,\qquad
V(N)=-100(0.2)=-20.
\]

EDT, using these probabilities, recommends not smoking. Yet if the hidden factor is already fixed and smoking does not affect disease, a causal theorist says smoking gains the pleasure without changing the risk.

This is an artificial example, not a claim about the actual health effects of smoking. Its purpose is to expose the issue: should an action be penalized because it is evidence of an unfortunate condition it does not cause?

The reference article states the criticism but does not settle it. One possible evidentialist response is that the agent should condition on all relevant evidence already available. If the agent knows their genetic status, or knows enough about their desire to smoke that the eventual act provides no further information about disease risk, the evidential association may disappear. For example, if

\[
P(\text{disease}\mid K,S)=P(\text{disease}\mid K,N),
\]

then smoking’s small benefit makes it preferable in this toy model.

That response is conditional, not a general refutation of the objection. The agent may not know the hidden factor, and the action may remain informative even after conditioning on everything currently known. In that case EDT’s basic formula retains the evidential penalty. Whether that is a virtue or a mistake is part of the philosophical disagreement.

## 6. Building a usable model

The reference article gives the central formula and examples, but leaves some modeling questions open. The following is an operational interpretation, not an extra theorem of EDT.

First, specify **the decision point and evidence** \(K\). Include observations already made, known commitments, the available options, and any information about how the other participants or predictors work. Do not condition on the candidate action as if it had already occurred; it is added separately in each evaluation.

Second, specify the **action variable and its alternatives**. “Take the pill,” “refuse the pill,” and “flip a coin and follow its result” may be three different actions. Whether randomization changes evidential correlations depends on how the randomizer is implemented and what other agents or predictors know about it.

Third, construct a joint probability model for actions and relevant states. One can often do this by specifying prior probabilities and likelihoods \(P(A=a\mid s,K)\), then applying Bayes’ rule. The likelihood is not a claim that the state makes the agent act against their will; it represents the model’s expectations about how the agent acts in different circumstances.

Fourth, define outcomes and utilities broadly enough to capture the whole decision. An action can be evidence of a favorable state and simultaneously cause harm. Both considerations belong in the calculation.

Finally, compute every conditional expectation using the **same background model**, inspect the dependence assumptions, and compare the results. Sensitivity analysis is especially valuable: if a recommendation reverses when a conditional probability changes slightly, the uncertainty about that probability is decision-relevant.

A difficulty arises if a fully specified model assigns \(P(A=a\mid K)=0\) to an available alternative. Ordinary conditional probability then does not determine \(P(O\mid K,A=a)\). This can happen if the agent models their own decision as perfectly predictable. The basic EDT formula does not by itself say what to do.

A reasonable practical proposal is to use a carefully specified model in which each genuinely considered option has positive probability—for example, a model containing uncertainty about the agent’s deliberation—and examine the conditional values as those probabilities become small. This is not guaranteed to produce a unique answer: different ways of approaching a zero-probability action can yield different limits. Where that happens, the model needs further assumptions, and the recommendation should be reported as unresolved rather than treated as a consequence of the simple formula.

## 7. Actions, policies, and repeated choices

Sometimes the object of choice is not a single act but a **policy**: a rule specifying what the agent will do in each possible information state. If \(\pi\) is such a policy, a natural evidential extension is

\[
V_K(\pi)=\mathbb E[u(\text{entire history})\mid K,\Pi=\pi],
\]

where \(\Pi\) represents the policy actually adopted. This is an operational extension of the source’s action formula. It requires a probability model in which policy adoption itself can be evidence about predictors, other agents, and future circumstances.

The distinction matters in repeated or sequential decisions. A predictor might forecast the agent’s policy rather than a particular move. A psychological twin might share a rule such as “cooperate with sufficiently similar players,” without being guaranteed to match every isolated action. Conditioning on adopting that rule can therefore give different probabilities from conditioning on a single move.

Policy evaluation must also include all branches of the policy and the total consequences across time. If a policy instructs an agent to accept a bet at several possible awakenings, its value depends on which awakenings occur, how often the bet is offered, and whether payoffs are paid per awakening or per experiment. Treating each occurrence in isolation may miss the cost of the complete strategy.

This is pertinent to **Sleeping Beauty**, where an agent’s number of awakenings depends on a coin toss and memory is manipulated. The reference article notes arguments that EDT can help with certain Dutch-book concerns about assigning probability \(1/2\) to heads, but also notes Conitzer’s argument that such “halfer” evidentialists can still be Dutch-booked. There is no general resolution in the article. To assess a particular betting arrangement, one must specify the credence model, the offers, the number of payments, and the allowed policy. “Use EDT” alone does not supply those details.

A related issue is dynamic consistency. A policy that looks best before new information arrives need not coincide with the act that looks best after conditioning on later information. Whether the agent can commit in advance, and whether commitment itself changes the evidence, are substantive features of the case.

## 8. What the theory does—and does not—promise

EDT does not guarantee a good outcome in each individual case. A one-boxer can encounter an inaccurate predictor and receive nothing; a cooperator can face a defecting twin. The prescription is to maximize *expected* utility according to the agent’s conditional probabilities.

Nor does the theory automatically make correlated agents cooperate, favor every predictive association, or override causal knowledge. Its conclusions follow from a combination of utilities, available actions, background evidence, and a joint distribution. Change any of these and the recommendation may change.

Finally, the source mentions an argument sometimes called the **evidentialist’s wager**: even someone uncertain that EDT is correct might give it substantial practical weight because evidential dependencies can involve many correlated decision-makers and hence large stakes. This is an argument within moral or decision-theoretic uncertainty, not a derivation of EDT’s rule. Its force depends on how uncertainty across theories is handled and on the magnitudes and comparisons of their stakes.

## Conclusion

EDT evaluates an action by asking what outcomes should be expected **conditional on that action occurring**. Its distinctive commitment is to count an action’s evidential links to outcomes, including links to earlier predictions and other agents’ correlated choices, as well as its causal effects.

The method is precise once its probability model and utilities are specified. The difficult work lies in specifying them: identifying what is already known, distinguishing observation from intervention, modeling correlations honestly, and deciding how to handle policies and zero-probability alternatives. Whether evidential value is the right guide to action remains contested, but the rule provides a clear framework for locating exactly where that contest matters.

## References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.