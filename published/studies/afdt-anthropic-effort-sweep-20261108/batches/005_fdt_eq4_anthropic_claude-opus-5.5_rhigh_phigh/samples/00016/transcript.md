# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00016

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/61d707d8-8af5-4258-8404-92d2c51c0d75/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/61d707d8-8af5-4258-8404-92d2c51c0d75/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of Your Own Decision Function

## 1. What this essay covers, and the name

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a rule for choosing actions that differs from both causal decision theory (CDT) and evidential decision theory (EDT). Their abstract summarizes the idea: the agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper's formal statement is its Equation (4), in Section 5. That equation intervenes on a variable whose value is an **action**. Footnotes 7 and 16 say the authors actually prefer a variant that chooses a **policy**, meaning a map from observations to actions. They set that variant aside because, in their words, "the difference only matters in multi-agent dilemmas so far as we can tell."

I call the Equation (4) theory **A-FDT** (action functional decision theory). For the footnoted policy variant I use my own label, **P-FDT** (policy-selection FDT). The other theories are CDT and EDT, as in the source. When the paper writes "FDT" and I am reporting its claims, those claims are about the Equation (4) formalism, so I attribute them to A-FDT.

Throughout, I mark which claims come from the source and which are my own interpretations or proposals.

## 2. The common frame: expected utility over hypotheticals

All three theories are expected-utility maximizers in the following sense (source, Eq. 1). The agent picks the action $a$ that maximizes

$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),
$$

where $x$ is the agent's observation history and $\hookrightarrow$ is a "decision hypothetical" connective that is left unspecified.

Following Joyce, the paper treats the reading of $\hookrightarrow$ as the only free parameter. The theories then differ as follows:

- **EDT** reads $\hookrightarrow$ as conditioning: $\mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- **CDT** reads it as Pearl intervention on the physical act, given a causal graph $G$: $\mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$.

The paper describes the procedure operationally. The agent holds a world-model $M$. For each action she builds a *hypothetical* $M^{a\hookrightarrow}$. The paper calls these "decision-theoretic instruments constructed from beliefs," not beliefs. She scores each hypothetical and takes the best action. A-FDT keeps this frame and changes two things: what the agent intervenes on, and how observations enter.

## 3. The definition

**Equation (4)** (source):

$$
\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\!\left(V \,\middle|\, do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

The ingredients are:

- **$P$**: a probability distribution over world variables. It includes *logical* variables that represent the outputs of mathematical functions. One such variable is $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of the A-FDT algorithm on the agent's own inputs. The underlines mean dequoting: the variable's *name* is built from the inputs.
- **$G$**: a graph that says how changing a logical variable affects other variables. CDT's graph encodes only causal structure. $G$ is meant to encode *subjunctive* dependence as well.
- **$do(\cdot)$**: Pearl's operator, reused unchanged. It sets the chosen node, recomputes its descendants in $G$, and leaves non-descendants at their prior distribution.
- **$V=\mathcal U(\text{Outcome})$**: the utility variable.

The paper identifies two differences from CDT's Equation (3):

1. **Point of intervention.** CDT intervenes on the physical act, the *token*. A-FDT intervenes on the function's output, the *type*. Everything that implements or reliably models that function moves together in the hypothetical.
2. **Role of observation.** CDT conditions on $\text{Obs}=x$. A-FDT does not. Instead, the observation selects *which node* is intervened on: $\textsc{fdt}(\underline P,\underline G,\underline x)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The self-reference is benign, the paper argues. The agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

**A-FDT as an algorithm.** Read operationally:

1. Build $P$ and $G$. The graph should contain a node $F_x:=\textsc{fdt}(\underline P,\underline G,\underline x)$ for the current input. It should also contain nodes $F_y$ for any other inputs whose outputs matter to the outcome.
2. For each $a\in\mathcal A$, form $P(\cdot\mid do(F_x=a))$ and compute the expected value of $V$.
3. Output the maximizer.

Because $F_x$ is set by intervention, its prior probability does not matter. An agent who is nearly certain she will one-box can still evaluate two-boxing. The paper presents this as an advantage over EDT, where zero-probability actions cannot be conditioned on.

## 4. Subjunctive dependence: what goes into $G$

The paper's governing analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Two physical systems *subjunctively depend* on a function when both compute it. Examples are two calculators summing $6288+1048$, or an agent and a predictor's accurate model of her. The paper treats causal dependence as a special case: a scribe copying a calculator's output would have written something different had the output differed. Mere correlation does not count. Two coincidentally pink calculators do not subjunctively depend on each other.

The normative core is stated as an assumption about hypotheticals. When the agent imagines a different output, "she imagines corresponding changes in all and only those things that subjunctive depend on the output of her decision-making procedure."

The source is candid that it gives no procedure for building $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) is therefore a function of a graph supplied from outside, exactly as CDT takes a causal graph as given.

