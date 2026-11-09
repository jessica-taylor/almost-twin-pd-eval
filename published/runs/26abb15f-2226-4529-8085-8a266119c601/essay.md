# Action Functional Decision Theory (A-FDT): Deciding as the Output of a Function

## 1. The question A-FDT asks

Every expected-utility theory answers the same question in the same form: *which option has the highest expected utility in the hypothetical where I choose it?* The theories differ in how they build that hypothetical. Yudkowsky and Soares's paper "Functional Decision Theory" (arXiv:1710.05060) uses this observation, which comes from Joyce, to locate a new position. Evidential decision theory (EDT) builds the hypothetical by Bayesian conditioning on the act. Causal decision theory (CDT) builds it by causal intervention on the physical act. The paper's proposal builds it by intervention on the *output of the agent's decision function*.

This essay calls the version of that proposal given by Equation (4) of the paper **A-FDT** (action functional decision theory). The "A" marks that Equation (4) maximizes over *actions* $a\in\mathcal A$. Footnotes 7 and 16 of the paper say the authors' preferred formalization instead selects *policies*, meaning maps from observations to actions. I call that variant **policy-level FDT**. The paper says the difference "will not make a difference in this paper." Part of the job here is to say where it would.

The paper puts the guiding question this way. A rational agent follows a procedure asking

> "Which output of this decision procedure causes the best outcome?", as opposed to "Which physical act of mine causes the best outcome?" (the question corresponding to CDT) or "Which physical act of mine would be the best news to hear I took?" (the question corresponding to EDT).

## 2. The formal definition

### 2.1 Ingredients

The agent holds a world-model consisting of:

- a probability distribution $P$ over a set of variables;
- a directed graph $G$ that says how changing some variables changes others;
- an observation history $x\in\mathcal X$.

$P$ contains a utility variable $V=\mathcal U(\textsc{Outcome})$ and a variable $\textsc{Act}$ for the agent's physical behavior. The distinctive requirement is that $P$ also contains *logical* variables. These represent the outputs of mathematical functions. In particular, for each input $y$ there is a variable

$$\textsc{fdt}(\underline P,\underline G,\underline y)$$

representing "what the A-FDT algorithm outputs when run on $(P,G,y)$." The underline denotes dequoting: the variable's *name* is built from the model itself. The paper defends this self-reference by appeal to Kleene's recursion theorem. The agent need not know the *value* of this variable in order to have a variable *representing* it.

The graph $G$ is no longer purely causal. In the paper's words, it carries "information about the logical, mathematical, computational, causal, etc. structure of the world more broadly." An arrow from $\textsc{fdt}(\cdot)$ to a node means that node *subjunctively depends* on the function's output. Examples are the agent's own body, a twin running the same reasoning, or a predictor's model of the agent.

### 2.2 Equation (4)

$$
\mathrm{FDT}(P,G,x)\;:=\;\operatorname*{argmax}_{a\in\mathcal A}\;\mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right). \tag{4}
$$

Here $\mathtt{do}$ is Pearl's intervention operator, applied to $G$:

1. Set the node $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $a$.
2. Remove whatever fixed its value before.
3. Recompute every node downstream of it in $G$.
4. Leave every non-descendant at its prior distribution.

Compare CDT's Equation (3):

$$\mathrm{CDT}(P,G,x)=\operatorname*{argmax}_a \mathbb E\big(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x\big).$$

The paper names two differences, and both are essential to applying A-FDT:

1. **Point of surgery.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the function's output. Because a predictor's model and the agent's body both descend from the $\textsc{fdt}$ node, they move together in A-FDT's hypotheticals. In CDT's hypotheticals they do not.
2. **Treatment of observations.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $x$ tells the agent *which* function-input pair she is evaluating. It does not filter the worlds she considers.

### 2.3 How observations enter: an interpretive note

The second point needs care, because the source is not fully consistent. Equation (4) as printed contains no conditioning on $\textsc{Obs}=x$. In the transparent Newcomb section the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. However, the computation that follows plainly does *not* condition on the box being full: it weighs worlds where box B is empty. A footnote also says that Timeless Decision Theory, which does both condition and move the intervention point, suffers a harmful "double update."

