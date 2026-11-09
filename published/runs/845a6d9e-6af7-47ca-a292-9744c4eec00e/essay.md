# Action Functional Decision Theory: A Guide to A-FDT

Action functional decision theory (A-FDT) is a decision theory that tells an agent to choose by asking:

> Which output of this very decision procedure would yield the best outcome?

The reference paper calls this theory functional decision theory, or FDT; in this essay I use the assigned name **A-FDT** throughout. A-FDT is presented as an alternative to evidential decision theory (EDT) and causal decision theory (CDT). EDT asks, “Which action would be best news to learn that I performed?” CDT asks, “Which physical action causes the best outcome?” A-FDT instead treats the agent’s decision as the output of a fixed mathematical function and asks which output of that function would produce the best world.

The primary formal statement of A-FDT, for this essay, is Equation (4) of Section 5 of the source paper:

\[
\FDT(P,G,x) \coloneqq \argmax_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do\bigl(\FDTvar(\underline P,\underline G,\underline x)=a\bigr)\right].
\]

Renaming the theory for this essay, we can write:

\[
\boxed{
\text{A-FDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb E\!\left[V \mid \Do\bigl(D_x=a\bigr)\right]
}
\]

where \(D_x\) is a variable in the agent’s model representing the output of the A-FDT decision procedure when run on inputs \((P,G,x)\). The underlines in the source indicate a quotation/dequotation device: \(D_x\) is not the algorithm itself, but a variable whose name encodes the algorithm, model, graph, and observation history. The source notes that this self-reference is harmless in principle; one can construct self-representing data structures using Kleene’s recursion theorem.

The purpose of this essay is to explain what this equation means, how A-FDT evaluates actions and policies, how it handles dependencies and counterfactuals, and what remains unspecified in the source.

---

## 1. The decision-theoretic setting

A-FDT is an expected utility theory. The agent has:

- a finite set of possible actions \(\mathcal A\);
- a countable set of possible outcomes \(\mathcal O\);
- a utility function \(\Util:\mathcal O\to\mathbb R\);
- observations \(x\) from some observation space \(\mathcal X\);
- a world-model \(M\), which the source treats as a pair \((P,G)\).

The probability model \(P\) is not merely a distribution over ordinary physical variables. For A-FDT, \(P\) must also contain variables representing mathematical or logical facts. The source gives the example of a variable representing the value of \(6288+1048\), which should place most of its probability on \(7336\). More generally, \(P\) can contain variables for the outputs of algorithms, including the agent’s own decision algorithm.

The graph \(G\) encodes how changing one variable affects others. In CDT, \(G\) is a causal graph. In A-FDT, \(G\) is meant to encode a broader class of decision-relevant dependencies: causal, logical, mathematical, computational, and what the source calls “subjunctive” dependencies. Given such a graph, the source reuses Pearl’s \(\Do\)-operator to construct counterfactual hypotheticals.

The expected utility of action \(a\), according to A-FDT, is therefore:

\[
\EU_{\text{A-FDT}}(a;x)
=
\mathbb E_P\!\left[V \mid \Do(D_x=a)\right]
=
\sum_o P\bigl(o \mid \Do(D_x=a)\bigr)\Util(o).
\]

A-FDT prescribes choosing an action that maximizes this quantity.

---

## 2. The central idea: intervene on the decision function, not merely the physical act

The difference between A-FDT and CDT can be summarized in one sentence:

> CDT intervenes on the physical action variable; A-FDT intervenes on the variable representing the output of the agent’s decision function.

In CDT, the agent considers hypothetical worlds produced by an intervention \(\Do(\Act=a)\). This sets the agent’s bodily action to \(a\) and propagates the effects forward along causal arrows. Variables not causally downstream of the action are held fixed. Thus, in Newcomb’s problem, a CDT agent who intervenes on \(\Act=\text{one-box}\) does not thereby change the predictor’s earlier prediction, because that prediction is not causally downstream of the action.

A-FDT changes the locus of intervention. Let

\[
D_x = \text{A-FDT}(P,G,x)
\]

be the variable representing the output of the agent’s decision procedure on input \(x\). A-FDT evaluates:

\[
\Do(D_x=a).
\]

This intervention says: “Suppose the decision procedure I am running, given these inputs, output \(a\). What would the world look like?” The intervention is on the logical output of the decision function, not directly on the physical movement of the agent’s body. The physical action may then be a downstream consequence of that logical output.

The source uses Peirce’s type/token distinction to explain this: CDT intervenes on the token “my action is \(a\),” while A-FDT intervenes on the type, namely the output of the decision procedure itself.

---

## 3. Subjunctive dependence

A-FDT relies on the notion of **subjunctive dependence**. Two systems are subjunctively dependent on a function when their behavior tracks the output of that function. The paradigmatic examples are:

- two agents running the same decision algorithm;
- an agent and a reliable predictor who has modeled that agent’s decision algorithm;
- a simulation of an agent and the agent itself;
- a prediction and the predicted action, insofar as the prediction is accurate.

The source emphasizes that subjunctive dependence is not mere statistical correlation. If two calculators happen to be pink, their colors are statistically correlated in that respect, but if one had been green instead, the other would not thereby change. There is no subjunctive dependence between their colors. But if two functioning calculators are computing \(6288+1048\), then, assuming no malfunction, their outputs are subjunctively dependent on the same mathematical function. If one outputs \(7336\), we expect the other to output \(7336\) too.

Causal dependence is treated as a special case of subjunctive dependence. If a scribe writes down the output of a calculator, the scribe’s writing causally depends on the calculator’s output and also subjunctively depends on it: if the calculator had output something different, the scribe would have written something different.

A-FDT’s graphical model \(G\) is supposed to encode these dependencies. When A-FDT imagines a different output of its decision function, it imagines corresponding changes in all variables that subjunctively depend on that function, while holding fixed variables that do not.

This is the key distinction between predictor-like dependencies and lesion-like dependencies. A predictor’s prediction depends on the agent’s decision procedure; a lesion that merely causes cancer and a preference for smoking does not.

---

## 4. A-FDT in Newcomb’s problem

Newcomb’s problem is the canonical test case.

An agent faces two boxes:

- Box A is transparent and contains \$1,000.
- Box B is opaque and contains either \$1,000,000 or \$0.
- A highly reliable predictor has already decided whether to fill Box B.
- The predictor filled Box B if and only if she predicted the agent would one-box.

The agent may take both boxes or only Box B.

A CDT agent intervenes on the physical action variable \(\Act\). Since the predictor’s prediction is already in the past and not causally downstream of the current action, CDT holds the contents of Box B fixed. Taking both boxes always adds \$1,000, so CDT two-boxes.

An EDT agent conditions on the action. Conditional on one-boxing, it is highly probable that the predictor filled Box B. Conditional on two-boxing, it is highly probable that Box B is empty. EDT one-boxes, because one-boxing is good news.

A-FDT gives the same prescription as EDT in this case, but for a reason structurally closer to CDT. The A-FDT agent does not merely condition on the action. She intervenes on the output of her decision procedure.

A simple A-FDT graph for Newcomb’s problem contains variables such as:

\[
D \to \Act,
\]

\[
D \to \Var{Prediction} \to \Var{BoxB},
\]

\[
\Act,\Var{BoxB} \to \Var{Outcome} \to V.
\]

Here \(D\) represents the output of the A-FDT procedure. The predictor’s prediction is modeled as subjunctively dependent on \(D\). If \(D=\text{one-box}\), then with probability \(0.99\) the predictor predicted one-boxing and filled Box B. If \(D=\text{two-box}\), then with probability \(0.99\) the predictor predicted two-boxing and left Box B empty.

Thus:

\[
\EU_{\text{A-FDT}}(\text{one-box})
\approx
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

And:

\[
\EU_{\text{A-FDT}}(\text{two-box})
\approx
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

A-FDT one-boxes.

The reasoning is not: “If I one-box, that will be good news.” It is: “If this decision procedure outputs one-box, then my body one-boxes and the predictor likely filled the box. If this decision procedure outputs two-box, then my body two-boxes and the predictor likely left the box empty. The first hypothetical world is better.”

---

## 5. A-FDT in the smoking lesion problem

The smoking lesion problem is the canonical case where EDT goes wrong.

An agent is deciding whether to smoke. Smoking is correlated with lung cancer, but the correlation is due to a common cause: a lesion that both causes a love of smoking and causes cancer. Smoking itself does not cause cancer. The agent gains \$1,000 in utility from smoking and gains \$1,000,000 from not dying of cancer.

EDT refrains from smoking, because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes, because smoking does not causally affect cancer.

A-FDT also smokes.

The crucial point is that, in the correct A-FDT graph, the decision-function variable \(D\) affects the action variable \(\Act\), but it does not affect the lesion, cancer, or death. The lesion is not a predictor. It does not model the agent’s decision procedure. It does not compute the output of A-FDT. It merely has a statistical association with smoking preferences.

The source formalizes this with a somewhat unusual complication: the lesion affects the agent’s preferences, so there are two possible utility functions and two possible decision procedures the agent might be running. If the agent has the lesion, she has preferences that favor smoking; if she lacks the lesion, she has preferences that disfavor smoking. The source introduces two model variables:

\[
\FDTvar(\underline{P_S},\underline{G})
\]

and

\[
\FDTvar(\underline{P_R},\underline{G}),
\]

where \(P_S\) corresponds to smoking-positive preferences and \(P_R\) to smoking-negative preferences. The lesion determines which of these decision procedures actually controls the action.

Despite this complication, the core calculation is simple. Let \(p\) be the agent’s prior probability of having the lesion. When A-FDT intervenes on the relevant decision-function variable and sets it to “smoke,” the probability of the lesion does not change:

\[
P(\Var{Lesion})
=
P\bigl(\Var{Lesion}\mid \Do(D=\text{smoke})\bigr).
\]

In the source’s model, the expected utility of the smoking hypothetical exceeds the expected utility of the refraining hypothetical by \(p\cdot \$1{,}000\). Therefore A-FDT smokes.

The important conceptual point is that A-FDT distinguishes between:

1. correlations that arise because the environment contains something that tracks the agent’s decision function; and  
2. correlations that arise from a mere common cause, such as a lesion.

A-FDT preserves the first kind of correlation in its hypotheticals but breaks the second kind.

---

## 6. Observations in A-FDT

One of the most distinctive features of A-FDT is its treatment of observations.

CDT responds to a new observation by conditioning. If the agent first observes \(x\) and later observes \(y\), CDT changes from evaluating

\[
\mathbb E[V\mid \Do(\Act=a), \Obs=x]
\]

to

\[
\mathbb E[V\mid \Do(\Act=a), \Obs=y].
\]

A-FDT, as presented in Equation (4), responds differently. It changes the node on which it intervenes. Upon observing \(x\), A-FDT intervenes on

\[
D_x = \text{A-FDT}(P,G,x).
\]

Upon observing \(y\), it intervenes on

\[
D_y = \text{A-FDT}(P,G,y).
\]

This is why the observation \(x\) appears as an input to the decision-function variable in Equation (4), rather than as an ordinary conditioning event.

The source says that FDT responds to observation “by changing which node it intervenes upon.” This is important in problems where the agent’s observation itself depends on a prediction of the agent’s decision procedure.

There is a slight subtlety here. In some later examples, the source appears to write expectations conditioned on the observation, such as \(\Obs=\Val{full}\). However, the central formal presentation in Equation (4) suggests that the observation enters primarily by selecting the appropriate decision-function output variable. On my operational reading, if one additionally conditions on \(\Obs=x\), one must be careful not to sever the very dependencies A-FDT is trying to preserve. The distinctive A-FDT move is that the observation is treated as an input to the decision procedure, not merely as evidence to be conditioned on in the EDT manner.

---

## 7. A-FDT in transparent Newcomb and Parfit’s hitchhiker

Transparent Newcomb’s problem brings out the novelty of A-FDT’s treatment of observations.

The setup is like ordinary Newcomb’s problem, except both boxes are transparent. The predictor placed \$1,000,000 in Box B iff she predicted that the agent would leave Box A behind upon seeing that both boxes are full. The agent now sees that both boxes are full. Should she one-box or two-box?

CDT says two-box. The boxes are already full; taking Box A adds \$1,000.

EDT also says two-box, because conditional on seeing Box B full, taking both boxes yields more money.

A-FDT says one-box.

To model this, A-FDT uses different decision-function variables for different observations:

\[
D_{\text{full}} = \text{A-FDT}(P,G,\text{full}),
\]

\[
D_{\text{empty}} = \text{A-FDT}(P,G,\text{empty}).
\]

The predictor predicts what \(D_{\text{full}}\) will output upon seeing full boxes. If the predictor predicts that \(D_{\text{full}}\) will one-box, she fills Box B. If she predicts that \(D_{\text{full}}\) will two-box, she leaves Box B empty.

When the agent sees full boxes, A-FDT intervenes on \(D_{\text{full}}\). The relevant comparison is:

\[
\EU_{\text{A-FDT}}(\text{one-box};\text{full})
=
\mathbb E[V\mid \Do(D_{\text{full}}=\text{one-box})],
\]

versus

\[
\EU_{\text{A-FDT}}(\text{two-box};\text{full})
=
\mathbb E[V\mid \Do(D_{\text{full}}=\text{two-box})].
\]

If \(D_{\text{full}}=\text{one-box}\), then with high probability the predictor predicted one-boxing, Box B is full, and the agent receives \$1,000,000. If \(D_{\text{full}}=\text{two-box}\), then with high probability the predictor predicted two-boxing, Box B is empty, and the agent receives only \$1,000.

Using the source’s 99% predictor accuracy, the one-boxing hypothetical is approximately:

\[
0.99\cdot \$1{,}000{,}000 + 0.01\cdot \text{small amount}
\approx \$990{,}000,
\]

while the two-boxing hypothetical is approximately:

\[
0.01\cdot \$1{,}001{,}000 + 0.99\cdot \$1{,}000
\approx \$11{,}000.
\]

So A-FDT one-boxes even while seeing both boxes full.

This may seem strange, but the source argues that it is precisely equivalent to paying the driver in Parfit’s hitchhiker problem. In that problem, a driver will rescue a dying agent only if she predicts the agent will pay \$1,000 after reaching the city. Once in the city, CDT and EDT both refuse to pay, because paying has no further causal benefit and is bad news given survival. The driver predicts this and leaves them behind. A-FDT pays, because the predictor’s earlier action depends on the output of the agent’s decision procedure in the city.

The lesson is that A-FDT does not ask, “Given that I already see the full box, what physical action maximizes utility?” It asks, “Which output of the decision procedure that produces my behavior in this situation leads to the best world?”

---

## 8. Counterfactuals and counterpossibles

A-FDT requires a distinctive kind of counterfactual reasoning. If the agent’s decision procedure deterministically outputs \(a^*\), then evaluating another action \(a\neq a^*\) requires considering a scenario in which the same function has a different output on the same input. Strictly speaking, that is a counterpossible: it runs counter to logical or mathematical necessity.

The source acknowledges this as a technical difficulty. We do not yet have a fully satisfactory general account of counterpossible reasoning. However, the source also argues that this difficulty is not fatal. Human beings routinely reason about uncertain mathematical claims, and A-FDT does not need full counterpossible reasoning in arbitrary mathematics. It only needs enough reasoning to answer questions like:

> If my decision procedure output one-box instead of two-box, how would the predictor’s prediction change?

Operationally, A-FDT handles this by taking the dependency graph \(G\) as given. The graph tells the agent which variables would change if the decision-function variable were set to a different value. This does not solve the metaphysics of counterpossibles, but it gives a usable decision procedure conditional on an appropriate model.

---

## 9. What counts as a relevant dependency?

A-FDT’s correctness depends heavily on the graph \(G\). The source says that Equation (4) works given a graph that accurately describes how changing a logical variable affects other variables, but it also says that constructing such a graph is perhaps the largest open problem for FDT.

The source’s own examples suggest the following principle:

> A variable should be downstream of \(D_x\) in \(G\) if its value depends, directly or through accurate prediction, on the output of the same decision procedure that the agent is running.

This includes:

- the agent’s own action, insofar as it implements the decision procedure;
- other agents running the same decision procedure;
- simulations of the agent running the same decision procedure;
- predictors who model the agent’s decision procedure;
- records or predictions that are reliably produced from that model.

It does not include variables that are merely statistically correlated with the action, such as a lesion that causes both smoking and cancer.

For example, in the psychological twin prisoner’s dilemma, the agent and her twin use the same reasoning procedure. The agent’s graph should therefore make the twin’s action depend on the same decision-function variable. If the shared procedure outputs cooperate, both cooperate. If it outputs defect, both defect. A-FDT cooperates, because mutual cooperation yields the better outcome.

By contrast, in the smoking lesion problem, the lesion does not compute or predict the agent’s decision procedure. It should not be downstream of the decision-function variable. Therefore A-FDT does not treat smoking as changing the probability of the lesion.

---

## 10. Evaluating policies rather than single actions

Equation (4), as presented in Section 5, quantifies over actions. However, the source notes in a footnote that the authors’ preferred formulation intervenes to choose a policy, meaning a mapping from observations to actions, rather than a single action. This distinction may matter in multi-agent or temporally extended dilemmas.

The source does not fully formalize the policy version. A natural operational extension, consistent with the spirit of A-FDT, is as follows.

Let \(\Pi\) be a policy variable representing a function from observations to actions:

\[
\Pi:\mathcal X\to\mathcal A.
\]

Instead of intervening on a single output \(D_x=a\), the agent intervenes on the policy variable:

\[
\Do(\Pi=\pi).
\]

The expected utility of policy \(\pi\) is then:

\[
\EU_{\text{A-FDT}}(\pi)
=
\mathbb E[V\mid \Do(\Pi=\pi)].
\]

A-FDT selects the policy maximizing this expectation.

This extension is especially useful when the same decision procedure will be run at multiple times or by multiple agents. For instance, in voting coalitions or repeated gym-going cases, the relevant subjunctive dependency may run between one’s present decision and one’s future decisions. A policy-level intervention allows A-FDT to evaluate the whole pattern of behavior rather than an isolated act.

I regard this policy formulation as a reasonable operational interpretation of A-FDT, rather than something fully specified by Equation (4) itself. Equation (4) gives the core action-level rule: intervene on the output of the decision procedure given the current input. The policy version generalizes that rule by intervening on the function that maps inputs to outputs.

---

## 11. A practical recipe for applying A-FDT

Suppose one wants to apply A-FDT to an unfamiliar decision problem. The source does not give a complete algorithm for constructing \(G\), but the examples support the following practical recipe.

### Step 1: Identify the decision procedure

Specify the procedure whose output is being evaluated. In the formal theory, this is the variable

\[
D_x = \text{A-FDT}(P,G,x).
\]

In practice, this might be “my current reasoning process,” “the algorithm implemented by me and my copies,” or “the decision procedure used by agents in this class.”

### Step 2: Identify possible outputs

List the candidate actions or policies:

\[
a_1,a_2,\ldots,a_n.
\]

For policy evaluation, list candidate policies:

\[
\pi_1,\pi_2,\ldots,\pi_n.
\]

### Step 3: Identify subjunctive dependents

Ask: if this decision procedure had a different output, what else would change?

Relevant variables include:

- physical actions caused by the decision;
- predictions made by agents who model the decision procedure;
- simulations or copies running the same procedure;
- actions of other agents using the same reasoning;
- rewards or punishments assigned on the basis of predicted behavior.

Do not include variables that are merely statistically correlated with the action, unless they are connected through prediction, simulation, or shared computation.

### Step 4: Draw the graph

Construct a directed graph \(G\). Place the decision-function variable \(D_x\) upstream of the variables that depend on its output. Place ordinary causal dependencies downstream of those variables.

For Newcomb’s problem:

\[
D_x \to \Act,
\qquad
D_x \to \Var{Prediction} \to \Var{BoxB}.
\]

For the smoking lesion problem:

\[
D_x \to \Act,
\qquad
\Var{Lesion} \to \Var{Cancer},
\]

with no arrow from \(D_x\) to \(\Var{Lesion}\) or \(\Var{Cancer}\).

### Step 5: Intervene and compute expected utility

For each candidate action \(a\), compute:

\[
\EU(a)
=
\mathbb E[V\mid \Do(D_x=a)].
\]

Choose the action with maximum expected utility.

This recipe relies on modeling judgments not fully determined by the source. In particular, the identification of subjunctive dependents is the hard part. The paper treats \(G\) as an input; it does not yet provide a general method for learning \(G\) from observation.

---

## 12. Relation to EDT and CDT

A-FDT agrees with EDT and CDT in simple cases where all correlations between the agent’s action and the environment are caused by the action. The source notes that in such models:

\[
\mathbb E[V\mid a]
=
\mathbb E[V\mid \Do(a)]
=
\mathbb E[V\mid \Do(D_x=a)].
\]

The theories diverge when the agent’s action is correlated with other events in a way not caused by the action itself. This happens in the presence of predictors, twins, simulations, and blackmailers.

EDT respects too many correlations. It treats all action-evidence as decision-relevant, so it refrains from smoking in the smoking lesion problem and pays in some blackmail problems because paying is good news.

CDT respects too few correlations. It severs correlations unless they are causal downstream effects of the action. Thus it two-boxes in Newcomb’s problem, fails to pay in Parfit’s hitchhiker problem, and becomes unstable in problems involving perfect predictors.

A-FDT attempts to preserve exactly the decision-relevant dependencies: those that flow from the output of the decision procedure itself.

The source also argues that A-FDT has its own notion of dominance. CDT dominance holds the predictor’s prediction fixed while changing the physical action. A-FDT dominance holds fixed the structure of subjunctive dependencies while changing the output of the decision procedure. Under A-FDT dominance, one-boxing is not dominated in Newcomb’s problem, because changing the decision output from one-box to two-box also changes the predicted box contents.

---

## 13. Open problems and additional assumptions

The most important open problem, explicitly acknowledged by the source, is the construction of \(G\). Pearl’s causal framework gives a well-developed account of causal inference, but there is no equally developed account of inferring logical or subjunctive dependencies from observation.

A second open problem is counterpossible reasoning. A-FDT needs to evaluate hypotheticals in which a deterministic computation has a different output than it in fact has. The source treats this as a technical obstacle rather than a philosophical refutation, but it remains unresolved.

A third issue is logical uncertainty. Real agents cannot assign perfect probabilities to mathematical facts. They may be uncertain about what their own decision procedure would output in complex cases. The source allows \(P\) to assign probabilities to logical variables, but does not give a complete theory of such probabilities.

Where the source leaves these questions open, I think a reasonable operational interpretation is to treat A-FDT as a normative ideal that requires the agent to supply the best available dependency model. In practice, one would use heuristics: identify predictors, copies, simulations, symmetric agents, and commitment-relevant institutions; model their dependence on one’s decision procedure; and evaluate interventions accordingly. If one is uncertain about the dependency structure itself, one could place a probability distribution over graphs \(G\), but that is an extension beyond the primary equation.

Another additional assumption concerns policies. Equation (4) formally chooses an action given an observation. To handle multi-stage or multi-agent problems fully, I think A-FDT should be extended to choose policies by intervening on a policy variable. This is consistent with the source’s footnote saying the authors prefer a policy formulation, but the precise equation is not supplied there. The extension I described above is therefore my own operational development, guided by the source’s general principles.

---

## 14. Conclusion

A-FDT is an expected utility theory that chooses the output of the agent’s own decision procedure by asking which output would produce the best world. Its core formal rule, Equation (4), tells the agent to maximize expected utility conditional on an intervention:

\[
\Do(D_x=a),
\]

where \(D_x\) represents the output of A-FDT given the agent’s model, graph, and observation.

This simple change has large consequences. A-FDT one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, one-boxes in transparent Newcomb, and resists blackmail in cases where EDT or CDT can be exploited. It does so by preserving predictor-like subjunctive dependencies while breaking merely statistical correlations.

The theory is elegant, but incomplete. Its main unresolved issue is the construction of the dependency graph \(G\), and its counterfactuals require reasoning about counterpossible changes to logical facts. Still, as a normative framework, A-FDT gives a clear and unified answer: do not merely choose an action; choose the output of the reasoning procedure that produces the action.

---

## References

Pearl, J. *Causality*. Cambridge University Press, 2000.

Soares, N., and Yudkowsky, E. “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.

Joyce, J. *The Foundations of Causal Decision Theory*. Cambridge University Press, 1999.