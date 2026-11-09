# Causal decision theory: choosing by changing the world

A decision is not merely a prediction of what kind of person one is. It is also an opportunity to change what happens. **Causal decision theory** (CDT) builds its recommendation around that distinction: choose the available action whose causal consequences have the greatest expected utility.

This can sound indistinguishable from ordinary expected-utility maximization. The difficulty lies in deciding which probabilities belong in the expectation. An action may be excellent news without being a useful intervention. For example, a patient’s choosing a particular treatment might be evidence that they are healthy, if healthy patients tend to choose it. That does not establish that the treatment causes health. Conversely, an action may be bad news about an unchangeable circumstance while still improving the outcome.

CDT asks what would happen *if the agent performed each action*, not merely what tends to be observed among agents who perform it. This essay presents that idea formally, then examines what is required to apply it—and why its recommendations are disputed in cases involving prediction and self-knowledge.

## Expected utility and counterfactuals

Suppose an agent has available actions \(a\in\mathcal A\), uncertain possible outcomes \(o\), and a utility function \(u(o)\). Utility represents the agent’s preferences over outcomes; money can be used as a proxy only when its marginal utility is appropriately treated as constant.

In the counterfactual formulation described by Gibbard and Harper, the causal value of an action is

\[
V_C(a)=\sum_o P(a\Box\!\!\to o)\,u(o),
\]

and CDT recommends an action in

\[
\operatorname*{arg\,max}_{a\in\mathcal A}V_C(a).
\]

Here \(a\Box\!\!\to o\) is read “if \(a\) were performed, \(o\) would result.” It is not the ordinary material implication “either \(a\) is false or \(o\) is true.” It is a claim about the outcome under a counterfactual supposition.

For this expression to be a standard expected utility, the counterfactual outcomes must form an appropriate probability distribution: for each possible situation, the outcome under \(a\) must be specified, or a suitable probability distribution over outcomes under \(a\) must be supplied. The underlying theory of counterfactuals matters. In particular, the reference article notes that some formal results depend on controversial assumptions about whether counterfactual alternatives are mutually exclusive and exhaustive.

A convenient operational interpretation is to use **potential outcomes**. Let \(O_a\) denote the outcome that would result under action \(a\). Given the agent’s current evidence \(E\),

\[
V_C(a\mid E)=\mathbb E[u(O_a)\mid E].
\]

This notation makes clear that uncertainty remains: the agent may not know which outcome \(a\) would produce. If an apple is good with probability \(0.7\), eating a good apple has utility \(10\), and eating a bad one has utility \(-8\), then its causal expected utility is

\[
0.7(10)+0.3(-8)=4.6,
\]

provided eating it has those effects and the probabilities reflect the evidence available at decision time. An alternative with utility \(5\) would be preferable. CDT is not a rule to maximize the best possible consequence; it weighs possible consequences by their probabilities.

The evidential alternative evaluates the same action differently:

\[
V_E(a\mid E)=\mathbb E[u(O)\mid A=a,E],
\]

where \(A\) is the action actually taken and \(O\) the actual outcome. EDT asks what outcome is likely *on learning that the action was taken*. CDT asks what outcome would result *under the action*. The two agree in many ordinary problems, but the probabilities need not agree.

Lewis’s work on probabilities of conditionals helps explain why one cannot generally replace a counterfactual probability with an ordinary conditional probability. The distinction is not merely verbal: conditioning on an action can change beliefs about its causes, while performing an action need not change those causes.

## A causal model for calculation

The reference article states that CDT itself does not supply a unique algorithm for counterfactual probabilities. A structural causal model is one useful additional assumption, not a definition mandated by the article.

Consider variables connected by equations

\[
X_i=f_i(\operatorname{Pa}_i,U_i),
\]

where \(\operatorname{Pa}_i\) are the direct causal parents of \(X_i\), and \(U_i\) represents background factors. The agent has a probability distribution over those factors and perhaps over competing models. To evaluate an action \(a\), replace the normal equation determining the action \(A\) with

\[
A:=a,
\]

and propagate its consequences through the remaining equations. This is written \(\operatorname{do}(A=a)\). In an appropriate model,

