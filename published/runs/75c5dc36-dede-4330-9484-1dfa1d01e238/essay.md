# Evidential decision theory: choosing by the news an action brings

Suppose you must choose an action whose consequences depend partly on facts you cannot observe. Your choice may affect those facts, but it may also reveal something about them. If you accept a job offer, for example, that decision might be evidence that you received an encouraging private signal about the employer. If a highly accurate predictor has already guessed your decision, your action may be evidence of what the predictor guessed.

Evidential decision theory, or **EDT**, evaluates an action by asking how desirable the world would be *conditional on that action being taken*. Its guiding idea is sometimes summarized as: do what you would most want to learn that you will do. This is not merely a recommendation to seek good news. It is a rule for choosing among actions using ordinary conditional probabilities and expected utility.

The rule can agree with causal reasoning in familiar decisions: if taking an umbrella makes getting wet less likely, the conditional evidence associated with taking it will often favor doing so. But EDT also counts dependencies that do not run from the action to the outcome. An action can be evidence about a prediction made yesterday, another agent’s simultaneous choice, or an underlying characteristic of the chooser. Those cases make EDT distinctive—and controversial.

The reference article presents the basic rule and its contrast with causal decision theory, illustrates them with Newcomb’s problem and a twin prisoner’s dilemma, and notes several objections and unsettled applications. The discussion below develops that framework into a procedure for unfamiliar cases. Where that requires assumptions the article does not settle, I identify them as proposals rather than as consequences of the basic rule.

## 1. Conditional expected utility

Let \(K\) denote the information available to an agent at the decision point, and let \(\mathcal A\) be the set of available actions. Suppose the possible outcomes \(O_1,O_2,\ldots\) form an exhaustive, mutually exclusive partition, and let \(u(O_j)\) be the agent’s utility for outcome \(O_j\).

For an action \(a\), EDT assigns the evidential value

\[
V_K(a)=\sum_j P(O_j\mid A=a,K)\,u(O_j).
\]

The recommendation is to choose an action maximizing \(V_K(a)\), provided these conditional probabilities are defined. In more compact notation,

\[
a^*\in\operatorname*{arg\,max}_{a\in\mathcal A}
\mathbb E[u(O)\mid A=a,K].
\]

The utility function need not measure money. It can incorporate risk, other people’s welfare, or any other consequences the agent values. If utility depends on the action itself as well as on the state of the world, one can instead write

\[
V_K(a)=\sum_s P(s\mid A=a,K)\,u(a,s),
\]

where \(s\) ranges over relevant states. The important point is that the state probabilities are *conditional on the action*.

This is an application of Bayesian conditioning. For any state \(s\) with positive probability,

\[
P(s\mid a,K)
=
\frac{P(a\mid s,K)P(s\mid K)}{P(a\mid K)}.
\]

Thus an action favors states in which that action is relatively likely. If a predictor is more likely to predict one-boxing for people who actually one-box, observing one-boxing raises the probability that the predictor made that prediction. EDT uses the same relationship when evaluating the prospective action.

The condition “given \(K\)” matters. Evidence already available to the agent should not be discarded when comparing actions. Nor should one automatically assume that a correlation observed in a population remains informative after conditioning on everything the chooser knows. An action can be strong evidence before one learns a relevant fact and weak evidence afterward.

## 2. Evidence and causal counterfactuals

The reference article contrasts EDT’s conditional probabilities with the counterfactual probabilities used by causal decision theory, or **CDT**. Schematically, CDT evaluates

\[
U_K(a)=\sum_j P(a\mathrel{\Box\!\!\to}O_j\mid K)\,u(O_j),
\]

where \(a\mathrel{\Box\!\!\to}O_j\) means that \(O_j\) would occur if the agent were to take \(a\), under the relevant causal counterfactual.

One way to make the contrast concrete is with a causal model. In suitable models, CDT is often represented using an intervention:

\[
U_K(a)=\sum_j P(O_j\mid \operatorname{do}(A=a),K)\,u(O_j).
\]

