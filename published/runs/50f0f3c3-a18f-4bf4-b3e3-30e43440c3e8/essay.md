# A-FDT: Choosing the Output of a Decision Procedure

A decision can matter in ways that are not captured by the immediate physical effects of an action. A predictor may already have acted on a forecast of that action. Another agent may be running the same reasoning in a separate room. In such cases, changing what a decision procedure outputs is associated with changes elsewhere, even when the physical act itself cannot cause those changes.

**Action functional decision theory (A-FDT)** takes these dependencies seriously. Its guiding question is: *What would the outcome be if this decision procedure, on these inputs, returned a different action?* It then selects the action associated with the highest expected utility.

This essay takes Equation (4) of Section 5 of Yudkowsky and Soares’s paper as the defining formal presentation. The authors call their broader approach functional decision theory; the name A-FDT here emphasizes that Equation (4) evaluates **action outputs**, rather than directly choosing complete policies. The distinction matters: the paper says its authors prefer a policy-based formulation, but does not specify it in comparable detail.

A-FDT is not a claim that an agent can send signals backward in time, or physically alter a mathematical fact. It is a proposal about which *hypothetical models* an agent should use to evaluate its options.

## 1. The decision problem

Let \(\mathcal A\) be a finite action set, \(\mathcal O\) a set of outcomes, and \(U(o)\) the agent’s utility for outcome \(o\). Every expected-utility decision theory must assign a value of the form

\[
Q(a)=\sum_{o\in\mathcal O} P_a(o)U(o)
\]

to each action and select an action maximizing \(Q(a)\). The central disagreement is what the action-indexed distribution \(P_a\) should be.

For **evidential decision theory (EDT)**, the relevant distribution is ordinarily obtained by conditioning on the action:

\[
Q_{\mathrm{EDT}}(a)
=\mathbb E[U(O)\mid X=x,A=a].
\]

The question is what taking \(a\) would be *evidence* about.

For **causal decision theory (CDT)**, the action is instead treated as an intervention on the physical action variable:

\[
Q_{\mathrm{CDT}}(a)
=\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

In a causal model, the intervention severs the ordinary causes of \(A\), sets it to \(a\), and propagates changes through its causal effects. The question is what the act would *cause*.

A-FDT differs from both. It intervenes on a variable representing the output of the very decision procedure performing the evaluation.

Let \(P\) be a probability model, \(G\) a graph representing relevant dependence relations, and \(x\) the observation history. Write

\[
D_{P,G,x}
\]

for the *variable in the model* representing the output of A-FDT on those inputs. It is important to distinguish that variable from the actual result of running the procedure. The action rule corresponding to the paper’s Equation (4) is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid
\operatorname{do}(D_{P,G,x}=a)
\right].
}
\tag{1}
\]

If several actions maximize the expectation, an implementation needs a tie-breaking rule.

In this expression, \(\operatorname{do}\) is used in a generalized graph that contains more than ordinary causal relationships. The model is supposed to say how a hypothetical change in the logical output \(D_{P,G,x}\) affects physical actions, predictions, and any other relevant variables.

Equation (1) is an idealized recipe, conditional on being given a suitable \(P\) and \(G\). It does not itself explain how to construct the graph. That omission is central: the paper identifies the discovery and representation of these noncausal dependencies as a major open problem.

## 2. What changes in an A-FDT hypothetical?

The paper calls the relevant relation **subjunctive dependence**. Causal dependence is one instance: if an action changes, its ordinary causal consequences may change. But the category is broader. Two calculations of the same deterministic function on the same input have the same output, even if performed on isolated machines. An accurate predictor can likewise reach a conclusion that tracks an agent’s decision procedure without receiving a causal signal from the future action.

A useful distinction is among three kinds of connection:

1. **Causal effect:** a payment triggers a receipt. Changing the payment changes the receipt.
2. **Computational or predictive dependence:** a predictor models the decision procedure and acts on the result. Changing the hypothetical output can change the prediction, even though the prediction occurred earlier.
3. **Mere correlation:** a background condition makes both an action and an outcome likely, but does not respond to the decision output. Intervening on the output need not change that condition.

