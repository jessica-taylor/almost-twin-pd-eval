# A-FDT: Choosing the Output of a Decision Procedure

A decision can be correlated with events that it does not physically cause. A predictor may have filled a box yesterday because it foresaw what you would choose today. A sufficiently similar agent may make the same choice in another room. In these cases, holding everything outside the causal effects of your present action fixed can discard information about how the situation is structured.

Action functional decision theory, or **A-FDT**, responds by treating a decision as the output of a mathematical procedure. Instead of asking only what would happen if a physical action were changed, it asks what would happen if the decision procedure produced a different output—and allows other things dependent on that output to change with it.

This essay takes Equation (4) of Yudkowsky and Soares’s paper as the primary formal statement of A-FDT. The paper also mentions a preferred formulation that chooses entire policies. That broader formulation is useful context, but it is not interchangeable with the action-level rule developed here.

## 1. Three ways to evaluate an action

Let \(A\) be a finite set of actions, \(X=x\) the agent’s observation history, and \(V\) the utility of the eventual outcome. Expected-utility theories agree that the agent should maximize a quantity of the form

\[
\operatorname{EU}(a)=\sum_o P_a(o)\,U(o).
\]

They differ over the hypothetical distribution \(P_a\): what should the world be taken to look like when evaluating action \(a\)?

**Evidential decision theory (EDT)** uses ordinary conditional probability:

\[
a_{\mathrm{EDT}}\in\arg\max_a
\mathbb E[V\mid X=x,\operatorname{Act}=a].
\]

It asks which action would be best *news*. Its answer can reflect any correlation between the action and the outcome, including a correlation caused by a hidden common cause.

**Causal decision theory (CDT)** instead uses an intervention on the physical action:

\[
a_{\mathrm{CDT}}\in\arg\max_a
\mathbb E[V\mid \operatorname{do}(\operatorname{Act}=a),X=x].
\]

In a causal model, this intervention replaces the action’s usual determining equation with \(\operatorname{Act}=a\), then propagates consequences along causal arrows. It does not change a prediction made yesterday merely because that prediction happens to correlate with today’s action.

A-FDT changes the intervention target. Let

\[
D_x=\mathsf{afdt}(\underline P,\underline G,\underline x)
\]

be a *variable in the agent’s model* representing the output of A-FDT on the indicated probability model \(P\), dependency graph \(G\), and observation history \(x\). The underlining indicates that the variable is indexed by representations of these inputs. The source’s Equation (4), using the assigned name, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)\in
\arg\max_{a\in A}
\mathbb E_P\!\left[
V\mid\operatorname{do}(D_x=a)
\right].
}
\tag{1}
\]

The symbol after the conditioning bar denotes an intervention, not ordinary Bayesian conditioning. The graph \(G\) must encode not only causal relationships but also relevant computational, logical, and other **subjunctive dependencies**.

The distinction between the variable \(D_x\) and the actual result of running the algorithm matters. To evaluate \(a\), the agent temporarily sets the *model variable* \(D_x\) to \(a\); after comparing all such hypotheticals, it returns an action. The hypothetical is a computational tool, not necessarily a belief that the algorithm could physically or mathematically have produced another result.

Equation (1) is self-referential: its model contains a variable representing the output of the procedure operating on that model. The paper appeals to self-representation techniques, including Kleene’s recursion theorem, to explain how a program can refer to its own description. That does not, by itself, solve every problem of constructing \(G\), guaranteeing termination, or assigning counterfactual probabilities.

## 2. What changes in an A-FDT hypothetical?

A subjunctive dependency is a relationship that should be preserved when considering how a decision-function output might differ. The source treats ordinary causal dependence as one kind, but also includes cases in which two systems compute the same function or one system predicts the other.

For example, two accurate calculators computing the same sum need not communicate. Nevertheless, their outputs are related by their common computation. Likewise, if a predictor simulates an agent’s decision procedure accurately, the prediction should vary with the procedure’s output in the relevant hypothetical—even though the prediction physically precedes the action.

This is not a general rule that all correlations must be preserved. If a lesion independently causes both a desire to smoke and cancer, the lesion does not thereby compute the agent’s decision. Changing the decision-function output need not change the lesion or the cancer.

