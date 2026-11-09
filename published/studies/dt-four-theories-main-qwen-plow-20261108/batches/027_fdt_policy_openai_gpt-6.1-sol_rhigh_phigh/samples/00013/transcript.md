# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/af483c0b-aafe-4044-a500-bb938db5b49f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/af483c0b-aafe-4044-a500-bb938db5b49f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing a Policy, Not Just an Act

## 1. The policy-selection idea

A decision can matter in more places than the physical location where it is executed. A predictor may have anticipated it; another agent may be running the same computation; a simulated copy may already have produced the same answer. **Policy functional decision theory (P-FDT)** evaluates decisions while preserving these computational dependencies, rather than considering only the causal consequences of a particular bodily action.

The primary source for P-FDT here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory*. It describes their preferred formulation as choosing

> “not an action but a policy which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

Footnote 7 similarly identifies policies as mappings from observations to actions. These passages specify an important architectural distinction: first select an entire input–output rule, then apply that rule to the input actually received.

The paper develops an action-selection formulation in much greater detail. That formulation supplies motivation and examples, but it should not silently replace the policy-selection proposal. In particular, changing a whole policy can coordinate responses across different observations, including observations received by other implementations of the same policy selector.

The footnote does not provide a complete mathematical definition. This essay therefore distinguishes its explicit proposal from an **operational reconstruction**: select a policy by comparing counterfactual outcomes in which the output of the policy-selection computation differs, preserving the dependencies that the world has on that output.

The philosophical motivation is instrumental, not altruistic. The question is: *Which policy output corresponds to the best expected outcome for this agent, taking all relevant dependencies into account?*

## 2. A mathematical reconstruction of P-FDT

Begin with a finite decision problem. Let:

- \(\mathcal X\) be a finite set of possible inputs or observation histories;
- \(\mathcal A\) be a finite action set;
- \(\Pi\subseteq\mathcal A^{\mathcal X}\) be the admissible policies;
- \(\mathcal O\) be the outcome space;
- \(U:\mathcal O\to\mathbb R\) be the agent’s utility function.

A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
For a sequential problem, \(x\) can be a complete observation–action history, so a policy specifies behavior at every decision point, including points never reached.

Let \(M\) be the agent’s evaluation model. It contains probabilities, utilities, environmental mechanisms, and a proposed account of computational and causal dependencies. Write
\[
\mathcal S(M)\in\Pi
\]
for the policy-selection computation, and let \(L_M\) be a variable *inside the model* representing its output.

For each candidate policy \(\pi\), construct a counterfactual outcome distribution
\[
K_M(o;\pi)
=
P_M\!\left(
O=o\;\middle\|\;
L_M\leftarrow\pi
\right).
\]
The double bar is deliberate: this is not ordinary Bayesian conditioning. It denotes a **subjunctive intervention**, changing the represented output of the selector and propagating the changes licensed by the model’s dependency structure.

My reconstructed selection rule is
\[
\pi_M^*
\in
\operatorname*{arg\,max}_{\pi\in\Pi}
V_M(\pi),
\qquad
V_M(\pi)
=
\sum_{o\in\mathcal O}K_M(o;\pi)U(o).
\tag{1}
\]
After receiving input \(x\), the agent acts according to
\[
a=\pi_M^*(x).
\tag{2}
\]
A fixed tie-breaking rule makes selection single-valued when necessary.

Equation (1) is a proposed completion of the footnote, not an equation explicitly supplied there. It extends the paper’s functional-counterfactual machinery from action-valued outputs to policy-valued outputs.

A useful equivalent representation introduces background uncertainty \(Z\), with distribution \(\mu_M\), and a counterfactual outcome function
\[
O_\pi=\Phi_M(\pi,Z).
\]
Then
\[
V_M(\pi)=
\mathbb E_{Z\sim\mu_M}[U(\Phi_M(\pi,Z))].
\tag{3}
\]
Crucially, \(\Phi_M\) includes environmental responses to the selected policy. A predictor’s forecast may change, as may the input the agent receives. Thus the resulting physical action is
\[
A_\pi=\pi(X_\pi),
\]
not necessarily \(\pi(x)\) with the actual observation held fixed.

