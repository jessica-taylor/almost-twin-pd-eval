# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00007

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/27adf0e0-a76e-4197-805a-d0b58d5b8a19/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/27adf0e0-a76e-4197-805a-d0b58d5b8a19/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies Under Functional Dependence

A decision can matter in more than one way. It can physically change what happens next; it can also be the conclusion of a computation represented elsewhere—in a predictor’s simulation, another agent’s reasoning, or a copy of one’s own program. **Policy functional decision theory (P-FDT)** evaluates decisions while preserving these relevant computational dependencies.

The distinctive object of choice is a **policy**: a mapping from inputs to actions. Rather than asking only what to do after one particular observation, P-FDT asks which response rule would yield the best outcome, accounting for the world’s dependence on that rule.

The primary source is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as choosing “not an action but a policy which maps inputs to actions,” after which the agent applies its inputs to select an action. Footnote 7 likewise identifies policies as mappings from observations to actions. The paper develops an action-selection formulation for ease of exposition and says that the policy distinction matters in some multi-agent dilemmas.

Those remarks identify P-FDT’s central move without fully specifying its mathematics. This essay develops an operational interpretation using the paper’s broader account of functional dependence. Where that requires additional assumptions—especially about observations, policy scope, and counterfactual semantics—I identify them explicitly.

## 1. A mathematical schema for P-FDT

Consider a finite decision problem with:

- an input space \(\mathcal X\);
- an action space \(\mathcal A\);
- an outcome space \(\mathcal O\);
- a utility function \(U:\mathcal O\to\mathbb R\);
- a world-model \(M\).

For now, policies are deterministic functions
\[
\pi:\mathcal X\to\mathcal A,
\qquad
\Pi\subseteq\mathcal A^{\mathcal X}.
\]
An input may encode an observation history, private information, or an agent’s role. For sequential problems, a policy can map each possible history to the next action. Its domain includes inputs that will not actually occur.

Let \(D_M\) be a variable in the world-model representing the policy output by the P-FDT selector operating with model \(M\). This variable must be distinguished from the physical action ultimately performed.

For every candidate \(\pi\), construct a hypothetical outcome distribution
\[
Q_M^\pi(o)
=
\Pr_M\!\left(
O=o\mid \operatorname{Ldo}(D_M=\pi)
\right).
\]
Here \(\operatorname{Ldo}\) denotes a **functional intervention**: hypothetically assigning the selector the policy \(\pi\), then propagating that assignment through the modeled functional and causal dependencies.

P-FDT selects
\[
\boxed{
\pi_M^*\in
\operatorname*{arg\,max}_{\pi\in\Pi}
\sum_{o\in\mathcal O}Q_M^\pi(o)U(o)
}
\]
and, on receiving actual input \(x\), performs
\[
a=\pi_M^*(x).
\]

A fixed tie-breaking rule makes the selector single-valued. Finite spaces ensure that a maximizer exists; infinite policy spaces require further existence and computational assumptions.

This is my policy-level reconstruction, not an equation supplied in footnote 16. It preserves the source’s distinction between **selecting a policy** and **applying an input**.

An equivalent operational representation uses background uncertainty \(W\sim\mu_M\). Under candidate policy \(\pi\), let
\[
X=X_M(\pi,W),\qquad
A=\pi(X),\qquad
O=O_M(\pi,W).
\]
Then
\[
V_M(\pi)
=
\mathbb E_{\mu_M}[U(O_M(\pi,W))].
\]
Crucially, the input itself may depend on the selected policy. A predictor may decide whether to offer a ride, fill a box, or send a threat by predicting how the policy responds.

## 2. Which dependencies should change?

The source calls the relevant relation **subjunctive dependence**. Its clearest examples involve systems implementing the same computation. Two correct calculators evaluating the same expression agree without either calculator causing the other’s answer.

P-FDT therefore distinguishes three relationships:

1. **Causal dependence:** an action changes a later outcome.
2. **Functional dependence:** another process implements, represents, or predicts the relevant computation.
3. **Merely evidential association:** an action provides information about something without the relevant counterfactual dependence.

The first two can warrant changes across P-FDT hypotheticals. The third, by itself, does not.

