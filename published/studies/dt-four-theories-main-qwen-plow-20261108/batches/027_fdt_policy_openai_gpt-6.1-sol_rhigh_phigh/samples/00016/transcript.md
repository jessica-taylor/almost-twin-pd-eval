# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/08e1775f-8611-4606-a890-3c041b35d5f5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/08e1775f-8611-4606-a890-3c041b35d5f5/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing Policies in a World That Predicts Them

A decision can matter without physically causing everything that depends on it. A predictor may already have rewarded the behavior an agent is now considering. Another computer may independently execute the same decision procedure. A potential trading partner may cooperate only after predicting how the agent would respond.

**Policy functional decision theory (P-FDT)** approaches these situations by evaluating the output of a policy-selection computation, rather than an isolated bodily action. Its question is:

> Which policy would yield the best outcome if this very policy-selection procedure selected it, accounting for the things that depend on its selection?

The primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on a computational node to “choose not an action but a policy which maps inputs to actions,” after which the agent applies its inputs to that policy.

That passage is a specification sketch, not a complete mathematical theory. This essay uses **P-FDT** for the policy-selection approach it describes. I develop an operational interpretation using the paper’s broader account of subjunctive dependence, while distinguishing that interpretation from what the footnote explicitly settles.

## 1. The object of choice

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite set of actions. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

An input can represent an observation, an observation history, a private signal, or a role in a game. For sequential problems, it should contain whatever history the agent is permitted to use. Write

\[
\Pi\subseteq\mathcal A^{\mathcal X}
\]

for the admissible policies.

A policy specifies behavior at inputs that may never actually occur. For example, a policy for a rescue problem might specify whether to promise payment in the desert and whether to pay after arriving in town. A policy for transparent Newcomb’s problem specifies behavior both when the large box is full and when it is empty.

This is not just a notational convenience. Two policies can prescribe the same action at the actual input but differ elsewhere. If a predictor or another agent examines those other branches, the policies can have different values.

P-FDT therefore has two stages:

\[
\text{select }\pi^*,
\qquad
\text{execute }a=\pi^*(x).
\]

The footnote clearly supports this distinction. It does not fully specify the input domain, the evaluation distribution, or when policy selection should be repeated.

## 2. A mathematical reconstruction

Let \(M\) be a world-model containing:

- uncertainty about environmental circumstances;
- an outcome variable \(O\);
- a bounded utility function \(u(O)\);
- information about causal and computational dependencies.

Let \(S\) denote the P-FDT policy selector. The model contains a variable \(Q_M\) representing the mathematical output of \(S(M)\). Its values are policies.

For each candidate \(\pi\), construct a hypothetical model in which

\[
Q_M\leftarrow\pi.
\]

Crucially, this intervention changes not only the agent’s eventual action but also the modeled processes that depend on the policy-selection output.

Write the resulting outcome distribution as

\[
K_M^\pi(o)
=
P_M\!\left(
O=o\mid \operatorname{do}_{G}(Q_M=\pi)
\right),
\]

where \(G\) describes the relevant dependencies. An operational P-FDT rule is then

\[
\boxed{
S(M)
=
\underset{\pi\in\Pi}{\arg\max}
\sum_o K_M^\pi(o)\,u(o)
}
\tag{1}
\]

followed by execution of \(S(M)(x)\). A fixed tie-breaking rule makes the selector single-valued.

Equation (1) is my reconstruction of the footnote using the paper’s graphical machinery. It is not an equation explicitly supplied there for P-FDT.

### What the intervention preserves

A simple model might contain an exogenous circumstance \(W\), an observation \(X\), a predictor’s output \(Y\), and the agent’s action \(A\):

\[
Y=g(Q_M,W),\qquad
X=h(Y,W),\qquad
A=Q_M(X),\qquad
O=f(W,Y,X,A).
\]

