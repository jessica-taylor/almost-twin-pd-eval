# P-FDT: Choosing a Policy as the Output of a Decision Function

A decision can influence the world without physically causing every relevant event. A predictor may have acted yesterday on a simulation of the decision we are making today. An independently acting copy may reach the same conclusion because it runs the same reasoning. In such cases, changing the answer of a decision procedure in a hypothetical may change several things at once, even when the corresponding physical actions cannot communicate.

**Policy functional decision theory**, or **P-FDT**, applies this thought to *policies*: rules mapping inputs to actions. It asks which policy the decision procedure should output, evaluates candidate policies using counterfactuals that preserve their relevant dependencies, and then applies the selected policy to the input actually received.

The primary source for this policy formulation is footnote 16 of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper’s main text instead presents a simpler action-selection formulation, which it says is sufficient for its examples. Footnote 16 gives the central policy-selection idea, but not a complete algorithm for every case. The formalization below is therefore an interpretation: it develops the footnote using the paper’s broader account of functional counterfactuals, while identifying further assumptions where they matter.

## 1. Why select policies?

Let \(x\) denote an agent’s information or decision input, and let \(\mathcal A(x)\) be the actions available on that input. A deterministic policy is a function

\[
\pi:x\longmapsto \pi(x)\in\mathcal A(x).
\]

For example, a policy for a transparent-box problem might say:

\[
\pi(\text{full})=\text{one-box},\qquad
\pi(\text{empty})=\text{two-box}.
\]

A policy can prescribe an action even for an input that is not actually encountered. That matters when someone predicts not simply what an agent does in the present circumstances, but what it *would* do under a specified observation.

Footnote 16 says that the authors’ preferred formulation intervenes on the decision-function node to choose “not an action but a *policy* which maps inputs to actions,” and that the agent then applies its inputs to that policy. Footnote 7 likewise describes iterating over policies. The paper says that the distinction appears to matter in some multi-agent dilemmas, although it sets the distinction aside in its worked examples.

Policy selection should not be confused with a physical promise made before a decision. A P-FDT agent need not have signed a contract or modified its body. Rather, the policy is the *output considered by the decision procedure itself*. Predictors, copies and other processes may depend on that output or on particular entries of the resulting policy.

## 2. Three ways to evaluate an alternative

Suppose an agent has utility \(U\), observations \(x\), and possible actions \(a\). Evidential decision theory (EDT) evaluates an action using a conditional expectation such as

\[
\mathbb E[U\mid X=x,A=a].
\]

It asks what taking \(a\) would be evidence about. Causal decision theory (CDT), in a standard graphical formulation, instead evaluates

\[
\mathbb E[U\mid X=x,\operatorname{do}(A=a)].
\]

Here the intervention changes the physical action and propagates its *causal* effects, while leaving causal antecedents unchanged.

P-FDT uses a different intervention point. It considers an alternative output of the policy-selection computation and propagates all modeled **subjunctive dependencies** on that output. These include causal effects, but can also include the output of a sufficiently accurate simulation, or the decision of a copy running the same relevant computation.

The distinction is neither “correlation versus no correlation” nor “past versus future.” A lesion can correlate with both a desire to smoke and cancer without evaluating the agent’s policy. A predictor can be physically in the past yet have based its prediction on a computation of that policy. P-FDT’s counterfactuals should preserve the latter kind of dependence when the model supports it, without automatically preserving every correlation.

## 3. A policy-selection model

Here is one useful formal interpretation. Let:

- \(\mathcal X\) be the domain of relevant inputs;
- \(\Pi\) be a set of admissible policies \(\pi:\mathcal X\to\mathcal A\);
- \(M\) be a probabilistic model containing outcomes, observations, actions and relevant dependencies;
- \(D(M)\) be the mathematical policy-selection computation;
- \(F\) be a node in \(M\) representing the output of \(D(M)\).

