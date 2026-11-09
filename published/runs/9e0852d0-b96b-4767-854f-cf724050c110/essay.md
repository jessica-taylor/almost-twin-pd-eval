# A-FDT: Choosing the Output of a Function Rather Than an Act

## 1. The question A-FDT asks

Yudkowsky and Soares (2017) present a family of views they call *functional decision theory*. Its central idea is that a deliberating agent should treat her decision as the output of a fixed mathematical function, and ask, in the paper's words, "Which output of this very function would yield the best outcome?" Her body is one physical implementation of that function. A predictor's simulation of her, or a psychological twin, may be another.

This essay covers one precise version of the idea. It is the formula given as Equation (4) in Section 5 of the paper, where the agent maximizes over **actions** given her current observation. I call this version **A-FDT** (action functional decision theory). The label matters because the paper notes, in footnotes 7 and 16, that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I call that variant **P-FDT** when I compare the two. The two standard rivals are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Throughout, I separate three kinds of claim:

- **(S)** marks what the source says.
- **(I)** marks my interpretation of something the source leaves implicit.
- **(P)** marks my own proposals.

## 2. The common template: expected utility with a hypothetical connective

**(S)** All three theories maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective that each theory interprets differently. Following Joyce (1999), the paper treats the theories as agreeing about value and disagreeing about "the epistemic perspective from which actions are to be evaluated."

Write $V := \mathcal U(\textsc{Outcome})$. The two classical rules are:

$$
\text{EDT}(P,x) = \arg\max_{a} \mathbb E\,[V \mid \textsc{Obs}=x,\ \textsc{Act}=a] \tag{2}
$$

$$
\text{CDT}(P,G,x) = \arg\max_{a} \mathbb E\,[V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x] \tag{3}
$$

EDT conditions on the act. CDT performs Pearl-style surgery on the physical act node in a causal graph $G$. Surgery sets the node to a value, cuts its incoming arrows, and propagates only downstream.

## 3. The definition of A-FDT

**(S)** Equation (4) defines A-FDT:

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left[V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right]\;} \tag{4}
$$

The ingredients are as follows.

- **$P$** is the agent's probability distribution over world variables. It includes variables standing for the *outputs of mathematical functions*. One example is a variable for the value of $6288+1048$, "that (hopefully) has most of its probability on 7336."
- **$G$** is a graph that says "how changing a logical variable affects all other variables." It encodes *subjunctive dependence* as well as ordinary causation.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the node representing what the A-FDT algorithm outputs on the agent's own inputs. The underlines denote dequoting: the node's name is built from the inputs.
- **$\mathtt{do}$** is Pearl's operator. Here it is applied to this logical node rather than to $\textsc{Act}$.

The model refers to itself, since $P$ and $G$ contain a node named after $P$ and $G$. The source calls this self-reference harmless. The agent needs only a variable *representing* her output, not its value, and Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.

**(S)** Equation (4) differs from Equation (3) in two ways:

1. **The intervention point.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the *type*, meaning the function's output. Everything downstream of that output in $G$ moves with it: the agent's body, a predictor's forecast, a twin's choice.
2. **The role of observation.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Seeing $y$ instead of $x$ moves the intervention from $\textsc{fdt}(\ldots,x)$ to $\textsc{fdt}(\ldots,y)$.

**A notational wrinkle.** In the transparent Newcomb computation the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a), \textsc{Obs}=\textit{full})$, with a dangling parenthesis. Yet the calculation it then carries out averages over the branch where the box is *empty*, so it does not condition on the observation.

**(I)** I take the boxed Equation (4), which has no conditioning on $\textsc{Obs}$, as authoritative. This reading also matches the source's later footnote rejecting the "double update" of the earlier Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes." Under A-FDT, observation enters *only* through which node is intervened on. Every other uncertainty is averaged under $P$.

## 4. Subjunctive dependence: what goes into $G$

The graph $G$ carries all of A-FDT's power, and almost all of its unresolved difficulty.

**(S)** The source offers a slogan: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" Two systems computing the same function both subjunctively depend on that function, much as two working calculators computing $6288+1048$ do. Two further points:

- Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's output depends on it both ways.
- Mere correlation is not subjunctive dependence. Two calculators that happen to be pink do not depend on each other's colour.

The decisive contrast is between a predictor, which "builds an accurate model of the agent and reasons about her behavior," and a carcinogenic lesion, which "does no such thing."