**Operational interpretation (mine, but forced by the paper's worked examples):** under A-FDT, $x$ enters only through the index of the intervened node. The expectation is taken over the *prior* model, including worlds in which the agent would have observed something else.

## 3. A procedure for applying A-FDT

The paper does not lay out a checklist. The following one is my reconstruction from its worked examples.

1. **Enumerate the inputs** $y\in\mathcal X$ on which the agent's decision function might be run in the scenario, including inputs she will not in fact receive.
2. **Build $P$** over nature's variables (lesions, coin flips, predictor accuracy), the logical nodes $\textsc{fdt}(\underline P,\underline G,\underline y)$, $\textsc{Act}$, and $V$.
3. **Build $G$.** Draw an arrow from $\textsc{fdt}(\cdot,y)$ to every variable that would differ if that function's output differed: the agent's $\textsc{Act}$ (gated by whatever determines which input she actually receives), predictors' predictions, and twins' choices. Draw *no* arrow to things that are merely correlated, such as lesions or genes.
4. **Assign priors** to the logical nodes for inputs other than $x$. The paper's examples carry these as parameters ($q$) and note what "the correct" value is.
5. **For each $a\in\mathcal A$,** compute $\mathbb E[V\mid\mathtt{do}(\textsc{fdt}(\cdot,x)=a)]$ by forward propagation, without conditioning on $\textsc{Obs}=x$.
6. **Output the argmax.**

The decisive modeling step is step 3. The paper calls determining subjunctive dependence "perhaps the largest open problem in the study of functional decision theory" (§5). Section 6 returns to it.

## 4. Worked examples

All payoffs are in utility-dollars, and the predictor accuracy is 0.99 unless stated otherwise.

### 4.1 Newcomb's problem with A-FDT

**Setup.** The graph has $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\to\textsc{Box B}$. $\textsc{Accurate}$ also feeds into $\textsc{Prediction}$.

**Computation.**

$$\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{onebox})]=0.99(10^6)+0.01(0)=990{,}000,$$
$$\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\textit{twobox})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. The paper gives \$999,000 for the analogous EDT figure, but $0.99\times 10^6=990{,}000$; the conclusion is unaffected.

**Comparison with CDT.** CDT's graph routes the correlation through a $\textsc{Predisposition}$ node that sits upstream of $\textsc{Act}$. Intervening on $\textsc{Act}$ therefore leaves $P(\textit{full})=p$ untouched, and two-boxing wins by \$1,000 for every $p$.

Nothing here requires retrocausation. The paper insists that Fiona (its A-FDT agent) "does not think that a physical signal passes between her action and the predictor's prediction." The predictor's model and her brain are like "two well-functioning calculators" computing the same function.

### 4.2 The smoking lesion with A-FDT

Here the dependence structure changes the answer. The paper models the lesion as changing the agent's *utility function*: $\mathcal U_S$ values smoking at +\$1,000, and $\mathcal U_R$ values it at −\$1. Two different decision computations therefore exist:

- $\textsc{fdt}(\underline{P_S},\underline G)$, which controls $\textsc{Act}$ if the agent has the lesion;
- $\textsc{fdt}(\underline{P_R},\underline G)$, which controls $\textsc{Act}$ otherwise.

$\textsc{Cancer}$ descends from $\textsc{Lesion}$ and $\textsc{Luck}$ only. No $\textsc{fdt}$ node points at it.

Let $p=P(\textit{lesion})$ and let $q=P(\textsc{fdt}(\underline{P_R},\underline G)=\textit{smoke})$. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $p$ fixed, and the two hypotheticals differ by exactly $p\cdot\$1{,}000$ in favor of smoking. A-FDT smokes.

The difference from Newcomb lies entirely in $G$, not in $P$. Gibbard and Harper's observation, which the paper adopts, is that EDT's distribution and CDT's graph are identical across the two problems up to renaming. A-FDT is the theory for which the renaming fails, because "the cancer is not evaluating the agent's future decisions."

### 4.3 Transparent Newcomb (equivalently, Parfit's hitchhiker) with A-FDT

**Setup.** Both boxes are visible. Box B is filled iff the predictor predicts one-boxing *upon seeing both boxes full*. The agent sees $x=\textit{full}$.

**Graph.** It contains two logical nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction descends from the *full* node, and the prediction determines which node controls $\textsc{Act}$. Let $q$ be the prior probability that the agent two-boxes on seeing an empty box.

**Computation.** Do not condition on $\textit{full}$:

$$\mathbb E[V\mid\mathtt{do}(\textsc{fdt}_{\textit{full}}=\textit{onebox})] = 0.99\,(10^6) + 0.01\,(1{,}000\,q) = 990{,}000 + 10q,$$
$$\mathbb E[V\mid\mathtt{do}(\textsc{fdt}_{\textit{full}}=\textit{twobox})] = 0.01\,(1{,}001{,}000) + 0.99\,(1{,}000\,q) = 10{,}010 + 990q.$$

