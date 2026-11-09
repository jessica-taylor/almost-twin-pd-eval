# A-FDT: Choosing the Output of a Decision Procedure

What should an agent do when another actor has already predicted its choice? Causal decision theory says to assess an action by its causal consequences. Evidential decision theory says to assess it by the evidence that taking it would provide. Action functional decision theory, or **A-FDT**, asks a different question: what would the world be like if the *decision procedure now being executed* returned one action rather than another?

This distinction matters when the procedure is represented elsewhere—for example, in a predictor’s simulation, or in another agent running the same computation. Changing the output in an A-FDT hypothetical can change the prediction or the other agent’s action, even when neither is causally downstream of the present physical act.

The central source is Yudkowsky and Soares’ *Functional Decision Theory: A New Theory of Instrumental Rationality*. For this essay, A-FDT denotes the action-level rule in their Equation (4), Section 5. The authors also mention a preferred policy-level formalization. That alternative is related, but it is not identical to the action-level rule and should not be substituted for it without further argument.

## 1. Three ways to evaluate an action

Let \(A\) be a finite set of available actions, \(X\) an observation variable, \(O\) an outcome, and \(U(O)\) the agent’s utility. A decision rule compares expected utilities of hypothetical outcomes:

\[
a^* \in \operatorname*{arg\,max}_{a\in A}
\sum_o P_a(O=o)\,U(o).
\]

The crucial question is how to construct \(P_a\), the distribution for the hypothetical in which \(a\) is selected.

**Evidential decision theory (EDT)** uses ordinary conditionalization:

\[
a_{\mathrm{EDT}}\in\operatorname*{arg\,max}_{a\in A}
\mathbb E[U(O)\mid X=x,\ \mathrm{Act}=a].
\]

It asks what taking \(a\) would indicate about the world. This expression requires the relevant conditional probabilities to be defined; in the paper’s formulation, actions assigned probability zero are excluded.

**Causal decision theory (CDT)** instead intervenes on the physical action:

\[
a_{\mathrm{CDT}}\in\operatorname*{arg\,max}_{a\in A}
\mathbb E[U(O)\mid \operatorname{do}(\mathrm{Act}=a),\ X=x].
\]

In a suitable causal model, the intervention replaces the equation determining the agent’s act, then recomputes its causal descendants. It does not change a predictor’s earlier prediction merely because that prediction and the act are correlated.

A-FDT also uses an intervention, but its target is not the physical act. It is a variable representing the output of the decision procedure on the relevant input.

## 2. The A-FDT rule

Write \(P\) for a probability model and \(G\) for a graph describing the dependencies used to construct hypotheticals. Let

\[
D_x := \mathsf{afdt}(\underline P,\underline G,\underline x)
\]

be a **variable inside the model** representing the output of the A-FDT procedure when supplied with \(P\), \(G\), and observation \(x\). The underlining indicates that the inputs identify the variable: it is a name for that computation’s output.

The action-level rule corresponding to Equation (4) is

\[
\boxed{
\mathrm{A\!-\!FDT}(P,G,x)
\in
\operatorname*{arg\,max}_{a\in A}
\mathbb E_{P,G}\!\left[
U(O)\mid \operatorname{do}(D_x=a)
\right].
}
\tag{A-FDT}
\]

For each candidate action, the agent:

1. Identifies the variable \(D_x\) representing this decision procedure’s output on the current input.
2. Intervenes to set \(D_x=a\).
3. Propagates that change through the dependencies represented in \(G\).
4. Calculates expected utility in the resulting hypothetical.
5. Outputs an action maximizing that expectation, using a specified tie-breaking rule if needed.

It is important to distinguish \(D_x\), a variable in the model, from \(\mathrm{A\!-\!FDT}(P,G,x)\), the action actually returned by the procedure. Self-reference enters because the model contains a representation of the computation using that model. Naming the computation does not require already knowing its output. The paper invokes techniques related to self-reproducing programs to argue that such representations are possible, although this does not by itself solve the more difficult problem of constructing correct counterfactual dependencies.

### What does the graph mean?

