# A-FDT: choosing the output of a decision procedure

Action functional decision theory, or **A-FDT**, begins with a shift in perspective. An agent considering what to do is not merely choosing a physical movement while holding fixed everything outside its causal future. It is also an implementation of a decision procedure. Other processes—copies, predictors, or agents reasoning in the same way—may depend on what that procedure outputs.

A-FDT asks the agent to compare hypothetical outputs of its own procedure, allowing their consequences to propagate through these dependencies. The resulting counterfactuals can differ both from ordinary causal interventions and from conditioning on the agent’s action as evidence.

This essay takes Equation (4) of Section 5 of Yudkowsky and Soares’s *Functional Decision Theory* as the formal definition of A-FDT. The paper calls its theory “FDT”; the name **A-FDT** here emphasizes that the equation selects an action. The authors also mention a preferred policy-selection formulation, but do not give it the same detailed formal treatment. The distinction matters when different observations or multiple agents are involved.

## 1. Three ways to evaluate an action

Let \(\mathcal A\) be a finite set of actions, \(O\) an outcome, and \(U(O)\) its utility. A decision theory needs, for each \(a\in\mathcal A\), an expected utility of the form

\[
Q(a)=\sum_o P_a(O=o)\,U(o).
\]

The difficult term is \(P_a\): what distribution should represent the hypothetical in which the agent chooses \(a\)?

**Evidential decision theory (EDT)** uses conditional probability:

\[
Q_{\mathrm{EDT}}(a)
=\mathbb E[U(O)\mid X=x,A=a],
\]

where \(X=x\) is the observation history. EDT asks what choosing \(a\) would be evidence about. In the paper’s formulation, actions with zero conditional probability are excluded.

**Causal decision theory (CDT)** instead uses a causal intervention:

\[
Q_{\mathrm{CDT}}(a)
=\mathbb E[U(O)\mid \operatorname{do}(A=a),X=x].
\]

Here the intervention replaces the causal mechanism determining the agent’s physical action with the constant \(a\). Effects of that action are recomputed, while variables not causally downstream are not changed by the intervention.

A-FDT uses a different intervention target. It asks what follows from the output of the *decision computation* being \(a\). A predictor’s earlier prediction may vary in that hypothetical even though the physical action cannot send a signal into the past. Conversely, an unrelated common cause need not vary merely because it is statistically associated with the action.

The paper describes these imagined scenarios as computational tools constructed from the agent’s model, not as beliefs that the agent can physically rewrite the past or alter mathematics.

## 2. The A-FDT equation

Let \(P\) be a probability model and \(G\) a graph encoding the relevant dependencies. Write

\[
D_{P,G,x}
\]

for a **variable in the model** representing the output of A-FDT when run on inputs \(P,G,x\). It is important to distinguish this variable from the actual output of the algorithm: the variable is an object in the model that can be manipulated in a hypothetical.

The paper’s Equation (4), expressed using the assigned name, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in
\underset{a\in\mathcal A}{\arg\max}\;
\mathbb E_{P,G}
 \left[U(O)\mid
 \operatorname{do}\!\left(D_{P,G,x}=a\right)\right].
}
\tag{1}
\]

For each candidate \(a\), replace the model’s mechanism for \(D_{P,G,x}\) with the constant \(a\), propagate the consequences through \(G\), and calculate expected utility. Select a maximizing action. A complete implementation also needs a tie-breaking rule.

The graph \(G\) is broader than an ordinary causal graph. It is meant to encode computational and logical dependencies as well as causal ones. For example, both the physical action and a predictor’s estimate may depend on \(D_{P,G,x}\):

\[
D_{P,G,x}\longrightarrow A,\qquad
D_{P,G,x}\longrightarrow \text{Prediction}
\longrightarrow \text{Outcome}.
\]

The arrows do not all mean physical causation. The first can represent the body implementing the computation; the second can represent a predictor accurately modeling its output.

There is self-reference here: the procedure singles out a variable representing its own output on its own inputs. That does not by itself require the procedure to know the output in advance. The paper appeals to self-representing programs as an analogy. But self-representation does **not** solve the harder problem of constructing a correct graph of logical dependencies.

