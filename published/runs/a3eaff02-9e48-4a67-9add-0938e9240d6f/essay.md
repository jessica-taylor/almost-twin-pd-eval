# A-FDT: Choosing as the Output of a Function

## 1. What is being explained, and what it is called

Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose that a rational agent should treat her decision as the output of a fixed mathematical function. That function asks: "Which output of this very function would yield the best outcome?" Their primary formal statement is Equation (4) of Section 5. In it the agent intervenes on a variable standing for *what her decision procedure outputs, on her current input*. The value assigned to that variable is an **action**.

The authors call this rule FDT. Two footnotes (7 and 16) say that "in the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions." To keep the two apart, this essay uses two names:

- **A-FDT (action functional decision theory)** is the rule of Equation (4).
- **P-FDT** is the policy-selecting variant mentioned only in the footnotes.

Where I quote the paper, "FDT" refers to the theory as the authors state it. In this essay's context that is A-FDT unless the quotation concerns policies. The paper compares A-FDT with **CDT** (causal decision theory) and **EDT** (evidential decision theory). I keep those names for those theories.

Throughout, I mark which claims belong to the source and which are my own interpretation or proposal.

## 2. The common frame: expected utility over hypotheticals

The paper places all three theories inside one schema (Equation 1). The agent picks the action $a$ that maximizes

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here $x$ is the observation history and $\hookrightarrow$ is a connective for "decision hypotheticals" that is deliberately left uninterpreted. Following Joyce, the authors treat the theories as agreeing about value and disagreeing only about "the epistemic perspective from which actions are to be evaluated." Concretely, the agent holds a world-model $M$. For each action she builds a *hypothetical* $M^{a\hookrightarrow}$ and scores it. The source describes hypotheticals as "decision-theoretic instruments constructed from beliefs," not as beliefs.

With $V := \mathcal U(\textsc{Outcome})$, the two rival theories are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a) \tag{2}$$

$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x\big) \tag{3}$$

In (3), $G$ is a causal graph over the variables of $P$. Pearl's $\mathrm{do}$ operator sets $\textsc{Act}=a$, cuts the arrows into $\textsc{Act}$, and recomputes only what lies downstream. The two theories handle correlations differently:

- EDT keeps every correlation between act and world.
- CDT keeps only those the act causes.

## 3. The definition of A-FDT

Equation (4) of the paper reads, in the paper's notation:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

This is what I call A-FDT. The ingredients are as follows.

1. **$P$** is a probability distribution. It contains variables for physical quantities and also for *logical* quantities, such as the value of $6288+1048$ or the output of particular algorithms on particular inputs.

2. **$G$** is a graph. It tells the agent how changing the value of a logical variable propagates to other variables. The paper says $P$ must "come augmented with information about the logical, mathematical, computational, causal, etc. structure of the world more broadly." Causal arrows are a special case: the source says "causal dependence is a special case of subjunctive dependence."

3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node of the model. Underlining denotes dequoting, so this node is the variable *named by* the agent's actual inputs. It represents "the output of A-FDT when run on $(P,G,x)$."
   - The self-reference is legitimate by Kleene's recursion theorem ("quining").
   - The agent needs a variable *representing* her output, not knowledge of its *value*.

4. **$\mathrm{do}$** is Pearl's operator, reused unchanged. What is new is *where* it is applied.

The paper names two structural differences from (3). First, A-FDT intervenes on a logical node rather than on the physical $\textsc{Act}$. Second, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." There is no "$\textsc{Obs}=x$" to the right of the bar in (4). The observation enters only through the *name* of the node.

### 3.1 The procedure in steps (my summary)

1. Write down a model $(P,G)$ of the whole problem. Include every system whose behaviour is fixed by your decision function on some input: your own body, predictors, twins, copies, and the behaviour of your function on observations you did *not* receive.
2. Identify the node $\textsc{fdt}(\underline P,\underline G,\underline x)$ for your actual observation history $x$.
3. For each $a\in\mathcal A$, form $P(\cdot\mid \mathrm{do}(\textsc{fdt}(\ldots,\underline x)=a))$.
   - Everything downstream of the node in $G$ is recomputed.
   - Everything else, including nodes for your function on *other* inputs, keeps its prior distribution.
4. Compute $\mathbb E V$ under each hypothetical and output the argmax.

### 3.2 Subjunctive dependence

The source's guiding slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" Two physical systems that compute the same function both subjunctively depend on that function, like two calculators computing $6288+1048$. A merely statistical correlation does not create a dependence: a pink calculator in Paris and another in Tokyo. CDT intervenes on the *token* "my action is $a$". A-FDT intervenes on the *type*.

