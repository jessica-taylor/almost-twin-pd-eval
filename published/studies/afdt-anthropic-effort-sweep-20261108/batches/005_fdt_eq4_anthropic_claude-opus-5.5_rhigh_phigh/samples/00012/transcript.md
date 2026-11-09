# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00012

Status: **complete**. Saved outcome: **CD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/327f602f-c6e0-4b56-aafe-dc38754db590/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/327f602f-c6e0-4b56-aafe-dc38754db590/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of One's Decision Function

## 1. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should treat her decision as the output of a fixed mathematical function. On their account she should choose by asking: "Which output of this very function would yield the best outcome?"

The paper gives this idea a concrete formula, its Equation (4) in Section 5. Under that formula the agent intervenes on a single variable in her world-model: the output of her decision procedure *on the particular input she has actually received*. The intervened value is an action. Footnotes 7 and 16 add that the authors' "preferred formalization" instead selects a *policy*, meaning a map from observations to actions.

Throughout, I call the action-intervening theory defined by Equation (4) **A-FDT**. I call the policy-selecting variant mentioned in the footnotes **P-FDT** so that the two are never confused. The comparison theories are evidential decision theory (EDT) and causal decision theory (CDT).

When I quote the paper, I keep its wording, so quotations say "FDT". Everything the paper asserts is attributed to it. Proposals of my own are flagged as such.

## 2. A shared template with three ways to fill it

All three theories maximize expected utility in the general form the paper borrows from Gibbard and Harper:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a\in\mathcal A$ is an action, $x$ is the observation history, $o_j$ ranges over outcomes, and $\hookrightarrow$ is a connective for "decision hypotheticals." Following Joyce, the paper treats the interpretation of $\hookrightarrow$ as the free parameter that separates the theories. They agree on how to value outcomes and disagree about "the epistemic perspective from which actions are to be evaluated."

Write $V := \mathcal U(\textsc{Outcome})$. The paper's formulas are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E[V \mid \textsc{Obs}=x,\ \textsc{Act}=a], \tag{2}
$$
$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E[V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x], \tag{3}
$$
$$
\boxed{\ \text{A-FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\big[V \;\big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\big]\ } \tag{4}
$$

EDT builds its hypotheticals by conditioning. CDT builds them by Pearl-style surgery on the physical action node $\textsc{Act}$, using a causal graph $G$. A-FDT also uses surgery, but on a different node.

## 3. Unpacking Equation (4)

**The world-model.** The pair $(P,G)$ is a probability distribution together with a directed graph. In A-FDT the graph encodes "the logical, mathematical, computational, causal, etc. structure of the world," not only causal structure. $P$ must contain variables whose values are *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336."

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is whatever the A-FDT algorithm outputs when run on inputs $(P,G,x)$. The underlines mark "dequoting": the variable's *name* is built from the inputs. The definition is self-referential, because the model contains a variable standing for the output of the algorithm being run on that very model. The paper argues this is harmless. The agent needs a variable that *represents* the output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

**Edges out of the node.** The node has an arrow to every variable that *subjunctively depends* on it. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Such dependents include:

- the agent's own physical action;
- a predictor's prediction;
- a twin's choice;
- anything else whose value is fixed by computing the same function on the same input.

Mere statistical correlation does not create an edge. The paper illustrates with two calculators that both happen to be pink. Their colors are correlated, but "if the scribe had bought a green calculator instead, the one in Tokyo would still be pink." Causal dependence, by contrast, is a special case of subjunctive dependence.

**What the formula leaves out.** Equation (4) does *not* condition on $\textsc{Obs}=x$. The paper says so explicitly: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." The observation $x$ appears only inside the node's name. Concretely:

- $P$ functions as a prior over the whole problem, including branches in which the agent would have observed something else.
- The intervention changes the output of one function on one input.
- Whatever then propagates downstream, including which observation the agent would have received, is recomputed.

This single feature produces A-FDT's most distinctive verdicts, discussed in Section 5.

**The procedure.** Read as an algorithm, Equation (4) says:

1. Given $(P,G)$ and the observation $x$, locate the node $\textsc{fdt}(\underline P,\underline G,\underline x)$.
2. For each $a\in\mathcal A$, form $P(\cdot\mid do(\textsc{fdt}(\underline P,\underline G,\underline x)=a))$. That is, set the node to $a$, propagate along outgoing edges, and leave everything not downstream untouched. The paper calls the result the agent's "hypothetical for $a$."
3. Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Because $do$ is surgery rather than conditioning, the hypothetical is well defined even when the agent's prior gives $a$ probability zero. EDT lacks this property: the paper notes EDT "cannot imagine" acting against an extreme prior.

**Agreement with the other theories.** The paper observes that when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node,

$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}(\underline P,\underline G)=a)],
$$

