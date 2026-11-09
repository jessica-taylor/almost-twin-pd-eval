# A-FDT: Choosing the Output of a Decision Function

## 1. Scope and naming

This essay explains the decision procedure given as Equation (4) in Section 5 of Yudkowsky and Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*. The paper calls the theory "FDT". I call the Equation (4) procedure **A-FDT** (the "A" is for *action*), partly to keep it distinct from nearby proposals the paper mentions:

- **FDT′**, a variant that asks "What if I made my decisions using a different decision function?" (the paper argues it saves no trouble),
- **FDT\***, which would use an unspecified $\mathtt{true}$ operator on logical sentences,
- the evidential version of footnote 9,
- the paper's "preferred formalization", which intervenes on *policies* rather than actions (footnotes 7 and 16),
- Wei Dai's updateless decision theory and Yudkowsky's timeless decision theory, which the paper credits as early variants.

I also contrast A-FDT with **CDT** (causal decision theory) and **EDT** (evidential decision theory).

I try to mark where I am reporting the paper, where I am computing something the paper leaves implicit, and where I am proposing an interpretation of my own.

## 2. The common frame: expected utility with a choice of hypotheticals

The paper's Equation (1) says that all three theories maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is the connective for "decision hypotheticals". The paper leans on Joyce's representation theorem. In Joyce's words, decision theories "should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

So the theories do not differ on values or on the maximization step. They differ on two things:

1. what the agent's world-model $M$ consists of, and
2. how a hypothetical $M^{a\hookrightarrow}$ is built from $M$ for each candidate action $a$.

The paper stresses that hypotheticals are "decision-theoretic instruments constructed from beliefs", like "notes on scratch paper", and are not beliefs and not metaphysically real possible worlds.

For EDT, $M = P(\cdot\mid x)$ and the hypothetical conditions on $a$. For CDT, $M=(P,G)$ with $G$ a causal graph, and the hypothetical is Pearl's $\mathtt{do}(\mathrm{Act}=a)$. The hypothetical is a surgery that updates $\mathrm{Act}$ and its causal descendants and leaves everything else alone.

## 3. Equation (4)

A-FDT takes as input a probabilistic model $P$, a dependence graph $G$, and an observation history $x$:

$$\text{A-FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\Big[\,V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big].$$

(This is the paper's Equation (4), with $\mathrm{fdt}$ written in the paper's small-caps. Underlines "represent dequoting".)

Four features need unpacking.

**(a) The intervention target is a logical variable.** $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model that represents the output of the A-FDT algorithm when run on exactly these inputs. This node is not the physical act. The agent's body, a twin, a predictor's simulation, and a record in Death's appointment book may each be downstream of this node. The agent intervenes on the common upstream fact about what the function returns.

**(b) The graph $G$ encodes more than causation.** Where CDT needs a causal graph, A-FDT needs a graph saying "how changing a logical variable affects all other variables". The surgery is Pearl's $\mathtt{do}$, applied to a graph whose edges mean subjunctive dependence. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In its words, A-FDT hypotheticals "preserve all decision-relevant subjunctive dependencies", where CDT preserves only causal structure.

**(c) Observation changes the node, not the distribution.** CDT updates on $x$ by conditioning. A-FDT instead responds to $x$ by choosing *which* node to intervene on. Seeing $x$ versus $y$ means intervening on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ versus $\mathrm{fdt}(\underline P,\underline G,\underline y)$. These are different logical facts, and $G$ can wire them differently. This is why A-FDT behaves "updatelessly" in the sense below, even though it does respond to evidence. It also lets A-FDT entertain hypotheticals in which, had its output differed, it would have *made different observations*.

**(d) Self-reference is harmless.** The node's name contains $P$ and $G$, which contain the node. The paper notes that the agent need not know the *value* of the function to have a variable *representing* it, and that Kleene's second recursion theorem ("quining") gives self-representing data structures.

### What the agent computes

A step-by-step reading of Equation (4):

1. Build $(P,G)$, with a node for each relevant output of the decision function, including its outputs on observations other than the actual one.
2. Locate the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual $x$.
3. For each $a$, set that node to $a$ and recompute every node reachable from it in $G$. This includes the body's act, any predictors, twins, or copies, and any node that determines which observation the agent receives. Leave all other nodes (nature's coin flips, the lesion, the infestation) at their prior.
4. Compute $\mathbb E[V]$ in each modified model and take the argmax.

