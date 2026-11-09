# A-FDT: Choosing as the Output of a Function

## 1. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should not ask "which physical act of mine causes the best outcome?" Instead she should ask "which output of *this decision procedure* yields the best outcome?" The paper gives one explicit equation for this rule, Equation (4) in its Section 5. That equation maximizes over **actions**. It intervenes on a node that represents the procedure's output *on the agent's actual observation history*.

The authors say in footnotes 7 and 16 that their preferred formalization instead iterates over **policies**, meaning maps from observations to actions. To keep these apart, I call the Equation (4) theory **A-FDT** (action functional decision theory). I call the footnoted variant **policy-FDT**. The paper itself uses "FDT" for both, and quotations below keep that usage. Other theories keep their usual names: causal decision theory (CDT) and evidential decision theory (EDT).

I try to mark clearly which claims belong to the source and which are my own interpretation or proposal. Equation (4) leaves several implementation details open. Some of them change verdicts, so they need explicit treatment.

## 2. The common frame: expected utility with a choice of "hypothetical"

The paper places EDT, CDT and A-FDT inside one expected-utility template (its Equation (1)):

$$
\mathcal{EU}(a) := \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j).
$$

Here $x$ is the observation history and $\hookrightarrow$ is a connective for "decision hypotheticals" that is left unspecified. Following Joyce's representation theorem, the authors treat the theories as agreeing about value and disagreeing about the *epistemic perspective* from which actions are evaluated. Operationally, the agent holds a world-model $M$. For each action she builds a hypothetical $M^{a\hookrightarrow}$, which the paper describes as "transient, useful, and possibly quite representationally thin". She then scores each hypothetical and acts on the best.

With $V := \mathcal U(\textsc{Outcome})$, the paper's three equations are:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$
$$
\text{A-FDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big) \tag{4}
$$

## 3. Anatomy of Equation (4)

The A-FDT equation has five ingredients.

**(i) A probabilistic model with logical variables.** $P$ ranges over ordinary physical variables (boxes, lesions, letters). It also ranges over variables standing for *outputs of mathematical functions*. In particular, for each observation history $y$ there is a variable

$$
F_y := \textsc{fdt}(\underline P,\underline G,\underline y),
$$

which represents what the A-FDT algorithm returns when run on the agent's own model and the input $y$. The underline means dequoting: the variable's *name* is built from the model itself. The paper argues that this self-reference is harmless. One can represent a value without knowing it, and Kleene's recursion theorem ("quining") shows how such self-representing structures can be built.

**(ii) A dependency graph $G$.** $G$ plays the role that a causal graph plays for CDT. It also records *subjunctive* dependencies, that is, which variables would change if a function's output changed. Footnote 9 is explicit that "we require that the relevant logical dependency structure be given as an input to FDT, in the same way that the relevant causal structure is given as an input to CDT."

**(iii) Pearl's $\mathtt{do}$ operator, applied to a logical node.** The ideal would be an operator $\mathtt{true}(\phi)$ that updates beliefs as if a logical sentence held. The paper concedes that "it's not clear how to define a $\mathtt{true}$ operator", so it reuses $\mathtt{do}$ on the graph. Setting $F_x=a$ cuts $F_x$'s incoming edges, recomputes everything downstream of $F_x$ in $G$, and leaves everything else at its prior distribution.

**(iv) Observations select the intervention point.** The paper states the second difference from CDT directly. "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Note that Equation (4) contains no $\textsc{Obs}=x$ term. The observation enters only through the subscript of $F_x$.

**(v) The physical action is downstream.** $\textsc{Act}$ is a child of the $F_y$ nodes. When observations depend on the world, a selector variable decides which $F_y$ actually drives the body. The agent's body is one implementation of the function among possibly several. A predictor's model or a twin may be others.

In words, A-FDT asks: "Imagine that the function I am computing, applied to exactly the input I am now facing, returned $a$. Everything that depends on that function's output changes to match, and nothing else changes. How good would the world be?"

## 4. What goes into $G$: subjunctive dependence

All of the theory's distinctive content sits in the edges out of $F_x$. The source's criterion is: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." It summarizes the theory with an analogy: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper calibrates the notion with three cases.

- **Causal dependence is a special case.** A scribe copying a calculator's output in Paris depends on that output both causally and subjunctively.
- **Shared computation counts.** Two working calculators computing $6288+1048$ on opposite sides of the world depend on the same arithmetic fact, even with no causal link between them. A reliable predictor's model of the agent is treated the same way: "In effect, the FDT agent has a 'twin' inside the predictor's mind."
- **Mere correlation does not count.** Two calculators that happen to be pink are not subjunctively linked. Neither are a lesion and a smoking habit. The lesion "is not evaluating the agent's future decisions."

