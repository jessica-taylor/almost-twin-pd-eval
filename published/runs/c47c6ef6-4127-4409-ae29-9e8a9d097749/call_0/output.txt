# Evidential decision theory: choosing what would be good news

A decision can be informative as well as effective. If I choose to carry an umbrella, my choice may be evidence that rain is likely: perhaps I saw a forecast that you did not. If an expert predicts my behavior, my eventual choice may also be evidence about what the expert predicted earlier.

Evidential decision theory, or **EDT**, takes this informational aspect of action as the basis for choice. It recommends an action whose occurrence would be the best news about how the world is going, as measured by expected utility. This can differ from choosing the action that would *cause* the best outcome. The distinction matters when an action is correlated with something it does not cause: a prediction already made, a hidden condition, or another agent’s simultaneous decision.

The central rule is simple. Applying it requires care about what the agent knows, what probabilities are conditioned on, and whether the alternatives are individual acts or complete policies. Some of those modeling choices are not settled by the rule itself. This essay presents the basic theory described in the reference article, then develops operational proposals for those less settled cases.

## 1. The basic calculation

Suppose an agent is considering actions \(a\) in a set \(\mathcal A\). Let \(K\) represent everything the agent currently knows, and let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive possible outcomes. Assign each outcome a utility \(u(O_j)\), representing how much the agent values it.

For an action \(a\), its **evidential value** is

\[
V_K(a)=\sum_{j=1}^{n}P(O_j\mid K,a)\,u(O_j).
\]

EDT recommends any action maximizing this quantity:

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}V_K(a).
\]

Equivalently, if utility is a random variable \(U\),

\[
V_K(a)=\mathbb E[U\mid K,A=a],
\]

where \(A\) is the agent’s action. The utility must cover everything the agent cares about: money, risk, other people’s welfare, moral costs, and so on. Monetary payoffs can stand in for utility in simple examples, but only when their marginal value and other consequences are appropriately represented.

The phrase “best news” is a mnemonic, not a recommendation to seek pleasant reports. The relevant news is the true proposition that the action occurs, and the relevant value concerns the *actual outcome*, including the consequences of that action. If learning that I will take a medicine tells me that I am ill, the action’s evidential value incorporates both the bad news about illness and any benefit or cost of the medicine.

Conditioning on an action can change beliefs about an outcome in more than one way:

1. **Causation:** taking a medicine changes the probability of recovery.
2. **Common causes:** an illness makes both taking medicine and poor health more likely.
3. **Prediction or similarity:** a predictor’s earlier choice, or a twin’s simultaneous choice, is correlated with the agent’s action.

EDT uses the resulting conditional probability in each case. It does not require every dependency to be causal. Nor does it imply that an action physically changes the past merely because the action is evidence about the past.

### Conditioning is not wishing

A useful application begins with a joint probability model for actions and outcomes. One does not first decide what would be desirable and then stipulate that it is probable given the preferred act. If the model says that an action is unlikely to be associated with a favorable outcome, EDT must use that unfavorable conditional distribution.

Likewise, all probabilities are conditional on the same available information \(K\). Information actually possessed by the agent should not be hidden in one calculation and revealed in another merely to generate a desired answer.

## 2. The contrast with causal decision theory

Causal decision theory, or CDT, evaluates an action by what would happen *if the agent were to perform it*, understood in a causal-counterfactual sense. In a suitable causal model one often writes this as

\[
C_K(a)=\sum_j P(O_j\mid K,\operatorname{do}(A=a))\,u(O_j).
\]

The intervention notation \(\operatorname{do}(A=a)\) represents setting the action to \(a\), rather than merely learning that \(A=a\). In a structural causal model, this typically cuts the ordinary causal arrows into \(A\) while preserving the mechanisms by which \(A\) affects its consequences. The reference article expresses the causal alternative using probabilities of counterfactuals; intervention notation is a useful formalization in appropriate models, though it does not exhaust every formulation of CDT.

The distinction can be illustrated by a hidden condition \(H\) that influences both action and outcome:

\[
H\longrightarrow A,\qquad H\longrightarrow O,\qquad A\longrightarrow O.
\]

Observing \(A=a\) can change the probability assigned to \(H\). Intervening to set \(A=a\) need not change it. Consequently,

\[
P(O\mid K,A=a)
\quad\text{and}\quad
P(O\mid K,\operatorname{do}(A=a))
\]

may differ.

When there are no relevant unblocked common causes and the causal model has the usual identification properties, these distributions can coincide. Then EDT and CDT give the same ranking. Their disagreement is not about whether actions have consequences; both theories can incorporate causal effects. It is about whether noncausal evidence supplied by an action belongs in the decision calculation.

## 3. Newcomb’s problem

The reference article’s central example is Newcomb’s problem. A predictor has already placed either \$1 million or nothing in an opaque box \(B\). A transparent box \(A\) contains \$1,000. The predictor filled \(B\) if it predicted that the player would take only \(B\), and left it empty if it predicted that the player would take both boxes.

Suppose the player’s probabilities satisfy