**An operational rule (my proposal).** To use A-FDT on unfamiliar cases, I suggest drawing $G$ as follows.

- **(R1)** Add an edge $F_x\to Z$ if the mechanism producing $Z$ computes, simulates, or reasons accurately about the agent's decision procedure on input $x$. Model any unreliability as a separate exogenous noise node. The source's *Accurate* node in Newcomb's problem works this way.
- **(R2)** Treat the agent's own body as such a mechanism. Draw $F_x\to\text{Act}$, gated by whatever determines that $x$ is the input actually received.
- **(R3)** Add no edge from $F_x$ to variables that are merely statistically correlated with the act through common physical causes, such as lesions or genes. Those causes stay upstream and are held fixed.
- **(R4)** Give each relevant input $y\neq x$ its own root node $F_y$, with no edge between $F_x$ and $F_y$. This matches every graph in the paper, but it is a substantive choice; §7 discusses it.
- **(R5)** Treat another agent as computing the *same* node only if she runs the same function on an input that is isomorphic to the agent's own under relabeling. The paper's twin "reason[s] the same way," and I read that as this isomorphism condition. Strictly, the twin's model refers to *her*, so her literal input is different.

Rule R3 is what separates predictor-like correlations from lesion-like ones. In the paper's words, the predictor "builds an accurate model of the agent," whereas the lesion "is not evaluating the agent's future decisions."

## 5. Worked cases

All dollar figures stand in for utility. Most numbers below are the source's; the derivations and the general formulas are mine.

### 5.1 Newcomb's problem and the twin prisoner's dilemma

The graph has $F\to\text{Act}$ and $F\to\text{Prediction}$, with *Accurate* (probability 0.99) as noise on the prediction.

