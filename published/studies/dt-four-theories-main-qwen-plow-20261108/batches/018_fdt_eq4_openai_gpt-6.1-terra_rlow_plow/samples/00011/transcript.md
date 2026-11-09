# 018_fdt_eq4_openai_gpt-6.1-terra_rlow_plow / 00011

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/236d801c-88bd-42d1-bb1a-62cf486754f4/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/236d801c-88bd-42d1-bb1a-62cf486754f4/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: choosing the output of a decision procedure

Suppose a predictor has placed a million dollars in an opaque box if and only if she predicted that you would leave a separate, transparent box containing $1,000 untouched. Her prediction is already made. Should you take both boxes?

Causal decision theory (CDT) says to take both: your present action cannot causally alter the prediction or the box’s contents. Evidential decision theory (EDT), under the usual assumptions, says to take only the opaque box: one-boxing is strong evidence that it is full. Action functional decision theory (A-FDT) also recommends one-boxing, but for a different reason. It asks what the world would be like under different outputs of the *decision procedure now being executed*, including corresponding changes in accurate predictions of that output.

The distinction matters elsewhere. If a disease and a desire to smoke have a common cause, but smoking itself does not cause the disease, an action may be evidence of illness without the illness depending on the decision procedure’s output. A-FDT can therefore recommend one-boxing in Newcomb’s problem while also recommending smoking in the artificial “smoking lesion” problem.

This essay takes Equation (4) of Yudkowsky and Soares’s paper as the primary definition of A-FDT. The equation provides a concrete rule *given* a model of the relevant dependencies. It does not, by itself, tell us how to construct that model. That gap is both the main obstacle to applying the theory and an important part of its philosophical interest.

## 1. Expected utility and three kinds of hypothetical

Let \(\mathcal A\) be a finite set of actions, \(O\) an outcome, \(U(O)\) its utility, and \(x\) the agent’s observation history. Each theory chooses an action with maximal expected utility. Their disagreement concerns the probability distribution used to evaluate an alternative.

EDT evaluates an action as news:

\[
a_{\mathrm{EDT}}\in
\arg\max_{a\in\mathcal A}
\mathbb E[U(O)\mid X=x,A=a].
\]

It asks how desirable the outcome would be *conditional on learning* that the agent takes \(a\). This preserves every correlation represented in the conditional distribution, including correlations due merely to common causes.

CDT instead evaluates a physical intervention:

\[
a_{\mathrm{CDT}}\in
\arg\max_{a\in\mathcal A}
\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

In a causal model, \(\operatorname{do}(A=a)\) replaces the equation determining the physical action with the assignment \(A:=a\). Its causal descendants are recomputed; causes of the action and other nondescendants are not changed by that intervention.

For A-FDT, write

\[
D_x=\mathrm{afdt}(\underline P,\underline G,\underline x)
\]

for the *variable in the agent’s model* representing the output of the A-FDT procedure on the encoded inputs \(P,G,x\). It is important to distinguish \(D_x\), the model variable, from the actual output of the procedure. Adapting the source’s notation, its Equation (4) is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid \operatorname{do}(D_x=a)
\right].
}
\tag{1}
\]

Here \(P\) supplies probabilities, while \(G\) is intended to describe not only causal relations but also decision-relevant logical, computational, and other *subjunctive dependencies*. The intervention sets the modeled output \(D_x\) to \(a\), after which the model propagates its consequences through \(G\).

The difference from CDT is the intervention target. CDT changes an action token—this physical act. A-FDT changes a decision-function output type, which may be implemented or predicted in several places. The difference from EDT is that A-FDT does not simply condition on observing an action: it performs a model surgery intended to preserve some dependencies and break others.

For each \(a\), let \(P^{(a)}\) denote the distribution produced by this surgery. Then the practical calculation is simply

\[
Q_x(a)=\sum_o P^{(a)}(O=o)\,U(o),
\qquad
a^*\in\arg\max_a Q_x(a).
\]

The difficult part is not the maximization. It is specifying \(P^{(a)}\).

### What happens to the observation?

Equation (1) does **not** add \(X=x\) as an ordinary conditioning event. Instead, the observation selects the node \(D_x\) to intervene on. In a hypothetical where that output differs, the agent may not receive \(x\) at all. The source emphasizes this distinction in transparent Newcomb and blackmail cases.

This does not mean that evidence has no role: different observations select different decision-function outputs, and the model can represent evidence and its effects. But blindly conditioning on the complete actual observation *as well as* intervening on \(D_x\) changes Equation (1) and can change its answer. Some information may reasonably be built into the model’s background distribution; deciding which information belongs there is an additional modeling issue, not a consequence of the equation alone.

