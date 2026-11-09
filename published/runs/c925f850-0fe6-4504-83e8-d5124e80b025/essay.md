# Evidential decision theory: choosing what would be good news

Suppose you are deciding whether to take an umbrella. Finding out that you took one would usually be evidence that rain was likely: people tend to carry umbrellas when the forecast is bad. But taking the umbrella does not make rain more likely. Does the evidential connection matter to your decision?

Evidential decision theory, or **EDT**, says that an action should be evaluated by the desirability of the outcomes conditional on taking it. Its slogan is: choose the act that you would most like to learn you are taking. In familiar problems this often agrees with the advice to choose the act that causes the best outcome. In less familiar problems, an act can be evidence about facts it cannot cause—another person’s decision, a predictor’s earlier judgment, or an unknown feature of your own psychology. Then evidential and causal evaluations can diverge.

The central attraction of EDT is that it takes seriously all the information contained in one’s own action. Its central difficulty is that information is not obviously something an agent can improve merely by choosing what to do. To use the theory well, we need both its formal rule and a careful account of what goes into the probabilities in that rule.

## The evidential rule

Let \(A\) be one of the actions available to an agent, and let \(O_1,\ldots,O_n\) be mutually exclusive and exhaustive outcomes. Write \(D(O_j)\) for the desirability, or utility, of outcome \(O_j\). The reference article states EDT’s rule as

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

The recommended actions are those with maximal \(V(A)\). More generally, if \(E\) is everything the agent currently knows, the relevant quantity is

\[
V_E(A)=\sum_j P(O_j\mid A,E)D(O_j)
      =\mathbb E[D\mid A,E].
\]

The second expression emphasizes that utility can depend on anything represented in the outcome: not just money, but health, other people’s welfare, or the agent’s preferences over risk.

The condition \(A\) means that the agent considers what would be probable *on learning that the action was taken*. It does not, by itself, mean that the action is imagined to have been forcibly imposed while all earlier facts are held fixed. Conditional probabilities may change because the action is evidence of an earlier cause, a shared disposition, or a prediction.

For example, suppose umbrellas are inexpensive and useful in rain. If the decision-maker already knows the forecast, that forecast belongs in \(E\). The evidential calculation should use the probability of rain conditional on both the forecast and the umbrella choice—not merely the association between umbrellas and rain in the population. Failure to include available information can make the choice appear more informative than it really is.

### Comparison with causal decision theory

The reference contrasts the evidential formula with causal decision theory, or **CDT**. Its causal expression evaluates an action using probabilities of outcomes in a counterfactual situation where that action is performed:

\[
U(A)=\sum_j P(A\mathbin{\Box\!\rightarrow}O_j)D(O_j).
\]

Here \(A\mathbin{\Box\!\rightarrow}O_j\) is read roughly as “if \(A\) were performed, \(O_j\) would occur.” Exact interpretations of causal counterfactuals vary. One useful illustration, when a suitable causal model is available, is an intervention:

\[
U_E(A)=\mathbb E[D\mid \operatorname{do}(A),E].
\]

The operator \(\operatorname{do}(A)\) sets the action while breaking the ordinary causal links that would otherwise determine it. This intervention notation is a modeling aid, not a claim that every formulation of CDT is identical to this one.

If the action is independent of relevant background conditions once \(E\) is known, and its downstream consequences are represented correctly, conditioning and intervention can agree. They differ when the ordinary occurrence of an action is informative about facts that an intervention would not change.

EDT therefore does use a kind of hypothetical: “What should I expect, conditional on my doing this?” But it does not generally evaluate the same counterfactual as “What would happen if my action alone were changed?” That distinction does much of the work in the theory.

## Newcomb’s problem: action as evidence about a prediction

The reference’s central example is Newcomb’s problem. There are two boxes:

- Transparent box \(A\) contains \$1,000.
- Opaque box \(B\) contains either \$1 million or nothing.
- A predictor has already filled \(B\) with \$1 million if it predicted that you would take only \(B\), and left it empty if it predicted that you would take both boxes.

You know the rules but not the prediction. Assume money is valued linearly over these amounts. For the calculation in the reference, suppose the relevant conditional probabilities are

\[
P(B\text{ full}\mid \text{one-box})=0.99,
\qquad
P(B\text{ full}\mid \text{two-box})=0.01.
\]

Then

\[
\begin{aligned}
V(\text{one-box})
&=0.99(\$1{,}000{,}000)+0.01(\$0)\\
&=\$990{,}000,\\[2mm]
V(\text{two-box})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)\\
&=\$11{,}000.
\end{aligned}
\]

EDT recommends taking only \(B\): that choice is strongly associated with the favorable prior prediction.

There is a useful qualification here. Saying merely that the predictor is “99% accurate” overall does **not** by itself establish both conditional probabilities above. Overall accuracy averages across one-boxers and two-boxers; the predictive value conditional on each choice also depends on how common the choices are and on the pattern of errors. The stated numbers are sufficient assumptions for the calculation, not consequences of accuracy alone.

