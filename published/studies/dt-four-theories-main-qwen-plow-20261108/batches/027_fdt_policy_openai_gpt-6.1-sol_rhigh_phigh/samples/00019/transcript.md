# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00019

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d9e2536d-a5d3-4633-af27-2f4cb698e780/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d9e2536d-a5d3-4633-af27-2f4cb698e780/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies in a World That Predicts You

Decision problems become especially interesting when the environment contains models of the decision-maker. A predictor may reward an anticipated choice; another agent may run the same reasoning; an adversary may issue threats only to agents expected to comply. In such settings, an action’s consequences are not exhausted by what the bodily movement physically causes.

**Policy functional decision theory (P-FDT)** evaluates these situations by treating a policy as the output of a mathematical decision procedure. It asks which output would produce the best outcome, allowing predictions and other relevant implementations of that procedure to vary correspondingly.

The primary source for this account is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on a decision-procedure node “to choose not an action but a policy which maps inputs to actions,” then applying that policy to the agent’s inputs. Footnote 7 similarly identifies policies as mappings from observations to actions.

These passages establish the object of selection, but leave important details unresolved. The mathematical framework below is therefore a reconstruction: the policy-selection commitment comes from the footnotes; the precise evaluation rule and modeling conventions are my proposed operational interpretation, informed by the paper’s broader discussion.

## 1. What P-FDT selects

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Inputs may be observations, private information, or complete observation histories. For sequential problems, history-dependent policies specify an action at every relevant decision point.

Let \(\Pi\subseteq\mathcal A^{\mathcal X}\) be the admissible policy class. Restricting \(\Pi\) can express computational or physical constraints. Initially, however, suppose every mapping is available.

P-FDT has two stages:

1. Select a policy \(\pi^*\).
2. On receiving input \(x\), perform \(\pi^*(x)\).

The second stage uses information normally: different observations can produce different actions. What distinguishes P-FDT is how the first stage evaluates alternative mappings.

Let \(M\) be a reference world-model, including probabilities, utilities, and relevant dependencies. Introduce a variable
\[
S_M
\]
representing the policy output by the P-FDT procedure on model \(M\). This is a representation inside the model, not a physical switch the agent can manipulate.

For each candidate \(\pi\), construct a hypothetical outcome distribution
\[
K_M^\pi(o)
=
P_M\!\left(O=o\mid
\operatorname{do}_{\mathrm{subj}}(S_M=\pi)\right).
\]
The special intervention notation means: suppose the policy-selection procedure outputs \(\pi\), and propagate the changes through all relevant dependencies.

Define
\[
J_M(\pi)=\sum_o K_M^\pi(o)\,U(o).
\]
My proposed P-FDT rule is
\[
\boxed{
\pi^*
=
\operatorname{TB}\!\left(
\arg\max_{\pi\in\Pi}J_M(\pi)
\right),
\qquad
A=\pi^*(X),
}
\]
where \(\operatorname{TB}\) is a specified tie-breaking rule.

This is expected-utility maximization. Its distinctive content lies in the hypothetical distribution \(K_M^\pi\), not in a novel utility function.

There is self-reference: \(M\) represents the output of the procedure evaluating \(M\). Representing an unknown output does not require already knowing it. Nevertheless, this observation does not solve every problem of computational consistency or counterfactual semantics.

## 2. Which dependencies should survive?

For comparison, evidential decision theory (EDT) evaluates an action through ordinary conditioning:
\[
\mathbb E[U(O)\mid X=x,A=a].
\]
Causal decision theory (CDT) instead uses a causal intervention:
\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT, as reconstructed here, intervenes on the policy-selection output rather than conditioning on an action or intervening on one bodily act.

The paper calls the relevant broader relationship **subjunctive dependence**. Two implementations of the same computation should agree, even when neither causally influences the other. Likewise, an accurate predictor’s representation of a computation should track its output. Conversely, an ordinary common-cause correlation need not survive an intervention on the decision procedure.

An operational model might contain
\[
A=\pi(X),\qquad
\widehat\pi=\operatorname{Predict}(S_M,N),
\qquad
O=g(A,\widehat\pi,W),
\]
where \(N\) describes prediction errors and \(W\) other background uncertainty. Under \(S_M=\pi\), the action and prediction are recomputed using these relationships.