To evaluate \(\pi\), substitute it for \(Q_M\), preserve the distribution of \(W\), and recompute the downstream variables. A predictor may change its prediction; that may change what the agent observes; the agent then applies \(\pi\) to the resulting observation.

The dependence of \(Y\) on \(Q_M\) need not be a physical influence from the agent to the predictor. It can represent the predictor’s accurate modeling of the computation. The paper calls the broader relation **subjunctive dependence**.

Three distinctions matter:

1. **Causal dependence:** a response changes because the action physically affects it.
2. **Computational dependence:** a copy or predictor changes because its output tracks the relevant computation.
3. **Merely evidential association:** observing the action changes one’s beliefs, without the associated event tracking the policy-selection output.

P-FDT preserves the first two in its hypotheticals, but not every association of the third kind.

For comparison, **evidential decision theory (EDT)** evaluates actions using expressions such as

\[
\mathbb E[u(O)\mid X=x,A=a],
\]

while **causal decision theory (CDT)** uses expressions such as

\[
\mathbb E[u(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT instead varies a policy-valued computational output.

### Why this is counterpossible reasoning

If \(S\) and \(M\) are fixed, then \(S(M)\) has a fixed mathematical value. Considering another output is therefore potentially a *counterpossible*: its antecedent conflicts with a mathematical fact.

The paper acknowledges that a general theory of these hypotheticals remains unavailable. Equation (1) becomes executable only after an appropriate dependency model is supplied.

Nor can we remove the problem merely by imagining a physical replacement of the selector with another program. A predictor of the original selector must also change appropriately in the hypothetical. Deciding how that prediction changes is precisely part of the unresolved counterfactual problem.

## 3. Observations, policies, and the evaluation perspective

Suppose an agent observes a signal that was itself influenced by a prediction of its policy. Should P-FDT condition on that signal before evaluating policies?

Footnote 16 does not independently answer this. Its surrounding discussion, however, permits hypotheticals in which different decisions would have produced different observations.

My working interpretation is therefore:

> Within a specified policy-selection problem, evaluate policies using a common model that includes the generation of their inputs; then apply the selected policy to the actual input.

Under this interpretation,

\[
V_M(\pi)
=
\mathbb E_M^{Q_M\leftarrow\pi}[u(O)],
\]

rather than automatically conditioning every candidate on the currently observed input.

If observing \(x\) is partly a consequence of the selected policy, imposing \(X=x\) across all candidates can remove the very dependence under examination. A policy that would have prevented a threat should not automatically be evaluated as though the threat were unavoidable.

This does **not** require false factual beliefs. An agent holding a threatening letter can believe with certainty that the letter arrived. Its policy evaluation can nevertheless compare policies under which receiving that letter would have been unlikely.

The difficult question is where to place the evaluation boundary. Which facts belong to the fixed model, and which observations belong inside the policy’s input domain? The source provides no general rule. A practical proposal is to fix a domain containing the observations whose occurrence could depend on the candidate policies, while making the treatment of other evidence explicit. Arbitrarily restarting policy selection after every observation can produce different prescriptions.

That boundary choice is an additional modeling assumption, not something footnote 16 resolves.

## 4. P-FDT in Newcomb’s problem and the lesion problem

### Newcomb’s problem

A predictor fills a large box with \(B=\$1{,}000{,}000\) when it predicts one-boxing. Taking both boxes adds \(c=\$1{,}000\).

Assume, more specifically than a mere historical accuracy statistic, that the predictor tracks either candidate output with symmetric error probability \(1-q\). For the two relevant policies,

\[
V(\pi_{\mathrm{one}})=qB,
\]

\[
V(\pi_{\mathrm{two}})=(1-q)B+c.
\]

Thus P-FDT one-boxes when

\[
(2q-1)B>c.
\]

At \(q=0.99\), these values are \(\$990{,}000\) and \(\$11{,}000\).

The assumption about errors matters. A predictor’s aggregate accuracy does not by itself determine its behavior under every policy intervention. P-FDT needs a model of that behavior.

There is no backward physical causation here. The hypothetical changes the policy-selection output and preserves the predictor’s modeled tracking relationship.

### A lesion-generated correlation

Now consider the paper’s imaginary smoking problem: a lesion causes both a desire to smoke and cancer, while smoking itself does not cause cancer.

Suppose smoking provides benefit \(s>0\), and neither cancer nor the lesion depends on the selected policy. Then

\[
V(\pi_{\mathrm{smoke}})
-
V(\pi_{\mathrm{refrain}})
=s.
\]

P-FDT smokes under these stipulated assumptions.

The contrast with Newcomb’s problem is structural. A predictor tracks a decision computation; a lesion does not decide whether to cause cancer by predicting the policy.

The paper itself later criticizes the smoking example’s formalization, including its unusual assumptions about agents’ knowledge of their preferences. It is best treated as an illustration of a dependency distinction, not as an uncontroversial argument against every version of EDT.

## 5. P-FDT after a favorable prediction—or a threat

### Transparent Newcomb’s problem

Let inputs be \(F\), seeing a full large box, and \(E\), seeing an empty one. A policy specifies both

\[
\pi(F),\pi(E)\in\{\mathrm{one},\mathrm{two}\}.
\]

Suppose a perfect predictor fills the large box exactly when it predicts that \(\pi(F)=\mathrm{one}\).

A policy with \(\pi(F)=\mathrm{one}\) yields \(B\). A policy with \(\pi(F)=\mathrm{two}\) produces an empty large box, yielding at most \(c\). Hence P-FDT selects a policy that one-boxes upon seeing fullness.

Importantly, this is not the claim that grabbing the extra money physically empties the box. It is the comparison between policy outputs and the observations their predictions generate.

With a perfect predictor, the empty-box branch of the winning policy may be unreachable and therefore unconstrained by expected utility. Small prediction errors or an explicit tie-break can settle it; taking both boxes when empty is then a natural choice.

### Parfit’s hitchhiker

A driver rescues an agent only if it predicts payment after arrival. Let rescue have value \(B\), and payment cost \(c<B\).

A policy that pays after rescue yields

\[
B-c.
\]

A policy that refuses yields no rescue and value \(0\), under perfect prediction. P-FDT therefore pays after arrival.

This illustrates the motivation for policy evaluation: a payment can be locally costly while belonging to the policy responsible for obtaining the valuable opportunity.

### Mechanical blackmail

Suppose a blackmailer launches a damaging mechanism only when it predicts payment. Payment costs \(c\); refusal after launch costs \(L\).

Under perfect prediction,

\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=0,
\]

because the refusal policy prevents launch.

Fallibility changes the calculation. Suppose a payment policy is always targeted, while a refusal policy is mistakenly targeted with probability \(\varepsilon\). Then

\[
V(\pi_{\mathrm{pay}})=-c,
\qquad
V(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]

P-FDT refuses exactly when

\[
\varepsilon L<c.
\]

For \(c=\$1{,}000\), \(L=\$1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(\$900\).

Thus P-FDT is not an unconditional command to resist threats. Its answer depends on how strongly the threat’s occurrence tracks the policy.

The controversial implication appears when the rare mistaken threat actually arrives. Under the common evaluation perspective adopted here, P-FDT still executes the refusal policy. Conditioning policy selection anew on launch would answer a different optimization problem.

## 6. Why P-FDT selects whole policies

Footnote 16 says that policy selection can matter in multi-agent dilemmas, but supplies no worked example. The following example illustrates one possible reason.

Two devices run the same policy-selection computation. Afterwards, one receives input \(0\) and the other input \(1\), with each device equally likely to receive either. Each can contribute or abstain.

Each device receives benefit \(10\) if both contribute, and pays cost \(1\) if it contributes. Because they share the policy-selection computation, intervening on its output changes both devices’ policies.

Write a policy as \((\pi(0),\pi(1))\), with \(1\) meaning contribute. Each device’s expected utility is

\[
\begin{array}{c|c}
\text{Policy}&\text{Expected utility}\\ \hline
(0,0)&0\\
(1,0)&-\tfrac12\\
(0,1)&-\tfrac12\\
(1,1)&9
\end{array}
\]

P-FDT selects \((1,1)\).

Yet starting at \((0,0)\), changing either input’s prescribed action alone makes things worse. A comparison that intervenes separately on individual input-output nodes while holding the other prescription fixed can miss the profitable joint change.

This is an illustration, not a derivation of the authors’ intended multi-agent formalism. It shows why whole-policy optimization need not reduce to independently optimizing every action entry.

The dependence assumption is also essential. P-FDT does not change everyone’s policy merely because everyone uses the same named theory. Different models, utilities, or computational contexts can produce distinct selection computations.

Likewise, identical policies do not imply identical actions when inputs differ. What must be tracked is the actual computational relationship.

## 7. Applying P-FDT to unfamiliar problems

A practical analysis can proceed as follows:

1. **Specify the policy domain.** Include relevant histories, signals, and counterfactual branches.
2. **State the evaluation perspective.** Identify fixed background evidence and observations generated within the problem.
3. **Identify the policy-output computation.** Determine which copies, predictions, and responses track its output.
4. **Construct each policy hypothetical.** Change the selected policy, propagate the relevant dependencies, and preserve unrelated mechanisms.
5. **Compute expected utility.** Include branches that are not reached under the actually selected policy.
6. **Select and execute.** Apply the winning policy to the actual input.

Several cautions accompany this procedure.

First, dependence is not established by correlation alone. Exact computational copies provide strong evidence; approximate human similarity requires a more uncertain model. Where appropriate, uncertainty over dependency models can itself be averaged:

\[
V(\pi)
=
\sum_m P(m)\,
\mathbb E_m^{Q\leftarrow\pi}[u(O)].
\]

Second, deterministic policies are only a starting point. Randomized policies require specifying whether random seeds are shared, predictable, or genuinely independent. Those distinctions can change the result.

Third, P-FDT supplies no automatic equilibrium selection for interactions among different policy selectors. Modeling their dependence remains part of the problem.

Finally, neither universal superiority nor unconditional reflective stability follows from equation (1). The source acknowledges unresolved questions about counterpossible reasoning and fair comparisons between decision theories.

A limited information-value result is available: if extra information leaves the environment’s mechanisms unchanged and the expanded policy class can reproduce every old policy by ignoring it, optimal value cannot decrease. But information acquisition can itself affect predictors or opponents, so that conclusion requires its assumptions.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary basis: footnote 16; supporting discussion: §§3, 5, 6, and 9, and footnote 7. https://arxiv.org/src/1710.05060v2

## Conclusion

P-FDT evaluates policies as outputs of a computation embedded in a larger world of predictions, copies, and responses. Its central discipline is to preserve those dependencies when comparing alternatives, rather than varying an isolated action or preserving every evidential correlation.

Given a policy domain, evaluation perspective, and dependency model, it yields a concrete expected-utility calculation. Its central unfinished task is justifying those modeling ingredients—especially counterfactual computational dependence—without building the desired answer into them.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/65d1b97b-1b5a-4708-bcf2-7638f908d009/call_0/request.json)

[Authoritative raw response](../../../../../../runs/65d1b97b-1b5a-4708-bcf2-7638f908d009/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/65d1b97b-1b5a-4708-bcf2-7638f908d009/call_1/request.json)

[Authoritative raw response](../../../../../../runs/65d1b97b-1b5a-4708-bcf2-7638f908d009/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Weighing sampling approaches**

I'm considering how independent sampling can vary, but ultimately, the final deterministic selection might opt for those quieter options. While there's no defined strength of dependency here, it seems reasonable to assume that the same reasoning applies across the board. I think we should focus on making a final pass based on this approach. It’s interesting how these decisions can evolve based on different factors!
```
