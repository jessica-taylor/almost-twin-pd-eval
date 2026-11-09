# Evidential Decision Theory: Choosing Good News

Suppose you must choose an action whose consequences depend on facts you do not know. Ordinarily, you estimate what each action will accomplish and choose accordingly. Evidential decision theory, or **EDT**, proposes a closely related but distinctive test: ask what each possible action would tell you about the world, and choose the action associated with the best expected outcome.

The slogan is “do what you most want to learn that you will do.” It is not merely advice to seek reassuring information. The action is part of the outcome being evaluated, and its ordinary causal effects matter. But an action may also be evidence about facts it does not cause: an earlier prediction, another agent’s decision, or a hidden feature of the chooser. EDT counts those evidential relationships when estimating outcomes.

This makes EDT agree with familiar decision-making in many cases while producing controversial answers in others. The central question is whether a rational choice should be evaluated by the outcomes *conditional on making it*, or by the outcomes that making it would *cause*. The reference article presents EDT as the first approach and causal decision theory, or CDT, as the second.

## The basic calculation

Let \(K\) represent everything the agent knows when deciding. Let \(\mathcal A\) be the available actions, and let \(O_1,O_2,\ldots\) be mutually exclusive, exhaustive outcomes. If \(u(O_j)\) is the utility of outcome \(O_j\), EDT assigns action \(a\) the value

\[
V_{\mathrm E}(a\mid K)
 = \sum_j P(O_j\mid A=a,K)\,u(O_j),
\]

where \(A\) is the random variable representing the action actually taken. It recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A} V_{\mathrm E}(a\mid K).
\]

Equivalently, with a utility random variable \(U\),

\[
V_{\mathrm E}(a\mid K)=\mathbb E[U\mid A=a,K].
\]

This is the reference article’s conditional expected-utility rule, with the agent’s background information made explicit. If outcomes are described without mentioning the action, one can instead write \(u(a,O_j)\) to ensure that action-specific costs and benefits are included.

The utility scale should represent the agent’s preferences over complete outcomes. Money is often used as a convenient illustration, but maximizing expected dollars assumes, at least over the relevant range, that utility is linear in money. If an agent is risk-averse or cares about other people, those considerations belong in \(u\), not in an afterthought.

The conditional probabilities are just as important as the utilities. In general,

\[
P(O_j\mid A=a,K)
=\frac{P(O_j,A=a\mid K)}{P(A=a\mid K)}
\]

when \(P(A=a\mid K)>0\). These are not probabilities calculated by pretending the action has no history. They describe a joint probabilistic model in which the agent’s action and the rest of the world can be statistically dependent.

For example, taking an umbrella may be evidence that rain is likely because the agent saw a forecast. Carrying the umbrella does not cause the forecast, but both the forecast and rain affect the conditional distribution associated with carrying it. If the agent already knows the forecast, however, that information belongs in \(K\); the calculation must not count the same evidence again as though it were newly discovered.

## Conditioning and causal counterfactuals

The reference contrasts EDT with a causal expected-utility rule. In one common causal-model formulation,

\[
V_{\mathrm C}(a\mid K)
 = \mathbb E[U\mid \operatorname{do}(A=a),K],
\]

where \(\operatorname{do}(A=a)\) represents an intervention that sets the action to \(a\). The precise interpretation of causal counterfactuals is contested, and the intervention notation is a modeling choice rather than a complete account of CDT. Its purpose here is to show the distinction.

Consider a hidden variable \(H\) that influences both the agent’s action and an outcome. Conditioning on \(A=a\) changes the distribution of \(H\), because learning the action provides evidence about it. Intervening to set \(A=a\), by contrast, ordinarily severs the causal influences into \(A\); it does not thereby change \(H\). Both calculations can retain effects flowing *out of* the action.

Schematically, when \(H\) is causally prior to the action,

\[
P(O\mid A=a,K)
 =\sum_h P(O\mid A=a,H=h,K)\,P(h\mid A=a,K),
\]

