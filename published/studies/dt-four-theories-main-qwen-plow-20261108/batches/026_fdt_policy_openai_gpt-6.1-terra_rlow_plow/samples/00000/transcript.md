# 026_fdt_policy_openai_gpt-6.1-terra_rlow_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/328a559e-3452-40dd-bf07-432ab9066e89/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/328a559e-3452-40dd-bf07-432ab9066e89/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: choosing a policy as the output of a decision function

A decision is often described as a choice among physical acts: take one box or two, pay a driver or keep the money, cooperate or defect. Policy functional decision theory—**P-FDT**—starts one level higher. It asks which *policy*, understood as a mapping from possible inputs to actions, the agent’s decision procedure should output. The agent then applies the selected policy to its actual input.

The motivation is that an agent’s act can be linked to other events without causing them. A predictor may have already acted on a forecast of the agent’s decision; another agent may run the same computation; a simulation may reproduce the relevant reasoning. P-FDT proposes evaluating alternative policies while preserving these dependencies, rather than changing one physical act and holding every non-effect fixed.

This essay takes footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory* as its starting point. The footnote says that the authors’ preferred formulation intervenes on the decision function to select “not an action but a *policy* which maps inputs to actions,” and that the agent applies its inputs to the resulting policy. The paper’s main equations instead intervene on an action-valued output. Footnote 7 also states the policy formulation and notes that it can matter in multi-agent dilemmas.

The footnote does not provide a complete algorithm for policy selection. In particular, it does not settle every question about the policy space, observations, randomization, or the construction of logical counterfactuals. The mathematical procedure below is therefore an **operational interpretation**, not a theorem or fully specified definition supplied by the paper.

## 1. The distinctive counterfactual

Let \(A\) be an action, \(O\) an outcome, \(U(O)\) utility, and \(x\) the agent’s observation. Two familiar approaches evaluate actions differently.

Evidential decision theory (**EDT**) compares

\[
\mathbb E[U(O)\mid A=a,x].
\]

It asks how good the outcome would be as *news*, conditional on taking \(a\). Causal decision theory (**CDT**), in a graphical formulation, compares

\[
\mathbb E[U(O)\mid \operatorname{do}(A=a),x].
\]

It changes the physical action and propagates its causal effects, while leaving causal non-effects unchanged.

P-FDT instead asks what would follow if the relevant **decision function selected a different policy**. That change can affect the agent’s action and also a predictor’s model, copies of the computation, or other systems whose behavior depends on the same policy output. It does not, merely because the agent’s action is statistically correlated with a fact, change that fact.

The paper calls the relevant relation **subjunctive dependence**. Causal dependence is one example: a scribe’s writing depends on the calculator output she observes. Shared computation is another: two reliable calculators given the same input produce the same answer even if neither causes the other’s output. A correlation with no such dependence—for example, two calculators that happen to have the same color—does not suffice.

Thus the slogan is not “change everything correlated with my decision.” It is:

> Vary the decision-function output and propagate the consequences through the dependencies the model says are relevant, while holding unrelated background factors fixed.

These are hypothetical changes to a model, not claims that an agent sends information into the past or physically manipulates mathematics. The paper treats hypotheticals as tools for decision-making, not as beliefs about literal alternative universes.

## 2. Policies and the selection rule

Let \(\mathcal X\) be a set of decision-relevant inputs and \(\mathcal A(x)\) the actions available at input \(x\). A deterministic policy is a function

\[
\pi:\mathcal X\to\mathcal A,
\qquad \pi(x)\in\mathcal A(x).
\]

An input might include the observation history, available actions, and other information the policy is permitted to use. It must not contain unavailable future information: otherwise the policy would not be implementable. In a sequential problem, \(x\) can be a history and \(\pi(x)\) the next action.

Write \(S\) for the mathematical decision procedure whose output is a policy, and let \(\Pi\) be a variable in the world-model representing that output. For each candidate \(\pi\), suppose the model supplies a counterfactual distribution

\[
Q_\pi(\,\cdot\,)
   =P_G\!\left(\,\cdot\mid \operatorname{do}(\Pi=\pi)\right).
\]

The subscript \(G\) emphasizes that the model includes assumptions about dependence, not just an ordinary probability distribution. The intervention sets the policy-output variable to \(\pi\), then propagates that assignment through the relevant logical, computational and causal structure.