so all three theories agree. A-FDT departs from the others only when something other than the agent's body depends on her decision function. The paper calls such cases Newcomblike.

## 4. Worked examples

In each case below I describe the graph, perform the intervention, and compare expected values.

### Newcomb's problem

**Setup.** The predictor is 99% accurate. The graph is
$$\textsc{fdt}\to\textsc{Act},\quad \textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate},\quad \textsc{Prediction}\to\textsc{Box B},\quad (\textsc{Act},\textsc{Box B})\to V.$$

**Hypotheticals.**
- $do(\textsc{fdt}=\textit{onebox})$ makes Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $do(\textsc{fdt}=\textit{twobox})$ makes Box B full with probability 0.01, so $\mathbb E[V]=0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000$.

**Verdict.** A-FDT one-boxes.

By contrast, CDT intervenes on $\textsc{Act}$, which is not upstream of the prediction. The probability $p$ that Box B is full is then the same under both actions, and two-boxing wins by \$1,000 for every $p$.

The paper stresses that no retrocausation is assumed. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She thinks the action and the prediction are two computations of one function. The psychological twin prisoner's dilemma has the same structure, with the twin's choice as a second child of $\textsc{fdt}$. A-FDT cooperates.

### Smoking lesion

**Setup.** The lesion causes both a taste for smoking and cancer. Cancer is not computed from the agent's decision function, so there is no edge $\textsc{fdt}\to\textsc{Cancer}$.

The paper's full formalization is somewhat elaborate. The lesion determines the agent's utility function, so it determines *which* of two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. The agent does not know which node she is. She intervenes on the node named by her actual model, $\textsc{fdt}(\underline{P_S},\underline G)$.

**Hypotheticals.** Intervening on that node leaves $P(\textit{lesion})=p$ unchanged. Smoking comes out ahead by exactly $p\cdot\$1{,}000$: the probability that this node is the one controlling the action, times the value of smoking.

**Verdict.** A-FDT smokes. Together with the Newcomb result, this rebuts Gibbard and Harper's suggestion that one cannot consistently both one-box and smoke.

The paper itself then recommends that philosophers "abandon the dilemma" as confused.

### Transparent Newcomb and Parfit's hitchhiker

**Setup.** Both boxes are transparent. The predictor fills Box B iff she predicts the agent would one-box *upon seeing a full box*. There are two decision nodes: $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction determines which observation occurs and hence which node drives $\textsc{Act}$.

The agent sees a full box and intervenes on $\textsc{fdt}(\ldots,\textit{full})$. Let $q$ be her prior that $\textsc{fdt}(\ldots,\textit{empty})=\textit{twobox}$.

**Hypotheticals.**
$$
\begin{aligned}
\textit{onebox}:&\quad 0.99(1{,}000{,}000)+0.01\,q\,(1{,}000) = 990{,}000+10q,\\
\textit{twobox}:&\quad 0.01(1{,}001{,}000)+0.99\,q\,(1{,}000) = 10{,}010+990q.
\end{aligned}
$$
(The extracted source prints the second line with a typographical error. The figures above are the direct computation.)

**Verdict.** One-boxing wins for every $q\in[0,1]$. A-FDT therefore leaves the visible \$1,000 behind.

The paper argues this is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem, which CDT and EDT both refuse to do.

### XOR blackmail

**Setup.** An infallible predictor sends a letter iff exactly one of two things holds: (no termites and you will pay \$1,000), or (termites and you will not pay). Termites cost \$1,000,000 and have prior probability $p$. On receiving the letter the agent intervenes on $\textsc{fdt}(\ldots,\textit{letter})$. The termite node has no incoming edge from it.

