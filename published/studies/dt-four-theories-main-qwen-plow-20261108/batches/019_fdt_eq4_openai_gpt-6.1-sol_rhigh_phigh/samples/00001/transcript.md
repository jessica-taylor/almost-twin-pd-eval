# 019_fdt_eq4_openai_gpt-6.1-sol_rhigh_phigh / 00001

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/eeab117d-94ae-42fc-9f2a-5475262336fa/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/eeab117d-94ae-42fc-9f2a-5475262336fa/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of a Decision Function

A decision can be understood both as a physical event and as the result of a computation. Usually these perspectives agree about what to do. If choosing an umbrella affects whether I get wet, and nothing else depends on my choice, ordinary causal reasoning suffices.

They can diverge when someone predicts my computation, another agent implements it, or an earlier benefit depends on what that computation would recommend later. **Action functional decision theory (A-FDT)** evaluates alternatives by varying the output of the relevant computation, preserving dependencies between that output and its implementations or predictions.

This essay takes Equation (4) of Section 5 of Yudkowsky and Soares’s paper as its defining rule. The source calls the theory presented there “FDT”; here, **A-FDT** specifically names its action-output formulation. This distinction matters because the paper also mentions a different formulation that selects whole policies.

## 1. The formal rule

Let:

- \(\mathcal A\) be a finite action set;
- \(X\) be an observation-history variable, with current history \(x\);
- \(O\) be an outcome variable;
- \(V=\mathcal U(O)\) be utility, with finite relevant expectations;
- \(P\) be a probabilistic world-model;
- \(G\) describe the dependencies used to construct decision counterfactuals.

The distinctive ingredient is a model variable
\[
D_x:=\text{the represented output of }\operatorname{A\!-\!FDT}(P,G,x).
\]
Strictly, its identity depends on \(P,G,x\), not merely \(x\). It represents what this very decision procedure outputs on these particular inputs.

Renaming the source’s notation, Equation (4) becomes
\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\operatorname*{arg\,max}_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\]
A fixed tie-breaking rule can make the result single-valued. Predictors must model that rule too.

For comparison, **evidential decision theory (EDT)** evaluates
\[
\mathbb E[V\mid X=x,A=a],
\]
while the paper’s formulation of **causal decision theory (CDT)** evaluates
\[
\mathbb E[V\mid\operatorname{do}(A=a),X=x].
\]

A-FDT differs in two ways.

First, it intervenes on a represented **computational output**, rather than directly on the physical action \(A\). That output may determine both the agent’s action and a predictor’s forecast.

Second, Equation (4) contains **no additional conditioning on \(X=x\)**. Observation selects the intervention target \(D_x\). When the history changes to \(y\), the target becomes \(D_y\). This is essential, not a notational omission.

Finally, \(D_x\) is not the same thing as the actual answer returned by the algorithm. It is a variable *representing* that answer, which the agent manipulates while deliberating. The source appeals to computational self-reference techniques to explain how a program can represent its own computation without already knowing its result. Such representation does not, by itself, solve questions of computational tractability or model consistency.

## 2. Dependencies and counterpossibilities

The source calls the relevant relation **subjunctive dependence**. Two systems can depend on the same computation without either system physically causing the other’s behavior.

Suppose two isolated machines evaluate the same deterministic program on identical inputs. Their outputs must agree. Alternatively, a sufficiently accurate predictor might compute a representation of one machine’s output. Its prediction should then track that output, subject to prediction errors.

A-FDT preserves these relationships in its decision hypotheticals. It does not preserve every statistical correlation. A medical condition correlated with my action need not track the output of my decision computation.

The guiding question is therefore:

> Which features of the modeled world would vary with this particular computational output?

This is not an instruction to imagine replacing one’s decision procedure with an arbitrary alternative. Predictors may specifically be predicting the original procedure. The intervention instead supposes that the **fixed procedure on fixed inputs** returns another result.

That supposition may be logically impossible. A deterministic mathematical function has only one value at a given input. A-FDT therefore needs **counterpossible** reasoning: structured evaluation of antecedents that may contradict mathematical fact.

The source treats the resulting hypotheticals as decision-making instruments, not ordinary beliefs about possible worlds. No physical signal travels backward in time when a hypothetical changes an earlier prediction. The agent is altering a representation of a computational dependence.