A-FDT tries to preserve the first two connections in its action hypotheticals without automatically preserving the third. EDT’s conditioning can preserve all correlations; CDT’s physical-action intervention generally preserves only causal effects of the physical act.

The word “hypothetical” does important work. Suppose a deterministic decision function in fact outputs \(a_1\). On fixed inputs, the proposition that it outputs a different action \(a_2\) is false as a matter of computation. The alternative is therefore a *counterpossible*: its antecedent conflicts with a mathematical fact. Ordinary conditioning on a known false logical proposition is not available.

The paper’s practical response is to treat the graph as a tool for constructing a limited counterpossible model: set the output node to \(a_2\), then recompute its modeled dependants. This is not an account of counterpossible reasoning in general. Nor does the existence of a self-referential variable solve the problem: a program can refer to a representation of itself, but deciding which mathematical consequences to preserve under an impossible intervention remains difficult.

## 3. Newcomb’s problem

A predictor has placed \$1 million in an opaque box if and only if she predicted that the agent would take only that box. A transparent box contains \$1,000. The agent can take the opaque box alone or take both boxes. The prediction has already been made.

Consider the following explicit model. Let \(D\) be the decision-output node, and let \(E\) be an independent error variable. With probability \(p\), the predictor correctly matches \(D\); with probability \(1-p\), she predicts the other action. The opaque box is full exactly when the prediction is “one-box.” The physical action follows \(D\).

Under A-FDT’s intervention on \(D\),

\[
Q(\text{one-box})=p\cdot 1{,}000{,}000,
\]

while

\[
Q(\text{two-box})=(1-p)\cdot 1{,}000{,}000+1{,}000.
\]

Thus A-FDT one-boxes when

\[
p>\frac{1+0.001}{2}=0.5005.
\]

At \(p=0.99\), the respective values are \$990,000 and \$11,000.

The numerical conclusion depends on the stated symmetric error model. Knowing only that a predictor has been right 99% of the time in some population does not by itself establish her error probabilities under both interventions on this particular decision function. Calibration, selection effects, and how she predicts all matter.

CDT instead holds the already-filled box fixed under intervention on the physical action. Taking both boxes then yields \$1,000 more whether the opaque box is full or empty. EDT can one-box because one-boxing is evidence that the prediction was favorable, although its answer depends on the probabilities assigned to the actions.

A-FDT’s justification is neither that the present act causes the past prediction nor merely that one-boxing is good news. In its model, the predictor’s prediction and the act are both downstream of the decision-function output. The agent evaluates the alternative outputs while retaining that dependence.

## 4. Why correlation alone is not enough

Now consider the paper’s imaginary smoking-lesion problem. A lesion is correlated with a desire to smoke and with fatal cancer, but smoking itself has no effect on cancer. Smoking gives the agent an additional \$1,000 worth of utility.

In a simplified model where the lesion and cancer risk do not depend on the decision-output node, let \(s\) be the probability of surviving cancer. Then

\[
Q(\text{smoke})=1{,}000{,}000s+1{,}000,
\qquad
Q(\text{refrain})=1{,}000{,}000s.
\]

A-FDT smokes. Changing the decision output changes the physical act, not the prior lesion.

This calculation assumes the action node is controlled by the intervened decision function throughout the cases being averaged. The paper’s fuller model makes the case subtler: the lesion can determine which of two preference-dependent decision procedures is being run. Intervening on the smoking-preferring procedure changes behavior only in the cases where that procedure controls action. If the probability of that case is \(r>0\), the advantage is \(1{,}000r\), rather than necessarily \$1,000.

The example is also controversial as a test of EDT. The paper acknowledges that, once preferences and an agent’s knowledge of them are modeled carefully, the smoking lesion setup can be contrived; modified versions of EDT can smoke. The lesson for A-FDT is narrower and more robust: **a statistical association does not, by itself, establish that the lesion changes when the decision function’s output changes.**

## 5. Observations and the transparent-box case

