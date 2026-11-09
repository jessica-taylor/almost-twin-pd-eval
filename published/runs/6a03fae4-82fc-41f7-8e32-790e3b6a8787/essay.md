# P-FDT: Choosing Policies Through Functional Counterfactuals

A decision can matter in ways that its immediate physical consequences do not capture. A predictor may have anticipated it; another computer may execute the same calculation; a negotiating partner may respond to a model of how the decision-maker would behave. **Policy functional decision theory (P-FDT)** evaluates choices while preserving these dependencies.

Its distinctive proposal is to select not merely an action, but a **policy**: a mapping from inputs to actions. The agent then applies that policy to its actual input.

The primary source is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as intervening on a node representing the decision function “to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action.” Footnote 7 similarly describes iterating over policies rather than actions.

These passages specify an important architecture, but not a complete theory. They leave open the policy’s domain, the evaluation distribution, and the construction of functional counterfactuals. This essay develops one operational interpretation, drawing on the paper’s broader discussion while distinguishing that interpretation from what the footnote explicitly establishes.

## 1. From actions to policies

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite action set. A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Inputs might include observations, private signals, an agent’s role, or an entire observation history. In a sequential problem, a policy specifies an action at every relevant history, including histories that will not actually occur.

Write
\[
\Pi\subseteq\mathcal A^{\mathcal X}
\]
for the admissible policies. Restrictions on \(\Pi\) can represent computational limitations or unavailable actions. Fix an outcome space \(\mathcal O\) and a bounded utility function
\[
U:\mathcal O\longrightarrow\mathbb R.
\]

The basic P-FDT architecture is
\[
\pi^*=S(M),\qquad a^*=\pi^*(x),
\]
where \(M\) is a background model, \(S\) is the policy-selection procedure, and \(x\) is the actual input.

For tractability, I interpret \(M\) as specifying a fixed decision problem, with varying observations represented inside \(\mathcal X\). Footnote 16 does not uniquely prescribe this division between background model and policy input. Nevertheless, it makes the two stages explicit: first select an input-sensitive response rule; then evaluate it at the observed input.

The difficult question is how to score candidate policies.

An ordinary causal policy optimizer might ask what would happen if the agent physically installed different software. P-FDT instead asks:

> What would the relevant world look like if this very policy-selection computation returned \(\pi\)?

The distinction matters when another system predicts the original computation. Merely imagining different software in the agent’s body need not change a prediction of its original software. P-FDT’s counterfactual must reach the represented computation and its relevant predictors.

Let \(\boldsymbol{\Pi}\) be a variable in \(M\) representing the output of \(S(M)\). Introduce a functional intervention notation
\[
[\boldsymbol{\Pi}\leftarrow\pi].
\]
This changes the represented selector output and propagates the change through the model’s specified functional dependencies.

A natural mathematical reconstruction is
\[
J_M(\pi)
=
\sum_{o\in\mathcal O}
Q_M\bigl(o;[\boldsymbol{\Pi}\leftarrow\pi]\bigr)U(o),
\]
followed by
\[
\boxed{
S(M)=\operatorname*{arg\,max}_{\pi\in\Pi}J_M(\pi),
\qquad
a^*=S(M)(x).
}
\]
A fixed tie-breaking rule makes the selector single-valued.

This is my proposed policy-level formalization, not an equation supplied in footnote 16. Its shape follows the paper’s expected-utility framework; its intervention target follows the footnote.

## 2. Which dependencies survive?

P-FDT requires more than a joint probability distribution. It needs an account of what the world depends on **subjunctively**: what would vary together under the relevant hypothetical change.

The paper distinguishes three relationships.

**Causal dependence.** If an agent presses a switch, a lamp turns on. Changing the policy’s prescribed action changes the lamp through ordinary physical causation.

**Computational or predictive dependence.** Two computers may execute the same calculation without communicating. A predictor may model the agent’s selector. Their outputs can track the policy-selection computation without being caused by its later physical execution.