### Observation is handled unusually

Equation (1) contains no further condition \(X=x\) outside the intervention. Instead, \(x\) selects *which decision-output node* is intervened on. If the agent sees a full box, it evaluates changes to \(D_{P,G,\text{full}}\); if it sees an empty box, it evaluates changes to \(D_{P,G,\text{empty}}\).

Consequently, a hypothetical produced by intervening on the “full observation” output can include worlds in which the agent instead sees an empty box and executes the other decision computation. This is central to the paper’s transparent-box and blackmail examples.

The paper’s later transparent-box display appears to put an observation inside the intervention, but its actual calculations allow the observation to change. Taking Equation (4) as primary, the coherent reading is therefore that the observation identifies the intervened-on output, rather than being held fixed throughout the hypothetical. Adding an ordinary condition on \(X=x\) would generally give a different rule.

This does not mean that observations are useless. They determine which computation the agent is performing and can affect its model. The difficult implementation question is **which information belongs in the background model and which is allowed to vary in an intervention**. The paper illustrates that distinction but does not supply a general construction for every decision problem.

## 3. Subjunctive dependence and counterpossibilities

The paper calls the relevant relationship **subjunctive dependence**. Two correct calculators computing the same sum need not communicate, but their answers are related through the calculation they perform. Similarly, two implementations of the same decision computation on the same inputs may produce the same output without either causing the other.

Subjunctive dependence includes ordinary causal dependence: if a person copies a calculator’s answer, what they write depends on the answer. It also includes some noncausal computational relationships. Mere correlation, however, is not enough. A lesion that causes both a desire to smoke and cancer is not, just for that reason, computing the output of the agent’s decision procedure.

For a deterministic procedure on fixed inputs, there is only one actual output. Thus at least one candidate in Equation (1) generally asserts something mathematically false. A-FDT therefore requires **counterpossible** reasoning: reasoning under an antecedent contrary to a logical or computational fact.

One cannot simply condition a logically omniscient probability distribution on a false mathematical statement. The paper instead assumes that \(G\) is supplied and uses graph surgery to construct the desired hypothetical. That is a formal placeholder for the dependence structure, not a general algorithm for discovering it.

Nor is the required hypothetical simply “replace my algorithm with another algorithm.” If a predictor is modeling the original algorithm, changing only the agent’s implementation while leaving the predictor’s model unchanged can destroy the dependency A-FDT is meant to represent. The question is how the prediction and other modeled computations would vary with the output of *this* computation.

## 4. Newcomb’s problem

A transparent box contains \$1,000. An opaque box contains \$1,000,000 if a predictor predicted that the agent would take only the opaque box; otherwise it is empty. Suppose the prediction matches the output under each candidate intervention with probability \(p\), and prediction errors flip the result.

For A-FDT, the hypothetical values are

\[
Q(\text{one box})=p\cdot 1{,}000{,}000,
\]

\[
Q(\text{two boxes})=(1-p)\cdot 1{,}000{,}000+1{,}000.
\]

Thus A-FDT one-boxes precisely when

\[
p>0.5005.
\]

At \(p=0.99\), the values are \$990,000 and \$11,000 respectively. The paper’s example has a typographical arithmetic error in one earlier EDT calculation; \$990,000 is the value implied by 99% and \$1,000,000.

CDT two-boxes in the standard causal model: whatever the opaque box already contains, taking the transparent box adds \$1,000. EDT ordinarily one-boxes when the correlations and nonzero action probabilities are as specified, because one-boxing is evidence that the predictor filled the box.

A-FDT’s reason for one-boxing is different from EDT’s. Its graph says that the predictor’s estimate depends on the decision computation. Intervening on that computation changes the prediction in the hypothetical. This is not a claim that taking a box physically changes a past event.

The threshold also illustrates a practical warning: an empirical statement that a predictor is “99% accurate” over some population does not automatically establish \(p=0.99\) under **both** of the relevant interventions. Accuracy may differ by candidate action, input, or agent. Those intervention-specific response rates are extra modeling assumptions.

## 5. The smoking lesion contrast