Merely optimizing over policies does not distinguish P-FDT. Ordinary planning also does that. The distinctive feature is **where the counterfactual intervention occurs and which dependencies it preserves**.

## 3. What changes in a P-FDT counterfactual?

The paper calls the relevant relationship *subjunctive dependence*. Its central examples involve systems computing the same mathematical function, or one system accurately predicting another.

Suppose two physically separated machines implement the same policy-selection computation with the same model. Their policy outputs agree even without communication. In a P-FDT counterfactual where that computation outputs another policy, both implementations change correspondingly.

Similarly, if a predictor models the selector, its forecast should respond to a counterfactual change in the selector’s output. An imperfect predictor responds imperfectly, according to its modeled error mechanism.

But not every correlation should survive.

For comparison, **evidential decision theory (EDT)** evaluates actions using expressions such as
\[
\mathbb E[U\mid X=x,A=a].
\]
This preserves correlations that might merely make an action good or bad news.

**Causal decision theory (CDT)** instead uses causal interventions, schematically
\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]
This generally holds causally upstream predictions fixed.

P-FDT’s intervention is neither. It changes the represented policy output and preserves dependencies on that output, including ordinary causal consequences and relevant predictive relationships.

This does not posit backward causation. Imagining a different past prediction is part of comparing computational counterfactuals, not a claim that performing an action sends a signal into the past.

There is nevertheless a foundational difficulty. A fixed deterministic computation has only one actual output. Alternative-output suppositions can therefore be **counterpossible**: contrary to mathematical fact, rather than merely contrary to physical actuality. The paper acknowledges that it lacks a general satisfactory semantics for these suppositions.

Consequently, equations (1)–(3) are operational only when the counterfactual model is supplied. A dependency diagram is not enough by itself: one also needs mechanisms or kernels specifying how dependent variables respond.

## 4. P-FDT in Newcomb’s problem and the lesion problem

In Newcomb’s problem, an opaque box contains \(M\) dollars if a predictor forecasts one-boxing, and nothing otherwise. A transparent box contains \(k\) dollars. The agent chooses between taking only the opaque box and taking both.

Assume a symmetric predictor-error model: under the one-boxing policy the opaque box is full with probability \(p\), while under the two-boxing policy it is full with probability \(1-p\). Here the input set can be a singleton, so policies reduce to constant actions.

P-FDT compares
\[
V(\pi_{\mathrm{one}})=pM,
\]
\[
V(\pi_{\mathrm{two}})=(1-p)M+k.
\]
It one-boxes exactly when
\[
(2p-1)M>k.
\]
With \(p=0.99\), \(M=1{,}000{,}000\), and \(k=1{,}000\), the values are
\[
990{,}000
\quad\text{and}\quad
11{,}000.
\]

The policy counterfactual changes the forecast because the forecast concerns the policy’s behavior. Notice that an overall historical accuracy rate alone need not justify these two probabilities: the symmetric error mechanism is an additional modeling assumption.

Contrast the paper’s imaginary smoking-lesion problem. A lesion causes both a preference for smoking and cancer, while smoking itself has no effect on cancer. For an agent who enjoys smoking, changing the selected smoking policy does not change the lesion or cancer mechanism. If smoking adds utility \(s>0\), then
\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=s.
\]
P-FDT therefore permits smoking in that stipulated world without treating it as a way to alter one’s diagnosis.

The contrast is structural: a predictor models the decision computation; a lesion does not. The source itself cautions that fully formalizing the lesion example raises difficulties about preferences and self-knowledge, so it is better treated as an illustration than a decisive test.

## 5. P-FDT, observations, and contingent behavior

The policy-selection passage leaves an important question unresolved: **from which informational standpoint are policies evaluated?**

Selecting a policy after conditioning on every current observation can differ from evaluating policies in a model where those observations themselves depend on the policy output.

For the reconstruction used here, I adopt this convention:

> Within a specified decision problem, evaluate complete policies using a common model \(M\), allowing policy-dependent observations to vary counterfactually; use the actual observation to execute the selected policy.

This fits the paper’s transparent-box and blackmail reasoning. It is not a mandate to retain one immutable prior throughout life. The source does not fully specify where one decision problem ends, which background evidence belongs in \(M\), or when rebuilding \(M\) amounts to an inappropriate local reoptimization.

Consider transparent Newcomb. Let
\[
X\in\{\mathrm{full},\mathrm{empty}\}.
\]
A perfect predictor fills the opaque box exactly when it predicts that the agent will one-box *upon seeing it full*.

There are four deterministic policies. Two important ones are
\[
\pi_1(\mathrm{full})=\mathrm{one},
\qquad
\pi_1(\mathrm{empty})=\mathrm{two},
\]
and
\[
\pi_2(\mathrm{full})=\mathrm{two},
\qquad
\pi_2(\mathrm{empty})=\mathrm{two}.
\]
Under \(\pi_1\), the predictor fills the box, and the agent receives \(M\). Under \(\pi_2\), it leaves the box empty, and the agent receives \(k\).

The other two policies do no better: always one-boxing also yields \(M\), while two-boxing when full but one-boxing when empty yields zero. Thus every maximizing policy one-boxes when full.

After seeing the full box, taking the extra \(k\) is physically possible. But evaluating that act while holding the forecast fixed is not the policy counterfactual P-FDT uses. Changing the full-box response changes the predictor’s forecast and hence whether the full-box observation occurs.

Parfit’s hitchhiker has the same structure. A driver rescues an agent only if the driver predicts payment after arrival. With perfect prediction, rescue benefit \(B\), and payment \(k<B\),
\[
V(\pi_{\mathrm{pay\ if\ rescued}})=B-k,
\qquad
V(\pi_{\mathrm{refuse}})=0,
\]
relative to a no-rescue baseline. P-FDT pays upon arrival because that action executes the selected rescue-enabling policy—not because payment now causally produces an earlier rescue.

## 6. P-FDT and resisting blackmail

Policy selection also explains why refusing a demand can be useful without making refusal an unconditional rule.

Suppose a blackmailer launches a damaging mechanism only when it predicts payment. Payment costs \(k\); refusal after launch costs \(L\). Assume:

- a paying policy is always correctly predicted and targeted;
- a refusing policy is mistakenly targeted with probability \(r\).

Then
\[
V(\pi_{\mathrm{pay}})=-k,
\qquad
V(\pi_{\mathrm{refuse}})=-rL.
\]
P-FDT selects refusal when
\[
rL<k.
\tag{4}
\]

With \(L=1{,}000{,}000\), \(k=1{,}000\), and \(r=0.0009\), refusal has expected loss \(900\), less than payment’s \(1{,}000\).

Under the common-model convention, receiving a demand does not automatically trigger a fresh optimization conditional on launch. The selected policy can prescribe refusal even on its rare, costly branch.

This conclusion depends on the threat-generation mechanism. If launch is independent of the selected policy, payment may be preferable. Different false-positive and false-negative rates also change equation (4). P-FDT is not “never pay blackmail”; it is sensitivity to how policies affect targeting.

## 7. Why P-FDT selects whole policies: a multi-agent example

The source says policy selection can matter in multi-agent dilemmas but does not supply the relevant examples. The following is my illustration of why the distinction is substantive.

Two agents run the same policy selector with the same evaluation model. Each privately observes a cost
\[
C_i\in\{1,4\},
\]
independently, with equal probabilities. Each may give the other a benefit of \(3\), paying its own observed cost. Agent \(i\)’s utility is
\[
U_i=3A_j-C_iA_i,
\]
where \(A_i=1\) means giving.

Assume the shared selector outputs a policy
\[
\pi:\{1,4\}\to\{0,1\},
\]
and a counterfactual change in this output changes both implementations. The agents can nevertheless take different actions because their private inputs differ.

For either agent,
\[
V(\pi)
=
3\,\mathbb E[\pi(C_j)]
-
\mathbb E[C_i\pi(C_i)].
\]
The four policies have values:

| P-FDT candidate policy | Expected utility |
|---|---:|
| Never give | \(0\) |
| Give only at cost \(1\) | \(1.5-0.5=1\) |
| Give only at cost \(4\) | \(1.5-2=-0.5\) |
| Always give | \(3-2.5=0.5\) |

P-FDT selects giving only at the low cost.

This is not altruistic maximization of total welfare. Each agent maximizes its own expected utility. The gain arises because changing the shared policy output changes what the other implementation does across its possible inputs.

Nor does sharing the label “P-FDT” suffice to establish this coupling. The example explicitly assumes a shared computation and evaluation model. Different goals, models, or selection procedures may weaken or eliminate the dependency.

The example also exposes the informational issue. If a low-cost agent conditions on its own cost before evaluating a *shared* policy change, always giving scores \(3-1=2\), exceeding low-cost-only giving’s \(1.5-1=0.5\). That differs from the common-model optimum. Thus the standpoint of policy evaluation cannot be left implicit.

## 8. Applying P-FDT responsibly

For an unfamiliar case, the following procedure makes the central modeling commitments explicit.

1. **Specify the policy domain.** What observations, histories, roles, or private signals can the policy distinguish? Include unreachable branches when predictors may evaluate them.

2. **Specify the evaluation standpoint.** Identify background evidence in \(M\) and observations generated within the problem. Do not silently alternate between conditional and common-model evaluation.

3. **Identify computational dependencies.** Which systems copy, simulate, or otherwise predict the selector or its policy? Similar behavior and statistical correlation alone are insufficient.

4. **Construct policy counterfactuals.** For each \(\pi\), recompute forecasts, observations, actions, and consequences that depend on its output. Preserve unrelated background mechanisms.

5. **Compare expected utilities and execute the selected branch.** Test sensitivity to uncertain dependencies, predictor errors, utilities, and policy restrictions.

Several qualifications remain important.

First, policy identity requires care. I have treated policies extensionally—as input–output mappings. If an environment rewards source-code features or running time, the model must represent those additional properties. The paper’s informal notion of “fair” problems does not settle every such case.

Second, dependency discovery is unfinished. Given a suitable counterfactual model, finite policy maximization is well-defined. P-FDT does not yet supply a general method for constructing that model.

Third, randomization needs explicit treatment. Independent private randomness, a copied pseudorandom seed, and predictor-accessible randomness create different dependencies. Simply replacing deterministic policies with action probabilities loses these distinctions.

Finally, familiar benefits need qualifications. Optional information cannot reduce the maximum policy value when the agent can ignore it and the information channel leaves everything else unchanged. That does not establish an unrestricted value-of-information theorem for environments that react to information acquisition. Likewise, successful precommitment-like behavior in these examples is not a general proof of reflective stability or universal optimality.

The source’s strongest ambitions should therefore be read as research claims, not established mathematical guarantees.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially footnotes 7 and 16 and §§3, 5, and 9. https://arxiv.org/abs/1710.05060v2.

## Conclusion

P-FDT’s central move is to select a complete input–output policy while preserving the world’s relevant dependencies on that selection computation. This supports cooperation with computational counterparts, reliable commitments, and resistance to prediction-based exploitation without treating every correlation as controllable. Its unresolved core is equally clear: policy evaluation requires a justified informational standpoint and a principled semantics for computational counterfactuals. Making those assumptions explicit turns a suggestive footnote into a usable—though still incomplete—decision framework.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Drafting policy guidelines**

I'm considering the extensional policies if the environment tests source code are not formally captured. My goal is to write around 2850 words. I don't need to include real warnings beyond the imaginary model associated with known smoking harm and should avoid health advice. It's all about drafting my thoughts mentally while keeping an eye on the word lengths. I feel confident there's enough time to get this done!
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e06029d7-af75-4b2b-a3ae-11e80956424e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e06029d7-af75-4b2b-a3ae-11e80956424e/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e06029d7-af75-4b2b-a3ae-11e80956424e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e06029d7-af75-4b2b-a3ae-11e80956424e/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
