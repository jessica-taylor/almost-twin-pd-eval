# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00017

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0a0d54d5-18c9-4444-ae47-cf505d8980ab/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0a0d54d5-18c9-4444-ae47-cf505d8980ab/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: choosing the output of a decision procedure

A decision can matter in ways that are not captured by asking what a physical movement causes. A predictor may have already acted on a model of what you will decide. A person in another room may reach the same conclusion because she is running the same reasoning. In such cases, changing your action while holding the prediction or the other person’s reasoning fixed may be a poor way to evaluate your options.

**Action functional decision theory (A-FDT)** addresses this by evaluating hypothetical outputs of the decision procedure itself. Its central question is: *Which output of this procedure corresponds to the best outcome, once the consequences and other dependencies of that output are represented?*

The account below takes Equation (4), Section 5 of Yudkowsky and Soares’s paper as its primary definition. The paper uses “functional decision theory” as its general name; here **A-FDT** denotes the action-output formulation in that equation. The authors also mention a preferred policy-output formulation. That related formulation should not be silently substituted for the action rule: choosing a whole mapping from observations to actions can differ from choosing the output associated with one observation.

## The decision-theoretic question

Suppose an agent has actions \(a\in\mathcal A\), possible outcomes \(o\), and a utility function \(U(o)\). An expected-utility rule selects an action maximizing

\[
\sum_o P_a(o)U(o),
\]

where \(P_a\) is the distribution used to represent what would happen under the hypothetical action \(a\). The central disagreement between decision theories concerns how to construct \(P_a\).

**Evidential decision theory (EDT)** uses ordinary conditionalization:

\[
\operatorname{EDT}(P,x)
\in\arg\max_a \mathbb E_P[U\mid X=x,A=a].
\]

It asks what taking \(a\) would be evidence about, given observation \(x\).

**Causal decision theory (CDT)**, in the paper’s graphical presentation, instead intervenes on the physical action:

\[
\operatorname{CDT}(P,G,x)
\in\arg\max_a
\mathbb E_P[U\mid \operatorname{do}(A=a),X=x].
\]

Here \(G\) represents causal relationships. The intervention replaces the mechanism determining \(A\), while its downstream causal effects are recalculated. A prediction made yesterday is not a causal descendant of today’s physical act, so it ordinarily remains fixed.

A-FDT also uses a graph and an intervention, but its intervention target is different. It changes a variable representing the output of the decision computation, not merely the physical act that computation produces. This can change a predictor’s prediction or a copy’s decision in the hypothetical, even when neither is causally downstream from the agent’s physical action.

The paper’s motivation is consequentialist: a good decision procedure should tend to produce valuable outcomes. Its philosophical wager is that the correct counterfactual perspective includes relevant computational and logical dependencies, as well as causal ones.

## The A-FDT equation

Let \(P\) be a probability model, \(G\) a graph describing relevant dependencies, and \(x\) the agent’s observation history. Write

\[
D_x=\mathsf{afdt}(\underline P,\underline G,\underline x)
\]

for a **variable inside the model** representing the output of A-FDT on those inputs. The underlines indicate that the variable’s name refers to the particular inputs. \(D_x\) is not itself the action returned by the algorithm; it is the model’s representation of that output.

In this notation, the paper’s Equation (4) becomes

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[U\mid
\operatorname{do}(D_x=a)\right].
}
\tag{A-FDT}
\]

The notation after the expectation denotes an **interventional distribution**, not ordinary conditioning on the proposition \(D_x=a\). Operationally, for each candidate \(a\):

1. Identify the node \(D_x\) representing the output of this decision procedure on inputs \((P,G,x)\).
2. Replace that node’s determining mechanism with the value \(a\).
3. Recompute the nodes downstream of \(D_x\) according to the dependency structure in \(G\).
4. Compute expected utility in the resulting hypothetical.
5. Return a maximizing action, using a specified tie-breaking rule if needed.

