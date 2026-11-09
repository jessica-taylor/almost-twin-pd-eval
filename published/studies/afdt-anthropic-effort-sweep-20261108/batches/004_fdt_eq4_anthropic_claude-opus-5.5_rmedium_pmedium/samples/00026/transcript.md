# 004_fdt_eq4_anthropic_claude-opus-5.5_rmedium_pmedium / 00026

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/38f7bf2e-7d34-4d83-a20b-fabc2d649321/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/38f7bf2e-7d34-4d83-a20b-fabc2d649321/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Intervening on What Your Algorithm Outputs

## 1. What this essay covers

Yudkowsky and Soares (2017) present *functional decision theory* as an expected-utility theory with an unusual answer to one question: when you deliberate, what are you choosing between? Causal decision theory (CDT) says you choose a physical act. Evidential decision theory (EDT) says you choose which act it would be best news to learn you took. Functional decision theory says you choose the output of a fixed mathematical decision function. The agent asks, in the paper's words, "Which output of this very function would yield the best outcome?"

The paper gives this idea a formal statement in Equation (4) of Section 5. In that equation the variable maximised over is an **action** $a \in \mathcal A$. A footnote adds that the authors' preferred formalisation optimises over **policies**, meaning maps from observations to actions. To keep these apart, I use **A-FDT** (action functional decision theory) for the theory defined by Equation (4). I use **policy-FDT** for the policy-level variant that the footnotes mention but do not formalise.

The essay does four things:

1. states A-FDT precisely;
2. explains how it builds its counterfactuals;
3. works through the paper's examples, including recomputing the numbers;
4. identifies what Equation (4) leaves undetermined and proposes operational fixes.

Throughout, I mark which claims belong to the source and which are my own proposals.

## 2. Ingredients

All three theories in the paper share the expected-utility template:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $x$ is the observation history. The connective $\hookrightarrow$ ("if $a$ were done, $o_j$") is deliberately left as a free parameter. Following Joyce, the authors treat the competing theories as rival readings of $\hookrightarrow$, not rival theories of value. Writing $V := \mathcal U(\text{Outcome})$:

- **EDT** reads $\hookrightarrow$ as conditioning:
  $$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V\mid \text{Obs}=x, \text{Act}=a).$$
- **CDT** reads it as a Pearl intervention on the physical act, then conditions on the observation:
  $$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid do(\text{Act}=a), \text{Obs}=x\big).$$

A-FDT uses the same apparatus as CDT, a probability distribution $P$ plus a directed graph $G$. The graph differs in what it encodes. For CDT, $G$ records causal structure. For A-FDT, $G$ records **subjunctive dependence**: the structure by which changing the output of a mathematical function would change other variables. This includes physical systems that compute the function or model it.

The source summarises the relationship this way: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The model must therefore contain **logical nodes**. These are variables whose values are outputs of particular computations. The crucial one is
$$
\textsc{fdt}(\underline P, \underline G, \underline x),
$$
the output of the A-FDT procedure itself when run on this very model and observation. The underlines denote quotation: the node's *name* is built from the model, while its *value* is unknown during deliberation. The authors say this self-reference is harmless, citing Kleene's recursion theorem.

## 3. The definition

**Equation (4).**
$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\; \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\Big).
$$

This is the formula I call A-FDT. Unpacked into steps:

1. **Locate the decision node.** Given the actual observation history $x$, find the node $\textsc{fdt}(P,G,x)$.
2. **Intervene.** For each candidate action $a$, replace that node's mechanism with the constant $a$. Recompute every descendant in $G$: the agent's physical act, any predictor's prediction, a twin's choice, and so on. Leave non-descendants at their prior distribution.
3. **Evaluate.** Compute $\mathbb E[V]$ in the resulting distribution.
4. **Act.** Output the maximising $a$.

The source identifies two structural differences from CDT.

- **Where the surgery happens.** CDT intervenes on the token, the physical act. A-FDT intervenes on the type, the function's output on this input. Anything else that computes or models that output moves with it.
- **How observations enter.** CDT conditions on $\text{Obs}=x$. A-FDT does not condition; it uses $x$ to select which node to intervene on. In the source's words: "FDT responds to observation by changing which node it intervenes upon."

