# A-FDT: Decisions as outputs of a function

A decision can affect the world in more ways than a physical act’s immediate consequences suggest. A reliable predictor may have acted yesterday on a model of what you will choose today. A copy of your decision procedure may be running in another room. Neither circumstance requires information to travel backward in time or between sealed rooms. Yet in both, your choice and another event may be linked by the computation that produces them.

**Action functional decision theory (A-FDT)** takes such links seriously when evaluating actions. Its central question is not merely “What would happen if my body performed action \(a\)?” but “What would the world be like if this decision procedure, on these inputs, output \(a\)?”

This essay uses Equation (4) of Section 5 of Yudkowsky and Soares’s *Functional Decision Theory* as the primary definition of A-FDT. The paper itself uses the broader name “FDT” and notes that its authors prefer a policy-based formulation in some settings. Here, **A-FDT** names the action-output formulation given by that equation. Where a policy interpretation is useful, I will identify it as an additional construction rather than silently substituting it for the equation.

## 1. Three perspectives on expected utility

Let \(\mathcal A\) be a finite set of actions, \(O\) an outcome, and \(U(O)\) its utility. Write \(V=U(O)\), and let \(x\) be the agent’s observation history. Expected-utility theories agree, at a high level, that an agent should choose an action with the greatest expected utility. They differ in what probability distribution represents the consequences of an alternative action.

**Evidential decision theory (EDT)** evaluates an action as news:

\[
\operatorname{EDT}(P,x)
\in \arg\max_{a\in\mathcal A}
\mathbb E_P[V\mid X=x,A=a].
\]

It asks what an agent should expect upon learning that she takes \(a\). In the paper’s formulation, an action assigned probability zero cannot be evaluated by this conditional.

**Causal decision theory (CDT)** instead evaluates a physical intervention:

\[
\operatorname{CDT}(P,G,x)
\in \arg\max_{a\in\mathcal A}
\mathbb E_P[V\mid \operatorname{do}(A=a),X=x].
\]

Here \(G\) specifies causal structure. The intervention sets the physical action to \(a\), propagates its causal effects, and does not automatically alter its causes or mere correlates.

A-FDT also uses intervention, but its target is different. Let

\[
D_x=\mathsf{afdt}(\underline P,\underline G,\underline x)
\]

be a variable *in the agent’s model* representing the output of the A-FDT procedure on the specified inputs. Underlining indicates that the variable’s name refers to those inputs. Equation (4), expressed using the assigned name, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid
\operatorname{do}(D_x=a)\right].
}
\tag{A-FDT}
\]

The graph \(G\) now represents decision-relevant **subjunctive dependencies**, not just physical causal dependencies. The intervention changes the represented output of the decision function and propagates the consequences through that graph.

Two distinctions are essential.

First, \(D_x\) is a *model variable*. It is not itself the action returned by the procedure. The agent manipulates a representation of the output in order to calculate which output to return.

Second, Equation (4) has no additional condition \(X=x\) to the right of the intervention. Observation \(x\) selects *which decision-output variable* is intervened on. A counterfactual in which \(D_x\) has a different value may contain histories in which \(x\) is not observed at all. This feature drives the paper’s transparent-box and blackmail examples.

The source presents hypotheticals as tools constructed from beliefs, not as claims that an agent can physically alter the past or change mathematical truth. Still, using such tools requires a model of what changes under an intervention—and that is the most difficult unresolved part of the theory.

## 2. Subjunctive dependence and counterpossibility

Suppose two reliable computers run the same deterministic program on the same input. Their outputs agree, even if the computers are physically isolated. If we consider what their outputs would be *if that computation returned a different answer*, we should normally change both outputs together. By contrast, two computers may happen to have the same casing color without their colors depending on the same computation.

The paper calls the relevant relationship **subjunctive dependence**. It includes ordinary causal dependence but is broader: a prediction or another implementation of a computation can depend on the computation’s output without being caused by the agent’s later physical action. Mere statistical correlation does not by itself establish such dependence.