The paper's guiding condition is that when the agent "imagines herself taking two different actions, she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

### Relation to CDT and EDT

If every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$, with the possible exception of the logical node on which $\mathrm{Act}$ itself depends, then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}(\underline P,\underline G)=a)],$$
and the three theories coincide. They come apart only when something correlates with the action without being caused by it, as with predictors, twins, and copies.

The paper's diagnosis is that EDT "respects too many action-environment correlations, while CDT respects too few". A-FDT keeps exactly the correlations that survive when the *function's output* is changed.

## 4. Subjunctive dependence

The paper defines subjunctive dependence loosely. Two physical systems that compute the same function have behaviours that "subjunctively depend" on that function. Three clarifications come from the text:

- **Causal dependence is a special case.** A scribe who copies a calculator's display depends causally on it, and would also have written something else had the output been different.
- **Mere correlation is not dependence.** Two calculators that are both pink are correlated, but if the scribe had bought a green one, the other would still be pink.
- **Imperfection weakens but does not remove it.** If a predictor's model of the agent is imperfect, or the agent is nondeterministic, the dependence is weakened. In the paper's calculator analogy, a cosmic ray might corrupt one calculator, yet one can still infer much about it from the other.

Because a function has only one output on a given input, the surgery is a *counterpossible*: its antecedent contradicts logic, "any more than there are possible worlds where $6288+1048\neq 7336$". The paper concedes this is "the main drawback" relative to CDT. Its defense is that the task is technical rather than philosophical, that A-FDT only needs the restricted question of how predictions change if the algorithm's output changed, and that humans do this passably.

Equation (4) sidesteps the problem by taking the dependence structure as *input*, "in the same way that the relevant causal structure is given as an input to" CDT. The paper says deducing that structure from observation and experiment "is perhaps the largest open problem in the study of functional decision theory". It also doubts that Pearl's framework can already do it.

## 5. Worked examples

### 5.1 Newcomb's problem

Take $\mathrm{Accurate}$ to be true with probability 0.99. In $G$, the node $\mathrm{fdt}(\underline P,\underline G)$ feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor's model of the agent is a "twin". Then:

- $\mathtt{do}(\mathrm{fdt}=\text{onebox})$: $\Pr(\text{full})=0.99$, so $\mathbb E[V]=0.99\times 10^6=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\text{twobox})$: $\Pr(\text{full})=0.01$, so $\mathbb E[V]=0.01\times1{,}001{,}000+0.99\times1000=\$11{,}000$.

So A-FDT one-boxes. (The paper's text gives $\$999{,}000$ for EDT's one-boxing value in the same setup, which looks like a slip, since $0.99\times10^6=990{,}000$.)

Two points matter philosophically. First, nothing retrocausal is assumed. The agent does not think her act changes a past box. She thinks it is "foolish to imagine her action changing without also imagining the output taking on a different value", given a good predictor. Second, A-FDT does not become a two-boxer when it is nearly certain that it one-boxes. The imagined two-boxing world is one where the function outputs *twobox* on these inputs, so the predictor's record differs too.

### 5.2 Smoking lesion

Here the graph differs, and this is the example that shows that the graph, not the equation, carries the content. The lesion is a common cause of the act and of the cancer, and the cancer does not run any model of the agent. So in $G$ the logical node points to $\mathrm{Act}$ but *not* to $\mathrm{Cancer}$. The paper needs a small formalization trick: the lesion fixes which utility function the agent has, so there are two nodes, $\mathrm{fdt}(\underline{P_S},\underline G)$ and $\mathrm{fdt}(\underline{P_R},\underline G)$. The lesion selects which one controls $\mathrm{Act}$. Since $\Pr(\text{lesion})=p$ is unaffected by the surgery, smoking is better than refraining by $p\cdot\$1{,}000$, the chance that the intervened node is the controlling one, times the value of smoking. A-FDT smokes.

So one rule one-boxes in the first case and smokes in the second. The only thing that changed is the dependence structure: a predictor contains a representation of the agent's decision function, while a lesion does not. The paper admits the smoking lesion problem is contrived and recommends philosophers abandon it.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