\[
V_C(a\mid E)
 =\sum_o u(o)\,P(o\mid \operatorname{do}(A=a),E).
\]

The intervention breaks the normal causal inputs into the action variable, while leaving other mechanisms intact. It does **not** freeze every other variable: downstream effects of the action are precisely what must be allowed to change. Nor does it automatically freeze everything in the past by logical necessity. Rather, the usual model of an ordinary present action has no causal arrows from that action into already settled past events. If a problem genuinely includes retrocausation, the causal model would have to represent it.

The model should also respect the timing and content of the evidence \(E\). If the agent has observed a test result, that observation changes the distribution of background factors used to evaluate every action. One should not, however, automatically treat the hypothetical intervention \(A=a\) as a newly observed action and condition on it in the ordinary evidential way. That would reintroduce the very distinction CDT is intended to draw.

A simple illustration is confounding. Let \(H\) be health, \(A\) exercise, and \(O\) later well-being. Suppose health causes both a greater propensity to exercise and better later well-being:

\[
H\longrightarrow A,\qquad H\longrightarrow O,\qquad A\longrightarrow O.
\]

Observing that a person exercises supplies information about \(H\), but forcing exercise does not thereby cause the person to have had better prior health. Nonetheless, exercise may causally improve \(O\). A useful calculation separates these paths rather than declaring either that correlation is worthless or that all correlation is causation.

An especially practical point follows: observational data alone do not always identify \(P(O\mid\operatorname{do}(A=a))\). Causal assumptions, experiments, or other evidence may be needed. If several causal models remain plausible, the agent can average their action values using its current credences:

\[
V_C(a\mid E)=\sum_m P(m\mid E)\,
\mathbb E_m[u(O_a)\mid E].
\]

This is an ordinary Bayesian way to handle model uncertainty. It does not remove the possibility that reasonable people disagree about which models deserve credence.

## The king and the hidden cause

The reference’s example of King David illustrates the contrast with EDT. David wants to summon Bathsheba but fears a revolt. Suppose a hidden trait, charisma, influences both whether a king behaves unjustly and whether revolt succeeds. Uncharismatic kings are more likely to act unjustly and more vulnerable to revolt; unjust acts themselves do not cause successful revolt in the stipulated example.

To see the structure numerically, imagine that half of kings are charismatic. Successful revolt occurs with probability \(0.1\) for charismatic kings and \(0.6\) for uncharismatic kings. Suppose \(10\%\) of charismatic kings summon someone, while \(90\%\) of uncharismatic kings do. Then

\[
P(\text{uncharismatic}\mid\text{summon})=0.9,
\]

whereas

\[
P(\text{uncharismatic}\mid\text{abstain})=0.1.
\]

Consequently, summoning is associated with a higher revolt probability: \(0.55\), rather than \(0.15\). But if summoning has no causal effect on charisma or revolt, the probability of revolt under either intervention is

\[
\tfrac12(0.1)+\tfrac12(0.6)=0.35.
\]

Thus, if David values summoning and assigns no other relevant cost to it, CDT recommends summoning. EDT may instead recommend abstaining if the bad news about revolt outweighs the benefit of summoning.

These numbers are an illustration, not claims about the historical David. Nor does CDT imply that injustice is costless: moral disutility, harm to Bathsheba, and any real causal effect on revolt can all be included in the outcome. The philosophical point is narrower. Evidence that an action is associated with danger is not necessarily evidence that the action creates the danger.

## Newcomb’s problem and causal dominance

In Newcomb’s problem, a predictor has already filled an opaque box \(B\). If it predicted that the player would take only \(B\), it put \(\$1{,}000{,}000\) there; if it predicted that the player would take both boxes, it left \(B\) empty. A transparent box \(A\) contains \(\$1{,}000\). The prediction is highly accurate, and the player cannot see inside \(B\).

Under the usual causal assumptions, the player’s present choice does not change the predictor’s earlier decision or the contents already placed in \(B\). For either possible content of \(B\),

\[
\begin{aligned}
u(\text{take both})&=u(\text{take only }B)+1000
\end{aligned}
\]