There is a philosophical complication. If a deterministic function on fixed inputs actually outputs \(a_1\), then its output cannot literally be \(a_2\) on those same inputs. An A-FDT hypothetical with \(D_x=a_2\) is therefore a **counterpossible**: its antecedent conflicts with a mathematical fact. Ordinary conditioning on a logically false statement does not automatically define such a hypothetical.

The paper does not supply a general counterpossible logic. Instead, Equation (1) assumes a graph that says how to propagate a stipulated change. This is a substantial input to the theory, not a consequence of writing down \(\operatorname{do}\). The paper identifies learning or constructing the correct subjunctive-dependency structure as a central open problem.

## 3. Newcomb’s problem

An opaque box contains either \$1,000,000 or nothing; a transparent box contains \$1,000. A predictor filled the opaque box if it predicted that you would take only that box. Assume, more specifically than the bare statement of overall accuracy, that under either candidate output the predictor matches that output with probability \(0.99\).

An A-FDT model can use these dependencies:

\[
D \longrightarrow \operatorname{Act},\qquad
D \longrightarrow \operatorname{Prediction}
\longrightarrow \operatorname{Box}
\longrightarrow V.
\]

The first arrow says the decision output determines the physical action; the second says the predictor’s model tracks that output. Prediction errors are represented separately.

Under the stipulated symmetric error model,