More concretely, one can sample background variables, override the equation determining \(S_M\), and evaluate the remaining equations. This supplies \(K_M^\pi\) when the dependency model has a well-defined evaluation.

The crucial question is which relationships belong in that model. A predictor trained to anticipate the agent may track the selected policy. A carcinogenic lesion does not thereby track it. Nor does every agent using the same named decision theory automatically share the same policy: beliefs, objectives, inputs, and implementation can differ.

P-FDT therefore does **not** license the inference, “If I cooperate, everyone cooperates.” It requires a substantive model explaining why particular other decisions vary with this policy-selection output.

The counterfactuals are also not claims about retrocausation. A past prediction can differ between policy hypotheticals without a present action sending a signal backward in time. The comparison concerns different stipulated outputs of a computation and their representations.

Indeed, if the procedure is deterministic, an alternative output on exactly the same arguments may be mathematically impossible. The paper explicitly recognizes this need for **counterpossible reasoning**. Its intervention graphs are a proposed interface for such reasoning, not a completed account of how to derive every logical dependency.

## 3. Information and the reference perspective

The most consequential ambiguity in footnote 16 concerns information. Relative to which evidence should a whole policy be evaluated?

The paper’s displayed action-selection formulation—call it **action-FDT**, to distinguish it from P-FDT—often responds to observations by changing the decision-procedure node being intervened upon, rather than conditioning its entire evaluation on the observation. Its examples allow hypothetical observations to change when the decision output changes.

A natural policy-level interpretation is:

> Represent the possible inputs within a reference model, evaluate complete input-to-action mappings in that model, and then apply the selected mapping to the actual input.

Thus the observed input need not remain fixed across policy hypotheticals. If receiving a threat depends on the predicted policy, then comparing policies can change whether the threat arrives.

This does not mean the agent disbelieves its observations. It distinguishes two questions:

- **Belief:** Given the letter in my hand, what happened?
- **Policy evaluation:** What outcomes correspond to different outputs of the policy-selection procedure, including different chances of receiving a letter?

However, the footnote does not specify a uniquely privileged prior, a universal policy domain, or a rule saying that all evidence must forever remain outside the reference model. Those would be additional commitments.

For applications, I propose making the reference perspective explicit. State which facts are fixed parameters of \(M\), which are variable inputs to \(\pi\), and which may change under policy intervention. In particular, one cannot fix “the threat has arrived” as immutable background while simultaneously claiming that the same comparison captures the policy’s deterrent effect.

This choice matters. Policy selection by itself does not determine whether evaluation is conditional or unconditional. The examples below use a reference model established before the policy-dependent observations are fixed.

## 4. P-FDT in Newcomb’s problem and the lesion problem

In Newcomb’s problem, an opaque box contains \(B\) if a predictor anticipates one-boxing, and zero otherwise. A transparent box contains \(c\). Suppose the predictor tracks either contemplated choice correctly with probability \(q\), symmetrically.

There is no informative input, so policies reduce to constant choices. Under the stipulated subjunctive dependency,
\[
J(\pi_{\mathrm{one}})=qB,
\]
whereas
\[
J(\pi_{\mathrm{two}})=(1-q)B+c.
\]
P-FDT one-boxes exactly when
\[
(2q-1)B>c.
\]
For \(B=1{,}000{,}000\), \(c=1{,}000\), and \(q=0.99\), the respective values are \(990{,}000\) and \(11{,}000\).

The predictor’s past action varies across these hypotheticals because it tracks the decision procedure, not because taking one box physically changes the past.

The assumption about prediction deserves emphasis. A reported historical accuracy of \(99\%\) does not, by itself, identify prediction behavior under every alternative policy. The calculation assumes a particular counterfactual error model. On unfamiliar cases, one must justify that model rather than automatically substitute an observed accuracy percentage.

Now consider the paper’s fictional smoking-lesion problem. Smoking provides benefit \(s>0\), while a lesion causes both a smoking disposition and cancer. Smoking itself does not cause cancer.