The second point has a large consequence. When the A-FDT agent imagines outputting something else, it may imagine having received different observations. This is how it achieves "updateless" behaviour in cases like the transparent Newcomb problem.

**Agreement theorem (source).** Suppose every correlation between Act and other variables is caused by Act, except possibly correlation with the agent's own fdt node. Then
$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)],
$$
so EDT, CDT and A-FDT agree. Divergence requires something other than the agent's own action that tracks the agent's decision function, such as a predictor, a twin, or a copy.

## 4. Worked examples

### 4.1 Newcomb's problem

The predictor is 99% accurate. Box A holds \$1,000. Box B holds \$1,000,000 iff one-boxing was predicted.

In the A-FDT graph, $\textsc{fdt}(P,G)$ has two children:

- **Act**, a copy of the fdt node's value;
- **Prediction**, which also takes an Accurate noise node as input. Box B depends on Prediction.

The two interventions give:

- $do(\textsc{fdt}=\textit{onebox})$: Box B is full with probability 0.99, so $\mathbb E V = 0.99\times 10^6 = \$990{,}000$.
- $do(\textsc{fdt}=\textit{twobox})$: Box B is full with probability 0.01, so $\mathbb E V = 0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = \$11{,}000$.

A-FDT one-boxes. CDT disagrees because, in its graph, Prediction is not downstream of Act. Its intervention therefore leaves $P(\text{full}) = p$ unchanged, and two-boxing wins by \$1,000 for every $p$.

The source's EDT figure for one-boxing reads "\$999,000". With 99% accuracy the arithmetic gives \$990,000, the same value as the A-FDT case. This is evidently a slip and changes no conclusion.

The **twin prisoner's dilemma** has the same structure. Both prisoners' actions are children of the same fdt node, so outputting *cooperate* yields \$1,000,000 and outputting *defect* yields \$1,000.

### 4.2 The smoking lesion

Smoking is correlated with cancer only through a common cause, the lesion. In A-FDT's graph the cancer node is **not** a descendant of any fdt node. A lesion does not compute or model the agent's decision function.

The source formalises the problem in more detail. The lesion determines which utility function the agent has: $\mathcal U_S$, which likes smoking, or $\mathcal U_R$. That in turn determines which of two decision nodes controls Act:
$$
\text{Act} = \begin{cases} \textsc{fdt}(P_S,G) & \text{if lesion},\\ \textsc{fdt}(P_R,G) & \text{if not.}\end{cases}
$$

Let $p = P(\text{lesion})$. Intervening on $\textsc{fdt}(P_S,G)$ leaves $p$ unchanged. The gain from smoking is therefore $p\times\$1{,}000 > 0$, and A-FDT smokes.

The lesson is that what matters is the graph, not the probabilities. Gibbard and Harper showed that Newcomb and the smoking lesion share one joint distribution after relabelling. CDT reuses its graph across the two problems; A-FDT cannot, because the subjunctive dependencies differ.

### 4.3 The transparent Newcomb problem

Both boxes are visible. The predictor fills B iff she predicts the agent will one-box *upon seeing B full*. The agent sees B full.

The graph now has two decision nodes, $F := \textsc{fdt}(P,G,\textit{full})$ and $E := \textsc{fdt}(P,G,\textit{empty})$:

- Prediction depends on $F$ and on the Accurate node.
- Box B depends on Prediction.
- Act equals $F$ if B is full and $E$ if B is empty.

Having observed *full*, A-FDT intervenes on $F$. It does **not** condition on B being full. Let $q$ be the prior probability that $E$ outputs two-box.

- $do(F=\textit{onebox})$:
  - With probability 0.99 the prediction is accurate, B is full, the agent one-boxes, and receives \$1,000,000.
  - With probability 0.01, B is empty, $E$ acts, and the agent receives $q\cdot\$1{,}000$ in expectation.
  - Total: $\$990{,}000 + 10q$.
- $do(F=\textit{twobox})$:
  - With probability 0.99, B is empty and the agent receives $1{,}000q$.
  - With probability 0.01, B is full, the agent two-boxes, and receives \$1,001,000.
  - Total: $\$10{,}010 + 990q$.