while an intervention model might yield

\[
P(O\mid \operatorname{do}(A=a),K)
 =\sum_h P(O\mid \operatorname{do}(A=a),H=h,K)\,P(h\mid K).
\]

The difference lies in how the action is related to the hidden state. If the action is appropriately randomized, so that it gives no additional evidence about \(H\), and the rest of the causal model is suitable, the two calculations can coincide. In that setting, EDT and CDT will often agree.

Neither calculation says that merely observing an action changes the past. EDT’s claim is instead that the action one actually takes can be evidence about the past. Its controversial step is treating the resulting conditional expectation as the correct guide to choice.

## Newcomb’s predictor

Newcomb’s problem makes the distinction vivid. A predictor has already filled an opaque box \(B\) with either \$1 million or nothing. A transparent box \(A\) contains \$1,000. The predictor put \$1 million in \(B\) if it predicted that the player would take only \(B\); otherwise it left \(B\) empty. The player chooses between taking only \(B\) and taking both boxes.

Assume, as in the reference’s numerical example, that

\[
P(B\text{ is full}\mid \text{one-box})=0.99
\]

and

\[
P(B\text{ is full}\mid \text{two-box})=0.01.
\]

With dollar-linear utility, the evidential values are

\[
V_{\mathrm E}(\text{one-box})
=0.99(\$1{,}000{,}000)=\$990{,}000
\]

and

\[
V_{\mathrm E}(\text{two-box})
=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=\$11{,}000.
\]

EDT therefore recommends one-boxing.

These conditional probabilities need care. Saying only that a predictor is “99% accurate” *overall* does not, by itself, entail 99% accuracy conditional on each possible choice. Accuracy could be unevenly distributed across one-boxers and two-boxers. The calculation requires the stated action-conditional probabilities or a more detailed model from which they follow.

A causal argument gives the opposite answer under the standard setup. The predictor has already made its prediction, and the opaque box’s contents are fixed. For either fixed content, taking both boxes gives exactly \$1,000 more than taking only \(B\). If the present action has no causal influence on the earlier prediction or box content, the causal value of two-boxing exceeds that of one-boxing by \$1,000.

The evidentialist does not need to say that one-boxing sends a signal backward in time. Rather, one-boxing is highly correlated with the earlier prediction, perhaps because the predictor studied the player’s disposition or reasoning. The causal theorist replies that, whatever the correlation, the player cannot now make the already-filled box fuller by choosing one box. The disagreement concerns which comparison is relevant to choice.

The result is also quantitative, not magical. Let

\[
p_1=P(B\text{ full}\mid \text{one-box}),\qquad
p_2=P(B\text{ full}\mid \text{two-box}).
\]

EDT one-boxes, on linear monetary utility, precisely when

\[
\$1{,}000{,}000(p_1-p_2)>\$1{,}000.
\]

A predictor need not be nearly perfect; the evidential advantage need only exceed the certain extra \$1,000.

## A correlated opponent

The twin prisoner’s dilemma illustrates evidence about another agent rather than an earlier prediction. Aomame and her psychological twin choose independently, without communication, between cooperation and defection. Their individual payoffs are:

| Aomame | Twin | Aomame’s payoff |
|---|---|---:|
| Cooperate | Cooperate | \$5 |
| Cooperate | Defect | \$0 |
| Defect | Cooperate | \$10 |
| Defect | Defect | \$1 |

If their reasoning is perfectly correlated, learning that Aomame cooperates would imply that her twin cooperates; learning that Aomame defects would imply that her twin defects. EDT then assigns cooperation value \$5 and defection value \$1, so recommends cooperation.

The conditional dependence, not mere similarity as a verbal description, does the work. Let

\[
q_C=P(\text{twin cooperates}\mid A=C,K),\qquad
q_D=P(\text{twin cooperates}\mid A=D,K).
\]

Then