If intervening on the relevant policy leaves cancer risk unchanged, then
\[
P(C=1\mid\operatorname{do}_{\mathrm{subj}}(S_M=\pi))
\]
is constant across the smoking and abstention policies. Consequently,
\[
J(\pi_{\mathrm{smoke}})
-
J(\pi_{\mathrm{abstain}})=s>0.
\]
P-FDT prescribes smoking under these stipulated conditions—not under real-world smoking risks.

The contrast is structural: a predictor models the decision; the lesion merely correlates with it. The source also acknowledges difficulties in making the lesion example fully coherent, including questions about agents’ knowledge of their own preferences. Its lesson should therefore concern dependency modeling, not an unqualified verdict against every formulation of EDT.

## 5. P-FDT after revealing observations

### Transparent Newcomb

Suppose both boxes are transparent. The predictor fills the large box exactly when it predicts that the agent would one-box **upon seeing it full**.

Let
\[
\mathcal X=\{F,E\},
\]
representing full and empty. A policy specifies both \(\pi(F)\) and \(\pi(E)\). Assume the same symmetric prediction accuracy \(q\).

Because the filling decision depends only on the full-box response, taking both boxes when empty gains \(c\) without affecting that decision. Thus an optimal policy has
\[
\pi(E)=\mathrm{two}.
\]

The remaining alternatives are
\[
\pi_1(F)=\mathrm{one},
\qquad
\pi_2(F)=\mathrm{two}.
\]
Their values are
\[
J(\pi_1)=qB+(1-q)c,
\]
and
\[
J(\pi_2)=(1-q)(B+c)+qc=(1-q)B+c.
\]
Thus P-FDT selects \(\pi_1\) when
\[
(2q-1)B>qc.
\]
With the previous numbers, the values are \(990{,}010\) and \(11{,}000\).

After seeing a full box, the agent therefore one-boxes. This is not conditional wealth maximization holding the full box fixed. It is execution of the policy selected by a comparison in which box contents depend on the predicted policy.

The same structure explains payment in Parfit’s hitchhiker problem: willingness to pay after rescue is what makes rescue likely beforehand.

### Predictive blackmail

Consider a blackmailer who issues a costly threat only when predicting payment. Let payment cost \(c\), and let damage following refusal cost \(L\).

