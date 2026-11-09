# P-FDT: Choosing the Policy Your Decision Procedure Should Output

A decision can matter without physically causing everything that depends on it. A predictor may have anticipated it yesterday; another computer may be running the same calculation elsewhere; a future interaction may depend on what someone expects you to do. **Policy functional decision theory (P-FDT)** evaluates choices while preserving such dependencies—not merely their causal consequences, but not every statistical correlation either.

The primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as choosing “not an action but a *policy* which maps inputs to actions,” after which the agent applies that policy to her inputs. Footnote 7 similarly describes policies as mappings from observations to actions.

These passages identify the object of choice but do not supply a complete mathematical theory of policy selection. The paper’s main equations instead select individual outputs for particular inputs. This essay develops an operational interpretation of the policy-selection passage, using the paper’s broader account of functional dependencies. Where additional assumptions are needed, I identify them explicitly.

## 1. Policies and the P-FDT selection rule

Let \(\mathcal X\) be a finite set of possible inputs and \(\mathcal A\) a finite set of actions. A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
Inputs may be observations or, in a sequential problem, complete observation-and-action histories. Let
\[
\Pi\subseteq\mathcal A^{\mathcal X}
\]
be the admissible policy set. Restrictions on \(\Pi\) can express computational limitations or constraints on available actions.

An agent has a world-model \(M\), containing uncertainty about the environment, a utility function \(u:\mathcal O\to\mathbb R\), and information about relevant dependencies. Assume bounded utility for simplicity.

The distinctive ingredient is a model variable \(K\) representing the **policy-valued output of the agent’s fixed policy-selection procedure**. For each candidate \(\pi\), construct a hypothetical outcome distribution
\[
Q_M^\pi(o)
=
P_M\!\left(o\mid\operatorname{sdo}(K=\pi)\right).
\]
Here \(\operatorname{sdo}\) denotes a *subjunctive intervention*: a hypothetical change propagated through the dependencies relevant to P-FDT. This notation is mine, not an operator formally defined in the source.

The resulting rule is
\[
\pi_M^*
\in
\operatorname*{arg\,max}_{\pi\in\Pi}
V_M(\pi),
\qquad
V_M(\pi)
=
\sum_o Q_M^\pi(o)\,u(o).
\]
On receiving actual input \(x\), the agent executes
\[
a=\pi_M^*(x).
\]
A fixed tie-breaking rule makes this single-valued when necessary.

This reconstruction makes two substantive choices. First, the intervention concerns the selector’s policy-valued output, rather than one entry \(\pi(x)\). Second, candidate policies are evaluated from a common reference model \(M\). The footnote motivates the first choice but does not fully specify the second; evidence management will therefore require separate discussion.

Crucially, this is not simply the question, “What if someone physically installed this alternative program?” A predictor might be predicting the actual selection procedure, not the candidate program considered in isolation. P-FDT asks what would follow **if this very selector returned \(\pi\)**, including corresponding changes in representations of that selector.

## 2. Which dependencies should change?

The paper calls the relevant relationship **subjunctive dependence**. Its paradigmatic example is two reliable computers performing the same calculation. Their answers agree because of what they compute, even without communication between them.

For P-FDT, this suggests three distinctions.

**Causal consequences propagate.** If the selected policy makes the agent buy a ticket, the resulting payment and travel opportunities belong in its evaluation.

**Computational counterparts change together where the model warrants it.** If another system accurately predicts the selected policy, its prediction should change when the policy output is hypothetically changed. Exact copies sharing a selector may likewise implement the same alternative policy.

**Mere correlations need not persist.** If a medical condition independently causes both a behavioral tendency and an illness, changing the selector’s output does not thereby remove the condition.

One operational representation uses structural equations. Suppose the model contains background uncertainty \(W\) and variables satisfying
\[
Z_i=f_i(\operatorname{Parents}_i,W).
\]
Constructing a policy hypothetical replaces the equation determining \(K\) with \(K=\pi\), then recomputes dependent variables. Unlike an ordinary causal model, however, some arrows represent computational or predictive dependence rather than physical influence.

This construction is useful only when those dependencies have been justified. Identical software with different inputs need not take identical actions:
\[
\pi(x)\neq\pi(y)
\]
is entirely compatible with sharing a policy. Conversely, physically different predictors can depend on the same computation.

The difficult case is a fixed deterministic selector. Its output is mathematically determined, so alternative outputs may be logically impossible. The paper explicitly accepts the need to evaluate such **counterpossibilities**. P-FDT’s hypotheticals are therefore decision-evaluation instruments, not assertions that mathematics can physically change.

The unresolved problem is how to construct these instruments systematically. The source supplies no general algorithm for discovering subjunctive dependencies. A dependency graph is additional modeling information, not something automatically recoverable from observed correlation.