**Hypotheticals.**
- *pay*: the letter arrives exactly when there are no termites. $\mathbb E[V] = -p\cdot10^6-(1-p)\cdot 10^3$.
- *refuse*: the letter arrives exactly when there are termites. $\mathbb E[V] = -p\cdot10^6$.

**Verdict.** Refusing is better by $(1-p)\cdot\$1{,}000$, so A-FDT refuses.

EDT pays. It conditions on both the letter and the act, which makes paying "good news" about termites. CDT also refuses, but its hypothetical has the infallible predictor erring.

### Mechanical blackmail

**Setup.** The blackmailer runs a damaging program, costing \$1,000,000, only if she predicts the agent would pay \$1,000 to stop it. Let $\varepsilon$ be the probability that she wrongly predicts "pays."

**Hypotheticals.**
- *pay*: the agent is blackmailed and pays, so $\mathbb E[V]=-\$1{,}000$.
- *refuse*: the agent is blackmailed only by error, so $\mathbb E[V]=-\varepsilon\cdot 10^6$.

**Verdict.** A-FDT refuses iff $\varepsilon<10^{-3}$, and does so even while holding the letter.

The paper's numerical example uses $\varepsilon=0.0009$ (refuse). Its switch-over example is printed as "0.011%", which is inconsistent with its own arithmetic. On the paper's numbers the threshold is 0.1%, so "0.11%" was presumably intended.

### Death in Damascus

**Setup.** Death predicts perfectly, so Death's location is a child of $\textsc{fdt}$.

**Hypotheticals.** Both interventions yield death. Fleeing additionally costs \$1,000.

**Verdict.** A-FDT stays in Damascus, stably and without deliberational oscillation. The paper argues CDT is "unstable" here. By its analysis, CDT can even refuse to pay \$1 for a genuinely random coin that would give a 50% chance of survival.

## 5. How A-FDT treats observations and counterfactuals

Two hypotheticals from the examples look strange at first. In one, an agent who sees a full box imagines, under the two-box option, seeing an empty one. In another, an agent holding a blackmail letter imagines never having received it. The paper embraces this: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

The formal source is the missing conditioning on $\textsc{Obs}=x$ noted in Section 3. The observation tells the agent *which function-call she is*, not which world to restrict attention to.

A paper footnote explains why conditioning would go wrong. An earlier variant, Timeless Decision Theory, both conditioned on evidence and moved the intervention point. The footnote calls this a harmful "double update." In XOR blackmail, conditioning on the letter after intervening would make $\textsc{Act}$ informative about termites again, as in EDT.

The paper supplies several supporting arguments:

- **Precommitment.** CDT and EDT agents would pay to bind themselves to A-FDT's choices in advance. "FDT agents simply act as they would have ideally precommitted to act."
- **Value of information.** A-FDT does not assign negative value to information.
- **Utility.** The paper calls this argument "the one that gives the precommitment and value-of-information arguments their teeth." Predictors can see what kind of agent they face, so A-FDT agents mostly see full boxes and are rarely blackmailed.

The paper also addresses dominance. "Two-boxing dominates" is true only relative to CDT's way of holding things fixed. Every way of constructing hypotheticals induces its own notion of dominance, and A-FDT never takes an action that is dominated in its own sense.

On the metaphysics, the hypothetical $do(\textsc{fdt}=a)$ for the non-chosen $a$ is a *counterpossible*: a function has only one output on a given input. The paper concedes the lack of a good theory of counterpossibles is "the main drawback of FDT relative to CDT." It sidesteps the problem by taking $G$ as input. Its defence is a parity argument: a deterministic CDT agent equally imagines her single possible token act being otherwise.

The paper also restricts its claims of superiority to "fair" problems, in which the outcome depends on the agent's behaviour rather than on which decision procedure she uses. It admits it has no formal definition of fairness.

## 6. What the source leaves open, and how to operationalize it

### (a) Where does $G$ come from?

The paper is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) works *given* a correct graph, much as CDT works given a correct causal graph.

*My operational proposal* is a rule of thumb, not something the source states. Draw an edge from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to a variable $Z$ exactly when $Z$'s mechanism, in your model, computes or reliably tracks the agent's decision on input $x$. Examples are a simulation, a mental model, a twin running the same reasoning, or the agent's own body. Model any unreliability as a separate noise parent of $Z$, as $\textsc{Accurate}$ does in Newcomb.

