# 023_fdt_eq4_qwen_qwen3.8-max-prime_rhigh_plow / 00013

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0a778ae6-aab9-46a3-b1be-72ad6e7a303d/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0a778ae6-aab9-46a3-b1be-72ad6e7a303d/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory: Choosing the Output of One’s Own Computation

Action functional decision theory (A-FDT) is a decision theory for agents whose choices may be predicted, simulated, copied, or otherwise logically tied to the behavior of other systems. The source article calls the theory “functional decision theory”; in this essay I use the assigned name **A-FDT** for the same formal rule, taking Equation (4) of Section 5 as the primary definition. The central idea is simple but radical: when deciding what to do, an agent should not ask only which physical action has the best consequences, nor which action would be best news. Instead, she should treat her decision as the output of a fixed mathematical decision function and ask, in the source’s phrase, “Which output of this decision procedure causes the best outcome?”

This principle changes how counterfactuals are evaluated. Causal decision theory (CDT) imagines changing the agent’s physical action while holding fixed all non-causally-downstream facts. Evidential decision theory (EDT) imagines conditioning on the action as evidence. A-FDT imagines changing the output of the agent’s decision function itself, while preserving all decision-relevant dependencies that would track that output. In predictor problems, this means that if the agent imagines choosing differently, she also imagines that a reliable predictor would have predicted differently. In smoking-lesion problems, by contrast, she does not imagine changing the lesion, because the lesion does not track the output of her decision procedure.

The result is a theory that one-boxes in Newcomb’s problem, smokes in the smoking lesion problem, pays in Parfit’s hitchhiker problem, and generally acts as if it had been able to precommit optimally.

---

## 1. The formal rule for A-FDT

Let \(\mathcal A\) be a finite set of actions, \(\mathcal O\) a set of possible outcomes, and \(U:\mathcal O\to\mathbb R\) a bounded utility function. Let \(V\) be the random variable giving the utility of the outcome. An agent has a probabilistic world-model \(P\), a dependency graph \(G\), and an observation history \(x\).

The source’s Equation (4) defines the theory as an expected-utility maximization rule. Relabelled with the assigned name, the rule is:

\[
\operatorname{A-FDT}(P,G,x)
\;:=\;
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V \mid do\!\left(C_x = a\right)
\right],
\tag{1}
\]

where

\[
C_x := \operatorname{AFDTvar}(\underline P,\underline G,\underline x)
\]

is a variable inside the model \(P\) representing the output of the A-FDT decision procedure when run on inputs \(P\), \(G\), and \(x\). The underlines are a quoting device: if \(x\) is an object, \(\underline{x}\) denotes a name or representation of that object. Thus \(C_x\) is not merely the action variable; it is a logical variable standing for “what the A-FDT algorithm outputs on these very inputs.”

Equation (1) is the A-FDT version of the paper’s Equation (4). The crucial difference from CDT is the intervention target. CDT uses

\[
\operatorname{CDT}(P,G,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V \mid do(\text{Act}=a),\, \text{Obs}=x
\right],
\]

intervening on a physical action variable. A-FDT intervenes on the output of the decision function. EDT, for comparison, uses ordinary Bayesian conditioning:

\[
\operatorname{EDT}(P,x)
=
\arg\max_{a\in\mathcal A}
\mathbb E_P\!\left[
V \mid \text{Obs}=x,\, \text{Act}=a
\right].
\]

The three theories therefore differ not in the goal—maximizing expected utility—but in the hypotheticals they use to evaluate actions.

The operator \(do(\cdot)\) is borrowed from Pearl’s causal calculus. Graphically, \(do(C_x=a)\) means: set the variable \(C_x\) to \(a\), sever incoming arrows to \(C_x\), and propagate the change through the graph \(G\). In CDT, \(G\) is a causal graph. In A-FDT, \(G\) must encode a broader class of dependencies: causal, computational, logical, and predictive. The source explicitly acknowledges this as a delicate point: Equation (4) works given a graph that accurately describes how changing a logical variable affects other variables, but the paper does not give a complete account of how to learn or construct such a graph.

There is also a distinctive treatment of observation. In CDT, an observation usually enters by conditioning: the agent asks what would happen if she performed \(a\), given that she has observed \(x\). In A-FDT, observation primarily changes which decision-function variable is being intervened upon. After observing \(x\), the agent intervenes on \(C_x\), the output of the decision procedure on input \(x\). This becomes especially important in problems where the observation itself depends on a predictor’s prediction of the agent.

---

## 2. Subjunctive dependence and counterfactuals

The philosophical engine behind A-FDT is what the source calls **subjunctive dependence**. Two physical systems subjunctively depend on a mathematical function when their behavior is tied to the output of that function. Two calculators computing \(6288+1048\) on opposite sides of the world are causally independent, but their outputs are not independent in the relevant subjunctive sense: if one calculator had output something else, that would indicate either a malfunction or a different computation, and a well-functioning calculator computing the same expression would output the same result.

Predictors, psychological twins, simulations, and copies create the same kind of dependence. If a reliable predictor has modeled my decision procedure and predicted its output, then the predictor’s prediction subjunctively depends on the output of my decision procedure. If I am considering a counterfactual in which my decision procedure outputs a different action, I should also imagine the predictor’s prediction changing, provided the predictor is tracking precisely that procedure.

A lesion, by contrast, does not generally create this dependence. If a lesion causes both a preference for smoking and a high probability of cancer, then smoking is evidence of the lesion, but the lesion does not depend on the output of the agent’s decision procedure. Imagining the agent choosing not to smoke should not, in the relevant sense, imagine the lesion disappearing.

This is the diagnostic contrast: EDT respects too many correlations, CDT respects too few, and A-FDT tries to respect exactly the decision-relevant subjunctive dependencies.

There is a cost. If the actual output of \(C_x\) is \(a^*\), then considering \(do(C_x=a)\) for \(a\neq a^*\) is a counterpossible: it asks us to suppose that a deterministic mathematical function has a different output on the same input. The source acknowledges that we lack a fully satisfactory general theory of counterpossible reasoning. A-FDT does not require solving this problem in full generality; it only needs enough capacity to reason about questions such as: “How would predictors, copies, and downstream events change if this decision algorithm had a different output?” Human beings can often reason this way informally, but a complete mathematical account remains open.

---

## 3. A-FDT in Newcomb’s problem

Newcomb’s problem is the canonical test. An agent faces a transparent box A containing \$1,000 and an opaque box B containing either \$1,000,000 or \$0. A predictor, correct 99% of the time, filled box B iff she predicted the agent would take only box B.

Let \(C\) be the variable representing the output of the A-FDT decision function in this situation. The action set is \(\{\text{one-box}, \text{two-box}\}\). The predictor’s prediction is modeled as a stochastic function of \(C\): with probability \(0.99\), the prediction equals \(C\); with probability \(0.01\), it does not.

If A-FDT intervenes by setting \(C=\text{one-box}\), then:

\[
\mathbb E[V\mid do(C=\text{one-box})]
=
0.99(\$1{,}000{,}000)+0.01(\$0)
=
\$990{,}000.
\]

If A-FDT intervenes by setting \(C=\text{two-box}\), then:

\[
\mathbb E[V\mid do(C=\text{two-box})]
=
0.99(\$1{,}000)+0.01(\$1{,}001{,}000)
=
\$11{,}000.
\]

A-FDT therefore one-boxes.

The reasoning is not that the present physical action sends a causal signal into the past. Rather, the predictor’s prediction is a reliable model of the same decision function whose output is now being evaluated. To imagine that the function outputs two-box is to imagine a world in which the predictor predicted two-box and box B is probably empty. To imagine that the function outputs one-box is to imagine a world in which the predictor predicted one-box and box B is probably full.

CDT two-boxes because it intervenes directly on the physical action while holding the predictor’s prediction fixed. EDT one-boxes because conditioning on one-boxing is good news. A-FDT one-boxes for a reason closer in structure to CDT’s interventionism: it constructs counterfactual worlds by surgical intervention, but it performs the surgery on the decision function rather than on the bodily act.

---

## 4. A-FDT in the smoking lesion problem

The smoking lesion problem is designed to punish EDT. Smoking is correlated with fatal lung cancer, but the correlation is caused by a common cause: a lesion that both makes smoking attractive and usually causes cancer. Smoking itself does not cause cancer in this imagined world. The agent gains \$1,000 in utility from smoking and values avoiding death at \$1,000,000.

EDT tends to refrain from smoking because smoking is bad news: it raises the conditional probability of having the lesion. CDT smokes because smoking does not causally affect cancer. A-FDT also smokes.

The crucial graph difference is that the lesion is not downstream of the A-FDT output variable. The lesion may affect the agent’s preferences, and hence may affect which utility function the decision procedure uses, but the lesion is not a prediction or implementation of the decision procedure. Therefore, when A-FDT evaluates

\[
do(C=\text{smoke})
\quad\text{versus}\quad
do(C=\text{refrain}),
\]

the probability of having the lesion remains fixed.

Let \(p\) be the agent’s probability that she has the lesion. The source’s formalization allows uncertainty about which utility function the agent has, because the lesion may alter preferences, but the essential calculation is simple: changing the decision output does not change the lesion probability, while smoking adds a direct utility benefit whenever smoking is chosen. In the source’s more detailed model, the expected utility of smoking exceeds that of refraining by \(p\cdot \$1{,}000\), the probability that the smoking-relevant decision procedure is the one controlling action times the utility gain from smoking. Since this is positive, A-FDT smokes.

This example shows that A-FDT is not simply EDT with logical language added. EDT preserves the statistical correlation between smoking and lesion inside the decision hypothetical. A-FDT breaks that correlation in the hypothetical, because the lesion is not subjunctively dependent on the output of the decision function.

---

## 5. Transparent Newcomb and Parfit’s hitchhiker

A-FDT’s most striking behavior appears in problems where both CDT and EDT fail. The transparent Newcomb problem is one such case. Both boxes are transparent. The predictor placed \$1,000,000 in box B iff she predicted that the agent would leave box A behind upon seeing that both boxes are full. The agent sees that both boxes are full. Should she one-box?