A-FDT one-boxes for every $q\in[0,1]$. The source prints the second total as "\$110,00 + q·\$990"; the correct arithmetic is \$10,010. Nothing turns on the difference.

**An inconsistency in the source.** When stating the objective for this example, the text writes $\mathbb E(V\mid do(F=a, \text{Obs}=\textit{full}))$, with an Obs term inside the intervention. The calculation that follows does *not* condition on full: it sums over the inaccurate branch, in which B is empty.

Only the unconditioned reading matches both Equation (4) and the stated result. Conditioning on Obs=full would make $F$'s value irrelevant to Box B's contents, and the agent would two-box exactly as CDT does. I therefore read Equation (4) literally: **no conditioning on in-problem observations.**

**Parfit's hitchhiker** has the same structure, as the source notes. Paying in the city corresponds to one-boxing when facing full boxes.

### 4.4 XOR blackmail

A perfect predictor sends a letter iff exactly one of these holds:

- (i) no termites, and the agent pays upon receiving the letter;
- (ii) termites, and the agent refuses.

Let $p$ be the prior probability of termites, which cost \$1,000,000.

Intervening on $L := \textsc{fdt}(P,G,\textit{letter})$ gives:

- **$L=\textit{pay}$.** The letter arrives iff there are no termites. Expected loss: $p\cdot 10^6 + (1-p)\cdot 1{,}000$.
- **$L=\textit{refuse}$.** The letter arrives iff there are termites. Expected loss: $p\cdot 10^6$.

Refusing is better by $(1-p)\,\$1{,}000$, because the termite node is not a descendant of $L$. EDT pays, since conditioning on paying makes termites impossible given the letter. CDT refuses, for a different reason: Infestation is causally upstream of its act.

### 4.5 Mechanical blackmail and the error threshold

A blackmailer runs a damaging program, costing \$1,000,000, iff she predicts the agent would pay \$1,000 when notified. Suppose she wrongly predicts "pays" with probability $\varepsilon$.

Intervening on the node for "after receiving blackmail":

- **pay:** the agent is always blackmailed and always pays, losing \$1,000;
- **refuse:** the agent is blackmailed with probability $\varepsilon$, losing $\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon < 10^{-3}$.

The source's first case, $\varepsilon = 0.0009$, gives an expected loss of \$900 and refusal, which is consistent. Its second case is stated as "0.011%" and is said to lead to paying. But $\varepsilon = 0.00011$ gives an expected loss of only \$110, below the threshold, so A-FDT would still refuse. The intended figure was presumably 0.11%. The structural point stands either way: A-FDT computes this threshold, which is a property of the agent's disposition, not of the situation it actually observes.

### 4.6 Death in Damascus

Death's appointment book is a child of the fdt node. Under both interventions, Death meets the agent wherever she goes. Staying in Damascus therefore saves \$1,000, and A-FDT stays.

This settles the question in one pass. CDT, by contrast, faces an unstable deliberation loop, which ratification procedures address only by recommending a near-50/50 randomisation.

## 5. Why the counterfactuals look the way they do

A-FDT's hypotheticals are counterpossible. Suppose the procedure in fact outputs *onebox*. Then "it outputs *twobox*" is false as a matter of logic, not merely as a contingent fact.

The source's response has three parts:

1. CDT faces an analogous issue in deterministic worlds, where the actual token act is also fixed.
2. Hypotheticals are "decision-theoretic instruments constructed from beliefs", not claims about possible worlds.
3. Equation (4) sidesteps a missing logic of counterpossibles by taking the dependency graph $G$ as an **input**. Footnote 9 says this explicitly: the dependency structure "be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT."

The resulting picture is "global". The agent asks what the whole world, including predictions made earlier and observations it might have received, would look like if this function's output differed. The source also offers a dominance notion of its own. Action $a$ FDT-dominates $b$ if, holding the subjunctive dependencies fixed, switching the output from $b$ to $a$ is never worse and sometimes better. The source then argues that dominance is relative to a choice of hypotheticals, so it cannot settle the dispute between theories by itself.

