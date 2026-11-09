# Action Functional Decision Theory (A-FDT): Deciding as the Output of a Function

## 1. What this essay covers

Yudkowsky and Soares (2017) propose that a rational agent should treat its decision as the output of a fixed mathematical function. On their account, the agent asks the question (quoting the abstract) *"Which output of this very function would yield the best outcome?"* Their paper calls the theory *functional decision theory*. It gives a formal decision rule as Equation (4) of Section 5, in which the agent intervenes on a node representing the **action** its decision procedure outputs on its actual input.

Footnotes 7 and 16 of the paper add that the authors' *preferred* formalization instead selects a **policy**, meaning a map from observations to actions. To keep these apart, this essay uses:

- **A-FDT** (action functional decision theory) for the rule of Equation (4);
- **policy-FDT** for the footnoted policy-selection variant;
- **CDT** (causal decision theory) and **EDT** (evidential decision theory) for the two standard rivals.

I first give A-FDT's definition, then work through the paper's main cases, and finally isolate what Equation (4) leaves undetermined. Where I fill a gap with my own proposal, I say so explicitly.

## 2. The common template: expected utility over hypotheticals

All three theories share the expected-utility form (the paper's Equation (1)):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce, the paper treats the theories as agreeing on how to value prospects and disagreeing about the *epistemic perspective*, that is, about how "$\hookrightarrow$" is to be read.

The paper operationalizes this disagreement as follows. The agent holds a world-model $M$. For each action $a$ it builds a *hypothetical* $M^{a\hookrightarrow}$, computes a value $V_a$ from it, and takes the best action. The authors stress that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." The three theories differ in what $M$ must contain and in the surgery used to build $M^{a\hookrightarrow}$.

With $V := \mathcal U(\textsc{Outcome})$, the rival rules are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$
$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$

In (3), $G$ is a causal graph and $do$ is Pearl's intervention operator.

## 3. The definition of A-FDT

**Equation (4).** The A-FDT agent has a probability distribution $P$ and a graph $G$. Unlike CDT's graph, this $G$ encodes "the logical, mathematical, computational, causal, etc. structure of the world." Among its variables is a node $\textsc{fdt}(\underline P,\underline G,\underline x)$, which stands for *the output of the A-FDT procedure itself when run on these very inputs*. The underline marks dequoting: the variable's name is built from the model and the observation. Then:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ } \tag{4}
$$

The paper identifies exactly two differences from CDT.

1. **Locus of intervention.** CDT intervenes on $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on a *logical* fact: what this function outputs on this input. Every variable downstream of that node in $G$ changes in the hypothetical. This includes the agent's own physical act, but also any predictor's forecast, any twin's choice, and any simulation of the agent. In the paper's type–token language, CDT intervenes on the token and A-FDT on the type.

2. **Treatment of observations.** Equation (4) does **not** condition on $\textsc{Obs}=x$. The observation enters only by selecting *which* node is intervened on: $\textsc{fdt}(\underline P,\underline G,\underline x)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline y)$. A hypothetical in which the agent's function outputs something different may therefore be a world in which the agent *never receives observation $x$*. This feature drives the theory's most distinctive verdicts.

The self-reference in (4) is described in the paper as harmless. The agent needs a variable *representing* its output, not knowledge of that output's value. Kleene's recursion theorem ("quining") shows how a program can contain a representation of itself.

**Why a $do$ on a logical node, and not a "$\mathtt{true}$" operator?** Ideally one would condition on the counterpossible sentence "the A-FDT function outputs $a$ here," since a deterministic function has only one output. The paper acknowledges that nobody knows how to define such a $\mathtt{true}$ operator. Its workaround is to *require the dependency structure as input*: "Given a graph $G$ that tells us how changing a logical variable affects all other variables, we can re-use Pearl's $do$ operator." This parallels CDT, which takes causal structure as given.

**The organizing slogan** is: *"Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."* Two systems are subjunctively dependent when both compute (or reliably model) the same function. The paper's analogy is two calculators computing $6288+1048$. Causal dependence is a special case: a scribe copying a calculator's output would have written something different had the output differed. Mere correlation is not subjunctive dependence: two calculators that are both pink by coincidence do not depend on each other.