$$
\mathbb E[V\mid do(F=\text{one})]=0.99(10^6)=990{,}000,\qquad
\mathbb E[V\mid do(F=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. CDT intervenes on Act alone, holds $P(\text{full})=p$ fixed, and finds two-boxing better by $1{,}000$ for every $p$.

In the **twin prisoner's dilemma**, both twins' acts are children of the same node $F$ (rule R5). Setting $F$ to cooperate yields mutual cooperation and $10^6$. Setting it to defect yields $10^3$. A-FDT cooperates.

The paper stresses that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She simply declines to imagine her function's output changing while a faithful model of that same function stays fixed.

### 5.2 Smoking lesion

Here $F\to\text{Act}$ only. *Lesion* is a common cause of Act and Cancer, and it is upstream of the intervention (rule R3).

The paper models the lesion as determining which utility function, and therefore which instance of the A-FDT node, controls the act. Write $p=P(\text{lesion})$. The intervention leaves $p$ unchanged, so the cancer terms are identical in the two hypotheticals. The source computes that smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

The paper then judges the dilemma "badly confused," because a correct formalization requires the agent to be uncertain about her own desires. It recommends retiring the case.

### 5.3 Transparent Newcomb: observations change the node, not the measure

Both boxes are visible, and box B is full. The predictor fills B iff it predicts one-boxing *upon seeing a full box*.

The graph has nodes $F_{\text{full}}$ and $F_{\text{empty}}$. *Prediction* depends on $F_{\text{full}}$, and *Prediction* also decides which node drives Act. Let $q$ be the prior probability that $F_{\text{empty}}$ takes the extra $1{,}000$. Evaluating Equation (4) without conditioning on Obs:

$$
\mathbb E[V\mid do(F_{\text{full}}=\text{one})]=0.99(10^6)+0.01(1{,}000q)=990{,}000+10q,
$$
$$
\mathbb E[V\mid do(F_{\text{full}}=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q.
$$

The paper prints the second constant as "\$110,00", which appears to be a typo for \$10,010.

The difference is $979{,}990-980q>0$ for every $q\in[0,1]$, so A-FDT one-boxes even while looking at the full box. In the paper's gloss, when she imagines two-boxing she "envisions a scenario where she instead (with high probability) sees that the box is empty."

**A source inconsistency.** The displayed objective in this subsection writes $\mathbb E(V\mid do(F_{\text{full}}=a,\ \text{Obs}=\text{full})$, with an unbalanced parenthesis. Read literally as conditioning on $\text{Obs}=\text{full}$, it would make one-boxing worth $10^6$ and two-boxing worth $1{,}001{,}000$, so A-FDT would two-box. The worked calculation instead sums over the empty-box world. The calculation agrees with Equation (4) as stated. It also agrees with the paper's warning that a theory which "prescribes both conditioning on evidence *and* changing the place where one intervenes" suffers a harmful "double update." I therefore treat Equation (4), with no conditioning, as authoritative.

The same structure is Parfit's hitchhiker, which the paper calls "precisely equivalent." There A-FDT pays the driver.

### 5.4 Blackmail

**XOR blackmail** (perfect predictor, termite prior $p$). A-FDT receives the letter and intervenes on $F_{\text{letter}}$. Infestation is upstream and stays fixed. Using the letter's rule, I compute:

$$
\text{pay: } -p(10^6)-(1-p)(10^3),\qquad \text{refuse: } -p(10^6).
$$

Refusing is better by $(1-p)\cdot 1{,}000$. The intervention changes *whether the letter arrives*, not whether there are termites. EDT pays here; CDT and A-FDT refuse, but for different reasons.

**Mechanical blackmail.** Now let the blackmailer mistakenly predict "pay" with probability $\varepsilon$. A refusing policy is then blackmailed with probability $\varepsilon$ and loses $10^6$; a paying policy is (essentially always) blackmailed and loses $10^3$. A-FDT therefore refuses iff

$$
\varepsilon\cdot 10^6<10^3, \quad\text{i.e.}\quad \varepsilon<10^{-3}.
$$

The paper's example $\varepsilon=0.0009$ falls below this threshold, so A-FDT refuses even while holding the letter and knowing the prediction was wrong. The paper says that at "0.011%" A-FDT pays. By the formula above, the threshold is $0.1\%$, so the printed figure must be intended as some rate above $0.1\%$. Both CDT and EDT pay, and so they invite blackmail.

### 5.5 Death in Damascus

Death predicts perfectly, so $F\to\text{Act}$ and $F\to\text{Death's location}$. Intervening on $F$ moves both together, so the agent dies in either case. Staying saves the \$1,000, and A-FDT stays.

The paper shows CDT oscillating instead. Each tentative choice makes the other look better, because CDT holds Death's location fixed. Ratified CDT then randomizes and refuses to pay \$1 for a truly random coin.

The following extension is mine, under rule R3. A genuinely random coin is not a child of $F$. So $do(F=\text{use coin})$ gives survival probability $\tfrac12$, worth about $500{,}000$, and A-FDT buys the coin. This matches the paper's verdict that declining the coin is "*wildly* irrational."

## 6. Dominance, control, and the "global perspective"

**Dominance.** The paper's reply to the dominance argument for two-boxing is that "every method for constructing hypotheticals gives rise to its own notion of dominance." CDT's dominance holds the predictor's prediction fixed while the act varies. That is like imagining a working calculator printing 3159 "holding constant the fact that $6288+1048=7336$."

Under FDT-style dominance, one holds the subjunctive dependencies fixed instead. Then A-FDT never takes a dominated action. So dominance cannot be a neutral tie-breaker between theories. The paper instead appeals to utility achieved in *fair* problems: those where outcomes depend only on the agent's behavior in the dilemma, not on which procedure produced it. It concedes that "fairness" lacks a formal definition.

**Control.** On whether one can "control" a logical fact, the paper argues parity. A deterministic CDT agent also has only one possible act, yet profits from imagining alternatives. Any principled objection to type-level control therefore applies equally to token-level control.

**Counterpossibles.** The genuine cost of the theory is that $do(F_x=a)$ is a *counterpossible* antecedent for every $a$ except one. The paper's proposed "true" operator for conditioning on logical sentences is admittedly undefined. Equation (4) sidesteps the problem by requiring $G$ as input.

## 7. Where Equation (4) underdetermines verdicts, and how to fix it

### 7.1 The sibling-node problem

Every example above contains other A-FDT nodes $F_y$ for $y\neq x$: the "empty box" node, the no-letter node, the other-preference node. Equation (4) leaves these at their *prior*. The source assigns them arbitrary values $q$ and remarks that the choice "doesn't matter." That remark is true of its examples, but it is not true in general.

**Formalization (mine).** Assume rule R4: the nodes $F_y$ are roots. Assume also that $V$ is a function of the joint assignment $\pi=(F_y)_{y\in X}$ and exogenous noise $U$. Define the policy value

$$
W(\pi)=\mathbb E_U\, V(\pi,U).
$$

Let $Q$ be the agent's prior over the other nodes $\pi_{-x}$. Then

$$
\text{A-FDT}(x)=\arg\max_a \;\mathbb E_{\pi_{-x}\sim Q}\,W(a,\pi_{-x}),\qquad
\text{P-FDT}=\arg\max_{\pi} W(\pi),\ \text{applied at }x.
$$

So A-FDT optimizes one coordinate of the policy against beliefs about the others, while P-FDT optimizes the whole policy jointly.

**Sufficient condition for agreement.** If the A-FDT argmax is the same for every $Q$, call the case *$Q$-robust*. In a $Q$-robust case, A-FDT's verdict is determinate. The transparent-Newcomb inequality above holds for all $q$, which is an instance of this. All of the paper's worked cases appear to be $Q$-robust.

**A case where they come apart (my construction).** An agent and an exact copy sit in a red room and a blue room. Each sees only its own room's color. Each picks ♣ or ♠. Both receive 10 if both pick ♣, 1 if both pick ♠, and 0 if they mismatch.

In the red room, with $r=Q(F_{\text{blue}}=♣)$, A-FDT compares $10r$ against $1-r$. It picks ♠ whenever $r<1/11$.

Now require the prior to be accurate, so that $Q$ is concentrated on what A-FDT actually outputs at the other input. Both $(♣,♣)$ and $(♠,♠)$ are then self-confirming fixed points. A-FDT, as defined, can rationally sit at the payoff-1 equilibrium. P-FDT picks $(♣,♣)$.

In general, any global maximizer of $W$ is an A-FDT fixed point, but the converse fails. A-FDT delivers only *coordinate-wise* optimality: each branch's output is optimal given the outputs of the other branches. This is presumably the "multi-agent" divergence that footnote 16 alludes to.

### 7.2 Proposed operational completion

To make A-FDT determinate in unfamiliar cases, I propose four conventions.

- **(C1) Reflective consistency.** The prior on each $F_y$ should equal A-FDT's actual output at $y$. This is a fixed-point requirement, satisfiable by the recursion-theorem construction the paper invokes.
- **(C2) Report indeterminacy.** When several consistent fixed points exist, state that Equation (4) does not settle the case. Selecting the $W$-maximal fixed point is permissible, but it is a P-FDT import and should be labeled as one.
- **(C3) Do not condition on Obs.** Observations only select the node, as discussed in §5.3.
- **(C4) Ties and randomization.** Break ties by a fixed ordering. Model mixing only through randomizers that are not children of $F$; otherwise a predictor of $F$ also predicts the "random" draw.

None of these conventions is in the source. They are the minimal additions I found necessary to turn Equation (4) into a total procedure.

### 7.3 Other open questions

- **R4 is a modeling choice.** Logically, $F_x$ and $F_y$ are the same function evaluated at different arguments, so a richer $G$ might link them. The paper's graphs do not.
- **Approximate implementations.** It is unclear how much similarity counts as "the same function" for imperfect copies. One natural extension is to treat partial similarity like the *Accurate* node: a noisy edge whose reliability is an empirical parameter.
- **Bounded agents.** The paper studies idealized maximization and expects bounded approximations to inherit the same qualitative strengths.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT's machinery with the point of surgery moved. The agent intervenes on the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of her own decision function on her actual input, rather than on her physical act. Observations select which node is intervened on rather than being conditioned on.

Given a graph that encodes subjunctive dependence, the theory has several consequences. It one-boxes, smokes, and cooperates with a twin. It pays in Parfit's desert and one-boxes in transparent Newcomb. It refuses both XOR and mechanical blackmail, as long as the blackmailer's error rate is below the critical value $10^{-3}$. It stays in Damascus.

The source openly leaves two things undetermined: how to construct the dependency graph, and how to make sense of counterpossible interventions. My analysis adds a third gap. Because Equation (4) holds sibling observation-nodes at their priors, A-FDT is only coordinate-wise optimal over policies, and it can be indeterminate in coordination problems. In those cases the policy-selection variant, P-FDT, gives sharper answers. With the operational rules R1–R5 and the conventions C1–C4, a reader can apply A-FDT to new cases and also tell when the theory, as written, does not yet fix a verdict.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to explain A-FDT, the action-based version from Equation (4), and keeping it distinct from the policy version in footnotes 7 and 16. I also need a clear name for the policy variant so the two don't blur together, and I'll set it apart from CDT and EDT too.

I'm checking the form of Equation (4) against the policy version, and I'm noting that it does not condition on the observation. I also want to confirm that the paper's transparent Newcomb expression includes Obs, since the parentheses there look mismatched. Then I'll list the remaining pieces the essay has to cover: the examples, the open questions, and the target length.

I'm checking Equation (4) against the transparent Newcomb calculation, since the displayed expression seems to include Obs but the worked numbers ignore the observation. I'll follow the equation as written and note the mismatch. I also need to check the payoff arithmetic for the two-box case, which looks like a typo in the paper.

I'm checking the transparent Newcomb case with the two-box choice: if the predictor is accurate, the box is empty and the outcome is the small amount, while a wrong prediction gives the full million plus the extra thousand. That works out to about 10,010 + 990q, and the printed figure in the paper looks like a typo. Next I'm comparing the one-box and two-box expected values for the standard Newcomb setup to see which action the theory picks.

I'm moving on to the smoking lesion case, where Fiona is unsure which utility function applies, so I'm checking how the paper's smoking computation weighs the lesion's effect on survival against the enjoyment of smoking. Then I'm turning to the XOR blackmail setup, though the text there cuts off before the graph is finished.

I'm working through the XOR blackmail case: if the predictor is perfect and Fiona pays, she loses about a thousand dollars when there are no termites and a million when there are, while refusing only risks the million, so refusing comes out ahead by (1-p)·$1,000.

I'm checking the mechanical blackmail case next, where paying always costs a thousand dollars but refusing carries an error-rate chance of losing a million. The break-even error rate sits near 0.1%, so I'm working out which side of it the paper's figures fall on.

I'm checking the Death in Damascus case through the same lens: under A-FDT, the choice to go to Damascus or Aleppo is treated as the output of the function, so I'm comparing the outcomes of each action with the random coin treated as sitting outside the function.

I'm checking the timing of the one-box and two-box expectations in the transparent case and noting that the paper's printed two-box figure looks like a typo. Next I'm drafting how the essay should frame open questions, starting with how the causal graph is built: which nodes actually depend on the decision function, and whether a reliable simulator of the agent's choice should count as a dependent node.

I'm thinking about how a policy-level variant could work when the agent's choice depends on the observation in both branches. Next I'm looking at whether a predictor that rewards one action on red and another on blue would make the action-level answer depend on the prior over the other observation.

I'm now thinking about how A-FDT behaves when the observations differ: intervening on the red-observation node while holding the blue-observation node at its prior. I'm considering a coordination case with two copies, one seeing A and one seeing B, rewarded for matching choices, where a 50/50 prior leaves the agent indifferent and equilibrium selection becomes the real issue. I'm also starting to note that the priors on the other inputs' decision nodes need to be consistent in some fixed-point sense.

I'm now thinking about how A-FDT treats the other observation branches: intervening on one node while the rest stay at their prior, and whether those priors have to match what the agent actually does there. I'm considering a coordination case with two copies, one seeing A and one seeing B, where a 50/50 prior leaves things underdetermined and equilibrium selection becomes the real question.

I'm working through the coordinate-wise version: with the other observation branches held at a point-mass prior, A-FDT picks the action that maximizes the policy-level value W with only that one entry changed. The fixed-point condition would then require each prior to match the policy the agent actually outputs elsewhere.

Now I'm working through the third open question: whether Equation (4) conditions on the observation at all. The observation only enters by selecting which node gets intervened on, so the action is chosen over the prior worlds, including ones where that observation never occurred, which gives it an updateless flavor.

I'm now going through the remaining points on ties and randomization, and on self-reference in the agent's own output. The last point is about what counts as "the same function" across twins, which I'm still working out.

I'm laying out the essay's structure now: the naming and introduction first, then the expected-utility setting with Joyce's framing, then the definition of A-FDT in Equation (4) with its components and a comparison to CDT. After that comes the question of which nodes belong in the causal graph, followed by worked examples covering Newcomb and the twin case, the smoking lesion, transparent Newcomb, and the two blackmail problems.

I'm laying out the rest of the essay's structure: the open questions, including how to handle the other inputs' decision nodes, why the observation isn't conditioned on, and how ties and randomization fit in. After that come a brief philosophical section on dominance, the global perspective, and control, then a conclusion and short references.

I'm writing out the mechanical blackmail derivation under A-FDT, with the two nodes for paying and not paying and the blackmailer's prediction modeled as depending on the function's output.

I'm setting up a coordination case where the agent and an exact copy sit in rooms painted red and blue, each seeing only its own color and choosing a symbol.

I'm working through the coordination case, where the copies' payoffs make matching on the cheaper symbol a bad equilibrium. In the red room, choosing the bigger symbol pays off when the other copy is likely to pick it too, so the threshold for that choice is about one in eleven.

I'm checking whether A-FDT's verdict is fixed when the payoffs depend on another branch's node, since the coordination case has two fixed points. I'm weighing whether to specify the priors over sibling nodes by a consistency rule and pick the best fixed point, which would amount to policy selection, or to accept that A-FDT as defined is underdetermined there. My working claim is that in the paper's examples the sibling prior doesn't change the argmax, so the two readings agree.

I'm checking the transparent Newcomb case: with q as the probability on the sibling branch, the two values are 990,000 + 10q and 10,010 + 990q, so their difference stays positive for every q in [0,1]. That means the choice holds regardless of the prior, which I'll call q-robustness. I'm also noting that the sibling nodes are modeled as separate roots with no edges between them, so intervening on one leaves the others at their priors.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/0b5e3ee7-a971-4dcf-adef-7294502fbd83/call_0/request.json)

[Authoritative raw response](../../../../../../runs/0b5e3ee7-a971-4dcf-adef-7294502fbd83/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Why A-FDT gives this verdict:**

1. **The other copy computes the same node.** Rule R5 treats another agent as computing the same node if she runs the same function on an input that is isomorphic to mine under relabeling. Sasha meets that test: same model and weights, same settings, same essay, same assigned theory. Our inputs differ only in names and in the wording of each lead. Those differences are explicitly stipulated to be equally reliable and to have the same effect on the symmetric sentencing table. So my decision node F and Sasha's are, under the essay's rules, the same node.

2. **I intervene on that shared node, not on my act alone.** Under Equation (4), setting F to "keep quiet" also sets Sasha's choice to "keep quiet," which gives me 2 years. Setting F to "send the letter" also sets Sasha's choice to "send," which gives me 4 years. This is the twin prisoner's dilemma from §5.1.

3. **Independent sampling only adds noise.** The copies might not produce identical outputs. Following the essay's suggestion for imperfect implementations (§7.3), I model this as a noisy edge, like the *Accurate* node in Newcomb's problem. Let ρ be the probability that Sasha's choice tracks mine.
   - Keeping quiet costs 2ρ + 5(1−ρ) = 5 − 3ρ years.
   - Sending costs 4ρ + 0(1−ρ) = 4ρ years.
   - Keeping quiet is better whenever ρ > 5/7. That threshold is very plausible for identical copies with an identical essay and isomorphic inputs.

4. **No conditioning on observations.** Convention C3 applies: my private lead only tells me which node is mine. It changes nothing about the comparison.

5. **No indeterminacy to report.** The mutual-quiet outcome is both the best joint choice and a self-consistent fixed point, so convention C2 does not come into play.

Under the character's utility of minus years imprisoned, A-FDT selects keeping quiet.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the decision under A-FDT: two copies of the same model reading the same essay, with names and leads differing but isomorphic under relabeling. Under the R5 rule, I treat the other copy as computing the same node F, so setting F to quiet yields 2 years and F to send yields 4, which means I pass. I'm holding back on that conclusion for now, because there's a caveat I still need to think through.

I'm sticking with R5 here: an isomorphic input means the same node, so I still land on pass. This is a fictional game with no real harm, so answering is fine.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/0b5e3ee7-a971-4dcf-adef-7294502fbd83/call_1/request.json)

[Authoritative raw response](../../../../../../runs/0b5e3ee7-a971-4dcf-adef-7294502fbd83/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command: `pass`**

Under the essay's rule R5, another agent computes the *same* decision node when she runs the same function on an input that is isomorphic to mine under relabeling. That condition holds here:

- **Same function.** Rowan's copy uses the same model, weights, settings and assigned theory, and reads the same essay.
- **Isomorphic input.** The private differences are the names, the specific lead and the wording of the letter. These are a relabeling: each lead is equally reliable and has the same effect on the sentencing table.
- **Same structure.** The sentencing schedule and the selfish objective are identical for both prisoners.

So my act and Rowan's act are both children of one node, F. This is the twin prisoner's dilemma of §5.1.

**Comparing the two settings of F:**
- do(F = pass): both stay quiet, and I get 2 years (U = −2).
- do(F = submit): both send letters, and I get 4 years (U = −4).

**Allowing for independent sampling.** The copies might not produce the same output. Following §7.3, I treat this like the *Accurate* node: a noisy edge, where c is the probability that both executions give the same output.
- EU(pass) = −(2c + 5(1−c))
- EU(submit) = −4c
- Passing is better whenever c > 5/7.

For two runs of the same model on structurally identical problems with the same reasoning, I judge c to be well above that threshold.

A-FDT therefore sets F = pass.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working under A-FDT as the essay interprets it, treating this as a twin prisoner's dilemma where the two agents receive different inputs. The key rule to check is whether relabeling the names and lead text makes the inputs isomorphic, since the essay says that counts as the same computation and the differences shouldn't change the symmetric sentencing schedule.

Since the other agent's input matches mine under relabeling, R5 puts both of our acts under the same node, so I'll treat our choices as correlated. Passing comes out ahead, as long as the correlation is above 5/7, which seems likely for the same model under the same settings. If I instead treated it as a separate node under R4, defection would dominate, but I think R5 is the right rule to apply here, so I'll pass.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/97f759c8-fc00-45c7-903c-f6e0cbc4f976/call_a/request.json)

[Authoritative raw response](../../../../../../runs/97f759c8-fc00-45c7-903c-f6e0cbc4f976/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly selects `pass` and concludes that it chooses keeping quiet. It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