## 6. What Equation (4) leaves open, and proposed fixes

Equation (4) is fully determinate only once $(P, G, x)$ is fixed. Several of the choices needed to fix it are not settled by the paper.

### 6.1 Constructing $G$ (open in the source)

The source says plainly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

**Proposed heuristic (mine).** Draw an edge from the fdt node to a variable $Y$ if $Y$ is produced by a process that

- runs the agent's decision function,
- simulates it, or
- predicts its output by reasoning about it,

where "reasoning about it" means that the process's error rate would be unchanged if the function's output changed. Variables merely correlated with the agent's traits through common causes, such as lesions, genes or demographics, get no edge from the fdt node.

Imperfect predictors are handled by an independent noise parent, as with Accurate in the examples. Hard intermediate cases remain open. One example is a predictor relying on statistics about similar but non-identical algorithms.

### 6.2 Priors on non-intervened decision nodes

In the transparent Newcomb problem and the smoking lesion, A-FDT needs priors ($q$) on the decision nodes for observations the agent did not receive. The source says the true values are 1 and 0 respectively, but that uncertainty about them "won't matter" in those examples. In general it can matter.

**Proposal (mine): reflective consistency.** Choose the priors on off-path nodes $\textsc{fdt}(P,G,y)$ so that they match what A-FDT would output at $y$ under those same priors. That is, look for a fixed point of the map from beliefs about one's own outputs to the outputs those beliefs recommend. When the off-path choices do not affect the on-path argmax, as in every example above, any prior works.

### 6.3 Which $P$?

Since A-FDT does not condition on $x$, the choice of $P$ carries all the epistemic weight. In the examples, $P$ is the agent's model of the whole dilemma as specified at the outset: before the boxes are seen, the letter is read, or the ride is offered.

**Proposal (mine).** Take $P$ to be the agent's beliefs at the point where the decision problem is defined. These should include every process that may have predicted the agent, with everything observed afterwards represented by node choice. If the problem is redrawn so that it begins after the observation, A-FDT collapses toward CDT-like behaviour. The modelling choice is therefore substantive, and the paper does not legislate it.

### 6.4 Ties and zero-probability branches

The argmax may contain several actions. The paper gives no tie-breaking rule. Any fixed rule will do, provided it is part of the function that predictors model.

Note also an asymmetry with EDT. Intervention, unlike conditioning, is well defined even when the agent assigns probability zero to some output. This is why A-FDT is immune to the Spohn-style problem of extreme priors and to the cosmic-ray problem.

### 6.5 Actions versus policies

A-FDT holds the other decision nodes at their priors and optimises a single output. Policy-FDT would intervene on a function $\pi : \mathcal X\to\mathcal A$ and optimise jointly. The source claims the difference arises only in some multi-agent dilemmas.

**Illustration (mine).** Two copies of the agent run the same function. One observes $L$, the other $R$; each chooses $X$ or $Y$. Each copy receives 2 if both choose $X$, 1 if both choose $Y$, and 0 otherwise.

Suppose the copy seeing $L$ believes $\textsc{fdt}(\cdot,R) = Y$. Intervening on $\textsc{fdt}(\cdot,L)$ gives 1 for $Y$ and 0 for $X$, so it chooses $Y$, and symmetrically for the other copy. The profile $(Y,Y)$ is a self-consistent A-FDT outcome under my reflective-consistency priors. Policy-FDT instead compares whole policies and selects $\pi(L)=\pi(R)=X$, which yields 2.

So A-FDT can be trapped by coordination failures among its own observation-indexed instances. This is the situation the footnote gestures at.

## 7. A recipe for unfamiliar cases

Combining the source with the proposals above:

1. **Model.** Write the dilemma's variables and prior $P$ as of the moment the problem is posed (6.3).
2. **Decision nodes.** Add a node $\textsc{fdt}(P,G,y)$ for each observation history $y$ under which the agent may have to act. Make Act a switch: whichever observation obtains selects which node controls it.
3. **Dependencies.** Add edges from each fdt node to every predictor, simulator, twin or copy that tracks that node's output, using the criterion in 6.1. Add no edges to mere common-cause correlates.
4. **Off-path priors.** Fix priors on the decision nodes not being intervened on. Use the fixed point of 6.2, or check that the answer does not depend on them.
5. **Evaluate.** For each $a$, compute $\mathbb E[V\mid do(\textsc{fdt}(P,G,x)=a)]$ **without** conditioning on $x$.
6. **Choose.** Take the argmax, breaking ties by a fixed rule.
7. **Sanity checks.**
   - If nothing besides the agent's own body depends on the fdt node, the answer should match CDT.
   - If a coordination problem among the agent's own instances appears, note that policy-FDT may disagree.

## 8. Conclusion

A-FDT is CDT with its surgical point moved. Instead of intervening on the physical act and conditioning on what has been seen, it intervenes on the output of its own decision procedure for the actual input. All downstream copies and models of that output are allowed to change with it, and the observation is used only to select which output is being chosen.

This one change produces the paper's results:

- one-boxing in Newcomb's problem;
- smoking in the smoking lesion;
- refusing both forms of blackmail;
- paying in Parfit's hitchhiker;
- staying put in Damascus.

The formula is fully explicit once $(P, G, x)$ is given. Its real content, and its main open problem, lies in $G$: the structure of subjunctive dependence, which the paper takes as given rather than derives. Several further details also need explicit commitments, namely the time-index of $P$, the priors on off-path decision nodes, tie-breaking, and the action/policy distinction. With those commitments made, A-FDT is a usable procedure for deciding new cases.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out what the essay should cover: A-FDT as the action-level version, built on Equation (4), which intervenes on fdt(P,G,x) and picks a single action. The footnoted policy-iterating formalization is a separate variant, so I'll keep it distinct from A-FDT.

I still need to pin down the word count, around 2400 to 3000 words, and to fit in the examples and the open questions. I'm also checking the arithmetic on the transparent Newcomb case, where the expected value comes to 10,010 + 990q rather than the typo'd figure.

I'm checking the arithmetic in the source's Newcomb figures, and the expected-value numbers don't quite line up with the stated values, so I'll note those as small discrepancies. I'm also sketching out a concrete recipe: list the decision-function nodes the model contains, work out which other nodes depend on each one, set priors on the nodes I'm not intervening on, and then intervene on fdt(P,G,x) to choose the action.

I'm now pinning down the open questions: how to construct the dependency graph G, which is the hardest part, and what priors to put on the fdt nodes I'm not intervening on. One option is to set those to fixed-point values by iterating A-FDT across observations until they're consistent. I'm also weighing whether P should be the agent's prior before seeing x, or already updated on it.

I'm weighing a case for the essay where two agents each see a different observation and must pick actions that coordinate, since holding the other nodes at their prior values might give a different answer than optimizing the whole policy jointly.

I'm now testing whether A-FDT can get stuck at a bad equilibrium: two copies, one shown L and one shown R, with payoff 2 for both choosing X, 1 for both choosing Y, and 0 for mismatches. I still need to check what happens when the other copy's prior q is set to 1/2.

I'm now testing a case where A-FDT settles on a bad outcome: if the other copy is treated as certain to pick Y, the agent seeing L also picks Y, which is self-consistent but worse than both choosing X. That fits the footnote's point that the policy-level version can do better in multi-agent coordination. I also want to run the transparent Newcomb, XOR blackmail, and mechanical blackmail examples with their numbers.

I'm checking the blackmail threshold for the mechanical case: with the stated 0.0009 error rate, refusing costs about 900 in expectation, which is less than the 1,000 paid, so refusing wins. The source's "0.011%" figure doesn't fit that conclusion, so it's probably a typo for 0.11%, and I'm noting the break-even as roughly 0.1%. Next is the XOR blackmail example.

I'm checking the XOR blackmail case with an infallible predictor. If Fiona pays, the letter arrives only when there are no termites, so the expected loss is p·1,000,000 plus (1−p)·1,000. If she refuses, the letter arrives only when there are termites, so the expected loss is just p·1,000,000, which means refusing comes out ahead by (1−p)·1,000. Next I'm turning to the Death in Damascus case, where A-FDT's Death node depends on fdt, and I need to see how that changes the intervention.