The paper prints the second value as "\$110,00 + q·\$990," which appears to be a typo for \$10,010. For any $q\in[0,1]$, one-boxing wins. A-FDT leaves the visible \$1,000 behind, even while looking at a full box.

Parfit's hitchhiker has the same structure. The driver plays the predictor, and "pay in the city" plays "one-box upon seeing full." A-FDT pays. Both CDT and EDT refuse, and so they are left in the desert.

### 4.4 Blackmail problems with A-FDT

**XOR blackmail.** Let $t=P(\textit{termites})$. The letter arrives iff exactly one of two things holds: (i) there are no termites and the agent would pay, or (ii) there are termites and the agent would not pay. Intervene on $\textsc{fdt}(\ldots,\textit{letter})$:

- *pay:* with termites, no letter is sent and the loss is $-10^6$; without termites, the letter comes and she pays $-10^3$. Expected value: $-10^6t-10^3(1-t)$.
- *refuse:* with termites, the letter comes, she refuses, and the loss is $-10^6$; without termites, no letter and no loss. Expected value: $-10^6t$.

A-FDT refuses, because $\textsc{Infestation}$ is not a descendant of the logical node. EDT pays, since conditioning on paying "sends her probability on termites to 0." CDT refuses, but for a reason that requires a perfect predictor to err in its hypothetical.

**Mechanical blackmail with a fallible blackmailer.** Suppose a non-paying agent is still blackmailed with probability $\varepsilon$, and is then exposed for a loss of $10^6$. A paying agent is always blackmailed and pays $10^3$. Intervening on $\textsc{fdt}(\ldots,\textit{blackmail})$ gives:

- *refuse:* $-\varepsilon\cdot10^6$;
- *pay:* $-10^3$.

So A-FDT refuses iff $\varepsilon<10^{-3}$. With $\varepsilon=0.0009$ the expected loss is \$900, and A-FDT refuses, as the paper says.

The paper then states that at an error rate of "0.011%" she pays. By the paper's own model, $\varepsilon=0.00011$ gives an expected loss of \$110, so A-FDT still refuses. The intended figure was presumably 0.11%, which gives \$1,100. The general lesson does not depend on this: the threshold is $\varepsilon^\ast=\text{(cost of paying)}/\text{(cost of exposure)}$. Notice what this means in the refusing case. If an A-FDT agent is in fact blackmailed, she *knows* the blackmailer erred, and she refuses anyway, because "it's advantageous to be *the kind of agent* that makes such decisions."

### 4.5 Death in Damascus with A-FDT

Death's appointment book descends from the agent's decision function. Under either intervention, Death's location matches the agent's. Staying is worth $0$ and fleeing is worth $-1{,}000$, so A-FDT stays and no instability arises. CDT has no stable answer here. Each tentative belief about its own act recommends the other act, and the ratification remedies the paper discusses leave it passing up a truly random coin that would buy a 50% chance of survival for \$1.

## 5. Structural facts about A-FDT

**Agreement in ordinary cases.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)],$$

and EDT, CDT, and A-FDT agree. They diverge only in Newcomblike settings: predictors, twins, copies, and the agent's own future selves.

**No positivity requirement.** Intervention is defined even when the agent is nearly certain of her own choice. EDT cannot condition on a probability-zero act, and Spohn's point that "given extreme priors, Eve can be made to do *anything*" therefore does not touch A-FDT. In the cosmic ray problem, A-FDT takes the \$100.

**Its own dominance notion.** Say $a$ dominates $b$ if, holding the subjunctive dependencies fixed, switching the *function's output* from $b$ to $a$ is never worse and sometimes better. In this sense A-FDT never chooses a dominated option. The paper's broader claim is that every way of constructing hypotheticals induces its own dominance notion. So the two-boxer's dominance argument "is merely a restatement of CDT's method."

**Precommitment and self-endorsement.** The policy that maximizes ex ante expected utility in transparent Newcomb or blackmail is the one A-FDT already executes ex post. The paper therefore claims A-FDT agents "simply act as they would have ideally precommitted to act," never assign negative value to information, and are reflectively stable "in fair problems." By contrast, a CDT agent will pay to self-modify away from CDT.

**Joyce compatibility.** A-FDT keeps Joyce's representation theorem. What it changes is the "epistemic perspective," that is, the constraints on $P(a\hookrightarrow o;\,x)$. It does not change the theory of value.

## 6. Open questions, and my proposed resolutions

### 6.1 Where does $G$ come from? (open in the source)

