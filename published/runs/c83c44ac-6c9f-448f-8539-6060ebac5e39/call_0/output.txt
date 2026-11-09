# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

Any expected-utility theory has to say what "if I did *a*" means. Yudkowsky and Soares, in the paper this essay draws on, write expected utility as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where "$\hookrightarrow$" is the connective for decision hypotheticals. Evidential decision theory (EDT) reads it as conditionalization. Causal decision theory (CDT) reads it as Pearl's intervention on the physical act. This essay is about **A-FDT**, the theory given by Equation (4) of Section 5 of the paper (the paper itself calls it FDT). It reads the connective as an intervention on a node representing the *output of the agent's decision function*:

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathrm{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The paper's motto is that A-FDT is to subjunctive dependence as CDT is to causal dependence. Note that this is a procedure for evaluating *actions*; footnote 7 of the paper says the authors' preferred version iterates over policies, which matters only in some multi-agent cases.

## 2. The ingredients

**World-model.** The input is a pair $(P,G)$. $P$ is a probability distribution over variables, and $G$ is a graph saying how intervening on one variable propagates to others. For CDT, $G$ records causal structure. For A-FDT, $G$ must record *all decision-relevant dependence*: causal, logical, mathematical and computational. Variables representing outputs of mathematical functions (such as $6288+1048$) live in $P$ alongside ordinary ones.

**The intervention node.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable representing the output of the A-FDT procedure itself on the agent's own model and observations. The underlines mean "dequoting", so the node's name depends on the model. This self-reference is harmless: the agent need not know the node's *value* to have a variable representing it, and Kleene's second recursion theorem (quining) shows that such self-representation is constructible.

**Observations.** CDT responds to observation $x$ by conditioning. A-FDT responds by *changing which node it intervenes on*: from $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$. The paper's slogan is that the agent does not update, she re-indexes. This is why A-FDT can value a hypothetical in which she would have observed something different from what she actually saw.

**Procedure.** For each $a$:
1. Construct the hypothetical by $\mathrm{do}(\mathrm{fdt}(\cdot,\cdot,x)=a)$. This sets the node, then recomputes everything downstream of it in $G$, leaving everything else untouched.
2. Compute $\mathbb E[V]$ in that hypothetical.
3. Output the argmax.

**What counts as downstream.** Anything that subjunctively depends on the function's output: the agent's own act, a twin's act, a predictor's model of the agent, and decisions of third parties that respond to predictions. Mere statistical correlates (a common-cause lesion) are not downstream and stay fixed. The paper's calculator example makes the point: two calculators computing the same sum are subjunctively linked, while two that are both pink are not. Causal dependence is a special case of subjunctive dependence.

## 3. A worked pair of examples

**Newcomb's problem.** Let the node $F=\mathrm{fdt}(P^F,G^F)$ have arrows to $\mathrm{Act}$ and to $\mathrm{Prediction}$. Prediction is noisy: it matches $F$ with probability 0.99. Then

- $\mathrm{do}(F=\text{onebox})$: act is onebox, box B is full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(F=\text{twobox})$: box B is full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. No retrocausation is invoked. The agent simply declines to imagine the act varying while the predictor's model of that very function does not.

**Smoking lesion.** Here $G$ has no arrow from the decision node to $\mathrm{Cancer}$, because the lesion does not model the agent's function. The paper makes this work by letting the agent be uncertain which of two functions governs her act (one for each utility function, depending on the lesion); intervening on either leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$. So the same rule one-boxes and smokes; only $G$ differs between the two problems. This is the key practical lesson: **the decision-relevant content is in the graph.**

## 4. Observations and counterpossible-looking worlds

**Transparent Newcomb.** Suppose the agent sees a full box. She intervenes on $\mathrm{fdt}(P,G,\text{full})$. If this node outputs *twobox*, then in the hypothetical the predictor (who predicts this node) most likely left the box empty, so the agent would be running a *different* node, $\mathrm{fdt}(P,G,\text{empty})$. With $q$ her probability of two-boxing on seeing empty, the paper computes:

- one-box: $\$990{,}000 + 0.01q\cdot\$1{,}000$
- two-box: about $\$11{,}000 + 990q$

(The paper's printed "$\$110{,}00$" appears to be a typo; $0.01\times1{,}001{,}000\approx\$10{,}010$ plus $0.99q\cdot\$1{,}000$ is the correct arithmetic. Either way one-boxing wins.) A-FDT one-boxes even while looking at a full box. The same structure gives payment in Parfit's hitchhiker, and the paper notes these cases are equivalent.

**Blackmail.** In the mechanical blackmail case, the node $\mathrm{fdt}(\cdot,\cdot,\text{blackmail})$ determines both what she does on receiving the letter *and* whether the letter is sent. Setting it to *refuse* gives a hypothetical in which she is almost never blackmailed. Setting it to *pay* gives one in which she is always blackmailed and loses \$1,000. She refuses. With an imperfect blackmailer the comparison is quantitative: if the error rate is 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against a sure \$1,000, so she refuses. At 0.011% she pays, because then refusing costs \$1{,}100 in expectation. Note that the threshold is where expected losses equal, not some separate principle.

**Death in Damascus.** Death's location depends on the agent's decision node, so in every hypothetical Death is wherever she goes. Staying saves \$1,000. There is no instability, in contrast with CDT, whose hypotheticals hold Death fixed.

**Distinguishing cases.** In the XOR blackmail and cosmic ray problems, A-FDT breaks merely statistical correlations that EDT respects. When all correlations with the act are caused by the act (plus, possibly, the decision node), the paper notes that A-FDT, CDT and EDT agree.

## 5. Claims versus extensions

**What the source claims.**
- Equation (4) is a valid, Joyce-compatible expected-utility rule; the three theories differ only in the "epistemic perspective" they supply.
- A-FDT matches or beats CDT and EDT on the listed problems and, in the authors' view, on "fair" problems generally; the authors know of no counterexample.
- The theory is only as good as the graph $G$.

**What the source leaves open (and says so).** The paper flags as "perhaps the largest open problem" how to *derive* subjunctive dependence structure from observation and experiment, analogous to Pearl's causal discovery. A genuine $\mathtt{true}$ operator (conditioning on false logical sentences) is also undefined, so $G$ is taken as an *input*. Also unresolved is a formal definition of "fair" problems; footnote 15 gives an example (punishing whoever matches a copy of the agent) showing the notion is delicate.

**My own operational proposals (not from the paper).** To use A-FDT on a new case, I suggest this checklist:

1. *Enumerate the computations.* Ask which processes in the story implement or approximate the agent's decision function: twins, predictors, simulators, future selves facing the same problem. These get arrows from the decision node.
2. *Weigh by fidelity.* The paper treats imperfect prediction by noise variables (such as $\mathrm{Accurate}$). I'd extend this by letting each arrow be probabilistic, with strength given by the predictor's reliability.
3. *Keep common causes out.* If the correlate arises through a shared cause that does not model the function, it is not downstream.
4. *Index on observations.* Write one node per possible observation; use the nodes for observations that would differ across the hypothetical, as in transparent Newcomb.
5. *Mind the unconditional policy value.* The comparison is between whole hypotheticals, so an observation-conditional act is evaluated by its effect on how often that observation arises.

A caution: the checklist's step 1 depends on judgments (does this predictor model *me*, or only my action?) that the source does not formalize. The paper's own defense of fairness is that the predictor tracks *actions*, not the procedure. Cases where a mind-reader targets the procedure itself are, by the paper's own account, unfair to any theory.

## 6. Philosophical motivation

The paper's defense has three strands. First, **utility**: agents following Equation (4) predictably end up richer in fair problems. Second, **reflective stability**: A-FDT agents act as they would have precommitted to act, without costly binding mechanisms, and should not wish to self-modify. Third, **parity of "delusion"**: a deterministic CDT agent also imagines worlds in which her act differs from what it physically must be. Imagining a different function output is analogous to imagining a different token act, so objections about "control" cut equally against both. Dominance arguments are rejected as theory-neutral: each hypothetical-construction method yields its own dominance notion, and CDT's dominance simply restates CDT.

My own reservation is that this makes A-FDT only as determinate as the dependence graph. Two reasonable modelers could draw different graphs for the same story, and the theory gives no tie-breaker. That is why the paper's open problem is not peripheral.

## 7. Conclusion

A-FDT evaluates each action $a$ by imagining that the agent's own decision function outputs $a$, propagating that change along every dependence in the model, and choosing the best resulting world. Observations shift which node is intervened upon rather than conditioning the model. This single rule produces one-boxing, smoking, paying the hitchhiker, refusing blackmail and staying put in Damascus. Its main practical limitation is that the dependence graph must be supplied, and a principled theory of how to learn it remains an open problem.

**Reference.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.