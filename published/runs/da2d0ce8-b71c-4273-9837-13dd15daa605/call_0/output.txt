# P-FDT: Choosing the Policy Behind the Action

A decision can matter without physically causing everything that depends on it. A predictor may already have anticipated it; another agent may independently run the same computation; a copy of one’s program may be negotiating elsewhere. Policy functional decision theory—**P-FDT**—evaluates decisions while preserving these computational dependencies, rather than considering only the downstream effects of a bodily action.

Its distinctive object of choice is a **policy**: a mapping from inputs or observation histories to actions. The central question is not simply “What happens if I perform this act?” but “What happens if this policy-selection computation returns this policy?”

The primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes the authors’ preferred formulation as choosing

> “not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.”

The paper calls its theory FDT; **P-FDT** is the name used here for this policy-selection formulation. Most of the paper instead develops an action-output formulation for expositional convenience. Its discussion of dependencies and counterfactuals provides essential background, but footnote 16 does not specify a complete policy-selection algorithm.

Accordingly, this essay distinguishes the source’s commitments from a concrete mathematical reconstruction. The reconstruction makes P-FDT usable in finite examples without pretending that its hardest foundational questions have been solved.

## 1. Policies and a P-FDT Selection Rule

Let \(\mathcal H\) be a finite set of possible observation histories and \(\mathcal A\) a finite action set. A deterministic policy is a function

\[
\pi:\mathcal H\longrightarrow\mathcal A.
\]

Write \(\Pi\subseteq\mathcal A^{\mathcal H}\) for the admissible policies. Histories may include earlier actions, so this representation also accommodates sequential decisions. A policy specifies behavior at histories that never actually occur, not merely at the current history.

Let \(M\) be a world-model containing:

- uncertainty about environmental conditions;
- the agent’s utility function \(u\);
- representations of relevant computations and predictions;
- a specification of how counterfactual changes propagate.

Suppose a fixed selector \(D\), given \(M\), returns a policy. Within \(M\), introduce a variable \(S_M\) representing that output:

\[
S_M=D(M).
\]

P-FDT compares hypothetical outputs of this very selector. Schematically,

\[
\pi^*
=
D(M)
=
\operatorname*{arg\,max}_{\pi\in\Pi}
\mathbb E_M
\left[
u(O)
\;\middle\|\;
\operatorname{do}_{\mathrm{subj}}(S_M=\pi)
\right],
\tag{1}
\]

where \(O\) is the outcome and \(\operatorname{do}_{\mathrm{subj}}\) denotes a **subjunctive intervention**, explained below. A fixed tie-breaking rule makes the selection single-valued.

After receiving actual history \(h\), the agent acts by

\[
a=\pi^*(h).
\tag{2}
\]

The double bar emphasizes that this is not ordinary Bayesian conditioning. Learning that the selector returned \(\pi\) and counterfactually evaluating its returning \(\pi\) are different operations.

Equivalently, define a counterfactual outcome distribution

\[
Q_M^\pi(o)
=
P_M\left(
O=o
\;\middle\|\;
\operatorname{do}_{\mathrm{subj}}(S_M=\pi)
\right).
\]

Then P-FDT maximizes

\[
V_M(\pi)=\sum_o Q_M^\pi(o)u(o).
\tag{3}
\]

Equations (1)–(3) are my reconstruction, not equations stated in footnote 16. Their central feature—the selector returns a whole input-to-action mapping—is directly sourced.

### The evaluation context

One further specification is necessary. My reconstruction uses a fixed evaluation context for a specified decision problem. Observations to which the policy responds are represented *inside* that problem rather than automatically conditioned upon when scoring policies.

Thus the policy-induced distribution of histories can vary between alternatives:

\[
V_M(\pi)
=
\sum_{h,o}Q_M^\pi(h,o)u(o).
\tag{4}
\]

This reading fits the paper’s discussion of counterfactuals in which the agent would have received different evidence. Nevertheless, footnote 16 alone does not determine the evaluation context, its temporal scope, or which background information may legitimately change it. Those remain substantive choices.