With transparent boxes, $\mathrm{Obs}$ reveals the box. The predictor fills the box iff it predicts one-boxing upon seeing a full box. $G$ has nodes $\mathrm{fdt}(\cdot,\text{full})$ and $\mathrm{fdt}(\cdot,\text{empty})$, and $\mathrm{Prediction}$ decides which controls $\mathrm{Act}$. Having seen "full", the agent intervenes on $\mathrm{fdt}(\cdot,\text{full})$. Let $q$ be her prior probability that she two-boxes when she sees empty.

- **One-box**: with probability 0.99 the prediction is accurate, the box is full, and she gets \$1,000,000. Otherwise she faces an empty box. So $\mathbb E[V]=990{,}000+10q$.
- **Two-box**: if the prediction is accurate, the box is empty and the node intervened on is not even the one controlling her act. If it is inaccurate, she gets \$1,001,000. So $\mathbb E[V]=0.01\times1{,}001{,}000+0.99\times 1000q=10{,}010+990q$. (The paper prints this as "$\$110{,}00+q\cdot\$990$", which appears to be a typo.)

For any $q\in[0,1]$, one-boxing wins. A-FDT one-boxes while staring at a full box. When it imagines two-boxing, it imagines a world in which it likely saw an empty box. The paper argues that this is exactly equivalent to paying the driver in Parfit's hitchhiker.

### 5.4 Blackmail: why the intervention point matters

In the mechanical blackmail problem, the blackmailer runs the program iff she predicts the agent would pay on receiving the letter. A-FDT's node $\mathrm{fdt}(\cdot,\text{blackmail})$ feeds the blackmailer's prediction (hence whether a letter exists) and the agent's act. Setting it to *pay* gives probability about 1 of being blackmailed and a loss of \$1,000. Setting it to *refuse* gives probability about 0 of being blackmailed.

If the predictor errs with probability $\epsilon$, refusing costs $\epsilon\cdot10^6$ in expectation and paying costs \$1,000. The paper's numbers fit this: at $\epsilon=0.0009$ refusing costs \$900 and A-FDT refuses, while at $\epsilon=0.00011$ the cost is \$110 and A-FDT pays. The break-even is $\epsilon=0.001$. Note that A-FDT refuses even holding a letter and knowing the predictor erred in its own case, "because it's advantageous to be *the kind of agent* that makes such decisions."

Two related cases show the same pattern. In **XOR blackmail**, the infestation node is not downstream of the logical node, so A-FDT refuses; EDT pays because conditioning on paying "sends her probability on termites to 0". In **cosmic ray**, A-FDT takes the \$100 because the correlation between taking \$100 and being hit by a ray is merely statistical and is broken by the surgery. In **Death in Damascus**, Death's book depends on the function's output, so A-FDT stays home and saves the \$1,000. It also never has the CDT-style instability, in which its beliefs and its choice keep chasing each other.

## 6. An extension of my own: partial subjunctive dependence

The paper only shows near-perfect predictors and clean cases, but the equation is meant to handle graded dependence. Here is a simple model, which is my own illustration and not from the paper.

In the twin prisoner's dilemma, suppose the other player copies the output of my decision function with probability $r$. With probability $1-r$ she acts independently of it, cooperating with fixed probability $c$. Payoffs are those of the paper (\$1,000,000 for mutual cooperation, \$1,000 for mutual defection, \$1,001,000 for defecting on a cooperator). Applying $\mathtt{do}(\mathrm{fdt}=a)$:

$$\mathbb E[V\mid C]-\mathbb E[V\mid D]=r\cdot 999{,}000-(1-r)\cdot 1000 = 10^6 r-1000.$$

The independent player's bias $c$ cancels out. A-FDT cooperates iff $r>0.001$. At $r=0$ (a "pink calculator" correlation) it defects, which matches CDT. At $r=1$ it cooperates. In between, the threshold is just the ratio of cost to benefit. The point is that A-FDT's behaviour depends on a *dependence strength*, not on a binary label.

## 7. What the source determines, and what I add

**From the source.**
- The form of Equation (4), the intervention on the logical node, the treatment of observations by switching nodes, and the role of $G$ as input.
- The qualitative criterion that predictors, twins, and models of the agent depend on the function while lesions and coincidental correlations do not.
- Verdicts in the worked problems above.
- The acknowledgment that the construction of $G$, the counterpossible semantics, and a formal notion of "fair" problems are unresolved.