Under the usual causal description, by contrast, the contents of \(B\) are already fixed. Holding those contents fixed, taking both boxes adds \$1,000. CDT therefore recommends two-boxing in this standard setup. It is not denying that actual one-boxers tend to receive more; it is denying that a present choice can causally alter the earlier prediction.

The disagreement is especially vivid because each side can describe a real feature of the situation. Among actual players in the assumed population, one-boxing is excellent news. For either fixed box content, taking the extra box produces an extra \$1,000. EDT takes the first comparison as decisive; CDT takes the second.

## Correlated decisions: the twin prisoner’s dilemma

The same structure can arise without a predictor. The reference considers a prisoner’s dilemma played against a psychological twin: someone whose reasoning is exactly analogous to yours, in a situation where you cannot communicate.

Your individual monetary payoffs are:

| Your action | Twin cooperates | Twin defects |
|---|---:|---:|
| Cooperate | \$5 | \$0 |
| Defect | \$10 | \$1 |

For either fixed action of the twin, defecting pays \$5 or \$1 more than cooperating. Yet suppose your decisions match perfectly, with both alternatives assigned positive probability in the model:

\[
P(\text{twin cooperates}\mid \text{you cooperate})=1,
\quad
P(\text{twin cooperates}\mid \text{you defect})=0.
\]

Then

\[
V(\text{cooperate})=\$5,\qquad
V(\text{defect})=\$1.
\]

EDT recommends cooperation. Your choice is evidence of your twin’s choice, even though the two of you are in separate rooms and your act need not cause hers.

The result depends on the correlation, not merely on calling the other player a “twin.” Let

\[
p=P(\text{twin cooperates}\mid \text{you cooperate},E),\qquad
q=P(\text{twin cooperates}\mid \text{you defect},E).
\]

Then

\[
V(C)=5p,\qquad V(D)=10q+1(1-q)=1+9q.
\]

Cooperation is evidentially preferred precisely when

\[
5p>1+9q.
\]

Strong correlation can favor cooperation; weak correlation need not. In an ordinary prisoner’s dilemma against an independent opponent, there is no automatic EDT argument for cooperating. The agent must model how their own choice bears on the opponent’s.

## The “managing the news” objection

David Lewis characterized EDT as an irrational policy of “managing the news.” The worry is not that evidence is irrelevant to rational belief. It is that choosing an action because it is evidence of a good situation may confuse improving the situation with receiving a favorable report about it.

A stylized medical example makes the objection clear. Suppose an unknown condition \(G\) increases both a person’s desire to smoke and their risk of disease. Assume, for the example, that smoking itself has no effect on disease but gives the person one unit of enjoyment. Let avoiding disease be worth 100 units, with

\[
P(G\mid \text{smoke})=0.8,\qquad
P(G\mid \text{abstain})=0.2,
\]

and suppose disease occurs exactly when \(G\) is present. If these are the relevant probabilities at the decision point, then

\[
V(\text{smoke})=0.2(100)+1=21,
\qquad
V(\text{abstain})=0.8(100)=80.
\]

The simple evidential rule recommends abstaining. But if smoking does not change \(G\) or disease, critics ask why the agent should forgo the enjoyment. Abstaining cannot make an already existing condition disappear.

An evidentialist may reply that the action is not merely an arbitrary report: under the stipulated model, the world in which the agent abstains is genuinely more likely to be healthy. The dispute is whether that conditional association is the right basis for choice when the act cannot produce the favorable background state.

The details of the agent’s information are crucial. Suppose the person already knows a diagnostic result—or knows the strength of their craving—and this information screens off the association between choice and \(G\). If

\[
P(G\mid \text{smoke},E)=P(G\mid \text{abstain},E),
\]

then disease risk cancels from the evidential comparison, and EDT recommends smoking for the stipulated enjoyment. This kind of response is often called **screening off**: information already possessed can remove an apparent evidential connection.

But screening off is not a universal escape. A model may leave residual correlation between action and condition even after all available evidence is included. In that case the “managing the news” criticism applies to the remaining association. One should neither use population-level correlations uncritically nor assume in advance that every problematic correlation disappears.

## How to apply EDT to an unfamiliar case

The reference gives the core expected-utility formula, but it does not fully settle how an agent should construct the probability model in every decision. The following is an operational proposal for applying it, rather than an additional rule explicitly supplied by the article.

### 1. Specify the decision and the utilities

List the feasible actions and the outcomes that matter. If consequences depend on hidden states, include them. If the agent values another person’s welfare or dislikes risk, represent that in utility rather than silently treating dollars as utility.

Ask whether the decision is an isolated act or the selection of a rule for future acts. “Take the medicine now” and “follow this treatment policy whenever a test is positive” are different alternatives.

### 2. Fix the information available at the decision point

Let \(E\) include the observations, memories, forecasts, and knowledge of the setup available when the choice is made. Update on that evidence before comparing alternatives:

\[
V_E(A)=\mathbb E[D\mid A,E].
\]

Do not include facts merely because an outside analyst knows them. Conversely, do not omit information the agent actually has simply because an unconditional statistic is easier to find.

