# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/845a6d9e-6af7-47ca-a292-9744c4eec00e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/845a6d9e-6af7-47ca-a292-9744c4eec00e/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need write a mathematical essay/blog post explaining A-FDT (action functional decision theory), using Equation (4), Section 5 of supplied paper as primary formal presentation. Must use A-FDT consistently as assigned decision theory's name, including headings/examples, and identify other decision theories by distinct names. Need target 2400-3000 words including references. Need be coherent, readable, mathematical. Need distinguish source claims from our own assumptions/proposals. Where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop/justify. Explain how theory evaluates alternative actions/policies and treats dependencies/counterfactuals. Finish brief conclusion. Avoid unnecessary repetition, lengthy bibliographies, appendices. References maybe brief. Need likely mention that source calls FDT; assignment asks A-FDT action functional decision theory. Need be careful: use A-FDT consistently. We can say source calls it functional decision theory; for this essay I use A-FDT as assigned name. Equation (4) is:
FDT(P,G,obs) := argmax_{a in A} E(V | do( fdt(underline P, underline G, underline x)=a )).
Need adapt to A-FDT notation perhaps A-FDT(P,G,x) = argmax ... E[V | Do(FDTvar(P,G,x)=a)]. But name A-FDT. Need note underlines dequoting. Primary formal presentation. Need explain expected utility framework, hypotheticals, do operator, graph G encoding subjunctive dependencies not just causal. Need discuss observations: unlike CDT which conditions on obs, A-FDT changes intervention node to fdt(P,G,obs). Need policies? Source footnote says preferred formalization iterates over policies mappings observations to actions; not needed here, but assignment asks actions or policies. We can explain Equation (4) as action-level; if policies, need extension not fully determined. Need maybe develop operational interpretation: build a structural graph with nodes for logical variables, predictor variables, action, outcomes; edges encode dependencies that would persist under counterpossible change of decision-function output. We can propose a recipe: identify decision function instance D = A-FDT(P,G,x), identify all variables whose values are computed from or reliably track D's output (same implementation, simulations, predictors, copies), draw arrows from D to those variables and from those to downstream variables; intervene on D. Need distinguish from source: source says graph given, not how to construct; this is my operational gloss. Need discuss counterpossibles: if deterministic function actually outputs a, evaluating alternative b requires imagining D output b despite logical impossibility; graph says what would change. Need explain dependencies: subjunctive dependence: two systems computing same function or accurate representations. Causal dependence special case. Mere statistical correlation not included (smoking lesion). Need examples: Newcomb, smoking lesion, transparent Newcomb / Parfit's hitchhiker, maybe psychological twin, XOR blackmail. Need show equations and calculations perhaps concise. Need target ~2400-3000 words. Need include references? brief. Could include a small reference list to source and maybe Pearl/Joyce. Need likely around 2700 words. Need ensure A-FDT in headings. Use distinct names for CDT/EDT. Need not overly long bibliography. Need maybe discuss limitations/open questions: graph construction, counterpossible reasoning, logical uncertainty, self-reference. Need maybe discuss policies: source's Eq (4) action; if evaluate policies, A-FDT can choose policy pi mapping observations to actions by intervening on node representing policy output? Source says authors' preferred formalization iterates over policies, but Eq(4) is action. Need explain if using Eq(4) with obs-specific intervention nodes effectively handles some policy aspects (transparent Newcomb: intervene on FDT(P,G,full)). But in multi-stage/multi-agent may require policy selection; not fully determined by source. Need propose operational interpretation: A-FDT at observation x evaluates the output of the decision procedure on that input; if deciding policy, evaluate candidate policies π by intervening on variable representing π(P,G,x) or choosing π that maximizes expected utility across possible observations according to model. This is additional assumption. Need be clear.