**(S)** The source admits that it gives no procedure for building $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." The intended semantics is a counterpossible: what would be different if this algorithm had a different output? The source mentions a $\mathtt{true}(\cdot)$ operator that would make this precise, but says "it's not clear how to define" it. Equation (4) sidesteps the issue by requiring the dependency structure as an *input*, in the same way CDT takes the causal graph as given.

**(P)** For hand-solving cases, I suggest the following recipe for constructing $G$:

1. **Locate implementations.** Find every process in the problem whose output is determined, reliably, by evaluating or modelling the agent's decision function on a particular input. Examples are the agent's body, a twin, a predictor's simulation, and a future self facing an identical decision.
2. **Add one node per input.** Create a node $\textsc{fdt}(\underline P,\underline G,y)$ for each input $y$ the agent might receive, including inputs she has not in fact received.
3. **Draw arrows from these nodes.** Draw an arrow from each such node to every process that implements or predicts the function *at that input*. Model imperfect reliability with an exogenous noise parent, such as $\textsc{Accurate}$.
4. **Route the agent's act.** Make $\textsc{Act}$ a deterministic switch. Whichever input the world actually supplies selects which $\textsc{fdt}$ node drives the body.
5. **Exclude mere correlates.** Draw no arrow from any $\textsc{fdt}$ node to a variable that is merely correlated with the agent's behaviour, such as lesions or genes. Such variables may still be causal *parents* of which function the agent runs.

The source's own graphs for Newcomb, the transparent variant, the smoking lesion, and both blackmail problems all fit this recipe. Step 1 is where real judgement is needed. Deciding whether a crude human forecaster "implements" one's function is exactly the open problem.

## 5. Applying the rule: worked cases

### Twin prisoner's dilemma

**Setup.** One node $f$ drives both the agent's act and the twin's act. Mutual cooperation pays $1{,}000{,}000$, mutual defection pays $1{,}000$, and a lone defector gets $1{,}001{,}000$.

**Evaluation.**

- $\mathtt{do}(f=\textit{cooperate})$ yields $1{,}000{,}000$.
- $\mathtt{do}(f=\textit{defect})$ yields $1{,}000$.

**Verdict.** A-FDT cooperates. CDT defects, because it holds the twin fixed.

### Newcomb's problem (99% predictor)

**Setup.** The node $\textsc{fdt}(\underline P,\underline G)$ drives both $\textsc{Act}$ and $\textsc{Prediction}$. The predictor is accurate with probability 0.99. Box B holds $1{,}000{,}000$ if one-boxing was predicted; box A holds $1{,}000$.

**Evaluation.**

$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] = 0.99(1{,}000{,}000)=990{,}000,
$$

$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

**Verdict.** A-FDT one-boxes. Under CDT's graph, $\textsc{Box B}$ is not downstream of $\textsc{Act}$, so two-boxing wins by $1{,}000$ whatever the agent believes about the box.

**A common objection.** If the agent is almost sure that box B is full, why not take both? **(S)** The source answers that to imagine two-boxing she must imagine the *function* outputting *twobox*. In that counterpossible world the predictor's model outputs it too. No backward causation is involved.

### Smoking lesion

**Setup.** **(S)** The lesion is a causal parent of *which* decision function the agent runs. With the lesion, she runs the function with preferences $\mathcal U_S$, which values smoking. Without it, she runs the function with $\mathcal U_R$. Concretely, $\textsc{Act}(\textit{lesion},s,r)=s$ and $\textsc{Act}(\textit{nolesion},s,r)=r$. The lesion also causes cancer. No $\textsc{fdt}$ node points to $\textsc{Cancer}$.

**Evaluation.** Let $p$ be the probability of the lesion and $q$ the agent's belief that the non-lesion function smokes. Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. The two options are:

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q)$
- refrain: $p(10{,}000)+(1-p)(990{,}000+1{,}000q)$

The difference is $1{,}000\,p>0$.

**Verdict.** A-FDT smokes, and it does so for any value of $q$. EDT refrains because smoking is bad news; CDT smokes.

### Transparent Newcomb (seeing box B full)

**Setup.** There are two nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. The prediction concerns the *full* node. The prediction also determines what the agent sees, and so which node drives $\textsc{Act}$. Let $q$ be her prior that she two-boxes when she sees an empty box.

**Evaluation.** Intervening on the *full* node:

- onebox: $0.99(1{,}000{,}000)+0.01\cdot 1{,}000q = 990{,}000+10q$
- twobox: $0.01(1{,}001{,}000)+0.99\cdot 1{,}000q = 10{,}010+990q$

