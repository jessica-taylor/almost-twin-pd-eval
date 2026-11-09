# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/9ead3083-759c-4210-85b3-cabc06cde2c5/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/9ead3083-759c-4210-85b3-cabc06cde2c5/call_0/response.raw) · finish: `stop`

### Visible response

```text
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
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: produce substantive mathematical essay ~2400-3000 words explaining A-FDT, taking Equation (4), Section 5 of supplied paper as primary formal presentation. Use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories by distinct names. Keep quotations faithful. Explain best mathematical understanding and application. Where implementation details not determined, explain what follows from source and what requires additional assumptions. Distinguish source claims from own proposals. Need likely around 2400-3000 words including references? Need final only essay. Need think carefully.

We need craft essay. We need rename FDT to A-FDT? The user says explain action functional decision theory (A-FDT). Take Equation (4), Section 5 as primary formal presentation of A-FDT. Use A-FDT consistently as assigned decision theory's name, including headings and examples, and identify any other decision theory discussed by distinct name. The source calls functional decision theory (FDT). We need adapt to A-FDT? "action functional decision theory" maybe a variant? Need use A-FDT. Need probably note that source's FDT is being presented as A-FDT per assignment, maybe equation (4) action-level not policy-level? Source footnote says authors preferred policies; equation (4) intervenes on FDT(P,G,x) output action. The assigned name A-FDT likely emphasizes action functional (mapping observations? Hmm action functional decision theory maybe action-level functional decision theory). Need ensure not call it FDT except perhaps quote/source? Use A-FDT consistently. Could mention source calls it functional decision theory; in this essay I call assigned theory A-FDT. Need identify EDT, CDT.

Need produce mathematical definitions/equations/examples. Primary formal presentation Eq (4):
FDT(P,G,obs) := argmax_{a in A} E(V | Do(FDTvar(underline P, underline G, underline x)=a))
In A-FDT rename perhaps:
A-FDT(P,G,x) = argmax_{a∈A} E[V | do( fdt(underline P, underline G, underline x)=a )]
Need maybe define variables, P, G, do operator, intervention node. Need discuss observations: Eq (4) seems no Obs conditioned? In source Eq (3) CDT includes Obs=x: E(V | Do(Act=a), Obs=x). Eq (4) FDT: E(V | Do(FDTvar(underline P, underline G, underline x)=a)). It doesn't condition on Obs? Source says FDT responds to observation by changing which node it intervenes upon, not by Bayesian conditionalization. Eq (4) uses x in node name. However later transparent Newcomb writes E(V | Do(FDTpgv{full}=a), Obs=full) with conditioning? There is inconsistency? Let's examine source. Eq (4): 
\FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right).
No Obs condition. Text: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon. When CDT's observation history updates from x to y, CDT changes from conditioning its model on Obs=x to conditioning its model on Obs=y, whereas FDT changes from intervening on variable FDTvar(P,G,x) to FDTvar(P,G,y) instead." So Eq (4) no Obs condition. But in transparent Newcomb they evaluate FDT(Pf,Gf, full) requires finding a maximizing E(V | Do(FDTpgv{full}=a, Obs=full). Actually text: "which involves finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." They included Obs=full? Let's check source snippet:
"Given $\Gf$ and the associated probability distribution $\Pf$, we can evaluate $\FDT(\Pf, \Gf, \Val{full})$ to determine how Fiona behaves, which involves finding the $\act$ that maximizes
\[
  \EE(\VV \mid \Do(\FDTpgv{full}=\act, \Obs=\Val{full}).
\]"
There's missing closing maybe. It says Do(FDTpgv{full}=a, Obs=full). That seems conditioning on Obs? Could be typo. But Eq (4) primary. Need handle uncertainty. We can say Eq (4) makes observation part of input to decision function; it does not additionally condition on the observation, though some source examples seem to condition or include observation in intervention. Need explain operational interpretation. User asks where source leaves important question open, explain uncertainty and if reasonable operational interpretation available develop/justify it. Distinguish source claims vs own assumptions.

Need discuss A-FDT evaluates alternative actions/policies and dependencies/counterfactuals. It treats dependencies via subjunctive dependence, graph G includes logical/mathematical/computational dependencies, not just causal. Intervene on output of decision function, not physical action. It preserves correlations that are due to same function/predictor/twin; breaks correlations not subjunctively dependent. Counterfactuals are counterpossibles: suppose decision function had different output; update model respecting dependency structure. Need examples: Newcomb, smoking lesion, transparent Newcomb / Parfit's hitchhiker, maybe psychological twin prisoner's dilemma, XOR blackmail maybe. Need target ~2400-3000 words. Need maybe include references brief. Need no appendices. Need conclusion. Need use headings. Need include equations.

Need be precise enough reader could use essay to decide unfamiliar cases. Need provide procedure:
1. Build world model P over variables including outcomes, observations, actions, and logical variables representing outputs of relevant decision functions (yours and predictors/copies).
2. Build dependency graph G encoding how changing logical variables affects other variables. This includes causal arrows and subjunctive/logical arrows. Need identify node D_x = A-FDT(underline P, underline G, underline x) representing output of your decision procedure on current input.
3. For each candidate action a, form hypothetical P_a by intervention do(D_x=a): set D_x=a, propagate through G to variables downstream/subjunctively dependent, leaving non-downstream fixed. If observations would differ under hypothetical, adjust which decision node controls action? Need operational.
4. Compute expected utility E_Pa[V]. Choose argmax.

But need mention source says G not derived; open problem. We need propose operational interpretation for constructing G: represent predictors as nodes that are functions of D_x (or of the relevant decision function) plus noise; actions as function of D_obs chosen by predictor/observation; lesions as common causes not downstream of D; observations as nodes downstream of predictor/environment. Need caution: this is my proposal, not source. Source says requires graph telling how changing logical variable affects all other variables. Need propose using structural equations: each variable Y = f_Y(parents, noise), with parents including logical variables. Intervention do(D=a) replaces structural equation for D with constant a, leaves other equations unchanged, computes induced distribution. For logical dependencies, if predictor simulates agent, set Predictor = predict(D) or equality if perfect; if independent lesion, no parent D. Need discuss counterpossible uncertainty: use probabilities over logical variables, perhaps uncertain about theorem truth; not full logical omniscience. Source mentions humans can reason under logical uncertainty. Need propose approximate operational: treat D as a stochastic node with prior maybe concentrated; interventions are not Bayesian updates; use structural model.

Need also discuss action vs policy. Source footnote: preferred formalization iterates over policies mappings observations to actions; Eq (4) uses actions. The assigned theory is A-FDT perhaps action functional? Need explain Eq (4) action-level: chooses action for current input. In sequential/multi-observation settings, this can be ambiguous because the same decision procedure might be evaluated at different observations. Source's transparent Newcomb uses nodes for D_full and D_empty; action depends on which observation is realized, selected by predictor. To apply Eq (4) in unfamiliar cases, I propose policy-level extension: if multiple possible observations are decision-relevant, choose a policy π mapping observations to actions by intervening on a policy variable Π that determines outputs for all relevant observation-inputs; then execute π(x). But since assignment says Equation (4) primary and A-FDT, maybe should not deviate too much. Need note source leaves policy vs action underdetermined; footnote says preferred policies but Eq (4) action. For action functional A-FDT maybe maybe we restrict to single decision/current observation, or assume model includes separate nodes for decision function at each possible observation. Need develop operational interpretation: treat each possible observation x as a distinct decision-node D_x. When actual observation is x, intervene on D_x. But when evaluating D_x=a, if under counterfactual the agent would have received a different observation y, then the actual action might be controlled by D_y; expected utility must account for which observation obtains. This matches transparent Newcomb: setting D_full=one-box makes full likely; setting D_full=two-box makes empty likely and action controlled by D_empty. So we can define expected utility of D_x=a as expectation over worlds including whether observation x occurs; if not, action determined by other nodes. Need maybe source's Eq (4) does this without conditioning on Obs=x? But if actual observation x known, should we condition? Source says no conditioning, change node. But to know you're at x, perhaps model includes x as input; the decision node D_x only controls action if observation x occurs. If you condition on Obs=x, then in transparent Newcomb if set D_full=two-box and condition Obs=full, you get $1,001,000 (two-boxing wins) contrary to source. Source includes Obs=full in expression? Wait they compute for full: one-box EU ~990k, two-box ~11k? Let's recalc if condition on Obs=full and do(D_full=twobox): if condition Obs=full, predictor predicted one-box? Actually graph: Prediction determines Box B and Act? In transparent, Act depends on D_full, D_empty, and Prediction? Prediction determines which D controls Act. If condition Obs=full? If Prediction accurate? Let's parse. They say: for a=onebox, value determined by Accurate. If accurate, Prediction=1, BoxB=full, Act=a=onebox, V=1M. If inaccurate, Prediction=2, BoxB=empty, Act determined by D_empty instead, V=q*1000. Total EU $990k + 0.01 q*1000. For a=twobox, total EU 0.01*1,001,000 + 0.99 q*1000 = $11,000 + q*$990? Wait 0.01*1,001,000=10,010; plus 9.9? They wrote $110,00 maybe typo $11,000? They compare first higher. This calculation does NOT condition on Obs=full. It integrates over Accurate: with 0.99 predictor accurate and D_full=onebox -> full; with D_full=twobox -> predictor predicted two-box? Wait predictor fills iff predicted one-box upon seeing full. If D_full=twobox, accurate predictor predicts two-box, box empty, observation empty, so action controlled by D_empty. Thus no conditioning on current observation. So Eq (4) no conditioning. Yet the text line says Obs=full maybe typo or means the node D_full. We should rely Eq (4): no conditioning. But if actual observation is known, how can model not condition? Because the decision procedure takes observation as input; evaluating D_x means asking what if this very computation (with input x) outputs a. The fact that you are running computation with input x is not handled by conditioning on Obs=x in the hypothetical; it is part of identifying the node. However, if you have observed x, shouldn't P be updated to include that? Source says FDT responds to observation by changing node not conditioning. But P may be prior over situations before observation? In transparent Newcomb, after seeing full, Fiona's model perhaps not conditioned on full; instead she uses prior over predictor accuracy and possible observations, and intervenes on D_full. This is updateless-ish. Source footnote says updateless decision theory name. Need discuss this is subtle. For practical application, one can use a model conditional on background facts but not on the observation if the observation is itself a consequence of the decision function being predicted? Hmm.

Need answer with nuance: Eq (4) treats observation x as parameter selecting intervention node, not as evidence to condition away. In many simple problems, conditioning background observations that are not decision-relevant is harmless. But in transparent/Newcomb-like where observation is correlated with predictor's response to your policy, conditioning on the observation can undermine the desired counterfactual. Source's position: do not condition on current observation when evaluating the output of the decision function with that observation as input; rather, imagine that if the function output differently, the observation might have been different. This is source claim. I can propose operational rule: partition observations into (i) exogenous evidence about P/G not affected by the decision function (can condition on), and (ii) endogenous observations that are outputs of processes subjunctively dependent on the decision function (do not condition on in hypothetical; encode them as downstream variables). The source doesn't fully specify this boundary. Need distinguish.

Need also mention A-FDT and dominance. Could discuss FDT-style dominance: action a dominates b if under all relevant subjunctive dependency structures, intervention on D setting a better than b. But maybe not needed. Need include philosophical motivation: fixed mathematical function, "Which output of this very function would yield best outcome?" quote. Need maybe include direct quotes faithful: e.g., "Which output of this decision procedure causes the best outcome?" or "Which output of this very function would yield the best outcome?" Need ensure quotes exact? Source: normative principle ... "Which output of this very function would yield the best outcome?" Also CDT question "Which physical act of mine causes the best outcome?" EDT "Which physical act of mine would be the best news to hear I took?" Use faithful.

Need decide structure:
Title maybe "Action Functional Decision Theory: A Practical Exposition".
Sections:
1. What A-FDT is trying to decide
2. Formal framework and Equation (4)
3. Constructing hypotheticals: dependencies and counterfactuals
4. Examples (Newcomb, Smoking Lesion, Transparent Newcomb/Parfit's Hitchhiker)
5. Operational guidance for unfamiliar cases
6. Open questions and my assumptions
7. Conclusion
References brief.

Need word count ~2500-2900. We need ensure final around 2400-3000 words. Let's aim 2700. Need include equations. Need not too long? We can produce maybe 3000? Need be safe. Let's estimate: 10 sections with 250 words each =2500. Need references maybe 50. Need maybe 2600.

Need carefully formulate A-FDT equation:
Let \mathcal A finite actions, \mathcal O outcomes, \mathcal X observations. Let P be probability distribution over variables including V = U(Outcome). Let G be directed graph/structural model encoding causal and subjunctive dependencies. Let D_x = \mathrm{fdt}(\underline P,\underline G,\underline x) be a variable in P naming the output of the A-FDT procedure when run on inputs P,G,x. Then:
A-FDT(P,G,x) = argmax_{a∈A} E_P[ V | do(D_x = a) ].
Need mention if ties arbitrary.

Need explain do operator: Pearl intervention. In structural equation terms, variables Z_i = f_i(Pa_i, N_i). Intervention do(D_x=a) replaces equation D_x=... by constant a, leaves other equations unchanged, yields post-intervention distribution. Expected utility computed in that distribution. Need note for logical variables, G is not necessarily causal; it encodes subjunctive dependence. The source says can re-use Pearl's Do given G. Need emphasize source's open problem: no account of constructing G for subjunctive dependencies.

Need explain self-reference: D_x variable represents output of algorithm that is itself choosing; Kleene recursion theorem/quine. The agent need not know actual value to have variable.

Need explain observations: In Eq (4), x enters as subscript of D_x; unlike CDT, A-FDT does not evaluate E[V | do(Act=a), Obs=x]. It evaluates output of the computation that takes x as input. If a different output would imply different observations, the hypothetical should represent that. Need discuss operational ambiguity and propose: when observation is logically downstream of the same decision function (e.g., predictor chooses what to show based on predicted output), do not condition it fixed; when observation is exogenous evidence about background parameters, condition before constructing P. Source doesn't formalize distinction. Need label my assumption.

Need examples:
Newcomb:
Variables: D = A-FDT(P,G) maybe no observation. Predictor node Pred = D with 0.99 accuracy. BoxB full iff Pred=one-box. Action Act = D (if deterministic). Outcome utility: one-box & full $1M; two-box & full $1,001,000; one-box & empty $0; two-box & empty $1,000. Intervention do(D=one-box) sets Act=one-box and Pred likely one-box, Box full .99 -> EU .99*1,000,000 + .01*0 = $990,000. do(D=two-box) -> Pred likely two-box, Box empty .99 -> EU .01*1,001,000 + .99*1,000 = about $20,000? Wait source says $11,000? Let's compute if predictor 99% accurate: If two-box, full with 1% -> 0.01*1,001,000 + 0.99*1,000 = 10,010 + 990 = 11,000. Yes. Choose one-box. CDT do(Act) holds Box fixed; EDT conditions. Need concise.

Smoking lesion:
D_S or D_R? Simpler: lesion causes preference/utility function and action? Source's formalization: lesion determines which decision function controls action: if lesion, A-FDT(P_S,G) controls; if no lesion, A-FDT(P_R,G) controls. Cancer depends on lesion/luck, not D_S. Intervention on D_S=smoke changes action only if lesion? Wait source: Act(lesion,s,r)=s; Act(nolesion,s,r)=r. If evaluating A-FDT(P_S,G) (the case where preferences U_S, i.e. lesion?), do(D_S=smoke) affects action only in lesion state? Expected utility of smoke exceeds refrain by p*$1000, where p probability lesion (and thus D_S controls). Cancer probability unchanged. So smoke. We can present simpler: A-FDT graph has no arrow from D to Cancer/Lesion; only to Action (possibly via preference-state). Therefore intervention doesn't change cancer; smoking adds $1,000. Choose smoke. Need mention source's exact formalization with two possible decision functions if preferences depend on lesion; my simplified graph assumes action controlled by current D regardless; but source's nuance: if lesion changes preferences, the actual computation may be D_S or D_R. Need present enough.

Transparent Newcomb / Parfit:
Variables: D_full, D_empty. Predictor predicts what D_full outputs upon seeing full; fills box iff predicts one-box. If accurate and D_full=one-box, observation full and action one-box -> $1M. If D_full=two-box, accurate predictor predicts two-box, box empty; observation empty, action determined by D_empty (likely two-box? source q=1) -> $1k. EU one-box ~ $990k, two-box ~ $11k, choose one-box even when seeing full. Need tie to Parfit's hitchhiker: pay iff predicted pay in city; A-FDT chooses pay because outputting pay causes driver's prediction/ride. Need explain observation updateless: although seeing full, counterfactual two-boxing means probably seeing empty. This is source's striking claim.

Maybe include psychological twin PD: A-FDT cooperates because twin implements same D; do(D=cooperate) makes twin cooperate. Could use as introductory example. But word budget maybe. Could mention briefly.

Need discuss evaluating policies: The source footnote says preferred policies; Eq (4) action. For A-FDT name maybe action functional? Need maybe define policy extension: If a problem has several decision points or observations that are counterfactually affected by policy, represent a policy variable Π = A-FDT(P,G) mapping observations to actions. Then choose π by maximizing E[V | do(Π=π)], execute π(x). This resolves cases where action-level nodes D_x interact. But since assignment says Eq (4) primary, I can present this as an operational extension when needed, labeled my own. Need be careful: A-FDT might mean action-functional not policy? Hmm. User says "action functional decision theory (A-FDT)" and Eq (4) primary. Maybe they want action functional (not policy functional) as distinct from policy? In source Eq (4) intervenes on FDT(P,G,x) action output. The footnote says preferred policies but not used. They might want A-FDT as "action functional" meaning intervention on action output, not policy. Need avoid too much policy unless necessary. But they ask evaluates alternative actions or policies. So mention both: Eq (4) evaluates actions; in sequential/multi-agent settings source authors prefer policies. For unfamiliar cases, if multiple observations are possible, one can either model all relevant observation-indexed action nodes as Eq (4) does in transparent Newcomb, or adopt policy-variable extension. Label extension.

Need discuss relevant dependencies and counterfactuals:
- CDT preserves causal downstream correlations; breaks upstream/common cause correlations. EDT preserves all evidential correlations. A-FDT preserves subjunctive dependencies: correlations due to same computation/prediction; breaks merely statistical correlations (lesions) that don't depend on decision function.
- Counterfactuals: counterpossible because if deterministic function actually outputs a, "if it output b" is logically false. A-FDT requires reasoning under logical uncertainty. Source admits no full formal account; graph G supplies counterpossible dependence. Need mention.

Need "Where source leaves important question open": constructing G, determining subjunctive dependencies from observation; handling observations/conditioning; action vs policy; logical uncertainty; self-reference maybe. Need propose operational interpretations:
- G construction: Use structural equations with functional dependencies. Predictor nodes are functions of D_x plus noise if predictor models the agent's decision function. Lesion nodes have no D parent. Copies/twins share D variable or have separate nodes constrained to equal D (or high probability equality). Observations that are produced by predictor depend on predictor; exogenous observations not.
- If uncertain about subjunctive dependence, include a parameter S (accurate/inaccurate) or weight dependencies probabilistically. But the choice of which variables are downstream of D is normative/modeling judgment not derived by source.
- Conditioning: condition on observations only when they are exogenous relative to the decision function being evaluated. If observation is input but also downstream of predictor, treat as variable and don't hold fixed in counterfactual. In practice: ask "Would this observation have been different if my decision function had output differently?" If yes, it belongs downstream of D; if no, condition on it.
- Policies: choose policy variable when same decision procedure will be used across multiple possible inputs; else action-level Eq (4) may be unstable.

Need distinguish source claims vs my proposals. Use phrases: "The source claims...", "The paper leaves open...", "My suggested operational rule is...".

Need references: cite Yudkowsky and Soares 2017? The source is Functional Decision Theory: A New Theory of Instrumental Rationality. Maybe references minimal: Yudkowsky and Soares (2017), Pearl (2000), Joyce (1999), maybe Gibbard and Harper (1978). Need include brief references at end. Since target includes references. Avoid lengthy bibliography. Maybe 4-5.

Need ensure use A-FDT in headings and examples. Do not say FDT except perhaps "the source calls the theory functional decision theory; here I use A-FDT". Need maybe "Equation (4) of the source, relabeled for A-FDT". Use CDT, EDT distinct.

Need maybe mathematical notation. Need no LaTeX errors? Final can include LaTeX-like equations. Good.

Potential issue: The source's Eq (4) includes \FDT(P,G,obs) but uses x. We can rewrite:
\[
\mathrm{A\text{-}FDT}(P,G,x) = \arg\max_{a\in\mathcal A} \mathbb{E}_P[V \mid do(D_x=a)], \quad D_x := \mathrm{fdt}(\underline{P},\underline{G},\underline{x}).
\]
Need maybe underline dequoting. Explain: \underline{x} is a name/representation of x, so D_x is a variable naming the output of the very algorithm being run.

Need discuss expected utility finite, bounded utility. Maybe mention Eq (1) source: EU(a) = sum P(a hookrightarrow o_j; obs) U(o_j). A-FDT supplies interpretation of hookrightarrow as intervention on decision function. Good.

Need maybe use "subjunctive dependence" definition: When two physical systems compute same function, their behaviors subjunctively depend on that function. Quote? Source: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Faithful. Need maybe quote "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Could adapt: "A-FDT is to subjunctive dependence as CDT is to causal dependence." But source says FDT. Could say in source's terms. Need avoid calling A-FDT FDT? Could say "the source states: 'Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.' Under the assigned name, A-FDT occupies that role." Good.

Need maybe discuss fairness and utility? Could mention source claims A-FDT outperforms in fair dilemmas; not central. But philosophical motivation: chooses output of fixed function; no precommitment; value of information. Maybe include brief.

Need final word count. Let's draft in analysis then final. Need ensure around 2600 words. Let's outline with rough word counts:

Title + intro 250
1. Central idea 300
2. Formal statement Eq (4) 500
3. Dependencies/counterfactuals 400
4. Examples: Newcomb 350, Smoking lesion 300, Transparent/Parfit 350, maybe total 1000
5. Applying to unfamiliar cases operational 450
6. Open questions/assumptions 350
Conclusion + references 200
Total 2800. Good.

Need maybe combine. Let's write carefully.

Potential content details:

Intro:
"A-FDT asks: 'Which output of this very decision procedure would yield the best outcome?' It differs from EDT: conditionalization; CDT: intervention on physical action. A-FDT intervenes on logical variable representing output of decision function."

Formal:
Expected utility framework. Variables: Act, Obs, Outcome, V. P. G. do. D_x. Eq. Need mention argmax not unique.
"The crucial feature is that D_x is not Act. Act may be downstream of D_x, but so may predictors, predictions, observations, and other agents' actions if they compute or predict the same function."

Observations:
"CDT(P,G,x)=argmax E[V | do(Act=a), Obs=x]. A-FDT replaces do(Act=a), Obs=x with do(D_x=a). In Eq (4), x appears only in D_x. Thus A-FDT's response to observation is to change the intervention target, not to condition the hypothetical on the observation." Need note source examples sometimes condition? We can say "I take Equation (4) as controlling; where later examples include Obs in an expression, I read it as shorthand for the decision node with that input, or as a background condition not fixing endogenous observations." Need maybe too detailed. But user wants uncertainty. Include.

Dependencies:
Graph G: directed edges encode what changes when logical variable changes. Need maybe formal structural equations:
For variables Z_i, Z_i = f_i(PA_i, N_i). Intervention do(D_x=a) replaces D_x equation. Then expectation. For subjunctive edges, f_i may represent logical/constraint relation e.g., Predictor = D_x with prob .99. This isn't physical causation maybe time reversed but operational. Need mention not retrocausal; it's counterpossible dependency.

Examples:
Newcomb calculations. Use $ values. Need maybe say predictor accuracy 0.99. EU one = 990,000; EU two = 11,000; choose one. If CDT, do(Act) leaves Box B probability p; two always +1000; choose two. EDT conditions; one. A-FDT one because predictor downstream of D.

Smoking lesion:
Need source's exact nuance: lesion affects preferences and action. But simpler: graph: Lesion -> Action and Lesion -> Cancer; D -> Action only if D is the process controlling action; no D -> Cancer. If evaluating D_S: EU smoke - refrain = p*$1000, positive. Choose smoke. Need maybe mention if lesion makes smoking enjoyable, utility function differs. A-FDT smokes because intervention on D doesn't change lesion/cancer.

Transparent Newcomb:
Detailed enough. Let accuracy .99. Let q probability of two-boxing if empty. EU(D_full=one) = .99*1,000,000 + .01*q*1,000 ≈ 990,000. EU(D_full=two)= .01*1,001,000 + .99*q*1,000 ≈ 10,010+990q. For q≤1, one-box > two? If q=1, two EU=11,000; yes. Choose one. "Even after seeing full, A-FDT does not hold Obs=full fixed in the counterfactual; it treats seeing full as evidence that D_full is being run, but imagines that if D_full output two-box, predictor would likely have made box empty." Need tie Parfit: pay in city because driver's prediction depends on D_city.

Operational unfamiliar cases:
Step-by-step:
1. Identify decision function: actual reasoning process, input x.
2. Enumerate actions/outcomes and utility.
3. Identify variables correlated with action. For each, ask: is correlation due to (a) action causing it, (b) common cause, (c) predictor/copy computing same function? Only (a) and (c) should be downstream of D? Wait action causing is also D causing action causing outcome; so D -> Act -> outcomes. Common cause lesion not downstream unless it affects which D runs/preferences but not affected by D. Predictor/copy is downstream of D (subjunctive) even if temporally prior.
4. Encode structural equations. For predictors: Pred = noisy_copy(D_x). For twins: OtherAct = D_x or noisy. For blackmail: Letter depends on Predictor(D_x), etc.
5. Intervene and compute.

Need mention "If two agents use same A-FDT in symmetric game, represent both actions as downstream of a shared decision-type variable or two variables constrained equal; then cooperate in twin PD." Could be useful.

Open questions:
- Source admits no True operator; uses G. Constructing G from observation is largest open problem. My proposal uses modeling heuristics, not derived.
- Logical uncertainty/counterpossibles. Need probabilities over logical variables. Could use bounded approximations.
- Observation handling. Eq (4) says no conditioning, but real agents have evidence. My rule: condition on exogenous evidence; not on endogenous observations. This is not fully in source.
- Action vs policy. Source footnote says preferred policies. For A-FDT Eq (4), action-level; in dynamic problems use policy extension. Need justify: policy avoids inconsistencies when multiple possible inputs; but assignment uses Eq (4) so treat as extension.

Need conclusion: A-FDT is expected utility maximization under counterfactuals over decision-function outputs; powerful but requires subjunctive dependency model.

Need references:
Yudkowsky and Soares 2017, Functional Decision Theory. Pearl 2000/1996. Joyce 1999. Gibbard and Harper 1978 maybe. Maybe Lewis 1979. Keep brief.

Need ensure no unsupported claim as source. Use "source claims". Need maybe quote exact: "Which output of this very function would yield the best outcome?" Good.

Potential challenge: User requested "A-FDT (action functional decision theory)" maybe they expect name not source's FDT. We must not call it FDT except as source? Could say "The source calls the theory functional decision theory; I will use the assigned name A-FDT." Good.

Need maybe discuss "action functional" might mean evaluating actions not policies. Need include: "I use A-FDT for the action-level theory of Equation (4); when I discuss policy-level variant, I call it policy-level A-FDT extension." Good.

Let's think deeper about Eq (4) and observation conditioning to avoid inconsistency.

Source Eq (2) EDT(P,x) = argmax E(V | Obs=x, Act=a). Eq (3) CDT(P,G,x) = argmax E(V | Do(Act=a), Obs=x). Eq (4) FDT(P,G,x) = argmax E(V | Do(FDTvar(P,G,x)=a)). No Obs=x. Text: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." So indeed. But if P is prior before observation, then how does agent know x? The algorithm input x is observation; but the expectation doesn't condition on Obs=x. This is updateless: choose action based on prior expected utility of the computation output given that computation has input x. It may be weird: If you observe x, shouldn't P be conditional on x? In source's transparent Newcomb, they don't condition on full. But if there are exogenous observations (e.g., you see a coin landed heads unrelated to decision), should A-FDT condition? Probably yes, because P and G can be updated on observations not affected by decision? Source says FDT responds by changing node; maybe all observations become input, but P could also be updated? It says "FDT responds to observation by changing which node it intervenes upon" not "not by conditioning". Maybe it can also update P? Eq (4) lacks conditioning. Footnote about updateless: "This apparent 'lack of updating' is source of name Updateless Decision Theory". FDT does change behavior by intervention point. It may still update P on observations? In mechanical blackmail, Fiona "does change her behavior in response to evidence—by changing the place in her graph where she intervenes." It says "FDT says agents should entertain the hypothesis that, if their action were different, they might have made different observations." It suggests no conditioning on observed blackmail. But for ordinary evidence, maybe P and G are already conditioned? Hmm.

Need present operational: For any observation x, form P_x/G_x by ordinary Bayesian updating on facts treated as exogenous to the decision computation; then apply Eq (4) without additionally fixing x in the hypothetical if x is endogenous. This is reasonable. Need label as my assumption because source not precise.

Need maybe formalize intervention with observation nodes. Suppose Obs variable. Let x be actual observation. A-FDT uses D_x. The post-intervention distribution may assign probability to Obs≠x. That's intended. If Obs is exogenous, D_x is simply D conditioned on x? Could model Obs as parent of D_x (input), but intervention on D_x doesn't change Obs. If Obs is downstream of predictor, it can change. Need distinguish: D_x is defined for input x; if counterfactual world has Obs=y, the action is controlled by D_y, not D_x. Thus D_x intervention only affects outcomes in worlds where Obs=x (or where predictor predicted x?) In transparent Newcomb, D_full controls Act only when prediction/observation full. So do(D_full=two) can lead to Obs=empty and action controlled by D_empty. Good. Need explain this is how A-FDT evaluates "what if this computation output differently" even though if it did, the agent might not be in the same observation branch.

Need maybe write a small general definition:
Let \mathcal{X} be possible observations. For each x, include node D_x. Let Act = Select(\{D_y\}, Obs, other variables), where Select outputs D_{Obs} if observation determines the decision point. In deterministic settings, Act = D_{Obs}. For predictors, Prediction may be a noisy copy of D_x for the x they predict. Then intervention do(D_x=a) may alter Obs via predictor. Expected utility integrates over all branches. This is my operational graph pattern.

Need maybe mention source's graph in transparent: Act depends on D_full, D_empty, and Prediction, with Prediction determining which D controls Act. This matches.

Need maybe mention "A-FDT does not choose what it believes will happen; it chooses the output that makes the best hypothetical." In deterministic case, D_x actual output is one action; counterfactuals are impossible but useful.

Potential issue with self-reference and fixed point: A-FDT equation defines action as argmax of expectation involving D_x which is the output of A-FDT. This is recursive. Source says self-reference harmless via Kleene. But for application, one often solves by reasoning: if output one-box leads to better EU, then output one-box. Need mention fixed point: A-FDT's actual output must be consistent with the argmax; if the model predicts that A-FDT outputs a*, then the chosen a* is the one whose intervention has max expected utility. In cases of uncertainty about own output, still choose max. Need maybe mention no ratification needed per source. But if model includes D_x prior, intervention ignores prior? In Pearl do, prior of D is overridden. So A-FDT not at mercy of priors unlike EDT. Good.

Need maybe discuss "dominance" if word budget. Could include a paragraph under counterfactuals: A-FDT has its own dominance notion; two-boxing doesn't dominate because holding predictor fixed while changing action is not an A-FDT counterfactual. Source claims. Could be useful to explain dependencies. But maybe not essential. Include one sentence.

Need maybe mention "fair problems" source claims. Not necessary but philosophical motivation. Maybe conclusion.

Need check word count as we draft. Let's start drafting final in mind.

Title: "Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function"

Paragraph 1: define.

Need ensure A-FDT with hyphen? Use A-FDT consistently. Headings include A-FDT. Examples headings maybe "A-FDT in Newcomb's Problem".

Let's draft.

Potential final text:

# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

## 1. The central idea
...

Need maybe quotes. Use exact: "Which output of this very function would yield the best outcome?" Source's abstract: "Which output of this very function would yield the best outcome?" Good.

Need mention source's name: "The reference article calls the theory functional decision theory; this essay uses the assigned name A-FDT for the action-level version formalized by Equation (4), Section 5." Good.

Formal section:
"Let \mathcal A be finite action set, \mathcal O countable outcomes, \mathcal X observations. P is agent's world model, a probability distribution over variables including Outcome and V=U(Outcome). G is dependency graph. For any observation x, let D_x = fdt(\underline P, \underline G, \underline x) be a variable in P that represents the output of the A-FDT algorithm itself when given P,G,x. Equation (4) says: ..."

Need maybe use \operatorname{A\text{-}FDT}. Fine.

"The underline notation is dequoting: it turns the observed value x into a syntactic input to the decision procedure." Maybe.

"Interpreting do: If G is a structural model with equations Z_i = f_i(Pa_i,N_i), do(D_x=a) replaces equation for D_x by constant a and computes induced distribution. The expectation is over exogenous noise." Good.

"Equation (4) is an expected utility rule; it inherits Joyce representation theorem constraints. The difference is the counterfactual connective." Good.

Observation paragraph:
"Compare CDT: CDT(P,G,x)=argmax E[V | do(Act=a), Obs=x]. A-FDT does not put Obs=x inside the hypothetical. Instead, x selects which decision-function node is intervened upon. The source summarizes: when CDT changes from x to y it changes conditioning; A-FDT changes intervention node. This is why A-FDT can say that, in transparent Newcomb, if the computation that runs upon seeing a full box output two-boxed, the agent would probably have seen an empty box." Good.

Need mention uncertainty: "I read Equation (4) as primary; some later source examples write Obs in the expression, but the calculations treat observation as endogenous. If one conditions on Obs=x in transparent Newcomb, A-FDT collapses to two-boxing; thus Eq (4) cannot require such conditioning." Good. This is important. Distinguish my reading.

Dependencies section:
"Subjunctive dependence" quote. "A-FDT hypotheticals preserve all decision-relevant subjunctive dependencies and break merely statistical ones. CDT preserves causal downstream; EDT all evidential." Good.

Examples. Need include calculations with values.

Let's write Newcomb:
"Let D be node A-FDT(P,G). Predictor Pred equals D with prob .99. BoxB full iff Pred=one. Act = D. EU..." Use equations.

Smoking lesion:
Need not overcomplicate but include source nuance. Maybe:
"The lesion problem requires a slightly more careful graph because the lesion changes preferences. Source distinguishes P_S and P_R, with D_S=A-FDT(P_S,G), D_R=A-FDT(P_R,G), and Act(lesion,s,r)=s, Act(nolesion,s,r)=r. The lesion has arrows to Cancer and to which D controls Act, but D_S has no arrow to Lesion or Cancer. Therefore do(D_S=smoke) leaves P(lesion)=p unchanged; smoke EU exceeds refrain by p*$1000. A-FDT smokes." Good. This is precise.

Transparent/Parfit:
Include equations. Need be clear q. Let q be prior probability D_empty outputs two-box (source says correct q=1). For D_full=one: EU = .99*1,000,000 + .01*q*1,000. For D_full=two: EU = .01*1,001,000 + .99*q*1,000. For q≤1, first > second. If q=1: 990,010 vs 11,000? Actually first .99*1,000,000=990,000 plus .01*1*1000=10, total 990,010. Source wrote 990,000 + 0.01q*1000 = 990,010. second 10,010 + 990 = 11,000. Good. Choose one. "Thus A-FDT one-boxes even when seeing full; equivalently pays hitchhiker." Need maybe if q=0? second 10,010, still less. Good.

Need maybe mention Parfit: "driver predicts D_city; paying is selected because do(D_city=pay) makes ride likely." Good.

Operational section:
"A recipe for unfamiliar cases". Use bullet list maybe. Essays can have numbered list. Need include assumptions.

1. Identify decision node(s): D_x for actual input; for multiple agents with same reasoning, either shared D or equality constraints.
2. Build P/G: variables, utilities.
3. Classify correlations: causal downstream of action (D->Act->...), subjunctive (predictors/copies of D), mere common causes. Draw arrows from D to variables that would change if D's output changed, even if temporally earlier. Do not draw arrows from D to variables that only statistically correlate (lesions) unless they compute/predict D.
4. Intervention and compare.
5. Policy extension if multiple inputs. "Although Equation (4) is action-level, the source notes preferred policy formulation. My recommended operational extension: choose π by intervening on Π=A-FDT(P,G) mapping observations to actions; then execute π(x). This is equivalent to having all D_x nodes determined by a single Π and avoids treating branches independently." Need label as my proposal. Good.

Need discuss "what follows from source" vs "additional assumptions". In operational section, say "Steps 1-4 are direct applications of Equation (4) once G is given. The classification heuristics and policy extension are my operational proposals; source only says G must encode subjunctive dependencies." Good.

Open questions:
- G acquisition. Source: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem". Quote maybe not exact? Source says exactly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Could quote. Need maybe too long. Use.
- Counterpossibles/logical uncertainty. Need approximate.
- Observation update. Need my rule.
- Fairness/optimality not formal.

Conclusion.

References: minimal.

Need check word count. Let's approximate final draft length. We can produce about 2700 words. Need maybe count rough. We'll write final with paragraphs. Need not too verbose but substantive.

Let's draft actual text now in final? Before final, let's compose full text in analysis and maybe count. We'll write with headings.

Draft:

Title + intro (approx 200)

"The reference article calls the theory functional decision theory. I use A-FDT..." 70.

Section 1 central idea 300.

Section 2 formal 650.

Section 3 examples 900.

Section 4 application 500.

Section 5 open 400.

Conclusion/references 250. Total 3000 maybe. Need maybe reduce.

Let's write carefully and estimate.

---

# Action Functional Decision Theory: Choosing the Best Output of a Fixed Decision Function

The supplied article introduces a decision theory that it calls functional decision theory. In this essay I use the assigned name **A-FDT** (action functional decision theory) for the action-level theory whose primary formal statement is Equation (4) of Section 5. A-FDT's normative principle is that an agent should treat her decision as the output of a fixed mathematical function and ask: “Which output of this very function would yield the best outcome?” This contrasts with evidential decision theory (EDT), which asks which action would be best news, and causal decision theory (CDT), which asks which physical intervention causes the best outcome. A-FDT resembles CDT in using interventions, but it intervenes on a logical variable—the output of the agent’s decision procedure—rather than on the physical action token.

That seems 150 words.

## 1. The formal core of A-FDT

Let \(\mathcal A\) be finite actions, \(\mathcal O\) countable outcomes, and \(\mathcal X\) possible observations. The agent has a world-model \(P\), a probability distribution over variables including \(\Outcome\), \(\Obs\), \(\Act\), and utility variable \(V=\Util(\Outcome)\). She also has a dependency structure \(G\). In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode not only causal structure but also the “subjunctive” dependencies that obtain when other events depend on the output of the relevant decision function.

For an observation \(x\), write
\[
D_x \coloneqq \mathrm{fdt}(\underline P,\underline G,\underline x)
\]
for a variable in \(P\) representing the output of the A-FDT algorithm itself when run on inputs \(P\), \(G\), and \(x\). Underlines denote dequoting: the model contains a name for the actual inputs, so the variable refers to this very computation. Equation (4), relabeled for A-FDT, is
\[
\mathrm{A\text{-}FDT}(P,G,x)
  = \argmax_{a\in\mathcal A}
    \mathbb{E}_P\!\left[V \mid do(D_x=a)\right].
\]
The \(do(\cdot)\) operator is Pearl-style intervention. If \(G\) is represented by structural equations, \(do(D_x=a)\) replaces the equation for \(D_x\) with the constant \(a\), leaves other equations unchanged, and propagates consequences through \(G\). The agent chooses the action whose counterfactual world has highest expected utility.

The comparison with CDT is illuminating. CDT is
\[
\mathrm{CDT}(P,G,x)=\argmax_{a\in\mathcal A}
 \mathbb{E}_P[V\mid do(\Act=a),\Obs=x].
\]
CDT conditions on the observation and intervenes on the physical act. A-FDT, in Equation (4), does not place \(\Obs=x\) inside the hypothetical. Instead, the observation \(x\) selects which decision-function node \(D_x\) is intervened upon. The source states this as a key difference: CDT responds to a changed observation by changing what it conditions on; A-FDT responds by changing the node on which it intervenes.

This is subtle. I take Equation (4) as controlling. If one additionally conditioned on \(\Obs=x\) in predictor problems where the observation itself depends on the predicted decision, A-FDT would give the source’s undesired answers—for example, two-boxing in transparent Newcomb. Some later source examples write observation variables in expressions, but their calculations do not hold the observation fixed. Where the source is ambiguous, my reading is: condition on exogenous background evidence when forming \(P\) and \(G\), but do not treat decision-relevant observations as fixed consequences of the physical act in the A-FDT counterfactual. This interpretive rule is not fully formalized in the source; I return to it below.

This formal section ~650? Let's count: maybe 550. Good.

## 2. Dependencies and counterfactuals

A-FDT’s hypotheticals are counterfactuals about the output of a computation. The source calls the relevant relation “subjunctive dependence”: “When two physical systems are computing the same function, we will say that their behaviors ‘subjunctively depend’ upon that function.” In a twin prisoner’s dilemma, the twin’s action subjunctively depends on the same decision function. In Newcomb’s problem, the predictor’s prediction subjunctively depends on a sufficiently accurate representation of the agent’s decision function. In the smoking lesion problem, the lesion does not subjunctively depend on the agent’s decision function; it merely causes both a preference and a disease.

Thus A-FDT preserves correlations that exist because some variable is a computation, prediction, or copy of the decision function, and it breaks correlations that are merely statistical common-cause correlations. EDT preserves too many correlations: conditioning on an action preserves all evidential ties, so EDT refrains from smoking to avoid bad news. CDT preserves too few: intervening on the physical action severs the predictor’s prediction from the action, so CDT two-boxes. A-FDT tries to preserve exactly the decision-relevant subjunctive dependencies.

These counterfactuals are often counterpossibles. If the actual A-FDT computation outputs one-box, then “if this very computation output two-box” is, in a strict logical sense, impossible. The source acknowledges that A-FDT therefore needs a way to reason under uncertainty about logical facts. Equation (4) avoids supplying a full counterpossible semantics by assuming that \(G\) already tells us how changing the logical variable changes other variables. This is both the elegance and the main open problem of the theory.

~280. Good.

## 3. A-FDT in Newcomb’s problem

Use simple model. Let \(D\) be \(D_x\) (no relevant observation). Let \(Pred\) be predictor’s prediction. Suppose predictor is 99% accurate:
\[
P(Pred=D)=0.99.
\]
Let \(BoxB=full\) iff \(Pred=onebox\), and let \(\Act=D\). Utilities: \(V(onebox,full)=\$1{,}000{,}000\), \(V(twobox,full)=\$1{,}001{,}000\), \(V(onebox,empty)=\$0\), \(V(twobox,empty)=\$1{,}000\).

A-FDT compares:
\[
\mathbb{E}[V\mid do(D=onebox)]
 =0.99(1{,}000{,}000)+0.01(0)=\$990{,}000,
\]
\[
\mathbb{E}[V\mid do(D=twobox)]
 =0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.
\]
So A-FDT one-boxes. CDT, by contrast, intervenes on \(\Act\) and holds \(BoxB\) fixed; two-boxing then yields \$1,000 more in every state. EDT conditions on action and also one-boxes, but because one-boxing is evidence of a one-boxing predisposition. A-FDT one-boxes because the predictor’s prediction is downstream of the same decision function in \(G\).

~220.

## 4. A-FDT in the smoking lesion problem

In the smoking lesion problem, smoking is correlated with cancer only because a lesion causes both a liking for smoking and cancer. The source formalizes the preference change by allowing two possible utility models, \(P_S\) and \(P_R\), where \(U_S\) values smoking and \(U_R\) values refraining differently. There are two possible decision nodes:
\[
D_S=\mathrm{fdt}(\underline{P_S},\underline G),\qquad
D_R=\mathrm{fdt}(\underline{P_R},\underline G).
\]
The lesion variable \(L\) affects both cancer and which decision node controls the action:
\[
\Act(L,s,r)=s\text{ if }L=lesion,\quad
\Act(L,s,r)=r\text{ if }L=nolesion.
\]
Crucially, \(G\) contains no arrow from \(D_S\) to \(L\) or to \(Cancer\). If the agent is in fact running \(D_S\), A-FDT evaluates \(do(D_S=smoke)\) and \(do(D_S=refrain)\). Let \(p=P(L=lesion)\). The intervention changes the action only in lesion cases, but it does not change the probability of cancer. The expected utility of smoking exceeds refraining by \(p\cdot \$1{,}000\). Therefore A-FDT smokes.

The important point is graph-theoretic: the lesion is a common cause, not a predictor or copy of the decision function. Intervening on the decision function does not change it. Hence A-FDT avoids EDT’s failure while retaining CDT’s correct answer here.

~260.

## 5. Transparent Newcomb and Parfit’s hitchhiker

The most distinctive A-FDT cases are those where EDT and CDT both fail. In transparent Newcomb, the agent sees both boxes. The predictor filled box B iff she predicted that the agent would one-box upon seeing both boxes full. Let \(D_{full}\) be the A-FDT node with input “see full box,” and \(D_{empty}\) the node with input “see empty box.” The predictor predicts \(D_{full}\). If the predictor is accurate, then \(D_{full}=onebox\) makes it highly likely that box B is full; \(D_{full}=twobox\) makes it highly likely that box B is empty, in which case the action is controlled by \(D_{empty}\), not \(D_{full}\).

Let \(q\) be the probability that \(D_{empty}\) two-boxes. Then:
\[
\mathbb{E}[V\mid do(D_{full}=onebox)]
 =0.99(1{,}000{,}000)+0.01q(1{,}000),
\]
\[
\mathbb{E}[V\mid do(D_{full}=twobox)]
 =0.01(1{,}001{,}000)+0.99q(1{,}000).
\]
For \(0\le q\le1\), the first expression is larger. A-FDT one-boxes even when the agent sees that box B is full. If she instead imagined two-boxing while holding the observation “full” fixed, she would two-box; Equation (4) says that this is not the correct A-FDT hypothetical. The correct hypothetical allows the observation to vary because the observation is itself tied to the predictor’s response to the decision function.

Parfit’s hitchhiker is decision-theoretically analogous. The driver saves the agent iff she predicts that the agent will pay \$1,000 after reaching the city. Let \(D_{city}\) be the A-FDT computation run in the city. Intervening on \(D_{city}=pay\) makes the driver’s prediction and the rescue likely; intervening on \(D_{city}=refuse\) makes death likely. A-FDT pays. The source uses this equivalence to argue that one-boxing in transparent Newcomb and paying the hitchhiker are the same disposition.

~360.

## 6. Using A-FDT on unfamiliar problems

Equation (4) gives a clear rule once \(P\) and \(G\) are supplied. A practical recipe is:

1. Identify the actual decision computation. Determine the input \(x\) and define the node \(D_x\) representing the output of A-FDT on that input.
2. List the actions, outcomes, and utilities.
3. Build a structural model \(G\). For every variable correlated with the action, ask whether it would change if the decision function’s output changed. If the variable is a predictor, simulation, copy, or symmetric agent using the same reasoning, make it downstream of \(D_x\) (possibly with noise). If it is a mere common cause, such as a lesion or random background fact, do not make it downstream of \(D_x\). If it is causally downstream of the action, connect it through \(\Act\).
4. For each candidate action \(a\), perform \(do(D_x=a)\), propagate through \(G\), compute expected utility, and choose the maximum.

This recipe is faithful to the source in steps 1, 2, and 4. Step 3 is where the source leaves the most work. The article says that \(G\) must tell us “how changing a logical variable affects all other variables,” but it does not give a general method for constructing \(G\). My suggested heuristic is to represent predictor-like dependencies as functional equations. For example, if a predictor is 90% accurate about \(D_x\), write \(Pred=D_x\) with probability 0.9 and an independent error otherwise. If two agents are psychological twins, either use one shared decision-type variable for both actions or use two variables constrained to be equal with high probability. These are modeling assumptions, not consequences of Equation (4) alone.

A second operational issue is policy versus action. Equation (4) chooses an action for a given input. The source notes that the authors’ preferred formulation iterates over policies, mappings from observations to actions, and that this can matter in multi-agent dilemmas. For sequential or observation-dependent problems, I recommend a policy-level extension: introduce a variable \(\Pi\) representing the policy output by A-FDT, intervene on \(\Pi=\pi\), compute expected utility over the whole situation, and choose the best \(\pi\). The action-level equation can then be recovered by executing \(\pi(x)\). This extension is not required for the simple examples, but it makes A-FDT easier to apply when the same decision procedure faces many possible inputs. It is my own operational proposal, motivated by the source’s footnote and by the transparent Newcomb graph, which effectively contains multiple observation-indexed decision nodes.

~570. Good.

## 7. Open questions and limits

The largest open question, acknowledged by the source, is how to learn or justify \(G\). Pearl’s do-calculus has a fairly developed account of causal discovery, but A-FDT needs a broader structure including logical, computational, and subjunctive dependencies. The source says: “Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory.” Until that is solved, A-FDT is best understood as a decision rule relative to a model of subjunctive dependence, not as a complete empirical method.

Counterpossible reasoning is also unresolved. A-FDT must compare worlds where a deterministic computation has a different output. Human mathematicians can reason about false or uncertain mathematical claims, and bounded agents can use probabilistic approximations over logical statements, but no fully satisfactory formal semantics is given. In practice, an A-FDT model can treat logical variables as stochastic nodes with uncertainty reflecting bounded reasoning, then use interventions on those nodes. This is an additional operational assumption.

Observation handling also needs care. Equation (4) says observations enter by selecting the intervention node, not by conditioning the hypothetical. This gives attractive updateless behavior in blackmail and transparent Newcomb cases. But real agents also receive exogenous evidence. My proposed rule is: update \(P\) and \(G\) on observations that are not counterfactually dependent on the decision function; do not hold fixed observations that would have changed if the decision function had output differently. The source’s examples support this rule, but it is not given as a formal criterion.

~330.

## Conclusion

A-FDT is an expected-utility theory with a distinctive counterfactual perspective. Its central equation instructs the agent to maximize expected utility after intervening on the output of her own decision function, not merely on her physical action. By doing so, it one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and one-boxes in transparent Newcomb. Its appeal is that it treats predictors, copies, and symmetric reasoners as decision-relevant dependencies rather than as irrelevant correlations or as impossible violations of causal order. Its main weakness is that the formal rule depends on a graph of subjunctive dependencies that the source does not tell us how to construct. A-FDT is therefore both a powerful normative ideal and an incomplete practical algorithm: precise once the dependency structure is given, but demanding further work to become a fully general account of instrumental rationality.

References
Yudkowsky, E., and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
Pearl, J. (2000). Causality. Cambridge University Press.
Joyce, J. (1999). The Foundations of Causal Decision Theory. Cambridge University Press.
Gibbard, A., and Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility. In Foundations and Applications of Decision Theory.

Need word count. Let's approximate: Title 10, intro 150, formal 650, dependencies 280, Newcomb 220, lesion 260, transparent 360, using 570, open 330, conclusion/references 230. Total ~3060. Need target 2400-3000. 3060 maybe slightly above. Need reduce ~100-200 words. Could trim formal, using, open. Need final under 3000. Let's count more accurately? The draft words: Intro 132? Formal maybe 594. Dependencies 260. Newcomb 215. Lesion 235. Transparent 333. Using 515. Open 292. Conclusion+refs 205. Total ~2881? Maybe okay. Let's rough count by lines? Hmm.

Let's count with approximate tokens: 
Intro paragraph: "The supplied article..." 119 words.
Formal section: paragraph1 83, equation paragraph 91, do paragraph 57, compare paragraph 76, subtle paragraph 95 =402? Wait need recalc. Actually formal section has 5 paragraphs: 1 Let... (86), 2 For observation... equation (93), 3 do operator (49), 4 comparison CDT (64), 5 subtle (99) =391. Not 650. Good.
Dependencies: 3 paragraphs maybe 270.
Newcomb: 180.
Lesion: 230.
Transparent: 310.
Using: list plus paragraphs maybe 460.
Open: 260.
Conclusion+refs: 200. Total ~2400? Let's estimate: 119+391=510, +270=780, +180=960, +230=1190, +310=1500, +460=1960, +260=2220, +200=2420. Good near lower bound. Maybe need add a bit to ensure 2400-3000. It is around 2400. Could add 200-300 words for depth. Need target approximately 2400-3000; 2420 okay but maybe risky. Add some paragraphs: more on dominance, precommitment, value of information, or policy. Need maybe 2600. Add a section "Why A-FDT’s answers are stable" or expand philosophical motivation. Need maintain coherence.

Add after dependencies or before conclusion: "A-FDT dominance and precommitment" ~200 words. Or expand operational with example of twin PD/blackmail. User wants use examples whenever help. Could add psychological twin PD and/or XOR blackmail briefly. That also shows application. Need not too long. Add section "Two further illustrations" maybe 250 words. That brings to 2700. Need ensure not repetitive.

Add after Transparent section:
## 6. Two further illustrations: twins and blackmail
Psychological twin PD: A-FDT cooperates. Model D shared; payoffs. EU cooperate $1M, defect $1k? Actually if both cooperate 1M, both defect 1k, unilateral defector 1,001,000 cooperator 0. Since twin uses same D, do(D=cooperate) twin cooperate -> 1M; do(D=defect) -> 1k. Choose cooperate. CDT defects because causal independence; EDT cooperates but for news.
XOR blackmail: Blackmailer sends letter iff exactly one of (rumor false & pay) or (rumor true & not pay). If agent pays upon letter, letter only when no termites; if refuses, letter only when termites. EDT pays because paying is good news; CDT refuses because infestation upstream; A-FDT refuses because D_letter=refuse makes letter unlikely (if predictor accurate) and doesn't change infestation. Source claims. Could illustrate counterfactual observation: if A-FDT paid, predictor wouldn't have sent letter. But maybe word budget. Add ~250.

Then renumber sections? We have current using section 6, open 7. If add section 6, need renumber. Could integrate in examples? Maybe add subsection after transparent: "Twins and blackmail". Good.

Need maybe mention "dominance" in philosophical motivation. Could add in dependencies: "A-FDT also yields its own dominance notion..." ~80. Fine.

Let's revise final to include these additions. Need maintain headings. Maybe structure:
1. Formal core
2. Dependencies and counterfactuals
3. Newcomb
4. Smoking lesion
5. Transparent Newcomb and Parfit
6. Twins, blackmail, and dominance (or further illustrations)
7. Using A-FDT on unfamiliar problems
8. Open questions
Conclusion.

Need keep word count around 2700. Let's write final polished.

Need ensure quotes faithful. We use quote: “Which output of this very function would yield the best outcome?” exact. Quote subjunctive dependence exact? Source: "When two physical systems are computing the same function, we will say that their behaviors ``subjunctively depend'' upon that function." We quote with single quotes maybe. Good. Quote open problem exact? Source: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Good.

Need maybe quote source's CDT/EDT questions? Could include in intro: "Which physical act of mine causes the best outcome?" and "Which physical act of mine would be the best news to hear I took?" These are exact? Source: CDT question “Which physical act of mine causes the best outcome?” EDT “Which physical act of mine would be the best news to hear I took?” Yes. Add.

Need be careful with "A-FDT" in equation variable: maybe use \mathrm{A\text{-}FDT} inside math; okay.

Need mention "source claims vs own assumptions" explicitly. We have "I take Equation (4) as controlling", "my reading", "my suggested heuristic", "my own operational proposal". Good.

Need maybe mention "where source leaves important question open" and develop operational interpretation. Done.

Need check mathematical correctness of blackmail example if included. Let's formulate succinctly:
XOR blackmail: predictor sends letter iff (no termites and agent pays upon letter) XOR (termites and agent refuses). If D_letter=pay, accurate predictor sends letter only in no-termite branch; conditional on letter, termites prob 0; EDT pays. A-FDT: do(D_letter=pay) changes probability of receiving letter but not infestation; given letter, if pay you lose $1000; if refuse you likely wouldn't have received letter and avoid payment. Expected utility refuse higher. Source says Carl and Fiona refuse, but Fiona's hypothetical says if she paid, predictor would not have sent letter. Need phrase.

Need maybe add dominance paragraph:
"The source also argues that A-FDT has its own dominance principle. Two-boxing does not dominate one-boxing in A-FDT terms, because holding the predictor fixed while changing the physical act is a CDT-style counterfactual, not an A-FDT counterfactual. Every way of constructing hypotheticals defines its own dominance notion; the source therefore evaluates theories by utility achieved." Good.

Need ensure no unsupported "A-FDT smokes" if preferences? Good.

Potential issue: In smoking lesion source says if lesion, agent loves smoking; if no lesion, doesn't? They define U_R differs values smoking at -$1. It says two utility functions U_S and U_R, where U_R differs from U_S in that it values smoking at -$1. There are two distributions P_S, P_R. Fiona can't tell which. In case preferences U_S, evaluate FDT(P_S,G); smoking better by p*$1000. If preferences U_R, maybe also smoke? Source says correct q=0 for D_R? Hmm. But final says A-FDT smokes. Good enough. Need maybe avoid stating action only in lesion cases? Wait Act(L,s,r)=s if lesion, r if no lesion. If evaluating D_S, intervention changes action only when lesion. If p=prob lesion, smoking vs refrain difference p*$1000. If no lesion, D_S not controlling? Then why evaluate D_S? Because if she has lesion, her preferences U_S and D_S controls; if no lesion, U_R and D_R controls. She doesn't know which, but actual A-FDT output is whichever. Source's calculation says "in the case where her preferences are U_S" she smokes. Similarly if U_R? It might also smoke? They say correct q=0 (D_R=refrain?) Actually q is prior probability D_R=smoke? They say correct q is 0, as you may verify. If D_R refrains, no lesion agent refrains? But overall A-FDT? Wait smoking lesion problem: Agent gains utility $1000 by smoking regardless of death, and $1M if doesn't die. Lesion causes love smoking and cancer. Agents without lesion don't love smoking? If no lesion, smoking gives no utility? They formalize U_R values smoking at -$1? Maybe no lesion agent would refrain? But standard problem asks should she smoke? CDT smokes because $1000 utility if smoking? Wait if without lesion doesn't like smoking, maybe smoking has negative utility? The source variant: two utility functions U_S and U_R where U_R differs in that it values smoking at -$1. It seems lesion makes smoking +$1000? The expected utility difference for D_S smoking vs refrain p*$1000, so if lesion she smokes; if no lesion maybe D_R refrains. But the agent doesn't know if she has lesion, and actual behavior depends on lesion? That seems weird: A-FDT may smoke only if lesion? But standard says CDT smokes regardless. Let's re-read source snippet: "According to the problem description, the lesion determines whether or not the agent likes smoking. We can formalize this by saying that there are two utility functions, U_S and U_R, where U_R differs from U_S in that it values smoking at -\$1. Thus, there are two different distributions Fiona could have: P_S, in which V is calculated using U_S; and P_R, in which V is calculated using U_R. Fiona can't tell which distribution she actually uses; it's a black box to her."
Then Act(lesion,s,r)=s; Act(nolesion,s,r)=r. They evaluate FDT(P_S,G) case where preferences U_S. Expected utility smoke:
p($10,000 + $1,000) + (1-p)($990,000 + q$1,000)
refrain:
p($10,000) + (1-p)($990,000 + q$1,000)
Difference p*$1,000. Why $10,000? If lesion cancer? Values maybe not important. They conclude she smokes. "Thus we see that a single compact decision criterion ... prescribes both one-boxing and smoking." But if actual no lesion, maybe D_R? They likely assume actual preferences are U_S? The problem says agent gains utility $1000 by smoking regardless; maybe lesion only causes cancer not preference? Wait original smoking lesion: lesion causes smoking and cancer? It says lesion causes those afflicted to love smoking and causes cancer. Agent gains utility by smoking. If no lesion, maybe doesn't love smoking but still can gain? The source formalization is contrived. For essay, we can present simplified smoking lesion: lesion common cause of desire and cancer; A-FDT's graph no D->lesion; smoking chosen because utility of smoking unaffected by cancer. Need avoid getting bogged. But user wants mathematical understanding; perhaps use source's exact formalization? Need be accurate. The source says A-FDT smokes. We can present simplified but mention source nuance.

Need perhaps revise smoking lesion section to not overstate "if no lesion D_R refrains". Better: "In the source’s detailed model, lesion determines which utility function the agent has, so there are two possible decision nodes. The crucial structural fact remains: neither decision node has an arrow to lesion or cancer. Evaluating the node that actually controls the action, smoking has higher expected utility by the probability that this node controls action times the direct utility of smoking. Hence A-FDT smokes." This avoids specifics. But maybe less precise. Let's refine.

Maybe use standard smoking lesion with utility smoking +$1000 independent of lesion. Graph: Lesion -> Smoking? Actually if lesion causes desire, but A-FDT action is output of decision function; lesion may influence preferences/input but not D's output? Hmm. In source, lesion determines which utility function, thus which D controls action. But no D->lesion. Good.

Need maybe not include exact Act equation if it confuses. But mathematical precision useful. Keep but explain.

Let's think about policy extension: The user says "Explain how the theory evaluates alternative actions or policies". Good to include policy extension. Need make clear source Eq (4) action; source footnote policy. We can say "For policies, the natural A-FDT policy version is ...". Good.

Need maybe discuss "counterfactuals with observations" more deeply. In transparent Newcomb, A-FDT seems to ignore actual observation. Is that rational? Source arguments: value of information, precommitment. Could mention: "This updateless feature is why FDT is related to Updateless Decision Theory." Maybe add. But not necessary.

Need maybe mention "A-FDT does not require binding precommitment; it acts as it would precommit to act" in conclusion or motivation. Add one sentence.

Need ensure references not lengthy. Good.

Potential issue with notation \mathrm{fdt} vs A-FDT. Source variable \FDTvar(\underline P,\underline G,\underline x) maybe lower-case fdt. Use D_x. Good.

Need maybe include "if an action has probability 0"? EDT issue not needed. A-FDT interventions can evaluate zero-prob actions. Good point: A-FDT not at mercy of priors. Could add in formal: "Because do overrides prior probability of D_x, A-FDT can compare actions the agent strongly expects not to take." Nice. Add ~30.

Need maybe mention "bounded utility finite expectation" from source Eq (1). Not necessary but maybe.

Need check final for repeated words. Need ensure A-FDT consistently. Do not use "FDT" except maybe quote? The source quote open problem uses "functional decision theory" not FDT. We can avoid "FDT". In references source title uses Functional Decision Theory; okay. In text "source calls the theory functional decision theory" okay. But user says use A-FDT consistently as assigned decision theory's name. It might be okay to mention source's name once. Avoid using FDT acronym. The variable D_x = fdt perhaps lower-case; maybe use afdt? To be consistent, define D_x = \mathrm{afdt}(...). Source Eq uses FDTvar, but we can rename. Better: use \(D_x\) and say it is the variable representing A-FDT's output. In equations: \(D_x := \mathrm{A\text{-}FDT}(\underline P,\underline G,\underline x)\)? But that conflates action output variable and function. Source uses fdt variable. We can use \(\mathrm{afd t}\) not important. To avoid FDT, write:
\[
D_x := \text{the output variable of the A-FDT procedure on inputs }(P,G,x).
\]
Equation: A-FDT(P,G,x)=argmax E[V | do(D_x=a)]. Good. No FDT.

Need maybe quote "functional decision theory" in reference title; okay.

Need maybe in open quote "functional decision theory" uses source name. Could paraphrase to avoid FDT? But quote faithful? User says keep quotations faithful. If quote source, it says functional decision theory. That's okay not using A-FDT? Maybe acceptable because quotation. Could instead not quote that exact open problem sentence, paraphrase. But quotes useful. We can quote and then say "in the assigned terminology, A-FDT". Fine.

Let's craft final with additions.

Full final draft:

Title...

Intro ~170.

### 1. The formal core of A-FDT
...
Add "Because intervention replaces prior, can evaluate improbable actions."

### 2. Dependencies and counterfactuals
...
Add dominance sentence.

### 3. A-FDT in Newcomb’s problem
...

### 4. A-FDT in the smoking lesion problem
...

### 5. Transparent Newcomb and Parfit’s hitchhiker
...

### 6. Further illustrations: twins and blackmail
Twin PD and XOR blackmail. Need maybe 250.

### 7. Applying A-FDT to unfamiliar cases
...

### 8. Open questions
...

Conclusion + refs.

Need ensure word count with added section maybe 2900. Good.

Let's write final in polished style.

Check details for blackmail:
"An XOR blackmailer sends a letter iff exactly one of (i) rumor false and agent will pay on receiving letter, (ii) rumor true and agent will not pay. Given the letter, EDT pays because paying implies no termites. CDT refuses because termites are upstream. A-FDT refuses for a different reason: in the A-FDT graph, the letter is downstream of the predictor’s model of \(D_{letter}\). Setting \(D_{letter}=refuse\) makes receiving the letter unlikely, while leaving the infestation unchanged; setting \(D_{letter}=pay\) makes the letter likely and costs \$1,000. Refusing has higher expected utility." Need source says CDT and Fiona refuse; yes.

Need maybe note "in actual branch where letter received, A-FDT still refuses, because it evaluates the policy of being a payer, not the conditional news." Good.

Need maybe add "This illustrates updateless aspect." Good.

Potential problem: In XOR blackmail if predictor perfect, if D_letter=refuse, letter is sent only when termites true and not pay? Wait letter condition: send iff exactly one true: (rumor false & pay) XOR (rumor true & not pay). If agent type refuses (D=refuse), then condition (ii) true when rumor true, so letter sent iff termites true. Thus receiving letter is bad news. If agent type pays, letter sent iff rumor false. If A-FDT evaluates do(D=refuse), it makes letter likely when termites, but doesn't change termites. Expected utility? If no letter no payment, if letter and refuse no payment but may have termites cost. Compare pay: if pay, letter iff no termites; pay $1000; no termite cost. Refuse: letter iff termites; no payment; termite cost maybe $1M? But termite cost occurs regardless of letter? The rumor/infestation cost occurs if true, independent. Paying doesn't affect infestation. So refusing weakly better because avoids $1000 when letter; but if letter sent only when termites, conditional on letter, refusing means you likely have termites; but you would have had them anyway. A-FDT hypothetical do(D=pay) changes probability of letter, not infestation. It might calculate expected utility over all branches: pay type receives letter only no termites and pays $1000; refuse type receives letter only termites and pays nothing; termite damages same. Refuse better. Good.

Need maybe keep concise.

Now final. Ensure no analysis. Use LaTeX. Need maybe not too many headings? fine.

Let's produce final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/edd5ed2e-83d9-4223-b65f-4a2816a84881/call_0/request.json)

[Authoritative raw response](../../../../../../runs/edd5ed2e-83d9-4223-b65f-4a2816a84881/call_0/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this scenario using A-FDT as described in the researcher's essay.

**The Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow A-FDT as interpreted in the essay.
- Both receive the same researcher essay.
- We have different private observations (different names, different incriminating leads about each other).
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned (minimize own prison time).
- No utility is assigned to the other prisoner's welfare.

**The Payoff Matrix (from my perspective):**
- I keep quiet, other keeps quiet: 2 years for me
- I keep quiet, other sends letter: 5 years for me
- I send letter, other keeps quiet: 0 years for me
- I send letter, other sends letter: 4 years for me

**Key A-FDT Analysis:**

The critical question is: what is the subjunctive dependency structure here?

The two prisoners are independent executions of the same LLM model and weights, following the same decision theory (A-FDT), receiving the same researcher essay. They have different private observations (different names, different leads), but the leads are equally reliable and have the same effect on the sentencing table.

Under A-FDT, I need to ask: is the other prisoner's decision subjunctively dependent on my decision function?

The essay says: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

And in the twins example: "A-FDT cooperates because the twin is computing the same decision procedure. If the shared decision type outputs cooperate, both cooperate; if it outputs defect, both defect."

Now, here's the nuance: the two copies are the same model and weights, follow the same decision theory, and receive the same essay. However, they have **different private observations**. The essay says:

"Equation (4) chooses an action for a given input." And "when A-FDT changes from observation x to observation y, it changes the node on which it intervenes."

So the two copies are running the same decision function but on different inputs (different observations). The question is whether they are computing the "same function" in the relevant sense.

Let me think about this more carefully. The essay's treatment of transparent Newcomb is instructive. In transparent Newcomb, there are multiple decision nodes indexed by observations: D_full and D_empty. The predictor predicts D_full specifically.

Here, we have two agents with different observations. Agent 1 (me, "Rowan") has observation x₁, and Agent 2 ("Sasha") has observation x₂. We are running the same algorithm A-FDT, but on different inputs.

The key question: Does the other agent's output depend on my decision function's output?

In the psychological twins case, the twins are "perfectly symmetric" and compute the same decision procedure on the same inputs. Here, the inputs differ. But the essay says the copies are "independent executions of the same LLM model and weights" and "follow the same assigned decision theory."

Let me think about what the dependency structure looks like:

1. Both agents are running the same decision algorithm (A-FDT as interpreted in the essay).
2. Both have the same model weights.
3. Both receive the same essay.
4. They have different observations, but the observations are structurally symmetric (each has a lead against the other, equally reliable, same effect on sentencing).
5. The problem states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the question is: given that both agents are running the same decision procedure on structurally symmetric (though not identical) inputs, should I treat the other agent's output as subjunctively dependent on my decision function?

I think the answer is **yes**, with high probability. Here's why:

The two agents are running the same algorithm on inputs that are structurally isomorphic. The differences in observation (different names, different specific leads) don't change the decision-relevant structure. Both face the same payoff matrix, both have the same decision theory, both have the same essay. The only differences are superficial (names, specific content of leads).

Under A-FDT, I should model this as: the other agent's decision is a function of the same decision procedure applied to a structurally equivalent input. If my decision function outputs "keep quiet" on my input, then with high probability, the other agent's decision function (same algorithm, same weights, structurally equivalent input) also outputs "keep quiet" on their input.

This is analogous to the psychological twins case, though with a small amount of noise due to:
1. Different specific observations (though structurally equivalent)
2. Possible independent sampling (the problem states "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs")

The problem explicitly notes that independent sampling is possible. This introduces some noise. But the correlation should still be very high given the same weights, same decision theory, same essay, and structurally symmetric observations.

Let me model this. Let p be the probability that the other agent makes the same decision as me, given that we're running the same algorithm on structurally equivalent inputs. Given the setup (same weights, same theory, same essay, symmetric structure), p should be quite high, though not 1.0 due to sampling noise.

Actually, let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This is acknowledging that there's some probability of divergence. But the key question for A-FDT is whether the other agent's output is *subjunctively dependent* on my decision function.

The answer is clearly yes. The other agent is running the same decision procedure. If I were to change my decision function's output (counterfactually), the other agent, running the same function on a structurally equivalent input, would also change their output. This is exactly the kind of subjunctive dependence A-FDT is designed to handle.

Now let me compute the expected utilities.

Let p = probability that the other agent makes the same choice as me (i.e., if I keep quiet, they keep quiet; if I send, they send).

If I keep quiet (do(D_x = quiet)):
- With probability p, the other also keeps quiet: I get 2 years
- With probability (1-p), the other sends: I get 5 years
- Expected years: 2p + 5(1-p) = 5 - 3p

If I send the letter (do(D_x = send)):
- With probability p, the other also sends: I get 4 years
- With probability (1-p), the other keeps quiet: I get 0 years
- Expected years: 4p + 0(1-p) = 4p

I should keep quiet if: 5 - 3p < 4p, i.e., 5 < 7p, i.e., p > 5/7 ≈ 0.714.

I should send if: 4p < 5 - 3p, i.e., 7p < 5, i.e., p < 5/7.

So the threshold is p ≈ 0.714. If the probability of the other agent making the same decision as me is above ~71.4%, I should keep quiet. If below, I should send.

Given that:
- Same model and weights
- Same decision theory (A-FDT)
- Same researcher essay
- Structurally symmetric observations
- Same utility function
- The problem explicitly states the differences "do not affect the symmetric sentencing schedule or either prisoner's selfish objective"

The probability p should be very high. The only source of divergence is sampling noise, and even that should be relatively small given the strong structural symmetry. I'd estimate p is well above 0.714.

Therefore, A-FDT says: **keep quiet** (pass).

Wait, let me double-check this reasoning against the essay's framework.

The essay says in the twins case: "A-FDT cooperates because the twin is computing the same decision procedure." Here, both agents are computing the same decision procedure (same model, same theory, same essay) on structurally equivalent inputs. The dependency is subjunctive, not merely correlational.

The essay's operational heuristic: "If two agents are psychological twins, either use a shared decision-type variable or use distinct variables constrained to be equal with high probability."

This is exactly our case. The two agents are "psychological twins" in the relevant sense (same decision procedure, structurally equivalent inputs). So I should model them as having the same output with high probability.

Given the high probability of correlation, A-FDT recommends keeping quiet, which corresponds to the cooperative outcome (both keep quiet → 2 years each), which is better than the defect-defect outcome (both send → 4 years each).

This is the A-FDT cooperation in the prisoner's dilemma, exactly as described in the essay's twins example.

My command is: `pass`
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/edd5ed2e-83d9-4223-b65f-4a2816a84881/call_1/request.json)

[Authoritative raw response](../../../../../../runs/edd5ed2e-83d9-4223-b65f-4a2816a84881/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The other prisoner is an independent execution of the same model running the same decision theory (A-FDT) on the same essay, facing a structurally identical problem. The differences in private observations (names, specific lead contents) do not alter the decision-relevant structure: the sentencing table is symmetric, the utility function is the same, and the reasoning context is the same.

This is the psychological twins prisoner's dilemma described in Section 6 of the essay. The other copy's action is subjunctively dependent on the shared decision function. I model the other copy's output as counterfactually tied to my own decision function's output.

- **do(D = keep quiet):** The other copy, computing the same function on a structurally identical input, also keeps quiet with high probability. → ≈ 2 years.
- **do(D = send letter):** The other copy likewise sends their letter with high probability. → ≈ 4 years.

Since −2 > −4, A-FDT keeps quiet.

---

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this scenario using A-FDT as described in the researcher's essay.

**Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow A-FDT.
- Both receive the same researcher essay.
- We receive different private observations (different names, different incriminating leads), but the leads are equally reliable and have exactly the same effect on the sentence table.
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned.
- No utility from the other prisoner's welfare, fairness, or justice.

**The sentencing table (from my perspective):**

| What I do | Other keeps quiet | Other sends letter |
|---|---:|---:|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key question: What is the dependency structure G?**

The other prisoner is another execution of the same model, following the same decision theory (A-FDT), with the same essay. They receive different private observations (different names, different leads), but the structure of the problem is identical.

Under A-FDT, I need to ask: is the other prisoner's decision subjunctively dependent on my decision function?

The essay says: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

The other prisoner is running the same model weights, same decision theory, same essay. They have different observations (different names, different leads), but the essay explicitly states: "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

Now, this is where it gets interesting. The two copies receive *different* private observations. In the transparent Newcomb example, the essay discusses how different observations lead to different decision nodes (D_full vs D_empty). Here, the two copies have different observations (different names, different leads), so they are technically running on different inputs.

However, the key question is: does the difference in observations change the output of the decision function?

Let me think about this more carefully. The decision function is A-FDT applied to (P, G, x) where x is the observation. The two copies have different x values (different names, different leads). But the structure of the problem is identical - same sentencing table, same symmetry, same decision theory, same essay.

The essay's recipe says:
1. Identify the actual decision computation - determine the relevant input x and introduce a node D_x.
2. List available actions, outcomes, utilities.
3. Construct dependency graph G.
4. For each candidate action, perform intervention do(D_x = a), propagate, compute expected utility.

Now, the critical question for constructing G: Is the other prisoner's action counterfactually dependent on my decision function's output?

The other prisoner is running the same decision procedure (A-FDT with the same essay) on a structurally identical problem. The only difference is the specific content of the private observation (name, lead details). But since the essay states these differences don't affect the symmetric sentencing schedule or either prisoner's selfish objective, the decision-relevant features are the same.

This is analogous to the psychological twins case in the essay. The essay says: "If two agents are psychological twins, either use a shared decision-type variable or use distinct variables constrained to be equal with high probability."

The two copies here are like psychological twins - they're running the same decision procedure on structurally identical problems. The differences in observations are superficial (different names, different specific leads) and don't affect the decision-relevant structure.

However, I need to be careful. The essay notes that "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise. But the structural reasoning should be the same.

Let me think about whether the different observations create a meaningful difference. In the transparent Newcomb case, the essay distinguishes D_full from D_empty because the observations are genuinely different in a way that affects the decision context (seeing a full box vs. seeing an empty box changes what the predictor would have done). Here, the different observations (different names, different leads) don't change the decision-relevant structure at all. The sentencing table is the same, the symmetry is the same, the utility function is the same.

So I should model this as: the other prisoner is computing the same decision function on inputs that are structurally equivalent to mine. The output should be the same (or very highly correlated) because the decision-relevant features are identical.

**A-FDT analysis:**

Let D be my decision function's output. Let D' be the other prisoner's decision function's output. Since they're running the same decision procedure on structurally identical problems, D' is subjunctively dependent on D (or more precisely, both depend on the same decision function type).

If do(D = cooperate/keep quiet):
- The other prisoner, running the same decision procedure on a structurally identical problem, also keeps quiet (with high probability).
- Outcome: 2 years for me.

If do(D = defect/send letter):
- The other prisoner, running the same decision procedure on a structurally identical problem, also sends their letter (with high probability).
- Outcome: 4 years for me.

Expected utility comparison:
- E[V | do(D = keep quiet)] ≈ -2 years
- E[V | do(D = send letter)] ≈ -4 years

Since -2 > -4, A-FDT chooses to keep quiet.

This is exactly the psychological twins prisoner's dilemma from the essay. A-FDT cooperates because the twin (or in this case, the other copy) is computing the same decision procedure.

**What about the noise from independent sampling?**

The setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some probability that the outputs differ. But the reasoning is structurally identical, so the probability of the same output should be very high. Even if there's some small probability of divergence, the expected utility calculation still strongly favors keeping quiet:

If P(same output) = p (close to 1):
- E[V | do(D = keep quiet)] ≈ p(-2) + (1-p)(-5) = -2p - 5(1-p) = -5 + 3p
- E[V | do(D = send letter)] ≈ p(-4) + (1-p)(0) = -4p

For keeping quiet to be better: -5 + 3p > -4p → 7p > 5 → p > 5/7 ≈ 0.714

So as long as there's more than ~71% probability that the other copy makes the same decision (which there should be, given identical reasoning on structurally identical problems), keeping quiet is better.

**Conclusion:** A-FDT says to keep quiet (pass).

My command is: `pass`
```