Since a function has only one output on a given input, intervening on $F_x$ amounts to entertaining a *counterpossible*. The paper calls the lack of a satisfactory theory of such reasoning "the main drawback of FDT relative to CDT at this time." It treats the difficulty as technical and points out that human mathematicians reason under logical uncertainty all the time. It also identifies "how to deduce the structure of subjunctive dependencies from observation and experiment" as "perhaps the largest open problem."

**Working rule (my operationalization).** Draw an edge from $F_y$ to a variable $Z$ when $Z$'s mechanism *evaluates* the agent's decision function on input $y$, or a sufficiently faithful copy or model of it. That covers the agent's body, exact twins, simulations, and predictions built from models of the agent. Imperfection in the evaluation goes into a separate noise parent, such as the paper's $\textsc{Accurate}$ node. Common causes that only *correlate* with the agent's choice, such as genes, lesions or upbringing, stay as ordinary upstream nodes with no edge from $F_y$.

## 5. Worked examples

All figures are in dollars, which stand for utility.

### 5.1 Twin prisoner's dilemma and Newcomb's problem

In the twin dilemma, both prisoners' acts are children of the same node $F$. Under $\mathtt{do}(F=\textit{cooperate})$ both cooperate and the agent gets \$1,000,000. Under $\mathtt{do}(F=\textit{defect})$ both defect and she gets \$1,000. A-FDT cooperates.

Newcomb's problem uses the same pattern. In the paper's graph, $F$ is the parent of both $\textsc{Act}$ and $\textsc{Prediction}$, and the predictor is accurate with probability 0.99:

$$
\mathbb E[V\mid \mathtt{do}(F=\textit{one})] = 0.99(10^6) = 990{,}000,
$$
$$
\mathbb E[V\mid \mathtt{do}(F=\textit{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
$$

A-FDT one-boxes. CDT's graph instead makes the box a sibling of $\textsc{Act}$ under a "predisposition" node, so intervening on $\textsc{Act}$ leaves the box's probability fixed, and CDT two-boxes. The paper stresses that this involves no retrocausation. The agent simply refuses to imagine her act changing while "holding constant" the output of the function the predictor evaluated.

### 5.2 Smoking lesion

In this problem the lesion shapes the agent's *preferences*. The paper therefore models two possible decision functions: $F^S$, which values smoking, and $F^R$, which does not. The lesion acts as a selector: $\textsc{Act}(\textit{lesion},s,r)=s$ and $\textsc{Act}(\textit{nolesion},s,r)=r$. Cancer is a child of the lesion and *not* of either decision node.

Let $p$ be the prior probability of the lesion and $q$ the prior probability that the $R$-function smokes. Intervening on $F^S$ gives

$$
\mathbb E[V\mid\mathtt{do}(F^S=\textit{smoke})] - \mathbb E[V\mid\mathtt{do}(F^S=\textit{refrain})] = p\cdot 1{,}000 > 0.
$$

So A-FDT smokes, while one-boxing in Newcomb's problem. The paper presents this pair of verdicts, which Gibbard and Harper had argued no rational agent could combine, as the headline result.

### 5.3 Transparent Newcomb: observations as selectors

This example shows how Equation (4) treats observations. The agent sees box B full. Her graph contains two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. $F_{\text{full}}$ feeds the prediction, since the predictor fills B iff it predicts one-boxing *upon seeing it full*. The prediction then determines which node drives $\textsc{Act}$. Let $q = P(F_{\text{empty}}=\textit{two})$.

$$
\mathbb E[V\mid \mathtt{do}(F_{\text{full}}=\textit{one})] = 0.99(10^6) + 0.01\,q(1{,}000) = 990{,}000 + 10q,
$$
$$
\mathbb E[V\mid \mathtt{do}(F_{\text{full}}=\textit{two})] = 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.
$$

The extracted source prints the second total as "\$110,00 + $q\cdot$\$990". The terms make clear that it means \$10,010 + \$990$q$. A-FDT one-boxes for every $q\in[0,1]$, even though she can see the money.

The paper notes that this is "precisely equivalent" to paying the driver in **Parfit's hitchhiker**. With a 99%-accurate lie detector,

$$
\mathbb E[V\mid\mathtt{do}(F_{\text{city}}=\textit{pay})] = -0.99(1{,}000) - 0.01(10^6) = -10{,}990,
$$

compared with $-990{,}000$ for refusing. A-FDT pays.

### 5.4 Blackmail

**XOR blackmail.** The letter is sent iff exactly one of two things holds: (i) there are no termites and the agent would pay, or (ii) there are termites and the agent would not pay. Assume an infallible predictor and a prior $p$ of termites.

- Under $\mathtt{do}(F_{\text{letter}}=\textit{pay})$, the expected value is $-(1-p)1{,}000 - p\cdot 10^6$.
- Under $\mathtt{do}(F_{\text{letter}}=\textit{refuse})$, the expected value is $-p\cdot 10^6$.

Refusal wins by $(1-p)\cdot 1{,}000$. The intervention leaves the termites alone, because the infestation does not depend on the agent's function. EDT pays because conditioning on paying "rules out" termites.

**Mechanical blackmail.** Let $\varepsilon$ be the probability that the blackmailer wrongly predicts payment. A paying disposition loses \$1,000 for certain. A refusing disposition loses $\varepsilon\cdot 10^6$ in expectation. So A-FDT refuses iff $\varepsilon < 10^{-3}$. The paper's $\varepsilon=0.09\%$ case gives refusal, as it says. The source then says she pays at "0.011%". That figure lies *below* the threshold and would still favor refusal, so it is presumably a misprint for something like 0.11%. The structural point stands: refusal is optimal exactly when the predictor's error rate makes the resulting outcome cheap enough.

### 5.5 Death in Damascus

Death's appointment book is a child of $F$. Under either intervention Death is wherever the agent is. Staying saves \$1,000, so A-FDT stays. The paper contrasts this with CDT's instability (Gibbard and Harper's term) and with CDT's refusal to pay \$1 for a truly random coin.

## 6. What Equation (4) leaves open, and how I would close it

### 6.1 Does A-FDT also condition on $x$?

The source's text is ambiguous here. Equation (4) has no conditioning term. However, the transparent-Newcomb passage writes $\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with unbalanced brackets.

The numbers decide the matter. The paper's calculation sums over the inaccurate branch, in which the box is empty, so it does *not* condition. And it must not. Conditioning on $\textsc{Obs}=\textit{full}$ after $\mathtt{do}(F_{\text{full}}=\textit{two})$ removes the empty-box worlds and yields \$1,001,000 against \$1,000,000, which flips the verdict to two-boxing. The paper's footnote on timeless decision theory names exactly this failure, conditioning and also moving the intervention point, as a "double update" that "proves harmful in practice."

**Interpretation adopted.** Read Equation (4) literally. $P$ is the agent's model *before* the observations in $x$. The observation $x$ only selects $F_x$.

**Proposition (my observation).** Suppose (a) $\textsc{Obs}$ is not downstream of $F_x$ in $G$, and (b) intervening on $F_x$ changes nothing within worlds where $\textsc{Obs}\neq x$. Then

$$
\mathbb E[V\mid \mathtt{do}(F_x=a)] = P(x)\,\mathbb E[V\mid \mathtt{do}(F_x=a),x] + \textstyle\sum_{y\ne x}P(y)\,c_y,
$$

where the constants $c_y$ do not depend on $a$. So when $P(x)>0$, the updateless argmax equals the conditioned one. A-FDT departs from "update then decide" only when the observation itself depends on the agent's function. That is the transparent-Newcomb and blackmail pattern.

A practical consequence follows. It is harmless to fold into $P$ any observations that no relevant process conditions on the agent's function. Observations that might be so conditioned must stay in $x$. The source does not say where to draw this boundary, so this is my operational answer.

### 6.2 The non-active nodes $F_y$, $y\neq x$

Equation (4) intervenes on one node and leaves every other $F_y$ at its *prior* distribution. Those priors are self-predictions. In the examples above they cancel out, which is why the paper can say of $q$ that "it doesn't matter." In general they do not cancel.

Here is a coordination case of my own construction. A fair coin shows red or blue, and the agent picks A or B after seeing it. A predictor pays \$10 if she would choose A under *both* colors, \$5 if she would choose B under both, and \$0 if her choices differ. At the red node, with $r = P(F_{\text{blue}}=A)$,

$$
\mathbb E[V\mid\mathtt{do}(F_{\text{red}}=A)]=10r,\qquad \mathbb E[V\mid\mathtt{do}(F_{\text{red}}=B)]=5(1-r).
$$

So A-FDT chooses A iff $r>1/3$. Both (A,A) and (B,B) are self-consistent profiles. If the agent expects B, she confirms it and earns \$5 where \$10 was available.

The source acknowledges the gap in general terms. Footnote 7 says that iterating over policies "makes a difference in certain multi-agent dilemmas." Policy-FDT would choose $\pi:\mathcal X\to\mathcal A$ maximizing $\mathbb E[V\mid \mathtt{do}(F=\pi)]$ and pick (A,A) directly.

**My proposals.** First, impose *reflective consistency*. The prior on each $F_y$ should match what A-FDT itself outputs at $y$, as the paper implicitly does when it remarks that "the correct $q$ is 1." This turns A-FDT into an equilibrium concept across the agent's observation-indexed instances. Second, where several consistent profiles exist, A-FDT taken alone does not say which one the agent lands in. Selecting the best one requires either the policy formulation or an added selection rule. Readers should treat verdicts in such cases as underdetermined by Equation (4).

### 6.3 Constructing $G$, ties, and randomization

The source supplies no learning theory for $G$. The heuristic in §4 is mine. Equation (4) also says nothing about ties, and none of the paper's examples involve mixed actions. I would break ties arbitrarily and treat genuine randomization as a separate act. Under that treatment the random coin in Death in Damascus, which a perfect predictor cannot anticipate, is worth buying. That fits the paper's verdict that refusing it is "wildly irrational", but the paper does not spell out how A-FDT itself would evaluate the coin.

One technical advantage is worth noting. Because Equation (4) uses $\mathtt{do}$, it never conditions on probability-zero events. EDT's dependence on extreme priors about its own act therefore has no counterpart in A-FDT.

## 7. A procedure for unfamiliar cases

1. **List the decision-relevant inputs.** For each possible observation history $y$, include a node $F_y$.
2. **Draw outgoing edges** from each $F_y$ to every mechanism that evaluates the agent's function on $y$: her body (through a selector driven by what she observes), twins, predictors, and simulators. Add noise nodes for imperfect evaluation. Leave merely correlated common causes without edges from any $F_y$.
3. **Specify $P$** on exogenous variables. Specify priors on $F_y$ for $y\neq x$, and make them consistent with A-FDT's own outputs.
4. **For each action $a$, apply $\mathtt{do}(F_x=a)$.** Propagate downstream and compute $\mathbb E[V]$ under the pre-observation model, *without* conditioning on $x$.
5. **Pick the argmax.** Then check that it agrees with the self-predictions assumed in step 3. If several consistent profiles exist, report the ambiguity, or defer to policy-FDT if you accept it.

In "simple" problems, where every correlation between act and outcome is caused by the act, the source shows that

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(F=a)],
$$

and the three theories coincide. They diverge only when predictors, twins or copies are present.

## 8. Philosophical motivation in brief

The source gives several arguments for A-FDT.

- **Utility achieved.** This is the primary argument. FDT agents "get more of what they want out of life."
- **Precommitment.** A-FDT behaves as CDT and EDT agents would *pay* to precommit to behave, with no rituals required.
- **Value of information.** A-FDT never assigns negative value to information.
- **Reflective stability.** CDT recommends self-modifying away from itself. A-FDT, so far as the authors know, is "reflectively stable in fair problems."

The paper also reframes dominance. Every way of constructing hypotheticals defines its own dominance relation. Under subjunctive dominance, holding the dependencies fixed, one-boxing is not dominated.

The intended scope is "fair" problems, where outcomes depend on the agent's *behavior* rather than on which decision procedure she runs. In Newcomb's problem, on this view, the predictor "punishes *two-boxers*," not rational agents. The paper admits that fairness has not been formalized. Its own example is a game that punishes anyone who acts as a copy of Fiona acts, which no FDT agent can win.

Against the objection that A-FDT agents believe they control mathematics or the past, the authors argue for parity. A deterministic CDT agent also imagines its single possible act varying. "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 9. Conclusion

A-FDT, as fixed by Equation (4), is CDT-style surgery moved from the physical act to the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$. Observations change *where* the surgery happens rather than what is conditioned on. This one move yields one-boxing alongside smoking, paying the driver in the hitchhiker case, refusing blackmail, and staying in Damascus.

The formal content is precise once $G$ is given. Most of the difficulty lies in producing $G$, because that is where counterpossible reasoning is hidden. I have argued for three further points of interpretation:

- Equation (4) must be read without conditioning on $x$; otherwise the theory collapses into a harmful "double update."
- The priors over the agent's behavior under other observations are a real parameter, best handled by a reflective-consistency requirement.
- In coordination problems across information states, A-FDT can stall at an inferior self-consistent profile that the authors' preferred policy formulation avoids.

With those caveats made explicit, the five-step procedure above lets a reader settle most unfamiliar cases.

**References.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060. Gibbard, A. & Harper, W. (1978), "Counterfactuals and Two Kinds of Expected Utility." Joyce, J. (1999), *The Foundations of Causal Decision Theory*. Pearl, J. (2000), *Causality*.