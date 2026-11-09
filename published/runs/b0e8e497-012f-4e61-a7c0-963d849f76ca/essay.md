# A-FDT: deciding by intervening on a decision function

What should a decision-maker hold fixed when comparing actions? In an ordinary choice, the answer may seem obvious: compare what happens if you take each action. But that instruction leaves open which other features of the world change with the action.

Suppose a reliable predictor has already filled a box if and only if she predicted that you would take only that box. Your taking two boxes cannot physically change what the predictor did yesterday. Nevertheless, if she predicted your decision by reasoning accurately about you, a hypothetical in which your decision procedure outputs “take both” may also be a hypothetical in which she predicted that output.

**Action functional decision theory**, or **A-FDT**, takes that dependence seriously. It evaluates actions by intervening not directly on the physical act, but on the mathematical output of the decision procedure producing it. It then propagates the intervention through a model of everything that depends on that output, whether causally or through prediction, shared computation, or another relevant relationship.

This essay uses Equation (4) of Yudkowsky and Soares’s paper as the formal statement of A-FDT. The paper calls its theory FDT; the name *A-FDT* here emphasizes that the equation selects an action. The authors also mention a preferred policy-based formulation, but do not provide a complete general formalization of it. That distinction matters when applying the theory to new cases.

## 1. Three ways to evaluate an action

Let \(A\) be an action, \(X=x\) an observation history, \(O\) an outcome, and \(V=U(O)\) its utility. An expected-utility decision rule chooses an action maximizing an expression of the form

\[
\sum_o U(o)\,Q_a(o),
\]

where \(Q_a\) is a probability distribution over outcomes in the hypothetical associated with action \(a\). The central disagreement is how to construct \(Q_a\).

**Evidential decision theory** (EDT) uses ordinary conditional probabilities:

\[
\operatorname{EDT}(P,x)
\in \arg\max_a \mathbb E_P[V\mid X=x,A=a].
\]

It asks what taking an action would be evidence of. In the paper’s equation, an action with conditional probability zero is excluded, since the conditional expectation is undefined.

**Causal decision theory** (CDT), in the paper’s graphical presentation, uses a causal intervention:

\[
\operatorname{CDT}(P,G,x)
\in \arg\max_a
\mathbb E_P[V\mid \operatorname{do}(A=a),X=x].
\]

Here \(G\) describes causal relationships. Setting \(A=a\) changes the physical act and its causal consequences, while severing influences into the action node.

For **A-FDT**, write

\[
D_x=\operatorname{afdt}(\underline P,\underline G,\underline x)
\]

for the *node in the model* representing the output of the A-FDT procedure on these particular inputs. Underlining indicates that the inputs identify the node: \(D_x\) is not itself the output, but a variable representing it. Equation (4), renamed as required here, is

\[
\boxed{
\operatorname{A\!-\!FDT}(P,G,x)
\in\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[V\mid\operatorname{do}(D_x=a)\right].
}
\tag{A}
\]

The graph \(G\) is now richer than a causal graph: it must encode decision-relevant logical, computational, predictive, and causal dependencies. An intervention sets \(D_x\) to a candidate output, cuts its incoming dependencies, and propagates the value through the specified downstream relationships.

Two features deserve emphasis.

First, the intervention concerns a **function-output type**, not merely this particular physical action token. If a predictor’s simulation and the agent’s body both depend on \(D_x\), both may change in the hypothetical. A physical intervention on the agent’s arm would not generally do that.

Second, unlike the displayed CDT equation, (A) does **not** additionally condition on \(X=x\). The observation selects *which output node* is intervened on. If changing that output would change what is predicted and consequently what is observed, the hypothetical may contain an observation other than \(x\). This is not a typographical omission to be repaired by automatically adding \(X=x\); it is central to the paper’s treatment of transparent Newcomb problems.

The distributions used in these calculations are **hypotheticals**, not necessarily the agent’s beliefs about what actually happened. The agent can believe that a box is full while evaluating a counterfactual distribution in which it is probably empty.

