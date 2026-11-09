# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

This essay explains **action functional decision theory**, which I will call **A-FDT**, using Equation (4) of Section 5 of the supplied paper as the primary formal statement. A-FDT is a decision theory for agents who must choose in environments containing predictors, copies, twins, simulations, or other agents whose behavior depends on what the agent’s decision procedure would output. Its central idea is simple: a rational agent should not ask only which physical act has the best consequences, nor which act would be best news. She should ask which *output of her own fixed decision function* would produce the best outcome.

A-FDT is distinct from **evidential decision theory** (EDT) and **causal decision theory** (CDT). EDT evaluates actions by conditioning on them as evidence. CDT evaluates actions by intervening on a physical action variable while holding upstream causes fixed. A-FDT instead intervenes on a variable representing the output of the agent’s decision procedure itself. This lets A-FDT preserve decision-relevant logical and computational dependencies that CDT discards, while avoiding merely evidential correlations that EDT mistakenly respects.

## 1. The core idea: decisions as outputs of a function

A-FDT treats an agent’s decision process as a mathematical function. Roughly, the function takes as input the agent’s model of the world and her observations, and returns an action. The normative question is:

> Which output of this very decision procedure would yield the best outcome?

This differs from CDT’s question, “Which physical act of mine causes the best outcome?” and EDT’s question, “Which physical act of mine would be the best news to hear I took?”

The difference matters when other parts of the world depend on the agent’s decision procedure. Suppose an agent faces a prisoner’s dilemma against a psychological twin who reasons in exactly the same way. The twin’s choice is not caused by the agent’s choice, so CDT treats the choices as independent. But the two agents are computing the same decision function. If the function outputs “cooperate,” both cooperate; if it outputs “defect,” both defect. A-FDT evaluates these two possibilities and chooses the output that gives the better result.

The supplied paper calls this kind of relation **subjunctive dependence**. Two systems subjunctively depend on a function when their behavior is constrained to agree insofar as they correctly compute or predict that function’s output. The paper’s calculator analogy is useful: two reliable calculators computing the same sum on opposite sides of the world will output the same number, even though neither causes the other. Causal dependence is a special case of subjunctive dependence, but mere statistical correlation is not. A lesion that causes both a preference for smoking and cancer may make smoking evidence of cancer, but the lesion does not compute or predict the agent’s decision. A-FDT must treat these cases differently.

## 2. The formal rule: Equation (4)

Let \(P\) be the agent’s probabilistic world-model. Unlike an ordinary Bayesian model that only represents physical events, \(P\) includes variables for mathematical and computational facts, including the outputs of decision procedures. Let \(G\) be a dependency graph describing how variables depend on one another. In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must also encode logical, computational, and other subjunctive dependencies.

Let \(x\) be the agent’s current observation or observation history. Let

\[
\operatorname{afdt}(\underline P,\underline G,\underline x)
\]

be a variable in \(P\) representing the output of the A-FDT procedure itself when run on inputs \(P\), \(G\), and \(x\). The underlines indicate “dequoting”: the variable’s name refers to the very model and inputs being used. This is self-referential, but the source notes that such self-reference can be handled by standard fixed-point or “quining” techniques. The agent does not need to know the value of the variable in order to represent it.

The primary formal statement of A-FDT is then the following adaptation of the paper’s Equation (4):