## 2. What a Subjunctive Intervention Preserves

P-FDT distinguishes three relationships.

**Causal dependence:** taking medicine changes a later health outcome.

**Computational dependence:** a simulation of the agent’s policy selector returns the same policy, or a predictor forecasts an action by evaluating that policy.

**Statistical association:** a disease correlates with an action because both have a common cause, without the disease responding to the decision computation.

The paper calls the relevant broader relationship **subjunctive dependence**. Its paradigm is two systems computing the same mathematical function. Neither physical output need cause the other, but their outputs are constrained to agree.

A P-FDT hypothetical changes the selector’s output and propagates that change through the dependencies relevant to that output. It does not preserve every observed correlation.

For a simple operational model, suppose

\[
\widehat\pi=R(S_M,N),\qquad
H=g(\widehat\pi,Z),\qquad
A=S_M(H),
\]

and

\[
O=k(A,H,Z),
\]

where \(Z\) describes environmental conditions and \(N\) describes prediction error. Here \(R\) represents an imperfect model of the selected policy.

To evaluate candidate \(\pi\):

1. substitute \(S_M:=\pi\);
2. recompute \(\widehat\pi\);
3. recompute the observation \(H\);
4. take action \(\pi(H)\);
5. calculate the resulting utility.

The distributions of \(Z\) and \(N\) remain fixed unless the model specifies a relevant dependency.

This resembles intervention in a structural causal model, but some arrows represent computational relationships rather than physical causation. A predictor acting yesterday can therefore vary across today’s decision hypotheticals without any claim that today’s action sends a signal backward in time.

It also differs from physically replacing one’s program. The selector remains \(D\); the hypothetical concerns what follows if *that selector* returns another policy. Predictors of \(D\) must be treated consistently with that supposition.

## 3. Why Ordinary Conditioning and Causal Intervention Differ

For comparison, evidential decision theory (**EDT**) typically evaluates an action using

\[
\mathbb E[u(O)\mid H=h,A=a].
\]

Causal decision theory (**CDT**) instead uses something like

\[
\mathbb E[u(O)\mid H=h,\operatorname{do}(A=a)].
\]

EDT asks which action would be favorable evidence. CDT asks which physical action would have favorable causal consequences. P-FDT asks which output of the policy-selection computation has favorable consequences under the relevant subjunctive dependencies.

These distinctions matter in Newcomb’s problem.

### P-FDT in Newcomb’s problem

An opaque box contains \(W=\$1{,}000{,}000\) if a predictor predicted one-boxing, and nothing otherwise. A transparent box contains \(b=\$1{,}000\).

Assume, specifically, that under either candidate policy the predictor matches the resulting choice with probability \(q\). This is stronger than merely knowing its historical average accuracy.

With no informative observation, the relevant policies are constant policies:

\[
\pi_1(h)=\text{one-box},
\qquad
\pi_2(h)=\text{two-box}.
\]

Preserving the predictive dependency gives

\[
V_M(\pi_1)=qW,
\]

and

\[
V_M(\pi_2)=(1-q)W+b.
\]

P-FDT therefore one-boxes when

\[
(2q-1)W>b.
\]

For \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

CDT’s intervention on the final action holds the already-filled box fixed and consequently favors taking the extra thousand. P-FDT’s intervention changes the computation being predicted and therefore changes the predicted box-filling behavior.

### P-FDT in the fictional smoking-lesion problem

Now suppose a lesion causes both a taste for smoking and cancer, while smoking itself has no effect on cancer. Assume smoking provides a utility gain \(s>0\).

If the lesion does not subjunctively depend on the selector’s output, its distribution remains unchanged between policies. Consequently,

\[
V_M(\pi_{\mathrm{smoke}})
-
V_M(\pi_{\mathrm{refrain}})
=s.
\]

P-FDT smokes in this fictional problem. It does not treat an action’s being evidence of disease as a reason to expect the policy intervention to change the disease.

The source itself cautions that the classic lesion example becomes problematic when preferences and self-knowledge are fully specified. Its useful lesson is structural: predictive dependence must not be confused with arbitrary statistical correlation. Nothing here concerns the actual health effects of smoking.

