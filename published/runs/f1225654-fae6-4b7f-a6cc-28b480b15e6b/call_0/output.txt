# Causal Decision Theory: Expected Utility under Intervention

Causal decision theory (CDT) says that a rational agent should choose the action that causes the best expected outcome. The supplied article contrasts CDT with evidential decision theory (EDT), which chooses the action that would be the best news if one learned that it had been taken. I develop the formal rule, explain the difference between counterfactual and conditional probabilities, and propose an operational method for applying CDT to new cases. The causal-model machinery below is my supplement; the source correctly notes that CDT itself does not specify a unique computational algorithm.

## 1. The core rule

Let \(\mathcal A\) be a finite set of possible actions. Let \(O_1,\dots,O_n\) be mutually exclusive and exhaustive outcomes, with desirabilities \(D(O_j)\). Gibbard and Harper formulate CDT as maximization of

\[
U(A)=\sum_{j=1}^n P(A\to O_j)D(O_j),
\]

where \(P(A\to O_j)\) is the probability assigned to the counterfactual: if \(A\) were performed, \(O_j\) would occur. The CDT decision rule is

\[
A^*\in\arg\max_{A\in\mathcal A}U(A).
\]

The probabilities here are not ordinary conditional probabilities \(P(O_j\mid A)\). They represent what would happen under an intervention that makes \(A\) true. In deterministic cases, they are 0 or 1; in stochastic cases, they are chances or credences about the consequences of intervening.

Example: eating an apple may cause happiness if the apple is good and sadness if it is bad. If \(p\) is the probability that the apple is good, then

\[
U(\text{apple})=pD(\text{happy})+(1-p)D(\text{sad}).
\]

If an orange certainly gives mild pleasure \(M\), then \(U(\text{orange})=D(M)\). CDT chooses the larger value. The same structure applies when uncertainty concerns hidden causal states, character traits, predictors, or physical mechanisms.

## 2. Counterfactuals are not conditional probabilities

EDT uses

\[
V(A)=\sum_j P(O_j\mid A)D(O_j).
\]

This measures how strongly the news of \(A\) supports \(O_j\). CDT asks instead what \(A\) would bring about. The source notes Lewis’s result that probabilities of conditionals do not generally equal conditional probabilities; if they always did, CDT would collapse into EDT. Gibbard and Harper showed that, under some assumptions—one related to the controversial principle of conditional excluded middle—statistical independence between \(A\) and the counterfactual \(A\to O_j\) makes the two calculations agree. The interesting cases are those where this independence fails because the action is evidence for background facts that also affect outcomes.

The King David example illustrates this. David wants to summon Bathsheba but fears revolt. Let \(K\in\{C,U\}\) represent whether David is charismatic or uncharismatic. Charisma is fixed in adulthood. Charismatic kings rarely face successful revolts; uncharismatic kings often do. Summoning Bathsheba is an unjust act and therefore evidence that David is uncharismatic, but by stipulation unjust acts do not themselves cause revolts. EDT evaluates

\[
V(\text{summon})=\sum_k P(K=k\mid \text{summon})D(\text{summon},k),
\]

and may abstain because summoning raises the posterior probability of \(U\). CDT evaluates

\[
U(\text{summon})=\sum_k P(K=k)D(\text{causal consequence of summon},k),
\]

holding fixed the prior probability of \(K\). Since David cannot change his charisma by acting, and summoning does not causally increase revolt, CDT recommends summoning. CDT does not ignore correlation in general; it refuses to treat an action’s merely evidential connection to a fixed trait as a causal route to the trait’s consequences.

## 3. Computing counterfactual probabilities

The source correctly points out that CDT does not itself specify how to calculate \(P(A\to O_j)\). Lewis proposed imaging: start with a probability distribution over possible worlds, and for each world \(w\) move its probability mass to the closest world \(w_A\) in which \(A\) is true. Then

\[
P(A\to O_j)=\sum_{w: w_A\models O_j}P(w).
\]