The graph can include paths from \(D_x\) to the agent’s act, to another implementation of the same computation, and to an imperfect predictor’s output. It also includes ordinary causal paths from those variables to outcomes. Nodes not downstream of the intervention retain their modeled distribution, subject to the rest of the structural model.

There is an important difference from the CDT equation: **A-FDT does not add \(X=x\) as a separate conditioning clause.** In the paper’s treatment, an observation changes which node is intervened on—from \(D_x\) to \(D_y\), for instance. The hypothetical generated by changing \(D_x\) can consequently include histories in which the agent does *not* observe \(x\). This feature drives the paper’s treatment of transparent Newcomb and blackmail.

That does not mean observations are irrelevant. They determine the computation whose output is under consideration, and the model must still represent how observations affect behavior. But one must not casually both intervene on \(D_x\) and condition every hypothetical on \(X=x\): that is a different rule and can erase the intended predictor dependence.

There is a textual wrinkle worth noting. In its later transparent-Newcomb calculation, the paper writes a formula that appears to include an intervention on the observation as well. Its numerical derivation, however, explicitly allows the observation to differ between hypotheticals. For consistency with Equation (4) and the accompanying explanation, the calculations below follow the latter reading.

## What does “subjunctive dependence” add?

The paper calls the relevant broader relation *subjunctive dependence*. If two machines compute the same function on the same input, their outputs agree insofar as both computations work correctly. Neither output need physically cause the other. Likewise, a predictor may run an accurate model of an agent, so its prediction tracks the agent’s decision computation without being caused by the agent’s later bodily movement.

A-FDT’s graph is intended to preserve such relationships when the decision-output node is changed. It does **not** preserve every observed correlation. If a lesion independently makes cancer likely and makes an agent enjoy smoking, cancer need not change in a hypothetical where the agent’s decision procedure outputs a different smoking action. The lesion is a common cause, not a predictor of that output.

This distinction cannot be read off from correlation alone. Two probability distributions may look alike while their dependency graphs prescribe different interventions. The graph is therefore doing substantive work; it is not just a visual restatement of \(P\).

Nor does A-FDT claim that an agent can send a physical signal into the past or literally alter a mathematical theorem. If a deterministic computation has an actual output, a hypothetical in which that same computation has another output is, strictly speaking, a **counterpossible**: its antecedent contradicts a logical fact. The graph supplies a disciplined way to calculate with such a supposition without treating every contradiction as proving every outcome.

The paper acknowledges that this is its main technical gap. It does not provide a general method for learning all logical and computational dependencies, nor prove that an ordinary Pearl-style graph can always represent them satisfactorily. Self-reference is also present: the model contains a node naming the output of the algorithm applied to that model. The authors appeal to self-referential constructions to argue that naming such a node is possible; that observation does not itself solve the harder problem of constructing a correct dependency graph or ensuring a tractable computation.

## A-FDT in Newcomb’s problem

A predictor fills an opaque box with \$1,000,000 if she predicts that the agent will take only that box. A transparent box contains \$1,000. The agent may take one box or both. Assume a symmetric error model: for either candidate output of the decision procedure, the predictor matches it with probability \(0.99\).

Let \(D\) be the decision-output node, \(A=D\) the actual action, and let the predictor’s output equal \(D\) except when an error variable fires. The predictor fills the opaque box exactly when it predicts one-boxing.

Under \(\operatorname{do}(D=\text{one})\),

\[
V(\text{one})=0.99(1{,}000{,}000)=990{,}000.
\]

Under \(\operatorname{do}(D=\text{two})\),

\[
V(\text{two})
=0.01(1{,}000{,}000)+1{,}000
=11{,}000.
\]

A-FDT therefore one-boxes. CDT, intervening on the later physical act while holding the box contents fixed, two-boxes. EDT can also one-box, but does so because one-boxing is evidence that the box is full, rather than because it explicitly models a shared computational dependency.

The numerical result requires more than the statement “the predictor was right 99% of the time.” Aggregate historical accuracy need not imply a 99% match rate under *each* intervention on this particular decision output. The symmetric error mechanism is an additional modeling assumption, used by the paper’s example.