The intervention fixes the action while leaving the mechanisms determining variables that causally precede it unchanged. The ordinary conditional \(P(O_j\mid A=a,K)\), by contrast, may change the probability assigned to those earlier variables because their values help predict the action. Intervention notation is a useful illustration, not a complete definition of every version of CDT: applying it still requires a causal model and care about what information belongs in \(K\).

Consider an underlying variable \(S\) that influences both an action \(A\) and an outcome \(O\):

\[
S\longrightarrow A,\qquad S\longrightarrow O.
\]

Learning \(A\) provides evidence about \(S\), hence about \(O\). But intervening to set \(A\) need not change \(S\). Consequently,

\[
P(O\mid A=a,K)
\quad\text{and}\quad
P(O\mid\operatorname{do}(A=a),K)
\]

can differ even when the two calculations use the same factual causal model.

EDT therefore does **not** require the agent to believe that choosing an action causes the past to change. Its “if I take \(a\)” is primarily a conditional-evidence question: which outcomes are probable among the possibilities in which I take \(a\)? CDT’s question is instead about what the action would bring about. The disagreement concerns which question should govern choice.

## 3. Newcomb’s problem

Newcomb’s problem makes the difference unusually sharp. A transparent box contains \$1,000. An opaque box contains either \$1 million or nothing, depending on a prediction already made:

- if the predictor predicted that you would take only the opaque box, it put \$1 million there;
- if it predicted that you would take both boxes, it left the opaque box empty.

You know the arrangement but do not know the prediction. You must choose one box or both.

For the numerical version in the reference article, assume the relevant conditional probabilities are

\[
P(\text{predicts one box}\mid\text{one box})=0.99
\]

and

\[
P(\text{predicts one box}\mid\text{both})=0.01.
\]

These are stronger specifications than the bare statement that the predictor is 99% accurate overall: overall accuracy alone need not fix accuracy conditional on each actual choice.

Treating money as utility, EDT obtains

\[
\begin{aligned}
V(\text{one box})
&=0.99(\$1{,}000{,}000)+0.01(\$0)\\
&=\$990{,}000,\\[3pt]
V(\text{both})
&=0.01(\$1{,}001{,}000)+0.99(\$1{,}000)\\
&=\$11{,}000.
\end{aligned}
\]

It recommends taking only the opaque box. One-boxing is strong evidence that the prediction favored one-boxing and the million is present; two-boxing is strong evidence that the opaque box is empty.

A standard CDT analysis instead holds the already fixed contents of the opaque box constant across the two actions. Whatever is in it, taking both boxes adds \$1,000. On that causal comparison, two-boxing wins.

Notice that EDT’s reasoning does not say that selecting one box physically sends a signal backward in time. The dependence can arise because the predictor used information about the agent’s disposition or reasoning. The prediction and the later choice are correlated; each is evidence about the other.

The recommendation is sensitive to the model. Suppose, for simplicity, that

\[
P(\text{full}\mid\text{one})=q,\qquad
P(\text{full}\mid\text{both})=1-q.
\]

Then one-boxing is preferred exactly when

\[
q(1{,}000{,}000)>
(1-q)(1{,}000{,}000)+1{,}000,
\]

or \(q>0.5005\). The numerical threshold depends on these conditional probabilities and on the payoffs; it is not a universal threshold for every predictor.

If the agent somehow observes the opaque box’s contents before choosing, the evidential situation also changes. Conditional on that observation, the earlier prediction may no longer provide a payoff-relevant difference between actions, and taking the additional \$1,000 can be favored. EDT’s advice follows the information actually available, not the story’s label.

## 4. Correlated choices: the twin dilemma

The article’s twin prisoner’s dilemma concerns an agent and a psychological twin who make choices separately. Each gets \$5 if both cooperate and \$1 if both defect. A defector against a cooperator gets \$10; a cooperator against a defector gets nothing.

If their choices are perfectly correlated, then

\[
P(\text{twin cooperates}\mid\text{I cooperate})=1,
\qquad
P(\text{twin cooperates}\mid\text{I defect})=0.
\]

Therefore,

\[
V(\text{cooperate})=\$5,\qquad
V(\text{defect})=\$1.
\]