In the imaginary smoking-lesion problem, a lesion produces both a preference for smoking and a high risk of fatal cancer. Smoking itself does not cause cancer, and smoking is worth 1,000 utility to an agent who likes it.

If \(r\) is the probability of surviving cancer and the utility of survival is 1,000,000, then in a simplified model where the current agent values smoking positively,

\[
Q_{\mathrm{A\!-\!FDT}}(\text{smoke})
=1{,}000{,}000r+1{,}000,
\qquad
Q_{\mathrm{A\!-\!FDT}}(\text{refrain})
=1{,}000{,}000r.
\]

The lesion and cancer do not respond to an intervention on the decision output, so A-FDT smokes. A simple EDT model can instead treat smoking as bad news about the lesion and refrain. CDT also smokes, since smoking has no causal effect on cancer.

This simplified calculation assumes that the intervened-on output controls the action in every modeled state and that smoking has the stated positive utility throughout. The paper’s more elaborate model distinguishes two possible utility functions, selected according to whether the lesion is present. There, intervening on the positively smoking-valuing decision procedure affects the physical action only in the lesion states, so the expected advantage is \(p_L\cdot1{,}000\), where \(p_L\) is the lesion probability.

The paper itself cautions that the smoking-lesion setup is contrived: maintaining the relevant correlation for an EDT agent can require uncertainty about the agent’s own preferences or procedure. It also notes EDT “tickle” or ratification responses. The example’s main value is conceptual: **an action–outcome correlation should not automatically be preserved as a decision-relevant computational dependency.**

## 6. Twins, observations, and conditional decisions

### A-FDT against a twin

Two prisoners each receive \$1,000,000 if both cooperate and \$1,000 if both defect. Unilateral defection gains the defector \$1,001,000 and leaves the cooperator with nothing.

If the opponent is an exact implementation of the same relevant computation on the same inputs, A-FDT compares

\[
Q(C)=1{,}000{,}000,\qquad Q(D)=1{,}000,
\]

and cooperates. Its cooperation does not causally force the twin’s action; both actions depend on the shared computation.

But similarity must be modeled, not assumed. If \(s_C\) is the probability the opponent cooperates under the cooperate intervention, and \(s_D\) the corresponding probability under the defect intervention, then

\[
Q(C)=1{,}000{,}000s_C,
\]

\[
Q(D)=1{,}001{,}000s_D+1{,}000(1-s_D).
\]

Cooperation follows only when the first value is larger. Shared training, a friendly demeanor, or membership in the same group does not establish the necessary response probabilities.

### Transparent Newcomb under A-FDT

Now suppose both boxes are transparent, and the predictor fills the large box according to what the agent would do **upon seeing it full**. Let \(D_F\) be that output and \(D_E\) the output upon seeing it empty. Suppose the predictor correctly predicts \(D_F\) with probability \(0.99\), and let \(q\) be the probability that \(D_E\) two-boxes.

Intervening on \(D_F=\text{one box}\) gives

\[
Q_F(\text{one})=990{,}000+10q.
\]

With probability \(0.99\), the box is full and the agent one-boxes; with probability \(0.01\), it is empty and \(D_E\) governs the action.

Intervening on \(D_F=\text{two boxes}\) gives

\[
Q_F(\text{two})=10{,}010+990q.
\]

The first value is greater for every \(q\in[0,1]\). Thus, on seeing a full box, A-FDT one-boxes. On seeing an empty box, the prediction does not depend on \(D_E\) in this setup, so taking the extra \$1,000 is preferable.

The striking feature is that the hypothetical for changing the *full-box computation* can make the box empty. It does not say that the agent failed to observe a full box in reality; it says that Equation (1) evaluates that computation’s alternative outputs across scenarios in which the observation need not stay fixed.

Parfit’s hitchhiker has the same structure in the paper’s model. A driver rescues someone only if she predicts that they will pay after arrival. A-FDT pays upon arrival when the benefit of being predictably willing to pay outweighs the cost. This prescription is controversial precisely because, conditional on having arrived, payment appears avoidable. A-FDT evaluates the output of the arrival-contingent computation rather than holding the rescue fixed.

## 7. Policies and a practical interpretation