More generally, let \(p_1\) be the probability that the opaque box is full under the one-box intervention and \(p_2\) its probability under the two-box intervention. With a large-box prize \(M\) and a sure extra amount \(b\), A-FDT one-boxes when

\[
M(p_1-p_2)>b.
\]

Thus even an imperfect predictor can make one-boxing worthwhile, but mere prediction is not enough: the change in its response must be large enough relative to the foregone payment.

## A-FDT and the smoking lesion

Now suppose, in an imaginary medical problem, smoking causes no cancer. An unseen lesion both makes cancer more likely and makes its bearer inclined to smoke. Smoking itself gives the agent utility \(b>0\).

In a simplified A-FDT model, let \(L\) be lesion status, \(C\) cancer status, and \(D\) the relevant decision output. The graph includes \(L\to C\) and \(D\to A\), but no path \(D\to C\). If \(p\) is the agent’s probability of cancer under either intervention, then

\[
V(\text{smoke})=M(1-p)+b,
\qquad
V(\text{refrain})=M(1-p).
\]

A-FDT smokes. Changing the decision output changes the act, not the lesion or its consequences. A simple EDT model can instead refrain if smoking is sufficiently strong evidence of the lesion.

The source’s fuller model is more delicate. It allows the lesion to determine which of two utility models and hence which decision computation controls behavior. Intervening on one computation affects the act only in the worlds where that computation is selected; the gain from choosing smoking is then weighted by the probability of being in those worlds. The paper also regards the standard smoking-lesion setup as contrived and notes that refined EDT defenses can address it. The lesson is the distinction between predictive dependence and common-cause correlation—not a proof that every EDT formulation must refuse to smoke.

## Observations that change across A-FDT hypotheticals

Consider **transparent Newcomb**. The predictor fills the large box if she predicts the agent will one-box *upon seeing it full*. The agent now sees it full.

Let \(D_F\) represent the decision computation on the full-box observation, and \(D_E\) the computation on the empty-box observation. Suppose the predictor predicts \(D_F\) correctly with probability \(0.99\), and let \(q\) be the probability that the empty-box computation two-boxes.

If A-FDT intervenes to set \(D_F=\text{one}\), the box is full with probability \(0.99\); with probability \(0.01\) the predictor errs, the box is empty, and \(D_E\) governs the act. Its value is

\[
V_F(\text{one})=990{,}000+0.01q(1{,}000).
\]

If it sets \(D_F=\text{two}\), the predictor usually leaves the box empty, so the full-box computation usually does not control the physical action:

\[
V_F(\text{two})
=0.01(1{,}001{,}000)+0.99q(1{,}000).
\]

The first value is larger for every \(q\in[0,1]\). A-FDT therefore one-boxes upon seeing the full box.

This is the theory’s most striking departure from ordinary conditional reasoning. The agent does not deny seeing the full box. Rather, when assessing what the *full-observation computation* should output, it includes worlds in which changing that output would have changed the prediction, and hence the observation. In those worlds the computation may be evaluated by the predictor without ever being physically executed by the agent.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded agent only if she predicts that the agent will pay after arrival. On the paper’s assumptions, A-FDT pays in the city: the hypothetical output “pay” is linked to being rescued, while “refuse” is linked to being left in the desert. This is not a claim that paying now physically causes the past rescue.

## A-FDT and a credible threat

The same logic can prescribe resisting a threat, but only when the modeled dependence makes resistance advantageous.

Suppose a blackmailer launches a damaging program if she predicts the agent will pay on receiving a letter. Paying costs \$1,000; refusing after launch costs \$1,000,000. Assume, for illustration, that a payer is blackmailed with probability one, while a refuser is mistakenly blackmailed with probability \(\varepsilon\). Then the A-FDT values of the letter-contingent output are

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-\varepsilon(1{,}000{,}000).
\]

Refusal is preferred when \(\varepsilon<0.001\). If \(\varepsilon=0.0009\), its expected loss is \$900, so A-FDT refuses even on receiving the letter. If \(\varepsilon=0.0011\), the expected loss is \$1,100, and paying is preferred under these assumptions.