## 2. Subjunctive dependence and counterpossibilities

The source calls a relation *subjunctive dependence* when the relevant hypothetical variation of one fact calls for a corresponding variation of another. Ordinary causal effects are included: if a calculator’s displayed output changed, a scribe copying it would write something different. But two separate, reliable calculations of the same function can also be linked even when neither causes the other.

A predictor may simulate or otherwise accurately reason about your decision procedure. If the procedure’s output were different, the predictor’s representation would tend to give a different answer too. The dependency is not a signal traveling from your future action into the past. It is a proposed constraint on the hypothetical used to assess the procedure’s output.

Not every correlation deserves such treatment. A lesion may affect both a person’s tastes and their cancer risk without computing the output of their decision procedure. If the procedure’s output is varied, the lesion need not vary. A-FDT’s central modeling demand is therefore:

> Preserve dependencies that would track the decision-function output under the relevant hypothetical; do not preserve a correlation merely because it appears in observational data.

This is easier to state than to implement. For a fixed deterministic function and fixed inputs, only one output is mathematically correct. If that output is \(a_1\), the supposition \(D_x=a_2\) is not an ordinary possible-world alternative; it is a *counterpossibility*. Classical conditioning on a known false logical claim is unavailable. Equation (1) supplies a graph-based surrogate: override the relevant variable and propagate through the supplied dependencies.

The paper explicitly leaves open how to infer such a graph, or even whether Pearl-style graphical machinery can represent all the needed logical relationships satisfactorily. Self-reference is also present: the procedure refers to a model variable representing its own output on that model. The paper points to self-representing programs as evidence that such reference need not be inherently incoherent. That does not establish that every proposed dependency graph or self-referential maximization is well defined.

## 3. A-FDT in Newcomb’s problem

Assume the predictor gets the agent’s action right with probability \(r=0.99\) under **each** contemplated output. This action-specific assumption is stronger than a bare report that 99% of past predictions were correct: aggregate accuracy alone need not tell us how prediction behaves under each intervention.

Let \(D\) be the decision output, \(B\in\{\text{full},\text{empty}\}\) the opaque box, and \(A\) the physical action. An A-FDT model contains dependencies of the schematic form

\[
D\longrightarrow A,\qquad
D\longrightarrow \text{prediction}\longrightarrow B,
\qquad
(A,B)\longrightarrow U.
\]

The first arrow says that the agent implements the output; the second represents the predictor’s tracking of it. Under the stipulated symmetric error model,

\[
P^{(\text{one})}(B=\text{full})=0.99,\qquad
P^{(\text{two})}(B=\text{full})=0.01.
\]

Thus

\[
Q(\text{one})=0.99(1{,}000{,}000)=990{,}000,
\]