In an ordinary causal graph, an arrow typically represents a causal dependency. In A-FDT’s graph, arrows can also represent **subjunctive dependencies**: relationships that should persist when the output of a mathematical computation is varied in the hypothetical.

For example, a predictor’s model and the agent may both depend on the same computation:

\[
D_x \longrightarrow \mathrm{Act},
\qquad
D_x \longrightarrow \mathrm{Prediction}.
\]

The second arrow need not mean that the present act sends a signal into the past. It means that, in the model’s counterfactual evaluation, a different output of the computation is associated with a different prediction.

The paper’s rule assumes that \(G\) correctly represents such relationships. It does **not** provide a general algorithm for discovering them. In particular, ordinary statistical correlation alone is insufficient evidence for an A-FDT arrow, and an arbitrary arrow to anything one would like to influence would make the rule useless.

### Counterpossibilities, not ordinary possible worlds

If a deterministic computation on fixed inputs actually returns \(a_1\), then its returning \(a_2\) on those inputs is mathematically impossible. A-FDT nevertheless asks the agent to evaluate that antecedent. Its hypotheticals are therefore *counterpossible*: they selectively suppose a false mathematical claim while retaining relevant structure.

They are decision tools, not beliefs that arithmetic changes or that the agent can physically alter the past. Nor does the use of Pearl’s \(\operatorname{do}\) notation automatically supply a complete semantics for logical interventions. The paper explicitly treats the construction and justification of \(G\) as an open problem.

## 3. Newcomb’s problem: a prediction is not just a correlation

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains \$1,000,000 if a predictor predicted that the agent would take only the opaque box, and otherwise contains nothing. The prediction and filling have already happened.

Suppose, as a model assumption, that the predictor matches either candidate output with probability \(p=0.99\). The relevant graph makes both the actual act and the prediction depend on \(D_x\). Then A-FDT evaluates:

\[
\begin{aligned}
V(\text{one-box})
&=p\cdot \$1{,}000{,}000
=\$990{,}000,\\
V(\text{two-box})
&=(1-p)\cdot \$1{,}000{,}000+\$1{,}000
=\$11{,}000.
\end{aligned}
\]

It therefore one-boxes. With symmetric accuracy \(p\), one-boxing is preferred when

\[
p(1{,}000{,}000)>
(1-p)(1{,}000{,}000)+1{,}000,
\]

or \(p>0.5005\). This threshold depends on the stipulated symmetric error model; an overall historical accuracy figure alone need not establish the error rates under both interventions.

CDT, by contrast, holds the box contents fixed under an intervention on the present physical act. Taking the additional \$1,000 is then better whether the opaque box is full or empty. EDT ordinarily one-boxes when the action is sufficiently strong evidence about the prediction, though its result can depend on its priors.

The A-FDT explanation is neither “my action causes the predictor to fill the box” nor simply “one-boxing is good news.” It is that the predictor’s representation is linked to the same decision computation that produces the act. A counterfactual change to that computation propagates to both.

## 4. A-FDT and the smoking lesion

Now suppose an agent enjoys smoking by \$1,000 in utility. In this imaginary problem, smoking has no causal effect on cancer. A lesion independently produces a desire to smoke and raises the probability of cancer; it does not predict the decision procedure.

A naive EDT calculation can favor abstaining: smoking is evidence of the lesion and hence of cancer. Under the intended A-FDT model, however, intervening on the output of the decision procedure does not change the lesion or the cancer risk. If the probability of survival is \(s\) in both hypotheticals, then, in a simplified model,

\[
V(\text{smoke})=1{,}000+s(1{,}000{,}000),\qquad
V(\text{refrain})=s(1{,}000{,}000).
\]

A-FDT smokes.

This calculation is an idealization. The paper’s fuller model has different possible decision-function inputs corresponding to different preferences. If the lesion determines which input is in use, an intervention on one output may affect the act only in the cases where that input controls it. The paper accordingly obtains an advantage of \(p\cdot \$1{,}000\), where \(p>0\) is the probability of the relevant lesion state. The conclusion is the same: the lesion is not made more or less likely by the logical intervention.