**Merely evidential association.** A background condition may correlate with behavior without responding to the computation’s output. Changing that output should not automatically change the condition.

For comparison, standard evidential decision theory evaluates actions using quantities such as
\[
\mathbb E[U\mid X=x,A=a],
\]
whereas causal decision theory uses causal interventions:
\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]
P-FDT evaluates an entire policy through a functional intervention. It neither preserves every observed correlation nor restricts variation to the physical consequences of one action.

One implementation uses structural equations. Let \(W\) collect exogenous uncertainties with distribution \(\mu\). Under a candidate selector output, compute
\[
X_\pi=h(\pi,W),\qquad
A_\pi=\pi(X_\pi),\qquad
O_\pi=g(\pi,X_\pi,A_\pi,W).
\]
Then
\[
J_M(\pi)=\mathbb E_\mu[U(O_\pi)].
\]
Dependence on \(\pi\) inside \(h\) or \(g\) can represent a predictor, another implementation of the selected policy, or ordinary downstream effects. Variables without such dependence remain unchanged.

This representation is useful, but it does not solve the central modeling problem: determining which dependencies belong in the equations.

Shared membership in the category “rational agent” is insufficient. Two agents with different information, preferences, or algorithms need not return the same policy. Even identical policies can produce different actions on different inputs. P-FDT must track specific computational relationships, not assume universal cooperation.

## 3. Counterpossibilities and observations

The selector \(S\) is a fixed mathematical function. On fixed input \(M\), it has one output. Consequently, considering other outputs can involve **counterpossible** antecedents: hypotheses inconsistent with the computation’s actual mathematical behavior.

The source explicitly accepts this difficulty. Its broader functional-decision framework treats hypotheticals as tools for evaluating decisions, not necessarily as logically possible worlds.

Operationally, one can replace the modeled equation for \(\boldsymbol{\Pi}\) by a candidate policy and recompute specified dependents. This avoids treating an inconsistent antecedent as licensing arbitrary conclusions. But the justification for a particular replacement-and-propagation rule remains incomplete. The paper identifies the construction of subjunctive-dependency models as a major open problem.

Observations create another important issue. In the interpretation developed here, the score is generally **not**
\[
\mathbb E[U(O_\pi)\mid X_\pi=x].
\]
The observation \(x\) determines which policy entry is executed. It need not constrain every candidate-policy hypothetical to reproduce that observation.

Why? Because receiving the observation may itself depend on the selected policy. A blackmailer might send a demand only after predicting compliance. Holding receipt fixed while comparing policies would discard the very dependency that P-FDT is intended to preserve.

This does not mean observations are false or irrelevant. The actual action remains \(\pi^*(x)\), and the policy can respond differently to different inputs. It means that factual belief and decision evaluation play different roles.

I adopt this evaluation perspective because it fits the paper’s transparent-box and blackmail discussions. Footnote 16 alone, however, does not establish a unique rule for choosing the background distribution or deciding which discoveries should revise \(M\). P-FDT should not be equated without qualification with ignoring all subsequent evidence or optimizing from an arbitrarily remote prior.

## 4. P-FDT in Newcomb’s problem

Suppose an opaque box contains \(V=\$1{,}000{,}000\) if a predictor anticipated one-boxing, and nothing otherwise. A transparent box contains \(c=\$1{,}000\).

Assume a symmetric prediction channel: under either candidate output, the predictor matches the prescribed action with probability \(r=0.99\). This is stronger than merely knowing that its historical accuracy was \(99\%\); the counterfactual error model must be specified.

With only one relevant input, policies reduce to constant action prescriptions. Their values are
\[
J(\pi_{\mathrm{one}})=rV,
\]
and
\[
J(\pi_{\mathrm{two}})=(1-r)V+c.
\]
Thus
\[
J(\pi_{\mathrm{one}})=\$990{,}000,\qquad
J(\pi_{\mathrm{two}})=\$11{,}000.
\]
P-FDT one-boxes whenever
\[
(2r-1)V>c.
\]

