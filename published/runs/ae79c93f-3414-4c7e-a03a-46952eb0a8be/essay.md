# A-FDT: Deciding by Intervening on Your Own Algorithm

## 1. The question A-FDT asks

Decision theorists have long argued about how an agent should evaluate options that are correlated with the world in ways her choice does not cause. Two standard theories are the usual reference points. Evidential decision theory (EDT) evaluates an act by conditioning on it. Causal decision theory (CDT) evaluates an act by causally intervening on it.

Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third answer. They state its central idea as follows:

> "A functional decision theorist holds that a rational agent is one who follows a decision procedure that asks 'Which output of this decision procedure causes the best outcome?', as opposed to 'Which physical act of mine causes the best outcome?'"

The paper's main formal statement is its Equation (4). In that equation the agent chooses an *action* by intervening on a node that represents the output of her decision function on her actual inputs. Footnotes 7 and 16 say the authors' preferred version instead chooses a *policy*. To keep the two apart, I use **A-FDT** (action functional decision theory) for the theory defined by Equation (4). When I mean the policy-selecting variant, I call it **P-FDT**.

This essay does four things:

- states A-FDT precisely;
- shows how to compute with it;
- works through the paper's examples, correcting two arithmetic slips along the way;
- marks where the source underdetermines the procedure, and proposes operational readings, flagged as my own.

## 2. The common frame: expected utility with a free "⟶"

All three theories maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where:

- $x$ is the observation history;
- $\mathcal U$ is utility;
- $P(a\hookrightarrow o;x)$ is the probability of outcome $o$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the only free parameter. On this view the three theories disagree about "the epistemic perspective from which actions are to be evaluated," not about value.

Each theory works with a world-model and turns it into a set of hypotheticals, one per action. Write $V=\mathcal U(\textsc{Outcome})$.

- **EDT:** $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$.
- **CDT** (Pearl-style): the model is $(P,G)$ with $G$ a causal graph, and the rule is $\arg\max_a \mathbb E(V\mid do(\textsc{Act}=a),\textsc{Obs}=x)$.

The source stresses that hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs or possible worlds. Holding onto this point dissolves several apparent paradoxes later on.

## 3. The definition of A-FDT

Equation (4) of the paper reads:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; do\!\left(\textsc{fdt}(\underline P,\underline G,\underline x)=a\right)\right).$$

The ingredients are as follows.

1. **$P$** is a probability distribution over variables. These include ordinary physical variables (box contents, lesions) and *logical* variables representing outputs of mathematical functions.
2. **$G$** is a graph that "tells us how changing a logical variable affects all other variables." It extends a causal graph to encode *subjunctive dependence*. Two systems subjunctively depend on a function when both compute it, as with an agent and an accurate predictor of that agent. A causal dependence is a special case. A mere statistical correlation, such as the lesion, is not one.
3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a single node: "a variable … that represents the output of FDT when run on inputs" $(P,G,x)$. The underlines denote dequoting, so the node's *name* depends on the actual inputs. The self-reference is defended by appeal to Kleene's recursion theorem. The agent needs a variable *representing* her output, not knowledge of its value.
4. **The surgery** sets that node to $a$ and propagates downstream along $G$, Pearl-style. Everything not downstream keeps its prior distribution.

The authors summarize two differences from CDT. First, the intervention target is a logical node (the decision *type*) rather than the physical act (the *token*). Second:

> "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

The second point is easy to miss. It is the source of A-FDT's "updateless" behaviour (Section 6).

### A recipe for applying A-FDT

To use A-FDT on a new case, proceed as follows.

- **(i)** List the decision-relevant computations. These are the agent's own decision function on each input she might receive, and any agent or process that evaluates those computations, such as predictors, twins, or copies.
- **(ii)** Draw $G$. Give each node $\textsc{fdt}(\cdot,\cdot,y)$, for each possible observation $y$, an arrow into the physical act when she is in situation $y$, and into every predictor or simulation of her behaviour in situation $y$. Draw no such arrows to merely correlated processes such as lesions.
- **(iii)** Put priors on exogenous nodes. This includes the *other* fdt nodes, the ones for inputs she did not receive.
- **(iv)** For each $a$, intervene on the node for her actual $x$, compute $\mathbb E(V)$, and take the argmax.

## 4. Worked examples

All payoffs are in dollars-as-utility, with predictor accuracy 0.99 unless stated.

### Newcomb's problem

In $G$, the node $\textsc{fdt}(\underline P,\underline G)$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$. The prediction is also affected by an independent accuracy node.

- Setting the node to *onebox* gives $P(\text{full})=0.99$, so
$$\mathbb E V = 0.99\times 10^6 = 990{,}000.$$
- Setting it to *twobox* gives $P(\text{full})=0.01$, so
$$\mathbb E V = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. The paper itself writes 990,000 for Fiona but 999,000 in the parallel EDT computation; 990,000 is correct for both.