The source also cautions that the smoking-lesion example is contrived. In a population of reflective agents, the assumed correlation between smoking and the lesion may not survive deliberation; some versions of EDT use additional “tickle” or ratification procedures to address it. The example illustrates the distinction between statistical and subjunctive dependence, not a universal proof that every EDT agent abstains.

## 5. Observation and the global hypothetical

A distinctive feature of Equation (4) is that the observation \(x\) selects *which output variable* is intervened on. Unlike the paper’s CDT equation, Equation (4) does not add a general condition \(X=x\) inside the expectation.

Thus an A-FDT agent who has observed \(x\) can evaluate an intervention on \(D_x\) using hypotheticals in which \(x\) is not observed. This is especially important when the event producing the observation depends on a prediction of what the agent would do *upon that observation*.

### Transparent Newcomb

Suppose the opaque box is now transparent. The predictor fills it if it predicts that the agent would one-box **upon seeing it full**. Let \(D_F\) be the output on seeing a full box and \(D_E\) the output on seeing an empty box.

Assume the predictor predicts \(D_F\) correctly with probability \(0.99\), and let \(q\) be the probability that \(D_E\) outputs two-box. Intervening on \(D_F\), Equation (4) gives:

\[
\begin{aligned}
V(D_F=\text{one})
&=0.99(1{,}000{,}000)+0.01q(1{,}000),\\
V(D_F=\text{two})
&=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first value is greater for every \(q\in[0,1]\), so A-FDT says to one-box upon seeing a full box. In the second hypothetical, the predictor usually predicts two-boxing, the box is empty, and the agent’s physical act is controlled by \(D_E\), not \(D_F\).

This is the striking implication: the agent sees a full box, yet one of the hypotheticals used to select its action mostly contains an empty box. The agent does not disbelieve its observation. It evaluates the output for that observation from a perspective that includes cases where the output affects whether the observation occurs.

There is a notational inconsistency in the source: one displayed expression in its transparent-Newcomb discussion appears to put \(\mathrm{Obs}=\mathrm{full}\) inside the intervention, while the subsequent calculation allows an empty observation. The calculation and surrounding explanation match Equation (4)’s lack of an additional observation condition. The latter is the interpretation used here.

### A practical distinction about evidence

Equation (4) should not be read as saying that observations never matter. They identify the computation \(D_x\), and evidence can also be reflected in the supplied model’s specification. But whether \(P\) is an earlier distribution, an already conditioned one, or contains some other representation of evidence can change the result. The paper’s transparent-box example requires a model in which intervening on \(D_F\) can change the probability of seeing the full box. Conditioning that possibility away in advance would not reproduce its calculation.

A useful operational discipline is therefore to record separately:

- evidence treated as fixed background in the model;
- the observation selecting the output node \(D_x\);
- observations that can themselves vary under the intervention.

That bookkeeping is an implementation proposal, not a fully specified rule supplied by the paper. It prevents an unnoticed “double update,” but deciding which evidence belongs in each category remains a substantive modeling question.

## 6. Twins, threats, and imperfect dependence

In the paper’s twin prisoner’s dilemma, two agents implement the same decision procedure on equivalent inputs. Mutual cooperation pays each \$1,000,000; mutual defection pays each \$1,000. A-FDT’s joint hypotheticals are

\[
D_x=\text{cooperate}\Rightarrow(C,C),\qquad
D_x=\text{defect}\Rightarrow(D,D).
\]

It cooperates. The reasoning does not apply merely because two people are similar: differing inputs, incentives, private information, or random seeds can weaken or eliminate the relevant link.

For a simple imperfect-twin model, suppose the other agent matches the candidate action with probability \(r\), regardless of which action is considered. Using the paper’s payoffs,

\[
\begin{aligned}
V(C)&=1{,}000{,}000r,\\
V(D)&=1{,}001{,}000(1-r)+1{,}000r.
\end{aligned}
\]

Cooperation is preferred when \(r>0.5005\). Again, this is a stipulated response model, not a consequence of knowing only that the two agents usually agree.

Consider also **mechanical blackmail**. A blackmailer starts a damaging program only if she predicts that the recipient would pay upon receiving a letter. If started, the program causes \$1,000,000 in damage unless the recipient pays \$1,000. Under a perfect prediction model, an A-FDT hypothetical in which the letter-response computation refuses is one in which the program is not started. The agent therefore refuses even upon receiving a letter—although, in the perfect model, receiving one while using that response is off the predicted path.

With prediction error, the answer depends on rates. For example, suppose paying leads to a letter and a \$1,000 payment with certainty, while refusal leads to an erroneous letter and \$1,000,000 loss with probability \(\varepsilon\). Then

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-\varepsilon\,1{,}000{,}000.
\]

