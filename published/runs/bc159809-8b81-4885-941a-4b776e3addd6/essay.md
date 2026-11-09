# P-FDT: Choosing the Policy Behind the Action

A decision can matter even when its physical consequences are small. A predictor may already have rewarded the decision it expects you to make. Another agent may independently reproduce your reasoning. Your willingness to honor an agreement may determine whether anyone offers it.

**Policy functional decision theory (P-FDT)** approaches such situations by evaluating the output of a policy-selection procedure, including relevant dependencies between that output and the surrounding world.

The primary source here is footnote 16 of Yudkowsky and Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*. It describes their preferred formulation as choosing “a policy which maps inputs to actions,” after which the agent applies its inputs to obtain an action. Footnote 7 similarly describes policies as mappings from observations to actions. Most of the paper instead develops an **action-output formulation of functional decision theory**, setting the policy distinction aside for exposition.

That distinction matters. Choosing one response at one information state need not be equivalent to choosing a whole contingent strategy. Unfortunately, the footnote does not completely specify the policy space, evaluation perspective, or intervention semantics. This essay therefore separates the source’s central proposal from an operational reconstruction: optimize a policy using a model of how the world subjunctively depends on the policy selector’s output, then execute that policy on the actual input.

## 1. The object P-FDT chooses

Let:

- \(\mathcal X\) be a set of possible inputs, such as observation histories;
- \(\mathcal A\) be a set of actions;
- \(\mathcal O\) be a set of outcomes;
- \(U:\mathcal O\to\mathbb R\) be a bounded utility function.

A deterministic policy is a function
\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]
If the selected policy is \(\pi\) and the actual observation is \(x\), the agent performs
\[
a=\pi(x).
\]

A policy is thus not a commitment to ignore future evidence. It specifies how to respond to evidence. A driving policy might prescribe braking when the road is blocked and accelerating when it is clear.

For simplicity, assume finite input and action spaces and a specified admissible set
\[
\Pi\subseteq\mathcal A^{\mathcal X}.
\]
Restrictions on \(\Pi\) can represent computational limitations or unavailable actions. Randomized policies require additional assumptions about the source of randomness and whether predictors or copies can access it.

The crucial question is how to assign a value to \(\pi\). Merely computing
\[
\mathbb E[U(O)\mid \text{I use }\pi]
\]
is not enough: this conditional may select favorable background circumstances rather than describe what changes with the decision. Nor is it generally enough to imagine physically installing a different program now. An earlier predictor may have been predicting the actual selector, not a replacement program.

P-FDT instead asks what would follow **if this very policy-selection procedure returned \(\pi\)**. Its counterfactual object is the selector’s mathematical output, not merely the physical action eventually performed.

## 2. A mathematical reconstruction of P-FDT

Let \(M\) be a reference world-model containing probabilities, utilities, and relevant dependency information. Let \(D_M\) be a variable representing the policy returned by the P-FDT selector on that model.

Write
\[
Q_M^\pi(o)
=
\Pr_M\!\left(
O=o\;\middle\Vert\;D_M\leftarrow\pi
\right).
\]
The double bar denotes a **subjunctive intervention**, not ordinary conditional probability. It means: construct the hypothetical in which the selector returns \(\pi\), propagating the corresponding changes through the dependencies represented in \(M\).

The proposed policy value is
\[
V_M(\pi)=\sum_{o\in\mathcal O}Q_M^\pi(o)U(o),
\]
and the selection rule is
\[
\pi_M^*
=
\operatorname*{arg\,max}_{\pi\in\Pi}V_M(\pi).
\]
A fixed tie-breaking convention makes this single-valued. The executed action is
\[
\boxed{\operatorname{P\!-\!FDT}(M,x)=\pi_M^*(x).}
\]

This equation is my reconstruction of the footnote, not a formula supplied there. Its essential feature is that the intervention changes an **entire policy-valued output**.

A useful operational representation introduces background uncertainty \(W\sim\mu_M\). Given the hypothetical policy output \(\pi\), structural equations determine
\[
X^\pi=g_X(\pi,W),\qquad
A^\pi=\pi(X^\pi),\qquad
O^\pi=g_O(\pi,X^\pi,A^\pi,W).
\]
Then
\[
V_M(\pi)=\mathbb E_{W\sim\mu_M}[U(O^\pi)].
\]

Here \(g_X\) may depend on \(\pi\): a predictor’s response can determine which observation the agent receives. Other agents’ actions can likewise depend on \(\pi\), where their computations genuinely track the same policy selection.

These equations resemble a structural causal model, but their arrows need not all represent physical causation. Some represent computational or logical dependence. The source calls the broader relation **subjunctive dependence**.

Three distinctions are central:

1. **Causal consequences remain relevant.** If the selected policy makes the agent press a button, the button’s physical effects change.
2. **Predictive and computational dependencies may also remain relevant.** An accurate simulation of the selector should generally track its hypothetical output.
3. **Mere correlation is insufficient.** A disease correlated with behavior need not change when the selector’s output changes.

