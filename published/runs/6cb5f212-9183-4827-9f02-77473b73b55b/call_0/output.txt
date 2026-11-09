# Evidential decision theory: choosing the best news

A decision can be good in two different senses. It can *bring about* a desirable result, or it can be a sign that a desirable result is likely. Ordinarily these go together: learning that you took an umbrella is good news about whether you stayed dry partly because the umbrella helped keep you dry. But they can come apart when an action is correlated with facts it does not cause.

Evidential decision theory, or **EDT**, evaluates an action by asking how desirable the world would be, on average, conditional on the agent taking that action. In Arif Ahmed’s formulation, the idea is to “do what you most want to learn that you will do.” Causal decision theory, or **CDT**, instead evaluates an action through the outcomes it would causally produce. The difference matters especially when another agent predicts your choice, when your choice reveals something about your circumstances, or when other decision-makers reason in ways correlated with yours.

The basic EDT calculation is simple. Applying it requires care: one must specify the agent’s information, utilities, and probabilities, including the relationship between contemplated actions and the rest of the world. The reference article gives the central rule and several examples, but leaves some issues—including how to evaluate probability-zero actions and how to apply the rule to entire policies—open. I will distinguish the rule from operational proposals for those cases.

## 1. The evidential rule

Suppose an agent knows background information \(E\), must choose among available acts \(a\in\mathcal A\), and cares about outcomes \(O_1,\ldots,O_n\). Let \(u(O_j)\) be the utility of outcome \(O_j\), and let \(P\) represent the agent’s probabilities at the decision point. EDT assigns act \(a\) the value

\[
V_E(a)
=
\sum_{j=1}^{n} P(O_j\mid E,a)\,u(O_j).
\]

The prescription is to choose an act maximizing \(V_E(a)\). More generally, if utility depends directly on both the act and a state \(s\), write

\[
V_E(a)
=
\sum_s P(s\mid E,a)\,u(a,s)
=
\mathbb E[u(a,S)\mid E,A=a].
\]

Here \(A\) is the random variable representing the act the agent in fact takes. The utilities should include everything the agent values: money, costs of effort, effects on others if relevant, and so on. Money figures can stand in for utility when, for example, the agent is assumed to value the amounts linearly.

The important term is \(P(s\mid E,a)\), not merely \(P(s\mid E)\). Learning that the agent acts in one way rather than another may change the probability of a state. By Bayes’ rule, when the relevant probabilities are positive,