Write \(M_{\pi}\) for the hypothetical model constructed by intervening on \(F\) to make it output \(\pi\). Under the simplest version,

\[
F:=\pi,\qquad A:=\pi(X),
\]

with the consequences propagated through every part of the model that depends subjunctively on \(F\). The selected policy and actual action are then

\[
\pi^\ast\in\arg\max_{\pi\in\Pi}
\mathbb E_{M_{\pi}}[U],
\qquad
a^\ast=\pi^\ast(x).
\tag{1}
\]

A fixed tie-breaking rule makes the prescription determinate when several policies maximize value.

Equation (1) is **my proposed operational reading**, not an equation supplied by footnote 16. In particular, it takes \(M\) to use an appropriate decision-time *base perspective*: a distribution over the circumstances relevant to policy selection that need not fix the current observation in every hypothetical. The actual input \(x\) still determines the executed action through \(\pi^\ast(x)\).

This choice reflects a feature of the paper’s action-level formulation. There, observing \(x\) changes which computation node is intervened on; it does not simply add \(X=x\) as an ordinary condition to every hypothetical. Consequently, a hypothetical can assign positive probability to a different observation. Policy selection provides another way to express that global perspective: evaluate an entire input–action rule, including what happens when different inputs arise.

The base perspective is a substantive choice. Some information known at decision time may be appropriate to include in \(M\); some observation may itself depend on the policy and must be allowed to vary. Footnote 16 does not specify a universal rule for drawing that boundary. Blindly conditioning on all current observations can destroy the predictor dependence that motivates the theory; blindly ignoring all evidence would discard useful information. In unfamiliar cases, the boundary should be stated and tested rather than hidden in notation.

### What the intervention means

The equation \(F:=\pi\) does not assert that the agent physically changes mathematics. If \(D(M)\) is a fixed deterministic computation, it has one actual output. Alternatives in which it has a different output are **counterpossible**: their antecedents conflict with the actual mathematical fact about the computation.

The paper treats these hypotheticals as decision tools rather than literal beliefs about possible histories. Its graphical proposal supplies dependencies as part of the model, much as a causal graph supplies causal dependencies for a CDT calculation. But it acknowledges an important gap: there is no general, established method for discovering all logical or computational dependencies, or for extending causal-graph surgery to them. Equation (1) is therefore a recipe *conditional on a suitable model*, not a complete solution to counterpossible reasoning.

## 4. P-FDT in Newcomb’s problem

In Newcomb’s problem, box A contains \$1,000. Opaque box B contains \$1,000,000 if a predictor predicted one-boxing, and is otherwise empty. Assume that, under each policy counterfactual, the predictor correctly predicts the relevant choice with probability \(0.99\).

With a single relevant input, compare the policies \(\pi_1=\) one-box and \(\pi_2=\) two-box. P-FDT’s model changes both the actual choice and the predictor’s prediction when the policy output changes:

\[
V(\pi_1)=0.99(1{,}000{,}000)=990{,}000,
\]

\[
V(\pi_2)=0.01(1{,}000{,}000)+1{,}000=11{,}000.
\]

Thus the selected policy one-boxes. The predictor’s past act changes *in the hypothetical* because the model represents it as depending on the output being varied. This is not a claim that reaching for a box sends a physical signal backward in time.

The accuracy assumption must be counterfactual, not merely a statistic observed across unrelated people. A predictor that is 99% accurate overall might systematically fail on this agent or on one candidate policy. For an unfamiliar case, one needs estimates such as

\[
P(\text{predict one}\mid \operatorname{do}(F=\pi_1))
\quad\text{and}\quad
P(\text{predict one}\mid \operatorname{do}(F=\pi_2)),
\]

interpreted in the supplied subjunctive model. Their difference, rather than accuracy in the abstract, determines how strongly prediction favors one-boxing.

## 5. Observation-dependent policies: transparent boxes

