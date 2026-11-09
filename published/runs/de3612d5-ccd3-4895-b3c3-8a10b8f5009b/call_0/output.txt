# Evidential Decision Theory: Choosing the Best News

Evidential decision theory (EDT) evaluates acts by their *news value*: the expected desirability of outcomes conditional on learning that the act was performed. The supplied reference article summarizes EDT with the slogan “do what you most want to learn that you will do” (Ahmed 2021). Instead of first asking, “What will this action causally bring about?” EDT asks, “If I received news that I had performed this action, how good would the world likely be?” The rational act is the one whose news is best in expectation.

This essay gives EDT’s central mathematical rule, explains how it treats dependencies and counterfactuals, and applies it to examples and policies. I follow the source in presenting EDT through conditional expected utility and contrasting it with causal decision theory (CDT). Where the source is silent—especially about probability assignments for actions and policy evaluation—I add operational assumptions and identify them.

## 1. The core rule

Let \(\mathcal A\) be a finite set of possible acts. Let \(O_1,O_2,\ldots\) be a partition of possible outcomes, and let \(D(O_j)\) be the desirability or utility of outcome \(O_j\). EDT assigns to act \(A\) the value

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This is the formula given by Gibbard and Harper (1976) in the source. The probability \(P(O_j\mid A)\) is the agent’s conditional credence that \(O_j\) will occur given that \(A\) is performed. EDT recommends choosing an act maximizing \(V(A)\).

If outcomes are continuous, replace the sum by an integral:

\[
V(A)=\int D(o)\,dP(o\mid A).
\]

Often outcomes are determined by acts and states. If \(S_k\) are possible states and \(O(A,S_k)\) is the outcome produced by \(A\) in state \(S_k\), then

\[
V(A)=\sum_k P(S_k\mid A)D(O(A,S_k)).
\]

This state-based form is useful: for each state, ask how likely that state is under the supposition that you do \(A\), evaluate the resulting outcome, and average.

The probabilities are *evidential conditionals*. If \(P(A)>0\), one may use

\[
P(O_j\mid A)=\frac{P(O_j\wedge A)}{P(A)}.
\]

But acts are not always ordinary events with stable prior probabilities. I discuss this below. The essential idea is the agent’s credence in \(O_j\) under the supposition “I do \(A\).”

CDT uses a different expression:

\[
U(A)=\sum_j P(A \mathrel{\Box\rightarrow} O_j)D(O_j),
\]

where \(A \mathrel{\Box\rightarrow} O_j\) is a counterfactual: the probability of \(O_j\) in the situation in which \(A\) is performed. The source emphasizes that \(P(A \mathrel{\Box\rightarrow} O_j)\) and \(P(O_j\mid A)\) are not always equal. When they coincide, EDT and CDT agree. When they diverge, EDT follows conditional probability, while CDT follows counterfactual or interventionist probability.

A helpful interpretation: imagine a reliable report tomorrow saying which act you performed. The value of the report “you did \(A\)” is \(V(A)\). EDT says to make the report you most want to receive true.

## 2. Dependencies and counterfactuals

EDT treats any probabilistic dependence between act and outcome as relevant, so long as it appears in \(P(O_j\mid A)\). If learning that \(A\) occurred raises the probability of a good outcome, \(A\) has high news value. Such dependence can arise in several ways.

First, the act may cause the outcome. Medicine may improve health; then EDT and CDT usually agree.

Second, the act may be correlated with an outcome through prediction or common cause. A predictor may have predicted your choice before setting a reward. Your action does not cause the past prediction, but it is evidence about it. Newcomb’s problem is this kind of case.

Third, the act may be correlated with another agent’s act through similarity or logical dependence. In the twin prisoner’s dilemma, Aomame’s action does not causally affect her isolated twin, but it is evidence of her twin’s action.

Fourth, dependencies may arise from indexical or selection effects. The source mentions Sleeping Beauty, where EDT has been invoked in Dutch-book arguments, though the source also notes Conitzer’s objection. I do not resolve that issue here.

The difference from CDT can be expressed by contrasting conditioning with intervention. EDT asks for \(P(O\mid A)\): the probability of \(O\) given the news \(A\). CDT asks for something closer to \(P(O\mid do(A))\): the probability of \(O\) if \(A\) were brought about by intervention. The source uses a counterfactual arrow rather than the \(do\)-operator, but the distinction is similar. An intervention may sever evidential links between an act and its causes; EDT leaves those links in place.

Thus, if a common cause \(C\) influences both \(A\) and \(O\), EDT may value \(A\) because it indicates \(C\), while CDT may not. This explanatory causal-graph formulation is my addition; the source’s claim is only that conditional and counterfactual probabilities can differ.

## 3. Examples

### Newcomb’s problem

The source describes Newcomb’s problem. A predictor is 99% accurate. Box A contains $1,000. Box B contains $1,000,000 if the predictor predicted one-boxing, and nothing if it predicted two-boxing. The player may take both boxes or only B.

EDT uses conditional probabilities:

\[
P(\text{1M in B}\mid \text{one-box})=0.99,
\]

\[
P(\text{1M in B}\mid \text{two-box})=0.01.
\]

Then

\[
V(\text{one-box})=0.99\cdot \$1{,}000{,}000+0.01\cdot \$0=\$990{,}000,
\]

while

\[
V(\text{two-box})=0.01\cdot \$1{,}001{,}000+0.99\cdot \$1{,}000=\$11{,}000.
\]

EDT recommends one-boxing. One-boxing is strong evidence that B was filled; two-boxing is strong evidence that B was left empty. CDT, as the source notes, recommends two-boxing because the contents are already fixed. The case shows that EDT rewards actions that are good evidence of desirable states.

