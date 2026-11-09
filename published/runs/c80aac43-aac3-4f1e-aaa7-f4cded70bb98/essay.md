# A-FDT: Choosing the Output of a Decision Function

A decision can be both a physical event and the output of a computation. Usually the distinction makes little difference: if an agent picks up a glass, the decision function outputs “pick up,” the hand moves, and water is drunk. But the distinction matters when other systems predict, copy, or otherwise track the agent’s reasoning.

**Action functional decision theory (A-FDT)** evaluates an action by asking what the world would be like if the agent’s decision function, on its present inputs, returned that action. The hypothetical changes not only the agent’s physical act but also things that depend on that output in the relevant computational or logical sense. It need not change things merely correlated with the act.

This essay takes Equation (4), Section 5 of Yudkowsky and Soares’s paper as the primary definition. The paper calls the theory “FDT”; here, **A-FDT** names its action-output formulation. The paper also mentions a preferred formulation that chooses whole policies, but does not fully develop it. The difference matters when comparing the behavior prescribed at different observations.

## 1. What is being maximized?

Let \(\mathcal A\) be a finite set of actions, \(O\) an outcome, and \(U(O)\) its utility. An expected-utility decision rule assigns each action \(a\) a hypothetical distribution \(Q_a\) over outcomes and chooses

\[
a^*\in\arg\max_{a\in\mathcal A}\mathbb E_{Q_a}[U(O)].
\]

The central disagreement between decision theories is how to construct \(Q_a\).

**Evidential decision theory (EDT)** uses ordinary conditional probability:

\[
Q_a^{\mathrm{EDT}}(O=o)
=P(O=o\mid X=x,A=a),
\]

where \(X=x\) is the observation history. EDT asks, in effect, what news it would be to learn that the agent takes \(a\). This formula requires care when \(P(A=a\mid X=x)=0\).

**Causal decision theory (CDT)** instead considers an intervention on the physical action:

\[
Q_a^{\mathrm{CDT}}(O=o)
=P(O=o\mid \operatorname{do}(A=a),X=x).
\]

In a causal model, this operation replaces the mechanism determining \(A\) with the constant \(a\), then propagates its consequences along causal paths. A predictor’s earlier prediction is normally not a causal descendant of the later action, so CDT does not change that prediction merely because it changes \(A\).

A-FDT intervenes on a different variable. Let \(P\) be the probability component of a world-model, \(G\) a graph encoding relevant dependencies, and \(x\) the observation history. Write

\[
D_x=\mathsf d(\underline P,\underline G,\underline x)
\]

for the **variable in the model** representing the output of A-FDT on those inputs. The underlines indicate that the inputs identify a variable; \(D_x\) is not itself the algorithm’s computed answer. Equation (4), in the notation used here, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_{P,G}\!\left[
U(O)\mid\operatorname{do}(D_x=a)
\right].
}
\tag{1}
\]

Thus A-FDT replaces the modeled output of its decision function by \(a\), propagates the change through the supplied graph, evaluates expected utility, and returns an optimizing action.

Two details are essential. First, the intervention is on the output of **this decision function on these inputs**, not on the proposition that the agent has adopted some unrelated function. Second, Equation (1) does not additionally condition on \(X=x\): the observation enters by selecting the node \(D_x\). The consequences of that choice will be significant.

The paper treats the resulting hypothetical distributions as tools for decision-making, not as beliefs that the intervention has physically happened. A-FDT does not claim that thinking about an alternative sends a signal backward in time.

## 2. Subjunctive dependence and counterpossibilities

The paper calls the relevant relation **subjunctive dependence**. Causal dependence is one example: if a scribe writes down a calculator’s output, her writing depends on that output. But two calculators accurately evaluating the same expression can also agree without either causing the other’s result. Likewise, a prediction made yesterday can track the output of a decision procedure executed today.

Mere correlation is insufficient. A lesion might influence both a desire to smoke and the development of cancer. It does not follow that changing the output of a decision procedure changes whether the lesion exists or whether cancer develops. A-FDT therefore needs a distinction between:

- correlations explained by a dependency that should survive an intervention on \(D_x\);
- correlations that should be broken by that intervention.

That distinction is supplied by \(G\), not derived automatically from the observational distribution \(P\). A graph can include the agent’s action as a descendant of \(D_x\), a predictor’s estimate as another descendant, and ordinary consequences of both further downstream. It can leave a lesion or an independent random event outside those paths.

The intervention is philosophically unusual. If a deterministic computation on fixed inputs actually returns \(a_1\), it cannot literally return \(a_2\) on those same inputs. Evaluating \(\operatorname{do}(D_x=a_2)\) therefore involves a **counterpossible**: a hypothetical contrary to a mathematical fact. Ordinary Bayesian conditioning on a known false mathematical proposition is not enough to specify what should follow.

The paper proposes graph surgery as a practical formal surrogate: replace one structural equation and retain the others. It does **not** provide a general method for discovering the correct graph, or prove that every logical dependence can be represented satisfactorily in a Pearl-style graph. That is its central implementation gap. Self-reference is a separate issue: an algorithm can in principle refer to a representation of its own output without first knowing that output. Such self-reference does not, by itself, solve the counterpossible-reasoning problem.

## 3. A-FDT in Newcomb’s problem

A predictor fills an opaque box with \(\$1{,}000{,}000\) if she predicts that the agent will take only that box. Otherwise she leaves it empty. A transparent box contains \(\$1{,}000\), available if the agent takes both boxes. Assume utility is linear in these amounts.

For a simple A-FDT model, let \(D\in\{1,2\}\) represent the decision output and let the predictor match it with probability \(r=0.99\), independently of the modeled output. The agent’s act follows \(D\). Then

\[
\begin{aligned}
V(1)&=0.99(1{,}000{,}000)=990{,}000,\\
V(2)&=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\end{aligned}
\]

A-FDT one-boxes. The predictor is represented as tracking \(D\), so changing \(D\) changes the prediction and hence the box’s contents in the hypothetical.

By contrast, CDT holds the already-filled or already-empty box fixed under an intervention on the physical act. Whatever probability \(p\) CDT assigns to a full box,

\[
V_{\rm CDT}(2)=V_{\rm CDT}(1)+1{,}000,
\]

so it two-boxes. EDT also normally one-boxes in this setup, but because one-boxing is evidence of a favorable prediction, not because it performs the A-FDT intervention.

The numerical conclusion depends on more than a bare claim that a predictor has been right 99% of the time. The calculation assumes a particular **counterfactual error model**: changing the decision output preserves the 99% matching mechanism. An observed success rate alone need not establish how prediction accuracy would change under both hypothetical outputs, especially for unusual agents or rare actions. Constructing that model is part of applying A-FDT, not a consequence of the argmax formula.

## 4. Why a lesion is different

In the smoking-lesion problem, smoking is pleasurable and does not cause cancer. A lesion causes both an inclination to smoke and a high cancer risk. A simplistic EDT model can make smoking bad news about the lesion and therefore prescribe abstention.

In an A-FDT model where changing the decision-function output affects smoking but not the lesion or cancer,

\[
V(\text{smoke})-V(\text{refrain})=1{,}000
\]

for an agent whose utility gains that amount from smoking. A-FDT smokes: its intervention does not treat the statistical association as a mechanism by which smoking prevents or produces cancer.

This simple equation assumes the intervened-on decision output controls the act in the relevant modeled cases. The paper explores a subtler construction in which the lesion changes which of two decision functions, associated with different preferences, is implemented. Intervening on one output then changes the act only in the cases where that function controls it; the advantage is \(p\cdot1{,}000\), where \(p\) is the probability of the lesion. The sign remains positive.

The paper also cautions that the smoking-lesion example becomes contrived when fully specified. An EDT agent with adequate self-knowledge may avoid the problematic correlation through a “tickle” defense, and a population of agents who all reason identically may not have the assumed smoking pattern. The example illustrates the distinction between statistical and subjunctive dependence; it is not, by itself, a universal refutation of EDT.