EDT recommends cooperation, although neither person’s choice need causally influence the other’s. Defection would be better *holding the twin’s action fixed*, but EDT does not hold it fixed when one’s own action is evidence about it.

Perfect psychological similarity is a strong assumption. For an imperfectly correlated case, set

\[
p=P(\text{twin cooperates}\mid\text{I cooperate},K),\qquad
r=P(\text{twin cooperates}\mid\text{I defect},K).
\]

Then

\[
V(C)=5p,\qquad V(D)=10r+1(1-r)=1+9r.
\]

Cooperation is recommended precisely when \(5p>1+9r\). If, for instance, \(p=0.9\) and \(r=0.1\), the respective values are \(4.5\) and \(1.9\). But if the twin’s choice is conditionally independent of yours, \(p=r\), then defection is better: against any fixed probability of cooperation it adds a payoff advantage.

The lesson is not that EDT invariably recommends cooperation with similar agents. It recommends cooperation when the *relevant conditional dependence*, combined with the payoff structure, makes cooperation better news.

## 5. How to apply the rule

A practical EDT analysis can proceed in five stages.

1. **Fix the decision and information.** Specify when the choice occurs, what the agent knows, and which options are genuinely available. Include evidence about predictions, prior signals, and commitments.

2. **Specify outcomes and utilities.** Include all consequences the agent values, including costs of acting. Do not silently equate dollars with utility if risk or other concerns matter.

3. **Build a joint probability model.** Identify variables that influence actions and outcomes: hidden traits, common causes, predictors, other agents’ reasoning, and random devices. The model must support probabilities such as \(P(s,a\mid K)\), not merely list causal effects.

4. **Condition separately on each action.** Compute \(P(s\mid a,K)\), then average \(u(a,s)\) over those states. Do not hold a correlated variable fixed merely because it is causally upstream or outside the agent’s control.

5. **Check sensitivity.** Ask which assumptions drive the ranking. In particular, distinguish an asserted correlation from one established by the problem, and examine whether additional information in \(K\) screens it off.

For example, suppose a medical test is optional and a patient who takes it is more likely to be ill, because symptoms tend to prompt testing. That correlation alone does not tell a particular patient to avoid the test. The patient must condition on their own known symptoms and other information, and account for the test’s benefits and costs. If symptoms fully explain the observed association, taking the test may provide no further evidence of illness once those symptoms are included in \(K\).

This illustrates both the power and the danger of “news value”: the relevant news is not the headline association but what the proposed action adds to the agent’s existing evidence.

## 6. Actions, policies, and randomization

An action is a choice made at a particular decision point. A **policy** is a rule for choosing actions across possible information states: for example, “take the test if symptoms exceed a threshold” or “cooperate unless I learn the other player has defected.”

EDT can evaluate a policy \(\pi\) by the same formal pattern:

\[
V_K(\pi)=\mathbb E[u(O)\mid \Pi=\pi,K].
\]

But this is not automatically the same question as evaluating a single action. Conditioning on adopting a policy may be evidence about the agent’s dispositions, what a predictor forecast, and decisions made in situations the agent does not actually encounter. The appropriate comparison depends on what the agent is choosing: an implementable commitment now, a general decision rule, or an act after further information arrives.

A reasonable operational proposal is to model these as distinct variables. If the present option is a binding policy, include its implementation mechanism and compare possible policy adoptions. If the present option is an individual act with no prior commitment, compare acts conditional on the information now available. This avoids treating an unchosen hypothetical policy as though it had already caused the predictor’s behavior. It does not settle the deeper question of which policy-selection theory an agent ought to use.

Sequential choices introduce a further complication. A policy that looks best before information arrives may prescribe an action that, after the information arrives, no longer maximizes conditional expected utility. EDT applied afresh at each point can therefore disagree with an earlier plan. Commitment may be valuable, but whether it is available and credible belongs in the model rather than being assumed.

Randomization likewise needs an explicit model. If an independent coin causes the choice, learning the resulting action may reveal little about the chooser’s underlying disposition. A predictor that cannot observe or forecast that coin may correlate much less strongly with the realized choice. Conversely, a predictor might know the randomization policy or have information about the coin. Randomizing does not automatically erase evidential dependence; independence is an assumption to check.