Now make both boxes transparent. The predictor fills B if it predicts that the agent will one-box **upon seeing B full**. Consider a simple perfect-prediction model. If B is empty, taking both boxes gives \$1,000; if B is full, one-boxing gives \$1,000,000.

Compare two policies:

\[
\begin{array}{c|cc}
&\text{full}&\text{empty}\\ \hline
\pi_C&\text{one-box}&\text{two-box}\\
\pi_D&\text{two-box}&\text{two-box}.
\end{array}
\]

The predictor inspects the full-box entry. Under \(\pi_C\), it fills B, the agent sees full, and receives \$1,000,000. Under \(\pi_D\), it leaves B empty, the agent sees empty, and receives \$1,000. Thus, in this model, P-FDT selects \(\pi_C\).

The key is that the two hypotheticals need not have the same observation. Under \(\pi_D\), the full-box entry still matters to the predictor, even though the resulting observation is empty and that entry is not executed. Once the actual agent sees full, it applies \(\pi_C(\text{full})\) and one-boxes.

A CDT agent holding the observed full box fixed sees an extra \$1,000 available from two-boxing. An EDT agent conditioning on the full box also ordinarily prefers the extra \$1,000. P-FDT’s disagreement is not about the arithmetic conditional on a full box; it is about which hypothetical comparison should guide the policy output.

There is an important off-path qualification. With a perfect predictor, \(\pi_C\)’s empty-box entry is never executed, but specifying it still makes the policy complete. With a fallible predictor, that entry can affect expected value, and should be evaluated rather than treated as automatically irrelevant.

## 6. P-FDT against a psychological twin

Suppose two agents independently play the prisoner’s dilemma from the paper. Each receives \$1,000,000 if both cooperate, \$1,000 if both defect, \$1,001,000 if they alone defect, and zero if they alone cooperate.

If both implement the *same policy-selection computation on the same relevant input*, a model can represent their choices as two applications of the same policy output. P-FDT then compares:

\[
V(\text{cooperate})=1{,}000{,}000,\qquad
V(\text{defect})=1{,}000.
\]

Cooperation is selected. The agents do not need a causal channel between their rooms; the linkage is through the computation they share.

But “similar agents” is not enough to establish a perfect linkage. Suppose instead that, in the relevant counterfactual model, the opponent cooperates with probability \(q_C\) when the agent cooperates, and with probability \(q_D\) when the agent defects. Then

\[
V(C)=1{,}000{,}000q_C,
\]

\[
V(D)=1{,}001{,}000q_D+1{,}000(1-q_D).
\]

Cooperation is preferred exactly when the first quantity is larger. This makes the empirical burden visible: P-FDT does not instruct an agent to cooperate with every stranger, nor to assume that an opponent’s action changes merely because mutual cooperation would be desirable.

Policy selection also permits subtler multi-agent cases. Two copies may receive *different* observations while applying the same output policy. Their actions are then \(\pi(x_1)\) and \(\pi(x_2)\), not necessarily identical. Varying the whole policy can change both entries together. Conversely, if their policy selectors are genuinely different computations, an intervention on one need not replace the other’s policy. Exactly when two selectors count as sufficiently linked is an unresolved modeling question, not something footnote 16 settles.

## 7. P-FDT and the smoking lesion

In the imaginary smoking-lesion problem, a lesion makes smoking desirable and also raises the chance of fatal cancer. Smoking itself does not cause cancer, and the agent gains 1,000 units of utility by smoking.

An EDT calculation can make smoking look like bad news about the lesion. In a P-FDT model, however, changing the policy output does not thereby change the lesion or its carcinogenic effect. If the probability of survival is \(p\) under both policy hypotheticals, then, in the simplified case where smoking has the stated value,

\[
V(\text{smoke})=1{,}000{,}000p+1{,}000,
\qquad
V(\text{refrain})=1{,}000{,}000p.
\]