**Verdict.** A-FDT one-boxes for every $q\in[0,1]$, even while looking at a full box. CDT and EDT both two-box, and so they get empty boxes.

**A transcription error in the source.** The paper prints the two-box value as "\$110,00 + q·\$990." The correct constant is $10{,}010$. The verdict is unaffected.

**The source's defence of this verdict.** **(S)** The paper identifies this case with Parfit's hitchhiker, where A-FDT pays the driver. It defends the verdict with three arguments:

1. **From precommitment.** CDT and EDT agents would *precommit* to one-boxing if given the chance.
2. **From the value of information.** A-FDT agents never assign negative value to information.
3. **From utility.** Agents who predictably one-box see full boxes.

### XOR blackmail and mechanical blackmail

**XOR blackmail.** **(S)** The letter's arrival depends on both the infestation and the $\textsc{fdt}(\ldots,\textit{letter})$ node, but the infestation does not depend on that node. Paying therefore changes only whether the letter is sent, not whether there are termites. A-FDT refuses, as CDT does. EDT pays, because paying is "good news."

**Mechanical blackmail: setup.** **(S)** The blackmailer runs a program that will publish damaging information unless the agent pays $1{,}000$. She runs it iff she predicts the agent would pay. Her prediction depends on the *blackmail* node.

**Evaluation.** Let $\varepsilon$ be the probability that she wrongly predicts payment from a refuser. Then:

- If the agent pays, she is always blackmailed and loses $1{,}000$.
- If she refuses, she is blackmailed with probability $\varepsilon$ and loses $10^6\varepsilon$ in expectation.

So A-FDT refuses iff $\varepsilon<0.001$.

**Verdict and a likely misprint.** The paper's case of $\varepsilon=0.0009$ gives "\$900" and refusal, which agrees with this threshold. The paper then says the agent pays at "0.011%." That cannot be right, because $\varepsilon=0.00011$ gives an expected loss of only $110$, so the agent would still refuse. **(I)** The authors probably meant 0.11%. The threshold itself follows directly from Equation (4).

### Death in Damascus

**Setup.** A perfect predictor (Death) will meet the agent wherever she goes tomorrow. Fleeing to Aleppo costs $1{,}000$.

**Evaluation.** One node drives both the agent's location and Death's appointment book. Every intervention yields death, and fleeing adds the $1{,}000$ cost.

**Verdict.** A-FDT stays in Damascus, with no instability.

**Contrast with CDT.** **(S)** The source argues that CDT oscillates. Whatever it expects to do, it prefers the other city, because its hypotheticals hold Death's location fixed. With ratification it lands on roughly a 50/50 mixture. It would even refuse to pay \$1 for a truly random coin offering a genuine 50% chance of survival. A-FDT, by contrast, values that coin correctly, since a true coin toss is not downstream of the $\textsc{fdt}$ node.

## 6. General properties

**Agreement in ordinary cases.** **(S)** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the $\textsc{fdt}$ node itself. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories agree. They come apart only when something other than the act's own effects tracks the decision, for example predictors, copies, or simulations.

**No zero-probability problem.** **(I)** EDT is undefined for acts the agent assigns probability 0. A-FDT is not, because $\mathtt{do}$ sets a node regardless of its prior. Even an agent nearly certain of her own output can evaluate the alternative. This is why, in the source's words, Fiona (the paper's A-FDT agent) can be "quite sure" box B is full and still coherently consider what two-boxing would mean.

**A matching dominance notion.** **(S)** Every way of constructing hypotheticals generates its own dominance principle. Under A-FDT counterfactuals, which hold subjunctive dependencies fixed, two-boxing is dominated. The source's conclusion is that "dominance doesn't afford us a neutral criterion," so it judges theories by the utility they achieve in "fair" problems: those where beliefs are accurate and outcomes depend only on the agent's behaviour, not on how she reasons.

**Reflective stability and "control".** **(S)** The source claims that A-FDT agents never wish to switch to CDT mid-problem, so A-FDT is "reflectively stable in fair problems." It also argues that the charge that A-FDT agents falsely believe they "control" logical facts applies equally to deterministic CDT agents "controlling" their physical acts.

## 7. Open questions and how to handle them

### 7.1 Beliefs about one's other branches