\[
P(B\text{ full}\mid\text{one-box})=0.99,\qquad
P(B\text{ full}\mid\text{two-box})=0.01.
\]

Assuming utility is linear in these monetary amounts, EDT calculates

\[
\begin{aligned}
V(\text{one-box})
&=0.99(\$1{,}000{,}000)+0.01(\$0)
=\$990{,}000,\\
V(\text{two-box})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\end{aligned}
\]

EDT therefore recommends taking only \(B\). Doing so is strong evidence that the predictor filled it.

The numbers deserve a qualification. Saying only that the predictor is “99% accurate” overall does not by itself establish both displayed conditional probabilities. Those probabilities also depend on how often the actions occur and on the pattern of prediction errors. The calculation assumes the relevant *action-conditional* accuracy rates.

The causal argument for two-boxing is different. At the moment of choice, the predictor has already acted. If taking both boxes cannot change the contents of \(B\), then, holding those contents fixed, taking both gives \$1,000 more than taking only \(B\). CDT accordingly recommends two-boxing under the standard causal setup.

EDT’s one-boxer need not believe that choosing now sends a causal signal backward in time. The point is that the agent’s choice and the earlier prediction can both depend on features of the agent that the predictor has assessed. Conditioning on the choice supplies evidence about those features and hence about the earlier prediction.

The result also depends on not already knowing the contents of \(B\). If the player has seen that \(B\) is full, and the predictor’s decision is fixed, one-boxing no longer supplies useful news about that fact. If taking the extra \$1,000 has no other adverse effects, both theories can recommend taking both boxes. The theory is applied to the agent’s *actual information*, not to a stock description of the problem.

## 4. Correlated agents: the twin prisoner’s dilemma

Now consider an agent playing a prisoner’s dilemma against a psychological twin. They are in separate rooms and cannot communicate. Each receives \$5 if both cooperate and \$1 if both defect. A defector facing a cooperator receives \$10; a cooperator facing a defector receives nothing.

In the idealized case described in the reference article, the twin’s reasoning is perfectly correlated with the agent’s:

\[
P(\text{twin cooperates}\mid\text{I cooperate})=1,
\]
\[
P(\text{twin cooperates}\mid\text{I defect})=0.
\]

Thus

\[
V(\text{cooperate})=1(5)+0(0)=5,
\qquad
V(\text{defect})=0(10)+1(1)=1.
\]

EDT recommends cooperation. Again, the recommendation does not require a signal between the rooms. The agent’s action is evidence of the twin’s action because their decision processes are correlated.

Perfect correlation is not necessary. Write

\[
p=P(\text{twin cooperates}\mid\text{I cooperate}),\qquad
q=P(\text{twin cooperates}\mid\text{I defect}).
\]

Then

\[
V(\text{cooperate})=5p,\qquad
V(\text{defect})=10q+1(1-q)=1+9q.
\]

Cooperation is favored exactly when

\[
5p>1+9q.
\]

For example, \(p=0.9\) and \(q=0.1\) yield values \(4.5\) and \(1.9\), respectively. But similarity alone is not enough: if both conditional probabilities are about \(0.7\), then defecting has greater evidential value. The important question is how much the probability of the other’s cooperation changes *conditional on one’s own action*.

This is why an EDT recommendation cannot be read directly from a payoff matrix. It also requires a probability model for the other player. Nor does EDT automatically recommend cooperation in ordinary prisoner’s dilemmas: if the other player’s action is independent of yours given your information, the usual dominance of defection remains.

## 5. The “bad news” objection

The most familiar criticism is that EDT can appear to recommend managing evidence rather than improving the world. Lewis called it an irrational policy of “managing the news”; Joyce emphasized the causal efficacy of actions. A stylized medical example makes the concern concrete.

Suppose a genetic condition causes both a craving for a particular drink and an elevated probability of disease. The drink itself has no effect on disease. Before the agent knows whether they have the condition, imagine the model assigns

\[
P(\text{disease}\mid\text{drink})=0.8,\qquad
P(\text{disease}\mid\text{abstain})=0.2.
\]

Let disease have utility \(-100\), and let drinking provide an additional benefit of \(1\). Then, ignoring other outcomes,

\[
V(\text{drink})=-79,\qquad
V(\text{abstain})=-20.
\]

EDT recommends abstaining. Yet, by hypothesis, abstaining cannot remove the genetic condition or prevent the disease. A causal theorist can regard the recommendation as sacrificing a benefit merely to make the agent’s action a favorable symptom.

An evidentialist response is that the action is not being chosen to manipulate a report; it is evaluated as part of a pattern of outcomes. Nevertheless, the example exposes a genuine philosophical dispute. The formula alone does not establish that correlations with hidden conditions should have decision-making significance when the agent cannot causally alter those conditions.

There is also a modeling issue. Does the agent already know whether they crave the drink? If so, craving belongs in \(K\). If craving screens off the relevant association—so that, for a fixed known craving state \(h\),

\[
P(\text{disease}\mid K,h,\text{drink})
=
P(\text{disease}\mid K,h,\text{abstain}),
\]