**Agreement theorem (informal, from the source).** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)],
$$

and A-FDT, CDT and EDT all agree. The theories come apart only when something correlates with the action without being caused by it. Predictors, twins and copies are the paradigm cases.

## 4. Worked examples

All dollar figures stand for utilities.

### 4.1 Newcomb's problem

A predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A holds \$1,000.

The A-FDT agent's graph has the $\textsc{fdt}$ node as a parent of both $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Accurate}$ is an independent noise parent of the prediction. The two hypotheticals give:

$$
\mathbb E[V\mid do(\textsc{fdt}=\textit{onebox})] = 0.99(1{,}000{,}000) = 990{,}000,
$$
$$
\mathbb E[V\mid do(\textsc{fdt}=\textit{twobox})] = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

A-FDT therefore one-boxes. CDT intervenes on $\textsc{Act}$, which leaves $P(\textit{full})=p$ unchanged. Two-boxing then gains exactly \$1,000 whatever $p$ is, so CDT two-boxes. The psychological-twin prisoner's dilemma is isomorphic: the twin's choice is a child of the same $\textsc{fdt}$ node, so A-FDT cooperates.

The paper emphasizes that no retrocausation is assumed. The agent simply refuses to imagine a well-functioning predictor of its function disagreeing with that function.

### 4.2 The smoking lesion

Here the lesion causes both a taste for smoking and cancer. Nothing models the agent's decision function, so the cancer node is *not* a child of the $\textsc{fdt}$ node. The paper's full formalization is more intricate. The lesion fixes which utility function, $\mathcal U_S$ or $\mathcal U_R$, the agent has, and therefore which of two decision nodes controls the act. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ fixed. The paper writes that smoking beats refraining by $p\cdot\$1{,}000$, which is the probability that this node actually controls the act times the value of smoking. Its displayed expected utilities share all other terms and differ only by that amount.

So A-FDT smokes. Combined with §4.1, a single rule one-boxes *and* smokes. This is the combination that Gibbard and Harper's framing appeared to rule out.

### 4.3 Transparent Newcomb: observation as node selection

Both boxes are now transparent. The predictor fills B iff it predicts the agent would one-box *upon seeing B full*. The agent sees B full.

The graph contains two decision nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. $\textsc{Prediction}$ depends on the first. $\textsc{Prediction}$ determines the box contents and hence which node controls $\textsc{Act}$. Let $q$ be the agent's probability that it two-boxes on seeing B empty. Intervening on the *full* node gives:

$$
\text{onebox}: \quad 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000 + 10q,
$$
$$
\text{twobox}: \quad 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.
$$

(The extracted source prints the second line as "\$110,00 + q·\$990", which appears to be a typesetting error. The arithmetic above follows directly from the setup.)

For every $q\in[0,1]$, one-boxing wins. A-FDT leaves the \$1,000 behind **while looking at a full box**. If it conditioned on $\textsc{Obs}=\textit{full}$, as CDT and EDT do, two-boxing would win (\$1,001,000 vs \$1,000,000). The paper argues this verdict is structurally identical to paying the driver in Parfit's hitchhiker problem, which many find intuitive.

### 4.4 Mechanical blackmail and a threshold

A blackmailer runs a damaging program (cost \$1,000,000) only if she predicts the agent would pay \$1,000 upon being blackmailed. The agent is blackmailed.

Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})$:
- **pay:** the agent is blackmailed (the prediction tracks this output) and loses \$1,000;
- **refuse:** blackmail occurs only through predictor error, with probability $\varepsilon$, and then costs \$1,000,000.

A-FDT refuses iff $\varepsilon\cdot 10^6 < 10^3$, that is, iff $\varepsilon < 10^{-3}$.

The paper's first illustrative case fits this threshold: with $\varepsilon = 0.0009$, refusing costs \$900 in expectation and the agent refuses. Its second case says the agent pays at an error rate of "0.011%". By the computation above, that rate ($\varepsilon=1.1\times10^{-4}$) would still favour refusal. The verdict to pay holds at 0.11%. I read this as a typo, but the threshold derivation is the robust content.

