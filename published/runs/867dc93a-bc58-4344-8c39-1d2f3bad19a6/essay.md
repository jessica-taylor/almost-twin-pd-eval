# A-FDT: Choosing the Output of One's Own Decision Function

## 1. What this essay covers, and naming

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a decision rule whose core slogan is that an agent should treat her decision as "the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper states this rule formally in Equation (4) of Section 5. I take that equation as the definition of the theory discussed here, and I call it **A-FDT (action functional decision theory)**.

The source itself just writes "FDT." The label "A-FDT" is mine, and it marks a distinction the source draws in two footnotes. In those footnotes the authors say that in their "preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." Equation (4) does not do this. It selects an *action* for the observation actually received. I call the footnoted alternative **policy-selection FDT**. **CDT** (causal decision theory) and **EDT** (evidential decision theory) are the two rivals the paper argues against.

Throughout, I separate three kinds of claim: what the source says, what follows from its definitions, and what I add as operational proposals.

## 2. The common frame: expected utility with a choice of hypothetical

The source places all three theories inside one expected-utility template:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history, the $o_j$ are outcomes, and $P(a \hookrightarrow o_j; x)$ is the probability of $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the authors say the theories disagree only about how to read the connective $\hookrightarrow$. In Joyce's words, they disagree "about the epistemic perspective from which actions are to be evaluated."

Write $V = \mathcal U(\text{Outcome})$. The two classical readings are:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \text{Obs}=x, \text{Act}=a), \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathrm{do}(\text{Act}=a), \text{Obs}=x). \tag{3}
$$

EDT conditions on the act. CDT performs a Pearl-style intervention on a node $\text{Act}$ representing the agent's *physical* behaviour, using a causal graph $G$. A $\mathrm{do}$ intervention cuts the node off from its parents, sets its value, and recomputes only what lies downstream. Every correlation between the act and things upstream of it, or merely parallel to it, is severed.

The source's diagnosis is that EDT's hypotheticals "respect too many correlations" while CDT's "respect too few." A-FDT is designed to keep exactly the correlations that run through the agent's decision function.

## 3. The definition of A-FDT

Equation (4) of the source, with the theory renamed, reads:

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathsf{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\;} \tag{4}
$$

Each ingredient needs some explanation.

**The world-model $(P,G)$.** $P$ is a probability distribution over variables. Unlike a CDT model, it includes variables standing for the outputs of mathematical functions, such as a variable for the value of $6288+1048$. $G$ is a graph that tells us, in the source's words, "how changing a logical variable affects all other variables." It encodes *subjunctive dependence*, not just causal dependence.

**The intervention node $\mathsf{fdt}(\underline P,\underline G,\underline x)$.** The underlines denote dequoting. This is the variable whose value is "whatever the A-FDT procedure outputs when run on exactly these inputs." The model therefore contains a representation of its own decision procedure. The source argues this is harmless, because the agent needs a variable *representing* the output, not knowledge of its *value*, and Kleene's recursion theorem ("quining") shows such self-representation is constructible.

**The intervention.** For each candidate action $a$, set this logical node to $a$. Then propagate along $G$ to everything that depends on it: the agent's physical act, a predictor's forecast, a twin's choice. Score the resulting distribution by $\mathbb E(V)$.

**Observations.** Compare Equations (3) and (4). The observation $x$ does not appear as a conditioning event in (4). The source draws two differences between CDT and A-FDT:

1. CDT intervenes on the physical action, whereas A-FDT intervenes on the output of the decision procedure.
2. "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

The second difference is what separates A-FDT from a theory that first updates on what it sees and then intervenes. A footnote describes that double move, attributed to Timeless Decision Theory, as "a kind of 'double update' which proves harmful in practice."

The source gives three readings of each of its equations, and they apply equally to (4):

- a Joyce-style constraint on $P(a \hookrightarrow o;x)$;
- advice about how to build hypotheticals from a world-model;
- an algorithm someone could execute.

In the type–token language the source borrows from Peirce, a CDT agent "intervenes on the token," and an A-FDT agent "intervenes on the *type*."