\[
P(s\mid E,a)
=
\frac{P(a\mid E,s)P(s\mid E)}
{\sum_{s'}P(a\mid E,s')P(s'\mid E)}.
\]

Thus an act is evidence for a state to the extent that the act is more probable in that state than in alternatives. No particular causal direction is built into this formula. The state might influence the action; the action might influence the state; both might have a common cause; or the dependence might arise from a predictor’s knowledge of the agent.

This explains EDT’s “news” metaphor. The agent compares the news “I take \(a\)” with the news “I take \(b\),” including all the differences in expected utility that those pieces of information imply. This is not a claim that merely hearing news changes the world. It is a rule for choosing on the basis of what each possible choice indicates.

### When EDT and CDT agree

Suppose an action has no evidential connection to an uncertain pre-existing state: \(P(s\mid E,a)=P(s\mid E)\) for every available act. Then EDT evaluates each act using the same distribution over states:

\[
V_E(a)=\sum_s P(s\mid E)u(a,s).
\]

In a standard decision problem where the action’s causal effects on the outcome are represented correctly by \(u(a,s)\), CDT will often agree. Both might recommend buying insurance, taking an effective medicine, or carrying an umbrella. The controversy is not over whether consequences matter, but over which probability distribution should be used to assess them.

## 2. Conditioning is not intervention

A causal model provides a useful contrast. Let \(P(O\mid E,\operatorname{do}(a))\) denote the outcome distribution under an intervention that sets the action to \(a\), with the rest of the model evolving according to its causal rules. A simplified causal value is

\[
V^{\mathrm{causal}}_E(a)
=
\sum_j P(O_j\mid E,\operatorname{do}(a))u(O_j).
\]

This is one way to represent the counterfactual probabilities used by CDT; particular causal theories and models can differ in their treatment of counterfactuals. The essential contrast is that conditioning on an act preserves its evidential associations, whereas intervention can break associations caused by influences on the action.

For example, suppose a hidden disposition affects both an agent’s action and a predictor’s earlier forecast. Observing the action provides evidence about the disposition and hence the forecast. But an intervention that simply forces the action to a particular value need not change the disposition or the earlier forecast.

EDT therefore does not normally ask, “What would happen if this action were externally forced while everything causally prior stayed fixed?” It asks, “Given that this action is taken, what should I expect?” The answer can involve facts in the past or actions by distant people, without implying backward causation or a mysterious causal influence at a distance.

The distinction also prevents a common misunderstanding. If taking an action is evidence that an outcome has already been secured, EDT may favor it even though the action does not *make* the past outcome happen. Whether this is rational insight or an error is the philosophical dispute.

## 3. Newcomb’s problem: evidence about a prediction

A predictor has already filled an opaque box \(B\). If it predicted that you would take only \(B\), it put \$1 million inside; if it predicted that you would take both \(B\) and a transparent box \(A\), it left \(B\) empty. Box \(A\) visibly contains \$1,000. You choose either one box or both.

For the numerical version in the reference article, assume the relevant conditional probabilities are

\[
P(B\text{ full}\mid \text{one-box})=0.99,
\qquad
P(B\text{ full}\mid \text{two-box})=0.01.
\]

With linear utility for money, EDT obtains

\[
\begin{aligned}
V(\text{one-box})&=0.99(1{,}000{,}000)=\$990{,}000,\\
V(\text{two-box})&=0.01(1{,}001{,}000)+0.99(1{,}000)
=\$11{,}000.
\end{aligned}
\]

It recommends taking only \(B\).

The numerical assumptions deserve attention. An *overall* prediction accuracy of 99% alone does not automatically establish both conditional probabilities above; the error rates and the distribution of choices matter. For the calculation, one needs the conditional reliability stated, or a joint probability model from which it follows.

A causal argument gives the familiar opposing verdict. Once the predictor has acted, the content of \(B\) is fixed. For either possible content, taking both boxes yields \$1,000 more than taking only \(B\). In a causal model where the current act cannot affect the past filling, two-boxing dominates.

EDT does not deny that the extra \$1,000 is attractive holding the box’s contents fixed. It denies that holding those contents fixed gives the right evidential comparison. In the stipulated model, one-boxers are much more likely than two-boxers to face a full opaque box. The additional \$1,000 is outweighed by the difference between the conditional prospects.

This case illustrates both the appeal and the difficulty of EDT. It explains why people following the one-box recommendation can do very well against accurate predictors. But it also invites the objection that a present action should not be selected merely because it is associated with a favorable past.

## 4. Correlated decision-makers

The reference article also considers a prisoner’s dilemma played against a psychological twin. Each player receives \$5 if both cooperate and \$1 if both defect. A defector facing a cooperator receives \$10; a cooperator facing a defector receives nothing.

If the twin’s decision is perfectly correlated with yours, then

\[
P(\text{twin cooperates}\mid \text{you cooperate})=1,\qquad
P(\text{twin cooperates}\mid \text{you defect})=0.
\]

Consequently,

\[
V(\text{cooperate})=5,\qquad V(\text{defect})=1.
\]

EDT recommends cooperation, even if there is no causal influence from your choice to the twin’s.

Perfect similarity is not essential. Let

\[
q_C=P(\text{twin cooperates}\mid \text{you cooperate}),\qquad
q_D=P(\text{twin cooperates}\mid \text{you defect}).
\]

Then

\[
V(C)=5q_C,\qquad V(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is favored exactly when

\[
5q_C>1+9q_D.
\]

This condition makes the dependence doing the work explicit. If the twin is almost certain to cooperate regardless of what your choice indicates, then defecting may be better. If your cooperation is strong evidence of theirs and your defection strong evidence of theirs, cooperation may be better.

One should not infer such correlations simply because cooperation would be mutually beneficial. Similar reasoning, shared information, common training, and observation of one another are possible reasons for dependence; whether they support the required conditional probabilities is an empirical and modeling question. Nor does EDT automatically recommend cooperation in every prisoner’s dilemma.

## 5. The objection: managing the news

EDT’s most persistent criticism is that evidence of a good outcome is not the same as a means of producing it. David Lewis described the view as an irrational policy of “managing the news”; James Joyce similarly argues that rational action should be guided by causal efficacy rather than auspiciousness.

Consider a simplified “smoking lesion” model. A hidden lesion makes a person both inclined to smoke and likely to develop a disease. Suppose, for illustration, that smoking has no effect at all on the disease but provides one unit of enjoyment. Disease costs 100 utility units, and at the decision point

\[
P(\text{disease}\mid \text{smoke})=0.10,\qquad
P(\text{disease}\mid \text{abstain})=0.01.
\]

The evidential values are

\[
V(\text{smoke})=1-100(0.10)=-9,\qquad
V(\text{abstain})=-100(0.01)=-1.
\]

EDT, using these probabilities, recommends abstention. Yet by hypothesis, abstaining does not prevent the disease. A causal theorist says that the agent gives up enjoyment for no causal benefit.

An evidentialist can answer that abstention is still the act associated with a better expected state of affairs. The critic replies that the agent is selecting a symptom of health rather than a cause of health. The example exposes the normative disagreement rather than settling it.

It also shows why background information matters. Perhaps the apparent correlation between smoking and disease is explained by a craving that the agent can already observe. If the agent’s evidence includes that craving and, conditional on it, the further act of smoking supplies no information about the lesion, then the probabilities for smoking and abstaining may become equal. EDT would then favor the enjoyable act. This is sometimes called a *screening-off* response.

But screening off cannot be assumed in every case. The agent might not know all relevant features of their own psychology, or the eventual action might remain informative even after all currently available evidence is included. Thus “condition on what you already know” is a crucial instruction, not a guarantee that EDT and CDT will agree.

## 6. Applying EDT to unfamiliar cases

A practical calculation can be organized as follows.

1. **Specify the decision point and evidence.** Include what the agent actually knows or observes, not facts available only to an outside analyst. The relevant probabilities are conditional on this evidence.
2. **List feasible acts.** Distinguish actions available now from plans the agent could have committed to earlier.
3. **Define outcomes and utilities.** Include action costs and all valued consequences; avoid treating a convenient monetary payoff as utility unless that is justified.
4. **Construct a joint probability model.** Ask how the act, hidden states, predictions, and other agents’ choices are related. Draw a causal diagram if useful, but retain all evidential dependencies relevant to conditioning.
5. **Calculate \(P(O\mid E,a)\) for each act.** Check whether reported predictor accuracy or correlations really imply the conditional probabilities used.
6. **Compute and compare expected utilities.** If the result is sensitive to uncertain correlations or utilities, report the thresholds rather than presenting a fragile verdict as certain.

For example, if an accurate predictor gives a reward \(M\) for predicting one-boxing and a transparent box contains \(b\), with conditional full-box probabilities \(p\) for one-boxing and \(r\) for two-boxing, then

\[
V(\text{one})=pM,\qquad
V(\text{two})=rM+b.
\]

EDT favors one box when \((p-r)M>b\). This formula isolates what matters: the **difference in conditional probabilities**, scaled by the reward, must exceed the extra amount available from taking both.

The probabilities themselves can be hard to justify. An agent who already knows exactly how a deterministic decision procedure will behave may assign probability one to one act and zero to another. The decision rule, however, asks for the value of each alternative. This is not merely a computational inconvenience: ordinary conditioning on \(P(a\mid E)=0\) is undefined.

## 7. Zero-probability acts and policies

The reference article states the conditional-probability rule but does not settle what to do when an alternative has probability zero. There is no unique extension supplied by elementary probability theory.

One operational proposal is to use a specified *trembling* model: assign each act a small positive probability, calculate its conditional value, and examine the limit as the tremble probability tends to zero. But this works only if the model says how the tremble relates to predictors and other agents. A random motor slip that a predictor could not anticipate may have different evidential significance from uncertainty about the agent’s reasoning. Different limiting models can therefore produce different answers. A limit is not an answer until its perturbation has been justified.

Another approach is to retain uncertainty about one’s own reasoning until the evaluation is complete, or to use a richer theory of conditional probabilities that explicitly assigns values to zero-probability conditions. Both are additional modeling commitments, not consequences of the basic EDT formula.

Policy choice raises a related issue. A policy \(\pi\) maps observations or histories \(h\) to actions \(\pi(h)\). One natural evidential extension is

\[
V_E(\pi)=\mathbb E[U(\text{whole outcome})\mid E,\Pi=\pi],
\]

where \(\Pi\) is the policy actually adopted. This is useful when a predictor, an institution, or other agents respond to—or can infer—the agent’s general disposition rather than just one isolated act. The outcome must include the entire sequence of payoffs and costs.

This proposal requires a probability model over policies. It also differs from evaluating each local action as though it were chosen independently. A plan adopted before receiving information may prescribe an action that, once new information arrives, the agent would not select by applying the local EDT rule anew. Whether to follow the original plan, revise it, or seek commitment depends on the available commitments and on the theory used for sequential choice. Policy EDT is therefore not automatically interchangeable with repeated act-by-act EDT.

## 8. Further questions

The reference article notes an application to the Sleeping Beauty problem and Dutch-book arguments: some argue that adopting EDT can help a “halfer” avoid certain betting vulnerabilities, while Vincent Conitzer argues that Dutch books remain possible under his setup. The lesson is not that EDT by itself resolves questions about self-locating probability or betting. Results depend on how awakenings, bets, information, and repeated decisions are modeled.

The article also mentions an argument sometimes called the *evidentialist’s wager*: even someone uncertain whether EDT is correct might give it substantial weight because correlated decisions can have unusually large stakes. That is a proposal about decision-making under uncertainty between theories, not part of the basic EDT formula. Its force depends on how such theories are compared and on whether the purported correlations and stakes are credible.

## Conclusion

EDT evaluates an act by the expected utility conditional on taking it. Its distinctive feature is that it counts an action’s evidential relationships with the rest of the world, including predictions and correlated choices, whether or not the action causes those facts.

This makes EDT powerful in cases such as Newcomb’s problem and the twin prisoner’s dilemma, but vulnerable to the charge that it confuses good signs with effective means. To apply it responsibly, specify the evidence, the joint probability model, and the utilities; then examine which dependencies actually support the verdict. For zero-probability alternatives and sequential policies, further assumptions are needed, and those assumptions should be made explicit.

### References

- Ahmed, A. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, A., and Harper, W. L. “Counterfactuals and Two Kinds of Expected Utility,” 1976.
- Lewis, D. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, V. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.
- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” reference revision.