CDT intervenes on $\textsc{Act}$, leaves $P(\text{full})=p$ untouched, and two-boxes for every value of $p$. The A-FDT agent appeals to no retrocausation. She simply refuses to imagine her act varying while the same computation, run inside the predictor's model, stays fixed.

### Smoking lesion

Here the lesion affects which utility function the agent has, and thus *which* fdt node controls her act. The source models this with two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The lesion selects which one sets $\textsc{Act}$, and neither has an arrow into $\textsc{Cancer}$.

Intervening on her own node therefore leaves $P(\text{lesion})=p$ unchanged. Smoking wins by $p\cdot 1{,}000$, so A-FDT smokes. The general lesson is that **correlation without shared computation creates no edge in $G$**. Merely correlated events are treated exactly as CDT treats them.

### Transparent Newcomb

Both boxes are visible. Box B was filled iff the agent was predicted to one-box upon seeing it full. The agent sees it full, with $x=\text{full}$.

The graph contains $\textsc{fdt}(\cdot,\text{full})$, which feeds the prediction, and $\textsc{fdt}(\cdot,\text{empty})$. The prediction decides which of the two controls the act. Let $q$ be the prior that the "empty" node outputs *twobox*.

- **onebox:**
$$0.99(10^6) + 0.01\,q(1{,}000) = 990{,}000 + 10q.$$
- **twobox:**
$$0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.$$

The source prints the second as "\$110,00 + q·\$990," a typo for \$10,010. Either way, onebox wins for every $q\in[0,1]$, so A-FDT one-boxes while *looking at* a full box. CDT and EDT both two-box here, and the source adds that they therefore tend to be shown an empty box.

The source argues that this case is structurally identical to **Parfit's hitchhiker**, where a lie-detecting driver rescues only those who will pay once in the city. A-FDT pays. Mapping that case onto the same template is a good test of the recipe.

### XOR blackmail and mechanical blackmail

**XOR blackmail.** A predictor sends a letter iff exactly one of two things holds: no termites and you will pay, or termites and you won't pay. The letter does not affect the termites. A-FDT's graph has no edge from the fdt node to $\textsc{Infestation}$. Intervening changes only whether the letter arrives and what she pays. With termite prior $\pi$ and damage $D=10^6$:

- the pay-policy loses $\pi D + (1-\pi)\cdot 1{,}000$;
- the refuse-policy loses $\pi D$.

So A-FDT refuses. EDT pays, because conditioning on paying "sends her probability on termites to 0."

**Mechanical blackmail.** A blackmailer launches a ruinous program only if she predicts payment. Upon receiving the letter, A-FDT intervenes on $\textsc{fdt}(\cdot,\text{blackmail})$:

- setting it to *pay* makes blackmail near-certain and costs about 1,000;
- setting it to *refuse* makes blackmail near-impossible.

A-FDT refuses. The source adds a quantitative threshold. With a false-positive rate of 0.0009, refusing has an expected loss of \$900 against \$1,000 for paying, so she refuses. At 0.011% the source says she pays. Note that 0.011% is 0.00011, which gives a refusing loss of \$110; 1.1% would give \$11,000 and flip the comparison. So "0.011%" should probably read 1.1%. The general rule: refuse iff $\varepsilon\cdot 10^6 < 1{,}000$.

### Death in Damascus

Death predicts perfectly. Under A-FDT the fdt node feeds both the agent's location and Death's appointment book, so either choice means death. Staying saves \$1,000, so she stays.

CDT, by contrast, oscillates: whichever city it expects to go to, it prefers the other. The source further argues that even a CDT agent who settles somewhere will reason as if it survives with probability at least 50%, and so will decline to pay \$1 for a genuinely random coin that would give it a real 50% chance of thwarting Death.

## 5. Dominance and fairness

**Dominance.** The source claims every hypothetical-construction method yields its own dominance notion. Under A-FDT counterfactuals, which hold subjunctive dependencies fixed, two-boxing does not dominate. The authors conclude that dominance "doesn't afford us a neutral criterion," and evaluate theories by utility achieved instead.

**Fairness.** They restrict claims of superiority to "fair problems": problems where outcomes depend only on the agent's behaviour in the dilemma at hand, not on which procedure produced it. They grant that a problem punishing FDT agents *as such* defeats A-FDT. Footnote 15 concedes that formalizing fairness remains open.

## 6. Observations: why A-FDT does not condition

Equation (4) contains no "$\textsc{Obs}=x$" in the conditioning bar. This is deliberate. Under A-FDT, the observation determines *which* node is intervened on, not which worlds are retained.