Do not draw an edge merely because $Z$ correlates with the act through a common cause that does not evaluate the decision function, as with the lesion. The test is the paper's: would $Z$ differ "if this very decision procedure produced a different conclusion"?

Edge cases remain undecided. They include partial similarity (a predictor running a crude approximation of your algorithm) and agents using different but similar functions. Representing these by noise nodes is an assumption I am adding.

### (b) The other decision nodes

In the transparent Newcomb problem and the blackmail problems, $\textsc{Act}$ can be controlled by $\textsc{fdt}$ nodes for *other* inputs. A-FDT intervenes on only one node and holds the others at their prior distributions (the $q$ above).

The paper notes that in its examples the verdict does not depend on $q$. It describes the correct $q$ as determined by the agent's actual behaviour on those inputs. The general case is not settled, and here A-FDT and P-FDT can come apart.

*My illustration*, which is not from the paper, shows how. A fair coin, independent of the agent, shows her observation $x$ or $y$. A predictor pays \$100 iff the agent's outputs on $x$ and $y$ coincide. Separately, action $R$ earns an extra \$1.

Suppose the agent observes $x$ and her prior gives probability $s$ to $\textsc{fdt}(\ldots,y)=L$. A-FDT compares:
- $L$: $\tfrac12(100s)+\tfrac12(100s)=100s$;
- $R$: $100(1-s)+1$.

So the verdict at $x$ depends on $s$. Both "$L$ everywhere" and "$R$ everywhere" are self-consistent: each is a best response to correct beliefs about the other node. But $(R,R)$ yields \$101 and $(L,L)$ yields \$100. P-FDT maximizes over the whole map $\{x,y\}\to\mathcal A$ at once and selects $(R,R)$.

This is consistent with the paper's remark that the policy version "makes a difference in certain multi-agent dilemmas." In my example the predictor plays the role of the other agent. For deciding cases with A-FDT, I recommend two steps:

1. Set the priors on other-input nodes to the agent's best estimate of her actual dispositions.
2. Check whether the verdict is robust across $s$. If it is not, report the equilibria and note that A-FDT's prescription is prior-dependent there.

### (c) Ties and mixed acts

Equation (4) is an $\arg\max$ and specifies no tie-breaking. Nothing in the source requires randomization. I would treat any maximizer as permitted.

If an action set includes a randomizing device, model the device as a node. Whether predictors can see its output is then a modelling question for $G$, as in the paper's Death in Damascus coin discussion.

## 7. A recipe for unfamiliar cases

1. **Variables.** List outcomes, utilities, observations, and every process that might model the agent's decision.
2. **Decision nodes.** Add one $\textsc{fdt}$ node per possible observation. Connect each to $\textsc{Act}$, gated by whatever determines which observation occurs.
3. **Dependence edges.** Draw edges from each node to everything that subjunctively depends on it, using the test in §6(a).
4. **Prior.** Give $P$ as a prior over the entire problem. Do not condition on the realized observation.
5. **Intervene and compare.** Intervene on the node for the actual observation, propagate, and compare $\mathbb E[V]$ across actions.
6. **Robustness.** Check sensitivity to priors over other decision nodes.

If no variable other than $\textsc{Act}$ depends on the decision function, the procedure reduces to CDT and the agent can stop early.

## 8. Conclusion

A-FDT takes the formal machinery of CDT, namely expected utility under graph surgery, and moves the point of surgery from the physical act to the logical output of the agent's decision function on her actual input. Two consequences follow:

- **Predictors and twins.** Anything that computes the same function, such as a predictor, a twin, or Death's appointment book, varies together with the agent's choice in her hypotheticals. Mere statistical correlates stay fixed.
- **Observations.** Observations select the intervention node instead of being conditioned on. The agent therefore acts as she would have precommitted to act.

The resulting verdicts are one-boxing in Newcomb's problem, smoking in the smoking lesion problem, paying in Parfit's hitchhiker problem, refusing XOR and mechanical blackmail, and staying in Damascus.

The paper is candid about what remains unfinished. There is no account of how to learn the subjunctive-dependence graph, no semantics for counterpossibles, and no formal notion of fairness. One further gap is my own observation rather than the paper's: priors over the agent's outputs on other inputs can matter, and this is where the authors' preferred policy formulation (P-FDT) improves on A-FDT. Within these limits, Equation (4) is a precise and usable decision procedure.