## 5. Observations that can change in the hypothetical

The most distinctive implication of Equation (1) appears when the current observation is itself downstream of a prediction about the current decision.

In **transparent Newcomb**, the predictor fills the opaque box if she predicts that the agent would one-box *upon seeing it full*. Let \(D_F\) be the output of A-FDT on the observation “full,” and \(D_E\) its output on “empty.” The predictor tracks \(D_F\). Which output controls the actual act depends on which box state is observed.

When the agent sees a full box, Equation (1) selects \(D_F\) for intervention. But the hypothetical generated by \(\operatorname{do}(D_F=a)\) can contain an empty box, in which case the physical act is governed by \(D_E\), not by the intervened-on node. The hypothetical asks what happens if the **full-observation computation** outputs \(a\), not simply what happens if the physical agent takes \(a\) while still seeing a full box.

Let the predictor match \(D_F\) with probability \(0.99\), and let \(q\) be the probability that the agent two-boxes on seeing an empty box. Then

\[
\begin{aligned}
V(D_F=1)&=990{,}000+10q,\\
V(D_F=2)&=10{,}010+990q.
\end{aligned}
\]

The first value is higher for every \(q\in[0,1]\), so A-FDT one-boxes when it sees a full box. Upon seeing an empty box, the choice does not affect the prediction of \(D_F\), and taking the extra \(\$1{,}000\) is preferable in this model.

This is an intentionally global comparison. It does not deny that the agent actually sees a full box. Rather, it permits the *hypothetical* associated with a different output of \(D_F\) to have a different observation.

There is a notational tension in the source: one displayed expression in its transparent-Newcomb discussion appears to put \(\mathrm{Obs}=\mathrm{full}\) inside the intervention. Its subsequent calculation, however, includes empty-box branches. Equation (4) itself has no such observation intervention. The calculation above follows Equation (4) and the paper’s verbal explanation, rather than forcing the observation to remain full.

The same structure appears in **Parfit’s hitchhiker**. A driver rescues an agent only if she predicts the agent will pay after reaching town. In the paper’s model, A-FDT pays in town because the output “pay” is linked to being rescued, whereas the hypothetical output “refuse” is linked to being left in the desert. CDT and ordinary EDT, conditional on already being in town, see payment as an avoidable cost. Whether one accepts A-FDT’s prescription turns partly on whether one accepts this global counterpossible comparison after the observation has occurred.

## 6. A-FDT, threats, and prediction error

Consider a blackmailer who starts a damaging program only if she predicts that the agent would pay \(\$1{,}000\) upon receiving a demand. Once started, the program causes \(\$1{,}000{,}000\) in damage unless payment is made. Assume, for a deliberately simple model:

- a payer is blackmailed with probability \(1\);
- a refuser is mistakenly blackmailed with probability \(\epsilon\);
- there are no other costs or benefits.

A-FDT evaluates the output at the demand observation as

\[
V(\text{pay})=-1{,}000,\qquad
V(\text{refuse})=-\epsilon\,1{,}000{,}000.
\]

It refuses precisely when \(\epsilon<0.001\). If \(\epsilon=0.0009\), the expected loss under refusal is \(\$900\), so refusal wins even if the agent actually receives the demand. If \(\epsilon=0.0011\), the expected loss is \(\$1{,}100\), so payment wins.

The threshold is model-dependent. If the blackmailer sometimes targets known refusers anyway, or never receives payment despite starting the program, those probabilities must enter the calculation. “Never pay blackmail” is not an A-FDT axiom. Nor is the predictor’s accuracy unconditional evidence for a particular intervention response.

The paper uses this kind of example to motivate A-FDT as a substitute for costly precommitment: an agent who would refuse is less attractive to a predictor-based blackmailer. But the conclusion is controversial precisely because the refusal may be prescribed after a demand has arrived and the damaging program is already running.

## 7. Using A-FDT on unfamiliar problems

Given a candidate model, the following procedure makes Equation (1) operational. The steps for constructing the model are a proposed practical interpretation, not a complete algorithm supplied by the paper.