The XOR blackmail problem shows the complementary point. The termite infestation is *not* downstream of the agent's function, so A-FDT refuses there too, though for different reasons from CDT.

### 4.5 Death in Damascus

Death's appointment book is written from a perfect prediction of the agent's decision procedure. So Death's location is a child of the $\textsc{fdt}$ node. Under either intervention the agent dies, and staying saves \$1,000. A-FDT stays, with none of the instability that sends CDT into Gibbard–Harper oscillation.

## 5. What Equation (4) leaves open, and how one might close it

### 5.1 Where does $G$ come from? (Open in the source)

The paper is candid about this: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." A-FDT is fully specified *relative to* $(P,G)$. Disagreements about cases frequently reduce to disagreements about $G$.

**My operational proposal.** Treat a variable $Z$ as a descendant of $\textsc{fdt}(\underline P,\underline G,\underline x)$ iff $Z$'s generating mechanism contains a computation that evaluates, or reliably approximates, the agent's decision function *on input $x$*. Errors in that computation become independent noise parents, like $\textsc{Accurate}$. A practical test is to ask whether the mechanism would produce a different value if handed a function that agreed with the agent's on all other inputs but differed on $x$.

On this criterion:
- predictors, simulations, twins running the same reasoning, and Death's book all qualify;
- lesions, coincidences, and correlations through shared ancestry without shared computation do not.

Partial similarity, such as a twin who is only "like me" in reasoning, requires further judgment. I would model it as a noisy channel whose reliability is estimated from track record. The paper itself proposes no such procedure, so this criterion is my addition.

### 5.2 What are the other decision nodes worth? (Partly open)

In §§4.2–4.4 the agent needs beliefs about decision nodes it is *not* intervening on: $q$ for the empty-box node, and a parameter for the $\mathcal U_R$ node. The paper says the correct values are computable ("as you may verify") and that uncertainty about them was harmless in its examples. In general they can matter.

**My proposal.** Set each sibling node's distribution to the A-FDT verdict at that input, computed recursively. Where this recursion is circular, require a fixed point: an assignment $\pi: \mathcal X\to\mathcal A$ such that for every $x$,

$$
\pi(x) \in \arg\max_a \mathbb E\big(V \mid do(\textsc{fdt}_x = a)\big)\quad\text{with } \textsc{fdt}_y \sim \pi(y) \text{ for } y\neq x.
$$

### 5.3 A-FDT versus policy-FDT (open; my illustration)

The fixed-point condition reveals where A-FDT and policy-FDT can diverge. A fixed point need not be the best one.

**Illustration (my construction).** A fair coin determines whether the agent sees *red* or *blue*. A perfect predictor pays \$10 if the agent's dispositions are (A on red, A on blue), \$5 if (B, B), and \$0 otherwise. Suppose the agent sees red and believes, perhaps from habit, that its blue node outputs B.

- Intervening on the red node: A yields \$0 and B yields \$5, so A-FDT picks B.
- The pair (B, B) is self-consistent under §5.2's condition.
- Yet the policy (A, A) is better.

Policy-FDT maximizes $\mathbb E[V\mid do(\textsc{fdt}=\pi)]$ over whole maps $\pi$ and selects (A, A). A-FDT optimizes one input-node at a time, so it is guaranteed only a kind of equilibrium across its own possible inputs. This is consistent with the paper's footnotes, which say the policy formalization is preferred and that the difference "will not make a difference in this paper" but matters in "certain multi-agent dilemmas." The example suggests it can also matter for a single agent whose possible inputs are linked by a predictor.

A practical recommendation, which is mine: when applying A-FDT, compute the policy-level optimum as well. If the two disagree, note that Equation (4) alone underdetermines the verdict until sibling-node beliefs are fixed.

### 5.4 Why not condition on $x$ as well?