For comparison, evidential decision theory (EDT) evaluates an action using an ordinary conditional expectation such as
\[
\mathbb E[U(O)\mid X=x,A=a].
\]
Causal decision theory (CDT) instead uses a causal intervention:
\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]
P-FDT intervenes on the **policy-selector output**, allowing both the physical execution and functionally dependent representations to vary.

This is not permission to invent favorable correlations. Another agent’s decision should not change merely because cooperation would be convenient. There must be a modeled reason: shared computation, an accurate simulation, or some other justified dependence.

Nor does sharing the name “P-FDT” establish identical policies. Different utilities, models, or computational limitations may yield different selectors. Even identical policies can produce different actions when supplied different inputs.

A practical model can represent dependencies through structural equations or prediction kernels. For example,
\[
\Pr(\widehat\pi=\rho\mid\operatorname{Ldo}(D_M=\pi))
=
K_M(\rho\mid\pi)
\]
specifies how a predictor’s representation responds under each candidate policy.

The kernel is substantive information. A predictor’s historical accuracy alone generally does not determine it: population-level accuracy need not equal accuracy under every counterfactual policy.

## 3. Why the intervention is counterpossible

A fixed deterministic selector with fixed inputs has only one mathematical output. If it selects \(\pi_1\), supposing that this very selector selects \(\pi_2\) can contradict a mathematical fact.

The source explicitly acknowledges this difficulty for functional interventions. P-FDT inherits it at the policy level.

Accordingly, \(Q_M^\pi\) should not be understood as an ordinary conditional distribution over logically possible worlds. It is a decision-evaluation construction: temporarily override the selector-output equation while preserving specified dependencies elsewhere.

In a tractable graphical model, one might:

1. identify the node representing the policy output;
2. replace its defining equation with \(D_M:=\pi\);
3. propagate the change through linked representations and physical consequences;
4. leave unrelated background mechanisms unchanged.

This describes a modeling procedure, not a completed theory of logical counterfactuals. Cyclic dependencies, approximate simulations, and uncertain computational equivalences require further machinery.

Simply imagining that the agent physically installs a different algorithm does not remove the problem. A predictor may be predicting the actual selector. If that selector hypothetically returns another policy, the predictor’s representation of **that selector** must respond accordingly.

Self-reference also remains: \(D_M\) represents the output of the very procedure evaluating these alternatives. Representing such a computation is possible in principle, but that alone does not establish that every proposed counterfactual model is coherent or computationally manageable.

## 4. P-FDT in Newcomb’s problem and the smoking lesion

In Newcomb’s problem, an opaque box contains \(B\) dollars if a predictor predicts one-boxing and nothing otherwise. A transparent box always contains \(k\) dollars.

With no informative input at execution, the relevant policies are constant: always one-box or always two-box. Assume a symmetric prediction mechanism with accuracy \(r\) under either policy. Then
\[
V(\pi_{\mathrm{one}})=rB,
\]
whereas
\[
V(\pi_{\mathrm{two}})=(1-r)B+k.
\]
Thus P-FDT one-boxes exactly when
\[
(2r-1)B>k.
\]
For \(r=0.99\), \(B=1{,}000{,}000\), and \(k=1{,}000\), the values are \(990{,}000\) and \(11{,}000\).

The predictor’s past behavior changes **in the hypothetical model** because its prediction depends on the computation being evaluated. P-FDT does not posit a physical signal traveling backward in time.

Now consider the source’s imaginary smoking-lesion setting. Smoking provides benefit \(b>0\), but a lesion causes both a tendency to smoke and cancer. Smoking itself does not cause cancer.

Under the stipulated dependency model, changing the selected smoking policy does not change the lesion or cancer mechanism. Consequently,
\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=b.
\]
P-FDT smokes in this artificial setting.

The distinction is structural: a predictor responds to a representation of the decision; a lesion does not. The source nevertheless cautions that fully specifying the smoking example introduces difficulties concerning preferences, self-knowledge, and population correlations. It should illustrate the dependency distinction, not serve as an uncontested refutation of every version of EDT.

## 5. Observations: selecting a response rule without freezing its input