## 2. What does “depends on the output” mean?

The paper calls the relevant relationship **subjunctive dependence**. Causal dependence is one example: if a person copies a calculator’s answer, what she writes depends causally on the displayed output. But two separate calculators evaluating the same expression can also agree because they implement the same mathematical computation, even without communicating.

Similarly, two agents executing the same deterministic decision procedure on the same input have the same output. A sufficiently accurate predictor need not literally run an identical program: she might instead reason well enough about the procedure to predict its answer. In either case, the paper treats the prediction as depending on the output.

This is not a rule to preserve every observed correlation. A lesion might both create a desire to smoke and cause cancer. Smoking and cancer could then be correlated even though cancer does not depend on the decision procedure’s output. In the appropriate A-FDT graph, changing that output changes the act but does not change whether the lesion exists.

Nor does A-FDT require backward physical causation. A prediction made yesterday and an action taken today can depend on a common computation. The graph’s arrow from a decision-output node to a prediction expresses a dependency in the *model used for deliberation*, not a signal traveling into the past.

There is, however, a philosophical cost. If a deterministic procedure on fixed inputs actually outputs \(a\), then its outputting a different \(b\) is mathematically impossible. Equation (A) therefore asks for a **counterpossible**: what follows under an antecedent contrary to a logical fact? The paper does not give a general semantics for such counterpossibles. Instead, it assumes a graph describing how to propagate the stipulated change.

That assumption is substantial. Pearl-style surgery is a useful notation once the relevant structure is given, but ordinary causal discovery does not by itself tell us how to construct a graph of logical dependencies. Self-reference adds another issue: the procedure must represent its own output. The paper notes that self-referential representations can be constructed using standard recursion techniques; this does not, on its own, solve the harder problem of computing all the right counterfactual consequences.

## 3. Newcomb’s problem: a predictor rather than a lesion

In Newcomb’s problem, a transparent box contains \$1,000. An opaque box contains \$1 million if a predictor predicted that the agent would take only the opaque box, and nothing otherwise. Assume the predictor matches either candidate output with probability \(p\), independently of the candidate, and utility is linear in dollars.

In the A-FDT model, the output node \(D\) influences both the act and the prediction. Thus

\[
\begin{aligned}
\operatorname{EU}(\text{one box}) &= p(1{,}000{,}000),\\
\operatorname{EU}(\text{two boxes}) &= (1-p)(1{,}000{,}000)+1{,}000.
\end{aligned}
\]

One-boxing is preferred when

\[
p>\frac{1}{2}+\frac{1{,}000}{2{,}000{,}000}
=0.5005.
\]

At \(p=0.99\), the respective values are \$990,000 and \$11,000. The numerical result depends on the *counterfactual* reliability model: an observed 99% accuracy across some population does not automatically establish 99% accuracy under each intervention on this particular decision procedure.

CDT instead holds the already-filled box fixed under a physical action intervention. Two-boxing adds \$1,000 whether the opaque box is full or empty, so CDT chooses both. EDT normally one-boxes when its nonzero-probability conditional model makes one-boxing strong evidence that the box is full. A-FDT arrives at the same choice as EDT here, but for a different reason: it preserves the predictor’s dependence on the computation rather than every statistical correlation with the act.

Now consider the imaginary **smoking lesion** case. Smoking brings 1,000 units of pleasure, but does not cause cancer; a lesion causes both a smoking tendency and cancer. In a simplified model, if survival has probability \(s\) under both interventions, then

\[
\operatorname{EU}(\text{smoke})=1{,}000{,}000s+1{,}000,\qquad
\operatorname{EU}(\text{refrain})=1{,}000{,}000s.
\]

A-FDT smokes because the lesion is not a predictor of the procedure in the relevant sense. Naive EDT may refrain if smoking is sufficiently bad news about the lesion.

The paper itself cautions that a fully specified lesion example is awkward: preferences, self-knowledge, and the agent’s probability model must be made consistent. Refined EDT responses can also smoke. The lesson is therefore about the kind of dependency being modeled, not a claim that every evidential decision-maker necessarily gets every lesion problem wrong.