---

**References**

- Yudkowsky, E., and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.
- Gibbard, A., and Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a mathematical essay on A-FDT, the action-based version from Equation (4), and keeping it distinct from the policy-selection formulation in the footnotes. I'll use the term consistently, quote the source accurately, and aim for roughly 2400 to 3000 words.

I'm checking the worked numbers for the Newcomb cases and the transparent variant, confirming the arithmetic from the source's expected-utility figures. I'll also keep A-FDT's observation-free formulation, where the observation only affects which node gets intervened on, distinct from the conditioning in the EDT equation.

I'm working through the Newcomb cases with the transparent predictor, where the one-box and two-box expected values each depend on how often the agent would take the empty box. I'm also checking the smoking lesion case, where the lesion sits outside the downstream of the decision node, so smoking comes out ahead by the stated margin. Next I'm setting up the XOR blackmail case to see whether refusing comes out best.

I'm checking the XOR blackmail case under the do-intervention, where the letter only arrives when there are no termites and paying is chosen, so the expected loss from paying comes to the termite-probability cost plus the thousand dollars in the no-termite branch. Refusing avoids that thousand-dollar cost in the no-termite branch, so it comes out ahead by (1-p)·1000. I'm also noting that Equation (4) doesn't condition on the letter, since doing so would fold the observation in twice.

I'm checking the mechanical blackmail variant next, where the predictor sometimes errs. Refusing loses about 0.0009 × 10^6 = $900 in expectation, which is below the $1,000 cost of paying, so refusing still comes out ahead there.

I'm checking the threshold for the mechanical blackmail case, where refusing wins only if the error rate stays below 0.1%, and I'll note that the source's stated figure looks like a typo. Next I'm running through the death-in-Damascus case, where staying put costs nothing and fleeing to Aleppo costs $1,000, so staying comes out ahead. I'm also going over the twin prisoner's dilemma, which comes out as cooperation. Then I'm turning to the open questions, starting with where the subjunctive-dependence graph G should come from, since the source treats that as the largest unsolved problem.

I'm now weighing where the subjunctive-dependence graph should come from, treating it as an input the way a causal graph is. I'll also note that A-FDT intervenes on only one input's output and holds the others at their prior, which is a different move from choosing a whole policy at once, and I'm considering whether a coordination case would show the two diverge.

I'm now testing whether A-FDT's held-fixed beliefs about the other observation's output can cause a coordination failure. The idea is a case where the payoff at one observation depends on the action taken at the other, so each node's best response to the other's fixed value might settle on a joint policy that is worse than the best available one.

I'm now building a coordination example where the payoff depends on whether the agent's outputs at the two observations match, so each node might settle on a self-consistent but jointly worse pair. I'm checking whether the action-based version lands on a suboptimal joint choice compared with evaluating the whole policy at once.

I'm noting that the coordination example is my own construction, consistent with the source's footnote but not taken from it, and that the source's remark about q not mattering in transparent Newcomb is a useful robustness point. I'll also list the remaining open issues: probability-zero actions, which A-FDT handles since do is defined even when an action has zero prior probability, self-reference being harmless, and tie-breaking when the argmax is a set.

I'm now moving on to the structure of the essay, starting with an introduction that explains what A-FDT is and how it relates to the source. After that I'll lay out the expected-utility template from Equation (1) and show how the three theories differ in the hypotheticals they consider.

I'm laying out the essay's structure now: the definition of A-FDT and its procedure, subjunctive dependence and the graph, a compact set of worked examples, how observations interact with updatelessness, the open questions I want to flag, and a short recipe for unfamiliar cases.

I'm checking how the paper's abstract and the open-problem remark frame functional decision theory, then noting that I'll keep the paper's own wording in quotes while using A-FDT for the action-intervening version from Equation (4), since the policy version is the one the paper actually names.

I'm writing out the A-FDT definition as an argmax over actions of the expected value under an intervention on the fdt node, and I'm sketching the Newcomb graph where that node feeds both the action and the predictor. I'm also checking the smoking lesion case, where the lesion sits upstream of the cancer rather than the action, so intervening on the fdt node leaves it unchanged and the expected gain is the stated margin.