Nevertheless, this creates a substantial foundational problem. One cannot preserve every logical consequence of an impossible antecedent using unrestricted classical reasoning. A-FDT requires a selective account of what changes and what remains fixed. Equation (4) delegates that task to \(G\); it does not derive the required dependency structure.

## 3. An operational interpretation

For finite examples, a useful operational completion is to supply an acyclic structural model. This is a modeling proposal consistent with the paper’s examples, not a general solution established by the source.

Let \(S\) collect exogenous uncertainties with distribution \(\mu\), and let endogenous variables satisfy equations
\[
Z_i=h_i(\operatorname{pa}_i,S).
\]
Some equations describe physical mechanisms; others describe computations, simulations, or predictions.

To evaluate \(a\):

1. Replace the equation for \(D_x\) by \(D_x:=a\).
2. Retain the other equations and the distribution of \(S\).
3. Recompute variables downstream in the supplied dependency structure.
4. Calculate the resulting utility \(V_a(S)\).

Then
\[
Q_x(a)=\int V_a(s)\,d\mu(s),
\qquad
a^*\in\arg\max_a Q_x(a).
\]

Observation variables themselves may change during this recomputation. One must not subsequently discard hypothetical outcomes merely because their observations differ from the actual history \(x\).

A graph alone may be insufficient: response equations or equivalent probability kernels are needed, particularly for counterfactual configurations absent from the observational distribution. Thus the operational input must include more than a list of correlations.

The practical procedure is consequently:

- specify outcomes and utility;
- identify the exact computation being evaluated;
- model which actions, predictions, and observations depend on it;
- compare interventions on that computation’s output.

This makes explicit where disagreements can arise. Two analysts may accept the maximization rule yet disagree about the appropriate counterfactual model.

## 4. A-FDT in Newcomb’s problem and the smoking lesion

### Newcomb’s problem

An opaque box contains \(M\) if a predictor forecast one-boxing, and zero otherwise. A transparent box contains \(k\), available only through two-boxing.

Assume a specific prediction mechanism: under either intervention on the decision output, the predictor agrees with that output with probability \(p\). Then
\[
Q(\text{one-box})=pM,
\]
\[
Q(\text{two-box})=(1-p)M+k.
\]
A-FDT one-boxes exactly when
\[
(2p-1)M>k.
\]

With \(M=1{,}000{,}000\), \(k=1{,}000\), and \(p=0.99\), these values are \(990{,}000\) and \(11{,}000\).

The relevant structure is
\[
D\longrightarrow A,
\qquad
D\longrightarrow\text{Prediction}
\longrightarrow\text{Box contents}.
\]
These are dependency arrows, not necessarily forward-time causal arrows. The earlier prediction changes in the hypothetical because it represents the same computation being varied.

The assumption about \(p\) is stronger than an unspecified historical accuracy rate. Aggregate predictive success alone need not establish how a predictor behaves under each candidate intervention. Applying A-FDT requires this additional modeling judgment.

### The smoking lesion

In the smoking-lesion story, a lesion produces both a tendency to smoke and cancer risk, while smoking itself does not cause cancer. Smoking provides a utility benefit.

Here, intervening on the decision-output node does not alter the lesion or cancer mechanism:
\[
P(C\mid\operatorname{do}(D_x=\text{smoke}))
=
P(C\mid\operatorname{do}(D_x=\text{refrain})).
\]
Where the intervened computation controls the action, smoking therefore gains its enjoyment benefit without changing cancer risk.

The contrast with Newcomb’s problem is structural: a predictor represents the decision computation; a lesion does not.

The source’s detailed construction is more complicated than this summary. It allows the lesion to affect preferences, thereby selecting between computations with different model inputs. Intervention on one such computation changes action only in the circumstances where that computation controls it. The expected smoking benefit is correspondingly probability-weighted.

The authors also acknowledge that the lesion problem is contrived and that sophisticated versions of EDT have defenses. Its strongest lesson here is not a universal refutation of EDT, but the distinction between **a correlated common cause** and **a representation of a decision computation**.

## 5. A-FDT and observations that change in hypotheticals

Transparent Newcomb brings Equation (4)’s treatment of observations into focus.

The predictor fills the large box iff it predicts that the agent would one-box **upon seeing it full**. Define
\[
D_f=\operatorname{A\!-\!FDT}(P,G,\text{full}),
\qquad
D_e=\operatorname{A\!-\!FDT}(P,G,\text{empty}),
\]
where these expressions abbreviate represented-output variables.

