# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 1. The question A-FDT asks

Every expected-utility theory answers the same question, "which action maximizes expected utility?", but answers it relative to some way of imagining what would happen if the agent acted otherwise. Yudkowsky and Soares (2017) call this imagined scenario the agent's *hypothetical* for an action. They adopt Joyce's view that rival decision theories agree about value and disagree only about "the epistemic perspective from which actions are to be evaluated."

There are three standard perspectives:

- **Evidential decision theory (EDT)** forms the hypothetical by Bayesian conditioning on the act.
- **Causal decision theory (CDT)** forms it by a causal intervention (Pearl's $\mathtt{do}$) on the physical act.
- **The theory this essay explains** forms it by an intervention on a *logical* variable: the output of the agent's own decision function on its current inputs.

The paper calls this third theory FDT. It also notes (footnotes 7 and 16) that the authors' *preferred* formalization chooses policies rather than actions. To keep the two apart, I call the action-selecting rule of the paper's Equation (4) **action functional decision theory (A-FDT)**. I call the policy-selecting variant mentioned only in those footnotes **policy-selecting FDT**.

The slogan the paper offers is that a functional decision theorist asks "Which output of this decision procedure causes the best outcome?" rather than "Which physical act of mine causes the best outcome?" The motivating case is a prisoner's dilemma against a psychological twin. When an A-FDT agent imagines her reasoning concluding "defect," she must imagine her twin's identical reasoning concluding "defect" too, because both are computing the same function.

## 2. The formal definition

### 2.1 Ingredients

Fix the following:

- a finite action set $\mathcal A$;
- a countable set $\mathcal X$ of observation histories;
- outcomes $\mathcal O$;
- a bounded utility $\mathcal U$, with $V := \mathcal U(\textsc{Outcome})$.

The agent's world-model is a pair $(P, G)$:

- $P$ is a probability distribution over variables.
- $G$ is a graph that tells "how changing a logical variable affects all other variables."

Unlike CDT's graph, $G$ is not merely causal. Among its nodes are variables standing for the outputs of mathematical functions. In particular, for each observation $x' \in \mathcal X$ the agent might receive, there is a node
$$\textsc{fdt}(\underline P, \underline G, \underline{x'}),$$
standing for "what the A-FDT algorithm outputs when run on world-model $(P,G)$ and observation $x'$." The underlines denote dequoting: the node's *name* depends on the model, but its *value* need not be known in order to be represented. The paper appeals to Kleene's recursion theorem ("quining") to show that this self-reference is harmless.

### 2.2 Equation (4)

The primary formal statement (Section 5, Equation 4) is
$$
\mathrm{FDT}(P, G, x) := \operatorname*{argmax}_{a \in \mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\!\left(\textsc{fdt}(\underline P,\underline G,\underline x)= a\right)\right).
$$
I write the left-hand side as $\text{A-FDT}(P,G,x)$. Compare CDT's Equation (3):
$$
\mathrm{CDT}(P,G,x) := \operatorname*{argmax}_{a}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\right).
$$

The paper identifies exactly two differences:

1. **Point of intervention.** CDT intervenes on a node representing the physical action. A-FDT intervenes on a node representing the output of its decision procedure on its inputs. This is Peirce's type/token distinction: CDT varies the token, A-FDT the type.
2. **Treatment of observations.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $y$ instead of $x$ moves the intervention from $\textsc{fdt}(\ldots,\underline x)$ to $\textsc{fdt}(\ldots,\underline y)$.

### 2.3 The operational procedure

Read as an algorithm, Equation (4) says:

1. Build $(P,G)$, including logical nodes for your own algorithm's outputs on each possible input, and edges from those nodes to everything that subjunctively depends on them. This includes your own body's action, predictors' predictions, twins' choices, and so on.
2. For each $a\in\mathcal A$, perform the graph surgery $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$. Cut the node's incoming edges, set its value to $a$, propagate along outgoing edges, and leave non-descendants at their prior distribution.
3. Compute $\mathbb E(V)$ in each resulting distribution, and output the maximizer.

### 2.4 Subjunctive dependence

What licenses an edge from the logical node? The paper's informal criterion is *subjunctive dependence*. When two physical systems compute the same function, both behaviors "subjunctively depend" upon that function. The paper's examples:

- Two well-functioning calculators computing $6288+1048$ subjunctively depend on that sum.
- A scribe copying a calculator's output depends on it both causally and subjunctively. Causal dependence is described as "a special case of subjunctive dependence."
- Two calculators that happen to be pink are merely statistically correlated. Colouring one green would not change the other.

The defining slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

### 2.5 Why the $\mathtt{do}$-operator

The paper first writes an idealized version with a $\mathtt{true}$ operator that updates $P$ on a counterpossible logical sentence:
$$
\mathrm{FDT}^*(P, x)=\operatorname*{argmax}_{a} \mathbb E\left(V\mid\mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\right).
$$
It then concedes that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) sidesteps the problem. The logical dependency structure is supplied as input, in the graph $G$, "in the same way that the relevant causal structure is given as an input to CDT." This is the theory's principal open problem. The paper says that "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

### 2.6 When the three theories agree

The paper shows that EDT, CDT and A-FDT coincide when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the correlation with the agent's own algorithm node. In that case
$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=a)].
$$
A-FDT is distinctive only in "Newcomblike" problems, where something other than the action's own effects tracks the action. The usual example is a predictor or a copy.