The most consequential interpretive question concerns information.

Suppose the agent has observed \(x\). Should it optimize a policy using a distribution already conditioned on \(X=x\)? Or should it evaluate complete policies against a reference model in which alternative policies may generate different observations?

Footnote 16 alone does not settle every aspect of this choice. The surrounding discussion strongly favors allowing observations to vary when they depend on the decision computation. I therefore adopt the following interpretation:

> Fix a reference model for the decision problem, optimize the complete policy relative to that model, and use the actual observation to determine which policy entry is executed.

This is not a requirement to ignore evidence in factual reasoning. An agent can believe with certainty that it has received a letter while evaluating a refusal policy under which such letters are rarely sent.

Consider Parfit’s hitchhiker with a perfect predictor. A driver rescues a stranded agent exactly when predicting that the agent will pay \(c\) after arriving. Survival is worth \(V>c\). The policy “pay if rescued” yields
\[
V-c,
\]
while “refuse if rescued” yields \(0\). P-FDT selects the paying policy and executes it in the city. Reoptimizing only conditional on already being rescued would erase the dependency that made rescue available.

Transparent Newcomb illustrates the same structure. Let the inputs be “full” and “empty.” Assume the predictor fills the large box according to its prediction of \(\pi(\mathrm{full})\), with symmetric accuracy \(r\).

Compare
\[
\pi_1(\mathrm{full})=\mathrm{one},
\qquad
\pi_1(\mathrm{empty})=\mathrm{two},
\]
with a policy \(\pi_2\) that always takes both boxes. Their values are
\[
V(\pi_1)=rB+(1-r)k,
\]
\[
V(\pi_2)=(1-r)B+k.
\]
When the first value is larger, P-FDT leaves the small box behind upon seeing the large box full.

The policy is sensitive to information: it behaves differently on different inputs. What it avoids is evaluating each input as though its occurrence were independent of the response rule.

## 6. P-FDT and fallible blackmail

Policy evaluation makes refusal of predictable extortion intelligible without making refusal absolute.

Suppose a blackmailer attacks anyone predicted to pay. Payment costs \(c\); refusal after an attack causes loss \(L\). Assume:

- a paying policy is attacked with probability \(1\);
- a refusing policy is attacked mistakenly with probability \(\varepsilon\);
- no attack means no loss.

Then
\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT refuses precisely when
\[
\varepsilon L<c.
\]