The physical action is selected by the generated observation:
\[
A=
\begin{cases}
D_f,&B=\text{full},\\
D_e,&B=\text{empty}.
\end{cases}
\]

The predictor depends on \(D_f\), not necessarily on \(D_e\). Thus, when evaluating the full-box decision, changing \(D_f\) may change the prediction, the box contents, and which decision node controls the eventual action.

Let prediction accuracy be \(p\), and let \(q\) be the modeled probability that \(D_e\) two-boxes. Then
\[
Q_f(\text{one-box})
=pM+(1-p)qk,
\]
whereas
\[
Q_f(\text{two-box})
=(1-p)(M+k)+pqk.
\]

The first expression includes accurate predictions leading to a full box and one-boxing; prediction errors lead to an empty box, where \(D_e\) controls the action. The second reverses the prediction probabilities.

In this model, \(D_e\) two-boxes: intervening on it changes what happens when the box is empty but does not change the predictor’s forecast of \(D_f\). Hence \(q=1\). With the earlier numbers,
\[
Q_f(\text{one-box})=990{,}010,
\qquad
Q_f(\text{two-box})=11{,}000.
\]

A-FDT therefore one-boxes even while seeing a full box. Its two-boxing hypothetical usually contains an empty box and an empty-box observation.

This does not mean that the agent believes its actual observation was mistaken. Belief and decision hypothetical play different roles. The agent sees a full box, but evaluates what the whole modeled process would look like under another output of the computation responsible for responding to a full box.

Conditioning both alternatives on “the box remains full” would eliminate precisely this feature and would not implement Equation (4).

## 6. Cooperation, rescue, and blackmail

### A-FDT against a computational twin

In the source’s twin prisoner’s dilemma, mutual cooperation yields \(1{,}000{,}000\) to each player; mutual defection yields \(1{,}000\). Defecting against a cooperator yields \(1{,}001{,}000\), while cooperating against a defector yields zero.

If both players implement the same computation on equivalent inputs, then
\[
D=\text{cooperate}\Rightarrow(C,C),
\qquad
D=\text{defect}\Rightarrow(D,D).
\]
A-FDT cooperates because \(1{,}000{,}000>1{,}000\).

This is instrumental rather than altruistic reasoning. It also does not license cooperation with every opponent who calls themselves rational. Different information, preferences, or computations can break the dependency. Shared terminology is not computational identity.

### A-FDT in Parfit’s hitchhiker

A driver rescues a stranded agent only if the driver predicts payment after arrival. The relevant node is the computation for the **city observation**.

Changing that node from payment to refusal changes both the later payment and the earlier rescue prediction. Accordingly, A-FDT compares reliable rescue followed by a fee with likely abandonment when refusal is predicted. Under the source’s stakes and prediction accuracy, it pays upon arrival.

The city’s safety is real, but it is not held fixed across the decision hypotheticals. This explains the connection between A-FDT and behaving as though beneficial commitments were already binding.

### A-FDT in mechanical blackmail

Suppose a blackmailer launches a damaging process only when predicting that the agent will pay. Payment costs \(c\); refusing an initiated threat causes loss \(L\).

Let
\[
s_p=P(\text{threat launched}\mid
\operatorname{do}(D_{\text{letter}}=\text{pay})),
\]
\[
s_r=P(\text{threat launched}\mid
\operatorname{do}(D_{\text{letter}}=\text{refuse})).
\]
Assume no payment or damage without a threat. Then
\[
Q(\text{pay})=-s_pc,
\qquad
Q(\text{refuse})=-s_rL.
\]
A-FDT refuses when
\[
s_rL<s_pc.
\]

For \(s_p=1\), \(c=1{,}000\), \(L=1{,}000{,}000\), refusal is favored when \(s_r<0.001\). Thus refusal is not unconditional: enough mistaken or indiscriminate threats make payment preferable in this model.

Again, these probabilities are not conditioned on already holding the letter. They evaluate the entire threat-generating process under alternative outputs.

With a perfect predictor, a refusing A-FDT agent never receives the threat. Actually receiving one is therefore incompatible with those idealized assumptions. A fallible model makes the prescription non-vacuous; real-world application also requires uncertainty about the blackmailer’s strategy and competence.

## 7. What A-FDT determines—and what remains open

Three qualifications are especially important.