A-FDT’s intervention is often **counterpossible**. If a deterministic function on fixed inputs actually returns \(a_1\), then, as a mathematical fact, it does not return \(a_2\). Nevertheless, the agent needs to compare a hypothetical in which its represented output is \(a_2\). Ordinary Bayesian conditioning is not enough: a logically false proposition has probability zero for a logically omniscient agent, and conditioning on it is undefined.

The paper proposes using an extended graph and a \(\operatorname{do}\)-style operation as a working substitute for a general logic of counterpossibles. This is a formal *interface*: given a suitable \(G\), Equation (4) tells us how to score actions. It is not a complete method for discovering \(G\), or a proof that every relevant logical relationship can be represented adequately in a Pearl-style graph.

Self-reference is also present. The model contains a variable naming the output of the procedure that is using the model. The paper appeals to standard self-reference techniques to explain how a procedure can represent itself. That addresses the possibility of naming the computation; it does not by itself solve the harder question of which counterfactual dependencies should be encoded.

## 3. Newcomb’s problem: intervening on the decision output

In Newcomb’s problem, an opaque box contains either \$1 million or nothing. A transparent box contains \$1,000. A predictor has filled the opaque box if she predicted that the agent would take only that box. The prediction was made before the agent chooses.

Consider the paper’s simple model: the predictor matches the output \(D\) with probability \(0.99\), and otherwise predicts the other action. The agent’s physical action and the prediction both depend on \(D\):

\[
D\longrightarrow A,
\qquad
D\longrightarrow \text{Prediction}
\longrightarrow \text{Box contents}.
\]

The first arrow need not represent the same sort of physical causation as every other arrow. It records the dependence needed for constructing the A-FDT hypothetical.

Under an intervention setting \(D\) to one-box, the opaque box is full with probability \(0.99\). Under an intervention setting \(D\) to two-box, it is full with probability \(0.01\). Thus, with dollars treated as linear utility,