## 3. Worked examples

All numbers are in dollars-as-utility. Following the paper, I write the observation-free node as $\textsc{fdt}(\underline P,\underline G)$ and the observation-indexed nodes as $\textsc{fdt}(\underline P,\underline G,\textit{obs})$.

### 3.1 Newcomb's problem (no observation)

The graph is $\textsc{fdt}(\underline P,\underline G)\to\textsc{Act}$ and $\textsc{fdt}(\underline P,\underline G)\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$. The predictor is accurate with probability $0.99$.

- **Intervening to one-box.** $\textsc{Act}=$ onebox, and box B is full with probability $0.99$:
$$\mathbb E V = 0.99\cdot 1{,}000{,}000 = 990{,}000.$$
- **Intervening to two-box.** Box B is full with probability $0.01$:
$$\mathbb E V = 0.01\cdot1{,}001{,}000+0.99\cdot1{,}000 = 11{,}000.$$

A-FDT one-boxes. The paper stresses that no retrocausation is assumed. The agent "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P,G)$ taking on a different value."

CDT, by contrast, holds $P(\text{full})=p$ fixed under $\mathtt{do}(\textsc{Act})$. Two-boxing then wins by exactly $1{,}000$ for every $p$.

### 3.2 The twin prisoner's dilemma

Both twins' actions are children of the same logical node.

- Setting it to *cooperate* yields $(C,C)$ and $1{,}000{,}000$.
- Setting it to *defect* yields $(D,D)$ and $1{,}000$.

A-FDT cooperates. CDT's dominance argument fails to apply because the twin's action is not held fixed under the intervention.

### 3.3 The smoking lesion

Here the modelling matters. The lesion is a common cause of the taste for smoking and of cancer. Cancer does not compute anything about the agent's algorithm, so there is **no** edge from any $\textsc{fdt}$ node to $\textsc{Cancer}$.

The paper formalizes the lesion as fixing which utility function, and hence which world-model $P_S$ or $P_R$, the agent's algorithm runs on. Accordingly, $\textsc{Act}$ is copied from either $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, depending on $\textsc{Lesion}$.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\text{lesion})=p$ unchanged. Let $q$ be the agent's belief about what the $P_R$-version does. Then

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot 1{,}000)$;
- refrain: $p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000)$.

Smoking wins by $p\cdot 1{,}000$. This is the probability that the intervened-on node actually controls the body, times the value of smoking.

The lesson is general and important. **The verdict is driven entirely by which edges $G$ contains.** The probability tables are identical, after renaming, to those in Newcomb's problem. The authors themselves recommend abandoning this dilemma as "badly confused," noting that EDT's distribution in it "lies to her."

### 3.4 Transparent Newcomb: observations change the node

Now the agent sees box B before choosing. There are two logical nodes, $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. $\textsc{Prediction}$ depends on the *full* node, and $\textsc{Prediction}$ also determines which node controls $\textsc{Act}$. Seeing a full box, the agent intervenes on $\textsc{fdt}(\ldots,\textit{full})$. Let $q$ be her prior that the *empty*-node outputs two-box.

- **Set it to one-box.** With probability $0.99$ the prediction is accurate, the box is full, and she gets $1{,}000{,}000$. With probability $0.01$ the box is empty and the other node acts, giving $1{,}000q$ in expectation. Total: $990{,}000+10q$.
- **Set it to two-box.** With probability $0.99$ the box is empty, giving $1{,}000q$. With probability $0.01$ the box is full and she takes both, giving $1{,}001{,}000$. Total: $10{,}010+990q$.