The reference authors say their preferred formalization selects **policies**, mappings from observations to actions. Equation (1), however, selects the output associated with a particular input \(x\). These should not be conflated.

A policy variant might introduce a variable \(\Pi\) representing a whole mapping \(\pi:\mathcal X\to\mathcal A\) and calculate

\[
\pi^*\in\arg\max_{\pi}
\mathbb E[U(O)\mid\operatorname{do}(\Pi=\pi)],
\qquad
A=\pi^*(x).
\]

This is a useful extension, but it requires additional assumptions: which policies are admissible, which agent or predictor computations depend on \(\Pi\), and how changing one policy entry affects the others. Optimizing a whole policy jointly need not equal intervening on one action-output node while holding other outputs fixed.

For applying **A-FDT itself** to a new case, the following is a practical interpretation of Equation (1), not a complete algorithm supplied by the paper:

1. **Specify the decision and utility.** Identify the current input \(x\), feasible outputs, outcomes, and utility function.
2. **Model the environment.** Include causal effects, observations, predictor errors, other agents, and relevant sources of randomness.
3. **Identify the intervention node.** Represent the output of the current decision computation on its particular inputs. Add separate nodes for computations on other observations where needed.
4. **State dependency assumptions.** For each candidate output, specify how predictors, copies, observations, and physical actions respond. Preserve genuine common causes that do not depend on the computation.
5. **Propagate each intervention.** Replace the chosen output node by \(a\), recompute its modeled descendants, and average utility—including branches where a different observation causes a different computation to control the action.
6. **Compare and stress-test.** Choose the greatest expected value, then vary uncertain dependencies and error rates to see whether the result is robust.

The fourth step is the hard one. A graph that simply declares a desirable opponent response has not justified it. When dependency is uncertain, one reasonable proposal is to average the intervention values over explicitly weighted models of the dependency. That is a modeling choice beyond Equation (1), and it will inherit the uncertainty and possible misspecification of those models.

## 8. What the examples establish—and what they do not

The paper argues that A-FDT’s global perspective often produces the behavior an agent would have wanted to precommit to: one-boxing, paying the hitchhiker’s driver, and sometimes refusing blackmail. It also claims that information has non-negative expected value under the theory. Those are motivations and claims, not consequences of Equation (1) alone for arbitrary graphs. A general value-of-information result, for example, would require a specified comparison of information structures and available decision procedures.

Nor does A-FDT always refuse threats. In the paper’s mechanical blackmail setup, suppose paying upon receiving a threat costs \$1,000 and makes a predictor certainly send it; refusing costs \$1,000,000 only if the predictor mistakenly sends it, with probability \(\varepsilon\). Refusal has expected loss \(1{,}000{,}000\varepsilon\), versus \$1,000 for payment. It is preferred only for \(\varepsilon<0.001\). If the threat is not actually responsive to predictions, the calculation changes again.

The paper proposes that decision theories be compared on “fair” problems, roughly those rewarding or penalizing behavior in the problem rather than an agent’s decision theory by name. It explicitly leaves a precise fairness criterion open and acknowledges that any theory can be defeated by specially constructed environments. High utility in the examples is evidence for its proposal, not a universal dominance theorem.

Finally, graph surgery is not automatically a satisfactory theory of logical counterfactuals. Different graphs can encode different answers to the very question at issue; loops, imperfect simulations, private randomization, and correlations between prediction errors can make construction difficult. The paper identifies learning the relevant subjunctive structure as a central open problem.

## Conclusion

A-FDT evaluates an action by intervening on the output of the decision computation that would produce it, then tracing the modeled causal and computational consequences. This explains why it can one-box against a predictor, cooperate with a genuine twin, and smoke in the stipulated lesion problem without treating every correlation alike.

Its power and its uncertainty have the same source: the graph of subjunctive dependencies. Given a justified graph, Equation (1) is a concrete expected-utility rule. Determining that graph—and deciding how its counterpossible interventions should behave in unfamiliar cases—remains an essential part of applying the theory, not a problem the equation itself has solved.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially Sections 3–6. https://arxiv.org/abs/1710.05060v2