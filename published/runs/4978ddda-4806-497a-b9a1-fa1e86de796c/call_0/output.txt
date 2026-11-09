# A-FDT: Deciding by Intervening on One's Decision Function

## 1. The idea

A-FDT is the decision procedure given by Equation (4), Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". Every expected-utility theory scores an action by the probability of each outcome in a hypothetical where that action is taken. The theories differ in how they build the hypothetical. A-FDT builds it by intervening on a variable that represents the output of the agent's own decision function, rather than on the physical act. This essay sets out the procedure, works through cases, and marks which claims come from the paper and which are my own additions.

## 2. The formal definition

The paper writes expected utility (Equation 1) as

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for decision hypotheticals. The paper (following Joyce) treats the theories as differing only in how $\hookrightarrow$ is read. Define $V:=\mathcal U(\text{Outcome})$. The three equations are:

- (2) EDT: $\arg\max_a \mathbb E(V\mid \text{Obs}=x,\text{Act}=a)$.
- (3) CDT: $\arg\max_a \mathbb E(V\mid do(\text{Act}=a),\text{Obs}=x)$.
- (4) A-FDT:
$$\text{FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\big(V\mid do(\text{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The inputs are a probability model $P$ over variables, a graph $G$, and an observation $x$. The variable $\text{fdt}(\underline P,\underline G,\underline x)$ stands for the output of this very procedure on these very inputs. The underlines denote dequoting. The self-reference is harmless because the agent needs a variable representing the value of its own output, not the value itself. The paper cites Kleene's recursion theorem (quining) for this.

The paper names two differences from CDT:

1. The intervention node is the output of the decision function, not the physical action.
2. Observation does not enter by conditioning. Observing $x$ changes which node is intervened on, from $\text{fdt}(\ldots,x)$ to $\text{fdt}(\ldots,y)$. The observation therefore indexes a different intervention point rather than restricting the model.

The graph $G$ must encode every dependence on the function's output, including causal, logical and computational links. The paper calls this subjunctive dependence. Mere statistical correlation does not count: two calculators that happen to be pink are not subjunctively dependent, and a lesion correlated with smoking is not either. Causal dependence is a special case of subjunctive dependence. The rule of construction is that when the agent imagines a different output, exactly the things that depend on that output change and everything else is held fixed.

The paper's footnotes add that the authors' preferred formalization intervenes on policies (maps from observations to actions), which matters only in some multi-agent problems. I follow the paper in treating this as a side remark and work with observation-indexed nodes.

## 3. How to apply it: a recipe

The recipe below is my reading of the paper's procedure.

1. Build $P$ with variables for the agent's decision-function output, one per possible observation, and for everything that could depend on it. Examples are a predictor's model of the agent, a twin, or an environment process that looks at the agent's policy.
2. Draw $G$ so that arrows leave $\text{fdt}(\cdot,x)$ for each node that reproduces or responds to the function's output on input $x$. This includes the agent's own act and the predictor's prediction. Draw nothing for nodes that are merely correlated.
3. For each $a$, set $\text{fdt}(\cdot,x)=a$ by $do$, propagate downstream, and compute expected $V$.
4. Output the maximizing $a$.

Step 2 is the hard part. The paper states plainly that nobody yet has a Pearl-style account of how to learn subjunctive-dependence structure from observation, and calls this "perhaps the largest open problem". It also admits a $\mathtt{true}$ operator over logical sentences is undefined, which is why $G$ is supplied as input. The case analyses below take $G$ as given, as the paper does.

## 4. Worked examples

### Newcomb's problem (99% accurate predictor)

The graph has $\text{fdt}\to\text{Act}$ and $\text{fdt}\to\text{Prediction}\to\text{Box B}$, plus a noise node *Accurate* (0.99).

- $do(\text{fdt}=\text{onebox})$: Box B is full with probability 0.99, so $\mathbb E V=\$990{,}000$.
- $do(\text{fdt}=\text{twobox})$: Box B is full with probability 0.01, so $\mathbb E V=\$11{,}000$.

A-FDT one-boxes. No retrocausation is involved. The agent simply does not imagine her act changing while the function's output stays fixed. CDT's graph has Prediction downstream of a *Predisposition* node but not of Act, so $do(\text{Act})$ leaves the box probability at $p$ and two-boxing wins by $\$1000$ for every $p$.

### Smoking lesion

Here the graph differs. The lesion causes both the desire to smoke and cancer, but the function's output is not upstream of cancer. The paper formalizes this with two utility functions, $\mathcal U_S$ and $\mathcal U_R$, so that two candidate functions exist and the lesion decides which one drives Act. Intervening on the node that actually runs leaves $P(\text{lesion})=p$ unchanged. Smoking gains $p\cdot\$1000$, so A-FDT smokes. The same equation therefore one-boxes in one problem and smokes in the other. All the work is done by $G$, which differs between the two problems. The paper also notes that this problem is contrived, since the agent is ignorant of her own preferences.

### Transparent Newcomb and Parfit's hitchhiker

Take the case where the agent sees a full box. The graph has two nodes, $\text{fdt}(\ldots,\text{full})$ and $\text{fdt}(\ldots,\text{empty})$, and Prediction determines which of them controls Act. Let $q$ be her credence that she two-boxes on seeing empty. Then:

- $do(\text{fdt}(\text{full})=\text{onebox})$ gives $0.99\cdot\$1{,}000{,}000+0.01\,q\cdot\$1000$.
- $do(\text{fdt}(\text{full})=\text{twobox})$ gives about $0.01\cdot\$1{,}001{,}000+0.99\,q\cdot\$1000$.

She one-boxes, even though she sees the full box. When she imagines two-boxing, she imagines a world where she probably saw an empty box. Parfit's hitchhiker is the same structure, so she pays the driver. The same reasoning refuses mechanical blackmail: paying is imagined as a world with a blackmail letter, and refusing as a world where the letter was probably never sent. If the blackmailer errs with probability 0.0009, refusal still wins. The paper reports that at 0.011% error, paying wins.

### Death in Damascus and XOR blackmail

In Death in Damascus, Death's location depends on the function's output through his book, so A-FDT stays, saving the $\$1000$. CDT oscillates, because it holds Death fixed. In XOR blackmail, changing the output changes whether the letter arrives, but not whether there are termites. A-FDT therefore refuses. EDT pays, because conditioning on paying makes termites impossible.

### Coordination examples

The paper's voting example (ten agents, each paying $\$1000$ to vote, with $\$1{,}000{,}000$ if all vote) and its gym example (the same function run today and next week) use the same mechanism. Dependence between identical or near-identical functions goes into $G$, so the choice moves the others' choices with it.

## 5. What distinguishes A-FDT from its rivals

The paper's summary is that EDT respects too many action-environment correlations and CDT too few. In simple models, where every correlation with Act is caused by Act, the three equations agree.

A-FDT also has its own notion of dominance. An action dominates if, holding fixed all subjunctive dependencies, switching the function's output to it is sometimes better and never worse. The paper's argument is that every method of constructing hypotheticals induces its own dominance principle, so dominance cannot arbitrate between theories without assuming one. The paper prefers to compare theories by utility achieved.

On fairness, the paper separates problems that reward or punish *actions* (Newcomb's predictor punishes two-boxers) from problems that punish the *procedure* a theory uses. No theory wins the latter kind. It claims A-FDT matches or beats rivals on fair problems, but admits it has no formal criterion of fairness. Its footnote 15 notes that a copy of the agent that punishes any matching action is unfair to A-FDT in a way that is hard to mirror for CDT.

The paper adds a point about reflective stability. A-FDT does not wish to self-modify, because it acts as it would have precommitted to act, and it does not assign negative value to information.

## 6. Open questions and my own proposals

**What the source leaves open.**
- *Structure learning.* How to infer $G$, including logical dependencies, is unsolved. The paper offers the human ability to reason about being predicted as evidence that workable heuristics exist.
- *Counterpossibles.* The intervention sets a logical fact to a value it does not in fact have. The paper defers to the literature on counterpossibles.
- *Policies versus acts.* Footnote 7 prefers policy-level intervention, but the paper does not develop it.

**My operational suggestions** (not in the source).
1. *A reliable heuristic for step 2.* Draw an arrow from the function's output to a node only if that node would be computed, copied or modeled from the same function on the same input. Check by asking: if the agent's reasoning concluded differently, would this node differ for that reason? Leave out nodes that differ only because of a shared cause that the agent does not control, such as the lesion.
2. *Degrees of dependence.* Where the predictor is imperfect, put noise nodes in the model, as the paper does with *Accurate*. Fiona's 99% reasoning is robust to this.
3. *Robustness check.* The answer should not depend on the agent's own priors over her output. In the paper's calculations the unknown $q$ and the prior on the node itself cancel or do not matter. If a decision depends on them, the graph is probably wrong.
4. *Error handling.* If the answer flips with small changes in the dependence strength, as in the blackmail example at 0.0009 versus 0.00011, compute the break-even point explicitly rather than rely on intuition.

These proposals are interpretive aids. A-FDT as defined needs only $(P,G,x)$.

## 7. Objections the paper addresses

*"Doesn't she ignore information?"* The paper says she responds to observation by switching the intervention node, and that A-FDT is a form of updatelessness. Older variants (Timeless Decision Theory) both condition and re-intervene, a "double update", which the paper says is harmful.

*"Isn't she deluded about control?"* The paper replies that a deterministic CDT agent also imagines worlds where her act differs. Both theories use imaginary hypotheticals, so "control" talk cannot separate them.

## 8. Conclusion

A-FDT is Equation (4): maximize expected utility under the surgery $do(\text{fdt}(\underline P,\underline G,\underline x)=a)$. It keeps CDT's causal surgery but applies it to the output of the agent's decision function, and it takes observations as indexing which function-node to intervene on. The result one-boxes, smokes, pays the hitchhiker, refuses blackmail and stays in Damascus, using a single rule whose entire sensitivity lies in the supplied dependence graph. Its main limitation, which the authors state themselves, is that no principled method yet exists for constructing that graph. A-FDT is therefore best seen as a well-specified decision rule resting on an incompletely specified theory of subjunctive dependence.