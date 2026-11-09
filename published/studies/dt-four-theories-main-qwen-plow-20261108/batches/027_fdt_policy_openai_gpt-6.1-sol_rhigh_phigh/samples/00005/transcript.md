# 027_fdt_policy_openai_gpt-6.1-sol_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/c57bb1e0-4b4b-421d-85db-11c5f8c44406/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/c57bb1e0-4b4b-421d-85db-11c5f8c44406/call_0/response.raw) · finish: `stop`

### Visible response

```text
# P-FDT: Choosing the Policy Your Reasoning Implements

Decision problems become unusual when the world contains representations of the decision-maker: a predictor anticipating her response, a software copy running the same calculation, or another agent reasoning symmetrically. In such cases, changing a physical action while holding everything else fixed can discard precisely the dependencies that make the problem interesting.

**Policy functional decision theory (P-FDT)** evaluates alternatives at the level of an entire policy: a mapping from inputs to actions. Its central question is:

> Which policy would produce the best expected outcome, accounting for the ways other processes depend on this policy-selection procedure’s output?

The primary source for this account is footnote 16 of Eliezer Yudkowsky and Nate Soares’s *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2. It describes their preferred formulation as choosing “a policy which maps inputs to actions,” after which the agent applies her inputs to select an action. Footnote 7 likewise identifies policies as mappings from observations to actions.

These passages establish the object of choice, but not a complete mathematical theory. In particular, they do not fully specify the policy domain, the reference information state, or policy-level counterfactuals. Below, I distinguish the source’s commitments from an operational reconstruction that makes these choices explicit.

## 1. From actions to policies

Let \(\mathcal X\) be a finite set of possible observation histories and \(\mathcal A\) a finite action set. A deterministic policy is a function

\[
\pi:\mathcal X\longrightarrow\mathcal A.
\]

Write \(\Pi\subseteq\mathcal A^{\mathcal X}\) for the admissible policies. After selecting \(\pi^*\), an agent observing \(x\) performs

\[
a=\pi^*(x).
\]

The distinction between selecting \(\pi\) and selecting \(a\) matters because a policy specifies behavior at *other inputs too*, including inputs never actually received. Predictors may inspect these hypothetical responses. Other agents may implement the same policy-selection procedure while receiving different observations.

Policy selection alone, however, does not define P-FDT. A causal decision theorist can also optimize policies before entering a problem. The distinctive issue is **how alternative policies are evaluated**, especially after the agent has received information that depends on predictions of her behavior.

For comparison, standard evidential decision theory (EDT) evaluates an action using

\[
\mathbb E[U\mid X=x,A=a],
\]

whereas standard causal decision theory (CDT) uses an intervention on the physical action:

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]

P-FDT instead considers a counterfactual change in the output of its policy-selection computation, propagating that change through relevant mathematical and causal dependencies.

The source treats decision hypotheticals as reasoning instruments, not necessarily as physically possible worlds. This is important: P-FDT does not require believing that a present action sends a signal into the past.

## 2. A mathematical reconstruction of P-FDT

Here is one precise implementation of the footnote’s proposal. It is a reconstruction, not an equation explicitly supplied there.

Let \(M\) contain:

- a reference probability model for the problem;
- an outcome utility function \(u\);
- a policy class \(\Pi\);
- a specification of the relevant dependencies.

Let \(S(M)\) denote the policy-selection computation, and let \(D\) be a variable *representing its output*. Thus the actual policy is \(D=S(M)\).

For each candidate policy \(\pi\), construct a hypothetical distribution

\[
Q_M^\pi
=
\operatorname{Hyp}_M(D\leftarrow\pi).
\]

The arrow denotes a **subjunctive intervention**: set the represented output of this very selector to \(\pi\), then propagate the change through the dependencies specified by \(M\). Define

\[
V_M(\pi)=\mathbb E_{Q_M^\pi}[u(O)],
\]

and choose

\[
\boxed{
\pi^*=S(M)
=
\operatorname{TB}\!\left(
\arg\max_{\pi\in\Pi}V_M(\pi)
\right),
\qquad
a=\pi^*(x).
}
\]

Here \(\operatorname{TB}\) is a specified tie-breaking rule. With finite sets, a maximizer exists.

For tractable examples, the hypothetical can be represented by structural equations. Let \(Z\sim\mu\) collect background uncertainty. After replacing \(D\) by \(\pi\), calculate

\[
X_\pi=h(\pi,Z),\qquad
A_\pi=\pi(X_\pi),\qquad
O_\pi=g(\pi,X_\pi,A_\pi,Z).
\]

Then

\[
V_M(\pi)
=
\int u(O_\pi(z))\,\mu(dz).
\]

The appearance of \(\pi\) in \(h\) and \(g\) permits predictors and copies to respond to the policy. It does **not** license arbitrary changes in background facts.

### The reference-information assumption

This reconstruction evaluates complete policies from a fixed reference model \(M\), rather than automatically conditioning their values on the observation currently received. Observations affect behavior through \(\pi(x)\).

This interpretation fits the paper’s discussions of transparent boxes and blackmail: alternative reasoning outputs can imply different observations. Nevertheless, footnote 16 does not uniquely determine the appropriate reference information state.

The assumption is therefore substantive. A policy evaluated from a model established before a prediction-sensitive observation can differ from a policy reoptimized conditional on that observation. Without specifying this boundary, “maximize expected policy utility” is incomplete.

## 3. What changes in a P-FDT counterfactual?

The source calls the relevant relation **subjunctive dependence**. It includes ordinary causal dependence but also relationships between computations, their copies, and reliable representations.

Three distinctions are central.

**Causal consequences change.** If a policy calls for buying an item, the agent’s money and possessions change accordingly.

**Representations of the selector’s output change appropriately.** If a predictor models this selector, then the hypothetical \(D\leftarrow\pi\) must affect its prediction according to its predictive mechanism.

**Mere correlates need not change.** A disease correlated with behavior does not thereby depend on the policy-selection output.

For exact copies, the dependency may be especially strong. If two systems run the same selector on the same model, a hypothetical change in that selector’s output changes both implementations. But different inputs, models, preferences, or algorithms can weaken or eliminate the link. P-FDT is not the instruction to assume that everyone reasons alike.

Imperfect prediction requires more than an observed accuracy rate. One must specify how the predictor would respond under *each candidate policy*. An aggregate historical success rate does not determine this counterfactual response.

There is also a foundational difficulty. A fixed deterministic computation has only one actual output. Asking what follows if it outputs another policy can therefore be **counterpossible**, rather than merely counterfactual. The source openly acknowledges that a general account of such reasoning remains unresolved.

A dependency model can make particular examples calculable, but notation does not solve this problem. Writing \(D\leftarrow\pi\) is useful only after explaining which relationships it preserves and which it breaks.

## 4. P-FDT in Newcomb’s problem and the lesion problem

In Newcomb’s problem, an opaque box contains \(H=\$1{,}000{,}000\) if a predictor forecasts one-boxing and nothing otherwise. A transparent box contains \(b=\$1{,}000\).

There is only one relevant observation, so policies reduce to the two constant responses. Assume a symmetric counterfactual error model: under either candidate response, the predictor forecasts it correctly with probability \(q\). With money treated as linear utility,

\[
V_M(\pi_{\mathrm{one}})=qH,
\]

\[
V_M(\pi_{\mathrm{two}})=(1-q)H+b.
\]

P-FDT selects one-boxing exactly when

\[
(2q-1)H>b.
\]

For \(q=0.99\), the values are \(\$990{,}000\) and \(\$11{,}000\).

The predictor’s earlier behavior changes in the hypothetical because it represents the selector’s output. The agent does not believe that taking one box physically changes an already-filled box.

Now contrast the imaginary smoking-lesion problem. A lesion causes both a desire to smoke and cancer, while smoking itself has no effect on cancer. For an agent who values smoking by \(s>0\), suppose that changing her selected policy leaves the lesion and cancer mechanisms unchanged. Then

\[
V_M(\pi_{\mathrm{smoke}})
-
V_M(\pi_{\mathrm{refrain}})
=s.
\]

P-FDT selects smoking in this fictional setup. Statistical evidence about disease is not treated as a disease-producing consequence of the policy.

The source later acknowledges complications in the traditional lesion problem, particularly uncertainty about preferences and population-level correlations. The clean lesson is narrower than an unqualified verdict against EDT: **predictive representation and ordinary common-cause correlation can require different counterfactual treatments**. Nothing here applies directly to real smoking, which causally harms health.

## 5. P-FDT after receiving prediction-sensitive information

Transparent Newcomb makes the reference-information issue unavoidable.

The agent sees whether the large box is full. The predictor fills it exactly when predicting that she would one-box *upon seeing it full*. A policy therefore specifies two responses:

\[
\pi(F),\qquad \pi(E),
\]

for full and empty observations.

Under the stipulated prediction mechanism, two-boxing at \(E\) adds \(b\) without affecting whether the box is filled. Thus restrict attention to policies with \(\pi(E)=2\). Compare

\[
\pi_1(F)=1,\qquad \pi_1(E)=2,
\]

with

\[
\pi_2(F)=2,\qquad \pi_2(E)=2.
\]

Using the same symmetric error model,

\[
V_M(\pi_1)=qH+(1-q)b,
\]

\[
V_M(\pi_2)=(1-q)H+b.
\]

At \(q=0.99\), these equal \(\$990{,}010\) and \(\$11{,}000\). P-FDT selects \(\pi_1\), and therefore one-boxes when observing \(F\).

This does not deny the observation. The agent believes that the actual box is full. But when evaluating another *policy*, she allows the predictor, box contents, and resulting observation to differ.

Conditioning both candidate policies on \(X=F\) would instead compare one million dollars with one million plus one thousand dollars. That is a different evaluation rule. Under the reconstruction here, it discards the policy’s effect on whether \(F\) is encountered.

Parfit’s hitchhiker has the same structure. A driver rescues a stranded agent only if predicting that she will pay after reaching town. A policy specifies the response at the town observation. Selecting a paying policy can produce rescue, although paying has no further physical benefit once the agent is safe.

This is why P-FDT resembles ideal precommitment. The resemblance is not an appeal to sunk costs or a moral obligation to keep promises. It comes from continuing to evaluate the policy together with its predictive dependencies.

### Imperfect blackmail

The same reasoning need not endorse unconditional stubbornness.

Suppose a blackmailer always targets a paying policy, extracting \(c\). A refusing policy is mistakenly targeted with probability \(\varepsilon\), causing loss \(L\). Assume no other relevant consequences. Then

\[
V_M(\pi_{\mathrm{pay}})=-c,
\qquad
V_M(\pi_{\mathrm{refuse}})=-\varepsilon L.
\]

P-FDT refuses when

\[
\varepsilon L<c.
\]

Thus refusal can be optimal despite occasional disastrous mistakes, but sufficiently frequent mistakes favor payment. The prescription depends on the counterfactual error model, not on a categorical prohibition against paying.

Again, receipt of a letter is prediction-sensitive evidence. Reconditioning the entire comparison on receiving it would remove the deterrence benefit that motivated the refusing policy.

## 6. Why P-FDT selects whole policies

The authors suggest that policy selection differs from their action-selection presentation in some multi-agent problems. They do not provide the relevant example in footnote 16. The following constructed example illustrates one reason the distinction can matter.

Two identical agents receive independent fair bits \(x,y\in\{0,1\}\). Each reports a bit. Both receive:

- \(10\) if both reports equal their respective inputs;
- \(4\) if both reports differ from their respective inputs;
- \(0\) otherwise.

Assume they implement the same policy selector with the same reference model. A policy-level hypothetical therefore changes both agents’ complete reporting policies.

There are four deterministic policies:

\[
\pi_{\mathrm{id}}(x)=x,\qquad
\pi_{\mathrm{inv}}(x)=1-x,
\]

and the two constant policies. Their values are

\[
V_M(\pi_{\mathrm{id}})=10,
\qquad
V_M(\pi_{\mathrm{inv}})=4.
\]

For either constant policy, both agents are correct with probability \(1/4\), both incorrect with probability \(1/4\), and mixed otherwise. Hence

\[
V_M(\pi_{\mathrm{constant}})
=
\frac{10}{4}+\frac{4}{4}
=3.5.
\]

P-FDT selects the identity policy.

Now consider a pointwise procedure that evaluates changing one input’s response while holding the other response fixed. Starting from the inverse policy, changing only one entry produces a constant policy, reducing value from \(4\) to \(3.5\). The inverse policy is therefore a local optimum under such changes, though globally inferior.

This does not prove that every action-selection formulation fails. It shows why optimizing a complete policy can differ from separately optimizing its entries. The relevant counterfactual changes responses across inputs as one package.

Notice also that selecting one shared policy does not mean selecting one shared physical action. Under the identity policy, agents receiving different bits report different bits. P-FDT coordinates the *mapping*, not necessarily the behavior at every input.

## 7. Applying P-FDT to unfamiliar cases

A practical analysis should proceed in the following order.

**First, define the policy domain.** Specify what counts as an input, including private information and observation histories. Sequential problems require contingent plans, not merely a first action.

**Second, identify the selector being represented.** Is a predictor modeling this agent’s response, a complete policy, or some different algorithm? Similarity alone does not establish identity.

**Third, specify the reference information boundary.** Which facts are already incorporated into \(M\), and which observations are generated within the policy-sensitive problem? This choice must be justified, not hidden.

**Fourth, construct each hypothetical.** Change the selector’s represented output, propagate changes through copies, predictors, actions, and consequences, and retain background mechanisms that do not depend on that output.

**Fifth, compute expected utility and apply the selected policy to the actual input.**

Several limitations remain important.

Policy classes may be computationally enormous. With \(n\) observations and \(k\) actions, there are \(k^n\) deterministic policies. Restricting to computable or affordable policies is natural, but changes the optimization problem. Randomized policies also require specifying whether random seeds are shared, predictable, or private.

Multi-agent dependencies can introduce circularity and multiple self-consistent solutions. A general treatment needs existence and selection principles beyond the footnote. Common names for decision theories do not by themselves imply common computations or preferences.

Finally, P-FDT’s attractive implications require qualifications. Free information has nonnegative policy value when the expanded policy class can ignore it and acquiring it has no adverse strategic effects. Reflective stability is plausible in the paper’s examples, not a universal theorem. The source itself leaves a general definition of “fair” decision problems and a corresponding optimality result open.

## Conclusion

P-FDT evaluates complete input-to-action policies by imagining different outputs of the policy-selection computation and preserving the dependencies that genuinely track those outputs. Its distinctive move is neither ordinary conditioning nor intervention on one isolated physical act.

This yields a coherent operational method when the policy space, reference information, and subjunctive dependencies are specified. The principal unfinished work lies in specifying them generally. Footnote 16 offers a powerful organizing idea; turning it into a fully general decision theory remains a substantive mathematical task.
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Calculating word count and model assumptions**

I need to calculate the word count generated, which is about 2900 words. I've got a time constraint of around 17 tokens and a budget close to 26,000 tokens, with remaining tokens being about 25,885, which should be enough. I want to be precise when discussing the multi-agent model interactions and how they relate to input and output predictions. It's important to clarify that my example isn't a proof but demonstrates motivating conditions related to model assumptions.**Interpreting policy selection and outputs**

I’m reflecting on how policies aren't just precommitments but involve interpreting outputs from various models and observations. It's crucial to understand that policy selection might change depending on the input. The counterfactual situation illustrates that observed outcomes can differ, affecting how we evaluate policies. Moreover, when updating information—like in medical contexts—it's not necessary to rely on fixed priors, as new evidence can change our understanding. I need to be careful about assuming that observations will remain invariant when faced with different policies.**Analyzing counterfactual invariance and noise**

I'm considering how counterfactual invariance connects to external events and whether conditioning is valid. If I'm inferring noise from a letter contingent on my own policy, the derived outcomes might not be invariant. It’s crucial to note that evidence outside intervention-sensitive areas doesn't lead to straightforward logical conclusions. In scenarios involving blackmail, the expected payoff remains targeted, especially when considering refusal risks. I notice some errors related to epsilon policies could be independent of conditions, highlighting a flexible approach to strategy.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/5585167c-418b-4d2a-b202-2fe7c38eda5e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/5585167c-418b-4d2a-b202-2fe7c38eda5e/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/5585167c-418b-4d2a-b202-2fe7c38eda5e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/5585167c-418b-4d2a-b202-2fe7c38eda5e/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