P-FDT smokes. This is a statement about the stipulated imaginary case, not about real smoking.

The paper notes that a fully specified lesion model is more awkward than the informal story suggests: preferences, knowledge of preferences and correlations between action and lesion must fit together. Some versions of EDT also smoke after accounting for relevant self-knowledge. The durable lesson is narrower: a P-FDT model should not treat every statistical association between an action and an outcome as a dependency of the outcome on the policy output.

## 8. Threats, errors and policy value

The paper’s mechanical blackmail case illustrates why a policy can be evaluated by what it tends to bring about even after an unfavorable observation. A blackmailer starts a damaging program only if she predicts that the agent would pay upon receiving a demand. Payment costs \$1,000; refusal after the program starts costs \$1,000,000.

For a simple model, suppose a pay-on-demand policy is always predicted correctly, while a refuse-on-demand policy is mistakenly targeted with probability \(\epsilon\). Then

\[
V(\text{pay policy})=-1{,}000,\qquad
V(\text{refuse policy})=-1{,}000{,}000\epsilon.
\]

P-FDT selects refusal when \(\epsilon<0.001\), and payment when \(\epsilon>0.001\), assuming no other consequences. If refusal is selected but a demand arrives because of prediction error, the selected policy still says refuse.

This conclusion depends on the model. If the threat was issued independently of any prediction, refusing may simply trigger the damage. If different blackmailers have different error rates or motives, those differences belong in the policy inputs and in \(M\). Nor is a low *actual* frequency of threats by itself proof that refusal caused the low frequency. The relevant question is how the threat process varies across policy hypotheticals.

## 9. Applying P-FDT without assuming the answer

For a new problem, the following procedure makes the theory’s commitments explicit:

1. **Define inputs and policies.** Include relevant observations and histories, not just the action available now. State which policies are feasible.
2. **Identify the selector and its links.** Model predictors, simulations, copies and later applications of the policy. Do not infer a link solely from resemblance or correlation.
3. **Construct policy hypotheticals.** Set the modeled selector output to each candidate policy. Recompute relevant causal and computational consequences, including observations that depend on the policy.
4. **Evaluate utility.** Average outcomes using the probabilities appropriate to each hypothetical, including errors and off-path observations.
5. **Select and apply.** Choose a maximizing policy, then execute its prescribed action on the actual input.
6. **Test assumptions.** Vary predictor reliability, the policy domain, the evidence used in the base perspective, and the strength of links to other agents. If the answer changes, report the threshold.

Several choices remain open. A policy may be stochastic rather than deterministic, but one must distinguish a predictable pseudorandom seed from a genuinely unpredictable draw. Multiple agents may have different utilities or inputs; shared code alone does not imply identical actions. Self-reference also requires care: representing a selector’s output is not the same thing as already knowing that output, and the existence of a self-representing program does not by itself guarantee a well-defined optimum.

Finally, the paper argues that functional reasoning performs well in many “fair” problems, but it does not prove dominance over every decision theory. It acknowledges both that theories can be deliberately rewarded or punished and that a general definition of fairness remains open. Likewise, the claim that information has non-negative value needs assumptions about the available policies and how information affects predictors; it is not a theorem supplied by footnote 16 alone.

## Conclusion

P-FDT evaluates alternative **policy outputs**, not merely isolated physical acts. Its distinctive move is to let a policy hypothetical change whatever genuinely depends on that output—including predictions and linked computations—while leaving merely correlated background facts alone. This can explain one-boxing, twin cooperation and resistance to predictive blackmail within one framework.

The central difficulty is equally clear: the result is only as good as the model of policy dependencies and the perspective from which policies are valued. Footnote 16 supplies a powerful selection principle; turning it into a general-purpose algorithm remains an open problem.

**Reference:** Eliezer Yudkowsky and Nate Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, especially footnotes 7 and 16. [arXiv:1710.05060v2](https://arxiv.org/abs/1710.05060v2).