A-FDT one-boxes even while looking at a full box. Two features of this calculation deserve emphasis.

**First, the computation does not condition on $\textsc{Obs}=\textit{full}$.** The worlds in which the box is empty contribute to the expectation. This matches Equation (4), which contains no conditioning term. However, the paper's displayed objective in this section is written
$$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full}))$$
(with an unbalanced parenthesis). Read literally, that would conflict with both Equation (4) and the arithmetic. If one conditioned on a full box after the intervention, two-boxing would win. The paper's numbers are consistent only with *no* conditioning. Its own footnote also warns that an earlier variant which "prescribes both conditioning on evidence *and* changing the place where one intervenes" suffers a harmful "double update." I therefore read Equation (4) literally: **observations select the node; they are not conditioned on.**

**Second, a misprint.** The source prints the two-boxing total as "$\$110{,}00 + q\cdot\$990$". The correct value under the stated model is $\$10{,}010+990q$. The verdict is unaffected for every $q\in[0,1]$.

### 3.5 Blackmail problems and thresholds

**Mechanical blackmail.** The blackmailer runs the program only if she predicts payment. Intervening on $\textsc{fdt}(\ldots,\textit{blackmail})$:

- *Pay*: she is blackmailed and loses $1{,}000$.
- *Refuse*: she is blackmailed only through predictor error at rate $\varepsilon$, and then loses $1{,}000{,}000$.

So A-FDT refuses iff $10^6\varepsilon<10^3$, that is, iff $\varepsilon<0.1\%$.

The paper's example $\varepsilon=0.09\%$ (expected loss $900$) gives refusal, as stated. The paper then says that at an error rate of "0.011%" she pays. Under the stated payoffs this is inconsistent, since $0.011\%<0.1\%$. It is presumably intended as $0.11\%$. The point to take away is the threshold structure: A-FDT is not dogmatically "anti-extortion." It compares the two hypotheticals, and the predictor's reliability matters.

**XOR blackmail.** Intervening on the *letter* node changes whether the letter is sent but not whether there are termites. Refusing therefore costs nothing in the hypothetical, and A-FDT refuses. CDT also refuses, but for a different reason: it holds the letter fixed and imagines the infallible predictor having erred.

### 3.6 Death in Damascus

Death's appointment book is written from an accurate prediction of the agent's algorithm. So Death's location is a child of the logical node. Setting the node to *Aleppo* puts Death in Aleppo, and setting it to *Damascus* puts Death in Damascus. Both hypotheticals contain death, and fleeing costs $1{,}000$, so A-FDT stays.

This is a stable answer, with no deliberational oscillation. CDT, which holds Death's location independent of its act, keeps wanting to move. According to the paper, CDT will even decline a truly random coin offered for \$1 that would give a 50% survival chance.

## 4. How to apply A-FDT to an unfamiliar case

The source supplies the equation; the following checklist is my own distillation of how the paper builds its graphs.

1. **List the agent's possible inputs** $x'\in\mathcal X$. Create a logical node for the algorithm's output on each one.
2. **Locate every implementation or model of those nodes.** These include the agent's body, copies, twins, simulations, and predictors that reason about the algorithm. Each gets an edge from the relevant node, mixed with noise variables where accuracy is imperfect, as with $\textsc{Accurate}$ in Newcomb.
3. **Locate merely statistical correlates.** Lesions and coincidences get no edge from the logical node, even when they correlate with the act.
4. **Model what determines which input the agent receives.** In the transparent and blackmail problems this is often the predictor's output. $\textsc{Act}$ is then a "switch" that copies whichever logical node corresponds to the realized input.
5. **Assign priors** to all non-intervened logical nodes, and to all upstream variables.
6. **Intervene on the node for the actual input $x$**, propagate, compute $\mathbb E V$ without conditioning on $x$, and take the argmax.

Two heuristics follow from the paper's treatment of dominance and precommitment:

- A-FDT "acts as it would have precommitted to act," at least where the relevant dependence runs through the single intervened node.
- Its notion of dominance holds the subjunctive dependencies fixed. So "two-boxing dominates" is, in the paper's words, "merely a restatement of CDT's method."

## 5. What the source leaves open, and how one might close it

### 5.1 Where $G$ comes from

Equation (4) is conditional on a correct dependency graph. The paper provides no criterion for when a predictor's model counts as "computing the same function." It offers no account of partial similarity, as with a colleague who reasons *somewhat* like you, and no learning procedure analogous to Pearl's causal discovery.

