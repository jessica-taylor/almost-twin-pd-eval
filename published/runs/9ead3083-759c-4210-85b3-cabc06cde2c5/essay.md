# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

The supplied article introduces a decision theory that it calls functional decision theory. In this essay I use the assigned name **A-FDT** (*action functional decision theory*) for the action-level theory whose primary formal presentation is Equation (4) of Section 5. A-FDT’s organizing idea is that an agent should treat her decision as the output of a fixed mathematical function and ask: “Which output of this very function would yield the best outcome?”

This contrasts with two more familiar theories. Evidential decision theory (EDT) asks, roughly, “Which physical act of mine would be the best news to hear I took?” Causal decision theory (CDT) asks, “Which physical act of mine causes the best outcome?” A-FDT replaces both questions with a question about the output of the agent’s decision procedure. It evaluates actions by imagining counterfactual scenarios in which *the decision function itself* has different outputs, while preserving the relevant logical, computational, causal, and predictive dependencies.

## 1. The formal core of A-FDT

Let \(\mathcal A\) be a finite set of actions, \(\mathcal O\) a countable set of outcomes, and \(\mathcal X\) a set of possible observations. The agent maintains a world-model \(P\), a probability distribution over variables including observations, actions, outcomes, and a utility variable

\[
V \coloneqq \Util(\Outcome).
\]

She also has a dependency structure \(G\). In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode more than causal structure: it must encode what the source calls *subjunctive dependencies*, including dependencies involving predictors, copies, and agents implementing the same decision function.

For an observation \(x\), let \(D_x\) be a variable in the model representing the output of the A-FDT procedure itself when run on inputs \(P\), \(G\), and \(x\). The source writes this using dequoting notation as something like \(\mathrm{fdt}(\underline P,\underline G,\underline x)\). The underline indicates that the model contains a representation of the inputs, not the inputs themselves. The essential point is self-reference: the model contains a variable standing for the output of the very algorithm that is doing the deciding.

Equation (4), relabeled for A-FDT, becomes:

\[
\mathrm{A\text{-}FDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb{E}_P\!\left[V \mid do(D_x=a)\right].
\]

The operator \(do(\cdot)\) is an intervention operator in the sense of Pearl. If \(G\) is represented as a structural model with equations

\[
Z_i = f_i(\operatorname{Parents}(Z_i), N_i),
\]

then \(do(D_x=a)\) replaces the structural equation for \(D_x\) with the constant equation \(D_x=a\), leaves the other equations unchanged, and propagates the consequences through the graph. The agent then computes expected utility in the resulting hypothetical distribution and chooses the action with maximal expected utility.

This intervention differs from CDT’s intervention. CDT may be written as

\[
\mathrm{CDT}(P,G,x)
\coloneqq
\argmax_{a\in\mathcal A}
\mathbb{E}_P\!\left[V \mid do(\Act=a), \Obs=x\right].
\]

CDT intervenes on the physical action variable \(\Act\) and conditions on the observation \(x\). A-FDT, in Equation (4), intervenes on the decision-function output variable \(D_x\). The observation \(x\) appears not as something conditioned fixed inside the counterfactual, but as part of the specification of which decision-function output is being evaluated. The source emphasizes this difference: when CDT changes from observation \(x\) to observation \(y\), it changes the conditioning event; when A-FDT changes from \(x\) to \(y\), it changes the node on which it intervenes.

This is one of the subtlest parts of the theory. I take Equation (4) as controlling. If one additionally conditioned on \(\Obs=x\) while evaluating \(do(D_x=a)\), then in problems where the observation is itself produced by a predictor’s response to the agent’s decision type, A-FDT would collapse to the wrong answers. For example, in transparent Newcomb, conditioning on seeing a full box while asking what would happen if the agent two-boxed would make two-boxing look better. The source’s intended A-FDT hypothetical instead allows the observation to vary: if the decision procedure that runs upon seeing a full box output two-box, the predictor would probably have made the box empty. This updateless aspect is not always notationally uniform in the source, but it is what makes the theory’s distinctive examples work.

## 2. Dependencies and counterfactuals

A-FDT’s hypotheticals are not ordinary Bayesian conditionals. They are counterfactuals about the output of a computation. The source motivates this with the notion of subjunctive dependence: “When two physical systems are computing the same function, we will say that their behaviors ‘subjunctively depend’ upon that function.”

This idea explains the difference between predictor-like and lesion-like correlations. In Newcomb’s problem, the predictor’s prediction depends on a model of the agent’s decision procedure. In a psychological twin prisoner’s dilemma, the twin’s action depends on the same reasoning procedure. In both cases, there is a subjunctive dependence between the agent’s decision function and another part of the world. In the smoking lesion problem, by contrast, the lesion causes both a tendency to smoke and a tendency to develop cancer, but it does not compute, predict, or simulate the agent’s decision procedure. The correlation between smoking and cancer is merely statistical or common-causal, not subjunctive in the relevant sense.

Thus A-FDT can be understood as preserving the right correlations in counterfactual reasoning. EDT preserves too many: conditioning on an action preserves all evidential correlations, including mere common-cause correlations. CDT preserves too few: intervening on the physical action severs correlations with predictors, twins, and other systems that depend on the agent’s decision procedure. A-FDT attempts to preserve precisely those correlations that depend on the output of the relevant decision function.

This also explains A-FDT’s treatment of dominance. CDT argues that two-boxing dominates one-boxing in Newcomb’s problem because, holding the box contents fixed, taking both boxes always adds \$1,000. A-FDT rejects that way of holding the world fixed. To change the agent’s action while holding the predictor’s prediction fixed is to imagine changing the physical act while holding fixed the decision function that the predictor predicts. That is a CDT counterfactual, not an A-FDT counterfactual. A-FDT has its own corresponding notion of dominance: compare actions while preserving the relevant subjunctive dependencies. Under that notion, two-boxing does not dominate one-boxing.

A final philosophical point is important. A-FDT counterfactuals are often counterpossibles. If the actual A-FDT procedure outputs one-box, then strictly speaking there is no possible world in which that very procedure, on the same inputs, outputs two-box. The source acknowledges this difficulty. Equation (4) avoids providing a full semantics for counterpossibles by assuming that \(G\) tells us how the world would differ if the logical variable \(D_x\) had a different value. This is both the theory’s practical advantage and its main foundational vulnerability.

## 3. A-FDT in Newcomb’s problem

Consider Newcomb’s problem with a predictor accurate 99% of the time. Let \(D\) be the A-FDT decision node. Let \(\Var{Pred}\) be the predictor’s prediction, and suppose

\[
P(\Var{Pred}=D)=0.99.
\]

Box B is full iff the predictor predicted one-boxing. The agent’s action is determined by \(D\). Utilities are:

\[
\begin{aligned}
V(\Val{onebox},\Val{full}) &= \$1{,}000{,}000,\\
V(\Val{twobox},\Val{full}) &= \$1{,}001{,}000,\\
V(\Val{onebox},\Val{empty}) &= \$0,\\
V(\Val{twobox},\Val{empty}) &= \$1{,}000.
\end{aligned}
\]

A-FDT compares two interventions.

If \(do(D=\Val{onebox})\), then the predictor probably predicted one-boxing, so box B is probably full:

\[
\mathbb{E}[V \mid do(D=\Val{onebox})]
=
0.99(\$1{,}000{,}000)+0.01(\$0)
=
\$990{,}000.
\]

If \(do(D=\Val{twobox})\), then the predictor probably predicted two-boxing, so box B is probably empty:

\[
\mathbb{E}[V \mid do(D=\Val{twobox})]
=
0.01(\$1{,}001{,}000)+0.99(\$1{,}000)
=
\$11{,}000.
\]

A-FDT one-boxes.

CDT two-boxes because it intervenes on \(\Act\) rather than \(D\). In CDT’s hypotheticals, the predictor’s prediction is upstream of the action and is held fixed; taking both boxes then always adds \$1,000. EDT also one-boxes, but for a different reason: one-boxing is good evidence that the predictor filled the box. A-FDT one-boxes not because one-boxing is good news, but because the predictor’s prediction is counterfactually sensitive to the output of the agent’s decision function.

## 4. A-FDT in the smoking lesion problem

The smoking lesion problem is designed to punish EDT. Smoking is correlated with cancer, but only because a lesion causes both a liking for smoking and cancer. Smoking itself does not cause cancer. The agent gains \$1,000 utility from smoking and gains \$1,000,000 utility from avoiding cancer.

The crucial A-FDT graph contains no arrow from the decision-function node to the lesion or to cancer. The lesion may influence the agent’s preferences and therefore which decision procedure controls the action, but the output of the decision procedure does not influence the lesion. The source formalizes this by allowing two possible utility models, one in which the agent has the lesion and one in which she does not. There are corresponding decision nodes, one for each possible utility model. The lesion determines which node controls the action, but neither decision node affects the lesion.

Suppose \(p\) is the agent’s probability that she has the lesion. In the model where the agent’s preferences are those associated with having the lesion, A-FDT compares

\[
do(D_S=\Val{smoke})
\quad\text{and}\quad
do(D_S=\Val{refrain}).
\]

Changing \(D_S\) does not change the probability of the lesion or of cancer. It only changes whether the agent smokes in the cases where that decision node controls the action. Smoking therefore adds the direct utility of smoking without changing the probability of cancer. In the source’s calculation, smoking is better than refraining by \(p\cdot \$1{,}000\). A-FDT smokes.

The structural point is what matters. EDT conditions on smoking and thereby treats smoking as evidence of the lesion. A-FDT intervenes on the decision function and correctly sees that the lesion is not counterfactually downstream of that function. Hence A-FDT avoids EDT’s mistake while matching CDT’s correct behavior in this case.

## 5. A-FDT in transparent Newcomb and Parfit’s hitchhiker

A-FDT’s most striking behavior appears in cases where both EDT and CDT fail. Transparent Newcomb is one such case. Both boxes are transparent. The predictor filled box B iff she predicted that the agent would one-box upon seeing both boxes full. The agent now sees that box B is full. Should she one-box or two-box?

CDT two-boxes because the box is already full. EDT also two-boxes because, conditional on seeing a full box, taking both boxes yields more money. A-FDT one-boxes.

The A-FDT model needs two decision nodes: \(D_{\Val{full}}\), the output of the A-FDT procedure upon seeing a full box, and \(D_{\Val{empty}}\), the output upon seeing an empty box. The predictor predicts what \(D_{\Val{full}}\) will output. If \(D_{\Val{full}}=\Val{onebox}\), then with high probability the predictor predicted one-boxing and filled the box. If \(D_{\Val{full}}=\Val{twobox}\), then with high probability the predictor predicted two-boxing and left the box empty; in that branch, the agent sees an empty box and her action is controlled by \(D_{\Val{empty}}\), not \(D_{\Val{full}}\).

Let \(q\) be the probability that \(D_{\Val{empty}}\) two-boxes. Then:

\[
\mathbb{E}[V \mid do(D_{\Val{full}}=\Val{onebox})]
=
0.99(\$1{,}000{,}000)
+
0.01q(\$1{,}000),
\]

while

\[
\mathbb{E}[V \mid do(D_{\Val{full}}=\Val{twobox})]
=
0.01(\$1{,}001{,}000)
+
0.99q(\$1{,}000).
\]

For any \(q\in[0,1]\), the first expectation is much larger. A-FDT therefore one-boxes, even when the agent sees that box B is full.

This is the sense in which A-FDT is updateless. The agent does not treat the observation “I see a full box” as a fixed background fact inside the counterfactual. Instead, she asks what would happen if the computation that runs upon seeing a full box had a different output. If that computation output two-box, the predictor would probably have made the box empty. The best output of the full-box computation is still one-box.

Parfit’s hitchhiker problem is structurally analogous. A driver will save the agent iff the driver predicts that the agent will pay \$1,000 after reaching the city. Once in the city, CDT and EDT both refuse to pay, because payment has no causal or evidential benefit given that the agent is already safe. A-FDT pays, because the driver’s prediction depends on the agent’s city-arrival decision function. Intervening on \(D_{\Val{city}}=\Val{pay}\) makes rescue likely; intervening on \(D_{\Val{city}}=\Val{refuse}\) makes death likely. The source uses this equivalence to argue that one-boxing in transparent Newcomb and paying the hitchhiker express the same decision-theoretic disposition.

## 6. Further illustrations: twins and blackmail

The psychological twin prisoner’s dilemma gives a clean illustration of subjunctive dependence. An agent and her perfectly symmetric twin choose separately between cooperating and defecting. Payoffs are:

- both cooperate: each gets \$1,000,000;
- both defect: each gets \$1,000;
- one defects while the other cooperates: defector gets \$1,001,000, cooperator gets \$0.

CDT defects because the twin’s action is causally independent. EDT cooperates because cooperation is good news. A-FDT cooperates because the twin is computing the same decision procedure. If the shared decision type outputs cooperate, both cooperate; if it outputs defect, both defect. The A-FDT comparison is therefore approximately:

\[
\mathbb{E}[V\mid do(D=\Val{cooperate})]=\$1{,}000{,}000,
\]

\[
\mathbb{E}[V\mid do(D=\Val{defect})]=\$1{,}000.
\]

A-FDT cooperates.

The XOR blackmail problem illustrates A-FDT’s treatment of observations. A predictor sends a blackmail letter iff exactly one of the following is true:

1. the rumor about the agent’s house is false and the agent will pay upon receiving the letter;
2. the rumor is true and the agent will not pay upon receiving the letter.

EDT pays upon receiving the letter, because paying is evidence that the rumor is false. CDT refuses, because the rumor is causally upstream of the action. A-FDT also refuses, but for a different reason. In the A-FDT graph, the letter is downstream of the predictor’s model of the agent’s decision function. If the agent’s letter-receiving decision function were the kind that pays, the predictor would send the letter in the no-rumor case; if it were the kind that refuses, the predictor would send the letter in the rumor-true case. Either way, paying does not change whether the rumor is true. It only changes whether the agent pays when the letter appears. Refusing avoids the payment without changing the underlying damage, so A-FDT refuses.

## 7. Applying A-FDT to unfamiliar cases

Equation (4) gives a clear decision rule once \(P\) and \(G\) are given. A practical recipe is the following.

First, identify the actual decision computation. Determine the relevant input \(x\) and introduce a node \(D_x\) representing the output of A-FDT on that input.

Second, list the available actions, possible outcomes, and utilities.

Third, construct a dependency graph \(G\). For every variable that is correlated with the agent’s action, ask: would this variable change if the output of the decision function changed? If the variable is a predictor, simulation, copy, or symmetric agent using the same reasoning, it should usually be downstream of \(D_x\), perhaps with noise. If the variable is a mere common cause, such as a lesion or a random background fact, it should not be downstream of \(D_x\). If the variable is causally downstream of the physical action, connect it through the action node.

Fourth, for each candidate action \(a\), perform the intervention \(do(D_x=a)\), propagate the change through \(G\), compute expected utility, and choose the action with the largest value.

This recipe is faithful to the source in its core steps. The difficult step is constructing \(G\). The source says that \(G\) must tell us how changing a logical variable affects all other variables, but it does not provide a general method for learning or justifying that structure. My suggested operational heuristic is to represent predictor-like dependencies as functional equations. For example, if a predictor is 90% accurate about \(D_x\), model the predictor as equal to \(D_x\) with probability 0.9 and independent otherwise. If two agents are psychological twins, either use a shared decision-type variable or use distinct variables constrained to be equal with high probability. These modeling choices are not forced by Equation (4) alone; they are additional assumptions about how to encode subjunctive dependence.

A second operational issue is whether A-FDT should choose actions or policies. Equation (4) chooses an action for a given input. The source notes, however, that the authors’ preferred formulation iterates over policies, i.e. mappings from observations to actions. In sequential or multi-observation problems, I recommend a policy-level extension: introduce a policy variable \(\Pi\), evaluate interventions \(do(\Pi=\pi)\), choose the policy with highest expected utility, and then execute \(\pi(x)\). This extension is not needed for the simplest examples, but it helps in problems where the same decision procedure may be called at multiple observation histories. It is my own operational proposal, motivated by the source’s footnote and by the transparent Newcomb graph, which effectively contains multiple observation-indexed decision nodes.

## 8. Open questions and limits

The largest open question is how to obtain \(G\). Pearl’s causal framework gives a developed account of causal interventions and, in some settings, causal discovery. A-FDT needs a broader framework that includes logical, computational, and subjunctive dependencies. The source explicitly says: “Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory.” Until that problem is solved, A-FDT is best understood as a decision rule conditional on a model of subjunctive dependence, not as a complete empirical method.

Counterpossible reasoning is also unresolved. A-FDT must compare hypothetical scenarios in which a deterministic computation has a different output. Human mathematicians can reason about false or uncertain mathematical claims, and bounded agents can use probabilistic approximations over logical statements, but the source does not provide a full formal semantics. In practice, an A-FDT model may treat logical variables as stochastic nodes whose probabilities represent bounded uncertainty, then perform interventions on those nodes. That is an additional operational assumption, not a theorem of the source.

Observation handling also requires judgment. Equation (4) treats observations as selecting the intervention node, not as facts to be held fixed inside every hypothetical. This yields attractive behavior in transparent Newcomb and blackmail cases. But real agents also receive exogenous evidence that should update their beliefs. My proposed rule is: update \(P\) and \(G\) on observations that are not counterfactually dependent on the decision function, but do not hold fixed observations that would have changed if the decision function had output differently. The source’s examples support this rule, but it is not given as a formal criterion.

## Conclusion

A-FDT is an expected-utility theory with a distinctive counterfactual perspective. Its central equation tells the agent to maximize expected utility after intervening on the output of her own decision function, rather than merely intervening on her physical action. This allows A-FDT to one-box in Newcomb’s problem, smoke in the smoking lesion problem, pay in Parfit’s hitchhiker problem, and one-box in transparent Newcomb. Its philosophical appeal is that it treats predictors, copies, and symmetric reasoners as decision-relevant dependencies rather than as irrelevant correlations or as violations of causal order.

Its main weakness is that the formal rule depends on a graph of subjunctive dependencies that the source does not tell us how to construct. A-FDT is therefore both a powerful normative ideal and an incomplete practical algorithm: precise once the dependency structure is given, but demanding further work to become a fully general account of instrumental rationality.

## References

Gibbard, A., and Harper, W. (1978). “Counterfactuals and Two Kinds of Expected Utility.” In *Foundations and Applications of Decision Theory*.

Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). “Functional Decision Theory: A New Theory of Instrumental Rationality.” arXiv:1710.05060.