then EDT sees no disease-related evidential advantage to abstaining. It recommends the drink if its benefit is positive. But screening off cannot simply be assumed: the act may still reveal additional information about the hidden condition. The lesson is not that every “bad news” objection disappears, but that the information available at the decision point is essential to assessing it.

## 6. Acts, policies, and sequential decisions

The reference article states EDT primarily as a rule for evaluating actions. In unfamiliar cases, an agent may instead be choosing a **policy**: a rule specifying what to do under each possible observation. For instance, a policy might say, “Take the medicine if the test is positive; otherwise do not.”

A natural extension, which is an operational proposal rather than a further rule established by the article, is

\[
V_K(\pi)=\mathbb E[U\mid K,\Pi=\pi],
\]

where \(\Pi\) is the policy adopted and the outcomes include those generated when it is followed. This is useful when predictors or other agents respond to the agent’s policy rather than merely to its last observable act. A firm deciding on a refund policy, for example, should model how customers’ expectations and behavior are correlated with the policy, as well as the refunds paid.

Policy evaluation and act evaluation need not agree. Before receiving a test result, the agent can compare complete policies. After receiving it, the agent can compare the acts available at that particular information state. Conditioning on a policy and conditioning on a later action are different operations; they can reveal different information about the world.

A practical procedure is therefore:

1. **Fix the decision point.** Specify what has already happened, what the agent knows, and which choices remain available.
2. **Choose the alternatives.** Decide whether they are immediate acts, commitments, or policies for future information states.
3. **Model dependencies.** Include relevant causal effects and correlations with predictors, other agents, and hidden conditions.
4. **Assign utilities.** Include the full outcomes the agent values, not just an easily measured component.
5. **Condition on each alternative.** Calculate its expected utility using the same background information.
6. **Compare and check robustness.** Examine whether plausible changes in conditional probabilities change the ranking.

For sequential problems, a further issue arises: a policy preferred initially may prescribe an act that the agent later rejects after updating on new information. Whether one should commit in advance, re-optimize later, or use a particular sophisticated planning rule is not determined just by the one-step formula. The physical availability and cost of commitment must be modeled, and different extensions of EDT may treat such cases differently.

## 7. Zero probabilities and the model of choice

The expression \(P(O\mid K,A=a)\) is undefined by the elementary ratio formula when \(P(A=a\mid K)=0\). Yet a deliberating agent may regard their eventual choice as predictable, or even believe with certainty that they will choose one option. How can they evaluate another?

The source’s formula does not settle this question. One possible operational approach is to use a family of probability models in which each feasible act has a small positive probability and examine the limit as that probability tends to zero. But this works only if a stable, justified limit exists. Different ways of assigning the small probabilities can produce different conditional distributions and hence different recommendations. A more elaborate conditional probability system can instead specify conditionals for zero-probability alternatives directly, but those specifications require justification.

This problem is connected to a broader issue: probabilities over one’s own actions are not automatically available just because one can list actions. A model should explain what uncertainty those probabilities represent—for example, uncertainty about one’s dispositions, information, deliberation, or randomization—and why it gives the stated correlations with outcomes. Newcomb calculations are informative only to the extent that such a model supports their conditional probabilities.

Randomization itself must also be modeled rather than treated as a magic escape from prediction. If an agent flips a coin, is the predictor informed about the result, or only about the randomization procedure? Do different coin results correlate with the predictor’s earlier choice? EDT evaluates each available act or policy using the probabilities appropriate to the stated arrangement.

## 8. Further applications and limits

The reference article mentions the Sleeping Beauty problem, where an agent is awakened under different schedules depending on a coin toss and may not know which awakening she occupies. EDT has been proposed in connection with betting and Dutch-book arguments about whether her credence in heads should be one-half or one-third. The article also reports Conitzer’s argument that adopting EDT does not, by itself, protect halfers from every Dutch book.

The cautious lesson is methodological. In such cases one must specify not just a credence, but also the payment schedule, what the agent knows at each awakening, whether bets are offered once or repeatedly, and what policy is being evaluated. The brief description in the source does not establish a general EDT solution to the dispute.

The article also notes an argument that EDT may deserve practical attention even from someone uncertain whether it is the correct decision theory: correlated decision-makers can make the stakes under an evidential analysis large. That is a possible consideration in choice under normative uncertainty, not a proof of EDT. How to compare recommendations from competing theories, and whether their value scales can be combined, requires further assumptions.

## Conclusion

EDT evaluates an alternative by asking how desirable the world is expected to be *conditional on that alternative occurring*. Its distinctive feature is that the conditioning can include evidence about predictors, hidden conditions, and correlated agents, not merely effects caused by the action.

That feature explains both its appeal in Newcomb-like problems and the criticism that it can mistake good news for effective action. To apply EDT responsibly, one must specify the agent’s information, a defensible joint probability model, the available acts or policies, and utilities for complete outcomes. Where conditional probabilities are undefined or sequential choices conflict, further assumptions are needed; the basic formula alone does not decide the case.

## References

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688), licensed CC BY-SA 4.0.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, Vincent. “A Dutch Book Against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.