\[
V_{\mathrm E}(C)=5q_C,\qquad
V_{\mathrm E}(D)=10q_D+1(1-q_D)=1+9q_D.
\]

Cooperation is recommended exactly when

\[
5q_C>1+9q_D.
\]

If the twin’s decision is independent of Aomame’s, then \(q_C=q_D=q\), and defection is better for every \(q\in[0,1]\). A correlation between decision-makers can therefore change the evidential verdict, but EDT does not automatically recommend cooperation in ordinary prisoner’s dilemmas.

Nor does “no communication” establish independence. Two agents may reach correlated decisions because of shared training, common evidence, or similar reasoning. Conversely, even very similar agents may use independent random devices, weakening the action-level correlation. The relevant probabilities must come from the actual model.

## Policies, information, and randomization

An action is a particular move at a decision point. A **policy** is a rule for choosing actions across possible information states. For example, a policy might say: cooperate if a test is positive and defect otherwise. If \(\pi\) is the policy actually followed and \(X\) is the later information observed, its realized action is \(A=\pi(X)\).

A natural extension of the EDT formula is to evaluate a candidate policy by

\[
V_{\mathrm E}(\pi\mid K)
 =\mathbb E[U\mid \Pi=\pi,K],
\]

where \(\Pi\) is a random variable for the policy actually adopted. This is an operational proposal consistent with the source’s basic conditional rule, not a fully specified policy theory supplied by the reference article. As with actions, the meaning of the conditional depends on a model of how policy adoption is correlated with other facts.

Policy evaluation is useful when others predict a standing rule, when decisions recur, or when a commitment changes later incentives. It also exposes a distinction between choosing a rule now and reconsidering an individual action later. The policy preferred ex ante need not always be the action preferred at every later information state under every way of modeling evidence. A model must say what is known at each point, whether a commitment is binding, and what evidence the later choice supplies. One should not assume that an attractive policy automatically settles every subsequent choice.

Randomization likewise needs an explicit model. Suppose an agent genuinely uses an independent coin with probability \(r\) of selecting \(C\). The decision to use that lottery is one act or policy; the later coin result is another event. Conditioning on the lottery’s adoption is not the same as conditioning on the eventual result.

This matters in the twin example. If the twins use independent coins, then observing Aomame’s coin result may provide little evidence about her twin’s result, even if their policies are identical. If they instead use the same public random seed, their realized actions may be strongly correlated. “Both randomize with probability \(r\)” is not enough to determine the joint distribution.

## The difficulty of assigning probabilities to one’s own choice

The formula requires \(P(O\mid A=a,K)\), but how can a deliberating agent assign probabilities to actions that are supposedly up to them? The reference gives the conditional rule without resolving every issue about self-prediction. Two difficulties deserve particular attention.

First, ordinary conditioning is undefined if \(P(A=a\mid K)=0\). An agent who is certain they will choose \(a_1\) cannot use the elementary ratio formula to evaluate \(a_2\), even if \(a_2\) remains physically available. Declaring an option impossible merely because one currently intends not to choose it risks making comparison circular.

A practical proposal is to build an explicit joint model in which each genuinely available candidate has positive probability, reflecting uncertainty about the factors or deliberative process determining the choice. One then computes the ordinary conditionals under that model. This is not automatically justified in every application: a decision-maker’s probability assignment to their own future act may itself be philosophically contentious. When positive probability is unavailable, another possible extension uses a carefully specified limiting family of positive-probability models. But different limits can give different answers, so a limit is an additional assumption, not a value uniquely dictated by EDT.

Second, the dependencies must survive conditioning on what the agent already knows. Suppose both action and outcome are correlated only because they depend on a known forecast. Once the forecast is included in \(K\), the action may supply no further evidence about the weather. Conversely, a predictor or twin may retain information about the agent’s decision process that the agent does not already know. Simply asserting either dependence or independence without a joint model can build the desired answer into the premises.

A useful discipline is therefore to specify:

1. **The information state:** What is known when the choice is made?
2. **The options:** Are these individual acts, randomized procedures, or policies?
3. **The outcomes and utilities:** What ultimately matters, including costs and risk?
4. **The joint distribution:** Why should each option be evidence about each relevant unknown?
5. **The conditional values:** Are the required conditioning events well-defined?
6. **Sensitivity:** Would the recommendation change under plausible alternative dependencies?

This procedure does not eliminate philosophical disagreement, but it makes clear where a recommendation comes from.

## The “bad news” objection

EDT’s most famous criticism is that it can seem to recommend managing evidence rather than improving outcomes. David Lewis called this an irrational policy of “managing the news”; James Joyce argued that agents should choose by causal efficacy rather than auspiciousness.

Consider a stylized medical case. A person may or may not have a disease caused by a hidden genetic factor. The same factor also makes people unusually likely to crave a harmless, enjoyable food. Suppose the food has no effect on the disease but gives one unit of pleasure. In a population model, people who eat it are more likely to have the disease than people who abstain. If disease is sufficiently bad, EDT’s conditional calculation could favor abstention: eating is bad news about one’s health.

The causal objection is immediate. Abstaining does not remove the genetic factor; it merely sacrifices a pleasure. In a model that fixes the already-present genetic state under intervention, eating is better.

An evidentialist can reply that the proper information state matters. If the agent already knows all the features of their own craving that explain the correlation, the additional fact that they eat may carry no further evidence of disease. But that reply depends on the model: if the choice itself remains informative about a hidden cause, the original tension can persist. It would be too quick either to declare all such objections decisive or to assume that conditioning on the agent’s information always removes them.

This example reveals the normative dispute. EDT treats an action’s evidential association with an unfavorable state as relevant to its value. CDT asks whether the action changes that state or its consequences. Which criterion is rational is not settled by probability theory alone.

## Further implications and limits

The reference notes an application to the Sleeping Beauty problem, where an agent’s awakenings and memory loss create uncertainty about both ordinary events and her location within a sequence of experiences. Decisions about repeated bets require a precise account of when offers occur, which awakenings count, and whether payoffs are charged once or repeatedly. The article reports disagreement over whether adopting EDT protects a “halfer,” who assigns probability \(1/2\) to heads upon awakening, from Dutch-book arguments. In particular, it cites Vincent Conitzer’s argument that halfers can remain vulnerable even if they use EDT. The lesson is not that EDT alone settles Sleeping Beauty, but that decision rules, self-locating credences, and betting arrangements interact.

The reference also mentions an “evidentialist’s wager”: even someone uncertain that EDT is correct might give it weight because correlated decisions can involve unusually large stakes. This is a proposal about decision-making under uncertainty over decision theories, not a straightforward consequence of the EDT equation. Whether it succeeds depends on how rival theories’ recommendations and stakes are compared.

More generally, EDT’s distinctive strength is that it takes correlations seriously wherever they bear on expected outcomes. Its distinctive vulnerability is that the same principle can reward actions for being signs of good fortune even when they do not produce it. Applying the theory responsibly means modeling both features rather than assuming the desirable one.

## Conclusion

EDT evaluates an action by the expected utility conditional on taking it, given the agent’s information. That rule can favor one-boxing against a predictor and cooperation with a correlated twin, without requiring either backward causation or communication. It can also yield controversial recommendations when an action is evidence of an independent good or bad state.

For unfamiliar cases, the essential work is to construct the joint distribution carefully, distinguish actions from policies and interventions, and make the agent’s information explicit. The formula is short; the philosophical and modeling questions lie in what one is entitled to condition on, and why conditional news value should guide choice.

### References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688; CC BY-SA 4.0.
- Arif Ahmed, *Evidential Decision Theory*, Cambridge University Press, 2021.
- Allan Gibbard and William L. Harper, *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- David Lewis, “Causal Decision Theory,” *Australasian Journal of Philosophy*, 1981.
- Vincent Conitzer, “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists,” *Synthese*, 2015.