when utility is linear in money. Taking both therefore **causally dominates** taking one: it gives \(\$1{,}000\) more in each relevant fixed state.

That conclusion does not require knowing the probability that \(B\) is full. It does require that taking \(A\) has no other cost, that the available actions are as stipulated, and that present choice does not causally alter the earlier filling.

EDT attends to the correlation between choice and prediction. If the conditional probability that the predictor was right is \(0.99\) for either choice, its illustrative values are

\[
V_E(\text{one box})=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V_E(\text{two boxes})=1{,}000+0.01(1{,}000{,}000)=11{,}000.
\]

It therefore recommends one box. The source’s bare claim of \(99\%\) accuracy does not by itself determine both conditional accuracies; the calculation adds that assumption.

This is the central tension. A two-boxer reasons that, whatever was predicted, taking the extra \(\$1{,}000\) helps. A one-boxer points out that one-boxers overwhelmingly receive the million in the stipulated population. Each side challenges the other’s notion of the relevant comparison. CDT’s recommendation is not a denial of predictive accuracy; it is a claim that evidential dependence on an earlier prediction is not the same as present causal influence over it.

## Actions, policies, and when commitment matters

An unfamiliar problem may offer not just an immediate action but a **policy**: a rule for choosing actions in response to later observations. If a policy \(\pi\) maps information \(I\) to an action \(\pi(I)\), its causal value can be written

\[
V_C(\pi\mid E)=\mathbb E[u(O_\pi)\mid E].
\]

Evaluating a policy requires modelling all consequences of adopting it. These can include other people learning about the policy, reacting to it, or predicting behavior from it. The intervention must represent the actual opportunity: installing a visible commitment device is not the same intervention as silently choosing an action later.

For example, before the predictor fills the Newcomb box, a player might be able to commit credibly to taking only \(B\). If that commitment causes the predictor to fill \(B\), adopting it can have high causal value. After the box has been filled, an agent with no binding commitment faces the original two-boxing calculation. This difference is about **timing and available causal influence**, not a blanket claim that CDT always favors two-boxing in every extended version of the story.

The distinction also creates a possible conflict across time. An earlier agent may prefer a commitment that its later unbound self would not follow. Whether a commitment is feasible, observable, costly, or enforceable must be specified. Simply calling a plan a “policy” does not make it causally influence a predictor, and simply evaluating it earlier does not prove it can be implemented.

In sequential problems, one can model a policy by replacing the action equations at the relevant decision nodes with the policy rule, then computing the distribution of final outcomes. If the agent can revise its policy later, those future revisions must be modelled too. Otherwise the calculation may incorrectly credit the agent with a commitment it cannot maintain.

## Dependence hypotheses and difficult self-knowledge

An intuitive way to calculate causal value is to divide the world into **dependency hypotheses**: specifications of how outcomes depend on actions. In a Newcomb calculation, for example, one hypothesis says the opaque box is full and another says it is empty. CDT weights the result of each intervention using the agent’s current probabilities for those hypotheses.

But what counts as the agent’s current information? This becomes difficult when the agent’s own inclinations are informative. The source reports Egan’s criticism that holding initial credences in dependency hypotheses fixed can disconnect CDT from the sensible advice to do what one expects will bring about the best result. It also reports Joyce’s response that CDT can take information about one’s inclinations or likely actions into account as evidence.

The **psychopath button** makes the issue vivid. Paul thinks that pressing a button will kill every psychopath. He strongly prefers surviving to dying, and thinks that only a psychopath would press it. At a fixed prior probability \(p\) that Paul is a psychopath, suppose pressing yields benefit \(b>0\) if he survives and loss \(L>0\) if he dies, relative to not pressing. Then a simple causal calculation gives

\[
V_C(\text{press})=(1-p)b-pL.
\]

Pressing is recommended when

\[
p<\frac{b}{b+L}.
\]

Yet Paul’s inclination to press may itself be strong evidence that he is a psychopath. If he has actually observed that inclination, updating on it may raise \(p\) enough to reverse the recommendation. That is legitimate even by the causal method: evidence acquired before the decision belongs in \(E\).