## 4. Why P-FDT Can Let Observations Vary

The most controversial applications concern evidence that earlier actors generated by predicting the policy.

Consider Parfit’s hitchhiker. A driver rescues an agent only if she predicts that the agent will pay \(c\) after arriving in town. Rescue is worth \(W>c\); otherwise utility is zero.

Under perfect prediction, compare policies specifying payment and refusal upon arrival:

\[
V_M(\pi_{\mathrm{pay}})=W-c,
\qquad
V_M(\pi_{\mathrm{refuse}})=0.
\]

P-FDT selects payment. When the agent reaches town, it applies that policy.

Conditioning policy evaluation on arrival would instead remove the rescue from the comparison: either way, the agent would already be safe, and refusal would save \(c\). But arrival is itself partly explained by the predicted policy. The reconstruction in equation (4) retains that dependency.

The same reasoning applies to transparent Newcomb. The predictor fills the large box if it predicts one-boxing *upon seeing it full*. A policy must therefore specify responses to both full and empty boxes. Its response to a full box influences whether that observation occurs.

This is not factual denial. The agent can believe with certainty that it presently sees a full box while evaluating a counterfactual under which its selector’s different output would usually have produced an empty one. Beliefs describe actuality; decision hypotheticals compare alternatives.

### P-FDT and the limits of blackmail resistance

Suppose a blackmailer launches a damaging mechanism whenever it predicts payment. Paying costs \(c\); refusing after launch causes loss \(L\).

Consider the following explicit error model:

- a paying policy is always targeted;
- a refusing policy is mistakenly targeted with probability \(\varepsilon\).

Then