**Actions are not whole policies.** For fixed \(P,G\), A-FDT induces a mapping
\[
\pi(x)=\operatorname{A\!-\!FDT}(P,G,x).
\]
But Equation (4) evaluates an intervention on one input-indexed output \(D_x\). It does not automatically change every \(D_y\).

A **policy-selection formulation**, mentioned in the source’s footnotes 7 and 16, instead intervenes on a policy-valued output. The authors note possible differences in multi-agent problems. Its prescriptions should not silently be attributed to A-FDT. One can model policies as candidate actions in a new problem, but that requires specifying a new intervention target and its dependencies.

**Dependency discovery remains unsolved.** The paper explicitly identifies the construction of logical-dependency models as a major open problem. Equation (4) works given the appropriate structure; it supplies no general method for recognizing equivalent computations, evaluating imperfect simulations, or choosing which logical consequences survive an intervention.

For uncertain models, a reasonable additional proposal is
\[
Q_x(a)=\sum_m w_m
\mathbb E_m[V\mid\operatorname{do}(D_x^{(m)}=a)].
\]
This averages over candidate dependency mechanisms. It requires defensible weights and corresponding intervention targets; it is not a solution supplied by the paper.

**The baseline model matters.** A-FDT’s absence of conditioning on \(x\) requires an encompassing model of how observations arise. Simply substituting \(P(\,\cdot\mid X=x)\) can erase the observation-changing counterfactuals responsible for its distinctive recommendations. The source does not fully specify how to select this baseline or revise it after unexpected evidence.

Finally, the source’s performance claims are not general optimality theorems. Its examples support claims about cooperation, commitment, and resistance to extortion. But arbitrary environments can reward particular decision procedures, and the proposed class of “fair” problems remains incompletely formalized. Neither universal superiority nor unrestricted equivalence to ideal precommitment follows from Equation (4) alone.

## References

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2, especially §§3, 5–6, 9.
- Pearl, J. *Causality: Models, Reasoning, and Inference*. Cambridge University Press, 2000.
- Joyce, J. M. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.

## Conclusion

A-FDT evaluates actions by intervening on the represented output of the computation making the decision. It preserves dependencies with predictions and equivalent implementations while breaking merely evidential correlations. Crucially, its hypotheticals may change the observations that would occur. This gives a precise procedure once a suitable dependency model is supplied. The theory’s central unresolved challenge is supplying that model reliably, without assuming the desired recommendation in advance.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Planning for essay production**

I’m working on producing a substantive essay with a word count between 2400 and 3000. The target is around 2750 words. I have plenty of tokens left, about 28,000, but I need to keep an eye on my actual usage, which is closer to 11,000. I want to avoid bugs and ensure any numerical sources are accurate. If I use quotations, I'll remember to note them properly without cluttering the essay.**Discussing section five of Eq4**

I need to focus on section five of Eq4, ensuring consistent naming without using generic FDT except for the title. I’ll define D_x as a logical A-FDT output, which involves function f A-FDT(P,G,x) with clear variable distinctions. It’s important to model P without considering the posterior x and reference Quine’s limits regarding epistemic beliefs versus hypotheticals. I should provide examples, like Newcomb's problem and simplified scenarios involving preferences while being careful about accuracy guarantees and clear labeling.**Exploring D_empty action**

I want to clarify how D_empty changes action only during an empty event, where the box remains unmodified because the predictor uses the full input, not the empty state. When the hypothetical full state is active, it’s important to treat D_empty—not set to 'a'. I need to make it clear that the "input-indexed action" in a policy-cell isn't universally applicable; different inputs impact actions differently. Additionally, I should explain the inconsistencies in the blackmail model calculations and how I've noted typos regarding percentages, but I won't draw attention unless it’s necessary.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4ebd0596-9258-4454-b441-cc2e10eebed5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4ebd0596-9258-4454-b441-cc2e10eebed5/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: readable reasoning_details blocks joined in saved order.

```text
**Deciding on submission**

I'm thinking about whether to submit, as I realize there are no logical guarantees for cooperation. The same model doesn't seem sufficient, so I question if I'm missing information. However, I feel like I should just use my own judgment and go ahead and submit. I notice we have a total of 27k, but I've only used 2k, so there's no need for more in this instance.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4ebd0596-9258-4454-b441-cc2e10eebed5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4ebd0596-9258-4454-b441-cc2e10eebed5/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