The hard question is whether contemplating, selecting, or being disposed to select an action must itself count as such evidence, and at what stage. If learning one’s inclination changes the recommended action, deliberation can become unstable: a move toward pressing raises the estimated risk, making abstention attractive; a move toward abstention may lower it again. The bare formula does not settle how self-locating evidence is acquired or how deliberation reaches an endpoint. A concrete application must specify a model of the agent’s information and deliberation rather than simply stipulate either a permanently fixed prior or a fully informative choice.

## Adversarial prediction

The source’s adversarial-offer example shows another cost of separating causal value from predictive correlation. Two boxes each cost \(\$1\). The previous day, the seller put \(\$3\) in each box she predicted the buyer would **not** acquire. The buyer may buy one box or none. Assume the prediction is correct with probability \(0.75\), as in the source.

At decision time, at least one box contains \(\$3\). If the buyer assigns probabilities \(q_1,q_2\) to the respective boxes containing money, then

\[
q_1+q_2\geq 1.
\]

Hence at least one box has \(q_i\geq 1/2\). If purchase does not causally alter the earlier contents, that box’s causal expected net payoff is at least

\[
3(1/2)-1=0.50,
\]

while buying nothing gives zero. On this calculation CDT recommends buying a box.

If the seller correctly predicts the box actually acquired with probability \(0.75\), that box is empty on those occasions; with probability \(0.25\), it contains \(\$3\). The buyer’s average net payoff is then

\[
0.75(-1)+0.25(2)=-0.25.
\]

The contrast depends on the prediction accuracy applying to the buyer’s actual choice under the offered decision procedure; the marginal causal calculation alone does not establish it. Given both stipulations, CDT assigns positive causal value to buying, while the predictable buyer loses money on average. The example sharpens rather than dissolves the dispute: should an agent reject an apparently beneficial intervention because its choice is correlated with how the past was arranged?

## What CDT leaves to be supplied

A workable application needs more than the slogan “choose the best causal consequences”:

1. **Available interventions:** What can the agent actually choose—an act, a randomized act, a commitment, or a contingent policy?
2. **Evidence and timing:** What has the agent observed before choosing, including evidence about its own dispositions?
3. **Causal structure:** Which variables influence which others, and which mechanisms change under each intervention?
4. **Utilities and uncertainty:** What outcomes matter, and what probabilities are assigned to the relevant models and background states?
5. **Counterfactual semantics:** What exactly counts as the outcome under an action, especially where interventions are unusual or the causal model is incomplete?

The source mentions Lewis’s *imaging* proposal: to evaluate a counterfactual, move probability from each possible world to a suitably close world in which the action occurs. This offers a general picture, but “closest” needs substantive interpretation. The article also notes concerns that specifying the required beliefs under the supposition may itself involve further conditionals. Structural models are a more operational alternative in many applications, but they too require justified equations and intervention rules.

## Conclusion

CDT evaluates alternatives by their expected consequences under intervention, not by the news conveyed by observing an action. This distinction explains both its appeal in confounded decisions and its controversial recommendations against predictors.

Its central rule is compact; applying it responsibly is not. The agent must identify the available decision, preserve the evidence already possessed, model causal dependencies, and specify what each counterfactual intervention changes. Where those inputs—especially self-knowledge and policy choice—are contested, CDT’s formula exposes the disagreement rather than automatically resolving it.

**References**

- Gibbard, A. and Harper, W. L. (1981), “Counterfactuals and Two Kinds of Expected Utility.”
- Lewis, D. (1976), “Probabilities of Conditionals and Conditional Probabilities.”
- Lewis, D. (1981), “Causal Decision Theory.”
- Egan, A. (2007), “Some Counterexamples to Causal Decision Theory.”
- Oesterheld, C. and Conitzer, V. (2021), “Extracting Money from Causal Decision Theorists.”
- Wikipedia contributors, [“Causal decision theory,” revision 1381555528](https://en.wikipedia.org/w/index.php?title=Causal_decision_theory&oldid=1381555528), the reference article for this essay.