This is not a universal injunction never to pay blackmail. If the blackmailer has already launched the program independently of predictions about this decision output, or if the response probabilities differ, the calculation changes. The theory’s prescription depends on the mechanism, not on the label “blackmail.”

## Applying A-FDT to unfamiliar cases

A workable procedure, consistent with Equation (4), is to make the model explicit before calculating:

1. **Specify the target computation.** Identify the observation \(x\), the candidate outputs, and the model node \(D_x\). Distinguish it from the physical action \(A\).
2. **Model the environment’s response.** Identify predictors, simulations, copies, and causal consequences. State which of them depend on \(D_x\), and quantify error or uncertainty.
3. **Represent observation-dependent execution.** If an intervention can change the observation, include nodes such as \(D_x,D_y\) and a rule selecting which one controls the physical act.
4. **Construct one interventional distribution per output.** Replace the mechanism for \(D_x\), propagate changes through the graph, and retain unrelated background variables.
5. **Compare expected utilities.** Report the values and the assumptions on which their ordering depends.

For imperfect twins or predictors, a useful *operational proposal* is to use stochastic structural mechanisms: for example, a twin’s action matches \(D_x\) with probability \(r\), and otherwise follows a specified error distribution. One then propagates that mechanism under each intervention. This is a modeling proposal, not a general solution supplied by the paper. In particular, the match probability must describe how the twin responds under the relevant counterfactual output, not merely an observed correlation in an unrelated population.

The same caution applies to repeated or multi-agent decisions. Two agents being similar is not enough to set their actions equal under intervention. They may have different observations, payoffs, random seeds, or source code. Conversely, if they really implement the same relevant computation, the graph should not treat their decisions as independent merely because they occupy separate rooms.

A policy-based extension might instead intervene on a node whose value is a whole function \(\pi:x\mapsto a\), then execute \(\pi(x)\). The source says its authors prefer such a formulation in general, particularly for some multi-agent problems, but does not derive it from Equation (4). As a proposed extension it can be useful, yet its policy space, dependencies, and relation to the action rule require separate specification.

## Limits and the case for A-FDT

A-FDT’s appeal is that it combines two intuitions: ignore correlations that do not track the decision computation, but retain dependencies that a predictor or another implementation creates. In the examples, this yields one-boxing in Newcomb, smoking in the lesion problem, cooperation with a sufficiently exact twin, and payment in the hitchhiker case.

Those successes are not a theorem that A-FDT wins in every environment. The paper itself concedes that an adversary can reward or punish agents for their decision procedure. It proposes an informal distinction between such “unfair” problems and problems rewarding predicted actions, but leaves a general formal criterion of fairness open. Its claims about nonnegative value of information and acting as one would have precommitted are motivations and results for its intended settings, not consequences established for every possible A-FDT graph.

The largest practical uncertainty remains the graph. A wrong graph can manufacture a fictitious predictor dependency or miss a real one. Counterpossible semantics, logical uncertainty, computational limits, tie-breaking, and randomized decisions also need further treatment. A-FDT supplies a decision rule *given* a suitable model; it does not yet supply a complete general algorithm for discovering that model.

## Conclusion

A-FDT evaluates actions by intervening on the modeled output of the decision procedure for the current input, then propagating all represented decision-relevant dependencies. This changes the unit of counterfactual evaluation from a physical act to a computation’s output.

Its distinctive cases show why that change can matter: a predictor or twin may track the computation even when it is not caused by the agent’s act. Whether A-FDT is a satisfactory general theory depends on the unresolved task of representing those dependencies reliably—and on whether its global counterfactual perspective is the right one for rational choice.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially Sections 3, 5 and 6. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e4f2df2f-2118-4ed3-bc70-808584f9740c/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e4f2df2f-2118-4ed3-bc70-808584f9740c/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e4f2df2f-2118-4ed3-bc70-808584f9740c/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e4f2df2f-2118-4ed3-bc70-808584f9740c/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