This creates a small inconsistency in the source. In the transparent-Newcomb computation the authors write $\mathbb E(V\mid do(\textsc{fdt}(\cdot,\text{full})=a),\textsc{Obs}=\text{full})$. Read literally, conditioning on Obs = full would eliminate the inaccurate-prediction branch and reintroduce exactly the "double update" that the source's TDT note warns against. Yet their numbers (the $0.01q$ term from the *empty* branch) show they did *not* condition.

**Operational reading (mine):** follow Equation (4) as printed. The observation selects the node and is otherwise not conditioned on. All of the source's numbers agree with this reading, and it is the only one that yields one-boxing in the transparent case.

The consequence is what the source calls acting "as they would have precommitted to act." The hypotheticals include worlds in which the agent never received her actual observation. The authors embrace this: FDT agents "imagine hypothetical worlds in which, if their action were different, they would have seen different things."

## 7. What the source leaves open, and reasonable fillings-in

**1. Where $G$ comes from.** This is the biggest gap. The authors call it "perhaps the largest open problem," since there is no analogue of Pearl's causal discovery for logical dependence. A-FDT is thus a procedure *relative to* a supplied $G$. My operational proposal: draw an edge from the fdt node for input $y$ to any process whose behaviour is (approximately) computed from a model of the agent's response to $y$. Partial reliability goes into separate noise nodes, like $\textsc{Accurate}$. Processes correlated with her act only through shared causes, such as lesions or demographics, get no edge. This matches every example in the paper, but it is a heuristic, not a theorem.

**2. Counterpossibles.** In reality the fdt node has a fixed value, so intervening on it is counterlogical. The paper sidesteps the need for a $\mathtt{true}(\varphi)$ operator by reusing $do$ on a given graph. It admits this rests on "shakier philosophical foundations" than CDT, and argues that CDT's interventions on deterministic tokens face an analogous problem.

**3. Priors on the agent's other nodes.** Quantities like $q$, the prior on her behaviour after unseen observations, are exogenous inputs to A-FDT. In the paper's examples the answer is insensitive to $q$, but nothing guarantees this in general. A natural fixed-point requirement (mine) is to set $q$ to what A-FDT would itself output on those inputs. This is computable by recursion in finite problems, but it can admit several self-consistent solutions.

**4. Action vs. policy.** The divergence matters most here. A-FDT intervenes on a single node and holds the other fdt nodes at their priors. Consider two copies of the agent who receive different observations, say "red" and "blue," and are paid only if they *mismatch* in a way that requires coordinated asymmetric acts. A-FDT on input "red" optimizes its own output against a fixed belief about the "blue" node. It can thereby settle on a coordination equilibrium that is worse than the jointly optimal pair.

P-FDT instead chooses the whole map $\pi:\mathcal X\to\mathcal A$ at once, maximizing $\mathbb E(V\mid do(\textsc{fdt}=\pi))$, and then applies $\pi(x)$. This avoids the problem. The source says this difference "makes a difference in certain multi-agent dilemmas" but none in the paper. That is consistent with my example; the example itself is my construction.

**5. Ties and zero-probability issues.** These are unaddressed. Unlike EDT, the $do$ operator keeps every action evaluable even at prior probability zero, which is one of A-FDT's advantages. Tie-breaking is simply unspecified.

## 8. Agreement with CDT and EDT, and why the authors favour A-FDT

When every correlation between the act and the world is caused by the act, all three rules coincide:
$$\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)].$$
Divergence requires predictors, copies, or other implementations of the agent's decision function.

The source's diagnosis is that "EDT respects too many action-environment correlations, while CDT respects too few." A-FDT keeps exactly those correlations that arise from shared computation.

The supporting arguments are:

- **Utility achieved.** The authors call this primary.
- **Precommitment.** A-FDT "acts as it would have precommitted to act."
- **Value of information.** A-FDT never pays to avoid information.
- **Reflective stability.** A-FDT is reflectively stable in fair problems. CDT, by contrast, recommends self-modification away from itself.

The authors also sketch applications to voting coalitions among similar reasoners, to self-coordination over time (going to the gym), and to AI systems that can be copied and predicted.

## 9. Conclusion

A-FDT is CDT with the surgery moved. Rather than intervening on the physical act, the agent intervenes on the node representing her decision algorithm's output on her actual inputs. That change propagates to every process that subjunctively depends on the output: predictors, twins, simulations. Observations change which node is intervened on rather than being conditioned upon.

With a correct dependency graph, the rule one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker, refuses both kinds of blackmail, and stays in Damascus. It is a single argmax with no ratification step.

Its weaknesses are just as specific:

- the dependency graph $G$ is an unexplained input;
- the counterpossible semantics behind the $do$ step is unsettled;
- priors over its own unrealized branches are exogenous;
- in some coordination settings, choosing an action rather than a policy can be suboptimal, which is why the authors themselves prefer the policy form.

To apply A-FDT to a new case, build the dependency graph honestly, intervene on the single node for your actual input, and compute expected utilities.

**Reference.** Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality*. arXiv:1710.05060.