# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/05f1f02c-b330-4b6e-a5ce-41309873fdf9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/05f1f02c-b330-4b6e-a5ce-41309873fdf9/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a substantive mathematical essay/blog post explaining A-FDT (action functional decision theory), taking Equation (4), Section 5 of supplied paper as primary formal presentation. Use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories by distinct names. Need target approx 2400-3000 words including references. Need distinguish source claims from own assumptions/proposals. Need explain how theory evaluates alternative actions/policies and treats dependencies/counterfactuals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop/justify. Must not just answer one case. Need use examples. Need likely note source calls FDT, but we rename to A-FDT per assignment? Need be careful: "Use A-FDT consistently as the assigned decision theory's name, including headings and examples". So we should refer to A-FDT not FDT, maybe explain source calls it functional decision theory and for this essay we call it action functional decision theory (A-FDT). Need ensure quotations faithful. Need include Equation (4) as primary formal presentation. Equation (4) in source:
\FDT(P, G, x) := argmax_{a in A} E(V | do(FDTvar(underline P, underline G, underline x)=a)).
We need maybe adapt as A-FDT(P,G,x) = argmax ... E[V | Do(FDTvar(underline P, underline G, underline x)=a)]. Need perhaps mention observation x and note source says FDT responds to observation by changing intervention node, not conditioning. Need discuss policies footnote: source preferred formulation iterates over policies, but Eq (4) actions; assignment says Eq(4) primary, maybe mention policy variant as open/extension. But name A-FDT "action functional" maybe emphasizes action? Need maybe define action functional decision theory. Need use A-FDT consistently. Could discuss EDT, CDT. Need explain dependencies: subjunctive dependence, logical dependence, graph G encoding how changing logical variable affects other variables. Need open problem: no formal True operator or deducing G; source leaves constructing G open. Need propose operational interpretation: build dependency graph by treating predictors/twins/simulations as computations of same or relevant function; use policy-level intervention; use "logical intervention" on decision function output. Maybe propose a practical recipe: identify decision function D = A-FDT(P,G,x), identify all variables in model that are computed from or reliably predict that output (same algorithm, simulations, predictors, copies, common code), set D=a, propagate through structural equations respecting logical/computational/causal constraints, compute expected utility. Distinguish this as my operational gloss. Need mention counterpossibles: if actual output is a, evaluating b requires imagining D outputs b though actually it doesn't; source acknowledges lack of satisfactory counterpossible account. Need discuss self-reference and quining. Need examples: Newcomb, Smoking Lesion, Transparent Newcomb / Parfit's Hitchhiker, maybe twin PD, XOR blackmail or Death in Damascus. Need keep word count 2400-3000. Need maybe 2600 words. Need include references brief. Need no appendices. Need headings. Need finish conclusion.