### Twin prisoner’s dilemma

In the source’s twin case, Aomame and her psychological twin choose separately. Payoffs: mutual cooperation gives $5 each; mutual defection gives $1 each; unilateral defection gives $10 to the defector and $0 to the cooperator. If the twins are perfectly alike,

\[
P(\text{twin cooperates}\mid \text{Aomame cooperates})=1,
\]

\[
P(\text{twin cooperates}\mid \text{Aomame defects})=0.
\]

Thus

\[
V(C)=1\cdot \$5+0\cdot \$0=\$5,
\]

\[
V(D)=0\cdot \$10+1\cdot \$1=\$1.
\]

EDT recommends cooperation.

A useful generalization, my own addition, is to let

\[
q=P(\text{twin cooperates}\mid C),\qquad r=P(\text{twin cooperates}\mid D).
\]

Then

\[
V(C)=5q,\qquad V(D)=10r+1(1-r)=1+9r.
\]

EDT recommends cooperation exactly when \(5q>1+9r\). Perfect correlation satisfies this; weak correlation may not. This shows how EDT handles partial dependencies.

### Smoking lesion: an additional example

The source does not mention the “smoking lesion” case, but it clarifies EDT’s controversial side. Suppose a lesion causes both cancer and a desire to smoke, while smoking itself does not cause cancer and gives small pleasure. Since smoking is evidence of the lesion, EDT may assign smoking low value. CDT would not penalize smoking causally. This illustrates Lewis’s criticism that EDT manages news, and Joyce’s claim that rational choice should track causal efficacy. The example is mine, but it follows directly from EDT’s rule.

## 4. Policies and practical use

The source focuses on acts, but many decisions involve policies: rules, algorithms, or dispositions. EDT can evaluate a policy \(\pi\) by treating it as a proposition: “the agent adopts and follows \(\pi\).” Then

\[
V(\pi)=\sum_o P(o\mid \pi)D(o).
\]

If a policy maps observations \(X\) to actions, one operational version is

\[
V(\pi)=\sum_x P(X=x\mid \pi)
       \sum_o P(o\mid X=x, A=\pi(x), \pi)D(o).
\]

This is not a new principle; it is the conditional-utility rule applied to a richer description of the act. The phrase “adopts and follows” matters. If merely announcing a policy is weak evidence that it will be followed, EDT should condition on actual execution or on whatever proposition reliably predicts outcomes. This operational clarification is my own; the source does not develop policy evaluation.

A practical procedure is:

1. Specify candidate acts or policies.
2. Specify outcomes and utilities.
3. Model states, predictors, other agents, and observations probabilistically.
4. For each candidate, compute \(P(\text{outcome}\mid \text{candidate is performed})\).
5. Choose the candidate with highest conditional expected utility.

The hard step is modeling the evidential dependencies. EDT does not by itself tell you which correlations are real or relevant; it tells you how to use your probability model once formed.

## 5. Open questions and an operational interpretation

The source leaves several questions open.

First, how should \(P(O_j\mid A)\) be defined when acts have zero or near-zero prior probability? If the ratio definition fails, EDT needs conditional credences under supposition. A reasonable operational interpretation is to use a “deliberative” probability model that assigns positive probability to each available act, or to treat the conditional probabilities as primitive judgments. In well-specified problems—predictors, twins, repeated statistical data—these conditionals can often be estimated or justified directly.

Second, how should EDT handle cases where conditioning on an act produces “good news” by indicating a desirable state that the act does not bring about? The source quotes Lewis and Joyce criticizing EDT for this. My view is that EDT is coherent if the decision problem is framed as choosing the proposition about oneself that one wants to be true. But if the aim is interventionist control, CDT may be more appropriate. In unfamiliar cases, ask: is the act valuable because it causes good outcomes, or merely because it indicates them? EDT counts both; many philosophers think it should count only the first.

Third, the Sleeping Beauty discussion in the source remains unresolved. EDT has been used to avoid Dutch books, but Conitzer argues that halfers using EDT may still be vulnerable. This suggests that EDT’s interaction with indexical probability is not settled by the basic formula alone.

Finally, the source mentions the “evidentialist’s wager”: even if one gives EDT modest credence, acting as if EDT were true may be advantageous when many correlated decision-makers are involved (MacAskill et al. 2021). This is a strategic argument, not a proof of EDT, but it gives EDT practical importance in large-scale correlated choices.

## Conclusion

EDT offers a simple, precise rule: choose the act or policy with the highest expected desirability conditional on its performance. Its power is that it takes seriously all evidential connections—prediction, correlation, duplication, and logical dependence. Its controversy is that it does not distinguish auspicious evidence from causal efficacy. To apply EDT, model the relevant dependencies, compute conditional probabilities, and maximize conditional expected utility. Whether that is the whole of rational choice is the enduring debate between EDT and CDT.

## References

Ahmed, Arif. 2021. *Evidential Decision Theory*. Cambridge University Press.

Conitzer, Vincent. 2015. “A Dutch book against sleeping beauties who are evidential decision theorists.” *Synthese* 192 (9): 2887–2899.

Gibbard, Allan, and William L. Harper. 1976. *Counterfactuals and Two Kinds of Expected Utility*.

Joyce, James M. 1999. *The Foundations of Causal Decision Theory*. Cambridge University Press.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

MacAskill, William, Aron Vallinder, Caspar Österheld, Carl Shulman, and Johannes Treutlein. 2021. “The Evidentialist’s Wager.”

Wikipedia contributors. 2026. “Evidential decision theory.” Revision 1373679688. https://en.wikipedia.org/w/index.php?title=Evidential_decision_theory&oldid=1373679688.