The intervention edits a representation used for deliberation. It does not assert that an agent sends signals backward in time or physically alters mathematics.

## 3. Why the dependency structure matters

For comparison, evidential decision theory (EDT) evaluates an action using expressions such as
\[
\mathbb E[U(O)\mid X=x,A=a].
\]
Causal decision theory (CDT) instead evaluates causal interventions:
\[
\mathbb E[U(O)\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT’s distinctive question concerns the output of the policy selector and everything appropriately dependent on that output.

### P-FDT in Newcomb’s problem

Suppose a predictor fills an opaque box with \(B=\$1{,}000{,}000\) when it predicts one-boxing, while a transparent box always contains \(b=\$1{,}000\).

Assume a symmetric prediction-error model: under either candidate output, the prediction agrees with the resulting choice with probability \(q\). This is stronger than knowing that a predictor was accurate \(q\) of the time in some historical population.

For the relevant constant policies,
\[
V(\pi_{\text{one}})=qB,
\]
while
\[
V(\pi_{\text{two}})=(1-q)B+b.
\]
Thus P-FDT one-boxes exactly when
\[
(2q-1)B>b.
\]
At \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The money does not change because the hand reaches differently. Rather, the predictor’s earlier model and the agent’s later behavior depend on the same policy-selection output. P-FDT preserves that dependency in its evaluation.

### P-FDT and a merely correlated condition

Contrast an imaginary medical case where a lesion causes both a desire to smoke and cancer, but smoking itself does not cause cancer. If smoking provides utility \(s>0\), and neither the lesion nor cancer subjunctively depends on the selected response, then
\[
V(\pi_{\text{smoke}})-V(\pi_{\text{refrain}})=s.
\]

Changing the policy output does not change the lesion. P-FDT therefore takes the benefit rather than selecting favorable evidence about its health.

This is a stylized distinction, not advice about actual smoking. The source itself later criticizes the traditional smoking-lesion problem as difficult to formalize coherently. The underlying lesson is more reliable than that particular example: **predictive tracking and common-cause correlation require different counterfactual treatment**.

## 4. Observation, policy evaluation, and hindsight

The hardest operational issue is the perspective from which policies are evaluated.

My reconstruction uses a reference distribution before conditioning on observations whose occurrence can itself depend on the candidate policy. Actual observations determine which policy entry is executed; they are not automatically imposed as fixed constraints on every policy hypothetical.

This interpretation is motivated by the paper’s treatment of transparent Newcomb problems and mechanical blackmail. Its action-output formulation allows an alternative output to produce different observations. Nevertheless, footnote 16 alone does not uniquely determine this evaluation rule.

### P-FDT in the hitchhiker problem

Suppose a driver rescues an agent only if the driver predicts that the agent will pay \(c\) upon reaching the city. Rescue is worth \(B>c\). Consider policies
\[
\pi_P(\text{city})=\text{pay},
\qquad
\pi_R(\text{city})=\text{refuse}.
\]

With perfect prediction,
\[
V(\pi_P)=B-c,\qquad V(\pi_R)=0.
\]
P-FDT selects \(\pi_P\). On arriving in the city, it pays.

At that moment, paying does not causally improve the rescue already received. The justification is instead that payment is the city-response of the policy whose predictable execution secures rescue.

The transparent Newcomb problem has the same structure. A predictor fills the large box only if it predicts that the agent’s policy leaves the small box behind upon seeing a full large box. The policy must specify responses to both full and empty boxes; its evaluation permits the observed contents to vary with that policy.

This is not the belief that the agent might presently be elsewhere despite seeing the city. It distinguishes:

- **factual belief:** which situation actually occurred;
- **policy evaluation:** which situations accompany alternative selector outputs.

### P-FDT does not generally ignore evidence

Suppose instead that an observation \(X\) is unaffected by policy selection and no dependency couples responses at different inputs. Then policy value decomposes:
\[
V_M(\pi)
=
\sum_x P_M(x)\,v_x(\pi(x)),
\]
where \(v_x(a)\) is the appropriate expected utility of action \(a\) after observation \(x\).

If all combinations of responses are admissible, maximizing \(V_M\) amounts to choosing, separately for every positive-probability input,
\[
\pi^*(x)\in\arg\max_a v_x(a).
\]

Thus a contingent policy can use ordinary evidence exactly as expected-utility reasoning recommends. The unusual behavior arises when fixing the observation would suppress a dependency central to evaluating the policy.

The unresolved boundary is important. Which information belongs in the reference model, and which belongs among policy inputs? If every new observation rebuilds the model from a freshly conditioned perspective, the hitchhiker argument can disappear. Conversely, an unnecessarily remote reference perspective can bind together decisions without justification. The source does not supply a general rule resolving this choice.

## 5. Why P-FDT selects whole policies

Footnote 16 says the policy distinction matters in multi-agent dilemmas “so far as we can tell.” The following original example illustrates a mechanism by which it can matter; it is not an example supplied by the paper.

Two agents perform complementary tasks. One receives role \(0\), the other role \(1\). Each chooses whether to work. Each receives benefit \(R\) if both work and pays personal cost \(c\) if it works, where \(R>c>0\).

Assume both instantiate the same policy selector with the same reference model. Their different role labels are inputs applied **after** a common policy is selected. Write
\[
\pi=(\pi(0),\pi(1))\in\{0,1\}^2,
\]
where \(1\) means working.

From a reference perspective assigning equal probability to occupying either role,
\[
V(\pi)
=
R\,\pi(0)\pi(1)
-\frac c2\bigl(\pi(0)+\pi(1)\bigr).
\]
Consequently,
\[
V(0,0)=0,\qquad
V(1,0)=V(0,1)=-c/2,
\]
but
\[
V(1,1)=R-c>0.
\]

Changing only one policy entry from the all-idle policy makes matters worse. Changing the whole policy makes both agents work and improves both agents’ outcomes.

This shows why independently optimizing one response while holding other responses fixed can miss a profitable policy change. It does not establish that every action-output formulation necessarily fails: additional logical dependencies might connect its response nodes. Rather, policy selection explicitly represents the larger unit of variation.

The common-policy assumption does substantial work. Two agents do not share a selector output merely because both endorse P-FDT. Different utilities, models, or computational procedures may break the relevant connection. Even identical algorithms receiving different selector-level inputs need not return identical policies.

P-FDT is therefore not a general instruction to cooperate. It recommends cooperation when the specified dependencies and payoffs make a cooperative policy best.

## 6. P-FDT under imperfect prediction

Policy evaluation also explains why resistance to exploitation is conditional rather than absolute.

Consider mechanical blackmail. Paying costs \(c\). Refusing after an attack causes loss \(L\). Assume:

- a predictable payer is always attacked;
- a predictable refuser is attacked with probability \(\varepsilon\);
- these probabilities remain valid under the corresponding policy interventions.

Then
\[
V(\pi_{\text{pay}})=-c,\qquad
V(\pi_{\text{refuse}})=-\varepsilon L.
\]
P-FDT selects refusal when
\[
\varepsilon L<c.
\]

On this evaluation, a refuser may refuse even upon receiving a letter, although that particular realization is costly. The policy earns its advantage by discouraging most attacks.

But if attacks occur independently of the agent’s predictable response, the calculation changes. Refusal no longer deters anything. P-FDT does not justify inventing a dependency because the resulting policy seems admirable.

Likewise, a predictor’s error probability may depend on the policy, available evidence, or randomization mechanism. A single accuracy figure cannot substitute for a counterfactual model.

## 7. What remains open in P-FDT

The mathematical maximization is straightforward once the hypothetical outcome laws are supplied. Supplying those laws is the difficult part.

**First, subjunctive interventions lack a complete general semantics.** A fixed mathematical selector has one output on a fixed input. Considering another output is therefore potentially counterpossible. The paper explicitly acknowledges that deriving suitable logical dependency structures remains an open problem. Structural equations provide a useful interface, not a finished foundation.

**Second, policy scope requires justification.** I have held utility and the reference model fixed while allowing observations and role labels to vary. If policies instead map every possible belief state and utility function to actions, one needs further principles explaining how those cases enter the objective.

**Third, implementation matters.** Mathematically equivalent policies may have different source code, execution costs, or predictability. Whether policies are identified extensionally by their input-output behavior or intensionally by their implementation can affect the problem.

**Fourth, optimality claims need qualification.** The paper argues that its broader approach performs well across familiar dilemmas, but acknowledges uncertainty about a general definition of fair comparison. Neither footnote 16 nor the examples prove universal superiority or reflective stability.

For an unfamiliar case, the practical procedure is therefore:

1. Specify the policy’s inputs, available responses, and evaluation perspective.
2. Identify what genuinely tracks the selector’s output.
3. Construct complete outcome distributions for alternative policy outputs.
4. Compare expected utilities and execute the selected policy’s actual-input response.
5. Test sensitivity to disputed dependencies and modeling choices.

Where those choices remain unresolved, the honest result is conditional rather than a uniquely determined verdict.

## Reference

Yudkowsky, Eliezer, and Nate Soares. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2. Especially footnotes 7 and 16 and §§3, 5, and 9. https://arxiv.org/abs/1710.05060v2

## Conclusion

P-FDT evaluates the contingent policy returned by a decision procedure, preserving relevant causal, predictive, and computational dependencies while breaking merely evidential correlations. Its appeal is that predictable policy execution can secure opportunities that locally tempting deviations undermine.

Footnote 16 supplies this central shift, not a complete mathematical theory. A usable P-FDT analysis must additionally specify policy scope, reference information, and subjunctive counterfactuals. Making those assumptions explicit turns an intriguing slogan into a disciplined—though still incomplete—method of decision-making.