**Left open by the source, with my proposals.**

1. *Building $G$.* The source gives no algorithm. My operational heuristic, which is an interpretation and not a derivation, is as follows. Add an edge from the logical node to a variable $Z$ if $Z$'s value is produced by a process that runs, simulates, or reasons from (a model of) the function, or from a process that implements it. Do not add it merely because $Z$ is correlated with the act. Then grade the edge. If the representation is imperfect, introduce a stochastic mediating variable, as the paper does with $\mathrm{Accurate}$. This turns "fidelity of the predictor" into a parameter, as in the twin model above.

2. *Policies versus actions.* Footnotes 7 and 16 say that the authors' preferred formalization selects whole policies, mapping observations to actions, and that the difference matters "only in multi-agent dilemmas so far as we can tell". Equation (4) is the action-level version. Here the other-observation nodes appear in the model with priors (the $q$'s above), and the surgery fixes only the node for the observation actually received. In the problems above the $q$'s drop out of the verdict, but I would not assume that in general. If two observation nodes are linked, for example in sequential problems where the same agent acts after observing $x$ and after observing $y$, a policy-level version may behave differently. I am not asserting that it does. I am flagging that Equation (4) leaves how the other-observation nodes get fixed unspecified, and this is a place where an additional assumption is needed.

3. *Ties and priors.* If the argmax is not unique, the equation is silent about tie-breaking.

4. *Accuracy of the model.* The paper evaluates agents "in situations where their models accurately portray the situations that they face". Garbage in, garbage out applies: a wrong $G$ gives wrong prescriptions, just as a wrong causal graph does for CDT.

## 8. Why take Equation (4) seriously: the paper's arguments

The paper's case is mainly about utility achieved. A-FDT does well in Newcomb's problem, the smoking lesion problem, Parfit's hitchhiker, and the blackmail variants, where CDT or EDT each do badly in some of them. It does so with one rule, with no ratification and no costly precommitment ("FDT agents always act as they would have precommitted to act").

Four supporting points:

- **Dominance is not neutral.** Each method of building hypotheticals induces its own dominance principle. CDT's dominance argument for two-boxing is a restatement of its method, not an independent argument. A-FDT has its own dominance notion, under which it never takes a dominated action.
- **Fairness.** The paper distinguishes punishing an agent for her *action* (even a predicted one), which it calls fair, from punishing her for the algorithm she runs, which it treats as unfair to any theory. "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." No formal criterion of fairness is given. Footnote 15 shows the difficulty: a problem that punishes anyone who matches a copy of A-FDT's action is unfair to A-FDT but not obviously to its rivals.
- **No "delusion".** Any objection that A-FDT pretends to "control" a mathematical function applies equally to a deterministic CDT agent pretending to "control" a physical act. Both are imagining counter-to-fact scenarios.
- **Reflective stability.** The paper claims A-FDT would not want to switch to CDT even while holding a blackmail letter, because by its own hypotheticals being a payer makes it a target.

My own caution is that all this evidence comes from hand-picked cases, and the paper says so ("we do not yet know whether FDT is optimal among decision theories"). The strongest claim the source actually makes is that it knows of no fair dilemma where A-FDT systematically loses to a rival.

## 9. Conclusion

A-FDT is a small modification of CDT's formula with large consequences. It keeps expected-utility maximization and Pearl-style surgery, but moves the surgery from the physical act to the logical output of the agent's own decision function, and it handles observations by changing which node is intervened on instead of by conditioning. The model supplies the dependence graph, and the behaviour follows from it: A-FDT cooperates with sufficiently correlated twins, one-boxes against predictors, smokes, refuses blackmail, and pays the hitchhiker.

Where the dependence graph is clear, A-FDT gives definite answers. Where it is not, for instance with partially correlated agents, unfamiliar predictors, or multi-observation problems, the equation does not tell you what to do until you decide how the graph is to be built. The paper is candid that doing this in a principled way, and making sense of counterpossible conditionals, remain the main open problems.

## References (selected)

- Yudkowsky, E., & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Gibbard, A., & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Soares, N., & Fallenstein, B. (2015). "Toward Idealized Decision Theory", arXiv:1507.01986.