For \(c=1{,}000\), \(L=1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(900\), versus \(1{,}000\) for payment.

If an attack actually occurs, refusal is locally costly. Nevertheless, P-FDT executes the policy whose predictable availability produces the better overall distribution.

The assumptions matter enormously. If the attack is independent of the policy, refusing does not deter it. If prediction errors are sufficiently frequent or the threatened loss sufficiently large, payment can maximize policy value. P-FDT does not supply an unconditional principle of defiance.

## 7. Why whole policies matter in multi-agent problems

The policy formulation can link choices made on **different inputs**, rather than only identical decision instances.

Consider two agents implementing the same policy selector with the same model and a common payoff. One receives role \(L\), the other role \(R\). Each chooses action \(0\) or \(1\), with payoff
\[
\begin{array}{c|cc}
 & A_R=0 & A_R=1\\ \hline
A_L=0 & 0 & 10\\
A_L=1 & 6 & 0
\end{array}.
\]

Assume their shared logical selector outputs one policy
\[
\pi:\{L,R\}\to\{0,1\}.
\]
Policy-level intervention changes the rule implemented by both agents. P-FDT selects
\[
\pi^*(L)=0,\qquad \pi^*(R)=1,
\]
yielding payoff \(10\).

Now consider the inferior policy
\[
\pi^{-}(L)=1,\qquad \pi^{-}(R)=0,
\]
yielding \(6\). Changing either entry alone produces payoff \(0\). An input-by-input optimization that holds the other entry fixed can therefore regard this inferior policy as locally optimal. Whole-policy comparison escapes that restriction.

This is my illustrative construction, not a dilemma analyzed in the source. It demonstrates why footnote 16’s choice of intervention target matters. An action-selection formulation equipped with suitable cross-input dependencies might reach the same result; the claim is not that every such formulation must fail.

The example also separates **sharing a policy** from **taking the same action**. Here the optimal shared rule deliberately prescribes different actions for different roles.

For agents with different objectives, no common-payoff maximization is automatically justified. One must model each selector, its utilities, and its dependence on the others. P-FDT is not simply a prescription to maximize collective welfare.

## 8. Applying P-FDT to unfamiliar cases

A useful working procedure is:

**Specify the policy domain.** Identify the inputs the rule can receive and the actions available at each input. Include relevant unrealized contingencies.

**Specify utility and background uncertainty.** Distinguish utility from money, and physical uncertainty from uncertainty about computations.

**Identify the intervention target.** Name the policy-selector output and determine which copies, predictions, or representations depend on it. Do not link agents merely because they use similar vocabulary.

**Construct each policy hypothetical.** Propagate the candidate policy through justified dependencies, allowing observations to vary where appropriate.

**Compare expected utilities and execute.** Select the best policy, then apply the actual input.

The difficult work lies in constructing the hypotheticals, not in the final maximization. Several questions remain open.

First, **which reference model should be used?** The source does not specify a universally privileged prior, a lifetime commitment point, or a general rule for incorporating new evidence into policy evaluation. Arbitrarily choosing a favorable reference distribution after observing an outcome would undermine the procedure.

Second, **how broad is the policy?** It might cover one experiment, an extended interaction, or many related decisions. A broader domain creates additional dependencies and computational demands. Footnote 16 does not prescribe unlimited lifetime optimization.

Third, **what counts as the same policy?** Treating policies extensionally—as input-output mappings—is natural here. Environments that inspect source code or computational cost may require richer objects.

Fourth, **how is randomization represented?** A randomized policy can map inputs to action distributions, but whether random draws are private, shared, predictable, or copied changes the resulting dependencies.

Finally, no universal optimality theorem follows from the examples. The source acknowledges that a satisfactory account of functional dependence and a principled comparison class of decision problems remain unfinished.

A limited information-value argument is available: if new information leaves the environment unchanged and the enlarged policy space contains every old policy, the agent can always ignore it. But when information acquisition itself changes predictions or incentives, those effects must also be modeled.

**Reference:** Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially footnotes 7 and 16 and §§3, 5, and 9.

## Conclusion

P-FDT evaluates complete response rules by hypothetically varying the output of the policy selector while preserving relevant functional and causal dependencies. It then executes the selected rule on the actual input.

Its central insight is that a policy can help determine the situation in which it is applied. That makes prediction, coordination, and deterrence part of decision evaluation—not merely background facts. Its central unresolved task is equally clear: specifying, rather than merely intuiting, which dependencies those policy counterfactuals should preserve.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Planning a math draft**

I’m writing a final piece of around 2850 words but want to aim for a more natural 2750. I’ll break down the sections: the opening can be about 200 words, the first section about math around 430, with various subsections like examples, observations, and limits. I'm also considering some policy arguments in relation to causal decision theory and algorithm predictions. It's essential I organize everything clearly without overlooking key observations or evidence from policy implementations.**Understanding evidence and policy**

I’m thinking about how to handle evidence that’s independent of policy. I can condition something μ on the evidence E, especially if it stays the same under different interventions. It's noted that we should absorb evidence that isn’t causally or logically affected. However, I need to be careful of stochastic noise in evidence, as it can expose errors based on the actual policy. So, I shouldn’t claim invariance too confidently; there's nuance here.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7ca5b3be-0f3c-4135-898a-ae73e6310a56/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7ca5b3be-0f3c-4135-898a-ae73e6310a56/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Considering model settings**

I'm analyzing an essay that discusses how sharing model settings doesn’t establish identical selectors when different private knowledge models are involved. It seems like the use of a policy selector effectively captures the inputs. The entire task appears symmetric even with different labels, and actual evidence policies are included in both cases, leading to an optimal outcome in the final pass. There's a lot to think through about optimizing how we handle these settings!
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7ca5b3be-0f3c-4135-898a-ae73e6310a56/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7ca5b3be-0f3c-4135-898a-ae73e6310a56/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
