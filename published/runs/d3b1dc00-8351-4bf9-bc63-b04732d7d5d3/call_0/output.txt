# Action Functional Decision Theory

Action functional decision theory, which I will call **A-FDT**, is a decision theory that treats an agent’s choice as the output of a fixed mathematical decision function. The central normative question is not “Which physical act of mine causes the best outcome?”—the question associated with causal decision theory, or **CDT**—nor “Which act would be best news to learn I performed?”—the question associated with evidential decision theory, or **EDT**. Instead, A-FDT asks something closer to: “Which output of this very decision procedure would yield the best outcome?”

The supplied paper calls this theory functional decision theory; in this essay I use the assigned name **A-FDT** throughout. The primary formal definition is the paper’s Equation (4), Section 5. On that definition, A-FDT is an expected-utility theory that differs from CDT mainly in the locus of its counterfactual intervention: CDT intervenes on the physical action variable, while A-FDT intervenes on a variable representing the output of the agent’s decision function. This seemingly small change allows A-FDT to preserve decision-relevant correlations with predictors, copies, twins, and simulations, while still ignoring merely statistical correlations of the sort that mislead EDT.

## 1. Expected utility and decision hypotheticals

All three standard theories discussed here—EDT, CDT, and A-FDT—are expected-utility theories. Given a countable set of outcomes \(o_1,o_2,\ldots\), a finite action set \(\mathcal A\), an observation history \(x\), and a utility function \(\mathcal U\), the expected utility of an action can be written schematically as

\[
\mathcal{EU}(a) := \sum_j P(a \hookrightarrow o_j; x)\,\mathcal U(o_j),
\]

where \(P(a \hookrightarrow o_j; x)\) is the probability of outcome \(o_j\) in the hypothetical situation in which action \(a\) is taken after observation \(x\). The theories differ in how they interpret the decision hypothetical connective \(\hookrightarrow\).

EDT interprets the hypothetical as ordinary Bayesian conditioning:

\[
\operatorname{EDT}(P,x)
:= \arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid \mathrm{Obs}=x, \mathrm{Act}=a\right],
\]

where \(P\) is the agent’s probability distribution and \(V\) is the utility variable. EDT therefore asks what would be likely to be true if it learned that it had taken \(a\).

CDT uses a causal intervention. In a Pearl-style causal model \((P,G)\), where \(G\) encodes causal structure, CDT chooses

\[
\operatorname{CDT}(P,G,x)
:= \arg\max_{a\in\mathcal A}
\mathbb E\left[V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x\right].
\]

The \(\mathrm{do}\)-operator sets \(\mathrm{Act}=a\) and propagates the change only along causal arrows. Correlations between the action and upstream variables are cut.

A-FDT keeps the expected-utility framework but changes the intervention target. Instead of surgically setting the physical action, it surgically sets the output of the agent’s decision function.

## 2. Equation (4) as the definition of A-FDT

In the paper’s Equation (4), the theory is defined as follows, adapted to the name A-FDT:

\[
\operatorname{A-FDT}(P,G,x)
:= \arg\max_{a\in\mathcal A}
\mathbb E\left[
V \mid
\mathrm{do}\!\left(
\operatorname{afdt}(\underline P,\underline G,\underline x)=a
\right)
\right].
\]

Here:

- \(P\) is the agent’s probabilistic world-model.
- \(G\) is a dependency graph describing how changes to logical, mathematical, computational, and causal variables affect other variables.
- \(x\) is the agent’s observation history.
- \(\mathcal A\) is the set of available actions.
- \(V\) is the utility variable.
- \(\operatorname{afdt}(\underline P,\underline G,\underline x)\) is a variable in the model representing the output of the A-FDT decision procedure when run on inputs \(P\), \(G\), and \(x\).
- The underlines indicate “dequoting”: the model contains a representation of its own inputs. The source notes that this self-reference is harmless in principle, because data structures can contain representations of themselves in the manner of Kleene’s recursion theorem.

The crucial term is

\[
D_x := \operatorname{afdt}(\underline P,\underline G,\underline x),
\]

the decision-function variable for the agent’s current situation. A-FDT evaluates each candidate action \(a\) by considering the hypothetical world obtained by intervening on \(D_x\) and setting it equal to \(a\). The expected utility of \(a\), relative to A-FDT, is therefore