There is no claim that taking one box sends a physical signal backward in time. Rather, both the eventual action and the earlier prediction depend on the computation being evaluated. The hypothetical variation follows that shared dependence.

Contrast the imaginary smoking-lesion problem. Suppose a lesion produces both cancer and a tendency to smoke, but smoking itself does not cause cancer. If smoking provides utility \(b>0\), and neither lesion nor cancer depends subjunctively on the policy output, then
\[
J(\pi_{\mathrm{smoke}})
-
J(\pi_{\mathrm{refrain}})
=b.
\]
P-FDT smokes in this stipulated world.

The source later emphasizes complications in making the lesion example coherent, including uncertainty about preferences and whether the assumed behavioral correlations survive accurate self-modeling. The robust lesson is the distinction between prediction and common-cause association—not that every informal lesion story determines a unique model.

## 5. P-FDT in transparent Newcomb and the hitchhiker problem

Now both boxes are transparent. Let the input be
\[
X\in\{\mathrm{full},\mathrm{empty}\}.
\]
The predictor fills the large box according to its prediction of what the agent would do **upon seeing it full**.

Compare two policies:
\[
\pi_G(\mathrm{full})=\mathrm{one},\qquad
\pi_G(\mathrm{empty})=\mathrm{two},
\]
and
\[
\pi_T(\mathrm{full})=\pi_T(\mathrm{empty})=\mathrm{two}.
\]
Under the same symmetric error model,
\[
J(\pi_G)=rV+(1-r)c,
\]
while
\[
J(\pi_T)=(1-r)V+c.
\]
The empty-box prescription takes the available \(c\), since this entry does not influence the predictor’s stipulated filling rule.

At \(r=0.99\),
\[
J(\pi_G)=\$990{,}010,\qquad
J(\pi_T)=\$11{,}000.
\]
P-FDT therefore selects \(\pi_G\). If it sees a full box, it takes only that box.

The controversial step is deliberate: when evaluating \(\pi_T\), P-FDT does not insist that the box remain visibly full. Under that alternative policy, the predictor would usually have left it empty.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded traveler only if she predicts that the traveler will later pay \(c\). With perfect prediction and rescue worth \(V>c\), the policy “pay after rescue” yields
\[
V-c,
\]
whereas “refuse after rescue” yields no rescue and utility \(0\), using death as the baseline.

P-FDT selects the paying policy and executes its payment entry after arriving safely. This is not a separate moral principle about gratitude. It follows from evaluating the response rule together with the rescue that predictively depends on it.

## 6. P-FDT and fallible blackmail

Policy evaluation does not always favor honoring demands. It favors whatever response rule performs best in the modeled dependency structure.

Suppose a blackmailer attacks agents predicted to pay \(c\). Paying prevents damage \(L\). Assume:
- a paying policy is attacked with probability \(1\);
- a refusing policy is mistakenly attacked with probability \(\varepsilon>0\).