## 3. Evidence guides the policy without necessarily screening off its effects

Policy selection requires a distinction between **knowing an observation** and **holding that observation fixed across every policy hypothetical**.

Under the operational interpretation adopted here, an episode begins with a reference model \(M\). A candidate policy generates a joint hypothetical distribution over observations and outcomes:
\[
Q_M^\pi(x,o).
\]
Its value is
\[
V_M(\pi)
=
\sum_{x,o}Q_M^\pi(x,o)u(o).
\]
The actual observation selects the action \(\pi(x)\); it need not restrict evaluation to worlds where that same observation occurs.

Why? Because receiving the observation may itself depend on what policy the agent implements. A threat may be issued only to predicted payers. A rescue may be offered only to predicted reciprocators. Conditioning every alternative on the threat or rescue having already occurred can discard precisely the dependence under examination.

This does **not** mean observations are ignored. A policy can prescribe different actions for different observations. The agent can also retain ordinary posterior beliefs about what actually happened. The distinction concerns which hypothetical distribution guides policy evaluation.

Nevertheless, choosing the reference perspective is an additional assumption. Footnote 16 does not specify whether policies range over an entire lifetime, one interaction, or another domain; nor does it completely settle which information belongs in the reference model.

A reasonable practice is to choose a domain containing the observations and commitments whose occurrence the candidate policies can affect. Information invariant across those alternatives can often be incorporated into \(M\). But changing the reference perspective opportunistically after seeing an unfavorable result would undermine the account.

Thus P-FDT needs an explicit specification of **policy domain and evidential reference point**. The source’s main action-output formulation provides motivation for allowing observations to vary, not a complete general solution to these choices.

## 4. P-FDT in Newcomb’s problem and the lesion problem

In Newcomb’s problem, an opaque box contains \(m\) dollars if a predictor forecasts one-boxing and nothing otherwise. A transparent box contains \(b\) dollars.

For a simple calculation, assume a symmetric predictive channel with accuracy \(p\) under either policy hypothetical:
\[
P(\widehat A=A\mid\operatorname{sdo}(K=\pi))=p.
\]
This is stronger than knowing only the predictor’s historical average accuracy.