Someone might add $\textsc{Obs}=x$ to the conditioning in (4). The paper's draft notes warn against this. Timeless decision theory both conditioned on evidence and switched intervention nodes, producing a harmful "double update." In transparent Newcomb, conditioning on *full* would erase the very dependence that makes one-boxing correct. Equation (4)'s omission of the conditioning is therefore deliberate.

### 5.5 Ties, randomization, and counterpossibles

The paper does not address several further details:
- tie-breaking within the argmax;
- whether $\mathcal A$ may include mixed actions;
- how predictors respond to randomization.

A reasonable convention is to include an explicit randomizing action whenever the problem allows one. One should also model *whether the predictor can predict the random source*. Death in Damascus shows that this choice is decisive. The paper argues that A-FDT, unlike CDT, correctly values a truly unpredictable coin at a 50% survival chance.

Underneath all of this sits the philosophical debt the paper openly acknowledges: Equation (4) evaluates *counterpossibles*, worlds in which a function outputs what it logically does not. The authors call this "technical rather than philosophical" and point to mathematicians' ordinary reasoning under logical uncertainty. They also argue that CDT incurs a parallel debt in deterministic worlds, where the physical act is likewise fixed.

## 6. A procedure for unfamiliar cases

Combining the source with the proposals above:

1. **List variables**, including outcomes, utilities, observation possibilities, and one decision node $\textsc{fdt}_y$ for each input $y$ the agent might face.
2. **Draw $G$.** Make $\textsc{Act}$ a child of whichever $\textsc{fdt}_y$ corresponds to the realized input. Make every predictor, copy or simulation of input $y$ a child of $\textsc{fdt}_y$, with error terms as separate parents. Leave merely correlated variables (lesions, coincidences) unconnected to the $\textsc{fdt}$ nodes.
3. **Fix beliefs about the non-intervened decision nodes**, ideally via the fixed-point condition of §5.2.
4. **For the actual input $x$**, compute $\mathbb E[V\mid do(\textsc{fdt}_x=a)]$ for each $a$. Do *not* condition on $x$; let worlds with other observations carry weight.
5. **Take the argmax.** As a check, compare it with the policy-level optimum and flag any divergence.

## 7. The philosophical case, briefly

The paper's arguments are mostly performance-based.

- **Precommitment.** CDT and EDT agents would pay to bind themselves to one-boxing or refusing blackmail. A-FDT agents simply act as they would have precommitted to act, and the paper claims they have no desire to self-modify, at least in fair problems.
- **Value of information.** EDT agents can rationally pay to avoid information. FDT agents, according to the paper, do not assign negative expected value to information.
- **Utility, which the authors treat as primary.** Predictors fill boxes for agents who predictably one-box, and blackmailers leave alone agents who predictably refuse.
- **Dominance.** CDT's appeal to dominance merely restates CDT's own way of constructing counterfactuals. "Every expected utility theory comes with its own notion of dominance," and under FDT-style counterfactuals FDT never chooses a dominated act.
- **Fairness.** Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." Problems that reward or punish an agent's *procedure* rather than its *behavior* are unfair to any theory.

The authors conjecture that FDT does at least as well as its rivals on every fair problem. They admit, in a footnote, that formalizing "fair" remains unsolved.

## 8. Conclusion

A-FDT is CDT with the intervention relocated, from the physical act to the logical output of the agent's decision function on its current input. Two consequences follow:

- Everything that computes or models that function moves with the intervention: predictors, twins, Death's book.
- Observations select the node rather than conditioning the distribution, so hypotheticals may include worlds where the agent sees something different.

Together these yield one-boxing, smoking, paying the driver, refusing blackmail below an error threshold of $10^{-3}$ in the mechanical case, and staying in Damascus, all from one rule.

The rule is precise only *given* a dependency graph $G$, and the source admits that no method yet exists for constructing $G$. I have also argued that A-FDT needs a convention for its beliefs about its own other decision nodes. Under such a convention it guarantees self-consistency but not global optimality, and the policy-level variant the authors prefer addresses exactly that gap. A reader who supplies $G$ and these sibling-node beliefs can compute A-FDT verdicts mechanically. The remaining disputes then concern which dependencies the world actually contains.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.