\[
\mathcal{EU}_{\mathrm{A\text{-}FDT}}(a;x)
=
\mathbb E\left[V \mid \mathrm{do}(D_x=a)\right].
\]

A-FDT then chooses an action maximizing this quantity.

This intervention is not ordinary conditioning. If the agent conditions on \(\mathrm{Act}=a\), it may infer that the world is one in which \(a\) was likely all along. If the agent causally intervenes on \(\mathrm{Act}=a\), it holds fixed upstream predictors and only changes downstream causal consequences. A-FDT instead asks: what would the world look like if the output of this very decision function were \(a\)?

The paper emphasizes that A-FDT intervenes on a *logical* variable rather than a physical action variable. CDT intervenes on the token physical act; A-FDT intervenes on the decision type. If a predictor, twin, simulation, or copy depends on the same computation or on an accurate representation of that computation, then changing the output of the decision function in the hypothetical also changes the predictor’s prediction, the twin’s choice, or the simulation’s behavior.

## 3. Subjunctive dependence and the graph \(G\)

The graph \(G\) is the heart of A-FDT. In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode more than causation: it must encode what the paper calls **subjunctive dependence**.

Two systems are subjunctively dependent when their behavior is tied to the same mathematical function, or when one system reliably represents or predicts the output of the other’s computation. The paper’s paradigm examples are two calculators computing the same arithmetic sum, a predictor who accurately models an agent’s decision procedure, and a psychological twin who reasons in the same way. Causal dependence is a special case of subjunctive dependence: if a scribe copies a calculator’s output, the scribe’s writing is both causally and subjunctively dependent on the calculator’s computation.

Mere statistical correlation is not subjunctive dependence. If two calculators are both pink, that does not mean that changing one calculator’s output would change the other’s color. Likewise, a lesion that causes both a preference for smoking and lung cancer is not subjunctively dependent on the agent’s decision function unless the lesion somehow predicts, simulates, or computes that decision function.

The source says that A-FDT’s hypotheticals should preserve all decision-relevant subjunctive dependencies while breaking correlations that are merely evidential. This is the A-FDT analogue of CDT’s rule that causal interventions preserve causal structure and cut noncausal correlations.

The paper is explicit that this is where the theory is least complete. Pearl’s causal framework gives a mature account of how to learn and use causal graphs, but the paper says we do not yet have an equally satisfactory formal account of how to infer subjunctive dependency structure from observation and experiment. Thus Equation (4) is precise **given** a suitable \(G\), but constructing \(G\) remains an open problem.

A reasonable operational rule, which I take to be an extrapolation from the source rather than a fully settled part of the theory, is this:

1. Include an arrow from the decision-function variable \(D_x\) to the agent’s physical action, because the action is normally the implementation or output of that function.
2. Include arrows from \(D_x\) to variables representing accurate predictors, simulations, copies, or twins of the agent’s decision process.
3. Include downstream causal arrows from those predictors or actions to payoffs, observations, and other physical consequences.
4. Do not include arrows from \(D_x\) to variables that are merely common causes of action and outcome, such as lesions or background traits, unless those variables themselves compute, simulate, or predict the decision function.
5. Represent imperfect prediction by probabilistic or noisy dependencies rather than deterministic ones.

This rule is not a complete formal foundation for A-FDT, but it is sufficient to recover the paper’s central examples.

## 4. A-FDT in Newcomb’s problem

Newcomb’s problem involves a reliable predictor who has placed \$1,000,000 in an opaque box B if and only if she predicted that the agent would take only B. Box A visibly contains \$1,000. The predictor has already acted.

Let \(D\) be the A-FDT decision-function variable. The relevant graph has approximately the following structure:

\[
D \rightarrow \mathrm{Act},
\qquad
D \rightarrow \mathrm{Prediction},
\qquad
\mathrm{Prediction} \rightarrow \mathrm{BoxB},
\qquad
(\mathrm{Act},\mathrm{BoxB}) \rightarrow V.
\]

Suppose the predictor is 99% accurate. If A-FDT intervenes on \(D=\text{one-box}\), then the agent almost certainly one-boxes and the predictor almost certainly filled box B. The expected utility is approximately

\[
\mathbb E[V\mid \mathrm{do}(D=\text{one-box})]
=
0.99 \cdot \$1{,}000{,}000
+
0.01 \cdot \$0
=
\$990{,}000.
\]