**When the theories agree.** The source shows that if every correlation between $\text{Act}$ and other variables is caused by $\text{Act}$ (apart from $\text{Act}$'s dependence on the $\mathsf{fdt}$ node), then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathrm{do}(a)] = \mathbb E[V\mid \mathrm{do}(\mathsf{fdt}(\underline P,\underline G)=a)],
$$

so all three theories coincide. They come apart only when something other than the act's causal consequences tracks the act. Predictors and copies of the agent are the paradigm cases.

## 4. Subjunctive dependence: what gets an arrow from the $\mathsf{fdt}$ node

Everything substantive in A-FDT sits in $G$. The source's criterion is that "when two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." It illustrates with calculators:

- Two well-functioning calculators computing $6288+1048$ are subjunctively linked, even on opposite sides of the universe.
- A scribe copying one calculator's output depends on it both causally and subjunctively. The source says "causal dependence is a special case of subjunctive dependence."
- Two calculators that happen to share a colour are only statistically correlated.

A predictor "contain[s] an accurate *mental representation* of the FDT agent's decision function," so it gets an arrow from the $\mathsf{fdt}$ node. A carcinogenic lesion "is not evaluating the agent's future decisions," so it does not.

From the source's examples I distil the following procedure for applying A-FDT to a new problem. It is my systematization, not a procedure the authors state.

1. **Outcomes and utility.** Identify the outcome variables and $V$.
2. **Enumerate inputs.** List each observation history $y$ the agent might be in when deciding. Create a node $\mathsf{fdt}(\underline P,\underline G,\underline y)$ for each.
3. **Locate implementations and models of the function.** For each place in the world where the decision function, on some input $y$, is computed or modelled (the agent's own body, a predictor's model, a twin, a future self), draw an arrow from $\mathsf{fdt}(\cdot,\underline y)$ to that place.
4. **Wire the actual act.** The physical act $\text{Act}$ depends on all $\mathsf{fdt}$ nodes, together with whatever determines which observation actually occurs. This is a switch: $\text{Act} = \mathsf{fdt}(\cdot,\underline{\text{Obs}})$.
5. **Add the rest of the world.** Represent imperfect prediction with a noise node, as the source does with $\text{Accurate}$. Model merely statistical correlations, such as lesions, through ordinary common causes that receive no arrow from any $\mathsf{fdt}$ node.
6. **Choose.** Given the actual observation $x$, apply (4):
   - for each $a$, set $\mathsf{fdt}(\cdot,\underline x)=a$;
   - leave every other $\mathsf{fdt}$ node at its prior;
   - propagate and compute $\mathbb E(V)$;
   - take the argmax.
   
   Do **not** additionally condition on $\text{Obs}=x$. The intervention may even change the probability that $x$ occurs.

## 5. Worked examples

**Twin Prisoner's Dilemma.** Payoffs are \$1M each for mutual cooperation and \$1k each for mutual defection. A unilateral defector gets \$1,001k and the cooperator gets nothing. Both twins' acts hang off the same $\mathsf{fdt}$ node. Setting it to *cooperate* yields \$1M and setting it to *defect* yields \$1k, so A-FDT cooperates. CDT defects, because by its lights defection dominates.

**Newcomb's problem (99% predictor).** In the agent's graph, $\mathsf{fdt}(\underline P,\underline G)$ points to both $\text{Act}$ and $\text{Prediction}$. $\text{Prediction}$ also depends on $\text{Accurate}$, which holds with probability $0.99$.

$$
\begin{aligned}
\mathbb E[V\mid\mathrm{do}(\mathsf{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)=990{,}000,\\
\mathbb E[V\mid\mathrm{do}(\mathsf{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT's graph has no arrow from the act to $\text{Box B}$, so it holds $P(\textit{full})=p$ fixed. Two-boxing then wins by \$1,000 whatever $p$ is.

Note what A-FDT does *not* claim. The source insists there is no "appeal to a belief in retrocausal physics." The agent simply finds it "foolish to imagine her action changing without also imagining" the function's output changing, and hence the prediction.

**Smoking lesion.** Here the graph differs from Newcomb's even though the statistics are isomorphic. The lesion determines which preferences the agent has, and hence which of two decision computations controls her act:

- $\mathsf{fdt}(\underline{P_S},\underline G)$ if she has the lesion and likes smoking;
- $\mathsf{fdt}(\underline{P_R},\underline G)$ if she lacks it.

Neither node has an arrow into $\text{Cancer}$. Let $p=P(\textit{lesion})$ and let $q$ be the probability that the other computation smokes. Intervening on the node she is running gives:

$$
\begin{aligned}
\textit{smoke}&:\ p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),\\
\textit{refrain}&:\ p(10{,}000)+(1-p)(990{,}000+1{,}000q).
\end{aligned}
$$

Smoking wins by $p\cdot 1{,}000$. The source reads this as "the probability that $\mathrm{FDT}(P_S,G)$ is actually the procedure controlling her action, times the value of smoking." So one rule yields one-boxing *and* smoking, which Gibbard and Harper had argued no rational agent could consistently do.

**Transparent Newcomb (and Parfit's hitchhiker).** Both boxes are visible. Box B was filled iff the predictor foresaw one-boxing *upon seeing it full*. The agent sees it full.

There are now two function nodes, $\mathsf{fdt}(\cdot,\textit{full})$ and $\mathsf{fdt}(\cdot,\textit{empty})$. The prediction depends on the first. Which node drives $\text{Act}$ depends on the prediction. Let $q$ be the prior probability that the agent two-boxes on seeing an empty box. Intervening on $\mathsf{fdt}(\cdot,\textit{full})$:

$$
\begin{aligned}
\textit{onebox}&:\ 0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,\\
\textit{twobox}&:\ 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
\end{aligned}
$$

A-FDT one-boxes for every $q\in[0,1]$, while staring at the full box. Under the *twobox* hypothetical it envisions probably seeing an empty box. CDT and EDT both condition on $\textit{full}$ and two-box.

The source stresses that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." Its arguments for accepting the verdict are three:

- *precommitment*: CDT and EDT agents would pay to bind themselves to this action;
- *value of information*: A-FDT agents never pay to avoid seeing;
- *utility*: A-FDT agents are the ones who see full boxes.

**Mechanical blackmail.** A blackmailer launches a damaging program, which costs the agent \$1M unless she pays \$1,000. She launches it only if she predicts the agent would pay once blackmailed. Suppose she wrongly predicts payment with probability $\varepsilon$. Intervening on $\mathsf{fdt}(\cdot,\textit{blackmail})$:

- *pay*: the agent is always blackmailed and loses \$1,000;
- *refuse*: she is blackmailed with probability $\varepsilon$ and loses $10^6\varepsilon$ in expectation.

So A-FDT refuses iff $\varepsilon < 10^{-3}$. The source's case $\varepsilon=0.0009$ gives a \$900 expected loss, so the agent refuses even "holding the blackmail letter."

The source also gives a contrasting error rate at which A-FDT pays. As printed, "0.011%" lies below the 0.1% threshold, so it appears to be a typographical slip. The structural point stands: refusal is warranted only when the blackmailer's error rate is below 0.1%.

**XOR blackmail and Death in Damascus.** These show A-FDT agreeing with CDT where EDT fails, and disagreeing with CDT where CDT becomes unstable.

- *XOR blackmail.* Intervening on the letter-receiving node changes whether the letter is sent, but has no arrow to $\text{Infestation}$. A-FDT therefore refuses, as CDT does.
- *Death in Damascus.* Death's appointment book depends on the $\mathsf{fdt}$ node, so Death's location moves with the agent's choice in every hypothetical. Survival is the same under both options, and A-FDT simply stays and saves \$1,000. By contrast, the source describes CDT as needing ratification and pseudorandomization, and as declining to buy a truly random coin worth a 50% survival chance for \$1.

## 6. How A-FDT treats counterfactuals

A-FDT's hypotheticals are, by the source's own admission, *counterpossible*. If the function outputs *cooperate* on some input, "there is no possible world in which it outputs *defect* on that input." The source's ideal would be a $\mathrm{true}(\phi)$ operator that updates a distribution on a logical sentence:

$$
\mathrm{FDT}^*(P,x)=\arg\max_a \mathbb E\big(V\mid \mathrm{true}(\mathsf{fdt}(\underline P,\underline x)=a)\big).
$$

Since "it's not clear how to define a $\mathrm{true}$ operator," Equation (4) instead takes the logical dependency structure as an *input* $G$, just as CDT takes causal structure as an input.

The authors' defence of this impossibility is a parity argument. CDT agents in deterministic worlds also imagine their one possible act being different. In the source's words, "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

This gives A-FDT its own dominance notion. Action $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies," switching the function's output from $b$ to $a$ is never worse and sometimes better. The source argues that dominance is always relative to a way of building hypotheticals. It therefore cannot neutrally settle disputes between theories, and the authors prefer to compare utility actually achieved.

## 7. What the source leaves open, and proposals for closing it

**(a) Where $G$ comes from.** The source calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem." Equation (4) is a function of $G$, so every verdict is conditional on a correctly drawn graph.

The hardest unresolved sub-case is *partial similarity*. Is a predictor using a crude heuristic "computing the same function"? Is a rival who reasons similarly but not identically a twin? The source treats imperfect predictors through a noise node, which suggests a working policy.

*My proposal:* treat partial similarity as a mixture. With probability $r$, the other system's output equals $\mathsf{fdt}(\cdot,\underline y)$. Otherwise it follows some independent distribution. Then $r$ is estimated from the system's track record of agreeing with the agent's kind of reasoning. This is an extra assumption. It reproduces the source's 99%-predictor treatment as the special case $r=0.99$, but the source does not endorse it in general.

**(b) Priors on the non-intervened function nodes.** Equation (4) intervenes on one node and leaves the others, such as $\mathsf{fdt}(\cdot,\textit{empty})$, at their prior. The source handles this by noting that "the correct value of $q$" is 1 (or 0), "but it won't matter." In its examples the verdict is indeed robust across $q$. Nothing guarantees robustness in general.

*My proposal:* impose a consistency requirement. The prior on each $\mathsf{fdt}(\cdot,\underline y)$ should put its mass on $\mathrm{A\text{-}FDT}(P,G,y)$ itself. This matches the source's remarks about what the "correct" $q$ is. It amounts to a fixed-point condition, and fixed points need not be unique, as the next example shows.

**(c) Action versus policy.** The authors' own preferred formalization uses policies:

$$
\pi^*=\arg\max_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V\mid \mathrm{do}(\mathsf{fdt}(\underline P,\underline G)=\pi)\big),\qquad\text{act on } \pi^*(x).
$$

This is my rendering of their footnoted description of policy-selection FDT. They say the difference "only matters in multi-agent dilemmas so far as we can tell."

Here is my own illustration of how the two can come apart. Two copies of the agent are run, one shown *red* and one shown *blue*. Each picks $L$ or $R$. The payoff to each is:

- 10 if both pick $L$;
- 5 if both pick $R$;
- 0 if they mismatch.

The *red* copy running A-FDT intervenes on $\mathsf{fdt}(\cdot,\textit{red})$ and holds $\mathsf{fdt}(\cdot,\textit{blue})$ at its prior $P(L)=q$. This gives

$$
\mathbb E[V\mid L]=10q,\qquad \mathbb E[V\mid R]=5(1-q).
$$

So it picks $L$ iff $q>1/3$. Two consistent fixed points exist: $(q=1, \text{both } L)$ and $(q=0, \text{both } R)$. The second is self-confirming but Pareto-dominated. Policy-selection FDT compares the four policies jointly and selects $(L,L)$ directly.

So in problems where several instances of the function receive different inputs and must coordinate, A-FDT's verdict can depend on priors over its own other-input outputs. This supports the authors' preference for policies. For the single-agent dilemmas in the paper, the two coincide.

**(d) Fairness.** The source claims A-FDT is optimal in "fair" problems, meaning those where outcomes depend only on the agent's behaviour, not on her decision procedure as such. It admits that this notion is not formalized. Its own footnote gives an awkward case: a game that punishes anyone who matches a copy of A-FDT. Claims of A-FDT's superiority should be read as conjectures relative to an informal class of problems.

## 8. Practical upshot

The source offers several brief applications.

- **Voting coalitions.** Ten like-minded agents each pay \$1,000 to vote and all win \$1M iff all vote. Their decisions all hang off one function node, so A-FDT agents vote.
- **Self-coordination over time.** An agent deciding whether to go to the gym today recognizes that tomorrow's self faces the same computation. Going today therefore corresponds to going every week.
- **AI systems.** The authors expect artificial agents, which are easily copied and predicted, to face Newcomb-like structures routinely.

In each case, applying A-FDT means doing the step in §4 that CDT skips: find everything in the world that runs, or models, your decision function, and let it move with your choice.

## 9. Conclusion

A-FDT, defined by Equation (4) of the source, is an expected-utility rule whose hypotheticals come from intervening on a *logical* variable: the output of the agent's own decision procedure on its actual input. It differs from CDT in where it intervenes, and in using observations to choose the intervention node rather than to condition. It differs from EDT in breaking merely statistical correlations, such as lesions.

This one change yields one-boxing, smoking, paying the hitchhiker's driver, refusing blackmail, and calm acceptance of Death's appointment book, all without ratification or precommitment devices. The theory is only as good as the dependency graph $G$ it is given, and the source openly leaves the construction of $G$ unsolved.

I have proposed two working conventions: mixture weights for partial similarity, and a self-consistency condition on priors over the agent's other-input outputs. These go beyond the source. The coordination example suggests that when several instances of the function must act together, the authors' preferred policy-selection variant is the more robust formalization.

**References**

- Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Gibbard, A. and Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Pearl, J. (2000). *Causality*.