## 7. The objection: managing the news

David Lewis’s criticism, noted in the reference article, is that EDT can look like an irrational attempt to *manage the news*. Suppose a hidden genetic condition increases both the desire to smoke and the risk of a disease, but smoking itself has no effect on disease risk. Assume further that smoking is pleasurable.

If choosing not to smoke is evidence that one lacks the condition, EDT might recommend abstaining, even though abstention does not remove the condition. Critics argue that this confuses evidence about health with a way to improve health. CDT, under the stated causal assumptions, recommends smoking for its pleasure.

The evidentialist response is that the rule never claims abstention changes the gene. It compares the expected desirability of the worlds conditional on each act. Nevertheless, whether that comparison is rational for a chooser who knows the causal story is the central dispute, not something the formula resolves by itself.

The example is also sensitive to available information. If the agent knows enough about their craving or genetic status to screen off the association between the act and the condition, then the evidential disadvantage of smoking can disappear. This observation limits some applications of the objection, but does not prove that all problematic correlations vanish: what the agent knows, and whether the choice adds evidence beyond it, must be modeled.

## 8. Unsettled edges

The basic formula leaves an important mathematical problem when \(P(A=a\mid K)=0\). Ordinary conditioning does not define \(P(O\mid A=a,K)\) in that case. This matters if a model describes an agent as certain to choose one action while the decision rule is supposed to compare alternatives.

One possible operational treatment is to introduce a small probability of each action—for instance, through an explicitly modeled chance of deliberative error—and examine the conditional values as that probability tends to zero. But different error models can produce different limits. A “tremble” is therefore an additional assumption, not a unique consequence of EDT. Alternatively, one can leave the verdict undefined until a probability model assigns meaningful conditional distributions to the alternatives.

There is a related issue of **self-reference**. A predictor may model the agent’s decision procedure, while the agent’s conditional probabilities depend on the predictor’s behavior. An analyst cannot simply assign probabilities that contradict the stipulated prediction mechanism. Finding a consistent joint model may require solving for a fixed point, or acknowledging that the description does not determine a unique one. The reference article’s simple formula does not by itself supply a general solution.

Finally, EDT does not settle every question about rational belief or uncertainty between decision theories. The article notes applications to Sleeping Beauty and Dutch-book arguments, while also reporting Conitzer’s objection to one proposed defense. Such cases depend on details of the betting protocol, information, and accounting across awakenings; the ordinary EDT formula alone does not resolve the underlying dispute. Likewise, the suggestion that one should act as an evidentialist because correlated decisions can create especially large stakes requires further assumptions about how to compare uncertainty across decision theories. It is a supporting argument, not a theorem of conditional expected utility.

## Conclusion

EDT evaluates an option by the expected utility of outcomes conditional on taking it. Its distinctive feature is that evidence supplied by an action can matter even when the action does not causally produce the correlated event. That explains its one-boxing recommendation in Newcomb’s problem and, under strong enough correlation, cooperation with a psychological twin.

To use EDT well, one must specify the agent’s information, utilities, available acts or policies, and a coherent joint probability model. The theory’s clarity lies in its conditional-expectation rule; its difficult philosophical question is whether an action’s evidential significance is always a sound basis for choosing it.

## References

- Wikipedia contributors, “[Evidential decision theory](https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688),” revision 1373679688.
- Ahmed, Arif. *Evidential Decision Theory*. Cambridge University Press, 2021.
- Gibbard, Allan, and William L. Harper. “[Counterfactuals and Two Kinds of Expected Utility](https://www.econstor.eu/bitstream/10419/220553/1/cmsems-dp0194.pdf),” 1976.
- Lewis, David. “[Causal Decision Theory](https://doi.org/10.1080/00048408112340011),” *Australasian Journal of Philosophy*, 1981.
- Conitzer, Vincent. “[A Dutch Book against Sleeping Beauties Who Are Evidential Decision Theorists](https://doi.org/10.1007/s11229-015-0691-7),” *Synthese*, 2015.