This captures minimal counterfactual change, but it requires a metric of closeness and can lead to regress, because we must know what we would believe if we were certain of \(A\). If no closest \(A\)-world exists, the counterfactual is undefined; if several are equally close, imaging must distribute mass among them. This illustrates why CDT needs additional structure.

To make CDT operational, I propose interpreting the counterfactual probability with a structural causal model. Let \(X\) be background variables, \(A\) the action variable, and \(O\) the outcome. A model specifies structural equations or conditional distributions, for example

\[
X:=f_X(U_X),\quad A:=f_A(X,U_A),\quad O:=f_O(A,X,U_O).
\]

The intervention \(do(A=a)\) replaces the equation for \(A\) by \(A:=a\), leaving the other equations unchanged. Then

\[
P(A\to O_j)\equiv P(O=O_j\mid do(A=a)),
\]

and

\[
U(a)=\mathbb E[D(O)\mid do(A=a)].
\]

If the agent is uncertain about the causal model \(M\), she can average:

\[
U(a)=\sum_m P(M=m)\,\mathbb E[D(O)\mid do(A=a),M=m].
\]

This yields a practical procedure: enumerate actions; assign utilities to outcomes; specify a causal model or counterfactual outcome distributions; for each action, intervene on the action variable, holding fixed variables not causally downstream of it; compute expected utility; choose the maximum. This is not in the source, but it is a natural operational reading of “expected causal consequences.”

The procedure also explains how CDT treats dependencies. In a causal graph, \(do(A=a)\) removes incoming arrows to \(A\). Correlations due to common causes of \(A\) and \(O\) are held fixed; correlations due to \(A\)’s causal influence on descendants are included. If a trait causes both the action and the outcome, the action is not treated as changing the trait. If the action changes a mediator that changes the outcome, that path is included.

## 4. Policies

For policies, let \(\pi\) map histories to actions. CDT can evaluate \(\pi\) by replacing the agent’s decision rule with \(\pi\):

\[
U(\pi)=\mathbb E[D(O)\mid do(\pi)].
\]

If adopting the policy is causally upstream of a predictor, the intervention changes the predictor. If the predictor’s prediction is already fixed, the intervention does not change it. Thus CDT can favor precommitment when precommitment has causal effects, while still evaluating already-fixed past predictions as fixed. At later choice points, the agent conditions on observations but still evaluates interventions relative to the resulting state. Thus CDT can be dynamically inconsistent: a plan chosen earlier may no longer maximize causal expected utility when the time comes, unless the plan itself has been made causally binding.

## 5. Newcomb’s problem

In Newcomb’s problem, a reliable predictor has already filled opaque box B: \(\$1{,}000{,}000\) if it predicted one-boxing, \(\$0\) if it predicted two-boxing. Box A always contains \(\$1{,}000\). The player chooses one box or both.

CDT treats the prediction and B’s content as fixed unless the present choice causally affects them. Given that the prediction is already made, two-boxing dominates one-boxing: if B contains \(M\), two-boxing yields \(M+1000\) versus \(M\); if B contains 0, two-boxing yields 1000 versus 0. Hence

\[
U(\text{two-box})-U(\text{one-box})=1000,
\]

so CDT recommends two-boxing.

EDT instead conditions on the action. One-boxing is strong evidence that the predictor predicted one-boxing, so with accuracy \(0.99\),

\[
V(\text{one-box})\approx 0.99\cdot 1{,}000{,}000,
\]

while two-boxing is strong evidence that B is empty, so

\[
V(\text{two-box})\approx 0.99\cdot 1{,}000.
\]

EDT recommends one-boxing. The disagreement is precisely whether the agent should act on evidence or on causal consequence. If the agent could adopt a policy before the predictor acts and the predictor observes that policy, CDT may recommend a one-boxing policy; after the prediction is fixed, it recommends two-boxing.

## 6. Counterexamples and fixed dependency hypotheses