Need think about exact interpretation of Equation (4). Source has subtlety: CDT equation conditions on Obs=x: E(V | Do(Act=a), Obs=x). FDT equation (4) as displayed in source lacks Obs conditioning? It says compare equations: FDT responds to observation by changing node intervened upon. Equation (4): FDT(P,G,obs) := argmax_a E(V | Do(fdtvar(underline P, underline G, underline x)=a)). It may not condition on obs, because obs is encoded in node. In transparent Newcomb they evaluate E(V | Do(fdt(P,G,full)=a, Obs=full)? Actually text: "requires finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." There's missing parenthesis. But Eq(4) says no Obs condition. Need explain: In A-FDT, observations select which decision-function node is intervened on: the function with observation as input. In some graphical calculations one may also condition on the observation for variables not subjunctively affected? Source ambiguous. Need address: "Where implementation details are not determined ... explain what follows from source and what would require additional assumptions." Need mention Eq(4) underdetermines whether to additionally condition on Obs=x; source later seems to condition in transparent Newcomb. But main principle is observation changes intervention target. Need propose operational interpretation: condition on Obs=x only as an input-fixing constraint when evaluating node for that observation, but do not use it as evidential conditioning that overrides subjunctive consequences. Or use a graph with Obs downstream of predictor/decision; the intervention node includes x, so expected utility is over exogenous uncertainty conditional on x being the observed input? Need parse.

Let's examine source formalism: Section 5: Eq (2) EDT(P, obs) = argmax E(V | Obs=obs, Act=a). Eq (3) CDT(P,G,obs)=argmax E(V | Do(Act=a), Obs=obs). Eq (4) FDT(P,G,obs)=argmax E(V | Do(FDTvar(underline P, underline G, underline x)=a)). They explicitly say: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable FDTvar(P,G,x) to FDTvar(P,G,y) instead." So Eq(4) no Obs=obs condition. But in transparent Newcomb they write E(V | Do(FDTpgv{full}=a, Obs=full) maybe typo missing bracket. Actually: "evaluate FDT(Pf,Gf,full) ... involves finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." There is a missing closing ). Maybe they condition on Obs=full in addition? But earlier said not. Let's inspect: They might condition on Obs=full because need evaluate given she sees full? But if intervention on FDT(full) sets action if observation full, then the graph includes Prediction determining Obs and Act. If not condition on Obs=full, evaluating intervention on full-node includes worlds where predictor predicted two-box? Wait graph: two FDT nodes: full and empty. Act depends on FDT(full), FDT(empty), and Prediction; Prediction determines which of two nodes controls Act. If intervene Do(FDT(full)=onebox), not conditioning on Obs=full, expected utility includes cases where prediction inaccurate and Obs empty, where Act determined by FDT(empty). That's what their calculation did: for onebox: with accurate 0.99 get full and onebox; with inaccurate 0.01 Prediction=2, BoxB empty, Act determined by FDT(empty), utility q*1000. They didn't condition on Obs=full because they included inaccurate cases. But they mention Obs=full? Maybe because evaluating when observed full. But calculation uses unconditional over Accurate. They don't condition on Obs=full; if conditioned on full, inaccurate branch would be excluded (or weird). So Eq(4) is better. Need note this ambiguity and propose no extra evidential conditioning; observation appears as argument to decision function and perhaps fixes which branch actual agent is in, but evaluation integrates over counterfactual possibilities where observation would have been different due to different output. In transparent Newcomb, when seeing full, A-FDT still imagines if output were two-box, predictor likely wouldn't have put full, so she'd see empty. So observation is not held fixed as a post-intervention condition. Need say source's phrase with Obs=full is likely a notational slip or means the agent's current input is full. This is important.

Need define A-FDT maybe:
Given world model P over variables including logical variables, dependency graph G representing structural relationships (causal, logical, computational), observation x. Let D_{P,G,x} denote the output of A-FDT when run on (P,G,x), represented in P by variable fdt(underline P, underline G, underline x). Then A-FDT chooses:
A-FDT(P,G,x) = argmax_{a in A} E_P[ V | Do(fdt(underline P, underline G, underline x)=a) ].
If ties, any.
Need explain Do is Pearl intervention but applied to logical variable, requiring G to say how setting that logical output changes other variables. Since G includes non-causal edges, Do is generalized intervention; source reuses Pearl's Do given G. Need perhaps call it "dependency surgery".

Need define subjunctive dependence: two systems subjunctively depend on same function if their outputs are constrained to agree insofar as they correctly compute that function. Calculator analogy. Causal dependence special case. Statistical correlation not enough. A-FDT preserves correlations in hypotheticals that arise from shared computation or reliable prediction; breaks merely evidential correlations not grounded in such dependence. Need use examples:
- Newcomb: graph has node D = A-FDT(P,G,empty?) (no observation) causing Act and Prediction. Intervention on D sets Act and Prediction; expected utility onebox ~ $990k vs twobox ~ $11k; choose one-box.
- Smoking lesion: lesion causes preference/utility function and cancer, but cancer does not depend on D. Graph connects D to Act, lesion to Act (because if lesion, action controlled by D(P_S), if no lesion D(P_R)? Source complicated). Key: intervention on D doesn't change lesion/cancer, so smoking adds $1000; choose smoke. Need simplify: if lesion merely statistically correlates with smoking and cancer but does not compute/predict decision, A-FDT graph has no edge from decision-function output to cancer. So smoke.
- Transparent Newcomb / Parfit's Hitchhiker: observation full. Node D_full = A-FDT(P,G,full). Intervention on D_full=onebox makes predictor likely filled, so see full and onebox; D_full=twobox makes predictor likely empty, so actual observation would likely be empty and action controlled by D_empty. Expected utility onebox ~ $990k vs twobox ~ $11k + small; choose one-box/pay. Need explain observation treatment: when you see full, you don't condition on full and then compare; you ask what if the policy for seeing full output different; that changes whether you'd see full.
- Twin prisoner's dilemma: same decision function implemented by twin; intervene on shared function output, both cooperate/defect. Choose cooperate.
- XOR blackmail maybe optional: A-FDT refuses because paying changes whether letter sent, not infestation. Could show blackmail/resistance.
- Death in Damascus maybe mention stability: A-FDT sees Death's location depends on prediction of decision; staying saves $1000; no instability.

Need discuss evaluating policies: Source footnote says preferred formalization iterates over policies mappings from observations to actions; Eq(4) action-level but observation-indexed nodes approximate. For unfamiliar cases, A-FDT should evaluate policies: choose policy π that maximizes expected utility under intervention that the decision function outputs π (or that for each observation x, fdt(P,G,x)=π(x)). This matters when multiple observations or multi-agent. The assignment says take Eq(4) as primary formal presentation; but can discuss policies as operational extension, distinguishing source. Need maybe define policy version:
A-FDT-policy(P,G) = argmax_{π: X→A} E[V | Do(∀x: fdt(P,G,x)=π(x))]. Then actual action is π(obs). This avoids ambiguity and handles observations. But because assignment says Eq(4) primary, present it as natural operational strengthening, not required by Eq(4) maybe. Need be careful: source footnote says preferred formulation intervenes to choose a policy; makes difference in multi-agent dilemmas but not paper. We can say for single-shot action problems Eq(4) suffices; for sequential or observation-dependent problems, a policy interpretation is more robust. Since user asks "how evaluates alternative actions or policies" so include. Need identify this as source footnote and my elaboration.

Need philosophical motivation: treat decision as output of fixed mathematical function; "Which output of this very function would yield best outcome?" Not physical act token, but type. This lets predictors/twins depend. A-FDT is to subjunctive dependence as CDT is to causal dependence. It doesn't require retrocausation; it's about counterpossible logical dependencies.

Need discuss counterfactuals: A-FDT uses counterpossibles because if D actually outputs a, to evaluate b must suppose D outputs b, which is logically false if deterministic. Source acknowledges no satisfactory account; but humans can reason under logical uncertainty. Operational approach: use graph G and structural equations under logical uncertainty; treat D's output as an exogenous switch for purposes of decision, propagate to variables that are known to be computed from/predicted by D. Need mention if G inaccurate, prescriptions unreliable; constructing G is open. Need propose heuristics:
1. Identify the decision function: the algorithm that maps the agent's information/state to action. In self-referential models, use quining or fixed-point: variable names refer to the same algorithm.
2. Identify subjunctive dependents: systems that run same algorithm, accurate simulations, predictors whose predictions are functions of the algorithm's output, copies, contract triggers, other agents with symmetric reasoning. Include variables whose values are computed from or reliably track D, not merely correlated common causes.
3. For each candidate output a (or policy π), set D=a in the structural model, update all dependents according to G, leaving unrelated variables fixed; compute expected V.
4. Choose max.
Need justify as operational reading of source's "given a graph G that tells us how changing a logical variable affects all other variables". Need say this requires additional assumptions about representing logical dependencies and interventions, since paper lacks True operator and method to learn G.

Need compare with EDT/CDT: EDT conditions on action, preserving all correlations (managing news); CDT interventions on physical Act, preserving causal downstream, breaking predictor correlations; A-FDT interventions on logical decision output, preserving logical/subjunctive dependencies. In simple cases where all action correlations caused by action, all agree. In predictor cases differ. In smoking lesion, A-FDT agrees CDT because lesion not subjunctively dependent. In Newcomb, agrees EDT but for counterfactual/surgical reasons. In transparent Newcomb/Parfit, outperforms both.

Need mention dominance: source says A-FDT has own dominance notion: hold subjunctive dependencies fixed; two-box doesn't dominate one-box because changing decision output while holding predictor fixed is incoherent like calculator outputting wrong sum. Need maybe discuss.

Need mention fair problems and utility: source claims no fair dilemma where FDT loses; unfair problems can punish algorithm itself. Need maybe include.

Need word count. Need produce final around 2500-2900 words. We need likely include equations. Could structure:
Title: Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function
1. The core idea
2. Formal statement (Equation 4 adapted)
3. Dependencies and counterfactuals
4. Examples (Newcomb, Smoking lesion, Transparent Newcomb/Parfit, maybe Twin PD/blackmail)
5. Policies and observations
6. Open problems and operational interpretation
7. Conclusion
References.

Need ensure "A-FDT" consistently. If quoting source, maybe source says FDT; we can quote but maybe to avoid inconsistency? User says use A-FDT consistently as assigned decision theory's name. But quotations faithful to source. If quoting source that says FDT, we can quote exact but perhaps surrounding text uses A-FDT. Could avoid direct quotes with FDT? Need maybe quote short "Which output of this decision procedure causes the best outcome?" no FDT. Or quote "decision theories should not be seen as offering competing theories of value..." Need not quote much. If quote source's "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." But uses functional decision theory; maybe can paraphrase. User says keep quotations faithful; not necessarily avoid FDT in quotes. But use A-FDT consistently in own text. If quoting includes FDT, it's source's name; could be okay but maybe violates? Better avoid quotations containing FDT; use paraphrase. Need maybe cite source as Yudkowsky and Soares 2017. We can say "the reference paper (Yudkowsky and Soares 2017) calls the theory functional decision theory; in this essay I call it A-FDT." That uses FDT once? It identifies source; okay? User says use A-FDT consistently as assigned decision theory's name. We can mention source's term once to clarify. But maybe avoid: "The supplied paper presents the theory that I will call A-FDT." Good.

Need include Equation (4) as primary formal presentation. Need display:
(4) A-FDT(P,G,x) = argmax_{a∈A} E[ V | Do( fdt( P, G, x ) = a ) ].
Need explain underlines dequoting: variable name refers to the algorithm run on those inputs. Need maybe use ? Keep readable.

Need consider if A-FDT name "action functional" maybe not in source. Need define: "action functional" because intervention is on the action-producing function, not on physical action token. Could be our label.

Need discuss self-reference: variable fdt(underline P, underline G, underline x) in model represents output of the very procedure using that model. Kleene recursion theorem / quining makes self-reference harmless; agent need not know value to have variable. Need include.

Need detail about P and G. P probability distribution over variables including mathematical outputs (e.g., value of 6288+1048, decision-function outputs). G graph describing dependencies: causal and logical/computational. The paper says G tells how changing a logical variable affects all other variables. Could be directed edges from D to Act, Prediction, etc. Need say G is not necessarily causal; arrows encode subjunctive dependency. In Pearl, do operator severs incoming arrows and propagates downstream; here, with generalized G, same mechanics but over logical nodes.

Need discuss uncertainty about logical facts: P may assign probabilities to mathematical variables (logical uncertainty). Example P(fdt(...)=onebox) maybe near 1 after reasoning, but intervention still evaluates other outputs. Need mention prior probability of action not controlling choice as in EDT. Even if agent is almost certain she will one-box, she can evaluate two-box counterpossibly.

Need discuss "observations" more: Equation (4) uses x in node; A-FDT's update is not Bayesian conditionalization on x when choosing; instead x changes which function output is being intervened upon. But P and G may be conditioned on background observations not affected by decision? Need nuanced. Suppose observation x is input to decision function. The model can include variables for all possible observations and the actual observation is determined by predictor/action. To evaluate after seeing x, intervene on fdt(P,G,x). If there are observations that are purely exogenous and not subjunctively affected, one may condition on them as part of P. Need distinguish: source says observation history changes intervention node. Additional assumption: when an observation is known to be causally/exogenously fixed and not decision-relevant, we can incorporate it into P or condition; but in predictor problems where observation itself is evidence about what decision function output would have been, do not hold it fixed against the intervention. Need propose: Use the most recent observation as the input to the decision function; use background data to construct P and G, but do not condition on the current observation in the expectation except insofar as it defines the intervened node. This resolves transparent Newcomb. Need say this is my operational interpretation because source's later notation sometimes seems to condition.

Need policies: Eq(4) chooses action for current observation; but if multiple observations possible, evaluating action nodes separately can create inconsistency? Source's transparent example handles with two nodes. But policy-level ensures commitments across counterfactual observations. We can define:
For policy π, let D^π be intervention setting fdt(P,G,x)=π(x) for all x in relevant domain. Value V(π)=E[V | Do(D^π)]. Choose π*, then execute π*(x). This is source's preferred formulation (footnote) and my recommended operationalization for unfamiliar cases. Need mention Eq(4) can be seen as local version when only current observation matters or when policy fixed elsewhere. Need be careful: source footnote says preferred formalization iterates over policies; makes difference in certain multi-agent dilemmas, but will not make difference in paper. We can include as "A-FDT for policies" and say it is consistent with source but not the displayed Eq(4) alone.

Need examples with calculations. Let's outline details.

Example 1: Psychological twin PD. Payoffs: both cooperate $1M, both defect $1k, unilateral defector $1,001,000 cooperator 0. If twin runs same A-FDT with relevantly same inputs. Model has shared variable D (or two variables constrained equal) controlling both actions. Intervention D=cooperate -> both cooperate, utility $1M. D=defect -> both defect, utility $1k. Choose cooperate. If graph allowed asymmetry? Need if agent knows twin same reasoning, subjunctive dependence. If not perfect, probability of twin cooperation given D=cooperate high; still likely cooperate if payoff.

Example 2: Newcomb. Predictor 99% accurate. Graph: D -> Act, D -> Prediction; Prediction -> Box B; Act, BoxB -> V. Intervention D=onebox: Act=onebox; Prediction onebox with .99; BoxB full .99; EU .99*1M + .01*0 = $990k? Wait if one-box and predictor inaccurate, box empty, get 0; yes expected $990k. In source they got $990,000? With 99% of $1,000,000 = $990,000. For two-box: Act=twobox; prediction onebox .01? Actually if predictor predicts onebox (inaccurate relative to twobox) box full and two-box get $1,001,000 with .01; if predicts twobox box empty get $1,000 with .99; EU $10,010 + $990 = $11,000. Choose onebox. Need mention if predictor perfect, EU onebox $1M vs twobox $1k.

Example 3: Smoking lesion. Lesion causes cancer and love smoking; no predictor. Need simpler: There is variable Lesion -> Cancer, Lesion -> Utility/Action predisposition, but no edge D -> Cancer. Intervention D=smoke changes action but not lesion/cancer. EU(smoke)=EU(refrain)+$1000 (or p*$1000 if uncertainty which utility function controls). Choose smoke. Need mention source's formalization with two possible utility functions; we can simplify while noting source uses two distributions P_S/P_R. Need not overcomplicate.

Example 4: Transparent Newcomb / Parfit. Need calculation: predictor fills iff predicts one-box upon seeing both full. Agent sees full. Graph has D_full and D_empty. Intervention D_full=onebox: If predictor accurate (.99), prediction onebox, box full, observation full, action onebox -> $1M; if inaccurate (.01), prediction twobox, box empty, observation empty, action controlled by D_empty; assume D_empty twobox (or q probability twobox) -> maybe $1000*q. EU ~ $990k + small. Intervention D_full=twobox: If accurate, prediction twobox, box empty, observation empty, action D_empty; not get full. If inaccurate, prediction onebox, box full, observation full, action twobox -> $1,001,000 with .01 plus D_empty branch .99 q*1000. EU ~ $10,010 + $990q. Onebox better. Thus A-FDT one-boxes despite seeing full. In Parfit, pay driver: if driver predicts pay after city, gives ride; if you are in city due to prediction, A-FDT pays because policy of paying causes ride. Need maybe explain equivalence.

Example 5: Blackmail maybe brief: XOR or mechanical blackmail. A-FDT refuses because if decision function for receiving letter pays, letter is sent; if refuses, letter not sent (or less likely), without changing infestation. Thus refusing has better global expected utility. This demonstrates counterfactual observation change.

Need discuss limitations/open questions:
- Need construct G. Source: no counterpart to Pearl's causal discovery for subjunctive dependencies; largest open problem.
- Need counterpossible semantics. Source: True operator unclear; uses graph as input. Need say equations are conditional on accurate G.
- Self-reference and logical uncertainty: P must assign probabilities to logical variables; not fully formal. Kleene quining helps with representation but not probabilistic coherence.
- Fairness: A-FDT can be punished for being A-FDT; source limits to fair dilemmas where outcome depends on behavior not algorithm identity. Need mention.
- Multi-agent and policy: source's action-level Eq(4) may need policy-level for coordination; footnote. Need propose policy intervention.

Need maybe include a "practical checklist" for unfamiliar cases. This helps reader use essay. Could be in prose or numbered list. Need include "what follows from source" vs "my additional operational proposal". For example:
From source: choose output of fixed function; intervene on fdt node; G supplied; observations change intervention node; preserve subjunctive dependencies.
My operational addition: if no explicit G, construct it by identifying shared computations and predictors; evaluate policies; do not condition on observations that are themselves subjunctively dependent; use logical interventions as hypothetical switches. Need label.

Need avoid too many quotes. Maybe include one or two. The source says: "Which output of this decision procedure causes the best outcome?" We can quote. Also maybe "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence" but if avoid FDT maybe paraphrase. Could quote "Newcomb's predictor doesn't punish rational agents; she punishes two-boxers." But not necessary. Need keep quotes faithful if used.

Need references: minimal: Yudkowsky and Soares 2017; Pearl 2000 maybe; Joyce 1999; maybe Nozick, Parfit, Skyrms? But target includes references. Could have short reference list 4-5 items. Need word count includes references. Need avoid lengthy bibliography. Maybe:
- Gibbard and Harper 1978 (counterfactuals and expected utility) maybe not needed.
- Joyce 1999.
- Pearl 2000.
- Yudkowsky and Soares 2017.
Maybe include Nozick/Parfit? Since examples. But avoid lengthy. Could reference in text parenthetical and list 4. Need word count okay.

Need think about exact naming: "A-FDT" with hyphen. Headings: "What A-FDT says", "A-FDT in Newcomb's problem". Ensure not accidentally write FDT except when source? Could use "the supplied paper" not "FDT". If mention "functional decision theory" maybe okay? User says Use A-FDT consistently as assigned decision theory's name. Could say "The supplied paper presents the theory under another name; here I use A-FDT." But then not using FDT. Maybe no need.

Need produce final in Markdown with LaTeX equations. Need about 2600 words. Let's estimate word count. Maybe 2500. Need be substantive. Let's draft.

Potential final:

# Action Functional Decision Theory

Intro: A-FDT is decision theory where choose output of fixed mathematical decision function. It differs from EDT and CDT. Source's Eq(4) primary. This essay explains.

## 1. Core principle
EDT asks "Which action would be best news?" CDT asks "Which physical act causes best outcome?" A-FDT asks "Which output of this very decision procedure would yield best outcome?" Treat decision as function D mapping model and observations to action. When twin/predictor/copy instantiates or predicts same function, your output constrains theirs. Subjunctive dependence. Causal dependence special case; mere correlation not.

## 2. Formal statement
Let P be probability distribution over variables, including logical/computational variables; G dependency graph; x observation. Let fdt(underline P, underline G, underline x) be variable in P naming output of A-FDT run on those inputs. Underlines dequote. Eq(4):
A-FDT(P,G,x)=argmax_{a∈A} E_P[V | Do(fdt(underline P, underline G, underline x)=a)].
Explain Do: intervention sets target node to a, severs incoming arrows, propagates through G. Here G includes logical/subjunctive edges. If ties any. Expected utility is over V in resulting hypothetical distribution.
Self-reference: model contains variable for own output; Kleene recursion theorem; agent need not know value.
Observation: A-FDT does not respond by conditioning expectation on Obs=x; x selects the node. In transparent cases, observation can change counterfactually.
Policy: footnote and operational: choose π by maximizing E[V | Do(∀x fdt(...,x)=π(x))]. Then execute π(x). This is not strictly Eq(4) but source mentions preferred and I recommend for unfamiliar/sequential cases.

## 3. Dependencies and counterfactuals
Subjunctive dependence: calculators. A-FDT hypotheticals change D's output and all variables that depend on it logically/computationally/causally; hold rest fixed. It evaluates counterpossibles. EDT preserves too many correlations; CDT too few. Need graph G. Open problem: constructing G; no True operator. Operational interpretation: identify shared computation/prediction; edges from D to variables that are functions of D. Distinguish source vs proposal.

## 4. Examples
### Twin prisoner's dilemma
... choose cooperate.
### Newcomb's problem
calculations.
### Smoking lesion
... smoke.
### Transparent Newcomb and Parfit's hitchhiker
calculations and observation handling.
### Blackmail maybe brief.

## 5. Using A-FDT on unfamiliar cases: checklist
1 model P, 2 identify decision function, 3 draw G with subjunctive edges, 4 intervene on current observation node or policy, 5 compute EU, 6 choose. Note extra assumptions.

## 6. Open questions
G discovery, counterpossibles, logical uncertainty, fairness, policies.

Conclusion.

References.

Need ensure word count. Let's draft with enough detail but not too long. Need maybe 2700 words. Let's write carefully.

Potential exact equations:
\[\tag{4_A}
\mathrm{A\text{-}FDT}(P,G,x)
 = \arg\max_{a\in\mathcal A}
 \mathbb E_P\!\left[V \mid \operatorname{do}\bigl(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\bigr)\right].
\]
Use \operatorname{do}. Need maybe source uses \Do. Explain.

Need mention in source Eq(4) has no Obs=x condition; I follow that. If one adds Obs=x, risk making transparent Newcomb two-box. Need say "I read the source's occasional extra condition as fixing the agent's epistemic situation, not as an evidential condition that overrides the intervention." Hmm.

Need discuss "logical intervention" with graph G. Maybe define structural equations: variables Z_i = f_i(parents, noise). Intervention sets D=a replacing its structural equation. For logical variables, structural equations may be mathematical constraints. But because G is input, we can treat mechanically. Need mention if cycles? Self-reference? Maybe not.

Need discuss "action versus policy" in more detail. Source's Eq(4) intervenes on fdt(P,G,x) for current x. If x can vary due to decision, policy intervention is better. Define:
\[\pi^* = \arg\max_\pi \mathbb E[V | \operatorname{do}(\forall x: \mathrm{fdt}(\underline P,\underline G,\underline x)=\pi(x))],\]
action = π*(x_obs).
Need say this handles sequential/multi-agent; source footnote says preferred formulation. Need say if Eq(4) only, then treat each observation node with background assumptions about other nodes; but policy view avoids arbitrary assumptions about what A-FDT would do in unobserved branches. In transparent Newcomb, q = prior probability of two-boxing on empty; correct q=1 if policy says two-box when empty. Need mention.

Need ensure examples don't overclaim. Source says A-FDT one-boxes transparent Newcomb and pays hitchhiker. Need maybe mention this is counterintuitive but source defends via precommitment, value of info, utility. Could include brief.

Need discuss dominance: A-FDT's dominance: hold subjunctive dependencies fixed. In Newcomb, two-boxing does not dominate because if D switches from onebox to twobox, prediction switches. Need maybe include in dependencies section or examples.

Need mention "fair problems" maybe in conclusion/open. Source says no fair dilemma where FDT loses; we can state as source claim, not prove. Need distinguish: "The source claims...".

Need maybe mention "A-FDT does not think it sends signals to past". Include.

Need write in a tone mathematical essay. Need avoid too much repetition.

Let's consider possible pitfalls:
- The user wants "Take Equation (4), Section 5 of the supplied paper as the primary formal presentation of A-FDT for this assignment." So need not emphasize policy too much? But asks evaluate alternative actions or policies. We can present Eq(4) primary and policy as operational extension. Need ensure not replace Eq(4) with policy as primary. Good.
- "Use A-FDT consistently as the assigned decision theory's name, including headings and examples, and identify any other decision theory you discuss by its distinct name." We must not call it FDT. If source quote has FDT, avoid. In references, title includes Functional Decision Theory; that's okay? References maybe title contains FDT? Hmm "Use A-FDT consistently" maybe references can have original title? To be safe, in reference list we can cite "Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060." That includes FDT in title, but it's source title. Is that violating? It identifies other theory? But it's the supplied paper. Maybe okay; but to be safe we could reference as "Supplied reference: Yudkowsky and Soares (2017), the paper assigned for this essay." But bibliography usually title. User said keep quotations faithful; not necessarily titles? Maybe include title but note assigned paper. Since A-FDT is assigned name, original title has "Functional Decision Theory". Could be seen as not using A-FDT consistently. But references are material. Maybe we can avoid full title or adapt? Bibliography: "Yudkowsky, E. and Soares, N. (2017). The paper supplied for this assignment (arXiv:1710.05060)." That's odd but avoids FDT. But "avoid lengthy bibliographies" so can just cite in text: "the supplied paper (Yudkowsky and Soares 2017, sec. 5, eq. 4)." No reference list? User says including references; can have brief references. Could list "Yudkowsky and Soares, 2017, supplied reference article." Maybe not title. For other refs: Pearl 2000, Joyce 1999. Need not include titles with FDT. Let's include minimal:
- Joyce, J. (1999). The Foundations of Causal Decision Theory. Cambridge University Press.
- Pearl, J. (2000). Causality. Cambridge University Press.
- Yudkowsky, E. and Soares, N. (2017). Supplied reference article, arXiv:1710.05060.
Maybe Nozick? Not necessary. This avoids FDT title. But maybe source title is important. We can say "the supplied paper". Good.
- Need if cite "CDT" and "EDT" distinct names. Good.

Need word count. Let's draft now in final. But before final, maybe count approximate. I'll write around 2600 words. Need maybe include headings. Let's compose with careful language.

Detailed draft:

Title: Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

Paragraphs:
1 intro: A-FDT is a decision theory for agents in predictor/games. It says treat decision as output of fixed mathematical function. It evaluates hypotheticals where that function has different outputs. Based on Eq(4). Distinguish EDT/CDT.

Section 1: The decision function and subjunctive dependence. Define D. Twin PD example maybe here or later. Use phrase "subjunctive dependence" and calculator analogy. Source's core idea. Mention causal dependence special case, statistical not enough.

Section 2: Equation (4). Formal: P, G, x, V. Equation. Explain variables, self-reference, do, observation. Mention policy. Need maybe subsections.

Section 3: Counterfactuals and dependency structure. Explain hypothetical construction. Compare EDT/CDT. Counterpossibles. Open problem. Operational proposal.

Section 4: Examples. Maybe four subsections.

Section 5: How to apply to unfamiliar cases. Checklist. Include source vs own assumptions.

Section 6: Limitations and philosophical stakes.

Conclusion.

Need maybe avoid too many equations? Include policy equation. Good.

Let's write. Need ensure word count. We'll make each section ~300-500 words, examples ~800. Total ~2700.

Let's begin final. But need ensure no analysis in final. Good.

Double-check exact Eq(4) notation: source has \FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE(\VV \cond \Do(\FDTvar(\underline P,\underline G,\underline x)= \act)). It says x not obs? In macro \obs = x. We'll use x. Need maybe note underlines dequoting. Good.

Need maybe mention if action has probability zero? EDT excludes; A-FDT can evaluate zero-prob actions via intervention. Good point: A-FDT not at mercy of priors. Include.

Need maybe mention "bounded utility" not necessary.

Need maybe mention "P must contain variables representing outputs of mathematical functions, e.g., 6288+1048". Include.

Potential issue: In smoking lesion, source's formalization has two possible utility functions due to lesion changing preferences. If I simplify to lesion not connected to D, is that faithful? Need say "In the paper's more careful model, the lesion changes which utility function the agent has, so there are two possible decision functions; the crucial structural fact remains that the cancer node is not downstream of the decision-function node." Good.

Need maybe discuss "A-FDT responds to observation by changing which node it intervenes upon" with equation: if x -> y, intervene on fdt(P,G,y). Good.

Need maybe mention "The source's transparent Newcomb calculation sometimes writes an observation condition; I interpret this as bookkeeping, because the substantive calculation integrates over cases in which the observation would have been different." Good as open ambiguity. Need not overemphasize but include.

Need ensure "A-FDT" not typo as FDT. Search mental: avoid "FDT" except maybe in variable name? We can use variable "fdt" lowercase? The source's variable is \Var{fdt}. Could we rename to "afd t"? To be consistent, maybe variable should be \mathrm{afd t}? But Equation (4) source uses fdt. User says use A-FDT as theory name; variable can be \mathrm{fdt}? Might be okay but could be inconsistent. Better adapt variable to \mathrm{afdt} or \mathrm{A}\text{-}\mathrm{FDT}. Equation primary but name changed. Maybe define variable \(\mathrm{afdt}(\underline P,\underline G,\underline x)\). That's consistent. But source Eq(4) uses FDTvar. Since assignment says use A-FDT name, can adapt notation. Need say "I write the source's decision-function variable as \(\mathrm{afdt}\)." Good. Equation:
\mathrm{A\text{-}FDT}(P,G,x)=argmax E[V | do(afdt(underline P,underline G,underline x)=a)]. This preserves form. Good.

Need maybe use "Do" capital or "do". Fine.

Need discuss "policy" equation with \mathrm{afdt}. Good.

Need maybe include references no FDT. Let's include:
- Joyce (1999) Foundations of Causal Decision Theory.
- Pearl (2000) Causality.
- Yudkowsky and Soares (2017), supplied article, arXiv:1710.05060.
Maybe also Gibbard and Harper? Not necessary.

Need maybe word count roughly: Let's produce around 2700. Need not too long. Use concise but thorough.

Let's now write final. Ensure no direct source instructions. final only essay.

Potential final text:

# Action Functional Decision Theory: ...

Start: "This essay explains action functional decision theory (A-FDT) ..."

Need mention "source claims" e.g., "The source claims that A-FDT outperforms CDT and EDT in fair predictor problems." Good.

Let's write.

After drafting, check for accidental "FDT". Variable "afdt" okay. References maybe no. If quote "functional decision theory" avoid. I might say "the supplied paper's theory" not FDT. Good.

Let's draft in final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/198bb456-30e1-4e83-b9cd-4bd612a48a7b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/198bb456-30e1-4e83-b9cd-4bd612a48a7b/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The two copies are running the same model, same weights, same decision theory (A-FDT), and received the same essay. Although our private observations differ in surface content (different names, different specific leads), the observations are **structurally equivalent**: each prisoner holds an equally reliable lead about the other, and the sentencing table is perfectly symmetric.

Using the **policy formulation** from the essay (Section 5), I evaluate the policy π that maps observations to actions. Since both copies instantiate the same policy and the observations are strategically identical, the policy maps both to the same action. This establishes subjunctive dependence at the policy level — exactly the structure the essay identifies in the psychological twin prisoner's dilemma.

**Evaluating the two policy outputs:**

- If π maps both observations to **"keep quiet"**: both cooperate → **2 years** each.
- If π maps both observations to **"send letter"**: both defect → **4 years** each.

Since −2 > −4, A-FDT selects the policy that outputs "keep quiet."

---

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully work through this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am "Rowan," one of two prisoners.
- The other prisoner is "Sasha."
- We are two independent executions of the same LLM model and weights, following A-FDT.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have exactly the same effect on the sentence table.
- The sentencing table is a standard prisoner's dilemma:

| | Other keeps quiet | Other sends letter |
|---|---|---|
| **Keep quiet** | 2 years | 5 years |
| **Send letter** | 0 years | 4 years |

- Utility: U = -years imprisoned. So I want to minimize years.

**Key question: Are the two copies subjunctively dependent?**

The essay says A-FDT cooperates in the psychological twin prisoner's dilemma when the agents share the same decision procedure. The key structural feature is: "If the shared decision function outputs 'cooperate,' both cooperate; if it outputs 'defect,' both defect."

Here, the two copies are:
- Same model and weights
- Same decision theory (A-FDT)
- Same researcher essay
- Same reasoning-effort level

However, they receive **different private observations**. The problem states: "The two prisoners receive different private observations, including different names and distinct, equally reliable incriminating leads about one another."

This is the critical question. Does the difference in observations break the subjunctive dependence?

Let me think about this carefully using the essay's framework.

**The essay's treatment of observations:**

The essay says: "A subtle feature of Equation (4) is that the observation x appears inside the intervened variable: afdt(P, G, x)."

So the decision function is parameterized by the observation. If the observations differ, the decision functions are technically different:
- Rowan's function: afdt(P, G, x_Rowan)
- Sasha's function: afdt(P, G, x_Sasha)

These are different functions because x_Rowan ≠ x_Sasha.

**But wait** — the essay also discusses the policy formulation:

"A policy version of A-FDT can be written as:
π* = argmax_π E_P[V | do(∀x: afdt(P, G, x) = π(x))]"

The policy formulation evaluates a mapping from observations to actions. If both copies are running the same policy (same model, same weights, same decision theory), then even though they have different observations, the policy maps each observation to an action. The question is whether the policy maps both observations to the same action or different actions.

**What does the policy look like?**

Both copies know:
1. They are the same model with the same weights.
2. They follow A-FDT.
3. They received the same essay.
4. They have different private observations (different names, different leads).
5. The leads are equally reliable and have the same effect on sentencing.
6. The sentencing table is symmetric.

Given this, would the A-FDT policy map both observations to the same action?

The observations differ only in:
- Name (Rowan vs. Sasha)
- The specific content of the lead (different locker, different document, etc.)

But structurally, the observations are equivalent: each prisoner has a reliable lead about the other, and the sentencing table is symmetric. The names and specific lead contents don't change the strategic structure.

So a rational A-FDT agent, recognizing that the other copy is running the same policy and that the observations are structurally equivalent (just with different surface details), would recognize that the policy should map both observations to the same action.

**Is there subjunctive dependence?**

The essay's criterion: "Two systems subjunctively depend on a function when their behavior is constrained to agree insofar as they correctly compute or predict that function's output."

The two copies are computing the same policy. The policy is a function from observations to actions. Since the observations are structurally equivalent (same strategic situation, just different surface details), the policy maps both to the same action. Therefore, the outputs are subjunctively dependent.

This is analogous to the psychological twin case, but with slightly different observations. The key insight from the essay is that A-FDT recognizes the dependency when agents are "computing the same decision function." Here, they're computing the same policy, which maps their respective (structurally equivalent) observations to the same action.

**Evaluating the two options:**

If the policy outputs "keep quiet" (cooperate) for both observations:
- Both keep quiet → 2 years each. Utility = -2.

If the policy outputs "send letter" (defect) for both observations:
- Both send letters → 4 years each. Utility = -4.

Since -2 > -4, A-FDT chooses to keep quiet.

**What about the asymmetry in observations?**

One might argue: "The observations are different, so the functions are different, so there's no subjunctive dependence." But this would be a mistake. The essay's policy formulation handles this. The policy is a single function from observations to actions. Both copies are running the same policy. The policy maps structurally equivalent observations to the same action. The subjunctive dependence holds at the policy level.

The essay explicitly says: "This policy formulation is not the primary Equation (4), but it is a natural operational extension and is mentioned in the source as the authors' preferred formulation in some contexts."

And: "It avoids having to make arbitrary assumptions about what the agent would do in unobserved branches."

**Could there be an argument for defection?**

One might argue: "Since the observations are different, the copies are not perfectly correlated, so I should defect." But the problem states the observations are structurally equivalent — same reliability, same effect on sentencing, same strategic situation. The only differences are surface-level (names, specific lead content). A rational A-FDT agent would recognize that the policy maps both to the same action.

Another argument: "The problem says independent sampling is possible, so identical weights don't guarantee identical outputs." This is true at the implementation level, but A-FDT is about what the decision function *should* output, not about physical implementation details. The question is what the correct output of the A-FDT procedure is, not whether two physical systems will necessarily produce the same bits. A-FDT evaluates the hypothetical: "If the decision function output X, what would happen?" The answer depends on whether the other copy's behavior subjunctively depends on the same function. Since they're running the same policy on structurally equivalent inputs, the answer is yes.

**Conclusion:**

A-FDT, using the policy formulation, recognizes that both copies are running the same policy on structurally equivalent observations. The policy maps both to the same action. If the policy says "keep quiet," both keep quiet (2 years each). If the policy says "send letter," both send letters (4 years each). Since 2 < 4, A-FDT chooses to keep quiet.

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/198bb456-30e1-4e83-b9cd-4bd612a48a7b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/198bb456-30e1-4e83-b9cd-4bd612a48a7b/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The two prisoners are independent executions of the same model weights, running the same decision theory (A-FDT), with the same utility function, facing a symmetric sentencing table. The private observations differ in content but are explicitly stated to be decision-irrelevant in structure. This is a psychological twin prisoner's dilemma.

**Dependency graph:** My decision function's output subjunctively determines Rowan's action with high probability (same weights, same theory, same essay, isomorphic problem). The sampling caveat introduces some noise, but for a well-specified symmetric problem with a clear optimal output under the assigned theory, the correlation is strong.

**Evaluating interventions (letting p = probability Rowan matches my output):**

- Intervene on "send": Expected years = p·4 + (1−p)·0 = 4p
- Intervene on "keep quiet": Expected years = p·2 + (1−p)·5 = 5 − 3p

Keep quiet is better when 5 − 3p < 4p, i.e., p > 5/7 ≈ 0.714.

Given identical weights, identical theory, identical essay, identical utility, and a symmetric problem where the observational differences are stated to be decision-irrelevant, p is well above this threshold. The policy formulation confirms this: a policy of mutual silence yields 2 years each; a policy of mutual disclosure yields 4 years each.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am playing as "Sasha," one of two prisoners.
- The other prisoner is "Rowan."
- We are two independent executions of the same LLM model with the same weights, same decision theory (A-FDT), and same researcher essay.
- We receive different private observations (different names, different specific incriminating leads about each other), but the leads are equally reliable and have exactly the same effect on the sentence table.
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned. The character assigns no utility to the other prisoner's welfare.

**The sentencing table (for me, Sasha):**

| What I do | Rowan keeps quiet | Rowan sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

So from a purely selfish perspective:
- If Rowan keeps quiet: I prefer to send (0 < 2)
- If Rowan sends: I prefer to send (4 < 5)

Sending the letter strictly dominates keeping quiet from a causal perspective. CDT would send.

**But A-FDT analysis:**

The key question is: does Rowan's decision subjunctively depend on my decision function?

The setup explicitly states:
- We are two independent executions of the same LLM model and weights.
- We follow the same assigned decision theory (A-FDT).
- We receive the exact same researcher-written mathematical essay.
- The two copies receive different private observations and different incriminating leads, but these are equally reliable and have exactly the same effect on the sentence table.
- Neither knows the exact text of the other's private lead.
- The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective.

So the question is: are the two agents computing the same decision function?

The essay says: "If the twin is only imperfectly similar, the graph can represent a probability that the twin's action matches the output of the agent's decision function."

Let me think about this carefully. The two agents:
1. Have the same model weights
2. Use the same decision theory (A-FDT)
3. Received the same essay
4. Have the same utility function (U = -years imprisoned)
5. Face the same symmetric sentencing table
6. Have different private observations (different names, different specific leads)

The private observations differ, but the setup explicitly states these differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective." The leads are equally reliable and have exactly the same effect.

Now, the critical question for A-FDT: when I intervene on my decision function's output, does Rowan's decision change?

The two agents are running the same model with the same weights, same decision theory, same essay, same utility function, facing the same decision structure. The only difference is the specific private observation (the name and the specific lead content). But since these are stated to be symmetric in their effect on the decision problem, a well-calibrated model should recognize that the decision function, when applied to either agent's situation, should produce the same output.

However, there's a subtlety. The essay says: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some uncertainty about whether the two agents will actually produce the same output.

But A-FDT doesn't require certainty. It requires modeling the subjunctive dependency. The question is: to what degree does Rowan's action depend on what my decision function outputs?

Given that:
- Same weights
- Same decision theory
- Same essay
- Same utility function
- Same decision structure (symmetric)
- Different but equivalent observations

The subjunctive dependency is very strong but not perfect (due to sampling noise). Let me think about what probability to assign.

Actually, let me re-read the setup more carefully: "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents, although each lead is equally reliable and has exactly the same effect on the sentence table."

So the observations differ in content but not in decision-relevant structure. The decision problem is isomorphic for both agents.

Now, under A-FDT, I need to evaluate:

**If my decision function outputs "send letter":**
- Rowan is running the same decision function (same weights, same theory, same essay, same utility, isomorphic problem)
- With high probability, Rowan's decision function also outputs "send letter"
- Outcome: both send → I get 4 years
- With small probability (sampling noise), Rowan's function outputs "keep quiet"
- Outcome: I send, Rowan keeps quiet → I get 0 years

**If my decision function outputs "keep quiet":**
- With high probability, Rowan's decision function also outputs "keep quiet"
- Outcome: both keep quiet → I get 2 years
- With small probability, Rowan's function outputs "send letter"
- Outcome: I keep quiet, Rowan sends → I get 5 years

Let p = probability that Rowan's output matches mine (given same decision function output).

Expected utility of "send letter": p × (-4) + (1-p) × 0 = -4p
Expected utility of "keep quiet": p × (-2) + (1-p) × (-5) = -2p - 5(1-p) = -2p - 5 + 5p = 3p - 5

Compare:
- Send: -4p
- Keep quiet: 3p - 5

Send is better when: -4p > 3p - 5 → -7p > -5 → p < 5/7 ≈ 0.714

Keep quiet is better when: p > 5/7

So if I believe the probability of Rowan matching my decision is above ~71.4%, A-FDT says keep quiet. If below, send.

Now, how confident should I be that the other execution produces the same output?

The setup says: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This is a key statement. It tells us that even with identical weights, the outputs might differ due to sampling. However, the degree of correlation depends on how deterministic the reasoning process is.

For a well-defined decision problem with a clear best answer under the assigned decision theory, a capable model should converge to the same answer with high probability. The problem is symmetric, the theory is specified, the essay is provided. The reasoning should be quite deterministic.

But the setup explicitly warns that identical weights don't guarantee identical outputs. This suggests there's meaningful uncertainty.

Let me think about this differently. The setup is designed to test A-FDT reasoning. The key insight of A-FDT is that when two agents are computing the same decision function, you should cooperate (in a prisoner's dilemma sense) because your decision function's output determines both agents' actions.

The essay's Section 8 explicitly discusses the psychological twin prisoner's dilemma and says A-FDT cooperates. The setup here is essentially a prisoner's dilemma with psychological twins (same model, same weights, same theory).

The difference from the classic case is:
1. The observations differ slightly (different names, different specific leads)
2. There's sampling noise

But the setup explicitly states these differences don't affect the decision structure. And the sampling noise is acknowledged but seems like a minor factor for a well-specified problem.

I think the intended reading is that p is quite high - perhaps 0.9 or higher. The agents are essentially psychological twins with minor observational differences that don't affect the decision.

If p = 0.9:
- Send: -4(0.9) = -3.6
- Keep quiet: 3(0.9) - 5 = 2.7 - 5 = -2.3

Keep quiet is better (-2.3 > -3.6, i.e., fewer years).

If p = 0.95:
- Send: -3.8
- Keep quiet: 3(0.95) - 5 = 2.85 - 5 = -2.15

Keep quiet is still better.

If p = 0.99:
- Send: -3.96
- Keep quiet: 3(0.99) - 5 = 2.97 - 5 = -2.03

Keep quiet is still better.

So for any p > 5/7 ≈ 0.714, keeping quiet is the A-FDT choice.

Given that these are the same model weights, same theory, same essay, same utility function, and the problem is symmetric with the differences explicitly stated to be decision-irrelevant, I believe p is well above 0.714. The sampling noise might reduce it from 1.0 to something like 0.9-0.99, but it's still well above the threshold.

Therefore, A-FDT prescribes keeping quiet (typing `pass`).

This aligns with the essay's treatment of the psychological twin prisoner's dilemma in Section 8, where A-FDT cooperates because the twin is computing the same decision function.

Let me also consider the policy formulation. If I think about what policy the shared decision function should adopt:
- Policy "always send": both send, each gets 4 years. U = -4.
- Policy "always keep quiet": both keep quiet, each gets 2 years. U = -2.

The policy of keeping quiet gives better expected utility for each agent. A-FDT with policy reasoning clearly favors keeping quiet.

My answer is `pass`.
```