Under an explicit error model, suppose a paying policy is always threatened, while a refusing policy is mistakenly threatened with probability \(\varepsilon\). Then
\[
J(\pi_{\mathrm{pay}})=-c,
\qquad
J(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT refuses exactly when
\[
\varepsilon L<c.
\]
For \(c=1{,}000\) and \(L=1{,}000{,}000\), the threshold is \(\varepsilon<0.001\).

This calculation captures both deterrence and its limits. P-FDT need not refuse regardless of prediction errors. But under the reference-model interpretation, it may refuse even in the rare case where a mistaken threat actually arrives. The selected policy accepts occasional large losses to avoid more frequent exploitation.

If the threat were issued independently of the policy, the deterrence benefit would disappear. P-FDT is not a general instruction to disregard threats.

## 6. Why P-FDT selects whole policies

Footnote 16 says the policy/action distinction matters in some multi-agent dilemmas, without supplying a worked example. The following is my illustration.

Two agents share the same policy-selection computation and reference model, but receive different role inputs:
\[
x_0=0,\qquad x_1=1.
\]
Their actions are
\[
a_0=\pi(0),\qquad a_1=\pi(1).
\]
Each personally receives the payoff in this table:
\[
\begin{array}{c|cc}
 & a_1=L & a_1=R\\ \hline
a_0=L & 0 & 10\\
a_0=R & 4 & 0
\end{array}
\]

There are four policies. The optimal one is
\[
\pi^*(0)=L,\qquad \pi^*(1)=R,
\]
giving each agent \(10\). Identical policy selection does not imply identical actions: different inputs appropriately produce different outputs.

Now consider the inferior policy
\[
\widetilde\pi(0)=R,\qquad
\widetilde\pi(1)=L,
\]
which yields \(4\). Changing either branch alone reduces the payoff to zero. It is therefore a strict local optimum under coordinate-by-coordinate policy changes, but not under complete policy selection.

This demonstrates a genuine reason to evaluate mappings jointly. A whole-policy intervention can change both role responses together.

It does not prove that every action-FDT implementation must become trapped at the inferior outcome. An action-level model could encode dependencies between its input-specific outputs. Rather, it illustrates why treating those outputs as separately intervenable is an additional substantive assumption—and why the footnote’s choice of intervention target can matter.

The example also identifies a boundary: the shared selector is part of the setup. Merely knowing that two agents both endorse P-FDT is insufficient to infer it.

## 7. Applying P-FDT—and recognizing unresolved cases

A practical analysis can follow five steps.

**First, specify policies and utilities.** List relevant inputs, feasible actions, and complete contingent mappings. Include branches that may not occur under the ultimately selected policy.

**Second, identify the selector.** What computation does \(S_M\) represent? Which copies, simulations, predictions, or future decisions depend on it? Distinguish exact shared computations from approximate behavioral similarity.

**Third, construct alternative-policy models.** For each \(\pi\), override the selector output and propagate its effects through the stipulated dependencies. Ordinary background uncertainty should remain unchanged unless there is a modeled dependency explaining otherwise.

**Fourth, calculate expected utility.** Evaluate \(J_M(\pi)\), including changes in which observations occur and which policy branches execute. Avoid counting only the branch currently observed.

**Fifth, execute the selected policy.** Apply \(\pi^*\) to the actual input.

The difficult work usually lies in steps two and three. Several uncertainties remain.

**Reference-model scope.** The source does not settle how much experience belongs inside the policy’s input space or when a new reference model should replace an old one. Different choices can change prescriptions.

**Dependency discovery.** A graph can encode that a predictor tracks a computation, but the paper does not provide a general algorithm for discovering all such relationships. Sensitivity analysis over plausible dependency models is often more honest than asserting a unique answer.

**Policy representation.** The footnote describes mappings, suggesting extensional policies: identical actions on every input constitute the same policy. If an environment rewards particular source code rather than behavior, implementation details must also be represented.

**Cycles and feasibility.** Arbitrary agents predicting one another may create cyclic equations. An equilibrium-selection or other solution rule is then needed. Likewise, large policy spaces require approximation; exhaustive enumeration is generally infeasible.

Policy selection also supports a qualified value-of-information result. If richer policies include every old policy as a special case that ignores a new signal, and ignoring it preserves the old outcome distribution, then
\[
\max_{\pi\in\Pi_{\mathrm{richer}}}J_M(\pi)
\ge
\max_{\pi\in\Pi_{\mathrm{poorer}}}J_M(\pi).
\]
But this conclusion requires a common evaluation perspective and the stated preservation assumption. It is not a theorem about arbitrary changes in what predictors observe.

Finally, success in these examples does not establish universal optimality. The source itself leaves both logical-counterfactual semantics and a satisfactory general comparison class open.

## Reference

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially footnotes 7 and 16 and Sections 3, 5, and 9. https://arxiv.org/abs/1710.05060v2.

## Conclusion

P-FDT’s central move is to select a complete input-to-action policy while preserving relevant dependencies between that selection, its implementations, and its predictors. It neither preserves every statistical correlation nor restricts attention to physical consequences of the current act.

Given a reference model and well-specified policy counterfactuals, its prescription is straightforward: compare expected utilities and execute the best mapping. The unresolved challenge is specifying those counterfactuals reliably. That challenge is not peripheral; it is where P-FDT’s mathematical foundations and its practical usefulness must ultimately be tested.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Exploring policy examples**

I need to consider multiagent matters by providing a robust example that deals with the same policy under different inputs. I want to highlight specific trade-offs, like pointwise vs. joint decisions, and avoid pitfalls such as impossible coordination or local optimization traps. I'm aiming to show how policy links across various input outputs while addressing the importance of independence, selecting shared criteria, and not relying on a raw, uniform policy.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/11b568f4-11c9-4085-864e-eff36795e445/call_0/request.json)

[Authoritative raw response](../../../../../../runs/11b568f4-11c9-4085-864e-eff36795e445/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/11b568f4-11c9-4085-864e-eff36795e445/call_1/request.json)

[Authoritative raw response](../../../../../../runs/11b568f4-11c9-4085-864e-eff36795e445/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