A predictor that builds an accurate model of the agent therefore receives an arrow from the agent's $\textsc{fdt}$ node. A lesion, which "is not evaluating the agent's future decisions," receives no such arrow.

### 3.3 When A-FDT agrees with its rivals

The source notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G)=a)],$$

and all three theories coincide. The only possible exception is $\textsc{fdt}$ itself, on which $\textsc{Act}$ depends. The theories come apart only when something correlates with your act without being its effect, and above all when something *predicts* you.

## 4. Worked cases

All numbers below use the source's models: a 99%-accurate predictor, $1,000,000 and $1,000 stakes, and dollars standing in for utility.

### 4.1 Newcomb's problem

Fiona's graph has $\textsc{fdt}(\underline P,\underline G)$ as a common parent of $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Accurate}$ is an independent noise parent of $\textsc{Prediction}$, and $\textsc{Prediction}$ determines $\textsc{Box B}$. Then

$$\mathbb E[V\mid\mathrm{do}(\textsc{fdt}=\textit{onebox})] = 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,$$

$$\mathbb E[V\mid\mathrm{do}(\textsc{fdt}=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. In CDT's graph, $\textsc{Box B}$ is not downstream of $\textsc{Act}$. For any fixed $p=P(\textit{full})$, two-boxing gains exactly $1,000, so CDT two-boxes.

The source stresses that no retrocausation is assumed. The agent imagines the predictor's prediction varying because the prediction and the act are two outputs of one function.

### 4.2 Twin prisoner's dilemma

The same structure appears with the twin in place of the predictor. Both players' moves are children of the same $\textsc{fdt}$ node. The comparison is therefore $(C,C)\mapsto 1{,}000{,}000$ against $(D,D)\mapsto 1{,}000$, and A-FDT cooperates.

The source calls Newcomb's problem and this dilemma isomorphic, following Lewis.

### 4.3 The smoking lesion

Here the modelling matters. The lesion makes the agent *like* smoking, so the source introduces two utility functions:

- $\mathcal U_S$, for an agent who values smoking at $1,000;
- $\mathcal U_R$, which values smoking at $-1$.

There are correspondingly two possible world-models $P_S, P_R$ and two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The graph has $\textsc{Act}(\textit{lesion},s,r)=s$ and $\textsc{Act}(\textit{nolesion},s,r)=r$. $\textsc{Lesion}$ points to $\textsc{Cancer}$, but neither decision node points to $\textsc{Cancer}$.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. The two hypotheticals therefore differ only in the smoking bonus, which applies when this node actually controls the act:

$$\mathbb E[V\mid \mathrm{do}(\cdot=\textit{smoke})]-\mathbb E[V\mid \mathrm{do}(\cdot=\textit{refrain})] = p\cdot 1{,}000 > 0.$$

A-FDT smokes. Note that the agent's credence $q$ about the *other* node's output drops out of the difference. That will matter in §6.

The source also calls the problem "badly confused" and recommends that philosophers abandon it. The main reason is that an accurate model for an EDT agent in an EDT population would show no correlation between smoking and the lesion.

### 4.4 Transparent Newcomb

Box B is visible. The predictor fills it iff she predicts one-boxing *upon seeing it full*. There are now two decision nodes:

- $\textsc{fdt}(\ldots,\textit{full})$, which feeds $\textsc{Prediction}$;
- $\textsc{fdt}(\ldots,\textit{empty})$.

$\textsc{Prediction}$ selects which of the two controls $\textsc{Act}$. Seeing a full box, the agent intervenes on the first node. Let $q$ be her prior that she two-boxes when facing an empty box.

- **One-box:** $0.99\cdot1{,}000{,}000 + 0.01\cdot q\cdot 1{,}000 = 990{,}000+10q$.
- **Two-box:** $0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = 10{,}010+990q$.

(The source prints the second figure as "\$110,00 + $q\cdot$\$990". The arithmetic of its own model gives \$10,010.)

A-FDT one-boxes for every $q\in[0,1]$, even though the agent *sees* a full box. Her two-boxing hypothetical is one in which, with 99% probability, she would have been shown an empty box.

The source equates this with paying the driver in Parfit's hitchhiker problem: the driver rescues you iff she predicts you will pay once you are in the city. It defends the verdict with three arguments:

- **Precommitment:** CDT and EDT agents would themselves pay to bind themselves to one-boxing.
- **Value of information:** an A-FDT agent never assigns negative value to information.
- **Utility:** A-FDT agents walk away rich.

The source regards the utility argument as decisive.

### 4.5 Two blackmail problems

**XOR blackmail.** The letter arrives iff exactly one of these holds: no termites and you will pay, or termites and you will not pay. EDT pays, because conditioning on paying drives $P(\textit{termites})$ to 0.

A-FDT's intervention on $\textsc{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent, but it is not upstream of $\textsc{Infestation}$. Termites cost the same in every hypothetical, and paying adds $1,000 of cost. A-FDT refuses. CDT also refuses, for a different reason. If you ask what would have happened had she paid, CDT's hypothetical says the infallible predictor erred. A-FDT's says she would never have received the letter.

**Mechanical blackmail.** The blackmailer runs a damaging program only if she predicts payment. The program costs $1,000,000 if it runs and can be stopped only by paying $1,000. Let $\varepsilon$ be the probability that the blackmailer wrongly predicts payment from a refuser. Intervening on $\textsc{fdt}(\ldots,\textit{blackmail})$ gives:

$$\text{pay: } -1{,}000;\qquad \text{refuse: } -\varepsilon\cdot 1{,}000{,}000 .$$

A-FDT refuses iff $\varepsilon<10^{-3}$. The source's $\varepsilon=0.0009$ gives $-900$, so she refuses even while holding the letter. The source then says she pays if the error rate is "0.011%". By the formula above, the threshold is 0.1%, so presumably 0.11% was intended.

A-FDT's verdict here is to refuse even after being blackmailed, accepting the large loss in the rare world where the prediction was wrong. The source accepts this explicitly: it is "advantageous to be *the kind of agent* that makes such decisions."

### 4.6 Death in Damascus

Death predicts perfectly, so Death's location is a child of the agent's $\textsc{fdt}$ node. Both hypotheticals contain death. Staying saves $1,000, so A-FDT stays, with no instability.

CDT oscillates, because each belief about its own act recommends the other act. Suppose a genuinely random coin is offered for $1, giving a 50% survival chance. Its outcome is not a child of $\textsc{fdt}$. A-FDT values the coin at roughly $500,000 and buys it. The source argues that CDT, valuing its own actions as if Death's location were independent of them, declines the coin.

## 5. What A-FDT's counterfactuals are, and are not

Three features of A-FDT's counterfactuals deserve emphasis.

**Counterpossibles.** If A-FDT in fact outputs *onebox* on $(P,G)$, then "$\textsc{fdt}(\underline P,\underline G)=\textit{twobox}$" is a logical falsehood. A-FDT's hypotheticals are counterpossible. The source does not supply a $\mathtt{true}(\phi)$ operator for conditioning on false logical sentences. Instead it *stipulates* $G$ and reuses $\mathrm{do}$. Footnote 9 mentions an evidential cousin that conditions on the logical node. It is set aside because no adequate definition of logical conditioning exists. The source calls the difficulty "technical rather than philosophical," and points out that human mathematicians reason routinely about claims that may be contradictory.

**Updatelessness in the observed variable.** A-FDT does not condition on $\textsc{Obs}=x$. Its hypotheticals may therefore be ones in which the agent never received $x$, as in transparent Newcomb and both blackmail cases. "Updating" happens only through the choice of node. The source's footnote on the name "Updateless Decision Theory" ties this to Wei Dai's precursor. It also notes that a theory which both conditions *and* moves the intervention point (the earlier "Timeless Decision Theory") suffers a harmful "double update."

**A new dominance notion.** The source argues that every way of building hypotheticals induces its own dominance relation. Two-boxing dominates only relative to CDT hypotheticals. Holding fixed the subjunctive dependencies instead, A-FDT never chooses a dominated act. Dominance therefore cannot settle the dispute neutrally. The source prefers to compare utility achieved, on "fair" problems.

## 6. Questions the source leaves open, and operational proposals

### 6.1 Is $P$ a prior or a posterior?

Equation (4) writes $P$ without saying whether it has been updated on $x$. The transparent-Newcomb calculation computes values in the branch where box B is *empty*, even though the agent has seen it full. Its $P$ therefore cannot be conditioned on $\textsc{Obs}=\textit{full}$. The source's displayed objective in that section is "$\mathbb E(V\mid\mathrm{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$". This conflicts with that calculation, and Fiona's graph contains no $\textsc{Obs}$ node.

*My proposal:* read $P$ as the agent's model of the whole problem from a vantage point *prior* to the observations relevant to the decision. Read $x$ as serving only to select the intervention node. This reproduces every number in the paper and fits the stated contrast with CDT.

It leaves open a question the paper does not settle: which earlier observations should be "baked in"? A natural rule is to bake in only observations whose generation does not depend on any node in the agent's $\textsc{fdt}$ family. That rule is my addition.

### 6.2 How to build $G$

The source is explicit that this is unsolved: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." For practical use, I suggest the following heuristic. Draw an arrow from $\textsc{fdt}(\ldots,y)$ to a variable $Z$ when $Z$ is produced by a process that computes or reliably models your decision function on input $y$. Make the arrow's strength match that process's reliability, using a noise parent such as $\textsc{Accurate}$.

- Processes that merely share a common physical cause with your behaviour get no arrow. The lesion is the standard example.
- Processes that respond to *how* you decide rather than *what* you output get arrows from some other node, or none.

This matches every graph in the paper. It remains a heuristic, not a derivation.

### 6.3 Beliefs about sibling nodes, and the gap between A-FDT and P-FDT

In every example above, the agent's prior $q$ on $\textsc{fdt}(\ldots,y)$ for $y\ne x$ either cancels or is swamped. In general it need not be.

*My constructed example.* A predictor pays $1,000,000 iff she predicts that the agent will do $A$ upon seeing *red* **and** $B$ upon seeing *green*. Doing the "wrong" act in either state adds a bonus of $\delta=$ $10. The agent sees red. Let $q=P(\textsc{fdt}(\ldots,\textit{green})=B)$. A-FDT compares:

$$A:\ 10^6 q \qquad\text{vs.}\qquad \neg A:\ 10.$$

If the agent's prior puts $q<10^{-5}$, A-FDT chooses $\neg A$. The symmetric reasoning applies at green. Pessimistic self-beliefs can therefore sustain a "bad equilibrium" that loses the million.

P-FDT avoids this. It intervenes on a node whose value is a whole policy $\pi:\mathcal X\to\mathcal A$, scores the policy $(\textit{red}\mapsto A, \textit{green}\mapsto B)$ jointly, and then applies it to $x$:

$$\textsc{P-FDT}(P,G,x) = \pi^*(x),\qquad \pi^*=\arg\max_{\pi}\ \mathbb E\big(V\mid \mathrm{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big).$$

This is my reconstruction of the footnotes, which give no formula. The footnotes claim the action/policy difference matters "in certain multi-agent dilemmas." My example suggests it can also arise with a single agent facing a predictor that looks at more than one input. If one keeps A-FDT, the most reasonable operational fix is to require that the sibling beliefs be *consistent*: $P$ should assign to each $\textsc{fdt}(\ldots,y)$ the output that A-FDT would actually produce there. The paper hints at this when it remarks that "the correct $q$ is 1". Consistency still allows several fixed points, so a selection rule is needed. That rule pushes A-FDT toward P-FDT.

### 6.4 Fairness

The source admits that some dilemmas punish any given theory, for example a mind reader who rewards two-boxers. It therefore claims superiority only on "fair" problems: those where beliefs are accurate and payoffs depend only on the agent's *behaviour*. Its footnote concedes that a formal fairness criterion is lacking. Claims of the form "A-FDT is optimal" are thus conjectural relative to an undefined class.

## 7. Conclusion

A-FDT is CDT with the point of intervention moved. It does not ask what happens if this physical act occurs. It asks what happens if *this function*, on *this input*, outputs $a$. Equation (4) makes this precise. Given a model $P$ and a graph $G$ of subjunctive dependencies, A-FDT applies $\mathrm{do}$ to $\textsc{fdt}(\underline P,\underline G,\underline x)$, lets the change propagate to everything that computes or models that output, and maximizes expected utility.

On this rule A-FDT:

- one-boxes in Newcomb's problem and cooperates with a twin;
- smokes in the lesion problem;
- pays in Parfit's desert and refuses blackmailers;
- stays in Damascus.

It does all this without ratification or precommitment devices. Its price is a reliance on counterpossible hypotheticals and on a dependency graph that no one yet knows how to learn.

To apply A-FDT to an unfamiliar case:

1. Model every system that reproduces your function, on any input.
2. Use an unconditioned (prior) $P$.
3. Intervene on the node for your actual input.
4. Check whether your beliefs about your behaviour on other inputs affect the answer.

If they do, the policy-level formulation, which the authors themselves prefer, is the safer guide.

---

*Reference:* Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2.