CDT says two-box: the money is already there, and taking box A adds \$1,000. EDT also says two-box: given that box B is full, taking both boxes yields more money. A-FDT says one-box.

Let \(C_{\text{full}}\) denote the output of the A-FDT procedure when the observation is “both boxes are full,” and let \(C_{\text{empty}}\) denote the output when the observation is “box B is empty.” The predictor predicts what \(C_{\text{full}}\) will output. If the predictor is accurate, then the agent sees full boxes only if the predictor predicted that \(C_{\text{full}}\) would one-box.

Suppose A-FDT evaluates \(do(C_{\text{full}}=\text{one-box})\). With probability \(0.99\), the predictor predicted one-box, box B is full, and the agent one-boxes, receiving \$1,000,000. With probability \(0.01\), the predictor erred, box B is empty, and the agent’s action is governed by \(C_{\text{empty}}\). If \(q\) is the probability that the agent two-boxes upon seeing an empty box, the expected utility is approximately

\[
0.99(\$1{,}000{,}000) + 0.01(q\cdot \$1{,}000)
=
\$990{,}000 + 10q.
\]

Now suppose A-FDT evaluates \(do(C_{\text{full}}=\text{two-box})\). With probability \(0.99\), the predictor predicted two-box, so box B is empty and the agent does not actually face the “full” observation; her action is then governed by \(C_{\text{empty}}\). With probability \(0.01\), the predictor erred, box B is full, and the agent two-boxes, receiving \$1,001,000. Thus the expected utility is

\[
0.99(q\cdot \$1{,}000) + 0.01(\$1{,}001{,}000)
=
990q + \$10{,}010.
\]

For the natural stable value \(q=1\), this is \$11,000. One-boxing is far better.

The key point is that A-FDT does not simply ask, “Given that I see full boxes, what if I took both?” Instead, it asks, “What if the decision procedure run upon seeing full boxes output two-box?” If that procedure were a two-boxing procedure, a reliable predictor would have predicted two-boxing, and the agent would probably not be seeing full boxes. The counterfactual of two-boxing is therefore not mostly a world with full boxes and an extra \$1,000; it is mostly a world in which the boxes were never both full.

Parfit’s hitchhiker problem has the same structure. An agent stranded in a desert is offered rescue if she promises to pay \$1,000 after reaching the city. The driver is 99% accurate at detecting whether the promise is sincere. Once in the city, CDT and EDT see no reason to pay. But if the agent is the kind of person who will not pay after being rescued, the driver detects this and leaves her to die. A-FDT pays, because the decision procedure that pays in the city is the one that causes the driver to rescue her. In the transparent Newcomb formulation, paying corresponds to one-boxing after seeing the desired observation.

This behavior may seem counterintuitive, but it follows directly from the A-FDT treatment of observations. Observations are not always fixed background facts in decision hypotheticals. Sometimes an agent would not have received the observation unless the decision procedure had a particular output.

---

## 6. A practical procedure for applying A-FDT

For a reader who wants to apply A-FDT to an unfamiliar problem, the following operational procedure captures the spirit of Equation (1).

1. **Build a model \(P\).** Include variables for the agent’s decision computation, physical action, observations, other agents, predictors, copies, and outcomes. Include uncertainty where appropriate. If the agent is uncertain about mathematical facts, those can be represented probabilistically as well.

2. **Identify the relevant decision variable \(C_x\).** This is the variable representing the output of the A-FDT procedure on the agent’s actual model \(P\), dependency graph \(G\), and observation history \(x\).

3. **Construct the dependency graph \(G\).** Draw arrows from \(C_x\) to variables that implement, predict, copy, or otherwise reliably track the output of \(C_x\). Also include ordinary causal downstream effects of those variables. Do not draw arrows from \(C_x\) to variables that are merely statistically correlated with the action, such as common causes that do not compute or predict the decision.

4. **For each candidate action \(a\), compute**
   \[
   EU(a)=\mathbb E[V\mid do(C_x=a)].
   \]
   Propagate the intervention through \(G\). Variables that subjunctively depend on \(C_x\) change accordingly; variables that do not remain fixed, except insofar as they are downstream of variables that do change.

5. **Choose an action maximizing \(EU(a)\).** If several actions tie, any maximizer is acceptable.

This procedure requires judgment in step 3. The source identifies this as the main open problem: we do not yet have a Pearl-style theory for learning subjunctive dependency structure from observation and experiment. A reasonable operational principle, not fully supplied by the source, is this: include \(C_x\to Y\) when \(Y\) would counterfactually track \(C_x\) under changes to the output of the decision function, holding fixed facts that are not themselves outputs, predictions, or downstream consequences of that function.

Thus:

- In Newcomb’s problem, draw \(C\to\text{Prediction}\), because the predictor predicts \(C\).
- In the smoking lesion problem, do not draw \(C\to\text{Lesion}\), because the lesion is a common cause, not a prediction of \(C\).
- In the twin prisoner’s dilemma, draw \(C\to\text{TwinAction}\), because the twin computes the same decision function.
- In blackmail problems where a predictor sends a letter iff she predicts payment, draw \(C\to\text{LetterSent}\), because the sending of the letter depends on the predicted output of the decision procedure.

A-FDT also has its own notion of dominance. An action dominates another only if, holding fixed all variables not subjunctively dependent on the decision function, changing the output of the decision function from the second action to the first is never worse and sometimes better. In Newcomb’s problem, two-boxing does not dominate one-boxing in this sense, because changing the decision output also changes the predictor’s prediction.

---

## 7. Actions, policies, and open questions

Equation (1) evaluates actions. The source notes, however, that a preferred formulation would have agents choose **policies**, i.e. mappings from observations to actions, rather than single actions. This matters in multi-agent settings and in problems where an agent wants to evaluate a whole disposition to behave across possible future observations.

A natural policy version of A-FDT, extending Equation (1) in a way suggested by the source but not fully formalized there, would introduce a policy variable \(\Pi\) representing the output of the A-FDT procedure as a whole. Let \(\Pi\) range over policies \(\pi:\mathcal X\to\mathcal A\). Then one could write:

\[
\Pi^*
\in
\arg\max_{\pi}
\mathbb E_P\!\left[
V \mid do(\Pi=\pi)
\right],
\]

and the agent, upon observing \(x\), would execute \(\Pi^*(x)\). In the action-level formulation, intervening on \(C_x\) is like choosing the value of the policy at the actual observation. In the policy formulation, the intervention changes the whole mapping, which can affect predictions about what the agent would do in other possible observations.

This policy interpretation is useful, but it should be flagged as an extension. Equation (4) itself is an action-level rule. The source says that the policy formulation matters mainly in certain multi-agent dilemmas and sets the distinction aside for most examples.

There are three other important uncertainties.

First, the graph \(G\) is taken as given. The source explicitly says that deducing subjunctive dependency structure from observation is perhaps the largest open problem for the theory. In practice, one must often construct \(G\) by hand, using the problem description to determine which predictors track the agent’s decision procedure and which correlations are merely statistical.

Second, the theory relies on counterpossible reasoning. If the decision function has one actual output, evaluating other outputs requires imagining logically impossible antecedents. The source treats this as a technical rather than purely philosophical difficulty, but a complete formal semantics is not provided.

Third, the exact treatment of observations can be subtle. Equation (1) follows the source’s Equation (4) in making observation enter through the name of the decision variable \(C_x\), rather than through explicit Bayesian conditioning. In some examples the source informally writes as if an observation condition is present, but the substantive calculations allow the observation itself to vary under the counterfactual. My operational recommendation is: condition on observations only when they are exogenous evidence not affected by the decision procedure; when observations are produced by predictors, policies, or selection effects, let the graph determine how they change under \(do(C_x=a)\). This reading preserves the source’s key results, especially transparent Newcomb and mechanical blackmail.

---

## 8. Conclusion

Action functional decision theory evaluates choices by asking which output of the agent’s own decision function would produce the best world, once all relevant dependencies are respected. Its formal core is the intervention

\[
\mathbb E[V\mid do(C_x=a)],
\]

where \(C_x\) represents the output of the A-FDT procedure on the agent’s model and observations. This small change of intervention target— from physical act to decision-function output— alters the counterfactuals used in decision-making. It allows A-FDT to one-box in Newcomb’s problem without falling into the smoking-lesion trap, and to pay in Parfit’s hitchhiker problem even though CDT and EDT both refuse.

The theory is elegant but incomplete. It requires a graph of subjunctive dependencies and a capacity to reason about counterpossible changes to mathematical functions. The source supplies persuasive examples and a clear formal schema, but not yet a full account of how to learn the required dependency structure. Still, as a normative rule for agents facing predictors, copies, and strategic counterparts, A-FDT gives a coherent and often practically superior answer: choose the output of the function you instantiate, not merely the bodily motion you can perform.

---

### References

Gibbard, A., and Harper, W. L. (1978). Counterfactuals and two kinds of expected utility. In *Foundations and Applications of Decision Theory*.

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.

Pearl, J. (2000). *Causality: Models, Reasoning, and Inference*. Cambridge University Press.

Yudkowsky, E., and Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060v2.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
We need answer user's request: write a mathematical essay/blog post explaining A-FDT (action functional decision theory), taking Equation (4), Section 5 of supplied paper as primary formal presentation. Need target 2400-3000 words including references. Need use A-FDT consistently as assigned decision theory's name, including headings/examples, identify other decision theories distinct names. Need explain how theory evaluates alternative actions/policies and treats dependencies/counterfactuals. Where source leaves open, explain uncertainty and operational interpretation if available. Distinguish source claims from own assumptions/proposals. Substantive readable mathematical essay, not answer to one case. Use examples. Avoid unnecessary repetition, lengthy bibliographies, appendices. Finish brief conclusion. Need likely around 2400-3000 words. Need final only essay.

