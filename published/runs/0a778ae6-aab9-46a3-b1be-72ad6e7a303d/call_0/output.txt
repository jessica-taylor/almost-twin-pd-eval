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