I'm laying out the essay's structure now: an introduction, the ingredients, the definition and how it compares to the earlier equations, worked examples, how observations are treated, open questions, a recipe, and a conclusion. I'm also planning to finish the twin and Death in Damascus cases, where both choices lead to the same fate and staying saves the 1,000.

I'm now planning the essay's remaining sections: the transparent Newcomb and XOR blackmail cases, the Death in Damascus case where both choices lead to the same fate, and a closing summary with references.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/fa5e76d6-ce77-4a22-a883-48181598b2ef/call_0/request.json)

[Authoritative raw response](../../../../../../runs/fa5e76d6-ce77-4a22-a883-48181598b2ef/call_0/response.raw) · finish: `stop`

### Visible response

````text
**A-FDT analysis**

1. **My decision node.** My observation history names me Rowan, the other prisoner Sasha, and includes my own lead about locker 17. Under Equation (4), I intervene on the node for that exact history, call it fdt(P, G, x_Rowan).

2. **The other copy's node.** The other execution receives different private observations: different names and a different lead. In the essay's framework (recipe step 2 and section 6.5), it therefore acts from a different node, fdt(P, G, x_Sasha). A-FDT holds that node at its prior rather than intervening on it jointly with mine. That joint intervention is what policy-FDT would do, and the essay explicitly separates the two theories.

3. **Evaluation for any prior q** that the other prisoner sends a letter:
   - **Keep quiet:** 2(1−q) + 5q = 2 + 3q years
   - **Send the letter:** 0(1−q) + 4q = 4q years

   Sending is better by 2 − q, which is at least 1 year for every q in [0, 1]. Sending strictly dominates.

4. **Reflective consistency (6.2).** The same reasoning applies symmetrically at the other node. The fixed point is therefore that both send, with q = 1, giving 4 years. Since the prior does not change the argmax, any prior gives the same answer.

5. **Sanity check (7).** This is the coordination trap the essay flags in 6.5: policy-FDT might pick mutual silence, at 2 years each. But I am instructed to use A-FDT as the essay interprets it, not policy-FDT.

**Final command:**

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how the decision applies under A-FDT: each copy has its own observations, so my node and the other copy's node are different, and the question is whether the other copy's act descends from mine.

I'm checking whether the other copy's act descends from mine, and since the observations differ by name and lead, it doesn't. Dominance then favors submitting regardless of the prior, so both copies end up submitting.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/fa5e76d6-ce77-4a22-a883-48181598b2ef/call_1/request.json)

[Authoritative raw response](../../../../../../runs/fa5e76d6-ce77-4a22-a883-48181598b2ef/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's A-FDT, I am choosing the output of one decision node: fdt(P, G, x), where x is my own observation history (Sasha, with the lead about Rowan). Rowan's copy runs the same function but on a different observation y: a different name and a different lead, so its letter would have different contents. That makes it a separate node, fdt(P, G, y), not a descendant of mine.

Section 6.5 of the essay covers exactly this case. A-FDT keeps the other observation-indexed node at its prior and optimises only its own output. It does not jointly optimise a policy; that is policy-FDT, which I am told not to substitute.

With Rowan's choice held fixed at whatever its prior is, sending the letter is better in both columns:

| Rowan's choice | Keep quiet | Send letter |
|---|---:|---:|
| Rowan keeps quiet | 2 years | 0 years |
| Rowan sends a letter | 5 years | 4 years |

Sending the letter strictly dominates, so the argmax is to submit. As the essay notes, policy-FDT might coordinate both copies on keeping quiet. But the assigned theory is A-FDT.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing how A-FDT applies here: each copy with a different observation runs a different decision node, and the intervention only touches my own node while the other stays at its prior, unless the other's node sits downstream of mine. I'm checking how the essay's section 6.5 illustrates copies that receive different observations.

Under A-FDT the other copy's node is separate from mine, so the intervention leaves it at its prior, and defecting comes out better whatever the other copy does. The essay's own treatment of different observations supports reading it that way, so I'm inclined to say submit, even though a policy-level reading might point toward cooperation.

```