When A-FDT intervenes on $\textsc{fdt}(\ldots,x)$, the nodes for other inputs $y\neq x$ keep their prior distribution. The quantity $q$ in the transparent Newcomb and lesion cases is such a prior. **(S)** In the paper's examples the verdict is the same for every $q$. Nothing in Equation (4) guarantees this in general.

**(P)** A natural operational rule is *self-consistency*: the agent's beliefs about $\textsc{fdt}(\ldots,y)$ should put full weight on what A-FDT actually outputs at $y$. In finite problems one can search for such fixed points by solving each branch given guesses about the others. My next example shows that this can have several solutions.

**(P) A coordination example.** A perfect predictor shows the agent signal $y_1$ or $y_2$ with probability ½ each. The agent then picks $A$ or $B$. Payoffs depend on her whole policy:

- $10$ if she picks $B$ under both signals;
- $1$ if she picks $A$ under both signals;
- $0$ otherwise.

Suppose that at $y_1$ she believes her $y_2$-node outputs $A$. Intervening on her $y_1$-node then gives

$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\ldots,y_1)=A)] = 1, \qquad \mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\ldots,y_1)=B)] = 0,
$$

so A-FDT picks $A$. By symmetry the same holds at $y_2$. The policy $(A,A)$ is therefore a self-consistent A-FDT solution, and so is $(B,B)$.

P-FDT avoids this. It intervenes once on a node whose values are whole maps $\pi:\mathcal X\to\mathcal A$, and so selects $(B,B)$ directly. This illustrates the source's remark that the policy formulation "makes a difference in certain multi-agent dilemmas." In my example the "other agent" is the agent's own counterpart at a different input.

**(P) Practical guidance.** When applying A-FDT to a new case:

1. **Compute the verdict across all $q$.** If it is robust, as in all the source's examples, report it.
2. **If it is not robust, list the self-consistent assignments.** Treat the choice among them as an equilibrium-selection problem that Equation (4) leaves open.
3. **Note where P-FDT differs.** P-FDT picks the policy with the best ex-ante value; A-FDT may not.

### 7.2 Ties

Equation (4) returns an argmax *set*, and the source specifies no tie-breaking rule.

**(P)** Any fixed deterministic rule will do. It must be part of the function, though, because predictors predict the function including its tie-breaker.

### 7.3 Building $G$ and fairness

Section 4 covered the first problem. The second is that the source's notion of a "fair" problem is informal, and its own footnote 15 notes difficulties. One example is a game that punishes anyone who acts like a copy of the A-FDT agent.

**(P)** A workable criterion for fairness is invariance. Outcomes should depend on the agent's function only through its input-output behaviour, and any predictor should be equally accurate whichever function produces that behaviour.

## 8. A procedure for unfamiliar cases

Pulling the above together, here is how to apply A-FDT to a new problem:

1. **Specify the variables and $P$.** Include the chance nodes, outcomes, and $V$.
2. **Build $G$ using the recipe in §4.** Create one $\textsc{fdt}$ node per possible input, draw arrows to every implementation or prediction of the function at that input, and make $\textsc{Act}$ a switch on the realized input.
3. **Choose the intervention node.** Use the agent's actual input $x$. Do not additionally condition on $x$.
4. **Evaluate each action.** For each $a$, compute $\mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\ldots,x)=a)]$, keeping priors on the other $\textsc{fdt}$ nodes.
5. **Check robustness.** Vary those priors. If the verdict changes, apply the fixed-point analysis of §7.1 and compare with P-FDT.
6. **Take the argmax,** using a declared tie-breaking rule.

## 9. Conclusion

A-FDT, as given by Equation (4), keeps CDT's machinery of expected utility plus graph surgery. It moves the point of surgery from the physical act to the logical output of the agent's own decision function, and it lets observations select the intervention point instead of being conditioned on. The resulting verdicts are:

- one-box in Newcomb's problem;
- smoke in the smoking lesion problem;
- pay the driver in Parfit's hitchhiker;
- refuse both kinds of blackmail;
- stay put in Damascus.

The source argues that this pattern achieves the most utility in fair problems. The formula itself is short. What remains open is everything Equation (4) takes as given: how to construct the subjunctive-dependence graph, how counterpossibles are to be understood, what to believe about one's own other branches, and how to define fairness. The action-level version also differs from the authors' preferred policy-level version in coordination-like cases. Readers can apply A-FDT reliably whenever the dependency structure is clear and the verdict is robust to beliefs about other branches. Outside those conditions, applying it requires the additional assumptions identified in §7.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.