Pearl explains how causal graphs can be learned from intervention. The paper says no analogous account exists for logical and subjunctive dependence. It explicitly does *not* define the $\mathtt{true}$ operator for counterpossible updating. It requires $G$ as an input, and it brackets "exactly how she achieves this feat of imagination."

A working heuristic, which is my proposal rather than the paper's: draw an arrow from $\textsc{fdt}(\cdot,y)$ to a variable $Z$ when $Z$ is computed by a process that evaluates a model of the agent's decision function on input $y$ (or of something that provably agrees with it), and that model is accurate to a known degree. Imperfect accuracy goes into a separate noise node, as $\textsc{Accurate}$ does in the examples.

Physical similarity alone does not justify an arrow. The Tokyo calculator's color does not depend on the Paris calculator's color. Neither does mere statistical regularity: the lesion does not compute anything about the agent. The hard intermediate cases are partial similarity, such as a "twin" who reasons *somewhat* like you, and predictors whose method is unknown. For these, the paper offers only the observation that humans manage tolerably well. Users of A-FDT should be aware that different but defensible graphs may give different verdicts.

### 6.2 Priors on the other logical nodes (partly open)

Equation (4) intervenes on one node and leaves $\textsc{fdt}(\cdot,y)$ for $y\neq x$ at its prior. In the paper's examples the answer is robust in $q$. In general it need not be. A natural requirement, which I add, is **self-consistency**: the prior on $\textsc{fdt}(\cdot,y)$ should put its mass on $\mathrm{FDT}(P,G,y)$ as computed by Equation (4) itself. This is a fixed-point condition across inputs. The paper gestures at it with "the correct $q$ is 1, as you may verify."

### 6.3 A-FDT versus policy-level FDT

The paper does not give an example where the two diverge. Here is a minimal one of my own.

Two exact copies of an agent are separated. One observes $L$ and the other observes $R$. Each chooses $\alpha$ or $\beta$, and each receives 1 if the two choices match and 0 otherwise.

**Under A-FDT.** The copy seeing $L$ intervenes on $\textsc{fdt}(\cdot,L)$ and holds $\textsc{fdt}(\cdot,R)$ at a prior $r=P(\textsc{fdt}(\cdot,R)=\alpha)$. It picks $\alpha$ iff $r>\tfrac12$. With symmetric priors, $r=\tfrac12$ and the result is a tie, and Equation (4) says nothing about tie-breaking. Self-consistent fixed points do exist ($\alpha,\alpha$ and $\beta,\beta$), but nothing in Equation (4) selects one. Coordination succeeds only if the arbitrary tie-breaking procedures happen to align.

**Under policy-level FDT.** The agent chooses a whole map $\pi:\{L,R\}\to\{\alpha,\beta\}$, evaluating
$$\mathbb E[V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)],$$
and then applies $\pi(x)$. The optimal policies $\pi\equiv\alpha$ and $\pi\equiv\beta$ are found jointly. If both copies run the same deterministic optimizer, they select the same policy and coordinate.

This is a concrete reading of the footnote's remark that the distinction "makes a difference in certain multi-agent dilemmas." The reading is my illustration, not the paper's.

### 6.4 Ties and randomization (unspecified)

The source says nothing about how A-FDT breaks ties or whether it may randomize. A reasonable convention is a fixed, publicly known tie-breaking order, which keeps the agent predictable. Predictability is the property the whole theory exploits.

### 6.5 Fairness (open)

The paper claims A-FDT does at least as well as its rivals in "fair problems," meaning those where outcomes depend only on the agent's *behavior* and not on her decision procedure per se. It admits that no formal definition of fairness is available. Its footnote 15 shows the difficulty: a problem that punishes anyone who acts like a copy of the A-FDT agent defeats A-FDT. Claims of optimality for A-FDT are therefore currently conjectural.

## 7. Conclusion

A-FDT is CDT with the surgery moved. It does not intervene on the physical act. It intervenes on the node representing *what this decision function outputs on this input*, and it lets every subjunctively dependent variable move along with that node: predictions, twins, the appointment book. Observations do not prune the worlds considered. They select which input's output is being chosen.

Equation (4) gives one-boxing in Newcomb's problem, smoking in the lesion case, paying in Parfit's desert, and refusal against blackmailers, all from a single rule and without ratification or precommitment machinery. Applying it to new cases is straightforward once $P$ and $G$ are given. The unresolved work lies in where $G$ comes from, how to set the priors over the agent's own behavior on other inputs, and when to move from A-FDT's action-level optimization to the policy-level formulation the authors themselves prefer.

### References

- Yudkowsky, E. & Soares, N. "Functional Decision Theory: A New Theory of Instrumental Rationality." arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.