## 4. Twin agents and partial dependence

Consider a prisoner’s dilemma with a perfect psychological twin. Both cooperate: each receives \$1 million. Both defect: each receives \$1,000. If one defects while the other cooperates, the defector gets \$1,001,000 and the cooperator gets nothing.

If both agents implement the same decision function on the same relevant input, the A-FDT graph connects their actions to the same output node. The comparison is then

\[
\operatorname{EU}(C)=1{,}000{,}000,\qquad
\operatorname{EU}(D)=1{,}000,
\]

so A-FDT cooperates. The agent does not claim that her button physically controls her twin’s button. She treats both as outputs of the computation being evaluated.

Exact identity is a strong assumption. Suppose instead that, under an intervention setting the agent’s output to \(C\), the other cooperates with probability \(r_C\), while under an intervention setting it to \(D\), the other cooperates with probability \(r_D\). Then

\[
\begin{aligned}
Q(C)&=r_C(1{,}000{,}000),\\
Q(D)&=r_D(1{,}001{,}000)+(1-r_D)(1{,}000).
\end{aligned}
\]

A-FDT cooperates precisely when the first quantity is larger. If \(r_C=r_D\), defection is better; if \(r_C=1\) and \(r_D=0\), cooperation is better. This parametrization is an operational illustration, not a dependency-learning rule supplied by the paper. The difficult work is estimating these **interventional** probabilities rather than substituting an observed resemblance between agents.

## 5. Observations that may change in the hypothetical

The distinctive observation treatment becomes clearest in **transparent Newcomb**. Both boxes are visible. The predictor fills the large box if she predicts the agent would leave the \$1,000 behind *upon seeing it full*. Let

\[
D_F=\text{output on seeing a full box},\qquad
D_E=\text{output on seeing an empty box}.
\]

The prediction depends on \(D_F\). The eventual act depends on whichever output corresponds to the observation actually generated.

Suppose prediction is correct with probability \(0.99\), and let \(q\) be the probability that \(D_E\) says to take both boxes. On seeing a full box, A-FDT intervenes on \(D_F\), but does not condition every hypothetical on the box remaining full:

\[
\begin{aligned}
Q(D_F=\text{one})&=990{,}000+0.01q(1{,}000),\\
Q(D_F=\text{two})&=0.01(1{,}001{,}000)+0.99q(1{,}000).
\end{aligned}
\]

The first wins for every \(q\in[0,1]\). In the second hypothetical, the predictor will usually predict two-boxing, leaving the large box empty; the agent then sees the empty box and \(D_E\), rather than \(D_F\), controls her physical act.

That result can be unsettling. The agent *actually sees* a full box, yet the hypothetical used to decide what to do upon that sight usually contains an empty box. This follows from Equation (A)’s specified intervention, not from denial of the observation. Adding an ordinary condition that the box is full would produce a different rule and, in this example, a different answer.

The same structure appears in **Parfit’s hitchhiker**. A driver rescues a stranded agent only if she predicts that the agent will pay after reaching town. In the paper’s model, A-FDT pays in town because its output on that observation affects whether the driver predicted payment and offered the ride. This is a claim about a specified predictive setup, not a general theorem that A-FDT honors every promise regardless of costs or predictability.

## 6. A-FDT and policies

A policy is a mapping \(\pi:x\mapsto a\). The paper says that its authors prefer a version that selects policies, although Equation (A) selects an action-output node. These should not be silently treated as the same algorithm.

An action-node intervention can have policy-like consequences. In transparent Newcomb, setting \(D_F\) changes a standing disposition to act on a particular observation, even in hypothetical runs where that observation never occurs. But \(D_E\) remains a separate node. A policy intervention would instead set a node representing an entire mapping, potentially changing multiple branches together.

As an **additional proposal**, one could model a policy version by defining a policy-output node \(\Pi\) and comparing

\[
\arg\max_{\pi}\mathbb E[V\mid \operatorname{do}(\Pi=\pi)],
\qquad A=\pi(X).
\]