The source cites Egan’s criticism that CDT holds fixed the agent’s unconditional credences in dependency hypotheses. In causal-model language, CDT does not update the distribution of background variables on the evidence of the action being evaluated. Egan argues this creates a disconnect with the intuitive rule “do what you expect will bring about the best results,” especially when the action reveals the agent’s type.

Death in Damascus is a classic predictor case: Death predicts where you will be and waits there. If your choice is correlated with Death’s prediction but does not cause it, CDT may treat each move as not changing the prediction, while the evidential structure makes the decision unstable. The source cites this as a problem for CDT.

The Adversarial Offer gives a monetary version. Two boxes cost \(\$1\) each; the seller put \(\$3\) in each box she predicted the buyer would not acquire, with prediction accuracy 0.75. The source says CDT reasons that at least one box contains \(\$3\), so the average box has causal expected value at least \(\$1.50\), exceeding the cost; CDT buys. Yet the seller profits. The example turns on CDT holding the seller’s prediction fixed under the buyer’s intervention.

The Psychopath Button is similar. Paul can press a button that kills all psychopaths. He prefers a world without psychopaths but believes only a psychopath would press it and prefers living with psychopaths to dying. EDT says not to press, because pressing is bad evidence about Paul. The source says CDT endorses pressing, because the causal effect of pressing is eliminating psychopaths while Paul’s psychopathy is held fixed. These cases motivate the worry that CDT can recommend actions that the agent expects to be bad once the action’s self-revealing character is taken into account.

The source also notes Oesterheld and Conitzer’s claim that CDT agents can voluntarily lose money and face diachronic Dutch books, and Joyce’s defense that CDT can use information about one’s inclinations as evidence. A careful CDT agent can update before the choice on self-knowledge; what it refuses is treating the choice as changing fixed background facts by mere evidential implication.

## 7. Applying CDT to unfamiliar cases

To apply CDT, ask which dependencies would remain if the action were imposed. A useful rule is:

- If \(A\) causes \(B\) or a chain to \(B\), include that effect.
- If a common cause \(C\) affects both \(A\) and \(O\), hold \(C\) fixed under \(do(A)\).
- If \(A\) is evidence of a fixed trait \(T\), do not let \(A\) change \(T\).
- If a prediction is already fixed and not causally affected by \(A\), hold it fixed; if \(A\) or a chosen policy causally influences the prediction, include that influence.
- When outcomes include the agent’s future choices, evaluate policies rather than isolated acts; the policy intervention fixes the decision rule, not merely a single action.

The main remaining uncertainty is the source of the causal model or closeness relation. CDT does not solve this by itself. The structural-model interpretation above is reasonable because it makes counterfactuals computable from explicit causal assumptions and allows uncertainty over causal structures. If no credible causal model is available, CDT may be indeterminate; any theory that distinguishes causation from correlation faces that problem.

## Conclusion

CDT’s central formula is

\[
U(A)=\sum_j P(A\to O_j)D(O_j).
\]

It evaluates actions by the expected value of what they would cause, not by the news value of the actions. This yields two-boxing in Newcomb’s problem and summoning in David’s case, while EDT reaches opposite recommendations when actions are strong evidence about background states. CDT’s main open question is how to compute counterfactual probabilities. Lewis’s imaging gives a philosophical semantics; structural causal models with the \(do\)-operator give a precise operational interpretation, though this is an addition to the source. With such an interpretation, CDT is a tractable decision procedure: model the causal structure, intervene on the action or policy, compute expected utility, and choose the best.

## References

Gibbard, Allan, and William L. Harper. 1981. “Counterfactuals and Two Kinds of Expected Utility.” In *Ifs*, 153–190.

Lewis, David. 1981. “Causal Decision Theory.” *Australasian Journal of Philosophy* 59 (1): 5–30.

Pearl, Judea. 2009. *Causality*. 2nd ed. Cambridge University Press. (Operational supplement.)

Wikipedia contributors. 2026. “Causal Decision Theory.” Revision 1381555528. Wikimedia Foundation.