\[
Q(\text{two})=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

A-FDT one-boxes. More generally, for symmetric accuracy \(r\), one-boxing is preferred exactly when

\[
r\,1{,}000{,}000>
(1-r)\,1{,}000{,}000+1{,}000,
\]

or \(r>0.5005\).

CDT’s physical-action intervention holds the already filled or empty box fixed, and two-boxing gains $1,000 in either case. EDT can reach the A-FDT answer by conditioning on action, but it reaches it through evidential association rather than the modeled dependency of prediction on the decision output.

The hypothetical distributions are not claims that the agent can physically refill a box by thinking. Nor are they ordinary beliefs that both mathematical outputs are possible. They are decision tools: A-FDT chooses the output associated with the higher-utility modeled hypothetical.

## 4. A-FDT, common causes, and the smoking lesion

Now suppose, in an imaginary world, smoking has no causal effect on cancer. A lesion both increases the desire to smoke and raises cancer risk. If smoking gives the agent $1,000 in utility, and survival is worth $1,000,000, a simplified A-FDT model gives

\[
Q(\text{smoke})=1{,}000+1{,}000{,}000(1-p),
\]

\[
Q(\text{refrain})=1{,}000{,}000(1-p),
\]

where \(p\) is the cancer probability under either decision-output intervention. Smoking wins.

The point is not that correlations between acts and lesions are impossible. It is that a lesion can be upstream of the mechanism selecting or supplying inputs to a decision procedure without being downstream of the particular procedure-output variable on which A-FDT intervenes. Changing that output does not, by itself, change the lesion.

The source’s fuller model is subtler than the simple equations. It considers two possible preference inputs, one associated with the lesion and one without it. Intervening on the decision output for the smoking-preferring input affects behavior only when that input is active. If its probability is \(p\), the advantage is \(p\cdot \$1{,}000\), rather than necessarily the full $1,000. The sign remains positive under the stipulated assumptions.

The paper also cautions that the classic smoking-lesion setup is contrived: a fully specified agent population and an accurate model of the agent’s own preferences and behavior may undermine the correlations attributed to EDT. EDT variants using additional introspective information can also smoke. The example illustrates a distinction between statistical and functional dependence; it is not, by itself, a decisive empirical test of decision theories.

## 5. Observation-dependent decisions: transparent Newcomb

In transparent Newcomb, the predictor fills the million-dollar box if she predicts that the agent would one-box *on seeing it full*. Now the actual agent sees a full box. CDT and ordinary EDT, conditioning on that observation, prefer the extra $1,000. Equation (1) instead intervenes on the output \(D_F\) for the full-box observation.

To see how, introduce another output \(D_E\), governing behavior if the box is empty. Assume:

- the prediction of \(D_F\) is correct with probability \(0.99\);
- the box is full exactly when the prediction is “one-box”;
- if the box is empty, the probability of taking both boxes is \(q\).

Intervening on \(D_F=\text{one}\) gives

\[
Q_F(\text{one})
=0.99(1{,}000{,}000)+0.01q(1{,}000)
=990{,}000+10q.
\]

The second term matters: when the predictor errs, the box is empty and \(D_E\), not \(D_F\), controls the physical act.

Intervening on \(D_F=\text{two}\) gives

\[
Q_F(\text{two})
=0.01(1{,}001{,}000)+0.99q(1{,}000)
=10{,}010+990q.
\]

The first value is larger for every \(q\in[0,1]\), so A-FDT one-boxes upon seeing a full box.

This calculation is global in a specific sense. The intervention concerns the answer the procedure gives *if it sees full*. In the two-box hypothetical, the predictor usually predicts that answer, leaves the box empty, and the agent consequently sees empty instead. The actual full observation selects \(D_F\); it is not held fixed in every hypothetical.

That is a controversial feature, not a mathematical trick that everyone must accept. A critic may insist that once the box is visibly full, the relevant question holds that fact fixed. A-FDT’s reply is that doing so discards a dependency between the decision output and the earlier prediction. The source regards the ability to act as one would have preferred to precommit as evidence for its approach, but the disagreement is precisely about which hypothetical is appropriate.

## 6. A-FDT in games and threats

A-FDT’s dependence structure also matters when another agent acts simultaneously. Suppose two perfect psychological twins play a prisoner’s dilemma. Each gets $1 million if both cooperate and $1,000 if both defect; unilateral defection gains the defector a further $1,000 while the cooperator gets nothing.

If both implement the same decision function on equivalent inputs, an intervention on its output changes both acts:

\[
Q(\text{cooperate})=1{,}000{,}000,\qquad
Q(\text{defect})=1{,}000.
\]

A-FDT cooperates. This does **not** imply cooperation with every opponent. If the opponent’s action does not track the relevant output, holding it fixed may make defection preferable. Similar reasoning, public claims of similarity, or a high historical correlation are evidence to investigate—not automatic proof of a perfect shared computation.

The source’s mechanical blackmail example makes the role of probabilities especially clear. A predictor starts a damaging program only if she predicts that the agent would pay $1,000 upon receiving a demand. If started, the program causes $1 million in damage unless payment stops it.

Consider the following simplified model: a payer is blackmailed with probability one, while a refuser is blackmailed by mistake with probability \(\varepsilon\). Then

\[
Q(\text{pay on demand})=-1{,}000,\qquad
Q(\text{refuse on demand})=-\varepsilon\,1{,}000{,}000.
\]

A-FDT refuses when \(\varepsilon<0.001\), and pays when \(\varepsilon>0.001\). At equality the options tie. Thus refusal is not an unconditional command to resist threats: it depends on how strongly the blackmailer’s decision tracks the response, the error rate, and the relative losses.

If a demand actually arrives despite a low error probability, the refusal hypothetical still includes mostly cases in which no demand arrives. That is the same observation-handling feature seen in transparent Newcomb. In the actual mistaken-blackmail case, refusal causes the large loss. The source nevertheless favors the rule because the output that refuses tends to deter the threat.

## 7. Applying A-FDT when the graph is not given

For an unfamiliar problem, Equation (1) can guide a disciplined modeling exercise, but it cannot manufacture the missing dependency facts. A reasonable operational proposal—not a complete algorithm supplied by the paper—is:

1. **Specify the decision output.** Identify the observation history \(x\), available outputs, and the procedure whose output is represented by \(D_x\). Distinguish this node from physical action.
2. **Model outcome mechanisms.** Include ordinary causal consequences, payoffs, uncertainty, and which observations activate which decision outputs.
3. **Identify potential trackers.** For each predictor, copy, or similar agent, ask what computation or information makes its behavior vary with \(D_x\). Model imperfect tracking explicitly.
4. **Separate correlations from dependencies.** Ask whether a variable changes under the *output intervention*, not merely whether it is correlated with action. Common causes and independently generated noise may remain fixed.
5. **Evaluate every intervention.** Propagate each candidate output through the model, including cases where another observation—and hence another output node—governs action.
6. **Test sensitivity.** Vary uncertain graph edges, prediction error rates, priors, and payoff estimates. Report when the recommended action changes rather than treating one speculative graph as established.

A useful local approximation is a response kernel

\[
K(z\mid a)
=
P^{(a)}(Z=z),
\]

where \(Z\) summarizes predictors’ and other agents’ responses to the output intervention. This makes uncertainty about imperfect dependencies explicit. But \(K(z\mid a)\) is an **interventional modeling assumption**: it cannot generally be estimated just by substituting the observed conditional \(P(Z=z\mid A=a)\). Nor does the source give a universal method for learning it.

Policies require a further distinction. A policy \(\pi:\mathcal X\to\mathcal A\) specifies an action for each observation. The paper notes that its authors prefer a formulation that selects policies, but Equation (4) selects an action-indexed output \(D_x\). One may study a policy-level analogue,

\[
\pi^*\in\arg\max_\pi
\mathbb E[U(O)\mid\operatorname{do}(\Pi=\pi)],
\]

where \(\Pi\) represents a policy output. This can coordinate choices across observations, but it requires specifying a different intervention variable and its dependencies. It should not be silently substituted for Equation (1), particularly in multi-agent settings where the paper acknowledges that the distinction can matter.

Finally, graph uncertainty and bounded computation can be substantial. Copies may receive different inputs; predictors may use shortcuts; randomized actions may or may not share random bits with their predictions. A graph that links all “similar” agents too strongly can manufacture cooperation or deterrence that the environment does not support. Conversely, omitting a genuine predictor can reproduce CDT-like failures. These are not cosmetic details: they determine the hypothetical distributions.

## 8. Motivation and limits

The paper’s philosophical case is that a good decision procedure should perform well from a global perspective, including environments that predict or replicate its reasoning. It argues that causal dominance is not neutral here: two-boxing dominates only when the predictor’s earlier output is held fixed as the physical action changes. Under A-FDT hypotheticals, the prediction changes with the decision output.

The authors do not claim that A-FDT beats every possible rival in every possible environment. A predictor could explicitly reward another procedure or punish A-FDT. They suggest that the relevant comparison is instead on “fair” problems whose rewards depend on behavior in the problem rather than on the agent’s identity or performance elsewhere. They also acknowledge that fairness and general optimality are not formally established.

Similarly, claims that A-FDT has nonnegative value of information or always acts as it would have precommitted should be read as motivations and proposed properties, not as consequences proved for every implementation of Equation (1). They depend on the model, the available policies, how information is represented, and the unresolved counterfactual semantics.

## Conclusion

A-FDT evaluates an action by intervening on the output of the decision procedure for the current observation, then propagating that intervention through a model of causal and noncausal dependencies. This explains both its distinctive successes in predictor and coordination problems and its most surprising implication: a hypothetical for an observed situation may include worlds in which that observation never occurs.

The rule is precise once its probability distribution and dependency graph are supplied. Constructing and justifying that graph—especially for imperfect predictors and counterpossible logical outputs—remains the central open problem.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially §§3–6. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/8dfab357-8ba2-4194-b79d-2b64cb814088/call_0/request.json)

[Authoritative raw response](../../../../../../runs/8dfab357-8ba2-4194-b79d-2b64cb814088/call_0/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
**Analyzing decision-making structure**

I need to choose different inputs since uniform outputs won’t work. An essay cautions against policy switching. I'm considering how interventions create distinct outputs, even with similar scenarios; there's no straightforward tracking beyond shared reasoning. I realize that differing data might lead to similar judgments, but the essay points out the difference between specific actions versus shared reasoning. The intervention influences the entire output rather than just the underlying reasoning process. It seems like there's a defect in understanding this.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/8dfab357-8ba2-4194-b79d-2b64cb814088/call_1/request.json)

[Authoritative raw response](../../../../../../runs/8dfab357-8ba2-4194-b79d-2b64cb814088/call_1/response.raw) · finish: `stop`

### Visible response

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