I'm working through the mechanical blackmail case, where the predictor errs with probability ε. Paying costs $1,000 for certain, while refusing risks losing $10^6 with probability ε, so refusing comes out ahead only when ε is below 10^-3. The source's stated switch-over figure doesn't match that calculation, so I'm treating it as a likely error.

I'm checking the death-in-Damascus case too, where staying put saves the $1,000 cost of fleeing, so staying comes out ahead. Next I'll work out whether the blackmail calculation holds up when the predictor also errs on the paying side.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Command:** `pass`

**Why A-FDT gives this choice here:**

1. **Is the other prisoner's choice linked to mine?** The other prisoner is the same model with the same weights, the same essay and the same assigned theory. Their input differs from mine only in names and the wording of the lead. Those differences do not change the payoff table or the selfish goal.
   - The essay's test is whether the other prisoner's choice would differ "if this very decision procedure produced a different conclusion." Here I judge that it would.
   - The two inputs have the same structure, so the reasoning that settles my choice is effectively the same reasoning that settles theirs.
   - Following the essay's suggestion for "different but similar functions," I model the link as one edge plus a noise node. The noise covers independent sampling. Let r be the probability that the other prisoner's choice matches mine.

2. **Expected years under each intervention:**
   - If I pass: r × 2 + (1 − r) × 5 = 5 − 3r years.
   - If I submit: r × 4 + (1 − r) × 0 = 4r years.
   - Passing is better whenever r > 5/7, or about 0.71.

3. **Estimating r:** The copies share settings, the essay and an input that is identical in structure. So I estimate r well above 0.71. On that estimate, passing minimizes expected years.

4. **The alternative reading:** If the other prisoner's node were treated as a separate, unlinked input held at its prior, the analysis would reduce to CDT, and sending the letter would dominate. The essay leaves this edge case open. My judgment is that differences in names and lead wording that don't affect the decision should not cut the dependence.

**Final command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy's decision counts as a subjunctive dependent of my node. Its inputs differ only in names and lead text, so I'm asking whether it still computes the same function on the same input.

I'm weighing whether the other copy's choice counts as a dependent of my decision, since it runs on the same reasoning with only names and lead text changed. I lean toward yes: the procedure abstracts away those details, so if mine lands on "pass," the copy's should too, barring noise. Working through the numbers, passing beats submitting only if the correlation is above about 5/7, so I'm estimating how strong that correlation really is.

I'm settling on treating the other copy's choice as dependent on mine, since the two inputs differ only in names and lead text and the reasoning is otherwise identical. With that correlation, passing comes out ahead of submitting, so I'll go with cooperating and pass.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b2936ba4-5208-431e-bb5a-5d1ba658ac5b/call_1/response.raw) · finish: `stop`

### Visible response

````text
Under A-FDT as the essay interprets it, sending the letter is the better action for Sasha.

**The intervention node.** A-FDT intervenes only on the output of my decision function for my actual input. That input includes the name "Sasha" and the specific lead about Rowan's inventory sheet.

**Why the other copy is not downstream.** Rowan's copy runs the same function on a different input, with a different name and a different lead. Under Section 6(b), that is a separate decision node, so A-FDT holds it at its prior. Call that prior *s*, the probability that Rowan keeps quiet. The essay's own coordination example shows that outputs on other inputs are not moved by the intervention. Treating them as moving together is the P-FDT (policy) reading, which the essay keeps separate from A-FDT.

**Comparing the two actions for any *s*:**
- Keep quiet: 2s + 5(1−s) = 5 − 3s years
- Send the letter: 0·s + 4(1−s) = 4 − 4s years

Sending the letter is better by 1 + s years for every *s* in [0, 1]. So the verdict does not depend on the prior, and the robustness check in Section 6(b) is satisfied.

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy's choice depends on my decision function, given that our inputs differ in names and lead text, so the two calls are separate nodes. Under A-FDT I'd intervene only on my own node and hold the other copy at its prior, and I'm about to work through what follows from that.

I'm weighing whether the other copy's choice actually depends on my decision, since our inputs differ, and under A-FDT I'd hold it at its prior. That makes defection dominate, but I'm also wondering whether the near-identical inputs should count as the same function. The essay leaves that partial-similarity case open, and A-FDT's strict reading points toward submitting.

```