Relative to an unattacked baseline,
\[
J(\pi_{\mathrm{pay}})=-c,
\qquad
J(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]
P-FDT refuses precisely when
\[
\varepsilon L<c.
\]

For \(L=\$1{,}000{,}000\), \(c=\$1{,}000\), and \(\varepsilon=0.0009\), refusal has expected loss \(\$900\), versus \(\$1{,}000\) for payment.

On the rare occasion when the refusing agent receives a demand, it still executes refusal. It knows an error occurred, but the selected policy was evaluated across the attack process that depends on that policy.

This is the sharpest philosophical cost of the interpretation: the actual rare encounter can go badly because the globally evaluated response rule performs better overall. A critic may reject that evaluation perspective; P-FDT’s defender argues that predictable willingness to make exceptions recreates the incentive to attack.

The conclusion is model-sensitive. If attack is independent of the response policy, then both policies face the same threat, and paying can be optimal when \(c<L\). P-FDT does not prescribe unconditional resistance to every extortion attempt.

## 7. Why whole-policy selection matters

Footnote 16 says the distinction between policy selection and the paper’s action-selection formulation matters in some multi-agent dilemmas. It does not supply a worked example. The following construction illustrates the motivation.

Two agents share one policy-selection computation and a common payoff. They receive different role inputs, \(0\) and \(1\), and implement
\[
A_0=\pi(0),\qquad A_1=\pi(1).
\]
Their payoff is
\[
U(A_0,A_1)=
\begin{cases}
2,&(A_0,A_1)=(C,C),\\
1,&(A_0,A_1)=(D,D),\\
0,&A_0\ne A_1.
\end{cases}
\]

Changing either entry alone from the policy \((D,D)\) reduces payoff from \(1\) to \(0\). Changing the entire policy to \((C,C)\) raises payoff to \(2\). Whole-policy selection can therefore identify coordinated improvements that isolated, entry-by-entry optimization misses.

This is not a proof that every action-selection functional model fails: a sufficiently rich dependency model might already link the relevant action computations. It illustrates why the intervention target must be specified rather than treated as an inconsequential notational choice.

Nor does shared selection imply identical actions. If the payoff instead rewards complementary actions, an optimal shared policy can satisfy
\[
\pi(0)=C,\qquad \pi(1)=D.
\]
The shared object is a response rule, not necessarily its output at different inputs.

In the paper’s psychological-twin prisoner’s dilemma, the twins have the same relevant input. Preserving their computational agreement compares mutual cooperation with mutual defection, yielding \(\$1{,}000{,}000\) versus \(\$1{,}000\). That argument does not automatically extend to an unrelated opponent whose choice is independent of the selected policy.

## 8. Applying P-FDT to unfamiliar problems

A useful procedure is:

1. **Define the policy domain.** Specify inputs, actions, and prescriptions at unrealized histories.
2. **Identify the represented computation.** Determine which selectors, copies, simulations, and predictors depend on its output.
3. **Construct each policy hypothetical.** Propagate causal and computational consequences, without preserving associations merely because they are observed.
4. **Evaluate total expected utility.** Allow the policy to change which observations and encounters occur.
5. **Execute the selected policy at the actual input.**

The most important work occurs before maximization. A claimed predictor’s overall accuracy does not determine its response to every candidate policy. Similar agents need not be identical computations. A policy-dependent observation cannot automatically be held fixed.

Several further choices remain unresolved by the source. **Policy scope** determines which decisions are optimized jointly. **Randomization** requires distinguishing a distribution over policies from policies that use private random inputs; predictors may track those differently. **Computational costs** may require restricting the policy class or representing implementation details, rather than treating every extensionally specified mapping as equally available.

Some attractive properties are conditional. If information merely expands the available response rules while leaving the environment unchanged, an agent can retain its old policy and ignore the signal. Hence additional information cannot reduce the maximum attainable value. But publicly acquiring information might alter predictors or commitment opportunities, changing the environment itself.

Likewise, the paper argues for reflective stability and strong performance in “fair” problems, but explicitly leaves general optimality and fairness unresolved. P-FDT is not accompanied by a theorem that it outperforms every rival in every environment.

### Reference

Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passages: footnotes 7 and 16; supporting discussion: §§3, 5–6, and 9–10. https://arxiv.org/abs/1710.05060v2

## Conclusion

P-FDT evaluates complete input-to-action policies by varying the represented output of the policy-selection computation and preserving relevant functional dependencies. It then applies the selected policy to the actual input. This explains both its sensitivity to predictors and its willingness to execute costly prescriptions after their benefits have already arrived.

Its unresolved core is not expected-utility maximization, but counterfactual modeling: deciding exactly what should vary together. Once that structure and the policy’s scope are specified, P-FDT becomes a concrete calculation. Without them, its compelling examples remain guidance rather than a complete algorithm.