Refusal is preferred when \(\varepsilon<0.001\). This illustrates why “A-FDT always refuses blackmail” is too broad: the prescription depends on how the threat responds to the decision function and on the costs and error rates. The source’s example compares \(\varepsilon=0.0009\), where refusal is preferred, with \(\varepsilon=0.00011\); the latter number would also favor refusal under its stated payoffs. A paying example would require an error rate above \(0.001\), such as \(0.011\).

## 7. Applying A-FDT to unfamiliar cases

A workable application begins with a model, not a slogan about acting as one would have precommitted.

1. **Define outputs and utilities.** Specify available actions, consequences, and whose utility is being maximized.
2. **Identify the computation.** State the input \(x\) and the output node \(D_x\). If other observations matter, include their output nodes separately.
3. **Model relevant dependencies.** Represent physical effects, predictors, copies, observations, and background variables. Explain why each changes—or does not change—when \(D_x\) changes.
4. **Supply intervention distributions.** For each candidate \(a\), specify the predictor’s behavior and other downstream outcomes under \(\operatorname{do}(D_x=a)\), including errors.
5. **Compute and compare expected utilities.** Do not automatically condition on the actual observation if doing so removes cases Equation (4) is intended to include.
6. **Stress-test the model.** Vary prediction accuracy and dependency assumptions; check whether the recommendation is robust.

The largest uncertainty is step 3. A proposed graph should be supported by an account of *how* a predictor, copy, or common computation relates to the agent. Merely saying “if I cooperated, others would too” is not enough. Conversely, ordinary causal independence is not enough to rule out a dependency between two executions of the same computation.

The paper’s authors prefer a formulation that selects a **policy**, a mapping from observations to actions. One can propose a policy-level rule by intervening on a variable representing an entire mapping \(\pi:x\mapsto a\), evaluating its world-level consequences, and executing \(\pi(x)\). That may help coordinate decisions across observations, but it requires specifying the policy space and its dependencies. It is not Equation (4), which directly compares actions at the selected output node; the two can differ, particularly in multi-agent settings.

## 8. Motivation and limits

The philosophical attraction of A-FDT is its global perspective. An agent cares about outcomes across the world, not only effects downstream of its body. Where predictors and copies respond to its decision procedure, those relationships can be relevant to choosing well. The paper argues that this explains success in Newcomb’s problem, cooperation with twins, and credible resistance to certain threats without costly precommitment.

Those successes are conditional on the models. No decision theory wins every constructed problem: an adversary can reward agents for following a particular theory. The paper proposes that A-FDT is promising on “fair” problems where outcomes depend on behavior in the problem rather than directly rewarding a decision procedure, but acknowledges that fairness and general optimality have not been formally established.

Nor does a representation theorem for expected utility prove that A-FDT’s counterfactual graph is correct. It shows, under appropriate axioms, that preferences can be represented by expected utility relative to an epistemic perspective; selecting that perspective remains the decision-theoretic dispute. Practical agents must additionally confront imperfect prediction, computational limits, uncertainty about their own implementation, and unresolved questions about logical counterfactuals.

## Conclusion

A-FDT evaluates actions by intervening on the output of the decision computation for the relevant input, then propagating that intervention through causal and other subjunctive dependencies. This yields one-boxing against a suitably reliable predictor, smoking in the stipulated lesion model, and cooperation with a sufficiently linked twin.

Its distinctive insight is that a decision can be connected to predictions and other computations without physically causing them. Its main unfinished task is equally clear: a general, justified method for constructing the dependency models on which its prescriptions rely.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially Sections 3–6 and Equation (4). https://arxiv.org/abs/1710.05060v2