A practical proposal of my own: model each external system as a mixture. With weight $\rho$ it copies the logical node, and with weight $1-\rho$ it follows an independent process. Here $\rho$ is estimated from the system's track record or from structural similarity. Newcomb's $0.99$ accuracy is the special case $\rho\approx 0.98$, since the remainder must account for chance agreement as well. This makes A-FDT continuous in the degree of dependence, but the choice of $\rho$ is an extra modelling assumption, not part of the source.

### 5.2 Counterpossibles

The agent's algorithm has only one actual output. Interventions setting it otherwise are counterpossible. The paper argues that this is no worse than CDT's position under determinism: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." Accepting this parity argument is a philosophical commitment, not a theorem.

### 5.3 Beliefs about the other logical nodes

In the transparent-Newcomb and lesion computations, the non-intervened node carries an arbitrary prior $q$. The paper notes that its verdicts there are insensitive to $q$. That insensitivity is a feature of those examples, not a general property.

Here is my own illustration of where it fails. A fair coin shows the agent $L$ or $R$. A perfect predictor pays $10$ if the agent's outputs on both inputs are $A$, pays $5$ if both are $B$, and pays $0$ otherwise. Suppose the agent sees $L$ and believes $P(\textsc{fdt}(\ldots,R)=B)=\pi$. Intervening on $\textsc{fdt}(\ldots,L)$ gives
$$
\mathbb E V(A)=10(1-\pi),\qquad \mathbb E V(B)=5\pi .
$$
So the agent chooses $B$ iff $\pi>2/3$. If she confidently expects her $R$-self to choose $B$, A-FDT ratifies the inferior pair $(B,B)$. Joint policy optimization would select $(A,A)$.

This is plausibly why the authors prefer policy-selecting FDT, which intervenes on a node whose value is a whole mapping $\mathcal X\to\mathcal A$ and then applies it to $x$. They say the difference matters "in certain multi-agent dilemmas." My example suggests it can matter whenever the payoff depends on the agent's behavior across several inputs.

For users of A-FDT as defined by Equation (4), I propose two disciplines:

- set beliefs about the other nodes by requiring consistency, so that each node's prior matches what A-FDT would output there;
- when several consistent profiles exist, flag the case as one where A-FDT is underdetermined and policy-selecting FDT should be consulted.

### 5.4 Ties, fairness, and scope

Equation (4) does not specify a tie-breaking rule. The paper also claims superiority only on "fair" problems, where outcomes depend on the agent's *behavior* rather than on the procedure that produces it. It admits that no formal definition of fairness yet exists. Its footnote 15 gives a case that defeats every candidate definition the authors tried: a copy of the agent is used to punish anyone who matches it.

## 6. Philosophical motivation in brief

The paper's case rests on three arguments.

- **The argument from utility.** A-FDT agents walk away rich in Newcomb's problem, smoke harmlessly, are carried out of Parfit's desert, and are not targeted by blackmailers.
- **The argument from precommitment.** CDT and EDT agents would pay to bind themselves to exactly what A-FDT does unaided. The authors take a theory that recommends replacing itself to be a weak candidate for the normative theory of choice.
- **The argument from the value of information.** A-FDT never pays to blindfold itself, whereas EDT sometimes does.

Underlying all three is a diagnosis. The paper says "EDT respects too many action-environment correlations, while CDT respects too few." A-FDT breaks correlations that are merely statistical and preserves those that hold because something else is computing, or modelling, the same function.

Through Joyce's representation theorem, A-FDT remains a standard expected-utility theory. It differs from CDT only in the constraints it places on hypotheticals: they must respect logical as well as causal structure.

## 7. Conclusion

A-FDT is CDT with the surgery moved. The intervention moves from the physical act to the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$, and the observation is used to choose the node rather than to condition the distribution.

Applying it amounts to drawing an honest graph of which variables subjunctively depend on one's own algorithm, then computing a Pearl-style intervention. This yields one-boxing, cooperation with twins, smoking, refusing extortion below a reliability threshold, and staying in Damascus.

The hard work lies outside the equation: constructing $G$, interpreting counterpossibles, and fixing beliefs about one's behavior on other inputs. The last of these is exactly where the action-selecting A-FDT and policy-selecting FDT can come apart. Readers applying A-FDT should treat Equation (4) as exact given a model, and treat the model itself as the place where judgment, and further theory, is required.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.