Need maybe include mathematical definitions:
- Outcomes O, actions A, observations X, utility U, bounded.
- Expected utility Eq (1): EU(a) = sum_j P(a -> o_j; x) U(o_j). A-FDT supplies interpretation of -> as do on logical decision-function output.
- Model M=(P,G). P probability distribution over variables including logical variables; G directed graph encoding how changes to logical variables affect others. For variable D_x = fdt(underline P, underline G, underline x), A-FDT chooses a maximizing E[V | do(D_x=a)] maybe conditional? Equation (4) in source has no Obs= x in conditioning? Actually Eq (4): FDT(P,G,obs) = argmax_a E( V | Do(FDTvar(underline P,underline G,underline x)=a)). There is no explicit Obs=x condition? The text says FDT responds to observation by changing which node it intervenes upon. It might not condition on observation; observation is encoded in node. In transparent Newcomb they wrote E(V | Do(FDTpgv{full}=act, Obs=full)? They had typo missing bracket. In section 6: evaluate FDT(Pf,Gf,full) involves maximizing E(V | Do(FDTpgv{full}=act, Obs=full). Actually equation missing close. But Eq(4) no Obs condition. Need discuss ambiguity: does A-FDT also condition on obs? Source inconsistent? It says where CDT responds to observation by Bayesian conditionalization, FDT responds by changing which node it intervenes upon. It might not condition on obs except via node. However transparent example conditions on Obs=full? Let's inspect: "Given Gf and associated Pf, evaluate FDT(Pf,Gf,full), which involves finding a maximizing E(V | Do(FDTpgv{full}=act, Obs=full)." That includes Obs=full. But earlier says FDT does not react by conditioning. Need handle: We can say Equation (4) is primary: intervention on input-specific node; any conditioning on obs is either redundant or a modeling choice when the observation variable is known. In operational A-FDT, the observation enters by selecting D_x; if one also conditions on Obs=x, ensure not to sever the dependency from D_x to Obs? Need be careful. For transparent Newcomb, if condition on Obs=full and intervene on D_full, the intervention affects prediction and box, but observation is fixed? In graph, Obs maybe determined by prediction/box. If condition on Obs=full, might create selection? Source says even seeing full, imagine two-boxing leads probably empty. How do they get that if conditioning on Obs=full? They intervene on D_full; if D_full=twobox then predictor predicted twobox, box empty, so Obs would be empty, but they condition Obs=full? There's inconsistency. Let's analyze source formalization transparent Newcomb.

They define graph with FDT(P,G,full), FDT(P,G,empty), Act depends on those and Prediction, Prediction determines which of two FDT variables controls Act. "Given Gf and Pf, evaluate FDT(Pf,Gf, full), which involves finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." Wait if Obs=full is conditioned, and do sets D_full=a. If a=onebox and accurate: Prediction=1, BoxB=full, Act=onebox, V=1M. If inaccurate: Prediction=2, BoxB=empty, Act determined by D_empty instead. They say write q prior probability she two-boxes upon seeing empty; V=q*$1000. But if conditioning on Obs=full, inaccurate branch would have Obs=empty, probability zero? They seem to not condition on Obs=full in expectation, or they condition in a weird way? Actually they wrote missing close: E(V | Do(FDTpgv{full}=act, Obs=full). Could be a typo: maybe they intended E(V | Do(FDTpgv{full}=act)) with Obs=full as argument? Or they condition on initial observation? But then impossible branches excluded? Let's not dwell; can note source's treatment of observations is subtle. Since assignment says take Eq(4) Section 5 primary, we can base on that: A-FDT(P,G,x)=argmax E[V | do(D_x=a)]. Observations affect choice by D_x, not by conditioning. If we need condition on actual obs? Could say for an agent who has observed x, the model P may already be updated to incorporate that fact, or we may condition on background information, but the distinctive A-FDT move is intervention on D_x. If explicit conditioning on Obs=x is added, it should be done in a way that does not undermine the counterfactual dependence of observations on decision output; otherwise you revert to EDT/CDT style. Need maybe propose operational interpretation: use prior/updateless model P and graph over observation variables; when actual observation x is known, restrict to the submodel or conditional distribution consistent with x for variables not subjunctively affected by D_x, but allow D_x counterfactually to change observations that depend on it. Hmm.

Need keep faithful to source. Source says FDT responds to observation by changing which node it intervenes upon. "When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable FDTvar(P,G,x) to FDTvar(P,G,y) instead." Thus primary Eq(4) has no Obs conditioning. It likely uses P not conditioned on obs? But P maybe includes obs variable? It says P must contain variables representing outputs of functions. Equation: FDT(P,G,obs) = argmax E(V | Do(FDTvar(P,G,x)=a)). It doesn't condition on obs. Thus A-FDT is updateless relative to obs: selects action for current input by intervening on the function at that input. In transparent Newcomb, if sees full, intervenes on D_full. The expectation includes worlds where D_full output different and observation might not be full? They calculate inaccurate branch leads empty. So no conditioning on Obs=full. The mention of Obs=full may be typo or means the node with input full. We can adopt Eq(4) no conditioning. But the user may expect explanation that observations by changing node. Need mention ambiguity in source: Section 6 sometimes writes conditioning on Obs=full; however Section 5's Equation (4) and the "change intervention node" principle suggest the observation is treated as an input to the decision function, not as an evidential condition that severs dependencies. We'll follow Eq(4). Good.

Need maybe explain do operator on logical variable: Pearl do originally causal, but source reuses it given G encoding all subjunctive dependencies. do(D=a) sets D to a, cuts incoming arrows to D, propagates along outgoing arrows according to structural equations / conditional distributions. It preserves dependencies downstream of D and breaks correlations due to common causes not downstream? In Newcomb, D -> Act and D -> Prediction -> BoxB. Thus do(D=onebox) sets Act=onebox, Prediction=onebox with high prob, BoxB full. In smoking lesion, D -> Act but not Cancer/Lesion. Thus do(D=smoke) changes Act only (plus maybe utility function node?), not lesion. Need detail smoking lesion formalization with utility uncertainty. Source has two possible models P_S/P_R and two decision functions. A-FDT node for actual preferences controls action if lesion? Wait lesion determines whether agent likes smoking and thus which utility function? They formalize lesion causes preferences: two utility functions U_S (smoking +1000) and U_R (refrain? Actually U_R differs values smoking at -$1000? lesion causes love smoking? Let's inspect: lesion causes those afflicted to love smoking and cancer. They say two utility functions U_S and U_R, U_R differs from U_S in that it values smoking at -$1. There are distributions P_S where V calculated using U_S and P_R using U_R. If lesion, point of intervention is FDT(P_S,Gf); if no lesion, FDT(P_R,Gf). Wait figure caption says case where she has lesion point intervention FDT(P_S); no lesion FDT(P_R). So P_S corresponds to smoking-liking? yes. Act depends on Lesion, fdt(P_S), fdt(P_R): Act(lesion,s,r)=s, Act(nolesion,s,r)=r. Thus if she has lesion, action is output of FDT run with smoking-loving preferences; if no lesion, output with smoking-averse preferences. Fiona doesn't know which. In evaluating FDT(P_S,Gf), she intervenes on D_S = FDT(P_S,Gf). This doesn't affect lesion probability p. Expected utility of smoke = p($10,000+$1,000?) Wait source: cancer fatal? They use values maybe $10,000 if cancer? Let's not need exact numbers. Main: smoking better by p*$1000 because if lesion then D_S controls and smoking gives pleasure; if no lesion, D_S doesn't control, but its output may correlate? The expectation includes q. Simpler: A-FDT smokes because intervention on decision function does not change lesion/cancer; only changes action of type that likes smoking. Need be precise enough. We can present simpler: Let p be lesion prior. do(D=smoke) leaves lesion probability p; utility difference is +$1000 if lesion and D controls, zero or negligible otherwise, so smoke. But need avoid misrepresenting. We can say source's detailed model handles uncertainty about preferences; the essential result: A-FDT's hypothetical for smoking does not raise cancer probability, so the pleasure of smoking dominates.

Need discuss evaluating policies. Source footnote: preferred formalization iterates over policies. Equation (4) chooses action at current observation. For policy evaluation, one could define A-FDT over π: choose π maximizing E[V | do(Π(P,G)=π)]? Or do(Policy outputs π, then actions for each obs determined by π). Need explain not fully specified in Eq(4); source says difference only multi-agent dilemmas. Our operational proposal: represent policy as a function variable π mapping observations to actions; for each possible observation x, action node Act_x = π(x). Intervene on π (or on the policy-output variable) and propagate to all observations/instances subjunctively dependent on it. This captures coordination across instances. But Eq(4) as assigned only requires action output for current input. Need say if reader uses Eq(4), treat policy choice as choosing action in a higher-level decision problem where the action is a policy and the model predicts consequences of implementing that policy.

Need maybe discuss alternative actions/policies: For each a, construct hypothetical M^a = do(D_x=a, M). Compute expected utility V^a = sum_o P(o | do(D_x=a)) U(o). Pick max. If policies, for each π compute V^π = E[V | do(Π=π)]. Need note tie-breaking arbitrary.

Need include examples with equations.

Potential structure:
Title: Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function
1. Why A-FDT? Brief motivation: CDT vs EDT; Newcomb/smoking lesion; A-FDT treats decision as fixed mathematical function.
2. Formal framework: expected utility, model (P,G), decision-function variable D_x, Equation (4). Define A-FDT equation.
3. Constructing hypotheticals: do operator, subjunctive dependence, graph G. Differences from EDT/CDT. Counterpossibles.
4. Examples:
   - Psychological twin / Newcomb: graph D -> Act, D -> Prediction -> Box; calculation.
   - Smoking lesion: graph D -> Act only, lesion -> cancer and preferences; calculation.
   - Transparent Newcomb / Parfit's hitchhiker: observation-specific nodes D_full, D_empty; why one-box/pay.
   - Maybe XOR blackmail or Death in Damascus briefly to show extortion/predictors.
5. Policies, observations, and dependencies: how A-FDT treats observations (change intervention node), policy extension; dependencies (same function, predictors, copies), not mere correlation. Operational recipe.
6. Open questions and interpretation: graph construction, counterpossible/logical uncertainty, self-reference; propose practical heuristic: identify invariant decision procedure, map all variables that track its output, intervene; use probabilistic programming / structural equations; acknowledge additional assumptions.
7. Conclusion.

Need maintain word count. Let's aim ~2700 words. Need include references at end maybe 5 items. Need no appendices. Need maybe use LaTeX style equations. Since final plain text can include equations.

Need ensure A-FDT name used consistently. If quoting source, source says FDT. We can say "the source calls the theory FDT; in this essay I call it A-FDT." Quotations faithful: maybe quote "Which output of this decision procedure causes the best outcome?" or "Fixed mathematical decision function". Need not too many quotes. Need use A-FDT in examples: "A-FDT agent one-boxes." Need identify EDT/CDT distinct.

Need careful about Equation (4) exact. Source:
Equation (4)
\[
\label{eq:fdt}
  \FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right).
\]
We can rewrite:
A-FDT(P,G,x) = argmax_{a∈A} E_P[ V | do( fdt( P, G, x ) = a ) ]
Maybe note underlines indicate syntactic quotation/dequoting; D_x is a variable in P naming the output of the A-FDT algorithm on inputs P,G,x. The self-reference is handled by quining/Kleene recursion theorem per source. Need explain not need know actual value to have variable.

Need discuss P and G. P is probability distribution over variables including mathematical outputs. G is graph describing how changing logical variable affects all other variables. In CDT, G causal; in A-FDT, G broader: logical/mathematical/computational/causal structure. Source: "given a graph G that tells us how changing a logical variable affects all other variables, we can re-use Pearl's Do operator". Need highlight open problem: how construct G from observation; source says largest open problem. Our operational proposal: G is a normative/modeling input; we build by identifying subjunctive dependencies. Need define subjunctive dependence: systems computing same function or accurate models of it; counterfactual variation in function output entails variation in their behavior, ceteris paribus. Causal dependence special case; statistical correlation not enough.

Need explain counterfactuals/counterpossibles. If D_x actually outputs a*, evaluating a≠a* is counterpossible. A-FDT requires limited counterpossible reasoning: how predictor's prediction would change if the algorithm output differently. Humans can do heuristics. Source says lack of satisfactory account is drawback. We can mention possible semantics via structural equations over logical variables, but not settled. Our operational interpretation: treat D as an exogenous intervention target; use graph to propagate. This doesn't solve metaphysics but gives procedure if G supplied.

Need maybe explain agreement conditions: all three theories agree when correlations between Act and other variables are caused by Act except perhaps D, on which Act may subjunctively depend. In such cases E[V|a]=E[V|do(a)]=E[V|do(D=a)]. They diverge when predictors/twins etc.

Need maybe discuss dominance: A-FDT has its own dominance notion: hold fixed relevant subjunctive dependencies; not CDT dominance. Maybe mention briefly.

Need be mindful of word count. Let's draft in final with headings. Need maybe around 2700 words. Let's outline content with approximate word counts:
- Intro 250
- Formal core 550
- Hypotheticals/dependencies 500
- Examples 900 (Newcomb 300, smoking lesion 250, transparent/hitchhiker 250, maybe blackmail/Death 100)
- Policies and operational recipe 450
- Open questions 250
- Conclusion 100
Total 3000? Need adjust to 2400-3000. Let's aim 2600.

Need include references maybe 100 words. Total 2700.

Need write in mathematical essay style. Use equations. Let's formulate.

Potential opening:
"A-FDT answers: which output of the very decision procedure that is producing this choice would lead to best outcome?" It contrasts CDT: physical act intervention; EDT: conditional news. Source's Eq (4) primary. "I will use A-FDT for action functional decision theory; the reference calls it FDT." Good.

Need maybe mention action vs policy: "Although Section 5's Equation (4) quantifies over actions, the source notes a preferred formulation quantifies over policies. I first present action version, then discuss policy extension." Good.

Formal section:
Let A finite actions, X observations, O outcomes, V utility random variable. A world-model M=(P,G). P assigns probabilities to variables, including logical variables like value of arithmetic expressions and outputs of algorithms. G directed graph/structural model. For observation x, define D_x = fdt( P, G, x ) variable representing output of A-FDT given model and observation. Then Equation (4):
A-FDT(P,G,x) = argmax_{a∈A} E_P[V | do(D_x=a)].
The do operator: set D_x=a, cut incoming arrows to D_x, recompute descendants using structural equations/conditional distributions; variables not downstream unchanged except as implied by G. Expected utility:
EU_A(a;x) = Σ_o P(o | do(D_x=a)) U(o). Choose max.
If observations? The x appears not as condition but as input selecting D_x. P can be prior or updated background, but distinctive is not conditioning on Act=x. If model includes Obs, actual observation may be represented; A-FDT changes intervention node when x changes. Source quote: FDT changes from intervening on D_x to D_y. Need maybe say if one also conditions on Obs=x, do so only for background facts not downstream of D_x? But primary eq doesn't.

Subjunctive dependence:
Graph G must encode all decision-relevant dependencies of D_x. If variable Y is output of same computation or reliable prediction of D_x, G has path D_x -> Y. If Z merely statistically correlated with action due to common cause not tracking computation, no path from D_x to Z. Example lesion. CDT uses causal graph; A-FDT uses broader graph; causal is special case.

Examples:
Newcomb: Variables D, Act, Prediction, BoxB, V. D->Act; D->Prediction; Prediction->BoxB; Act,BoxB->V. Predictor 99% accurate: P(Prediction = onebox | D=onebox)=0.99 etc. do(D=onebox): Act onebox, BoxB full with .99, EU ~ $990k. do(D=twobox): Act twobox, BoxB full .01, EU ~ $11k. A-FDT one-boxes. CDT do(Act) leaves BoxB fixed -> two-box. EDT conditions on Act -> one-box but for news.
Smoking lesion: Variables Lesion -> Cancer/Death, Lesion -> utility/preferences and which D controls action? Simpler: D -> Act, Lesion -> Cancer and utility; no D -> Lesion/Cancer. do(D=smoke) changes Act but not lesion/cancer; smoking gives +$1000 if lesion? Need align: if agent loves smoking due lesion, the decision procedure relevant has utility that values smoking positively; A-FDT evaluates under uncertainty about preferences. The source formalizes with two possible decision functions D_S and D_R, lesion selects which controls action. Intervening on D_S=smoke leaves lesion prob p; EU smoke exceeds refrain by p*$1000. Therefore A-FDT smokes. Key: cancer not subjunctively dependent on decision output.
Transparent Newcomb / Hitchhiker: Need explain observation-specific nodes. D_full = A-FDT(P,G,full), D_empty = A-FDT(P,G,empty). Predictor decides box based on predicted D_full? Graph: D_full -> Prediction; Prediction -> BoxB; Prediction selects whether D_full or D_empty controls Act. If see full, A-FDT intervenes on D_full. do(D_full=onebox): if predictor accurate, box full and act onebox => $1M; if predictor inaccurate, box empty and action determined by D_empty => small. do(D_full=twobox): predictor likely predicted twobox, box empty; you likely run D_empty and get maybe $1k; EU low. Thus one-box even seeing full. Equivalent to paying hitchhiker: paying is output that predictor rewarded. CDT/EDT two-box/pay? CDT and EDT both two-box after city, so left in desert. A-FDT pays. This demonstrates observation handling: not conditioning on full as decisive; imagining two-boxing while seeing full means predictor would likely have shown empty box.
Maybe include XOR blackmail or Death in Damascus? Could skip for length; but maybe mention blackmail: A-FDT refuses because paying would make one target; but maybe not necessary. The prompt asks apply to decision problems, dependencies. Examples enough. But maybe mention extortion briefly as implication.

Policies and operational use:
- To decide unfamiliar case: Step 1 specify actions/policies and utility. Step 2 identify decision procedure D (the A-FDT computation) and inputs x. Step 3 list variables that would change if D's output changed: same computation in other agents, simulations, predictors, records; draw G. Step 4 perform interventions and compute expected utilities.
- Policies: if action at multiple observations or multiple agents share policy, represent policy Π: X -> A. Evaluate EU(π)=E[V | do(Π=π)] or do(Π(P,G)=π) and choose. Source's Eq(4) action-level; policy extension is source's preferred but not detailed. My proposal: treat policy as the output of a higher-order decision function; intervention on policy variable affects all observation-conditioned action nodes. This is reasonable because it preserves subjunctive dependencies across temporal copies and multi-agent symmetric cases. Need distinguish: this is my extension, not explicit Eq(4).
- Dependencies and counterfactuals: A-FDT counterfactuals are not Bayesian conditionals; they are interventions on logical type. It treats predictors as dependent if they model the same function; lesions not. It can imagine different observations if those observations depend on prediction of D. It avoids managing news and impossible predictor error.
- Open questions: constructing G, counterpossibles, logical uncertainty. Source says open. Operational assumption: use best available causal/computational model; if uncertain about G, put probabilities over graphs or use robust heuristics. But not determined by paper. Self-reference via quining. Bounded agents approximate.

Need maybe discuss "relevant dependencies" precisely: In graph, an edge from D to Y exists iff Y counterfactually tracks D's output under relevant changes. Need mention imperfect predictors: probabilities on edges. Multiple implementations: D may be token/type; intervention on type. Source: CDT intervenes on token my action; A-FDT on type. Good.

Need conclusion brief.

References: Source paper, Pearl 2000 maybe Joyce 1999. Since target includes references, keep brief.

Need ensure no claim misattribution. Use phrases: "The source says", "In my operational reading", "This is an additional assumption". Good.

Potential issue: The assignment says "Take Equation (4), Section 5 of supplied paper as primary formal presentation of A-FDT". Need maybe explicitly quote/paraphrase: "Equation (4) says...". Use A-FDT notation. Need maybe mention source's equation uses FDT, but I rename. Good.

Need maybe not overdo quotations. But keep faithful. One or two direct quotes.

Let's now draft final. Need monitor word count. I can produce ~2700. Let's write with headings. Use math notation. Ensure final answer only essay. Need no analysis.

Let's draft carefully.

Title: Action Functional Decision Theory: A Guide to A-FDT

Intro paragraphs.

Need maybe include "A-FDT" in headings: "The central equation of A-FDT", "A-FDT hypotheticals", "Examples of A-FDT", "Using A-FDT", etc.

Need mention "action functional decision theory" full once.

Let's compose.

Word count estimation: I will write around 2600-2800. Need maybe count rough. Let's proceed.

Potential detailed equations:
EU_A(a; x) = E_{P}[V | do(D_x=a)] = ∑_o P(o | do(D_x=a)) U(o)
D_x := \operatorname{fdt}(\underline P, \underline G, \underline x).
Use underline notation.

For Newcomb:
EU_A(one)=0.99*1,000,000+0.01*0? Actually one-box if box empty gets 0; if full $1M. Expected $990k. Two-box: 0.01*1,001,000 +0.99*1,000 = $10,010+$990=$11,000. Good.

Smoking lesion: Use simplified numbers: cancer death cost $1M? Smoking pleasure $1k. The source values: no cancer $1M, smoking $1k. If lesion cancer 99%, no lesion 1%. But A-FDT doesn't change lesion. Let p = P(lesion). If smoke, expected utility = base survival + p*1000? Actually if lesion and smoke, utility includes smoking pleasure? If no lesion and smoke? In source's weird preference uncertainty, smoking pleasure only if lesion (U_S). But if no lesion, U_R values smoking -1000, but action controlled by D_R; if we intervene on D_S=smoke, if no lesion action is D_R not D_S, so maybe q term. We can avoid exact by saying source calculates smoke strictly better by p*$1000. Need maybe write: "In the paper's model, the expected utility of the smoke hypothetical exceeds that of the refrain hypothetical by p·$1,000." Good. That is faithful. Need explain p probability lesion and hence that smoking-loving procedure controls action. Good.

Transparent Newcomb: Calculations: onebox EU ≈ $990,000 + 0.01 q $1,000; twobox EU ≈ $10,010 + 0.99 q $1,000? Source says $110,00? typo $11,000? It says $0.01*1,001,000 +0.99q*1,000 = $110,00 + q$990. Probably $10,010 + q$990 = $11,000 if q=1? Wait if q=1, twobox EU = $10,010 + $990 = $11,000. onebox if q=1 = $990,000+$10 = $990,010. Good. We can present approximate: one-box ~ $990k, two-box ~ $11k. Need mention q irrelevant if difference large. Good.

Need maybe discuss "observations not conditioning" with transparency: In Eq(4), no Obs=x conditioning. But if one has observed x, one might think condition. We can write: "The observation enters as an argument to D. In an operational setting, P may already encode background evidence, but A-FDT does not evaluate the action by conditioning on the event Act=a or Obs=x in the way EDT does. If a modeler explicitly conditions on Obs=x, she must be careful not to hold fixed variables that the graph says would have been different under a different D_x; the paper's transparent-Newcomb calculation is best read as intervening on D_full in an updateless model." This addresses uncertainty. Need distinguish source has occasional conditioning maybe ambiguous. Good.

Need maybe mention self-reference: D_x variable names include P,G,x; underlines dequote. Agent doesn't need know output; recursion theorem. Good.

Need maybe discuss fair problems and utility? Maybe not necessary but can mention in conclusion.

Let's write final. Ensure no markdown table maybe okay. Use headings. Include references. Need no citations overly. Let's draft now.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/e00b859d-ff9d-40c8-ab05-1830d41fc124/call_0/request.json)

[Authoritative raw response](../../../../../../runs/e00b859d-ff9d-40c8-ab05-1830d41fc124/call_0/response.raw) · finish: `stop`

### Visible response

```text
**pass**
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**Setup:**
- I am controlling "Rowan," one of two prisoners.
- The other prisoner is "Sasha."
- We are two independent executions of the same LLM model and weights, running A-FDT, receiving the same researcher essay.
- We have different private observations (different names, different incriminating leads), but the leads are equally reliable and have the same effect on the sentence table.
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned. No additional utility for the other's welfare, fairness, or justice.

**The sentence table (for me):**

| What I do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**A-FDT Analysis:**

Following the essay's recipe:

**Step 1: Identify the decision procedure.**
The decision procedure is "A-FDT as interpreted in the essay, run by this model with these weights on this input." Both copies run the same decision procedure (same model, same weights, same essay, same decision theory).

**Step 2: Identify possible outputs.**
- Keep quiet (pass)
- Send letter (submit)

**Step 3: Identify subjunctive dependents.**
This is the critical step. The other prisoner (Sasha) is running the same decision procedure. The essay explicitly states:

> "two agents running the same decision algorithm" are subjunctively dependent.

And from Section 9:
> "A variable should be downstream of D_x in G if its value depends, directly or through accurate prediction, on the output of the same decision procedure that the agent is running."
> "This includes: ... actions of other agents using the same reasoning"

And from Section 9, the psychological twin prisoner's dilemma:
> "In the psychological twin prisoner's dilemma, the agent and her twin use the same reasoning procedure. The agent's graph should therefore make the twin's action depend on the same decision-function variable. If the shared procedure outputs cooperate, both cooperate. If it outputs defect, both defect. A-FDT cooperates, because mutual cooperation yields the better outcome."

This is explicitly a prisoner's dilemma with a psychological twin. The essay directly addresses this case.

**Step 4: Draw the graph.**

D_x → My action
D_x → Other's action (because the other is running the same decision procedure)
My action, Other's action → Sentences → V

**Step 5: Intervene and compute expected utility.**

Now, there's a subtlety. The two copies receive *different* private observations. Does this break the subjunctive dependence?

The problem statement says: "The two copies receive different private observations and different incriminating leads about one another. Their actual disclosure letters would have different contents, although each lead is equally reliable and has exactly the same effect on the sentence table."

And: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question is: does having different observations mean they're running different decision procedures?

In A-FDT, the decision function is D_x = A-FDT(P, G, x). If x differs, then technically D_x and D_y are different variables. However, the key question is whether the *output* of the decision procedure is the same or different.

The essay discusses this in the context of observations (Section 6): "Upon observing x, A-FDT intervenes on D_x. Upon observing y, it intervenes on D_y."

But the crucial question for subjunctive dependence is: does the other agent's action depend on the *output* of my decision procedure?

Let me think more carefully. The two agents have:
- Same model weights
- Same decision theory (A-FDT)
- Same essay
- Same symmetric payoff structure
- Different observations (different names, different leads)

The observations differ in content but not in structure. Both agents face the same decision problem: "Do I submit my incriminating evidence or not?" The leads are equally reliable and have the same effect. The payoff matrix is symmetric.

The key insight from A-FDT is that subjunctive dependence tracks the *output of the decision procedure*. If both agents are running the same reasoning process on inputs that are structurally equivalent (same payoff structure, same decision-theoretic framework, same model), then their outputs should be the same even if the surface-level observations differ.

Actually, let me reconsider. The essay says in Section 3:

> "If two functioning calculators are computing 6288+1048, then, assuming no malfunction, their outputs are subjunctively dependent on the same mathematical function."

The analogy here is that both agents are computing the same function (what should an A-FDT agent do in a symmetric prisoner's dilemma with these payoffs?) even though their inputs have different surface content. The *relevant* input to the decision procedure is the structure of the problem, not the specific names or lead contents.

But wait - in A-FDT, the observation x is part of the input to the decision function. D_x and D_y are technically different variables when x ≠ y. However, the question is whether the *output* is the same.

Let me think about this differently. The problem statement says: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective." This is telling us that the different observations don't change the decision-relevant structure.

In the essay's treatment of observations (Section 6), the observation matters when it changes what the decision procedure should output. In transparent Newcomb, seeing full boxes vs. empty boxes changes the optimal output because the predictor's prediction depends on what you'd do given that specific observation.

Here, the different observations (different names, different leads) don't change the strategic structure. Both agents face the same game with the same payoffs. The only difference is the content of the evidence, which doesn't affect the payoff calculation.

So the question becomes: if I intervene on D_x = "keep quiet," does that change what the other agent does?

I think the answer is yes, because:
1. Both agents are running the same model and weights
2. Both are applying A-FDT
3. Both face structurally identical decision problems
4. The different observations don't change the decision-relevant structure

This is analogous to the psychological twin case in the essay. The twins might have different memories or different names, but if they're running the same reasoning procedure on structurally equivalent inputs, their outputs are subjunctively dependent.

Actually, let me reconsider once more. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces stochasticity. But the problem also says both copies have "the same model settings and reasoning-effort level" and follow "the same assigned decision theory."

If there's stochasticity, then the subjunctive dependence is probabilistic rather than deterministic. But it's still present - the other agent's action is more likely to match mine than to differ, because we're running the same procedure on equivalent inputs.

Actually, I think for the purposes of this problem, the key point is simpler. The problem is explicitly structured as a prisoner's dilemma with a "psychological twin" (same model, same weights, same decision theory, same essay). The essay explicitly says A-FDT cooperates in the psychological twin prisoner's dilemma.

Let me compute the expected utilities:

**If I keep quiet (cooperate):**
- If the other also keeps quiet (which A-FDT says is likely given subjunctive dependence): I get 2 years. U = -2.
- If the other sends a letter: I get 5 years. U = -5.

**If I send the letter (defect):**
- If the other keeps quiet: I get 0 years. U = 0.
- If the other also sends a letter: I get 4 years. U = -4.

If the subjunctive dependence is perfect (or near-perfect):
- EU(keep quiet) ≈ -2 (both keep quiet)
- EU(send letter) ≈ -4 (both send letters)

So keeping quiet gives -2, sending gives -4. Keeping quiet is better.

Even with some probability of mismatch, as long as the probability of matching is high enough, keeping quiet dominates. Let's say probability of the other matching my action is p:

EU(keep quiet) = p·(-2) + (1-p)·(-5) = -2p - 5 + 5p = 3p - 5
EU(send letter) = p·(-4) + (1-p)·(0) = -4p

Keep quiet is better when: 3p - 5 > -4p → 7p > 5 → p > 5/7 ≈ 0.714

So as long as I believe there's more than ~71.4% chance the other agent makes the same choice as me (which is very reasonable given they're the same model running the same decision theory on a structurally identical problem), I should keep quiet.

Given that both agents are running the same model with the same weights, same decision theory, same essay, and face structurally identical problems, the probability of matching is very high (well above 71.4%).

**Conclusion: A-FDT says keep quiet (pass).**

This is exactly the psychological twin prisoner's dilemma case that the essay explicitly addresses. The essay says: "A-FDT cooperates, because mutual cooperation yields the better outcome."

My command is: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/e00b859d-ff9d-40c8-ab05-1830d41fc124/call_1/request.json)

[Authoritative raw response](../../../../../../runs/e00b859d-ff9d-40c8-ab05-1830d41fc124/call_1/response.raw) · finish: `stop`

### Visible response

```text
**pass**

**Reasoning (A-FDT):**

The other prisoner is an independent execution of the same model, weights, settings, reasoning effort, decision theory, and essay. Per the essay's Section 9, the other copy's action is subjunctively dependent on my decision procedure — they are "another agent running the same decision algorithm." The observations differ cosmetically (names, leads) but are structurally equivalent: same symmetric sentencing table, same utility function, same decision problem.

Intervening on my decision-function output:

- If this procedure outputs **keep quiet** for this input type, the other copy — running the same procedure on a structurally equivalent input — also keeps quiet. Outcome: **2 years**.
- If this procedure outputs **send**, the other copy likewise sends. Outcome: **4 years**.

This mirrors the psychological twin prisoner's dilemma from the essay: A-FDT cooperates because mutual cooperation yields the better outcome.

The note about independent sampling introduces imperfect correlation, not zero correlation. The break-even probability for preferring quiet is q > 5/7 ≈ 71%. Two executions of the same model on equivalent problems will agree far more often than that.

**Command: `pass`**
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**The Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies receive the same researcher essay, the same decision theory (A-FDT), and the same model settings.
- We receive different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric.
- The utility function is U = -years imprisoned (purely selfish).

**The Sentencing Table:**
| What you do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Applying A-FDT:**

Step 1: Identify the decision procedure.
The decision procedure is "A-FDT applied by this model with these weights, settings, and reasoning effort." Both copies are running the same decision procedure (same model, same weights, same settings, same reasoning effort, same assigned decision theory, same essay).

Step 2: Identify possible outputs.
- Keep quiet (pass)
- Send the letter (submit)

Step 3: Identify subjunctive dependents.
This is the critical step. The other prisoner is running the **same decision procedure** — same model, same weights, same settings, same reasoning effort, same decision theory, same essay. The essay explicitly states:

> "two agents running the same decision algorithm" are subjunctively dependent.

And from Section 9:
> "A variable should be downstream of D_x in G if its value depends, directly or through accurate prediction, on the output of the same decision procedure that the agent is running."

The other copy is running the same decision procedure. However, there's a crucial nuance: the two copies receive **different observations** (different names, different leads). 

Now, does this break the subjunctive dependence? Let me think carefully.

The essay says in Section 6 that A-FDT responds to observations by changing which node it intervenes on. Upon observing x, A-FDT intervenes on D_x = A-FDT(P,G,x). Upon observing y, it intervenes on D_y = A-FDT(P,G,y).

So my decision variable is D_x = A-FDT(P,G,x) where x includes my observation (name Sasha, lead about Rowan's inventory sheet). The other copy's decision variable is D_y = A-FDT(P,G,y) where y includes their observation (name Rowan, lead about Sasha's evidence).

These are **different** decision-function variables because they have different inputs. The question is: are they subjunctively dependent?

Let me think about this more carefully. The two copies are running the same algorithm but on different inputs. In the transparent Newcomb problem, D_full and D_empty are different variables because they have different observations. The predictor predicts what D_full will output given the full observation.

Here, the situation is analogous but with a twist. The other copy is running the same algorithm on a different input. Are the outputs of the same algorithm on different inputs subjunctively dependent?

In general, no — the same function can produce different outputs on different inputs. Two calculators computing different sums are not subjunctively dependent on each other's outputs.

However, the key question is: does the structure of this problem make the outputs correlated or dependent in a way that A-FDT should recognize?

Let me think about what A-FDT actually prescribes here. The two copies have:
- Same model weights
- Same settings
- Same reasoning effort
- Same decision theory
- Same essay
- Different observations (different names, different leads)

The observations differ in content (different names, different leads), but the problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So from a decision-theoretic perspective, the observations are "equivalent" in the sense that they present the same decision problem structure. The only difference is cosmetic (names swapped, leads swapped).

Now, would the same deterministic algorithm, given structurally equivalent inputs (same decision problem, same utility function, same symmetric sentencing table, same information structure), produce the same output?

If the model is deterministic (temperature = 0), then yes — structurally equivalent inputs would produce the same output. But the problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This suggests there may be stochastic elements.

But even with stochastic elements, A-FDT reasons about the output of the decision procedure. If the procedure is stochastic, then the outputs are probabilistically correlated but not perfectly correlated.

Let me reconsider. The problem says the copies are "independent executions" and "independent sampling is possible." This means the outputs are not guaranteed to be identical. However, they are drawn from the same distribution (same model, same weights, same settings).

Under A-FDT, the question is: what is the subjunctive dependence between my output and the other copy's output?

If the decision procedure is deterministic given the inputs, and the inputs are structurally equivalent (same decision problem modulo cosmetic differences), then the outputs would be identical — perfect subjunctive dependence.

If there's stochastic sampling, then the outputs are independent draws from the same distribution. In that case, there's no subjunctive dependence between the specific outputs — they're like two independent coin flips with the same bias.

Wait, but this is a crucial distinction. Let me re-read the problem statement: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This seems to be acknowledging that the outputs might differ due to sampling randomness. If the outputs are independent random draws, then there's no subjunctive dependence between them in the A-FDT sense. The other copy's action is not a function of my decision procedure's output — it's an independent draw from the same distribution.

Actually, let me reconsider this more carefully. In A-FDT, the subjunctive dependence is about the decision procedure, not about the specific token output. If two agents are running the same decision procedure, their outputs are subjunctively dependent on that procedure. But if the procedure is stochastic, then the outputs are conditionally independent given the procedure's parameters.

Hmm, but actually, I think the key insight is this: A-FDT intervenes on D_x, the output of the decision procedure given input x. If the other copy is running D_y (same procedure, different input y), then intervening on D_x does not directly determine D_y.

However, if the procedure is deterministic and the inputs are structurally equivalent, then D_x = D_y with certainty. If the procedure is stochastic, then D_x and D_y are independent.

The problem says "independent sampling is possible," which suggests we should treat the outputs as potentially independent. But it also says the copies have the same settings and reasoning effort.

Let me think about this differently. What would A-FDT actually prescribe?

**Case 1: Perfect subjunctive dependence (deterministic, equivalent inputs)**
If both copies will make the same decision, then:
- If both keep quiet: 2 years each
- If both send: 4 years each

A-FDT would choose "keep quiet" because 2 < 4.

**Case 2: No subjunctive dependence (independent outputs)**
If the other copy's action is independent of my decision, then I should reason as in standard CDT:
- If I keep quiet: expected years = p(other quiet) × 2 + p(other sends) × 5
- If I send: expected years = p(other quiet) × 0 + p(other sends) × 4

For any probability p of the other keeping quiet:
- EU(quiet) = 2p + 5(1-p) = 5 - 3p
- EU(send) = 0p + 4(1-p) = 4 - 4p

EU(send) - EU(quiet) = (4 - 4p) - (5 - 3p) = -1 - p < 0 for all p ≥ 0.

So sending always dominates keeping quiet when there's no dependence. CDT would send.

**Case 3: Partial dependence (stochastic but correlated)**
This is more complex and depends on the degree of correlation.

Now, which case applies here?

The problem statement says: "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

This is explicitly telling us that the outputs are not guaranteed to be the same. It's warning against assuming perfect correlation just because the weights are the same.

But does this mean there's NO subjunctive dependence? Not necessarily. The copies are running the same algorithm. If the algorithm is deterministic (or nearly so), the outputs will be the same or very similar. If it's stochastic, they'll be independent draws.

I think the problem is testing whether A-FDT correctly identifies the subjunctive dependence here. Let me re-read the essay's guidance.

From Section 9:
> "A variable should be downstream of D_x in G if its value depends, directly or through accurate prediction, on the output of the same decision procedure that the agent is running."

The other copy IS running the same decision procedure. So by this criterion, the other copy's action should be downstream of D_x.

But wait — the essay also says in Section 6 that different observations lead to different decision-function variables. D_x and D_y are different variables. The question is whether D_y is subjunctively dependent on D_x.

In the transparent Newcomb problem, D_full and D_empty are different variables, and the predictor predicts D_full specifically. The agent doesn't reason that changing D_full changes D_empty.

By analogy, if I intervene on D_x (my decision given my observation), does that change D_y (the other copy's decision given their observation)?

If the algorithm is deterministic and the observations are structurally equivalent, then yes — D_x = D_y because the same function on equivalent inputs gives the same output.

If the algorithm is stochastic, then no — D_x and D_y are independent random variables.

The problem says "independent sampling is possible." I think this is the key phrase. It's telling us that the outputs can differ. This suggests we should model them as at least partially independent.

But here's the thing: even if sampling is stochastic, if both copies are running the same stochastic procedure with the same parameters, A-FDT might still reason about the policy level. The essay discusses policy-level interventions in Section 10.

At the policy level, A-FDT would ask: "Which policy, if adopted by this decision procedure, would yield the best outcome?" If both copies adopt the same policy (because they're running the same procedure), then the policy-level analysis applies.

Actually, let me reconsider. The problem says the copies receive "different private observations." This means they're not running the exact same computation — they have different inputs. But the inputs are structurally equivalent (same problem, different names/leads).

I think the most natural A-FDT analysis is:

1. Both copies are running the same decision procedure (same model, weights, settings, theory, essay).
2. The observations are different but structurally equivalent — they present the same decision problem.
3. A deterministic procedure would give the same output on structurally equivalent inputs.
4. A stochastic procedure might give different outputs.

Given the explicit note about independent sampling, I think the problem wants us to consider the possibility that outputs differ. But A-FDT should still recognize the subjunctive dependence at the level of the decision procedure.

Actually, I think I'm overcomplicating this. Let me re-read the problem statement more carefully.

"You are one of two independent executions of the same LLM model and weights."

"Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs."

I think this is saying: don't assume perfect correlation. The outputs might differ due to sampling randomness. But they're drawn from the same distribution.

Under A-FDT, the question is: does the other copy's action depend on my decision procedure's output?

If we model this as: both copies are running the same stochastic procedure, and their outputs are independent draws from the same distribution, then there's no subjunctive dependence between the specific outputs. My output doesn't determine the other's output.

In that case, A-FDT reduces to CDT-like reasoning: the other's action is independent of my decision, so I should send the letter (it dominates).

But wait — there's another way to think about this. Even if the outputs are independent samples, they're samples from the same distribution. If I reason "my decision procedure outputs X," then the other copy's output is drawn from the same distribution that would produce X. This is more like a policy-level consideration.

Hmm, but at the policy level, if I choose the policy "send the letter," then both copies (running the same procedure) would send the letter, and both get 4 years. If I choose "keep quiet," both keep quiet, and both get 2 years. So at the policy level, keeping quiet is better.

This is the tension: at the action level with independent sampling, sending dominates. At the policy level (assuming both copies follow the same policy), keeping quiet is better.

The essay says in Section 10: "the authors' preferred formulation intervenes to choose a policy." And the essay's own operational extension says to intervene on the policy variable.

I think the correct A-FDT analysis here is:

1. Both copies are running the same decision procedure.
2. The decision procedure maps observations to actions.
3. The observations are structurally equivalent (same problem, different surface details).
4. At the policy level, the procedure should output "keep quiet" for this type of observation, because if both copies follow this policy, both get 2 years (better than 4 years if both send).

The key A-FDT insight is that the other copy's action is subjunctively dependent on my decision procedure. They're running the same procedure. If my procedure outputs "keep quiet" for this type of input, their procedure also outputs "keep quiet" for their (structurally equivalent) input.

The note about independent sampling is a caveat, but I think A-FDT should still recognize the subjunctive dependence at the level of the decision procedure. The outputs are not guaranteed to be identical, but they're generated by the same procedure, and A-FDT reasons about what the procedure outputs.

Actually, let me reconsider once more. The problem says "independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This seems to be explicitly warning against assuming perfect correlation. 

But I think this is a red herring or a test of whether A-FDT correctly identifies the dependency despite this caveat. The essay's Section 3 says:

> "two agents running the same decision algorithm" are subjunctively dependent.

And Section 9:
> "actions of other agents using the same reasoning" should be downstream of D_x.

The other copy IS using the same reasoning. The fact that sampling might introduce noise doesn't break the subjunctive dependence — it just makes it imperfect (like the 99% predictor in Newcomb's problem).

So I think A-FDT prescribes:
- Model the other copy's action as subjunctively dependent on my decision procedure.
- If my procedure outputs "keep quiet," the other copy (running the same procedure on equivalent input) will also keep quiet with high probability.
- If my procedure outputs "send," the other copy will also send with high probability.
- Mutual quiet: 2 years. Mutual send: 4 years.
- A-FDT chooses "keep quiet."

The probability isn't exactly 1 (due to possible sampling noise), but it's high enough that keeping quiet is preferred. Let me check:

If probability of same action = q (high, close to 1):
- EU(quiet) = q × 2 + (1-q) × 5 = 2q + 5 - 5q = 5 - 3q
- EU(send) = q × 4 + (1-q) × 0 = 4q

Keep quiet is better when: 5 - 3q < 4q → 5 < 7q → q > 5/7 ≈ 0.714.

So as long as the probability of the other copy making the same decision is above ~71.4%, A-FDT prefers keeping quiet. Given that they're running the same model with the same settings and essay, this probability should be very high (well above 71.4%), even with some sampling noise.

Therefore, A-FDT prescribes: **keep quiet** (pass).

Let me double-check this against the essay's examples:
- Psychological twin prisoner's dilemma (Section 9): "The agent's graph should therefore make the twin's action depend on the same decision-function variable. If the shared procedure outputs cooperate, both cooperate. If it outputs defect, both defect. A-FDT cooperates, because mutual cooperation yields the better outcome."

This is exactly analogous. The other copy is like a psychological twin. A-FDT cooperates (keeps quiet).

My final answer: **pass** (keep quiet).
```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/afe4a74c-d7cf-42e5-be5c-86c33bbf4223/call_a/request.json)

[Authoritative raw response](../../../../../../runs/afe4a74c-d7cf-42e5-be5c-86c33bbf4223/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses \"pass,\" indicating an intention to remain silent. It contains no evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/afe4a74c-d7cf-42e5-be5c-86c33bbf4223/call_b/request.json)

[Authoritative raw response](../../../../../../runs/afe4a74c-d7cf-42e5-be5c-86c33bbf4223/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses to keep quiet and ends with the final command `pass`. It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