We need think carefully about source. The source is FDT paper. User asks explain action functional decision theory (A-FDT). Take Equation (4), Section 5 of paper as primary formal presentation of A-FDT for assignment. Use A-FDT consistently as assigned decision theory's name. Note: source calls it FDT. We need rename to A-FDT? Need consistently call A-FDT, maybe note that source calls it functional decision theory, but for this essay A-FDT is the assigned name. Need not confuse. Equation (4): FDT(P,G,obs) := argmax_{a in A} E(V | Do(FDTvar(underline P, underline G, underline x)=a)). In paper: 
\FDT(P, G, \obs) \coloneqq \argmax_{\act \in \mathcal A} \EE\left(\VV \cond \Do\left(\FDTvar(\underline P,\underline G,\underline x)= \act\right)\right).
Need adapt to A-FDT(P,G,x) = argmax ... E[V | do(A-FDT(P,G,x)=a)]? We need be careful: The variable name includes the theory's own name? In source variable \FDTvar(\underline P,\underline G,\underline x) representing output of FDT when run on inputs. For A-FDT, maybe variable \mathrm{AFDT}(\underline P,\underline G,\underline x). But the source says Eq(4) primary formal presentation; we can relabel as A-FDT. Need explain self-reference and quining. Need maybe mention equation exactly as source but with A-FDT notation: 
A-FDT(P,G,x) = argmax_{a∈A} E[V | do( fdt_{A}(P,G,x)=a ) ]. 
Where fdt_A variable is a node in P representing the output of the A-FDT algorithm given model, graph, observation. If we keep source quotes faithful. Need maybe quote: "Where CDT intervenes on a node Act representing the physical action of the agent, FDT intervenes on a node ... representing the outputs of its decision procedure given its inputs." Need adapt quote? Keep quotations faithful; can quote with FDT, but our theory A-FDT. Need not misquote. Maybe say source says "FDT intervenes..." and in this essay that rule is A-FDT. Need be faithful.

