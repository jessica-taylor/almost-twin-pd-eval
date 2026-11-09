# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00012

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d0be3ddb-d3e8-400e-900d-043bbbee3788/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d0be3ddb-d3e8-400e-900d-043bbbee3788/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: choosing the policy behind the action

A decision can be viewed in two ways. One can ask which physical act will have the best consequences, given the state of the world. Or one can ask which *rule for acting* would have the best consequences, taking into account how other agents and predictors respond to that rule.

Policy functional decision theory, **P-FDT**, takes the second question seriously. It evaluates candidate policies by considering what the world would be like if the decision procedure selecting the policy output a different one. Those counterfactuals retain not only ordinary causal effects but also relevant dependencies involving predictions, simulations, and other implementations of the same computation.

This essay takes footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory* as its primary source. The footnote says that the authors’ preferred formulation intervenes on the decision-function node to choose “not an action but a *policy* which maps inputs to actions,” and then applies the agent’s inputs to that policy. The paper mostly develops an action-selection formulation instead, so a complete policy-level algorithm is not supplied. The mathematics below is an operational interpretation of the footnote, informed by the rest of the paper; where it makes choices beyond the source, I identify them as such.

## The object of choice

Let \(X\) be a set of possible inputs or observation histories, and let \(A(x)\) be the actions available at input \(x\). A deterministic policy is a function

\[
\pi:X\longrightarrow A,\qquad \pi(x)\in A(x).
\]

For example, a policy for a transparent-box problem might say:

\[
\pi(\text{full})=\text{take only the opaque-box counterpart},\qquad
\pi(\text{empty})=\text{take both}.
\]

The first entry describes what the agent does on seeing a full large box; the second describes what it does on seeing an empty one. A policy therefore specifies behavior at inputs the agent may never actually receive.

Write \(D(M)\) for a policy-selection computation applied to a model \(M\), and let \(\Pi_D\) be a variable *in that model* representing its output. A stylized P-FDT rule is

\[
\pi^\star\in
\operatorname*{arg\,max}_{\pi\in\mathcal P}
\mathbb E_M\!\left[U\mid
\operatorname{do}(\Pi_D=\pi)\right],
\qquad
a^\star=\pi^\star(x_{\mathrm{actual}}).
\tag{1}
\]

Here \(\mathcal P\) is the candidate policy set, \(U\) is utility, and the intervention is understood in an augmented model of causal **and subjunctive** dependencies. Equation (1) is my proposed policy-level rendering, not an equation stated in the footnote. In particular, the source does not fully specify \(M\), the policy space, or how the expectations are to be computed.

The distinction between \(D(M)\) and \(\Pi_D\) matters. The former is the policy actually produced by the selection procedure. The latter is a model variable manipulated when evaluating alternatives. Setting \(\Pi_D=\pi\) is not a physical operation that rewrites a program or changes the past. It constructs a hypothetical used to decide what the actual computation should output.

This also differs from simply asking, “What if I used some other algorithm?” A predictor may be predicting *this* policy-selection procedure. A useful hypothetical must say how that predictor’s behavior varies with the output of this procedure, rather than merely imagining the agent replaced by an unrelated program.

## Three ways to evaluate alternatives

The contrast with two familiar theories is useful. Let \(O\) be the outcome and \(x\) the present observation. In a simple formulation, **evidential decision theory** (EDT) evaluates an action by

\[
\mathbb E[U(O)\mid X=x,A=a].
\]

It asks what taking \(a\) would be evidence of. **Causal decision theory** (CDT), in a graphical formulation, instead evaluates

\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

It changes the physical action and propagates its causal consequences, while leaving causally upstream variables fixed.

P-FDT’s intervention is different from both. It varies the output of a policy-selection computation, then propagates all dependencies represented as relevant to that output. These include ordinary causal effects of actions but can also include a predictor’s earlier prediction or another system’s implementation of the same computation.