\[
\begin{aligned}
Q(\text{one-box})&=0.99(1{,}000{,}000)=990{,}000,\\
Q(\text{two-box})&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. CDT, in contrast, holds the already-filled box fixed when changing the physical act, and therefore takes the additional \$1,000. EDT can one-box because one-boxing is evidence that the prediction was favorable, but it reaches that conclusion through conditionalization rather than the computational dependency.

The numerical conclusion depends on the model. If predictor accuracy is symmetric and equal to \(r\), then

\[
Q(\text{one-box})=rM,\qquad
Q(\text{two-box})=(1-r)M+b,
\]

where \(M\) is the large reward and \(b\) the small-box reward. One-boxing is preferred exactly when

\[
(2r-1)M>b.
\]

Thus A-FDT does not say that every purported predictor should be treated as perfect. It requires a model of how the prediction responds to the decision output, including errors.

## 4. Why a lesion is different

In the imaginary smoking-lesion problem, a lesion makes smoking attractive and also makes cancer likely. Smoking itself does not cause cancer, and the agent receives a benefit from smoking. Action and cancer can therefore be correlated because of a common cause.

In a simplified A-FDT model, intervening on the decision output changes whether the agent smokes but not whether she has the lesion. If \(p\) is the probability of survival and smoking gives utility \(b>0\), then

\[
Q(\text{smoke})=pM+b,\qquad
Q(\text{refrain})=pM.
\]

A-FDT smokes. It does not infer from an intervention on its decision output that the biological lesion must change. An EDT agent whose action remains strongly correlated with the lesion may instead refrain because smoking is bad news about cancer.

There is a qualification. The paper’s fuller model allows the lesion to determine which utility function—and hence which decision computation—the agent is running. An intervention on the output of one computation may affect the physical act only in the states where that computation controls it. In the paper’s example, the advantage of outputting “smoke” is \(p_{\!L}b\), where \(p_{\!L}>0\) is the probability of the relevant lesion state, rather than necessarily \(b\). The sign is unchanged.

The authors also acknowledge that the smoking-lesion setup is contrived and that refined versions of EDT can respond to it differently. Its main lesson is structural: **a predictive computation and a common biological cause should not automatically be modeled as the same dependency merely because they induce similar correlations.**

## 5. Observations can change in A-FDT hypotheticals

The distinctive treatment of observation becomes clear in *transparent* Newcomb. Both boxes are visible, and the predictor fills the large box if she predicts that the agent will one-box **upon seeing it full**.

Let \(D_F\) be the output of A-FDT on the observation “full,” and \(D_E\) its output on “empty.” The predictor targets \(D_F\). Box contents determine which observation occurs, and thus which output controls the physical act.

Assume again that the predictor matches \(D_F\) with probability \(0.99\), and let \(q\) be the probability that the agent two-boxes upon seeing the large box empty. Intervening on \(D_F\) yields

\[
\begin{aligned}
Q(D_F=\text{one-box})
&=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
Q(D_F=\text{two-box})
&=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first value is larger for every \(q\in[0,1]\), so A-FDT outputs one-box on seeing a full box. If it sees an empty box, taking both is preferable in the paper’s model: that choice does not change the prediction of what it would do on *full*.

Notice what happens in the second hypothetical above. Most of its probability lies on an empty box, so the agent there observes “empty” and follows \(D_E\), not the intervened-on output \(D_F\). This remains true even though the actual agent evaluating \(D_F\) sees a full box.

There is an apparent notational inconsistency in the paper: its worked transparent-box section displays an expression including an intervention on \(\mathrm{Obs}=\mathrm{full}\), but its surrounding explanation and numerical calculation allow the box to be empty. The calculation is consistent with Equation (4)’s **unconditioned** intervention on \(D_F\). That is the interpretation used here.

This approach is deliberately “global.” It does not mean that observing a full box is ignored when selecting which computation is being evaluated. It means that the observation is not held fixed across every hypothetical used to evaluate that computation.

## 6. Threats, prediction errors, and thresholds

The same structure appears in the paper’s mechanical-blackmail example. A blackmailer runs a damaging program only if she predicts that the agent would pay upon receiving a demand. If run, the program causes loss \(L\), unless the agent pays cost \(c\).

For a simple operational model, suppose:

* if the agent would pay, the blackmailer sends the demand with probability \(s\);
* if the agent would refuse, she sends it with probability \(t\);
* when sent, payment costs \(c\), and refusal costs \(L\);
* there are no other effects.

The relevant decision-output variable is the action *upon receiving the demand*. Its A-FDT scores are

\[
Q(\text{pay})=-sc,\qquad Q(\text{refuse})=-tL.
\]

Refusal is preferred when

\[
tL<sc.
\]

For example, if \(s=1\), \(c=1{,}000\), \(L=1{,}000{,}000\), and \(t=0.0009\), expected losses are \$1,000 for paying and \$900 for refusing. A-FDT therefore refuses even in the rare case where the demand actually arrives.

This is not a general recommendation to refuse threats. If \(t=0.01\), refusal has expected loss \$10,000 and payment is better under these assumptions. Nor is the inequality valid if the blackmailer’s behavior, the loss, or other relevant outcomes respond differently. The theory’s prescription is sensitive to the model of the predictor—not to a slogan such as “never pay.”

Parfit’s hitchhiker has a similar form. A driver offers rescue only if she predicts that the passenger will pay after reaching the city. With a sufficiently reliable predictor and a large value for rescue, A-FDT pays in the city: the hypothetical where its city-payment computation refuses is one where rescue was unlikely. CDT and standard EDT, conditioning on already being safe, normally assess the payment as an avoidable cost.

## 7. Applying A-FDT to an unfamiliar case

Equation (4) is compact; using it responsibly requires explicit modeling. The following is an **operational proposal**, guided by the paper rather than a uniquely specified algorithm in it.

1. **Define the decision and utility.** List feasible actions, the observation \(x\), outcomes, and utility. Include relevant future costs, benefits, and other agents’ responses.

2. **Identify the output variable \(D_x\).** It represents the output of this decision procedure on these inputs. Distinguish it from the physical action and from outputs on other observations.

3. **Model dependencies.** Include physical effects of the action, predictors of \(D_x\), and other computations whose outputs depend on the same decision. Do not add such a link merely because two events are correlated.

4. **Specify uncertainty in each intervention.** For each \(a\), state how predictor errors, randomization, and environmental variables behave under \(\operatorname{do}(D_x=a)\). In particular, an observed prediction accuracy alone may not determine the predictor’s response under every alternative output.

5. **Propagate and compare.** Recompute downstream variables, including observations and which decision-output variable controls the eventual act. Calculate
   \[
   Q_x(a)=\mathbb E[V\mid\operatorname{do}(D_x=a)]
   \]
   and choose a maximizing action. A tie-breaking rule is an additional implementation choice.

6. **Test the model.** Vary uncertain dependencies and probabilities. If small plausible changes reverse the answer, report the prescription as model-sensitive rather than a robust theorem.

This procedure also guards against an overextension of the twin argument. Against a perfect psychological twin in the paper’s prisoner’s dilemma, cooperation yields \$1 million and defection \$1,000, because both outputs change together. Against an unrelated opponent who independently defects, the same graph is unjustified. Similarity of situation or aspiration is not proof of shared computation.

Randomization needs comparable care. A copied algorithm using a shared random seed may produce linked actions; copies using independent private randomness need not. A-FDT’s equation alone does not specify which random variables are shared or what a predictor can observe. Those are modeling assumptions.

## 8. Actions, policies, and open problems

A **policy** is a map \(\pi:x\mapsto a\). The paper notes that its authors prefer a policy-output formulation, especially for some multi-agent dilemmas. One possible policy-level analogue is

\[
\pi^\star\in\arg\max_{\pi}
\mathbb E[V\mid\operatorname{do}(D_{\mathrm{policy}}=\pi)],
\qquad
a=\pi^\star(x).
\]

This is not Equation (4). It requires a new output variable and assumptions about how changing a whole policy affects predictors, other agents, and observations. It can be useful when one predictor evaluates several branches together, but it need not agree with separate interventions on individual \(D_x\) nodes. The paper does not provide a general equivalence theorem.

Several broader questions remain open:

* **Graph construction.** How should an agent infer logical and computational dependence from limited evidence? A predictor can be accurate in observed cases while responding differently to an unfamiliar intervention.
* **Counterpossible semantics.** Which mathematical relationships remain fixed when one function’s output is counterfactually changed? Graph surgery supplies local answers only after the graph is chosen.
* **Computational limits and self-reference.** Representing one’s own procedure is not the same as solving an arbitrarily large self-referential model.
* **Performance guarantees.** The authors argue that their theory performs well in “fair” problems, where rewards depend on behavior in the problem rather than directly on the decision theory used. They acknowledge that fairness is not formally characterized and that no theory wins every constructed problem.

The paper also motivates its approach through precommitment and the value of information: in its examples, A-FDT behaves as an agent would have wanted to precommit to behave, without purchasing a binding device. Those examples do not establish an unconditional theorem that every implementation of Equation (4) always has nonnegative information value or always matches an optimal prior policy. Such claims require assumptions about the model, available policies, and how information changes the decision computation.

## Conclusion

A-FDT evaluates an action by intervening on the represented output of the decision procedure, then following the causal and computational dependencies supplied by its model. This explains why it can one-box against a predictor, cooperate with a genuine twin, and avoid treating a mere common-cause correlation as something its decision controls.

The rule is precise **conditional on a suitable dependency model**. Finding and justifying that model—especially for imperfect predictors, distinct computations, and counterpossible alternatives—remains an essential part of applying the theory, not a problem the equation itself has already solved.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, Sections 3–6 and 9. [arXiv:1710.05060](https://arxiv.org/abs/1710.05060).