1. **Specify the decision and its inputs.** List feasible actions, observation history \(x\), outcomes, and utilities. Identify the modeled output \(D_x\). State how ties are broken.

2. **Draw ordinary causal structure.** Include physical actions, observations, predictors, payoffs, and relevant environmental variables. Specify mechanisms and exogenous uncertainty, not merely a table of correlations.

3. **Add proposed subjunctive links.** Ask which other outputs would track \(D_x\): a literal copy on the same input, a predictor’s simulation, or an imperfect approximation. Record the assumed error mechanism. Do not add links merely because two actions are similar or correlated.

4. **Perform each output intervention.** Replace the equation for \(D_x\) by \(D_x=a\), recompute its descendants, and retain unaffected mechanisms. In particular, allow observations downstream of predictions to change when the model says they depend on \(D_x\).

5. **Calculate and compare utilities.** Use the full hypothetical outcome distribution, including branches where the current observation does not occur or \(D_x\) does not control the physical act.

6. **Test the assumptions.** Vary predictor accuracy, model structure, and the treatment of uncertain links. If plausible models disagree, report that the prescription is model-sensitive rather than presenting a single answer as a theorem of A-FDT.

For instance, in a prisoner’s dilemma against an exact psychological twin implementing the same function on the same input, one intervention can set both outputs. With the paper’s payoffs, cooperation gives \(\$1{,}000{,}000\) and defection gives \(\$1{,}000\), so A-FDT cooperates. Against a merely similar stranger, that equality is not established. The appropriate model might assign a weaker response to the intervention, and cooperation would then depend on payoffs and the strength of that response.

This is also why policy talk must be handled carefully. A policy \(\pi\) maps observations to actions; Equation (1), by contrast, intervenes on one output \(D_x\). The paper’s footnotes describe a preferred policy-output formulation, but do not give a full operational definition. As an additional proposal, one might introduce a node representing an entire policy and maximize over policy outputs before applying the selected policy to \(x\). Doing so requires assumptions about which policy alternatives are available, how predictors respond to them, and how outputs at different observations are linked. It is not automatically equivalent to the action-by-action rule above.

## 8. What remains unsettled

A-FDT’s appeal is that it preserves dependencies that physical-action interventions discard while refusing to preserve every statistical correlation. The paper argues that this produces better outcomes in a range of predictor, coordination, and extortion problems. Its broader claim is more tentative: it proposes “fair” problems, in which rewards depend on the agent’s behavior in the problem rather than directly on its decision-theory label, but does not provide a complete formal fairness criterion or a proof that A-FDT outperforms rivals on all such problems.

Several questions remain open:

- **Graph identification.** Observed correlations and predictor accuracy do not uniquely determine counterpossible dependencies.
- **Logical consistency.** Local graph surgery can represent useful counterpossibles, but a general account of which mathematical relationships to retain is missing.
- **Randomization.** A predictor may track an algorithm’s distribution without tracking a genuinely independent random draw. The model must distinguish these cases.
- **Dynamic consistency and information.** The paper argues that its approach behaves like desirable precommitment and assigns non-negative value to information. Those are motivations and claims about its intended behavior, not general theorems established by Equation (1) alone for arbitrary graphs and sequential settings.
- **Computational limits.** A realistic agent cannot enumerate all actions and exact world-models. Approximation may alter both its decisions and others’ ability to predict them.

These limitations do not make the rule empty: a sufficiently specified graph yields definite calculations. But they limit what can be inferred from a verbal description alone.

## Conclusion

A-FDT evaluates an action by intervening on the modeled output of the decision computation, then propagating its causal and other subjunctive consequences. This explains its one-boxing, cooperation with an exact twin, and sensitivity to prediction-based threats without treating every correlation as controllable.

Its strength and its difficulty are the same: the answer depends on which dependencies the counterfactual model preserves. Equation (4) gives a decision rule once that structure is supplied; a general method for constructing and validating the structure remains open.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, version 2, especially Sections 3–6. [arXiv:1710.05060](https://arxiv.org/abs/1710.05060).