This is useful when predictors inspect several branches or when coordination depends on an entire strategy. It is not determined by Equation (A): one must specify the policy space, how the predictor responds to policies, what observations are inputs, and how the policy-selection procedure represents itself. In particular, optimizing a whole policy jointly need not give the same answer as separately optimizing each action-output node.

## 7. A practical construction procedure—and its limits

For an unfamiliar case, Equation (A) suggests the following workflow.

1. **Specify the decision and utility.** List candidate outputs, relevant observations, outcomes, and utility—including costs of information, prediction errors, and future consequences.
2. **Identify the output node.** Represent the output of this procedure on the current model and observation. Distinguish that node from the physical action it may cause.
3. **Build dependency mechanisms.** Include causal effects, genuine copies, simulations, predictions, and their error mechanisms. Do not add an edge merely because two variables are correlated.
4. **Construct each hypothetical.** Set the output node to a candidate, propagate through the graph, and calculate expected utility. Allow the observation to change if the graph makes it downstream of the intervention.
5. **Check the model’s assumptions.** Vary prediction accuracy, shared randomness, inputs, and utilities. Report where the preferred action changes.

A useful **proposed operational interpretation** is to use explicit structural equations with exogenous noise. For example, a predictor node might equal \(D_x\) except when an independent error bit is one. Holding the distribution of that error bit fixed across interventions produces the Newcomb calculation above. This makes assumptions inspectable and supports sensitivity analysis.

But the proposal does not solve the general problem. It presupposes that we know which structural equations remain valid under a counterpossible change to a computation. Predictors may use source-code inspection, partial simulation, or evidence correlated with inputs; their error rates may differ across outputs. Multiple computations may be logically related without being identical. If randomness is involved, one must ask whether predictor and agent share a random seed or use independent draws. Incorrectly treating independent random choices as copies can manufacture nonexistent coordination.

There is also a question about the input distribution \(P\). Equation (A) does not give a complete recipe for deciding which background information is already incorporated into \(P\), which is represented by the observation input \(x\), or how to avoid inadvertently conditioning twice. For a concrete model, these choices must be stated and checked against the intended graph.

## 8. Why favor A-FDT?

The paper’s motivation is instrumental: a decision procedure should be evaluated partly by the outcomes agents using it attain. A procedure that predictably one-boxes can obtain a filled box; one that predictably pays the driver can obtain a ride. In such cases, an agent following CDT might wish beforehand to bind herself to act differently later. A-FDT aims to produce that useful disposition without requiring a separate binding device.

The argument is not that A-FDT wins every conceivable contest. A predictor could reward agents specifically for following CDT or punish agents specifically for following A-FDT. The paper calls problems “fair” when outcomes depend on behavior in the dilemma rather than directly rewarding a favored decision procedure, and suggests that A-FDT performs especially well in such problems. It explicitly leaves a satisfactory formal definition of fairness, and a general optimality theorem, open.

The paper also argues that A-FDT assigns nonnegative value to information because an agent can disregard information and act as it would have precommitted to act. That is an important motivation, but Equation (A) alone does not establish the claim for arbitrary graphs, observation mechanisms, computational costs, or policy spaces. Likewise, in a particular fixed hypothetical model, a candidate that is pointwise worse than another under an appropriate common coupling cannot have higher expected utility. Which coupling and dependencies are appropriate is precisely the disputed issue; calling an action “dominated” does not independently settle it.

## Conclusion

A-FDT evaluates a candidate action by asking what a model would look like if the decision function on the relevant input output that action. Its distinctive move is to propagate this intervention through predictive and computational dependencies, not merely through the physical consequences of an act.

This gives clear answers in idealized models of predictors and twins, and explains why observations themselves can vary across decision hypotheticals. Its central unresolved task is equally clear: constructing and justifying the dependency model that makes those hypotheticals meaningful. A-FDT is therefore both a decision rule conditional on a supplied graph and a research program for discovering which graph should be supplied.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially Sections 3–6. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).