\[
V_M(\pi_{\mathrm{pay}})=-c,
\qquad
V_M(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]

P-FDT refuses precisely when

\[
\varepsilon L<c.
\tag{5}
\]

With \(c=1000\), \(L=1{,}000{,}000\), and \(\varepsilon=0.0009\), refusal loses \(900\) in expectation rather than \(1000\).

Thus resistance is not an unconditional principle. A sufficiently unreliable blackmailer can make payment optimal under this model.

Nor does P-FDT recommend refusal merely because a threat exists. If launching the threat is independent of the selected policy and payment prevents a greater loss, the ordinary causal benefit of payment remains.

## 5. Why the Whole Policy Matters in P-FDT

Footnote 16 says the policy/action distinction matters in some multi-agent dilemmas, although the paper does not develop those differences. The following example is my illustration of the potential importance of policy-level intervention.

Two copies run the same selector on the same model. Each then receives a different role input, \(L\) or \(R\), with either copy equally likely to receive either role. They play a prisoner’s dilemma, with each player’s payoffs

\[
u(C,C)=1{,}000{,}000,\qquad
u(D,D)=1{,}000,
\]

\[
u(D,C)=1{,}001{,}000,\qquad
u(C,D)=0.
\]

The common selector returns

\[
\pi:\{L,R\}\to\{C,D\}.
\]

Under a symmetric, pre-role evaluation context, there are four policies:

| Policy | Resulting action pair | Expected utility for either copy |
|---|---|---:|
| \((C,C)\) | Both cooperate | \(1{,}000{,}000\) |
| \((C,D)\) | One cooperates, one defects | \(500{,}500\) |
| \((D,C)\) | One defects, one cooperates | \(500{,}500\) |
| \((D,D)\) | Both defect | \(1{,}000\) |

Changing the shared selector’s output changes both copies’ policies. P-FDT therefore selects unconditional cooperation.

Notice why bundling matters. Starting from \((D,D)\), changing only the \(L\)-entry to cooperation makes the policy worse; changing only the \(R\)-entry does likewise. Yet changing both entries together is much better.

A pointwise optimization that freezes every other entry can therefore miss the best policy. This is not a claim that the paper’s action-output formulation must freeze those entries: the example isolates precisely the dependency that a complete formalization must settle.

Two qualifications matter. First, the agents maximize their own utility, not an independently imposed group utility. Second, using the same named decision theory does not establish identical policy outputs. Different models, utilities, or selector inputs can break the link. Cooperation requires a warranted account of shared computation, not merely optimism about other agents.

The symmetric evaluation context is also an explicit assumption. Footnote 16 does not resolve every question about asymmetric information or role-specific interests.

## 6. What P-FDT Still Leaves Open

### Counterpossibles and computational identity

A fixed deterministic selector has one output on a given input. Supposing another output may therefore be mathematically impossible.

Ordinary probability theory does not supply the required counterfactuals. Conditioning on \(S_M=\pi\) can be undefined when that event has probability zero, and treating an inconsistent antecedent as implying everything makes evaluation useless.

The source openly identifies this difficulty. My operational interpretation treats candidate outputs as surgical substitutions in a structured model, preserving designated relationships without demanding a fully consistent alternative universe.

That works only when the dependency structure is supplied. Discovering it remains an open problem. Two programs might compute the same policy through different code; conversely, identical code on different inputs can produce different policies. Neither superficial similarity nor a decision-theory label settles computational dependence.

### Policy scope and updating

Does the selector choose a policy for one encounter, an extended interaction, or an entire lifetime? What observations belong inside its policy domain? When may new evidence change its evaluation model?

The footnote does not answer these questions. I favor specifying a bounded decision problem and its evaluation information explicitly, rather than assuming an unexplained lifetime prior.

Within that scope, a policy may perform Bayesian learning. The distinction is between using evidence to guide a selected policy and retrospectively changing its evaluation criterion in a way that discards policy-dependent selection effects. A general rule governing this boundary remains unresolved.

### Randomization, feasibility, and consistency

The finite deterministic formulation assumes all candidate policies are available and evaluable. Real agents face enormous policy spaces:

\[
|\Pi|=|\mathcal A|^{|\mathcal H|}
\]

when every mapping is admissible.

Randomized policies require additional assumptions. Are copies’ random seeds shared? Can predictors anticipate them? Selecting the same randomized policy does not imply identical realized actions.

Likewise, self-reference alone does not guarantee a unique coherent model when predictions interact cyclically. A practical implementation needs well-defined counterfactual distributions, not merely a suggestive self-referential equation.

Finally, the source’s favorable examples do not establish universal optimality. It acknowledges that any theory can be specifically rewarded or punished, and leaves a satisfactory formal characterization of “fair” comparisons open.

## 7. Applying P-FDT to an Unfamiliar Problem

A useful working procedure is:

1. **Specify the policy domain.** Include relevant observations, histories, and off-path contingencies.
2. **State the evaluation context.** Identify which information is fixed and which observations the policy may influence.
3. **Locate the selector variable.** Distinguish its output from physical actions and from other computations.
4. **Model dependencies explicitly.** Include predictors and copies, but do not preserve correlations without justification.
5. **Evaluate complete policies.** Propagate each hypothetical output through the model and maximize expected utility.
6. **Test sensitivity.** Vary prediction errors, uncertain computational links, and unresolved scope assumptions.

If two reasonable dependency models recommend different policies, P-FDT has not yet given a determinate answer. The remaining disagreement concerns the counterfactual model, not expected-utility arithmetic.

One conditional benefit follows immediately: if additional information merely expands the policy domain, while leaving the environment unchanged and allowing the agent to ignore it, optimal policy value cannot decrease. Old policies remain available. This is not an unrestricted claim that every information-producing intervention is beneficial.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passage: footnote 16; supporting discussion: §§3, 5, and 9, and footnotes 7–10. https://arxiv.org/src/1710.05060v2.

## Conclusion

P-FDT selects an input-responsive policy by comparing hypothetical outputs of a fixed policy selector. Its distinctive commitment is to preserve relevant predictive and computational dependencies without preserving mere statistical associations.

Given a policy space, evaluation context, and counterfactual dependency model, the procedure is precise: evaluate whole policies, select the highest-value one, and apply the actual input. Its unfinished work lies chiefly in justifying those models and contexts—the foundations that determine which alternatives the mathematics should compare.