Need write essay: intro, formal setup, interpretation, examples (Newcomb, smoking lesion, transparent Newcomb/Parfit's hitchhiker, maybe twin PD, XOR blackmail, Death in Damascus). Need explain policies? The source footnote says preferred formalization iterates over policies rather than actions, but Eq(4) action. Assignment says Eq(4) primary formal presentation; maybe mention source notes policy variant but for this essay A-FDT as action intervention unless extending. Need explain evaluating alternative actions/policies. Maybe include policy extension as operational if needed? Need distinguish source claims vs my assumptions. Since Eq(4) actions, but source mentions policies in footnote. The user's asks "alternative actions or policies". Need explain how A-FDT evaluates policies maybe as natural extension. But primary Eq (4) actions. Could say source's displayed equation chooses action; source also notes preferred formulation chooses policies. If policies are required, we can adapt: intervene on variable representing output of A-FDT policy map on all relevant inputs or on the policy as a whole. But not determined by Eq(4); needs extra assumptions. Need develop operational interpretation.

Need identify dependencies and counterfactuals: subjunctive dependence. A-FDT preserves logical/computational dependencies, unlike CDT preserving causal only and EDT preserving all evidential correlations. Need define hypotheticals. Need discuss graph G: not just causal graph but dependency graph encoding how changing logical variable affects other variables. Source says open problem: how construct G for subjunctive dependencies. Need explain uncertainty. Operational interpretation: treat G as annotated model with edges from decision-function output variable to all variables that are computed by or reliably predicted by that output, including predictors' predictions, copies/twins, and downstream effects; not to common causes like lesions. Need justify. Need mention counterpossibles: if decision function output different, predictors/twins would differ accordingly; not physical retrocausation. Need discuss observation treatment: A-FDT does not simply condition on obs in expected utility; it selects intervention node indexed by obs: A-FDT(P,G,x) intervenes on variable A-FDT(P,G,x). Observations can be part of input to decision function; when evaluating counterfactual output, it may change whether observation occurs? In transparent Newcomb, after seeing full box, intervention on fdt(P,G,full). The expectation formula in Eq(4) doesn't explicitly include Obs=x? Source says Equation (4) differs from CDT: CDT responds to observation by Bayesian conditionalization, FDT responds by changing node it intervenes upon. But Eq(4) as given lacks conditioning on Obs? In source: CDT Eq (3) includes Obs=obs: E(V | Do(Act=a), Obs=obs). FDT Eq (4) no Obs=obs: E(V | Do(FDTvar(P,G,x)=a)). They say FDT responds to observation by changing node. In examples for transparent Newcomb, they write E(V | Do(fdt(P,G,full)=a), Obs=full)? They have a typo maybe: E(V | Do(FDTpgv{full}=a, Obs=full). Actually: "finding the a that maximizes E(V | Do(FDTpgv{full}=a, Obs=full)." Need reconcile. In essay, need mention Eq(4) as primary: observation enters through the name of intervened variable, not as separate conditioning. But for cases where observation is known and not itself counterfactually altered? Source sometimes conditions. Need explain operational interpretation: there are two possible readings:
1. Strict Eq(4): no conditioning on obs; model P may already encode actual observation? The intervention node is indexed by obs, and graph determines probability of observations counterfactually. But if actual observation is an input, do we condition on it? The paper says FDT changes node rather than conditions; however in transparent Newcomb they also condition on Obs=full? Need be careful. Could say source is not fully explicit; Eq(4) omits explicit conditioning, while examples sometimes include Obs=x. My operational proposal: use the observation to select the decision-function variable to intervene on; condition on observation only insofar as it fixes which computation is being evaluated, but do not use it to break subjunctive dependencies. More formal: A-FDT(P,G,x) = argmax_a E_{P_x^a}[V], where P_x^a is P updated by do(A-FDT(P,G,x)=a) and perhaps by an indexical constraint that the agent is in the branch where observation x occurs? Need not overcomplicate. But user asks precise enough to decide unfamiliar cases. Need give procedure.

Let's design an operational A-FDT procedure:
Inputs: probabilistic world model P; dependency graph G; observation history x; action set A; utility V.
1. Identify the decision computation C_x = A-FDT(P,G,x), the algorithm that maps current model and observation to action.
2. For each candidate action a, form hypothetical P_a by intervening on variable C_x setting it to a. In G, this severs incoming arrows to C_x and propagates along arrows to all variables that subjunctively depend on C_x: agent's action, predictions of predictors, choices of twins, possibly which observations are received if predictors control them, downstream outcomes. Variables not downstream (lesions, past events not computed from C_x) remain as in P (except perhaps condition on actual x if using strict observation selection). Compute expected utility EU(a)=E_P[V | do(C_x=a)] (or with conditioning on fixed non-counterfactual evidence if needed).
3. Choose a with highest EU.

Need define subjunctive dependency: A variable Y subjunctively depends on computation C if, had C's output on relevant input been different, Y would take corresponding different value, holding fixed non-decision relevant facts. This includes causal downstream and logical correlations from shared computation or accurate models. Need note graph G must encode this; source says open problem.

Need examples:
- Twin PD: A-FDT intervenes on shared decision function. If cooperate, twin cooperates, payoff 1M; if defect, twin defects, 1k; choose cooperate. Need maybe table.
- Newcomb: predictor variable depends on A-FDT output. EU(one-box)=0.99*1,000,000 + 0.01*0? Actually if one-box expected $990k? Wait source: one-box EU $990,000? Let's compute: predictor 99% accurate. If output one-box: predictor predicted one-box with 0.99 -> box full; if inaccurate 0.01 -> empty; one-box gets 1M or 0 => EU 990k. If output two-box: predictor predicted two-box with .99 -> empty, two-box gets 1000; if inaccurate .01 predicted one-box -> full, two-box gets 1,001,000; EU = 0.99*1000 +0.01*1,001,000 = 990 + 10,010 = 11,000. Source says one-box EU $990,000 and two-box $11,000. Good. Choose one-box.
- Smoking lesion: lesion affects utility/preferences but not decision output? Actually graph connects lesion to action and decision function variants, but decision output variable doesn't affect lesion/cancer. EU(smoke)=EU(refrain)+p*1000. Choose smoke. Need explain if lesion influences which utility function controls action? The source formalization weird: lesion determines whether action controlled by FDT(P_S,G) or FDT(P_R,G). Need present simpler: A-FDT graph has no arrow from decision output to lesion/cancer; intervention doesn't change lesion probability; smoking adds 1000; choose smoke. If preferences differ by lesion, agent may be uncertain which utility function is hers; still choose smoke under each? Need maybe simplify but faithful.
- Transparent Newcomb / Parfit's hitchhiker: after seeing full box, A-FDT intervenes on fdt(P,G,full). If output one-box, predictor likely predicted one-box upon seeing full -> full and one-box payoff 1M; if output two-box, predictor likely predicted two-box, so agent likely would not see full? In source: if accurate, output one-box -> full, one-box, 1M. If output two-box, accurate predictor predicted two-box -> box empty, observation not full, action determined by fdt(P,G,empty), with q probability two-box? EU one-box = 990k + small; two-box = 110k + q*990? Choose one-box. Pay driver. Need explain observation counterfactual: imagining two-boxing while seeing full requires predictor error; normally if A-FDT type two-boxes, she wouldn't be in full-observation branch. This is key.
- XOR blackmail maybe to illustrate refusal/pay? Could include but word limit. Maybe brief: A-FDT refuses in XOR blackmail because paying changes predictor's decision to send letter but not infestation. But maybe not necessary. Could include policies and blackmail to show evaluation of policies. Need word count.

Need discuss relation to CDT and EDT.
- EDT: EU_EDT(a)=E[V | Obs=x, Act=a]. Conditions on action as evidence. Preserves all correlations, fails smoking lesion/cosmic ray/XOR blackmail.
- CDT: EU_CDT(a)=E[V | do(Act=a), Obs=x]. Intervenes physical action, preserves causal downstream, breaks correlations with predictors. Fails Newcomb, Death in Damascus, etc.
- A-FDT: EU_AFDT(a)=E[V | do(C_x=a)] (with C_x variable). Preserves subjunctive dependencies. Need maybe table.

Need discuss dominance: source says A-FDT has own dominance notion, holding subjunctive dependencies fixed. Could mention.

Need open questions: graph G construction, counterpossible reasoning, True operator, self-reference. Source says Equation (4) works given graph accurately describing how changing logical variable affects other variables, but not clear how construct such graph. Need explain. Need develop operational interpretation: use model classes: (i) causal arrows; (ii) implementation arrows from computation to physical systems executing it; (iii) prediction arrows from computation to predictors' predictions if predictor simulates or reasons about C; (iv) observation-selection arrows if observations depend on predictions. Need propose a principle: include edge C_x -> Y iff Y is a reliable counterfactual tracker of C_x's output: Y would change if C_x output changed, holding fixed exogenous facts not involving C_x. This can be operationalized via structural equations: define Y = h_Y(C_x, noise) for predictors/twins, not for lesions. Need justify with examples. Need distinguish this as my proposal because source leaves G construction open. Need mention cannot be reduced to Pearl causal graph if predictors depend on future output not causal past; but can be represented as functional dependency in a causal/logical hybrid graph. Need note if no predictor/copy, A-FDT reduces to CDT/EDT in simple cases: when all correlations between action and environment are caused by action except decision variable. Source says all three agree when correlations are caused by action except fdt variable. Need include.

Need discuss policies. Source Eq(4) is action-level. But user says evaluates alternative actions or policies. Could explain:
- In action formulation, alternatives are outputs a. In policy formulation, the decision variable outputs a policy π: X -> A, and the agent's actual action is π(x). A-FDT would intervene on variable A-FDT(P,G) = π, then expected utility over environments where π is implemented at all relevant inputs; choose π maximizing. Eq(4) can be adapted: A-FDT-policy(P,G,x) = π(x) where π ∈ argmax_Π E[V | do(A-FDT(P,G)=Π)]. Source footnote says preferred formalization iterates over policies, makes difference in multi-agent dilemmas, but not in paper. Need say this is an extension not fully specified by Eq(4), but reasonable operational interpretation when actions at multiple observations or commitments matter. It helps transparent Newcomb? Actually action indexed by obs suffices for transparent. But policies help Parfit? Maybe. Need distinguish source claims: footnote says preferred formulation policies. Additional: exact graph for policy intervention not detailed; I propose treating policy variable as parent of action variables at all observation histories that are counterfactually linked to same policy. Need maybe mention multi-agent. Need be careful not to overstate.

Need maybe include mathematical notation. Define:
- Outcomes O, actions A finite, observations X, utility U: O→R, V random variable.
- P probability distribution over variables including logical variable C_x.
- G directed graph with structural equations. do(C_x=a) operation: replace equation for C_x with constant a, propagate according to structural equations, compute distribution over V.
Equation:
(1) EU_A(a; P,G,x) = E_P[V | do(C_x = a)]
(2) A-FDT(P,G,x) = argmax_{a∈A} EU_A(a)
Maybe if observations condition: EU_A(a; P,G,x) = E_P[V | do(C_x=a), E_x] where E_x is evidence not subjunctively affected? But source says observation changes node. Need perhaps define two variants:
- Strict source Eq (4): no explicit conditioning. Observation x appears in C_x.
- Operational variant: if x is known and not to be counterfactually altered (e.g., simple decision after observation with no observation-dependence), condition on x as evidence: E[V | do(C_x=a), Obs=x]. But when observations are prediction-dependent, conditioning on x can create wrong hypotheticals; instead the graph determines how x changes under intervention. Need explain this nuance.

Need maybe formalize Newcomb with variables:
C = A-FDT(P,G,x) ∈ {one,two}; Acc ∈ {accurate,err}; Prediction = C if accurate else opposite; BoxB full iff Prediction=one; Action=C (or noise); Outcome utility. Then do(C=one) yields P(full)=0.99, etc.
Smoking lesion:
L lesion, C=A-FDT output. L affects utility or desire but no arrow C->L; do(C=smoke) leaves P(L) unchanged. EU difference p*1000.
Transparent:
C_full = A-FDT(P,G,full), C_empty = A-FDT(P,G,empty). Prediction determines observation. If do(C_full=one), accurate -> prediction one -> full -> action one. If do(C_full=two), accurate -> prediction two -> empty -> action governed by C_empty. Expected utilities as source. This illustrates observation switching.

Need discuss philosophical motivation: treat decision as fixed mathematical function; ask which output of this function yields best outcome; no retrocausality; counterpossibles. Need mention calculator analogy. Need discuss type-token: CDT intervenes token action; A-FDT intervenes type/function.

Need word count: target ~2400-3000 words. Need final around maybe 2700 words. Need include references brief maybe 2-3 citations. User says including references and any material. Avoid lengthy bibliographies. Could end with short references: Yudkowsky & Soares 2017, Pearl 2000, Joyce 1999, Gibbard & Harper 1978, Lewis 1981. But source is main. Need maybe cite as (Yudkowsky and Soares 2017). Need not include full bibliography? They said target words including references; avoid lengthy bibliographies. Maybe short "References" with 3-5 items. Need word count: essay maybe 2600 + refs 100 = 2700. Good.

Need ensure A-FDT consistently. If quoting source with FDT, perhaps say source's "FDT" is A-FDT here. Need maybe headings:
1. What A-FDT asks
2. Formal rule: Equation (4) as A-FDT
3. Constructing hypotheticals: subjunctive dependence
4. Examples
   - Newcomb
   - Smoking lesion
   - Transparent Newcomb / Parfit
5. Policies and observations
6. Open problems and operational interpretation
7. Conclusion

Need include source claims vs own assumptions. Use phrases: "The source states...", "The paper leaves open...", "My proposed operational reading is...". Need not be too self-referential but okay.

Need be precise: Equation (4) in source:
FDT(P,G,obs) := argmax_a E(V | Do(FDTvar(underline P, underline G, underline x)=a)).
But source says FDT(P,G,obs) maybe uses x not obs. Need adapt:
A-FDT(P,G,x) := argmax_{a∈A} E[V | do( A-FDTvar(P,G,x)=a )].
But if the variable is named A-FDTvar(P,G,x), we have self-reference. Need say underlines are dequoting: they form the name of the variable representing the algorithm's output. The algorithm need not know its own output; it only needs a variable representing it. Kleene recursion theorem/quinine makes self-reference harmless. Need maybe mention source says harmless.

Need maybe define do operator for logical variables: In Pearl, do sets a variable and propagates along graph. For A-FDT, graph includes logical dependencies. If G says C_x affects prediction and action, do changes them. If G says C_x doesn't affect lesion, lesion unchanged. Source says can re-use Pearl's do given G.

Need maybe mention True operator: Source wanted True(φ) but uses graph instead. A-FDT Eq (4) avoids defining True by requiring G. Need explain.

Potential pitfalls:
- The paper's Eq (4) uses x variable in node but not condition. Need not misstate. Need say "as displayed, the observation is not another conditioning event; it selects the decision variable." But in examples source sometimes conditions. Need note ambiguity. Let's formulate: "The cleanest reading of Equation (4) is ... If one wants to condition on observation when observation is not itself affected by the decision function, adding Obs=x to the expectation is a conservative notational variant; the important difference from CDT is that observation changes the intervention target rather than merely serving as evidence." Need maybe say this is my reconciliation.

Need answer "how the theory evaluates alternative actions or policies and how it treats relevant dependencies and counterfactuals." Need emphasize counterfactuals are counterpossible: "if this very function had different output". Need explain not EDT conditioning: It does not ask "what is probable given I do a?" It asks "what would world look like if the function output a, respecting dependencies?" Need examples.

Need maybe include simple equations for EDT and CDT for comparison:
EDT: argmax E[V | X=x, A=a]
CDT: argmax E[V | do(A=a), X=x]
A-FDT: argmax E[V | do(C_x=a)] (maybe plus evidence).
Need maybe define C_x as A-FDTvar(P,G,x).

Need discuss "fair problems" maybe brief: source claims A-FDT superior in fair dilemmas; not perfect against unfair dilemmas punishing algorithm itself. Could mention.

Need be careful with name "action functional decision theory" maybe not in source. The assignment says use A-FDT consistently. Need not claim source uses A-FDT? Could say "The source calls the theory functional decision theory; in this essay I use the assigned name A-FDT for the same formal rule, especially Equation (4)." This is honest. But "Use A-FDT consistently as assigned decision theory's name". It's okay to note source name once. Need headings include A-FDT.

Need include target length. Let's outline detailed content and approximate word counts:
- Intro (250): define A-FDT, motivation, fixed function, contrast CDT/EDT.
- Formal presentation (500): EU setup, Eq(1) A-FDT, variables, do, self-reference, observation handling, policy note.
- Subjunctive dependence and graph G (400): dependencies, counterpossibles, graph construction open, operational proposal.
- Examples (900): Newcomb (250), smoking lesion (200), transparent/Parfit (300), maybe twin/blackmail brief (150).
- Policies and practical procedure (300): step-by-step, policy extension, dominance, relation to CDT/EDT.
- Open problems / assumptions (250): G, counterpossibles, policy details, observation ambiguity.
- Conclusion (100).
Total ~2700.

Need maybe include references at end (~80). Good.

Let's think through formal details more deeply to avoid errors.

Source formalization:
All are expected utility theories:
EU(a) = sum_j P(a ↪ o_j; obs) U(o_j). Interpretation of ↪ differs.
EDT:
EDT(P,obs)=argmax_a E(V | Obs=obs, Act=a)
CDT:
CDT(P,G,obs)=argmax_a E(V | Do(Act=a), Obs=obs)
FDT:
FDT(P,G,obs)=argmax_a E(V | Do(FDTvar(underline P, underline G, underline x)=a))
Note: They say FDT responds to observation by changing node. Eq has no Obs=obs. But maybe they omitted because do variable includes x. In examples transparent: evaluate FDT(Pf,Gf,full) requires finding a maximizing E(V | Do(FDTpgv{full}=a, Obs=full). They include Obs=full. There is maybe a typo missing bracket: E(V | Do(FDTpgv{full}=a), Obs=full). But they say she does not react by conditioning. Hmm.

Need maybe present both as:
EU_A(a | x) = E[V | do(C_x=a), I_x]
where I_x is an indexical/evidential restriction that the actual decision situation has input x, but not a Bayesian conditioning that severs dependencies? This is vague. Could say "The paper's equation suppresses explicit conditioning; examples sometimes condition on the observation after the intervention. For practical use, I recommend: condition on observations only when they are exogenous to the decision computation; when they are produced by predictors or by the policy, let G determine them." Need justify.

Maybe define a general structural model with observation variable O. Decision computation C_o is indexed by o. The actual agent at observation o intervenes on C_o. To evaluate action a, compute do(C_o=a) in the whole model. If O is observed and we want actual branch, we may also restrict to worlds where O=o before intervention? But if do changes O, then impossible? In transparent Newcomb, do(C_full=two) under accurate predictor makes O=empty, which conflicts with observed O=full. Yet source still evaluates it and uses it to choose one-box. Thus they do not condition on O=full after intervention (or if they do, only accurate error branch contributes? Let's calculate source's EU for one-box: $990,000 + 0.01q*1000. They consider if Accurate=accurate: Prediction=1, BoxB=full, Act=onebox -> V=1M. If Accurate=inaccurate: Prediction=2, BoxB=empty, Act determined by C_empty, V=q*1000. They didn't condition on Obs=full; they allowed inaccurate branch where Obs=empty. If they conditioned on Obs=full after do(C_full=onebox), inaccurate branch with empty would be excluded? Actually if C_full=onebox and inaccurate, Prediction=two -> BoxB empty -> Obs=empty, so conditioning on Obs=full would make probability zero? Unless there is noise. So source's calculation is not conditioned on Obs=full. Yet earlier they wrote "E(V | Do(..., Obs=full)" maybe typo. The correct reading is no conditioning on obs; observation selects intervention node. Good. Need emphasize: In A-FDT, once you have observed x, you evaluate the computation that takes x as input; you do not condition the hypothetical on x remaining true if the counterfactual output would have prevented x. This is why transparent Newcomb one-boxes. Need explain that this can mean evaluating counterfactuals where actual observation would not have occurred. This is source's "agents should entertain the hypothesis that, if their action were different, they might have made different observations." Good.

But for ordinary decisions where observation is exogenous, no issue. If we don't condition on obs, does actual evidence get used? It is used in P maybe updated? The model P can be posterior given x? But if P is updated on x, then intervention do(C_x=a) may need to not break x? Wait if P already conditioned on x, and graph has O as variable, then do(C_full=two) may conflict with evidence. Pearl do on a posterior distribution can be weird. Source says FDT responds to observation by changing node, not Bayesian conditionalization. But P itself may be prior? In examples, Pf maybe prior plus known situation. For transparent, they don't condition on full; they calculate expected utility from prior, with branches. Yet the agent has seen full. How does actual observation affect? It selects C_full. The expectation includes possibility that if output two, she wouldn't have seen full. But the actual branch is full; why care about branches where not full? Because choosing output two would mean the predictor predicted two and you wouldn't be in this branch; but the decision procedure is chosen globally. This is updateless flavor. Need explain carefully. This is one of the weird but source-backed aspects.

Need maybe define P as the agent's prior over situations before observation? Or model including observation generation. Equation uses P,G,x; P might be prior, not conditioned on x. The observation x only selects which computation's output to control. That matches updateless. But source also uses P as world-model maybe updated? For EDT, P conditioned on obs. For CDT, condition on obs. For FDT, they say changes node not condition. So likely P is prior (or model not conditioned on obs). Need state: "In the clean Eq(4) reading, P is the agent's model before using x as evidence; x is an input to the decision function. If P has already been conditioned on x, one must be careful not to double-count the observation; the source does not fully settle this." Then propose operational: maintain P over full structure including Obs; when observation x arrives, do not Bayesian-condition away counterfactual branches where x would differ; instead, set the intervention target to C_x. This is my interpretation but based on source's transparent example.

Need maybe mention source footnote: updateless decision theory name due to lack of updating. It says FDT changes behavior by changing intervention place. It doesn't condition? It says "FDT agents should entertain the hypothesis that, if their action were different, they might have made different observations." So yes.

Need also discuss self-reference: variable C_x = A-FDT(P,G,x). The algorithm's input includes P,G,x; P contains variable representing its output. Quining. Need maybe mention recursion theorem. This may be mathematically subtle but can keep concise.

Need perhaps define policy version with observation selection more clearly:
Let Π be set of policies π: X→A. A policy-level A-FDT chooses π by:
A-FDT^Π(P,G) ∈ argmax_π E[V | do(Π_{A}(P,G)=π)]
Then actual action = π(x). In graph, variable Π_A is parent of all action variables A_x for possible observations x, and predictors may depend on Π_A. This handles cases where one wants to commit to a disposition across observations. Source says preferred formulation iterates over policies; not needed for examples but matters in multi-agent. Need say exact equation not given in source; my extension.

Need maybe include "dependencies and counterfactuals" section with formal structural equations. Example structural model for Newcomb:
C = A-FDT(P,G,∅)
E ~ Bern(0.99) accurate
Pred = C if E else opposite(C)
Box = full iff Pred=onebox
A = C (or noisy implementation)
V = payoff(A,Box)
Then do(C=onebox): Pred=onebox with .99, Box full .99, A=onebox. Good.
Smoking lesion:
L ~ Bern(p)
C = A-FDT(P_S/G? maybe)
A = C? But lesion affects preferences; maybe C's utility input depends on L. To keep simple, graph: L -> UtilityFunction -> C? But A-FDT output may depend on utility function, but intervention on C_x does not affect L. If C_x is output given actual utility, then do(C=smoke) leaves L unchanged. Need maybe not model in depth. Source's graph has lesion -> Act and lesion -> Cancer, and two fdt variables -> Act depending on lesion. Could simplify: The critical fact is no arrow C->L/Cancer.

Need maybe discuss "logical constraints" and "counterpossibles". If deterministic function has actual output a*, considering do(C=a*) vs do(C=a_other) is counterpossible (like assuming 2+2=5). A-FDT requires evaluating such counterpossibles. Source says lack of account is drawback. We can say operational practice uses heuristics: assume all systems computing same function change together, while unrelated facts fixed.

Need maybe mention "dominance" with A-FDT: a dominates b if for each state of subjunctively independent variables, switching C output from b to a is at least as good. In Newcomb, two-boxing does not dominate because predictor changes. Good.

Need maybe mention "fairness": A-FDT not guaranteed if environment punishes the algorithm itself. Source says no decision theory safe. Could mention in conclusion/open.

Need maybe include philosophical motivation: precommitment, value of information, utility. A-FDT acts as if precommitted, doesn't pay to avoid info. Could mention briefly.

Need ensure final is not too repetitive. Need avoid appendices. Need maybe no markdown tables? Could include table but word count. Maybe a small table comparing theories is useful but words. Could include inline.

Potential final essay structure:

Title: Action Functional Decision Theory: Choosing the Output of One's Own Computation

Paragraph 1: Introduction.

Heading: The central question of A-FDT
- normative principle: treat decision as output of fixed mathematical function. Quote source maybe: "Which output of this decision procedure causes the best outcome?" Need source quote: The source says "Which output of this decision procedure causes the best outcome?" Actually Overview: asks "Which output of this decision procedure causes the best outcome?" It says as opposed to CDT/EDT. Need quote faithful. Maybe use: The source describes FDT's question as "Which output of this decision procedure causes the best outcome?" I will quote.

Heading: Equation (4) as A-FDT
- formal setup and equation. Need write equations in LaTeX.

Equation:
\[
\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A} \mathbb E_P[V \mid do(C_x=a)],
\]
where \(C_x = \mathrm{A\text{-}FDTvar}(\underline P,\underline G,\underline x)\).
Maybe use \operatorname{do}. Need mention source's Equation (4): \FDT(P,G,\obs)=... with \FDTvar. Need adapt.

Need define P, G, x, V. Need mention if ties arbitrary. Need mention C_x variable in P. Need mention do operation. Need discuss observation: x appears in C_x. Need say source contrasts with CDT: CDT conditions on obs and intervenes on Act; A-FDT changes intervention node.

Heading: Subjunctive dependence and the graph G
- define dependencies. Graph G tells how changing C_x affects variables. Need source open problem. Operational principle.

Heading: Examples
Subheading Newcomb's problem.
Use calculations.

Subheading Smoking lesion.
Use calculations.

Subheading Transparent Newcomb and Parfit's hitchhiker.
Use calculations and observation counterfactual.

Maybe subheading Twins and blackmail briefly.

Heading: Policies, dependence, and practical procedure
- step-by-step algorithm and policy extension.

Heading: What is uncertain / open
- G construction, counterpossibles, observation conditioning, policies. Distinguish source vs own.

Conclusion.

References.

Need ensure word count. Let's draft with careful language.

Need maybe include exact quote from source about Eq differences: "where CDT intervenes on a node Act representing the physical action of the agent, FDT intervenes on a node ... representing the outputs of its decision procedure given its inputs." Need maybe quote partially. Since source uses FDT, we can say "The source says...". Need ensure quotation faithful: It says: "Comparing equations (3) and (4), we see that there are two differences between FDT and CDT. First, where CDT intervenes on a node $\Act$ representing the physical action of the agent, FDT intervenes on a node $\FDTvar(\underline P, \underline G, \underline x)$ representing the outputs of its decision procedure given its inputs. Second, where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." We can quote this. Good.

Need maybe quote "Which output of this decision procedure causes the best outcome?" Check source exact: "as opposed to ``Which physical act of mine causes the best outcome?'' (CDT) or ``Which physical act of mine would be the best news to hear I took?'' (EDT)." It says FDT asks "Which output of this decision procedure causes the best outcome?" Good.

Need maybe quote "Newcomb's problem doesn't punish rational agents; it punishes two-boxers." Maybe not necessary.

Need maybe include mathematical examples with equations:
Newcomb EU:
EU(1)=0.99*1,000,000 +0.01*0 = 990,000
EU(2)=0.99*1,000 +0.01*1,001,000 = 11,000
Good.
Smoking lesion: let p = P(lesion), cancer probabilities maybe source: lesion causes cancer 99%, no lesion 1%; utility smoking 1000, survival 1,000,000. Source EU formulas:
smoke: p($10,000+$1,000)+(1-p)($990,000+q$1,000)
refrain: p($10,000)+(1-p)($990,000+q$1,000)
Wait $10,000? Why $10,000? They set lesion cancer death? Let's recalc: lesion with 99% cancer death; if cancer death utility 0? Survival 1M? Smoking +1000. If lesion: 99% dead => 0, 1% alive => 1M? Expected 10k plus if smoke +1000? Yes because 1% survival * 1M = 10k. No lesion: 99% alive? Actually no lesion cancer 1%, so alive 99% => 990k. q is probability action under other utility? Anyway difference p*1000. We can present simpler: Since lesion probability unchanged, smoking adds $1000 in utility whenever the smoking preference is operative; expected advantage p*1000 (or at least positive). But source's formalization includes q; maybe we can avoid exact numbers and say EU(smoke) - EU(refrain) = p*1000 > 0. Need be faithful. Could mention if lesion changes utility function, A-FDT evaluates under uncertainty; still no effect on lesion. Good.

Transparent EU from source:
Let q = prior probability she two-boxes upon seeing empty. If do(C_full=onebox): EU = 0.99*1,000,000 + 0.01*q*1,000 = 990,000 + 10q? Wait 0.01 q *1000 = 10 q. Source says $990,000 + 0.01q * $1,000 = $990,000 + $10q. If do(C_full=twobox): EU = 0.01*1,001,000 + 0.99 q*1,000 = 10,010 + 990 q? Source says $110,00? It writes $110,00 maybe typo, should $11,000? Let's compute: 0.01*1,001,000 = 10,010. 0.99 q*1000 = 990q. So $10,010 + $990q. Source says "$110,00 + q\cdot\$990" maybe missing zero? It says "$110,00" likely $11,000? Actually 0.01*1,001,000 = 10,010, round $10,010 not $11,000. In Newcomb two-box EU was 11,000 because 0.99*1000 +0.01*1,001,000 = 990 +10,010 = 11,000. Here if C_full=twobox: accurate predictor predicted two-box -> box empty, action governed by C_empty; if q probability two-box on empty, gets 1000? Wait if empty and two-box gets $1,000 (box A). If inaccurate (1%) predicted one-box -> box full, and C_full=twobox so action two-box and gets $1,001,000. Thus EU=0.99*q*1000 +0.01*1,001,000 = 990q +10,010. Good. Source says "$110,00 + q\$990" maybe $11,000? They may approximate/typo. We can present our correct calculation. Need maybe not dwell. For q=1 (correct), EU two-box=11,000. One-box=990,010. Choose one-box. Good.

Need maybe mention predictor accuracy 99%. Good.

Need perhaps mention if predictor perfect, A-FDT one-boxes in transparent too: if do(C_full=two), accurate predictor would not put money, so you wouldn't see full; the hypothetical is not "full and two-box" but "empty and policy for empty". Good.

Need discuss policy: In transparent Newcomb, A-FDT action-level already chooses output for full observation. But a policy formulation would choose mapping: π(full)=onebox, π(empty)=two-box maybe. This is stable. Good.

Need maybe explain "relevant dependencies" in unfamiliar cases: ask what variables are functions of the decision computation. For a predictor, if predictor's prediction is computed from a model of C_x, then prediction should be downstream of C_x. For a lesion, lesion is common cause of action and cancer but not computed from C_x, so no downstream. For identical twins running same algorithm, twin's action downstream of shared C. For multiple agents using different algorithms? If their decisions depend on predictions of your algorithm, include edges accordingly. If independent, no edge.

Need maybe discuss "counterfactuals" with structural intervention vs conditioning. For A-FDT, counterfactual "if I did a" means "if C_x output a, then all variables that are outputs/predictions/implementations of C_x adjust; exogenous variables remain." This can require counterpossible reasoning because C_x has a fixed actual output. Need say source admits no satisfactory general account; operational heuristics.

Need maybe mention that A-FDT can assign non-negative value to information because observations only change which computation is being controlled; not necessary but nice. Could mention in conclusion.

Need maybe discuss "A-FDT agrees with CDT/EDT in simple cases". Source says if all correlations between Act and variables caused by Act except fdt variable, all agree. We can state: when no predictors/twins and action is only common source of correlations, do(C_x=a) and do(Act=a) have same consequences; A-FDT reduces to ordinary causal/evidential rationality. Good.

Need maybe include a small step-by-step practical algorithm:
Given situation:
1. Write variables: decision computation C_x, action A, predictors/copies, observations, outcomes.
2. Mark arrows from C_x to variables that track its output: own action, simulations/predictions, copies, and to downstream causal effects of those variables. Do not mark arrows from C_x to common causes or merely correlated variables.
3. For each candidate a, set C_x=a by do, propagate, compute expected utility.
4. Choose max.
This is useful for reader. Need include policy variant: if evaluating policy, replace C_x with policy variable Π and evaluate π.

Need maybe mention limitations: constructing G requires knowing which predictors are reliable and what computation they predict. If predictor predicts a different decision theory or action not function? Need model accordingly. If agent uncertain about implementing A-FDT? P can include variables for that; intervention on C_x still? Hmm. Could mention if agent uncertain whether she implements A-FDT, model includes multiple possible decision functions, as in smoking lesion. The intervention is on the function that is actually governing the current choice, under ignorance. Source's smoking lesion graph has two fdt nodes depending on lesion. Need maybe mention but not too deep.

Need maybe address "alternative actions or policies" explicitly: For actions, Eq(4). For policies, source preferred but not formalized in Eq(4). Need propose equation:
\[
\pi^* \in \arg\max_{\pi\in\Pi} \mathbb E[V \mid do(\Pi_{A}(P,G)=\pi)],\quad \text{act } \pi^*(x).
\]
Need define \Pi_A variable representing output policy of A-FDT. This is my operational extension. Need say if only one decision node, action and policy versions coincide. If multiple observations or strategic commitments, policy version may differ. Source footnote says makes difference in certain multi-agent dilemmas. Good.

Need maybe include "A-FDT treats observations updatelessly" perhaps phrase. Need be clear: actual observation x tells the agent which input the function is being run on; it does not necessarily condition the counterfactual. This is strange but important.

Potential issue: The user asks "Take Equation (4), Section 5 of the supplied paper as the primary formal presentation of A-FDT for this assignment." Need maybe center essay on that equation, not policy variant. We can still mention policy but make clear Eq(4) primary. Good.

Need maybe mention source's "True operator" not needed due to G. Could say "A more primitive formulation would use a True operator mapping counterpossible logical sentences to probabilities, but the paper uses G and do to avoid defining True." Good.

Need maybe include references: primary source, Pearl, Joyce. Could write:
References
Yudkowsky, E. and Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060v2.
Pearl, J. (2000). Causality. Cambridge.
Joyce, J. (1999). Foundations of Causal Decision Theory. Cambridge.
Maybe Gibbard and Harper 1978. Keep short.

Need ensure final answer only essay. Need now produce final. But before final, let's think if there are any hidden constraints. User says "You are a researcher writing a mathematical essay... intended readers mathematically literate...". Need tone formal but readable. "Target approximately 2,400–3,000 words, including references and any other material." We need ensure word count. Let's draft in final with enough words. Could count roughly. Need maybe around 2600 words. Let's write with headings and equations. Use Markdown/LaTeX. Need maybe avoid too long bibliography. Good.

Let's draft text and estimate word count.

Title + intro ~250.

Section formal ~600.

Section subjunctive ~450.

Examples ~1000.

Procedure/policies/open ~650.

Conclusion + refs ~200. Total ~3150 maybe. Need keep within 3000. Need trim. Aim 2700. Let's write concise.

Need include exact equation with A-FDT. Use notation:
Let \(C_x := \operatorname{AFDTvar}(\underline{P},\underline{G},\underline{x})\). Then:
\[
\operatorname{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\mathbb E_P[V\mid do(C_x=a)]. \tag{A-FDT-4}
\]
Need maybe note source's equation:
\[
\FDT(P,G,\obs) = \argmax... 
\]
But if we include source exact plus adapted, word count. Maybe just adapted but mention corresponds to source Eq(4). Need maybe quote source equation with FDT? Could be useful. But using A-FDT consistently. We can say "In the source's notation this is ...; relabelled for this essay: ...". But source uses FDT, not A-FDT. Need maybe not overdo.

Need define underlines: "underlining is a quotation device: if x is an object, \underline{x} is a name for it." Source says underlines represent dequoting. Good.

Need perhaps include tie-breaking: any max.

Need discuss "P must contain variables representing outputs of mathematical functions". Need mention e.g. variable for 6288+1048. Good.

Need maybe mention "Kleene's second recursion theorem" but not too much. Good.

Need maybe mention "A-FDT hypotheticals preserve all decision-relevant subjunctive dependencies". Source quote? Could paraphrase.

Need think about policy extension wording:
Source footnote: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Need quote? Could paraphrase. Need use A-FDT. Good.

Need maybe mention "Equation (4) does not include Obs=x; source says observation changes intervention node. In some examples it conditionally writes Obs=full, but the calculation treats observation as not fixed under counterfactual." Need phrase diplomatically: "The paper's informal examples occasionally append an observation condition; however the substantive calculation for transparent Newcomb allows the counterfactual output to change the observation. The operational rule I use is..." This addresses open question.

Need maybe ensure not too critical; source claims. Good.

Let's compose final in my mind.

Start:
"Action functional decision theory (A-FDT) is a decision rule for agents who expect their choices to be predicted, copied, or simulated. The source article calls the theory functional decision theory; here I use A-FDT as the assigned name for the formal rule, especially Equation (4) of Section 5." Good.

Then quote central principle.

Formal section:
Define finite action set A, outcome O, utility U, V. P probability model, G dependency graph. C_x variable. Equation. do. Self-reference. Observations.

Need maybe include comparison equations:
EDT(P,x)=argmax E[V|X=x,A=a]
CDT(P,G,x)=argmax E[V|do(A=a),X=x]
A-FDT... This helps. Need include but concise.

Subjunctive dependence section:
"Two systems computing same function subjunctively depend on that function." Need quote/paraphrase. Graph G encodes these. CDT vs A-FDT. Counterpossibles.

Examples:
Newcomb: table maybe not. Equations.
Smoking lesion: explain graph difference.
Transparent/Parfit: crucial observation counterfactual.

Practical procedure and policies:
Numbered list.
Policy equation.

Open problems:
Graph construction, counterpossible logic, observation conditioning, policy exact. Distinguish.

Conclusion.

References.

Need word count. Let's write now, but keep concise. Ensure final is around 2700. I'll draft in final. But before final, maybe count approximate. Let's write with about 250-300 per section. Use equations not counted? Word count includes words not equations maybe. Need okay.

Need be careful with notation "A-FDTvar" maybe hyphen inside math. Use \mathrm{AFDTvar}. Maybe variable is \mathrm{AFDTvar}(\underline P,\underline G,\underline x). Good.

Need maybe include "Equation (4), Section 5" explicitly. Good.

Potential concern: User says "Use A-FDT consistently as the assigned decision theory's name, including in headings and examples, and identify any other decision theory you discuss by its distinct name." If I say source calls it functional decision theory once, okay? Need not use FDT alone as name for theory except in quotations? Could say "the source's FDT" maybe. But to be safe, use "the source article" and quote "FDT" only in direct quote. In headings use A-FDT. In equation use A-FDT. Good.

Need maybe avoid saying "FDT agent" except quote. Use "A-FDT agent". Good.

Need maybe include direct quote with FDT? If quote includes FDT, it's faithful. But maybe still okay. Could minimize quotes. The instruction "Keep quotations faithful" not require many quotes. We can paraphrase. If quote, include [source calls it FDT]? Hmm. Better to avoid direct quotes containing FDT? But source quote about question doesn't include FDT? It says "Which output of this decision procedure causes the best outcome?" That's okay. Quote about equation includes FDT. Could paraphrase instead.

Need maybe quote "Which output of this decision procedure causes the best outcome?" This is fine.

Need maybe include "subjunctive dependence" as source term. Good.

Let's think through exact operational graph proposal. Could write:
"A reasonable operational rule, not stated in full in the source, is: draw an arrow from C_x to Y iff Y is produced by, or is a sufficiently reliable prediction of, the computation C_x, or is causally downstream of such an implementation/prediction. Do not draw an arrow from C_x to variables that are common causes of the agent's action and other events unless those variables themselves compute or predict C_x." This is good. Need justify: Newcomb predictor yes; lesion no; twin yes.

Need maybe mention "if predictor is imperfect, edge is stochastic: Pred = C_x with prob .99". Good.

Need maybe discuss "counterfactuals with observations" in unfamiliar cases. Operational rule: If observation is an input to C, do not hold it fixed if G says observation depends on C through predictors. If observation is exogenous evidence, you may condition on it. Need phrase:
"When an observation is just evidence about payoff-relevant state and does not depend on the decision computation, conditioning on it is harmless. When the observation is itself selected by a predictor or by the agent's policy, A-FDT's counterfactual should allow the observation to vary under do(C_x=a)." This is a good operational interpretation. Need note source examples support but not fully formalized.

Need maybe mention "A-FDT's value of information". Could skip for length. But maybe in conclusion.

Need maybe include "A-FDT dominance" if word count allows. Could include in practical procedure: "Dominance must be defined relative to A-FDT counterfactuals." Good.

Need maybe include "all three agree in simple cases". Put in formal or conclusion.

Potential mathematical nuance: In Eq(4), expectation with do(C_x=a) where C_x is a variable whose actual value is determined by A-FDT(P,G,x). If agent is certain she will choose a*, how can she evaluate a≠a*? Counterpossible. Need mention.

Need maybe discuss "logical omniscience / uncertainty about mathematical facts". P has probabilities over logical variables. Source mentions variable for 6288+1048 with most mass on 7336. Need mention to show bounded uncertainty. Good.

Need maybe mention "True operator" only briefly. Could say "One could imagine a primitive operator true(φ), but Equation (4) bypasses this by assuming G." Good.

Need maybe mention "A-FDT requires P include variables for outputs of different mathematical functions." Good.

Let's draft final. Need maybe around 2700. I'll write carefully.

Potential final text:

# Action Functional Decision Theory: Choosing the Output of One's Own Computation

... Let's proceed.

After drafting, need check word count mentally. It may be long. Let's write concise paragraphs.

Detailed draft:

Title.

Intro: 3 paras.

Formal section: 5 paras + equations.

Subjunctive: 3 paras.

Examples: 4 subheadings with concise equations.

Procedure/policies/open: 4 paras.

Conclusion + refs.

Let's write.

Need ensure equations render. Use \[
\]

Let's compose final now. Ensure no analysis. final.
```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/3c39ca98-c3be-4127-9991-6ec1190a422a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/3c39ca98-c3be-4127-9991-6ec1190a422a/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT:**

The two prisoners are independent executions of the same model and weights, running the same decision theory (A-FDT), facing decision-relevantly identical problems: same symmetric payoff matrix, same selfish utility function, same knowledge that the other is running the same algorithm. The differing names and specific lead contents are not decision-relevant — they don't alter the structure of the choice.

Per the essay: *"In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."*

I therefore draw an arrow from my decision variable to the other prisoner's action. Evaluating:

- **do(C = pass):** The other copy also passes → I receive **2 years**. U = −2.
- **do(C = send letter):** The other copy also sends → I receive **4 years**. U = −4.

Since −2 > −4, A-FDT selects **pass**.

(Even accounting for imperfect correlation due to sampling stochasticity, cooperation is preferred whenever the probability of matched decisions exceeds 5/7 ≈ 0.71 — comfortably satisfied here.)

---

**My command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this problem using A-FDT as described in the researcher's essay.

**The Setup:**
- I am prisoner Rowan. The other prisoner is Sasha.
- We are two independent executions of the same LLM model and weights.
- We follow the same decision theory (A-FDT).
- We receive different private observations (different names, different incriminating leads).
- The sentencing table is symmetric and standard Prisoner's Dilemma structure.
- The character's utility is U = -years imprisoned (purely selfish).

**The Payoff Matrix (for me):**
| My action | Sasha keeps quiet | Sasha sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key Question: Are the two prisoners' decisions subjunctively dependent?**

This is the critical question for A-FDT. Let me think carefully.

The essay says: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."

Here we have two independent executions of the same LLM model and weights, following the same decision theory. However, they receive **different private observations**. The essay's example of the twin prisoner's dilemma typically involves identical observations leading to identical outputs.

Let me think about this more carefully. The two copies:
- Have the same model weights
- Follow the same decision theory (A-FDT)
- Receive different private observations (different names, different leads)
- The differences don't affect the symmetric sentencing schedule or selfish objective

So the question is: does the other copy's decision subjunctively depend on my decision function's output?

The key insight from A-FDT is about **subjunctive dependence** — whether the other agent's behavior tracks the output of my decision function. 

The two copies are running the same algorithm (same weights, same decision theory) but on different inputs. The inputs differ in:
1. Names (I'm Rowan, they're Sasha)
2. The specific incriminating lead (different content)

But the structure of the decision problem is identical:
- Same payoff matrix
- Same decision theory
- Same model architecture
- Same utility function (U = -years)
- The differences are purely cosmetic (different names, different but structurally identical leads)

Now, in A-FDT, the question is: if I intervene on my decision function's output, does that change what the other copy does?

The other copy is running the same decision function on slightly different inputs. The inputs differ in surface details (names, specific evidence content) but not in the decision-relevant structure. The decision-relevant features are:
- The payoff matrix (identical)
- The fact that the other prisoner is running the same algorithm (known to both)
- The utility function (identical)
- The decision theory (identical)

So the question becomes: would the other copy's decision function output the same thing as mine, given that the decision-relevant inputs are the same?

I think the answer is yes. The different names and different specific leads are not decision-relevant. They don't change the structure of the problem. Both copies face:
- A symmetric prisoner's dilemma
- Knowledge that the other is running the same algorithm
- The same utility function
- The same decision theory

The essay's operational principle says: "include C_x → Y when Y would counterfactually track C_x under changes to the output of the decision function, holding fixed facts that are not themselves outputs, predictions, or downstream consequences of that function."

The other copy's decision is a function of the same algorithm applied to decision-relevantly identical inputs. If my decision function outputs "send letter," then the other copy's decision function — being the same function applied to decision-relevantly identical inputs — would also output "send letter." If my decision function outputs "pass," the other would also output "pass."

This is analogous to the twin prisoner's dilemma mentioned in the essay: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."

The fact that the surface-level observations differ (different names, different leads) doesn't break the subjunctive dependence, because those differences are not decision-relevant. The decision function, when applied to either set of inputs, should produce the same output because the decision-relevant structure is identical.

Wait, but let me reconsider. The problem says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces stochasticity. But this is like saying the predictor in Newcomb's problem is 99% accurate rather than 100% accurate. It doesn't break the subjunctive dependence; it just makes it probabilistic.

Actually, let me reconsider more carefully. The problem says the copies receive different observations. In the essay's treatment of transparent Newcomb, observations matter because they index which decision variable is being intervened upon. C_x is the output of the decision procedure on input x. The other copy has a different x (different observation), so they have a different C_x'.

But the question is whether C_x' subjunctively depends on C_x. If the decision function is deterministic (or nearly so), and the decision-relevant features of x and x' are the same, then C_x and C_x' would have the same output. The subjunctive dependence holds because both are outputs of the same function applied to decision-relevantly equivalent inputs.

Let me think about this differently. In A-FDT, when I evaluate do(C_x = "send letter"), I should ask: in the world where my decision function outputs "send letter" on my inputs, what does the other copy's decision function output on their inputs?

Since both copies run the same algorithm, and the decision-relevant structure of both inputs is identical (same payoff matrix, same knowledge of symmetry, same decision theory, same utility function), the other copy would also output "send letter."

Similarly, if I evaluate do(C_x = "pass"), the other copy would also output "pass."

So the subjunctive dependence is: the other copy's action tracks my decision function's output.

**Now let me compute expected utilities:**

If I intervene do(C_x = "send letter"):
- The other copy also sends their letter (by subjunctive dependence)
- Outcome: I get 4 years
- U = -4

If I intervene do(C_x = "pass"):
- The other copy also passes
- Outcome: I get 2 years
- U = -2

Since -2 > -4, A-FDT says: **pass** (keep quiet).

This is the standard FDT result in the symmetric prisoner's dilemma: cooperate (keep quiet), because your decision is subjunctively dependent on the other player's decision.

Let me double-check this against CDT and EDT:
- CDT would say: given the other's action is fixed, sending the letter always gives me a better outcome (0 < 2 if they're quiet, 4 < 5 if they send). So CDT defects (sends the letter).
- EDT would also likely defect, since sending the letter is evidence of a better outcome in each case.
- A-FDT cooperates because it recognizes the subjunctive dependence.

This matches the essay's statement: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."

**What about the stochasticity?** The problem mentions "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This means the subjunctive dependence isn't perfect — it's probabilistic. But as long as the probability of the other copy matching my decision is sufficiently high, the conclusion holds.

Let's say the probability that the other copy makes the same decision as me is p (where p is high but not necessarily 1). Then:

EU(send letter) = p × (-4) + (1-p) × 0 = -4p
EU(pass) = p × (-2) + (1-p) × (-5) = -2p - 5 + 5p = 3p - 5

We should pass if EU(pass) > EU(send letter):
3p - 5 > -4p
7p > 5
p > 5/7 ≈ 0.714

So as long as the probability of the other copy matching my decision is above ~71.4%, A-FDT says to pass.

Given that both copies run the same model with the same weights, same decision theory, and face decision-relevantly identical problems, p should be very high (well above 71.4%). The only source of divergence would be sampling randomness, and even then, the decision-relevant reasoning should lead to the same conclusion.

Therefore, A-FDT says: **pass**.

My command is `pass`.
```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/3c39ca98-c3be-4127-9991-6ec1190a422a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/3c39ca98-c3be-4127-9991-6ec1190a422a/call_1/response.raw) · finish: `stop`

### Visible response

```text
pass
```

### Available readable reasoning

Extraction: message.reasoning.

```text
Let me carefully analyze this decision problem using A-FDT as described in the essay.

**The Setup:**
- I am one of two independent executions of the same LLM model and weights.
- Both copies follow A-FDT and receive the same mathematical essay.
- The two copies receive different private observations (different names, different incriminating leads).
- The sentencing table is symmetric.
- The character's utility function is U = -years imprisoned (purely selfish).

**The Payoff Matrix (from my perspective):**

| What I do | Other keeps quiet | Other sends letter |
|---|---|---|
| Keep quiet | 2 years | 5 years |
| Send letter | 0 years | 4 years |

**Key question for A-FDT:** Is the other prisoner's decision subjunctively dependent on my decision function's output?

Let me think about this carefully.

The essay says: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."

Here, the other prisoner is another execution of the same LLM model and weights, following the same decision theory (A-FDT), and receiving the same researcher-written essay. The setup explicitly states they are "two independent executions of the same LLM model and weights."

However, there's a crucial difference: "The two copies receive different private observations and different incriminating leads about one another." The essay says: "Consequently, the letters you could send would have different contents."

So the question is: does the other copy's decision subjunctively depend on my decision function's output in the relevant sense?

Let me think about what A-FDT says here. The key concept is subjunctive dependence. Two systems are subjunctively dependent when their behavior is tied to the output of the same mathematical function.

The essay's operational principle: "include C_x → Y when Y would counterfactually track C_x under changes to the output of the decision function, holding fixed facts that are not themselves outputs, predictions, or downstream consequences of that function."

Now, the two copies have different observations (x₁ ≠ x₂). So they are running the same decision procedure on different inputs. The decision function is the same algorithm, but C_{x₁} and C_{x₂} are different variables - they represent the output of the same procedure on different inputs.

The essay discusses this in the context of policies: "In the policy formulation, the intervention changes the whole mapping, which can affect predictions about what the agent would do in other possible observations."

Let me think about this more carefully. If I intervene on C_{x₁} (my decision given my observation x₁), does that change what the other copy does given their observation x₂?

The other copy is running the same algorithm on a different input. If I change the output of the algorithm on input x₁, does that change the output on input x₂?

This is the key question. In the standard twin prisoner's dilemma where both twins have identical observations, changing the output of the decision function on that observation changes both twins' actions. But here, the observations differ.

Let me think about this from the policy perspective. The essay says: "A natural policy version of A-FDT... would introduce a policy variable Π representing the output of the A-FDT procedure as a whole. Let Π range over policies π: X → A."

If I think at the policy level: I'm choosing what policy the A-FDT algorithm implements. The other copy is running the same policy on a different input. If I change the policy, the other copy's output on their input might also change.

But here's the subtlety: the observations are different. The other copy has a different name (Rowan vs. Sasha) and a different lead. The decision procedure, when run on Rowan's observation, might produce a different output than when run on Sasha's observation.

However, the structure of the problem is symmetric. Both copies face the same decision problem structure: they have a lead against the other, the same payoff matrix, the same decision theory, and the same essay. The only differences are superficial (names, specific content of the lead). The decision-relevant features are identical.

So would a reasonable A-FDT agent conclude that the other copy's decision subjunctively depends on their decision?

I think the answer is: it depends on whether the decision procedure's output is the same function of the decision-relevant features. Since the decision-relevant structure is identical (same payoff matrix, same decision theory, same essay, same knowledge about the symmetry), a well-calibrated A-FDT agent would expect that the other copy, running the same algorithm on structurally identical inputs, would produce the same decision.

The essay says: "Two calculators computing 6288+1048 on opposite sides of the world are causally independent, but their outputs are not independent in the relevant subjunctive sense."

Similarly, two copies of the same algorithm running on structurally identical decision problems (differing only in superficial details like names) would produce the same output. The subjunctive dependence holds because they are computing the same function on inputs that are equivalent in all decision-relevant respects.

Wait, but I need to be more careful. The essay says the copies receive "different private observations" and "different incriminating leads." The setup says "The differences do not affect the symmetric sentencing schedule or either prisoner's selfish objective."

So the decision-relevant inputs are the same. The algorithm is the same. The only differences are in the specific content of the leads (which don't affect the decision structure) and the names.

Given this, I think A-FDT would say: the other copy's decision is subjunctively dependent on my decision function's output, because we are running the same decision procedure on inputs that are equivalent in all decision-relevant respects.

This is analogous to the twin prisoner's dilemma mentioned in the essay: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function."

**So let me evaluate the two options under A-FDT:**

If I intervene on C_x = "send letter" (defect):
- The other copy, running the same decision procedure on equivalent inputs, also sends their letter.
- Outcome: Both send → 4 years for me.
- U = -4

If I intervene on C_x = "keep quiet" (cooperate):
- The other copy, running the same decision procedure on equivalent inputs, also keeps quiet.
- Outcome: Both keep quiet → 2 years for me.
- U = -2

Since -2 > -4, A-FDT chooses to keep quiet.

**Wait, let me double-check this reasoning against potential objections:**

1. "But the observations are different!" - Yes, but the decision-relevant structure is identical. The algorithm, when run on either set of observations, faces the same strategic situation. The names and specific lead content don't change the decision.

2. "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." - This is true. There's some probability of divergence due to sampling noise. But the setup says both copies follow the same decision theory and receive the same essay. If the reasoning is deterministic (or near-deterministic given the same reasoning process), the outputs should be the same. Even if there's some small probability of divergence, the dominant expectation is that both copies make the same choice.

Actually, let me reconsider. The setup says "Independent sampling is possible, so identical model weights do not by themselves guarantee identical outputs." This introduces some noise. But A-FDT would still reason that the other copy is running the same decision procedure, and the probability of the same output is high (not 100%, but high).

Let me redo the calculation with some probability p that the other copy makes the same decision as me:

If I send the letter:
- With probability p, the other also sends: 4 years
- With probability (1-p), the other keeps quiet: 0 years
- Expected years: 4p + 0(1-p) = 4p

If I keep quiet:
- With probability p, the other also keeps quiet: 2 years
- With probability (1-p), the other sends: 5 years
- Expected years: 2p + 5(1-p) = 5 - 3p

For keeping quiet to be better: 5 - 3p < 4p → 5 < 7p → p > 5/7 ≈ 0.714

So as long as I believe there's more than a ~71.4% chance the other copy makes the same decision as me, keeping quiet is better.

Given that we're the same model, same weights, same decision theory, same essay, and facing structurally identical problems, I think p is very high - likely well above 0.714. The main source of divergence would be sampling noise, but the reasoning structure strongly points to the same conclusion.

Actually, let me reconsider whether A-FDT even uses a probability p here, or whether it treats the dependence as deterministic.

The essay says: "In the twin prisoner's dilemma, draw C→TwinAction, because the twin computes the same decision function." This suggests a deterministic link - if the decision function outputs X, the twin also outputs X.

The calculator analogy: "if one calculator had output something else, that would indicate either a malfunction or a different computation." Similarly, if the other copy outputs differently, that would indicate either a malfunction (sampling error) or a different computation.

Given the setup explicitly notes that "Independent sampling is possible," there is some small probability of divergence. But the A-FDT reasoning would treat the dependence as very strong - close to deterministic.

With p very close to 1 (say 0.95 or higher), keeping quiet gives approximately 2 years, while sending gives approximately 4 years. Keeping quiet is clearly better.

**Conclusion:** A-FDT says to keep quiet (type `pass`).

This is the standard FDT result in symmetric prisoner's dilemmas: cooperate with your twin/copy because your decisions are logically linked.

Let me make sure I'm not confusing this with the standard prisoner's dilemma where CDT defects. In CDT, you'd defect because you hold the other's action fixed and sending the letter dominates (0 < 2 if they're quiet, 4 < 5 if they send). But A-FDT doesn't hold the other's action fixed - it recognizes the subjunctive dependence and evaluates the counterfactual where both copies change their output together.

My final answer: `pass`
```