Equation (1) treats observation in a distinctive way. When the observed history changes from \(x\) to \(y\), the procedure changes its intervention target from \(D_{P,G,x}\) to \(D_{P,G,y}\). It does not, in Equation (4), add a separate condition \(X=x\) to every action hypothetical.

That is consequential when the observation itself depends on a prediction of what the agent would do upon seeing it.

Suppose both Newcomb boxes are transparent. The predictor fills the opaque box if she predicts that the agent would one-box **upon seeing it full**. Define two decision-output nodes:

\[
D_F=\text{output upon seeing full},\qquad
D_E=\text{output upon seeing empty}.
\]

Let the predictor correctly predict \(D_F\) with probability \(0.99\), and let

\[
q=P(D_E=\text{two-box})
\]

in the relevant model. Intervention on \(D_F\) changes the prediction, which changes which observation is actually produced. If the observation is empty, \(D_E\), not \(D_F\), controls the physical act.

For the two interventions, the expected utilities are

\[
\begin{aligned}
Q(D_F=\text{one-box})
&=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
Q(D_F=\text{two-box})
&=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first is larger for every \(q\in[0,1]\). Accordingly, A-FDT outputs one-box upon seeing the full boxes.

This result illustrates the theory’s most counterintuitive feature. Even when the actual observation is “full,” the hypothetical in which \(D_F\) outputs two-box includes mostly cases in which the predictor leaves the box empty—and the agent consequently never receives the input \(F\). The calculation evaluates the consequences of the *output of the procedure for that input*, not only outcomes conditional on the input actually occurring.

The paper’s detailed transparent-box derivation contains an expression that appears to intervene on the observation as well, but its subsequent numerical calculation and explanation allow the observation to vary. The calculation above follows Equation (4) and that substantive explanation, not an additional fixed-observation intervention.

An implementation must nevertheless specify the role of \(P\). If it is already conditioned on every detail of the current observation, then changing the target node alone may not reconstruct the relevant pre-observation alternatives. A reasonable operational interpretation is to retain a model of the process that generates observations—including the predictor—and use \(x\) to identify the intervention target. Which background evidence should remain fixed is an additional modeling question, not settled by the equation.

## 6. A-FDT and credible conduct

Parfit’s hitchhiker has the same structure. A driver rescues a stranded agent if she predicts that the agent will pay \$1,000 after reaching town. If rescue is worth \$1 million, an A-FDT model in which the driver accurately predicts the town decision favors an output of “pay,” even when evaluated upon arrival.

The point is not that paying causes the earlier rescue. Rather, the output “pay” belongs to a model in which the driver was more likely to rescue the agent. Ordinary CDT and EDT, once conditioned on safe arrival, can regard payment as a needless cost.

The same structure can recommend refusing certain threats, but only when the numbers and the threat-generation mechanism support it. Suppose a blackmailer launches a damaging program with probability \(b_P\) if she predicts payment and with probability \(b_R\) if she predicts refusal. Payment costs \(c\); refusal, if blackmailed, costs \(L\). If there are no other costs, A-FDT’s comparison is

\[
Q(\text{pay})=-b_Pc,\qquad
Q(\text{refuse})=-b_RL.
\]

It refuses when \(b_RL<b_Pc\). For example, if \(b_P=1\), \(c=1{,}000\), and \(L=1{,}000{,}000\), refusal is favored only if \(b_R<0.001\).

Thus “A-FDT refuses blackmail” is not a general rule. If the blackmailer launches the program regardless of prediction, then \(b_R=b_P\), and paying may be much better. What matters is whether the decision output affects the probability of being threatened in the modeled subjunctive sense.

## 7. Twins, policies, and imperfect links

Consider a prisoner’s dilemma against a perfect psychological twin. Mutual cooperation pays each player \$1 million; mutual defection pays \$1,000; unilateral defection pays the defector \$1,001,000 and the cooperator nothing.

If the twin implements the same relevant decision function on the same input, an intervention on that output changes both players’ modeled actions. The A-FDT comparison is therefore

\[
Q(C)=1{,}000{,}000,\qquad Q(D)=1{,}000,
\]

so the agent cooperates. CDT holds the other player’s act fixed and defects.

For an imperfect twin, the answer need not be cooperation. Let \(p_C\) be the probability that the other player cooperates under the intervention \(D=C\), and \(p_D\) the corresponding probability under \(D=D\). Then

\[
Q(C)=1{,}000{,}000p_C,
\]
\[
Q(D)=1{,}001{,}000p_D+1{,}000(1-p_D).
\]

Cooperation is favored only when the first expression is larger. Similarity of goals or membership in the same group is not enough to establish the needed dependence.

The distinction between actions and policies is especially important here. Equation (1) changes one output \(D_x\). A policy is instead a mapping \(\pi:x\mapsto a\) over possible observations. Choosing a whole policy could coordinate outputs at multiple inputs or across agents with different information. The paper notes that its authors prefer such a policy formulation and that it can differ in multi-agent problems. One should not silently replace Equation (1) with a policy optimization and present the result as entailed by A-FDT.

## 8. Applying A-FDT to an unfamiliar problem

The following is a practical proposal for using Equation (1), rather than an algorithm supplied by the paper for constructing the graph.

1. **Specify the decision and utility.** Identify available actions, relevant outcomes, and whose utility is being maximized. Include costs of threats, observations, and downstream acts.

2. **Identify the output node.** Represent the output of this decision procedure on the relevant inputs. If other inputs could occur, introduce separate output nodes for them.

3. **Model the environment’s mechanisms.** Include physical effects, predictors, copies, and observation-generation processes. For each candidate output, ask which variables would change if that output changed.

4. **Separate dependence from correlation.** A predictor that simulates the decision may track its output. An unrelated background condition correlated with behavior need not. Record uncertainty about these judgments.

5. **Perform each intervention and propagate it.** Set the selected output node to each action in turn. Recompute modeled dependants, including earlier predictions and possibly which observation is received. Leave variables not downstream in the chosen generalized graph at their modeled distributions.

6. **Compare expected utilities and test sensitivity.** Check whether the answer survives plausible alternatives for predictor accuracy, dependence strength, and background evidence. If it does not, the uncertainty is part of the answer.

This procedure is only as reliable as its dependence model. In particular, a predictor’s observed accuracy does not uniquely determine how its prediction would vary under a logical intervention. Different generalized graphs can fit the same observational data and yield different recommendations.

Randomization creates another unresolved choice: is the intervention on a deterministic action, a distribution over actions, or a function that also takes a random seed as input? If a predictor can see or simulate the seed, the link may be strong; if the seed is genuinely unavailable to it, the prediction may track only the distribution. Equation (1) alone does not fix that representation.

## 9. The philosophical case—and its limits

The paper argues for judging decision procedures by the utility they tend to achieve. In Newcomb-like problems, A-FDT can behave as an agent would have preferred to precommit to behave, without requiring a physical commitment device. Its authors also argue that their approach avoids certain negative values of information and resists extortion.

These are motivations, not unconditional theorems. A predictor can reward any specified decision theory and punish its rivals. The paper therefore appeals to an informal distinction between “fair” problems, where rewards depend on behavior in the problem, and cases constructed to reward a particular procedure. It acknowledges that a satisfactory general definition of fairness—and a proof that A-FDT is optimal on that class—remain open.

Likewise, claims about precommitment and information require assumptions about available policies, observations, models, and how decision procedures are compared. A-FDT’s success in the examples does not establish that it always reproduces the best policy chosen from an earlier perspective. Its distinctive accomplishment is instead a way to represent why an output can matter to predictors and copies that are not physically downstream of the current act.

## Conclusion

A-FDT evaluates an action by intervening on the modeled output of the decision procedure, then calculating expected utility while propagating relevant causal and subjunctive dependencies. This yields one-boxing in a suitably modeled Newcomb problem, smoking in the lesion model, cooperation with an exact twin, and sometimes costly credibility after an observation.

The rule is precise **given** its generalized dependency model. Constructing and justifying that model—particularly for imperfect predictors, logical counterpossibilities, and observation-dependent decisions—is the principal unfinished task.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially Sections 3–6, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).