\[
\tag{4}
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E_P\!\left[
V
\;\middle|\;
\operatorname{do}\!\left(
\operatorname{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

Here:

- \(\mathcal A\) is the finite set of available actions.
- \(V\) is the utility-valued outcome variable.
- \(\operatorname{do}(\cdot)\) is an intervention operator, borrowed from Pearl-style causal modeling, but applied to a logical or computational variable.
- The expectation is taken over the hypothetical distribution obtained by setting the decision-function output to \(a\) and propagating the consequences through \(G\).

The rule says: for each candidate action \(a\), imagine the world that would obtain if the agent’s decision function output \(a\), given the dependency structure \(G\). Compute the expected utility of that hypothetical world. Choose the action whose hypothetical world has highest expected utility.

This is not ordinary Bayesian conditioning. A-FDT does not ask, “What is likely given that I do \(a\)?” It asks, “What would the world look like if the decision function that produces my action had output \(a\)?”

## 3. Interventions on logical variables

In Pearl’s CDT, \(\operatorname{do}(\text{Act}=a)\) severs the incoming causal arrows to the action variable and propagates the intervention forward along causal arrows. Variables upstream of the action are held fixed. Thus, in Newcomb’s problem, CDT holds the predictor’s prediction fixed when evaluating one-boxing versus two-boxing.

A-FDT performs an analogous surgery, but on a different variable: the output of the decision function. If the predictor’s prediction depends on that function, then the prediction changes when the function’s output is changed. If a lesion does not depend on that function, then the lesion remains fixed.

This is the crucial structural difference:

- EDT conditions on the action, preserving all correlations.
- CDT intervenes on the physical action, preserving causal downstream consequences but breaking correlations with predictors and upstream causes.
- A-FDT intervenes on the decision function’s output, preserving dependencies that flow from the same computation or reliable prediction.

The source summarizes this by saying that A-FDT’s hypotheticals preserve decision-relevant subjunctive dependencies, while CDT’s hypotheticals preserve only causal dependencies.

There is an important technical cost. If the agent’s decision function in fact outputs \(a\), then evaluating a different output \(b\) requires considering a counterpossible scenario: a scenario in which the same function, on the same input, outputs something other than its actual output. The source openly acknowledges that we lack a fully satisfactory formal semantics for such counterpossibles. Equation (4) therefore works only given a graph \(G\) that correctly says how changing the logical variable would affect other variables. Constructing such a graph is the largest open problem for the theory.

## 4. How A-FDT treats observations

A subtle feature of Equation (4) is that the observation \(x\) appears inside the intervened variable:

\[
\operatorname{afdt}(\underline P,\underline G,\underline x).
\]

The paper emphasizes that A-FDT responds to observations differently from CDT. CDT updates by conditioning its model on \(\text{Obs}=x\). A-FDT instead changes which decision-function node it intervenes on. If the observation changes from \(x\) to \(y\), A-FDT changes from intervening on

\[
\operatorname{afdt}(\underline P,\underline G,\underline x)
\]

to intervening on

\[
\operatorname{afdt}(\underline P,\underline G,\underline y).
\]

This matters in problems where the observation itself is affected by what the decision procedure would have output. In the transparent Newcomb problem, for example, an agent sees whether the opaque box is full before choosing. If the agent sees a full box, A-FDT does not simply condition on “the box is full” and then compare one-boxing with two-boxing. Instead, it asks what would happen if the decision procedure for agents who see a full box output one-box versus two-box. If it output two-box, a reliable predictor would usually have predicted that, leaving the box empty. So the counterfactual in which the full-box procedure outputs two-box is largely a counterfactual in which the agent sees an empty box.

The source’s later discussion sometimes writes an observation condition alongside the intervention, but the core rule in Equation (4) treats the observation as an input to the function being intervened on. For practical use, I take the following operational interpretation: background observations used to build \(P\) and \(G\) may be conditioned on in constructing the model, but the current decision-relevant observation should not be held fixed by evidential conditioning if that observation is itself subjunctively dependent on the decision function. This interpretation is not explicitly fully formalized in the source, but it follows from the paper’s insistence that A-FDT changes the intervention target rather than merely conditioning.

## 5. Actions and policies

Equation (4) chooses an action for a given observation. However, the source notes that a more general formulation chooses a **policy**: a function from observations to actions. This is especially important in sequential problems, multi-agent problems, or cases where the agent must consider what she would do under observations she does not currently have.

A policy version of A-FDT can be written as:

\[
\pi^*
=
\arg\max_{\pi}
\mathbb E_P\!\left[
V
\;\middle|\;
\operatorname{do}\!\left(
\forall x:\operatorname{afdt}(\underline P,\underline G,\underline x)=\pi(x)
\right)
\right].
\]

The agent then executes \(\pi^*(x)\), where \(x\) is her actual observation.

This policy formulation is not the primary Equation (4), but it is a natural operational extension and is mentioned in the source as the authors’ preferred formulation in some contexts. It avoids having to make arbitrary assumptions about what the agent would do in unobserved branches. For example, in transparent Newcomb, the agent may need to know what she would do upon seeing an empty box while evaluating what to do upon seeing a full box. A policy tells her that directly.

In what follows, I will mostly discuss action-level choices, since Equation (4) is the assigned formal presentation, but I will note when policy reasoning clarifies the case.

## 6. Example: Newcomb’s problem

In Newcomb’s problem, an agent faces a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or nothing. A highly reliable predictor has already predicted whether the agent will take both boxes or only box B. Box B was filled iff the predictor predicted one-boxing.

EDT one-boxes because one-boxing is good evidence that box B is full. CDT two-boxes because the predictor has already left, so taking box A seems to add \$1,000 regardless of what is in box B.

A-FDT models the predictor as depending on the output of the agent’s decision function. Let \(D = \operatorname{afdt}(\underline P,\underline G,\underline x)\). The graph has arrows from \(D\) to the agent’s physical action and to the predictor’s prediction. The prediction determines whether box B is full.

Suppose the predictor is 99% accurate. If A-FDT intervenes on \(D=\text{onebox}\), then:

- the agent almost surely one-boxes;
- the predictor almost surely predicted one-boxing;
- box B is almost surely full.

The expected utility is approximately

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes on \(D=\text{twobox}\), then:

- the agent almost surely two-boxes;
- the predictor almost surely predicted two-boxing;
- box B is almost surely empty.

The expected utility is approximately

\[
0.99 \cdot \$1{,}000 + 0.01 \cdot \$1{,}001{,}000
=
\$11{,}000.
\]

A-FDT chooses one-boxing.

This is not because A-FDT thinks the current physical action causally changes the past. It is because A-FDT treats the predictor’s prediction as subjunctively dependent on the same decision function. To imagine the decision function outputting two-box is to imagine a world in which the predictor likely predicted two-boxing.

## 7. Example: the smoking lesion problem

In the smoking lesion problem, smoking is correlated with lung cancer, but only because a lesion causes both a preference for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and strongly disvalues dying of cancer.

EDT refrains from smoking because smoking is bad news: it is evidence of the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The key is that the lesion is not a predictor, simulator, or copy of the agent’s decision function. It is a common cause of smoking preference and cancer, but it does not compute the agent’s decision. In an A-FDT graph, the decision-function variable affects the action, but it does not affect the lesion or the cancer. Therefore, intervening on the decision function to output “smoke” changes whether the agent smokes but leaves the probability of cancer unchanged. Smoking adds \$1,000 in either cancer state.

The supplied paper gives a more careful model in which the lesion may alter the agent’s utility function, producing two possible decision functions depending on whether the agent has the lesion. But the important structural point remains: the cancer variable is not downstream of the decision-function variable. A-FDT therefore does not try to “manage the news” by avoiding smoking.

This example shows that A-FDT is not simply EDT with logical language added. It breaks merely evidential correlations when those correlations do not reflect subjunctive dependence.

## 8. Example: the psychological twin prisoner’s dilemma

Consider the psychological twin prisoner’s dilemma. The agent and her twin choose separately. If both cooperate, each gets \$1,000,000. If both defect, each gets \$1,000. If one defects while the other cooperates, the defector gets \$1,001,000 and the cooperator gets nothing. The agents know they reason in the same way.

CDT defects because the twin’s choice is causally independent. EDT cooperates because cooperation is good news. A-FDT cooperates for a reason closer to CDT’s counterfactual style: it imagines different outputs of the shared decision procedure.

If the shared decision function outputs “cooperate,” both cooperate and each receives \$1,000,000. If it outputs “defect,” both defect and each receives \$1,000. Since the first hypothetical is better, A-FDT outputs “cooperate.”

If the twin is only imperfectly similar, the graph can represent a probability that the twin’s action matches the output of the agent’s decision function. A-FDT then maximizes expected utility using that probability. The essential requirement is that the model represent the relevant dependency between the twin’s reasoning and the agent’s decision function.

## 9. Example: transparent Newcomb and Parfit’s hitchhiker

A-FDT’s most striking behavior appears in the transparent Newcomb problem. Both boxes are transparent. The predictor filled box B iff she predicted that the agent would one-box upon seeing that both boxes are full. The agent sees that box B is full. Should she one-box?

CDT says two-box, because the box is already full. EDT also says two-box, because conditional on seeing a full box, taking both yields more money. A-FDT says one-box.

Let \(D_{\text{full}}\) be the output of the decision procedure for agents who see a full box, and let \(D_{\text{empty}}\) be the output for agents who see an empty box. The predictor’s prediction determines which observation the agent receives.

If A-FDT intervenes on \(D_{\text{full}}=\text{onebox}\), then with high probability the predictor predicted one-boxing, box B is full, the agent sees a full box, and she one-boxes. The expected utility is close to \$1,000,000.

If A-FDT intervenes on \(D_{\text{full}}=\text{twobox}\), then with high probability the predictor predicted two-boxing, box B is empty, and the agent sees an empty box. In that branch, her action is controlled by \(D_{\text{empty}}\), not \(D_{\text{full}}\). The high payoff occurs only in the small probability branch where the predictor erred. Thus two-boxing has much lower expected utility.

A-FDT one-boxes even while seeing a full box. The source argues that this is equivalent to paying the driver in Parfit’s hitchhiker problem. In Parfit’s case, a driver saves the agent iff she predicts the agent will pay \$1,000 after reaching the city. Once in the city, CDT and EDT refuse to pay, so the driver predicts refusal and leaves them to die. A-FDT pays, because the policy of paying is what causes the driver to help.

This may seem counterintuitive. The source defends it with three arguments: A-FDT acts as it would be rational to precommit to act; it does not assign negative value to information; and it achieves higher utility in predictor environments. The paper’s strongest claim is pragmatic: A-FDT works in these problems, whereas CDT and EDT predictably end up poorer or dead in the desert.

## 10. Example: blackmail and extortion

A-FDT also resists certain forms of blackmail. Suppose a predictor sends a blackmail letter only if she predicts the agent will pay. The letter’s arrival may be good news in an evidential sense: conditional on receiving it and paying, some bad fact may be false. EDT can be led to pay because paying makes the bad fact less likely conditional on the letter.

A-FDT refuses if payment is triggered by the predictor’s prediction of payment. When A-FDT imagines the decision function outputting “pay upon receiving the letter,” it also imagines the predictor sending the letter. When it imagines outputting “refuse upon receiving the letter,” it imagines the predictor not sending the letter, or sending it only in rare error cases. The agent’s actual receipt of the letter is not simply conditioned away; rather, the counterfactual evaluates how the decision function’s output affects whether the letter is sent.

This illustrates the more general point: A-FDT avoids making itself predictable prey for predictors who condition their behavior on the agent’s expected response.

## 11. A practical recipe for unfamiliar cases

The paper presents A-FDT at an idealized level. To use it in an unfamiliar case, one needs a model \(P\), a dependency graph \(G\), and a way to evaluate interventions. The source supplies the formal rule but not a full method for constructing \(G\). The following operational recipe is my attempt to make the theory usable while staying close to the source.

1. **Identify the decision function.**  
   Specify the function whose output is the agent’s action given her model and observations. In self-referential settings, this function includes the very reasoning process being used.

2. **List the candidate actions or policies.**  
   For simple one-shot problems, use actions. For sequential or observation-dependent problems, use policies.

3. **Draw the dependency graph.**  
   Include causal arrows where appropriate. Also include subjunctive arrows from the decision-function output to variables that compute, simulate, predict, or reliably depend on that output. Do not draw subjunctive arrows to variables that are merely statistically correlated with the action.

4. **For each candidate output, intervene on the decision-function variable.**  
   Set \(\operatorname{afdt}(\underline P,\underline G,\underline x)=a\), or set the whole policy \(\pi\), and propagate the consequences through the graph.

5. **Compute expected utility in each hypothetical.**  
   Use the resulting distributions over outcomes.

6. **Choose the action or policy with highest expected utility.**

This recipe makes clear where additional assumptions enter. The source gives the formal maximization rule, but it does not give a complete account of how to learn or justify \(G\). In practice, one must use substantive assumptions about prediction, simulation, shared reasoning, and logical dependence.

## 12. Dominance, regret, and counterfactuals

CDT often appeals to dominance: two-boxing in Newcomb’s problem seems to dominate one-boxing because, holding the predictor’s prediction fixed, taking both boxes is always better. A-FDT rejects this dominance argument as question-begging. It says that holding the predictor’s prediction fixed while changing the output of the decision function is like asking us to imagine a calculator computing \(6288+1048\) but outputting a different number while holding the arithmetic fixed.

A-FDT has its own dominance notion: action \(a\) dominates action \(b\) if, holding fixed the relevant subjunctive dependency structure, changing the decision function’s output from \(b\) to \(a\) is never worse and sometimes better. In Newcomb’s problem, two-boxing does not dominate one-boxing under this notion, because changing the decision function’s output also changes the prediction.

This also explains why A-FDT avoids certain forms of regret. In Death in Damascus, a CDT agent flees because her hypotheticals imagine Death’s location fixed while her own location changes. But if Death perfectly predicts her decision procedure, fleeing does not improve survival; it only wastes money. A-FDT recognizes that Death’s location subjunctively depends on her decision function, so it does not generate unstable recommendations.

## 13. Open problems and uncertainty

A-FDT is elegant, but several parts are not fully settled.

First, the source does not provide a general method for constructing the dependency graph \(G\). CDT can appeal to Pearl’s theory of causal discovery. A-FDT needs an analogous theory of logical, computational, and subjunctive dependency discovery. The paper explicitly identifies this as a major open problem.

Second, A-FDT relies on counterpossible reasoning. If the actual decision function outputs one action, evaluating another output requires imagining a logically contrary-to-fact change. The source notes this difficulty and argues that humans manage such reasoning in practice, but a fully formal account is lacking.

Third, the treatment of observations in Equation (4) is terse. The equation places the observation inside the intervened function rather than as a separate condition. I believe this is the correct reading, especially for transparent Newcomb and blackmail cases, but the source’s occasional notational ambiguity means that some operational details require interpretation.

Fourth, the action-level formulation may be incomplete for multi-agent or sequential problems. The source’s footnote about preferring policies suggests that the most robust version of A-FDT evaluates policies rather than isolated actions. I regard the policy formulation as a reasonable and likely necessary operational extension, though Equation (4) remains the assigned core rule.

Finally, the source’s claim that A-FDT outperforms EDT and CDT is restricted to “fair” problems: problems where the environment rewards or punishes the agent’s behavior, not the mere identity of her decision theory. One can always construct a problem that punishes agents for using A-FDT specifically. That does not refute the theory any more than a problem that punishes CDT refutes CDT.

## Conclusion

Action functional decision theory evaluates choices by asking which output of the agent’s own decision function would lead to the best expected outcome. Its formal core is a Pearl-style intervention, not on the physical action variable, but on a variable representing the output of the agent’s decision procedure:

\[
\mathrm{A\text{-}FDT}(P,G,x)
=
\arg\max_{a \in \mathcal A}
\mathbb E_P\!\left[
V
\mid
\operatorname{do}\!\left(
\operatorname{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

This simple change has large consequences. A-FDT one-boxes in Newcomb’s problem because the predictor subjunctively depends on the decision function. It smokes in the smoking lesion problem because the lesion does not. It pays in Parfit’s hitchhiker problem and one-boxes in transparent Newcomb because it evaluates the policy that makes predictors help it. It resists blackmail because it recognizes that being the kind of agent who pays can cause blackmail attempts.

The theory is not yet complete. It needs a better account of subjunctive dependency graphs, counterpossible reasoning, logical uncertainty, and policy selection. But its central insight is powerful: in environments containing predictors, copies, and other reasoners, rational action is not just about what your body does here and now. It is about what the mathematical function you are running should output.

## References

Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). Supplied reference article, arXiv:1710.05060.