\[
\begin{aligned}
\operatorname{EU}(\text{one box})
 &=0.99(1{,}000{,}000)=990{,}000,\\
\operatorname{EU}(\text{two boxes})
 &=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. It does not claim that a physical act today sends a signal into the past. Rather, its two counterfactual models differ in both the decision output and the predictor’s earlier assessment.

By contrast, CDT holds the already filled or empty box fixed under a physical-action intervention. Whichever state the box is in, taking the additional \$1,000 is better, so CDT two-boxes. EDT can also one-box, but for a different reason: taking one box is evidence that the predictor likely filled it.

More generally, write

\[
p_1=P(\text{full}\mid\operatorname{do}(D=\text{one})),\qquad
p_2=P(\text{full}\mid\operatorname{do}(D=\text{two})).
\]

A-FDT one-boxes precisely when

\[
1{,}000{,}000(p_1-p_2)>1{,}000.
\]

This form is useful in unfamiliar problems: the relevant quantity is the *change in predicted box contents across interventions*, not merely the predictor’s reported accuracy on some unspecified population. Overall predictive accuracy alone does not establish \(p_1=0.99\) and \(p_2=0.01\).

## 4. A common cause is not a predictor

In the imaginary smoking-lesion problem, smoking itself does not cause cancer. An underlying lesion both makes smoking attractive and increases cancer risk. Suppose smoking gives the agent 1,000 utility, while avoiding cancer gives 1,000,000 utility.

A naïve EDT calculation can make smoking look bad because smokers are more likely to have the lesion. A-FDT, like CDT, distinguishes the action from its common cause. If intervening on the relevant decision output changes smoking but leaves the probability of cancer at \(p\), then

\[
\begin{aligned}
\operatorname{EU}(\text{smoke})&=1{,}000+1{,}000{,}000(1-p),\\
\operatorname{EU}(\text{refrain})&=1{,}000{,}000(1-p).
\end{aligned}
\]

Smoking wins by 1,000. This conclusion is about the stipulated imaginary case, not real-world smoking.

The source’s more elaborate model makes a further point. If the lesion changes the agent’s preferences, it may determine *which decision procedure or input* controls the action. An intervention on one procedure’s output changes behavior only in the cases where that procedure is actually used. The comparison can still favor smoking, but the expected gain is weighted by the probability that the intervened-on procedure controls the action.

The paper also cautions that the smoking-lesion story is awkward for EDT: agents with sufficient self-knowledge may screen off the evidential correlation, and maintaining the stipulated correlation can require contrived assumptions about the agent’s uncertainty. It recommends abandoning the example as a decisive test of EDT. Its value here is narrower: it illustrates why a correlation should not automatically be treated as a dependency on a decision output.

## 5. Observations can vary across hypotheticals

The most distinctive feature of Equation (1) is its treatment of observation. The equation does **not** simply add \(X=x\) as a condition after the intervention. Instead, the actual observation selects *which decision-function output* \(D_x\) to intervene on. In the resulting hypothetical, the observation itself may differ.

Consider transparent Newcomb. The predictor fills the opaque box if it predicts that the agent would leave the \$1,000 box behind *upon seeing both boxes full*. Let

\[
D_F=\text{decision output on seeing a full box},\qquad
D_E=\text{decision output on seeing an empty box}.
\]

The prediction depends on \(D_F\). The box contents determine which output is physically executed. Thus, when evaluating \(D_F\), A-FDT can consider worlds in which the box is empty and \(D_E\), rather than \(D_F\), controls the physical action.

Assume the predictor matches \(D_F\) with probability \(0.99\), and that the agent takes both boxes when the opaque box is empty. Then

\[
\begin{aligned}
\operatorname{EU}(\operatorname{do}(D_F=\text{one}))
 &=0.99(1{,}000{,}000)+0.01(1{,}000)
 =990{,}010,\\
\operatorname{EU}(\operatorname{do}(D_F=\text{two}))
 &=0.01(1{,}001{,}000)+0.99(1{,}000)
 =11{,}000.
\end{aligned}
\]

Thus, even when actually seeing a full box, A-FDT outputs “one box.” In the second hypothetical, the box is usually empty; the physical action is then controlled by \(D_E\).

This is deliberately different from saying, “Given that I see a full box, which action gives me more money?” On that condition, two-boxing gives an extra \$1,000. The A-FDT comparison instead evaluates the output of the procedure that would run *if* the full-box observation occurred, allowing the occurrence of that observation to depend on the output.

There is a notational inconsistency in the source’s detailed transparent-Newcomb calculation: it displays an intervention including an observation set to “full,” while its subsequent calculation explicitly allows the observation to be empty. The latter calculation is consistent with Equation (4) and the paper’s explanation that A-FDT changes the intervention target rather than conditioning on the observation. The analysis above follows that primary equation and the worked numerical reasoning.

This does not mean that A-FDT must disregard all evidence. A model may incorporate background information known to be unaffected by the output intervention. But deciding which evidence remains fixed and which is represented as a downstream observation requires modeling assumptions. Blindly conditioning on every present observation can erase the very dependency Equation (1) is meant to preserve.

## 6. Twins, coordination, and policies

In the psychological-twin prisoner’s dilemma, both participants run the same decision procedure on equivalent inputs. Both cooperating gives each \$1,000,000; both defecting gives each \$1,000. If one defects while the other cooperates, the defector gets \$1,001,000 and the cooperator gets nothing.

A-FDT represents both decisions as depending on the same output \(D\). Its comparison is therefore

\[
\operatorname{EU}(\text{cooperate})=1{,}000{,}000,\qquad
\operatorname{EU}(\text{defect})=1{,}000.
\]

It cooperates, not because cooperation causally forces the twin’s hand, but because both actions are implementations of the same computation. If the other player is only *approximately* similar, the graph should represent imperfect dependence. Calling someone a “twin” is not enough: differences in information, incentives, or reasoning can make their decision less responsive to the output being considered.

The source notes that its authors prefer a formulation that chooses a **policy** \(\pi:X\to A\), rather than a single action. For instance, a policy could specify both what to do when the box is full and what to do when it is empty. Optimizing an entire policy can coordinate choices across observations and agents. Equation (1), however, intervenes on \(D_x\), the output for one particular input. The two procedures need not agree in every multi-agent or sequential problem; a reader should not silently replace the action-level rule with policy optimization.

A policy comparison can nonetheless be a useful *additional modeling proposal*: specify a set of feasible policies, represent predictors as responding to those policies, and maximize expected utility under policy interventions. This requires decisions about policy identity, the intervention target, and what other computations change. Those details are not fixed by Equation (1).

## 7. Threats and the cost of being predictable

Consider the paper’s mechanical-blackmail problem. A blackmailer starts a program that will cause \$1,000,000 of damage unless the agent pays \$1,000. The blackmailer starts it only if she predicts the agent will pay. On receiving a letter, a CDT or ordinary EDT agent may see payment as the cheaper immediate outcome. A sufficiently reliable predictor can anticipate this and send the letter.

A-FDT instead intervenes on \(D_L\), the output of its decision procedure on receiving the letter. In a simplified model, suppose

\[
P(L\mid \operatorname{do}(D_L=\text{pay}))=1,
\qquad
P(L\mid \operatorname{do}(D_L=\text{refuse}))=\varepsilon.
\]

Assume payment costs \$1,000 if a letter arrives; refusal costs \$1,000,000 if one arrives; and there are no other costs. The hypothetical expected losses are

\[
\operatorname{Loss}(\text{pay})=1{,}000,\qquad
\operatorname{Loss}(\text{refuse})=1{,}000{,}000\varepsilon.
\]

A-FDT refuses when \(\varepsilon<0.001\), pays when \(\varepsilon>0.001\), and is indifferent at equality. Thus refusal is not an unconditional command to resist every threat. It depends on how strongly the threat’s occurrence responds to the decision output, as well as on the stakes.

The unsettling case is receiving the letter despite being the sort of agent who refuses. The source’s prescription is still to refuse when the above comparison favors refusal: in the refusal hypothetical, the letter is rare, although it is actually present. This is precisely where the global A-FDT perspective conflicts with an assessment that holds the observed threat fixed. It is also a reason to be cautious about transferring the example to practical threats, where prediction quality, the blackmailer’s incentives, and available remedies may be poorly known.

## 8. An operational recipe—and its limits

For an unfamiliar problem, the following is a practical interpretation of Equation (1), not a fully specified algorithm supplied by the paper.

1. **Identify the decision and its input.** Specify the candidate actions and the observation history \(x\). Introduce a model variable \(D_x\) for the output of the decision procedure on that input.

2. **Build a dependency model.** Include the physical action, outcomes, causal consequences, predictors, copies, and other observations where relevant. Distinguish evidence for a dependency from mere correlation.

3. **Specify intervention responses.** For each action \(a\), replace the equation for \(D_x\) with \(D_x=a\). Recompute variables modeled as dependent on it; leave unrelated variables governed by their original mechanisms. If a predictor is imperfect, specify its response probabilities under *each* intervention.

4. **Compute full-outcome utility.** Evaluate
   \[
   Q_x(a)=\mathbb E[V\mid\operatorname{do}(D_x=a)].
   \]
   Include branches where the observation changes and another decision output controls behavior, if the model permits them.

5. **Choose a maximizer and check robustness.** Compare the result under plausible alternative graphs and predictor-response probabilities. Tie-breaking, model uncertainty, computational approximations, and the treatment of randomness need further specification.

This recipe makes the theory usable *conditional on a model*. It does not solve the hardest step: deciding which subjunctive arrows are justified. A perfect simulation of the same deterministic computation supplies a clear idealized case. For an imperfect human predictor, the strength and direction of the counterfactual response may be difficult to estimate. Observed association alone is insufficient, just as it is insufficient to identify causal effects without assumptions.

Randomization introduces another unresolved choice. A predictor might predict a distribution, a pseudorandom seed, or the realized action; an independent random draw may be inaccessible to it. These are different models and can yield different prescriptions. Similarly, a model with feedback between predictions and decisions may require a fixed-point or other solution rather than a simple acyclic graph.

The paper argues that A-FDT performs well in examples where outcomes depend on predicted actions, and suggests that it may outperform rivals in “fair” problems. It also acknowledges that fairness is not formally defined and that any theory can be deliberately penalized. Consequently, neither Equation (1) nor the examples establish universal superiority. Claims about nonnegative value of information or acting as one would have precommitted also require care outside the paper’s modeled cases, especially when action-level interventions do not reproduce a jointly optimized policy.

## Conclusion

A-FDT evaluates actions by intervening on the modeled output of the decision procedure, then propagating the dependencies that the model says matter. This permits it to distinguish a predictor from a common cause, to coordinate with sufficiently similar computations, and—in the paper’s formulation—to consider hypotheticals in which present observations would have differed.

Its strength and its open problem are the same: the answer depends on an adequate account of subjunctive dependence. Given such a model, Equation (1) provides a definite expected-utility comparison. Constructing and justifying that model, particularly for imperfect predictors and counterpossible computations, remains a substantive research task.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially Sections 3–6. https://arxiv.org/abs/1710.05060