Care is needed with facts about the agent’s own deliberation. If the agent knows with certainty that they will choose \(A\), ordinary conditioning on an alternative may become impossible. This is not resolved simply by adding every description of the decision process to \(E\); it is an issue about how to model deliberation itself.

### 3. Model dependencies, not just direct effects

For each action, ask what its occurrence would indicate about relevant hidden variables. A useful representation might include a common cause \(H\), the action \(A\), another person’s choice \(T\), and an outcome \(O\):

\[
H\longrightarrow A,\qquad H\longrightarrow T,\qquad (A,T)\longrightarrow O.
\]

In such a model, conditioning on \(A\) changes beliefs about \(H\), and hence possibly about \(T\). EDT counts this information even if there is no arrow from \(A\) to \(T\). It also counts ordinary causal consequences of \(A\): conditioning on an action can provide evidence about its downstream effects as well as its upstream correlates.

Use a coherent joint distribution, not independently invented conditional probabilities. In particular, check whether claimed prediction accuracy really implies the probability of the desired outcome *given each action*.

### 4. Calculate and test sensitivity

Compute the expected utility for every action. Then vary uncertain correlations and payoffs. The twin example’s inequality \(5p>1+9q\) is more informative than the bare instruction “cooperate”: it shows exactly when that verdict holds.

This step is important because EDT is a decision rule, not a theory that automatically supplies numerical probabilities. Its recommendation inherits the uncertainty and potential errors of the probability model.

### 5. Handle zero-probability actions explicitly

Ordinary conditioning requires \(P(A\mid E)>0\). If an agent is certain they will choose one act, \(P(O\mid A,E)\) is undefined for the other. The reference’s formula does not by itself specify what to do.

One possible operational approach is to use a deliberative model in which each feasible action has positive probability, perhaps because of uncertainty about reasoning or implementation. Another is to define conditional values by limits of models in which the action has small positive probability. Neither is automatic: different ways of approaching zero can yield different limits. An analyst should state the perturbation or conditional-probability convention and check whether the recommendation depends on it. If it does, the case has not been settled by the bare EDT formula.

## Policies, randomization, and timing

EDT can evaluate policies as well as immediate acts. Let \(\pi\) be a rule mapping possible observations to actions. If the agent is now choosing a policy, an evidential evaluation can take the form

\[
V_E(\pi)=\mathbb E[D\mid \Pi=\pi,E],
\]

where \(\Pi\) is the policy the agent adopts. This asks what adopting that policy would be evidence of, including possible correlations with predictors or similarly situated agents.

That expression is a natural extension of the article’s act formula, but it requires a substantive modeling choice: what exactly counts as adopting a policy, and what in the environment is correlated with it? A predictor may predict the policy itself, the eventual action, or neither. These are different problems.

Policy evaluation can also differ from evaluating each later act in isolation. Information changes over time, and the occurrence of a later action may carry different evidence from the earlier adoption of a rule. A plan favored in advance need not be favored at every later decision point under every evidential model. If commitment is possible and matters, it must be represented as an actual available action, with its costs and consequences; it should not be assumed merely because a policy has been described.

Randomization needs the same care. If a genuinely independent coin determines an action, then, conditional on the known randomization procedure, the coin’s result may carry little or no information about a predictor’s earlier belief or a twin’s independent coin. But selecting the randomization procedure may itself be predictable or correlated with another agent’s procedure. Thus one must distinguish:

1. choosing a randomizing policy;
2. the random device’s realization; and
3. the final act.

Simply announcing “I will flip a coin” does not determine which correlations survive.

## What EDT does—and does not—settle

The reference notes an application of EDT to the **Sleeping Beauty** problem, involving repeated awakenings and disagreement over the credence Beauty should assign to a coin landing heads. Decision-theoretic arguments about Dutch books depend on the betting arrangement and on how repeated decisions are counted. The article also reports Conitzer’s argument that adopting EDT does not automatically protect “halfers” from Dutch books. The appropriate lesson is limited: EDT supplies an action-evaluation rule, but it does not, by itself, resolve every question about self-locating probability.

The article also mentions an argument for acting as if EDT were true under moral or decision-theoretic uncertainty: evidentially correlated decisions might affect much larger stakes than a narrowly causal calculation recognizes. That is a further argument about how to act under uncertainty between theories, not a direct consequence of EDT’s maximization formula. Its force depends on how competing theories and their stakes are compared.

## Conclusion

EDT evaluates an action by the expected desirability of outcomes **conditional on that action**, given the agent’s information. It therefore treats an action as evidence about predictors, psychological twins, hidden conditions, and ordinary causal consequences alike.

To apply it, specify the choice, utilities, information, and joint probability model; calculate conditional expected utilities; and expose any assumptions about correlations, zero-probability alternatives, policies, or randomization. The resulting recommendation can be sharply different from CDT’s. Whether choosing favorable evidence is rational when the act cannot cause the favorable fact remains the theory’s defining philosophical controversy.

### References

- Wikipedia contributors, [“Evidential decision theory,” revision 1373679688](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688).
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. *Counterfactuals and Two Kinds of Expected Utility*, 1976.
- Lewis, David. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59, 1981.
- Conitzer, Vincent. “A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists.” *Synthese* 192, 2015.