An illustrative P-FDT rule is

\[
\pi^*\in\arg\max_{\pi\in\mathcal P}
       \mathbb E_{Q_\pi}[U(O)],
\qquad
a^*=\pi^*(x_{\mathrm{actual}}).
\tag{1}
\]

Here \(\mathcal P\) is the admissible policy class, and a fixed tie-breaking rule can make the output unique. The first line selects a complete mapping; the second applies it to the input actually received.

Equation (1) is deliberately conditional on a model. It does not tell us how to infer \(G\), which prior to use, or how to represent every logical dependency. Nor is ordinary conditioning on \(\Pi=\pi\) generally adequate. If \(S\) is deterministic, exactly one policy is its actual output; a different output is, in a strict mathematical sense, impossible. P-FDT nevertheless needs nontrivial **counterpossible** evaluations of those alternative outputs. The paper proposes using a graph with a suitable intervention point as a provisional way to represent them, while acknowledging that a general theory of such counterfactuals remains open.

The intervention is also different from simply imagining that the agent installs an unrelated policy. A predictor may be predicting the output of *this* selector \(S\). Replacing the agent’s physical software after the prediction while leaving the predictor’s model of \(S\) unchanged would omit precisely the dependence P-FDT is intended to track. In the hypothetical, the model instead asks what the predictor and other dependent systems would do if the relevant output of \(S\) were \(\pi\).

## 3. What is held fixed?

A useful way to build a P-FDT model is to separate background uncertainty from downstream responses. Suppose \(Z\) represents exogenous facts and noise, and a model specifies an outcome

\[
O_\pi=F(\pi,Z).
\]

Then, for a chosen distribution over \(Z\),

\[
V(\pi)=\mathbb E_Z[U(F(\pi,Z))].
\tag{2}
\]

For each candidate, use the same distribution over background factors that do not depend on the policy output. Recompute things that do depend on it. These may include:

* the agent’s action \(\pi(x)\);
* an accurate prediction or simulation of that action;
* another implementation of the relevant policy;
* an observation caused by the predictor’s response;
* ordinary causal consequences of those events.

This does **not** mean that every instance of a similar algorithm changes together. Two agents can use different inputs, different selector invocations, or decision procedures that are only weakly related. Their relationship must be modeled. Nor does it mean a predictor is infallible: error mechanisms and their dependence on the candidate policy belong in \(F\).

The distinction from EDT is clearest in the smoking-lesion example. In the fictional problem, a lesion makes smoking attractive and also causes cancer; smoking itself does not cause cancer. If smoking gives the agent \(1{,}000\) units of utility, varying the policy between smoking and refraining need not vary the lesion or cancer. On that model, smoking adds \(1{,}000\) without changing the cancer probability.

An EDT calculation that conditions only on the act may instead treat smoking as bad news about the lesion. The paper notes, however, that the lesion example needs care: self-knowledge and the consistency of an agent’s beliefs about its own preferences complicate the simple EDT calculation. The robust P-FDT point is narrower: a statistical association by itself is not a reason to make cancer change in a policy counterfactual.

## 4. Newcomb’s problem under P-FDT

An opaque box contains \(\$1{,}000{,}000\) if a predictor predicted that the agent would take only that box. A transparent box contains \(\$1{,}000\). The predictor has already acted and is \(99\%\) accurate. Assume the relevant policy has only the two possible outputs, one-box and two-box, and that prediction error has the same probability under each candidate.

P-FDT compares the policies using the dependence between the selector’s output and the prediction:

\[
\begin{aligned}
V(\text{one-box})&=0.99(1{,}000{,}000)=990{,}000,\\
V(\text{two-box})&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

It selects one-boxing. CDT instead holds the already-filled or already-empty box fixed when changing the physical act, so taking the extra \(\$1{,}000\) dominates in its causal comparison. EDT commonly also one-boxes, but by conditioning on the action rather than by representing the prediction mechanism.

The predictor’s overall track record alone is not always enough to justify the two numbers above. What matters is the model’s prediction error *under each candidate policy*. A predictor that is \(99\%\) accurate in a population might be unreliable for a particular unusual policy. P-FDT requires the appropriate counterfactual response model, not an automatic “predictors always match me” rule.

There is no backward causation in this calculation. The actual decision does not physically refill an already prepared box. The counterfactual says that, if the relevant selector output had been different, an accurate earlier prediction of that output would generally have been different too.

## 5. Why a whole policy can matter

In a one-input problem, policy selection may collapse to action selection. With several inputs, the distinction is substantial: one policy-output intervention can change what the same policy prescribes at several inputs at once.

Consider two separated copies that implement the *same selected policy*. One receives input \(L\), the other \(R\), and each chooses \(0\) or \(1\). Suppose the objective used by the shared selector assigns both copies payoff

\[
u(0,0)=2,\quad u(1,1)=3,\quad
u(0,1)=u(1,0)=0.
\]

There are four deterministic policies, specified by \((\pi(L),\pi(R))\). Their values are respectively \(2,0,0,3\), so equation (1) selects

\[
\pi^*(L)=1,\qquad \pi^*(R)=1.
\]

Each copy applies that policy to its own input and outputs \(1\).

By contrast, a comparison that changes only the action at \(L\), holding the action at \(R\) fixed at \(0\), prefers \(0\): it sees \(2\) rather than \(0\). The analogous single-site comparison at \(R\) also prefers \(0\). Joint policy comparison can move from \((0,0)\) to \((1,1)\), whereas these local comparisons cannot.

This example makes an additional modeling assumption: both copies really are controlled by one relevant policy output and evaluate the same payoff. If they run separate selectors with distinct objectives or merely resemble one another, intervening on one selector need not alter the other. Footnote 16 says the policy/action distinction matters in multi-agent dilemmas, but it does not prescribe how to determine shared implementation in every case.

The familiar psychological-twin prisoner’s dilemma illustrates a related, simpler dependency. If two twins compute the same decision on the same input, their outputs match. With mutual cooperation worth \(\$1{,}000{,}000\) and mutual defection worth \(\$1{,}000\), P-FDT selects cooperation. This is not a claim that cooperation benefits the agent against every opponent; it depends on the modeled link between the decisions.

## 6. Observations, policies and the global perspective

The most consequential ambiguity in equation (1) is the distribution used to evaluate a policy after the agent has observed \(x_{\mathrm{actual}}\). Should the agent condition every candidate on that observation? Or should it evaluate complete policies from an earlier perspective, allowing the observation itself to differ between candidates?

The paper’s action-level formulation takes the latter approach in important examples. Its agent responds to an observation by changing the node at which it intervenes, rather than always conditioning its hypotheticals on the observation. A counterfactual action can therefore correspond to a world in which the agent would have seen something else.

A natural **policy-level proposal** is to choose a reference distribution before observations that may themselves depend on the selected policy. Inputs then appear inside the policy as contingencies: “if I see this, do that.” Evidence about stable background facts can be incorporated in the reference model, but policy-dependent observations are generated anew under each candidate. This resembles an ex ante policy comparison, though the policy output is still treated as the output of the actual selector, not merely as a physical commitment device.

Consider transparent Newcomb: the predictor fills the large box if it predicts that the agent would one-box *upon seeing it full*. Assume an accurate predictor with symmetric error probability \(0.01\). Let the policy take both boxes if the large box is empty. Compare two policies:

\[
\begin{array}{ll}
\pi_1:&\text{one-box if full; two-box if empty},\\
\pi_2:&\text{two-box whether full or empty}.
\end{array}
\]

Their values are

\[
\begin{aligned}
V(\pi_1)
 &=0.99(1{,}000{,}000)+0.01(1{,}000)
 =990{,}010,\\
V(\pi_2)
 &=0.01(1{,}001{,}000)+0.99(1{,}000)
 =11{,}000.
\end{aligned}
\]

Thus the proposed P-FDT policy one-boxes upon actually seeing a full box. If the large box is empty, it takes the small box.

The result is deliberately surprising. Conditional on seeing a full box, taking both boxes yields \(\$1{,}000\) more. But conditioning on fullness in *both* candidate evaluations would remove most of the policy’s effect on what the predictor does and what the agent sees. The global comparison instead evaluates the whole policy, including the probability of reaching each input.

This is not a license to ignore all evidence. It is a choice about **which evidence defines the reference distribution** and which observations are outcomes of the policy-dependent model. Footnote 16 does not completely settle that choice. Different reference points can yield different prescriptions, particularly after surprising evidence. A usable implementation must state its rule for incorporating observations rather than silently assuming one.

## 7. P-FDT and blackmail

The same global comparison explains why P-FDT can refuse a threat even after receiving it. Suppose a mechanical blackmailer runs a program if she predicts payment. The program causes a loss of \(L=\$1{,}000{,}000\) unless the agent pays \(c=\$1{,}000\). If she predicts refusal, she normally does not run it.

For a simple model, let a payment policy be blackmailed with certainty, and let a refusal policy be blackmailed by mistake with probability \(\varepsilon\). Relative to no loss,

\[
V(\text{pay policy})=-c,\qquad
V(\text{refuse policy})=-\varepsilon L.
\]

Refusal is preferable exactly when

\[
\varepsilon L<c.
\]

At \(\varepsilon=0.0009\), the expected loss from refusal is \(\$900\), so refusal wins. At \(\varepsilon=0.0011\), it is \(\$1{,}100\), so payment wins. These thresholds depend on the stated response model; the paper’s prose gives a second error percentage that is inconsistent with the conclusion that payment is then preferable.

If the agent actually receives a letter under the refusal policy, it suffers the loss in this model. P-FDT’s recommendation is based on the consequences of the *policy across its counterfactual applications*, including cases where no letter arrives. It is not based on a belief that a received letter will disappear. The tension between policy-level value and the apparent advantage of paying at the reached input is a central philosophical commitment of the view.

## 8. Limits and practical use

The procedure above gives a way to analyze unfamiliar cases, but its conclusions are only as good as its dependence model.

First, identify the selector and its output. Is the candidate a complete policy, a policy component, or a distribution over policies? Second, identify the inputs on which that policy can act. Third, describe which predictors, copies and causal processes respond to the selector’s output. Fourth, specify the reference uncertainty and propagate each candidate through the model. Finally, compare expected utilities and apply the winning policy to the actual input.

Several issues remain open:

* **Logical dependence.** The paper does not provide a general method for discovering the correct graph. Mathematical equivalence, imperfect simulation, shared code and behavioral similarity need not create the same dependency.
* **Policy boundaries.** A policy covering an entire life differs from one covering a narrow encounter. The footnote does not uniquely specify the domain or admissible class.
* **Randomization.** A policy may map inputs to distributions over actions, but one must model whether a predictor sees the distribution, the random seed, or neither. Shared and independent randomness produce different dependencies.
* **Dynamic consistency.** Recomputing from a different reference distribution at a later time need not reproduce the earlier selected policy. Stability requires assumptions about how the selector and its reference point persist.
* **Optimality.** The paper argues that its theory performs well in many examples, but explicitly leaves “fair” problem classes and general optimality unresolved. No decision theory can outperform every rival in every imaginable environment.

The authors emphasize that information should not have negative expected value when an agent can elect to ignore it. A policy-class argument supports that claim only under suitable assumptions: adding an observation cannot reduce the optimum if old policies remain available, obtaining the observation has no cost, and the environmental response model does not change disadvantageously. The result should not be asserted without those conditions.

## Conclusion

P-FDT evaluates decisions by varying the output of a policy-selecting decision function, propagating that variation through relevant causal and computational dependencies, and applying the best policy to the input actually received. Its characteristic move is to preserve links to predictors and other implementations without treating every statistical correlation as controllable.

Footnote 16 supplies the policy-selection idea, not a complete counterfactual calculus. The operational account developed here makes the resulting questions explicit: which policy is selected, which systems depend on it, and from what informational perspective its consequences are valued. Answering those questions is essential both to applying P-FDT and to assessing whether its sometimes counterintuitive prescriptions are justified.

**Reference:** Eliezer Yudkowsky and Nate Soares, [*Functional Decision Theory: A New Theory of Instrumental Rationality*](https://arxiv.org/abs/1710.05060), version 2, especially §§3–6 and footnotes 7 and 16.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/71a055cd-6cd9-46f2-8d8a-ec6c66a6b064/call_0/request.json)

[Authoritative raw response](../../../../../../runs/71a055cd-6cd9-46f2-8d8a-ec6c66a6b064/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/71a055cd-6cd9-46f2-8d8a-ec6c66a6b064/call_1/request.json)

[Authoritative raw response](../../../../../../runs/71a055cd-6cd9-46f2-8d8a-ec6c66a6b064/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