For constant one-boxing and two-boxing policies,
\[
V_M(\pi_1)=pm,
\qquad
V_M(\pi_2)=(1-p)m+b.
\]
Consequently, P-FDT selects one-boxing when
\[
(2p-1)m>b.
\]
With \(p=0.99\), \(m=\$1{,}000{,}000\), and \(b=\$1{,}000\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The alternative hypothetical changes the prediction because the predictor models the selector’s behavior. No backward physical signal is postulated.

Causal decision theory, by contrast, evaluates a physical-action intervention while leaving the already-filled box unchanged. Evidential decision theory conditions on the action. These can produce different distributions despite sharing expected-utility maximization.

Now consider the source’s imaginary smoking-lesion problem. A lesion causes both cancer and a tendency to smoke, but smoking itself has no adverse health effect. Suppose this agent enjoys smoking by \(s>0\) utility units.

If changing the policy does not change the lesion or cancer, then
\[
V_M(\pi_{\rm smoke})
-
V_M(\pi_{\rm refrain})
=s.
\]
P-FDT selects smoking in this stipulated world—not because cancer is unimportant, but because it is unaffected by the relevant alternative.

The source later acknowledges complications in formalizing the lesion example, including uncertainty about preferences and population behavior. The robust lesson is therefore structural: **a predictor of a computation and a common cause of behavior are not interchangeable dependencies**.

## 5. P-FDT after observing a benefit or a threat

Transparent Newcomb makes the role of observations especially clear. The predictor fills the large box exactly when it predicts that the agent would one-box *upon seeing it full*.

With a perfect predictor, compare
\[
\pi_R(\text{full})=\text{one-box},
\qquad
\pi_R(\text{empty})=\text{two-box},
\]
against the policy \(\pi_T\) that always two-boxes.

Under \(\pi_R\), the predictor fills the box, and the agent receives \(m\). Under \(\pi_T\), it leaves the box empty, and the agent receives \(b\). For \(m>b\), P-FDT selects \(\pi_R\).

Seeing a full box then calls for one-boxing. The comparison is not between two bodily movements with the observed box contents frozen. It is between policies, including their influence on the prediction and hence on which observation occurs.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded traveler only if the driver predicts payment after arrival. A policy that pays in the city can secure rescue; a policy that refuses may prevent arrival. P-FDT can therefore recommend paying after the rescue without treating the payment as a physical cause of a past event.

Mechanical blackmail reverses the incentives. Suppose:

- paying costs \(c\);
- refusal after a threat causes loss \(L\);
- the blackmailer always threatens predicted payers;
- a committed refuser is mistakenly threatened with probability \(q\).

Then the policy losses are
\[
\operatorname{Loss}(\pi_{\rm pay})=c,
\qquad
\operatorname{Loss}(\pi_{\rm refuse})=qL.
\]
P-FDT selects refusal precisely when
\[
qL<c.
\]
For \(L=1{,}000{,}000\), \(c=1{,}000\), and \(q=0.0009\), refusal has expected loss \(900\), versus \(1{,}000\) for payment.

This remains the selected response even on the rare branch where the refuser receives a threat. But P-FDT does not prescribe unconditional obstinacy: when \(qL>c\), this model favors payment.

These conclusions depend on the predictive setup. If the threatening process is independent of the agent’s policy, the model must not invent a deterrence benefit. The practical calculation is only as good as that dependency assessment.

## 6. Why P-FDT chooses whole policies

The source says policy selection matters in some multi-agent dilemmas but supplies no worked example establishing exactly where. The following is my illustration of why optimizing whole policies can differ from optimizing their entries separately.

Two agents share an identical policy selector. Each independently receives a private input \(x\in\{\ell,h\}\), with equal probabilities. Each chooses \(C\) or \(D\). Their respective payoffs are
\[
u_i
=
10\,\mathbf 1\{A_1=C,\ A_2=C\}
-
c(x_i)\mathbf 1\{A_i=C\},
\]
where
\[
c(\ell)=6,\qquad c(h)=7.
\]
Thus cooperation costs something even when the other agent defects.

Assume the policy-output node is shared: setting \(K=\pi\) makes both agents apply \(\pi\) to their own inputs. This does not force their actions to agree when their inputs differ.

There are four deterministic policies:

| \(\pi(\ell)\) | \(\pi(h)\) | Expected payoff to either agent |
|---|---|---:|
| \(D\) | \(D\) | \(0\) |
| \(C\) | \(D\) | \(-0.5\) |
| \(D\) | \(C\) | \(-1\) |
| \(C\) | \(C\) | \(3.5\) |

For example, under \((C,D)\), mutual cooperation occurs with probability \(1/4\), while an agent pays cost \(6\) with probability \(1/2\):
\[
V_M(C,D)=10/4-6/2=-0.5.
\]
Under \((C,C)\),
\[
V_M(C,C)=10-\frac{6+7}{2}=3.5.
\]

Whole-policy maximization therefore selects cooperation at both inputs. Yet starting from \((D,D)\), changing either policy entry alone reduces value. A coordinate-by-coordinate improvement procedure can remain at universal defection.

This is not a claim that every action-output formulation necessarily fails in this game. It demonstrates the mathematical distinction that a policy formulation must preserve: **jointly changing an input-output mapping can reveal improvements unavailable through isolated changes to its entries**.

Nor does sharing the label “P-FDT agent” establish a shared node. The example assumes identical selectors, compatible reference models, and symmetric objectives. With heterogeneous agents, their responses must be modeled rather than stipulated to track ours.

## 7. Applying P-FDT to an unfamiliar problem

Given these qualifications, an application can proceed systematically.

1. **Specify the decision domain.** Identify possible inputs, available actions, admissible policies, utility, and the reference model. Include relevant contingencies, not merely the observed branch.

2. **Locate the policy-output variable.** Determine what computation is represented by \(K\), and which predictors, copies, or later implementations depend on it.

3. **Construct policy hypotheticals.** For each \(\pi\), recompute those dependent processes and their consequences. Preserve unrelated background mechanisms; do not infer functional dependence from correlation alone.

4. **Maximize and apply.** Calculate \(V_M(\pi)\), select a maximizing policy, and execute its response to the actual input.

For finite spaces this is a definite optimization problem once the hypothetical distributions are supplied, though exhaustive search involves up to
\[
|\mathcal A|^{|\mathcal X|}
\]
policies. Practical approximations require restricted policy classes or structured optimization.

Several foundational questions remain. Which dependencies should a computational intervention preserve? How broad should the policy’s input domain be? How should uncertainty about the selector itself be represented? If randomization is allowed, can the predictor see the random seed, or only the distribution? These are different models, not interchangeable descriptions.

Finally, the paper’s favorable examples are not a universal optimality theorem. It acknowledges that adversarial environments can punish any particular decision procedure and leaves its notion of a “fair” problem incompletely formalized. Reflective stability and nonnegative value of information likewise require assumptions, rather than following from the word *policy* alone.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Primary passages: footnotes 16 and 7; supporting discussion: §§3, 5, and 9. https://arxiv.org/src/1710.05060v2

## Conclusion

P-FDT evaluates the policy a fixed decision procedure should output, then applies that policy to the input actually received. Its central commitment is to preserve relevant predictive and computational dependencies while rejecting merely evidential ones. This explains both its attraction and its unfinished character: once the policy hypotheticals are specified, optimization is straightforward; constructing and justifying those hypotheticals remains the deepest problem.