If A-FDT intervenes on \(D=\text{two-box}\), then the predictor almost certainly predicted two-boxing, so box B is almost certainly empty. The agent takes both boxes and receives the visible \$1,000 in the likely case, but receives \$1,001,000 in the unlikely case where the predictor erred:

\[
\mathbb E[V\mid \mathrm{do}(D=\text{two-box})]
=
0.01 \cdot \$1{,}001{,}000
+
0.99 \cdot \$1{,}000
=
\$11{,}000.
\]

A-FDT therefore one-boxes.

CDT reaches a different conclusion because it intervenes directly on \(\mathrm{Act}\) while holding the predictor’s prediction fixed. In a CDT hypothetical, whether box B is full does not change when the agent reaches for box A. Two-boxing then always adds \$1,000, so CDT two-boxes. EDT also one-boxes, but because one-boxing is good evidence that the predictor filled the box. A-FDT one-boxes for a more CDT-like reason: it uses a counterfactual intervention, but the intervention is on the decision function, so the predictor’s prediction changes with it.

## 5. A-FDT and the smoking lesion

In the smoking lesion problem, smoking is correlated with lung cancer, but the correlation is caused by a common cause: a lesion that both makes smoking appealing and causes cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from not dying of cancer.

EDT refrains from smoking because smoking is bad news: it is evidence that the agent has the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The important graphical fact is that the lesion is not subjunctively dependent on the agent’s decision function. The lesion may influence the agent’s preferences, and it may therefore influence which decision function is being run, but the lesion does not predict or compute the output of that decision function. In a simplified A-FDT graph:

\[
D \rightarrow \mathrm{Act},
\qquad
\mathrm{Lesion} \rightarrow \mathrm{Cancer},
\qquad
\mathrm{Lesion} \rightarrow \text{preferences or decision-function selection},
\qquad
(\mathrm{Act},\mathrm{Cancer}) \rightarrow V,
\]

with no arrow \(D \rightarrow \mathrm{Lesion}\) and no arrow \(D \rightarrow \mathrm{Cancer}\).

Therefore, when A-FDT evaluates

\[
\mathbb E[V\mid \mathrm{do}(D=\text{smoke})]
\]

against

\[
\mathbb E[V\mid \mathrm{do}(D=\text{refrain})],
\]

the probability of having the lesion, and hence the probability of cancer, remains the same in both hypotheticals. Smoking adds its immediate benefit without changing the cancer risk. So A-FDT smokes.

The paper gives a more careful model in which the agent is uncertain about her own preferences because the lesion affects whether she likes smoking. In that model there are two possible decision functions, one associated with smoking-positive preferences and one associated with smoking-negative preferences. The intervention is applied to the branch that would actually control the action. Even there, changing the relevant decision-function variable does not change the probability of the lesion. The expected advantage of smoking is weighted by the probability that the intervened branch controls the action, but it remains positive. A-FDT therefore smokes.

This example shows how A-FDT avoids EDT’s mistake. EDT preserves the statistical correlation between smoking and cancer; A-FDT breaks it, because the correlation is not grounded in subjunctive dependence on the decision function.

## 6. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A-FDT’s treatment of observations becomes clearest in the transparent Newcomb problem. Both boxes are transparent. The predictor fills box B if and only if she predicts that the agent will leave box A behind **upon seeing that both boxes are full**. The agent finds herself seeing that both boxes are full. Should she take both?

CDT says take both: box B is already full, so taking A adds \$1,000. EDT also says take both, because conditional on seeing box B full, taking A is better news. A-FDT says leave box A behind.

To see why, let

\[
D_{\text{full}} := \operatorname{afdt}(\underline P,\underline G,\underline{\text{full}})
\]

be the decision-function variable corresponding to the case where the agent sees a full box B, and let

\[
D_{\text{empty}} := \operatorname{afdt}(\underline P,\underline G,\underline{\text{empty}})
\]

be the corresponding variable for seeing an empty box B. The predictor predicts what \(D_{\text{full}}\) will output. If she predicts one-boxing, she fills B; otherwise she leaves it empty. The observation then determines which decision-function variable controls the action. A simplified graph is:

\[
D_{\text{full}} \rightarrow \mathrm{Prediction},
\qquad
\mathrm{Prediction} \rightarrow \mathrm{BoxB},
\qquad
\mathrm{BoxB} \rightarrow \mathrm{Obs},
\]

and the action depends on \(D_{\text{full}}\) if the observation is full, but on \(D_{\text{empty}}\) if the observation is empty.

After seeing that B is full, A-FDT evaluates alternatives by intervening on \(D_{\text{full}}\), not by conditioning on \(\mathrm{Obs}=\text{full}\). If

\[
\mathrm{do}(D_{\text{full}}=\text{one-box}),
\]

then with high probability the predictor predicted one-boxing, box B is full, and the agent receives about \$1,000,000. With small probability the predictor erred, box B is empty, and the agent’s action is instead governed by \(D_{\text{empty}}\). If

\[
\mathrm{do}(D_{\text{full}}=\text{two-box}),
\]

then with high probability the predictor predicted two-boxing, box B is empty, and the agent is not actually in the full-box branch; she instead receives whatever \(D_{\text{empty}}\) prescribes in the empty-box case. In the paper’s calculation, the one-boxing hypothetical has expected utility roughly

\[
0.99 \cdot \$1{,}000{,}000 + 0.01 \cdot q \cdot \$1{,}000,
\]

where \(q\) is the probability that the agent two-boxes upon seeing an empty box. The two-boxing hypothetical is much lower, roughly around \$11,000 when \(q=1\). Therefore A-FDT one-boxes even when it sees both boxes full.

This is closely analogous to Parfit’s hitchhiker problem. An agent is stranded in a desert. A driver will rescue her only if she promises to pay \$1,000 after reaching the city, and the driver is extremely good at detecting whether the promise is sincere. Once in the city, paying \$1,000 brings no further causal benefit. CDT and EDT both refuse to pay once in the city, so the driver detects insincerity and leaves them in the desert. A-FDT pays, because the driver’s prediction depends on the output of the agent’s decision function in the city-arrival branch. If that function outputs “pay,” the driver rescues her; if it outputs “refuse,” the driver does not. The A-FDT agent therefore acts as she would have wanted to precommit to act.

The counterfactual reasoning is unusual but important. When A-FDT imagines two-boxing after seeing a full box, or refusing to pay after being rescued, it does not hold the favorable observation fixed. It imagines that, had the decision function output differently, predictors would likely have behaved differently, and the agent might well have had a different observation. This is one reason the theory has an “updateless” flavor.

## 7. Policies, observations, and open operational questions

Equation (4) evaluates actions. The source notes, however, that a policy-based formulation is often preferable: instead of choosing an action for the current observation, the agent chooses a policy \(\pi : \mathcal X \to \mathcal A\) mapping observations to actions. The policy analogue of A-FDT can be written as

\[
\pi^*
:=
\arg\max_{\pi}
\mathbb E\left[V \mid \mathrm{do}(\Pi=\pi)\right],
\]

where \(\Pi\) is a variable representing the policy output by the agent’s decision procedure. The agent then executes \(\pi^*(x)\) upon observing \(x\). This policy formulation is not the primary equation assigned here, but it is a natural operational extension and matches the paper’s remark that the authors’ preferred formalization iterates over policies. It is especially useful in multi-agent and sequential settings where other agents predict an entire strategy rather than a single act.

There is also a subtle ambiguity about observations. Equation (4) does not include an explicit condition \(\mathrm{Obs}=x\) inside the expectation. The paper explicitly says that when CDT’s observation changes from \(x\) to \(y\), CDT changes the conditioning from \(\mathrm{Obs}=x\) to \(\mathrm{Obs}=y\), whereas A-FDT changes the node on which it intervenes, from \(D_x\) to \(D_y\). This suggests that A-FDT does not respond to decision-relevant observations by conditioning inside the hypothetical. Instead, the observation determines which branch of the decision function is the locus of intervention.

Some of the paper’s later examples appear to write an additional observation condition, but the central prescriptions—especially transparent Newcomb and mechanical blackmail—require that the agent not hold the observation fixed when evaluating the counterfactual output of the decision function. If one conditions on seeing the full box while asking what would happen if the decision function output two-boxing, the attractive answer is to take both boxes. That would defeat the paper’s main argument. My operational interpretation, therefore, is this:

- Use background evidence to construct \(P\) and \(G\).
- Let the current observation \(x\) select the decision-function variable \(D_x\).
- Do not condition the counterfactual evaluation on \(\mathrm{Obs}=x\) if that observation is itself downstream of predictors of \(D_x\).
- If an observation is genuinely exogenous to the decision function and its predictors, conditioning on it or fixing it in the graph is harmless.

This interpretation is not fully spelled out in the source, but it seems necessary to recover the source’s stated prescriptions.

The larger open problem remains the construction of \(G\). The paper is clear that A-FDT works given a graph that accurately represents how changing the logical decision variable affects the rest of the world, but it does not provide a general method for learning such graphs. This is the main gap in the theory. A practical A-FDT agent would need to identify which environmental variables are predictors, simulations, copies, or logical dependents of its own decision procedure, and which are merely correlated common causes.

A related difficulty is that A-FDT’s counterfactuals are often counterpossibles. If the agent’s decision function in fact outputs one action, then asking what would happen if that very function output another action is asking for a scenario contrary to mathematical fact. The source acknowledges that we lack a fully satisfactory theory of counterpossible reasoning. Operationally, however, bounded agents may not need full counterpossible logic. They need only reliable heuristics for answering questions such as: “If my decision procedure were the sort that output \(a\) in this situation, what would accurate predictors expect?” Humans appear capable of rough versions of this reasoning, and artificial agents could encode such dependencies explicitly.

## 8. What A-FDT achieves

The source argues that A-FDT unifies the desirable features of CDT and EDT while avoiding their characteristic failures. Like CDT, A-FDT uses counterfactuals rather than mere conditional evidence. Like EDT, it can one-box in Newcomb’s problem and cooperate with predictors. Unlike EDT, it smokes in the smoking lesion problem and resists managing the news. Unlike CDT, it pays in Parfit’s hitchhiker, one-boxes in transparent Newcomb, and avoids unstable reasoning in predictor-laden games.

A-FDT also comes with its own notion of dominance. CDT says two-boxing dominates one-boxing in Newcomb’s problem because, holding the prediction fixed, taking both boxes is better. A-FDT replies that this holds fixed the wrong thing. If one holds fixed the subjunctive dependency structure and changes the decision function’s output, two-boxing no longer dominates: switching from one-boxing to two-boxing makes the predictor likely to have left the big box empty. Thus A-FDT avoids dominated actions relative to its own counterfactuals.

The source also claims that A-FDT agents do not need costly precommitments. They simply act as they would have wanted to precommit to act. This is why A-FDT can assign nonnegative value to information in cases where EDT would pay to avoid information. Seeing the full box in transparent Newcomb does not hurt the A-FDT agent, because her decision rule is not destabilized by the observation.

These claims are strongest in what the paper calls fair problems: problems where the environment rewards or punishes the agent for predictions about her actions, rather than punishing her for using A-FDT itself. No decision theory can be expected to win in environments specifically designed to punish its algorithm. But the paper claims that A-FDT performs at least as well as rival theories in fair problems, and it presents no fair counterexample.

## Conclusion

A-FDT is best understood as expected-utility maximization performed over counterfactual outputs of the agent’s own decision function. Its core formal rule, Equation (4), tells the agent to choose the action \(a\) that maximizes expected utility under an intervention setting the decision-function variable \(\operatorname{afdt}(\underline P,\underline G,\underline x)\) equal to \(a\). The theory’s power comes from its treatment of subjunctive dependence: accurate predictors, twins, simulations, and copies vary with the decision function in counterfactual evaluation, while merely statistical common causes do not.

The main unresolved issue is the construction of the subjunctive dependency graph \(G\). Until that problem is solved, A-FDT is best treated as a precise idealized criterion plus a family of operational heuristics for identifying which correlations in a world-model should be preserved under counterfactual intervention. With that caveat, A-FDT gives a coherent and attractive answer to many problems where CDT and EDT fail: it one-boxes when predictors reward predictable one-boxing, smokes when lesions are merely evidential, pays rescuers when payment was predicted, and refuses blackmail when refusal makes blackmail unprofitable.

## References

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Nozick, R. (1969). “Newcomb’s Problem and Two Principles of Choice.” In *Essays in Honor of Carl G. Hempel*. D. Reidel.

Parfit, D. (1986). *Reasons and Persons*. Oxford University Press.