The source calls the broader relationship **subjunctive dependence**. Two exact copies computing the same function on the same input are linked in this sense: if the function’s output were different, both outputs would differ. A sufficiently accurate predictor can be linked less than perfectly: its prediction tends to vary with the predicted computation’s output, although it may make errors. By contrast, correlation alone does not establish such a link.

A graphical model can encode these assumptions, but the graph does not discover them. The paper explicitly identifies the construction of reliable models of logical and computational dependence as a major open problem. An arrow from a policy output to a prediction is a claim about the mechanism, not a license to make every correlated variable follow the chosen policy.

## Newcomb’s problem and the lesion contrast

In Newcomb’s problem, a transparent small box contains \$1,000. A large opaque box contains \$1 million if a predictor predicted that the agent would take only the large box, and nothing otherwise. Suppose the predictor is accurate with probability \(0.99\), under each candidate policy, and utility is linear in money.

Let \(\pi_1\) prescribe one-boxing and \(\pi_2\) prescribe two-boxing. A model in which the predictor tracks the relevant policy gives

\[
V(\pi_1)=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V(\pi_2)=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

P-FDT selects \(\pi_1\). In its two-boxing hypothetical, the predictor probably predicted two-boxing and left the large box empty. There is no assertion that the present act sends a signal into the past. The dependence is between a computation’s output and a prediction of that output.

The conditional accuracy assumption is substantive. The fact that a predictor has been right 99% of the time in some population does not by itself establish the same error rate under each policy intervention. An unfamiliar policy, randomization, or a change in what the predictor observes can change the model.

Now contrast the imaginary smoking-lesion problem. A lesion causes both a desire to smoke and a high risk of cancer, but smoking itself does not cause cancer. Suppose smoking gives the agent an additional 1,000 units of utility and changing the relevant policy does not change the lesion or cancer risk. Then

\[
V(\pi_{\rm smoke})-V(\pi_{\rm refrain})=1{,}000
\]

in the simple case where the policies differ only in whether this agent smokes. P-FDT smokes: the lesion is a common cause, not a predictor whose behavior tracks the policy output. EDT may instead regard smoking as bad news about the lesion, although the paper notes that more sophisticated versions of EDT can avoid this result through additional assumptions or procedures.

The pair illustrates the central modeling discipline: preserve the predictor relationship in Newcomb’s problem, but do not turn a merely statistical lesion–action correlation into policy control over cancer.

## Policies, observations, and counterfactual histories

The most consequential unresolved issue in equation (1) is the distribution used to evaluate policies. The paper’s action-level formulation can allow an observation to change in a counterfactual: when an agent sees a full transparent box and considers an alternative decision-function output, the predictor might instead have left the box empty.

A natural policy-level interpretation is therefore to evaluate policies from a **reference information state** that precedes observations whose occurrence may depend on the policy. The actual observation is still used when applying \(\pi^\star\), and policy-independent background evidence can be incorporated into the model. But an observation generated by a predictor’s response to the policy should not automatically be held fixed across all policy hypotheticals.

This is a proposal, not something fully specified in footnote 16. How to choose the reference state, especially for an agent with a long history and no obvious beginning, remains open. Conditioning on every current observation gives a different theory in cases where the observation is itself affected by the policy intervention. Never conditioning on new information is also too crude: a policy can and should respond to information through its input.

Consider transparent Newcomb with a perfect predictor. It fills the large box exactly when it predicts that the agent’s policy takes only that box **upon seeing it full**. Define

\[
\pi_C=(\text{one-box if full},\ \text{two-box if empty}),
\]
\[
\pi_D=(\text{two-box if full},\ \text{two-box if empty}).
\]

Under the predictor model,

\[
V(\pi_C)=1{,}000{,}000,\qquad
V(\pi_D)=1{,}000.
\]

The first policy produces a full box and leaves the small box behind. The second produces an empty large box and takes the small one. So, on this interpretation, P-FDT applies \(\pi_C\): when actually seeing a full box, it takes only the large box.

That is not a denial that the box is full. It is a refusal to hold its fullness fixed when comparing whole policies in a model where the predictor chose the contents by predicting the policy. A critic may reasonably prefer the CDT comparison, under which taking the extra \$1,000 is better given the already-filled box. The dispute is about which counterfactual comparison should govern action.

Parfit’s hitchhiker has the same structure. A driver rescues an agent only if she predicts that the agent will pay upon reaching town. A policy of paying in town can be more valuable than a policy of refusing, even though, once in town, refusing saves money in the immediate causal comparison. The policy-level model must include the rescue, the prediction, and what happens if the agent never reaches the payment decision.

## Blackmail and the cost of predictor error

Suppose a blackmailer starts a damaging program only when she predicts that the recipient would pay \$1,000 upon receiving a demand. If the demand is ignored, the recipient loses \$1 million. A perfect predictor would not send a demand to someone whose policy is to refuse.

With an imperfect predictor, the answer depends on error rates. For a simple model, suppose a paying policy always receives a demand, while a refusing policy receives one with probability \(\varepsilon\). Taking no demand as zero loss,

\[
V(\pi_{\rm pay})=-1{,}000,\qquad
V(\pi_{\rm refuse})=-\varepsilon(1{,}000{,}000).
\]

Refusal is better when \(\varepsilon<0.001\). At \(\varepsilon=0.0009\), its expected loss is \$900; at \(\varepsilon=0.0011\), it is \$1,100, so paying is better in this stipulated model. The paper gives the first numerical comparison but appears to contain a decimal-place error in its subsequent percentage example; the threshold follows directly from the equation above.

If a refusing agent nevertheless receives the demand, it has learned that the predictor erred in the actual case. Under the reference-state policy comparison just described, it still follows the refusal policy. This is the uncomfortable implication of optimizing the rule across the situations produced by that rule: an exceptional instance can go badly.

The calculation should not be transferred mechanically to real extortion. Actual blackmailers have varied motives and information; paying may affect future threats; refusal may impose costs on other people. Those factors belong in the model. P-FDT supplies a way to compare specified counterfactual policies, not an unconditional instruction never to pay.

## Why choosing a whole policy can matter between agents

Footnote 16 says the policy/action distinction matters in some multi-agent dilemmas but does not give a full example. The following illustrates one possible difference.

Two agents implement the *same* policy-selection computation. One receives input \(L\), the other \(R\). They simultaneously choose \(C\) or \(D\). Each receives 10 if their actions differ and 0 if their actions match. Their shared policy has two entries:

\[
\pi(L),\pi(R)\in\{C,D\}.
\]

Intervening on the common policy output gives four possibilities:

\[
(C,C),\quad(C,D),\quad(D,C),\quad(D,D).
\]

The asymmetric policies \((C,D)\) and \((D,C)\) each give both agents 10; the constant policies give 0. With a common tie-breaker, P-FDT can select one asymmetric policy, after which the agent with input \(L\) and the agent with input \(R\) take different actions.

This does **not** mean that copies must always choose the same physical act. They implement the same mapping, but different inputs can produce different outputs. Nor does similarity between two agents prove they share a policy-selection computation. If they use different algorithms, receive differently interpreted inputs, or have conflicting utilities, their relationship requires a separate model. In a general-sum game, each agent may evaluate the same candidate policy using a different utility function; agreement and a shared tie-breaker cannot simply be assumed.

The example also exposes why “intervene on the policy” needs clarification. A whole-policy intervention changes all its entries together. An action-level intervention at input \(L\) need not determine what happens at \(R\); depending on its graph, it may leave the other entry fixed. The two procedures can therefore evaluate different counterfactuals. The source tells us that the preferred formulation chooses policies, but does not settle how to represent partial overlaps between computations or dependencies among different inputs.

## Applying P-FDT to an unfamiliar problem

A practical analysis can proceed in six stages.

1. **Specify inputs and feasible policies.** Include actions at relevant future or counterfactual observations. Exclude physically impossible actions; decide explicitly whether randomized policies are available.

2. **Choose the evaluation model.** State the utility function, uncertainty, and reference information state. Identify which observations are outcomes of policy-dependent processes.

3. **Identify the computation being intervened on.** Determine whether other agents implement that same policy selector, predict its output, predict one policy entry, or are independent of it.

4. **Construct a hypothetical for each policy.** Set the policy-output node to the candidate, propagate the stipulated subjunctive dependencies and ordinary causal effects, and leave unrelated background variables governed by their existing distributions.

5. **Calculate expected utility.** Include histories in which the current observation does not occur, if the intervention can change whether it occurs. Check that error probabilities are specified under each candidate rather than inferred from an aggregate correlation.

6. **Select and apply.** Choose a maximizing policy using an explicit tie-breaker, then apply it to the actual input. Check whether later uses of the procedure reproduce the intended policy; if not, the model of sequential choice needs further work.

This procedure is only as reliable as its counterfactual model. A useful diagnostic is to ask which mechanism makes another system’s output vary when the policy output varies. A literal copy, a simulation, and a predictor with measured conditional accuracy support different strengths of dependence. A coincidental correlation supports none by itself.

Randomization adds another distinction. A predictor might know a policy’s probability distribution without knowing the result of a genuinely private future random draw. An intervention on the policy should then change the distribution, not automatically make the predictor know the realized draw. Pseudorandom seeds visible to a predictor may behave differently.

## Open foundations and interpretation

P-FDT’s counterfactuals can be **counterpossible**. If a deterministic computation in fact outputs \(\pi^\star\), then on the same input it cannot mathematically output a different \(\pi\). Nevertheless, the procedure asks what would obtain if it did. Ordinary conditioning is inadequate if the alternative has probability zero; a causal-style graph can provide stipulated answers, but the source acknowledges that a satisfactory general account of these logical interventions is missing.

Other choices remain unsettled: whether policies are finite or computable, how to handle ties and optimization that lacks a maximum, how to model predictors of parts of policies, and how a later agent identifies the same reference state or selector. Self-reference can be represented computationally, but that alone does not prove that the resulting optimization terminates or has a unique, stable answer.

Finally, performance claims need a qualification. The paper argues that functional decision theory performs well in “fair” problems, where outcomes depend on behavior in the problem rather than directly rewarding a named theory. It also acknowledges that fairness is not formally settled and that no theory wins every constructed problem. P-FDT’s favorable examples motivate the approach; they do not prove universal optimality, nonnegative value of information in every formalization, or automatic resistance to every manipulation.

## Conclusion

P-FDT evaluates candidate mappings from inputs to actions by varying the output of the policy-selection computation and tracing the relevant causal and subjunctive consequences. It can therefore account for predictors and copies without treating every correlation as something the agent controls. Its distinctive strength is also its central challenge: useful decisions require a defensible account of which computations depend on the selected policy, and of how to evaluate alternatives that may contradict a fixed computation’s actual output.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6 and footnote 16, [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6461b60a-4b89-49b4-842a-22b840d3c2cb/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6461b60a-4b89-49b4-842a-22b840d3c2cb/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Evaluating policy selection**

I need to choose a shared policy selection that takes into account symmetric preferences and inputs. If I use an asymmetric policy, it might favor my own input, but different utilities can lead to uncertainty in the shared selector. With a symmetric identity interpretation, this same selector feels like a constant, even if it seems quiet. It’s all a bit complex, trying to make everything align properly.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6461b60a-4b89-49b4-842a-22b840d3c2cb/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6461b60a-4b89-49b4-842a-22b840d3c2cb/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
