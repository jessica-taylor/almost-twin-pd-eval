# Action Functional Decision Theory (A-FDT): Surgery on a Function's Output

## 1. What is being explained

Yudkowsky and Soares (2017) propose that a rational agent should treat her decision as the output of a fixed mathematical function and ask, in their words, "Which output of this very function would yield the best outcome?" Their paper gives this idea one precise form, Equation (4) of Section 5. There, the agent intervenes on a node that represents her decision function's output, and the values she ranges over are *actions*.

The paper calls this theory simply FDT. A footnote, however, says that "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions." To keep the two apart, this essay uses the following names:

- **A-FDT (action functional decision theory)** is the action-valued rule of Equation (4), and it is my subject.
- **P-FDT** is my label for the policy-valued variant the footnote mentions, which the paper does not formalize.
- **CDT** and **EDT** are causal and evidential decision theory.

Throughout, I mark which claims come from the source and which are my own reconstructions or proposals.

## 2. The common template

The source treats EDT, CDT and A-FDT as three expected-utility theories that share one schema. Each recommends an action $a$ in a finite set $\mathcal A$ that maximizes

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \qquad (1)
$$

Here $x$ is the observation history, and $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the connective $\hookrightarrow$ is a free parameter. In Joyce's phrase, decision theories "should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated." Each theory fills in $\hookrightarrow$ differently. Write $V = \mathcal U(\textsc{Outcome})$.

**EDT (Equation 2)** conditions on the action:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$

**CDT (Equation 3)** applies a Pearl intervention to the physical action node, using a causal graph $G$:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x\big).$$

**A-FDT (Equation 4)** applies the intervention to a *logical* node:

$$
\mathrm{FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \qquad (4)
$$

## 3. Reading Equation (4)

Equation (4) has four ingredients.

**(i) The world-model.** The model is a pair $(P,G)$. $P$ is a probability distribution over variables. Some of these variables describe physical events, such as box contents or predictions. Others describe *the outputs of mathematical functions*. The source gives the example of a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on 7336." $G$ is a directed graph saying how changing one variable would change others. In A-FDT, the graph encodes not only causal structure but also "the logical, mathematical, computational, causal, etc. structure of the world more broadly."

**(ii) The self-referential node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is whatever the A-FDT algorithm outputs on inputs $(P,G,x)$. The underline denotes dequoting: the name of the variable depends on the model itself. The source argues this is harmless. The agent needs only a *representation* of this value, not knowledge of it, and Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.

**(iii) The surgery.** Pearl's $\mathrm{do}$ operator sets this node to $a$. It cuts the node's incoming edges and propagates the change to every descendant in $G$. Typically the descendants are:

- the agent's physical action;
- any predictor's prediction of her;
- a twin's choice;
- and whatever depends on those.

Everything that is not a descendant keeps its distribution under $P$.

**(iv) How observations enter.** Here A-FDT departs most sharply from CDT. The source notes that "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." There is no "$\textsc{Obs}=x$" to the right of the conditioning bar. Instead, $x$ appears inside the *name* of the intervened node. Seeing $x$ instead of $y$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline x)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline y)$.

### The underlying notion: subjunctive dependence

The source says that two physical systems' behaviors "subjunctively depend" on a function when both compute that function. The source then summarizes the theory by analogy: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

Causal dependence is a special case of subjunctive dependence. A scribe copying a calculator's output depends on that output in both senses. Mere correlation, by contrast, is not dependence at all: two calculators that happen to be pink do not depend on each other's colour.

### When the three theories agree

The source makes a structural claim. Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\textsc{fdt}=a)],
$$

and all three theories prescribe the same action. They come apart only when something other than the action itself tracks the agent's decision. Predictors, twins, and copies are the standard examples.

## 4. An operational recipe

The source supplies Equation (4) and worked examples, but no general algorithm. The following procedure is my own reconstruction. It reproduces every worked example in the paper.

1. **Fix the observation space.** Let $\mathcal X_0$ be the set of observation histories the agent might have at the decision point in this problem.
2. **Create one logical node per observation.** For each $y\in\mathcal X_0$, create a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ with values in $\mathcal A$.
3. **Gate the action through the observation.** Make the physical action a deterministic gate: $\textsc{Act}=F_{\textsc{Obs}}$. In graph terms, $\textsc{Act}$ has parents $\textsc{Obs}$ (or whatever determines it) and all of the $F_y$. This is exactly the structure of the source's graphs for transparent Newcomb and both blackmail problems.
4. **Wire in every process that computes or models the function.**
   - A predictor that simulates the agent's response to $y$ gets an edge from $F_y$.
   - A twin running the same function gets an edge from the corresponding node.
   - Imperfection is modelled with noise parents, such as the source's $\textsc{Accurate}$ node.
   - Processes that are merely correlated with the agent, such as a lesion, get *no* edge from any $F_y$.
5. **Assign priors.** Put priors on the root nodes. This includes beliefs about $F_y$ for $y\neq x$, since these are not intervened on.
6. **Evaluate and choose.** For each $a$, compute $\mathbb E[V\mid \mathrm{do}(F_x=a)]$ by summing over all non-intervened roots. Output the maximizer.

Step 6 sums over worlds in which the agent never sees $x$. That is intended. In the source's words, A-FDT says "agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

## 5. Worked examples

### 5.1 Twin prisoner's dilemma and Newcomb's problem

**Twin prisoner's dilemma.** The single node $F$ has two children: the agent's act and the twin's act. Under $\mathrm{do}(F=\text{cooperate})$ both twins cooperate, giving \$1,000,000. Under $\mathrm{do}(F=\text{defect})$ both defect, giving \$1,000. A-FDT cooperates. CDT, by contrast, holds the twin's act fixed and so defects.

**Newcomb's problem.** The source uses a 99%-accurate predictor. $F$ feeds both the act and the prediction, and the prediction passes through an $\textsc{Accurate}$ node. The two hypotheticals give:

$$
\mathbb E[V\mid\mathrm{do}(F=\text{one})]=0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E[V\mid\mathrm{do}(F=\text{two})]=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=11{,}000.
$$

A-FDT one-boxes.

The prior on $F$ plays no role, because the $\mathrm{do}$ operator overwrites it. EDT is different on this point. The source notes that with extreme priors "Eve can be made to do *anything*". A-FDT has no such sensitivity to its prior over its own act.

### 5.2 Smoking lesion

Here the lesion determines the agent's *utility function*, and therefore which of two decision computations controls her act. The source models this with two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The lesion selects which one sets $\textsc{Act}$, and the lesion also drives cancer. Crucially, neither $\textsc{fdt}$ node has an edge to $\textsc{Cancer}$.

Intervening on the node that is in fact running therefore leaves $P(\text{lesion})=p$ unchanged. The two hypotheticals differ only in the smoking bonus, and only in worlds where this node is the one in control:

$$
\mathbb E[V\mid\mathrm{do}(\text{smoke})]-\mathbb E[V\mid\mathrm{do}(\text{refrain})] = p\cdot\$1{,}000 > 0.
$$

A-FDT smokes. The theory's discriminating work is done entirely by the *absence* of an edge in $G$. The lesion does not compute the agent's function, so nothing the agent's function outputs can move it.

### 5.3 Transparent Newcomb

Box B is visibly full. The agent intervenes on $F_{\text{full}}$, and $\textsc{Act}=F_{\textsc{Obs}}$, where $\textsc{Obs}$ is determined by the prediction. Let $q$ be the prior probability that $F_{\text{empty}}=\text{two}$.

If $F_{\text{full}}=\text{one}$:
- With probability 0.99 the predictor is accurate, the box is full, and the agent one-boxes, receiving $10^6$.
- With probability 0.01 the predictor errs, the agent sees an empty box, and $F_{\text{empty}}$ acts, yielding $1{,}000q$ in expectation.

$$
\mathbb E[V\mid \mathrm{do}(F_{\text{full}}=\text{one})]=990{,}000+10q.
$$

If $F_{\text{full}}=\text{two}$:
- With probability 0.99 the box is empty, yielding $1{,}000q$ in expectation.
- With probability 0.01 the predictor errs, the box is full, and the agent takes both boxes, receiving \$1,001,000.

$$
\mathbb E[V\mid \mathrm{do}(F_{\text{full}}=\text{two})]=10{,}010+990q.
$$

A-FDT one-boxes for every $q\in[0,1]$, even while looking at the full box.

Two textual remarks on the source's version of this example:

- The source prints the two-box value as "\$110,00 + q·\$990"; the correct value is \$10,010 + 990q, as above.
- The source writes the objective as $\mathbb E(V\mid \mathrm{do}(\ldots=a, \textsc{Obs}=\text{full})$, with an unmatched parenthesis. Its actual calculation sums over the empty-box branch, so it does *not* condition on $\textsc{Obs}=\text{full}$. The calculation agrees with Equation (4). I take Equation (4) as authoritative and read the displayed "$\textsc{Obs}=\text{full}$" as a label for which node is intervened on.

The source argues that this case is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem.

### 5.4 Mechanical blackmail, and a threshold

A blackmailer runs a damaging program only if she predicts that the agent would pay upon being blackmailed. Let $\varepsilon$ be the probability that she wrongly predicts payment from an agent who would refuse. Intervene on $F_{\text{blackmail}}$:

- **Pay:** the agent is always blackmailed and always pays, so the expected loss is \$1,000.
- **Refuse:** the agent is blackmailed only with probability $\varepsilon$, and then loses \$1,000,000, so the expected loss is $10^6\varepsilon$.

A-FDT therefore refuses exactly when $\varepsilon<10^{-3}$.

The source's own example has $\varepsilon=0.0009$, giving an expected loss of \$900 from refusing, so the agent refuses. The source then says that at an error rate of "0.011%" she pays. By the arithmetic above, 0.011% (that is, $1.1\times10^{-4}$) still lies below the threshold, so I suspect 0.11% was intended. The general lesson stands either way. A-FDT may refuse while holding the letter and *knowing* the prediction was wrong. It does so because "it's advantageous to be *the kind of agent* that makes such decisions."

### 5.5 Death in Damascus

Death's appointment book is written from a perfect prediction of the agent's function. Every intervention $\mathrm{do}(F=\text{city})$ therefore also moves Death to that city. The comparison reduces to $-\$10^6$ for staying versus $-\$10^6-\$1{,}000$ for fleeing.

A-FDT stays. Its decision is stable: unlike CDT, it has no oscillation that needs ratification to resolve.

## 6. What the source leaves open

### 6.1 Where does $G$ come from?

The source is candid on this point: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." A cleaner semantics would replace $\mathrm{do}$ with an operator $\mathrm{true}(\phi)$ for counterpossible suppositions. The source admits "it's not clear how to define a $\mathrm{true}$ operator", and so it takes $G$ as an input to the theory.

In practice, then, applying A-FDT means modelling, and the decisive modelling question is always the same: *which processes are computing (or accurately simulating) this function?* I suggest three heuristics. They are my own additions.

1. **The rerun test.** Ask: "if the algorithm's code were rewritten to output something else on this input, holding all non-logical facts fixed, which variables would a competent modeller expect to change?"
2. **Predictor tracking.** A predictor's output tracks $F_y$ only insofar as the predictor's method actually consults the agent's input–output behaviour. A predictor that keys on a population base rate does not track it.
3. **Lesions.** A lesion, a gene, or any other common cause that does not itself evaluate the function gets no edge.

### 6.2 Partial similarity

The source says that with imperfect prediction or an indeterministic agent "the interdependence is weakened, but not eliminated." It models this only with an $\textsc{Accurate}$ noise variable.

For agents that run *similar but distinct* functions, such as a near-twin or another A-FDT agent with a slightly different prior, my operational proposal is to treat the other agent's act as a noisy channel from $F$:
$$P(\text{other}=b \mid \mathrm{do}(F=a))=\kappa_{ab}.$$
The kernel $\kappa$ encodes one's credence that the two computations agree. Setting $\kappa$ to the identity recovers the perfect twin. Setting $\kappa$ to have identical rows, so that the other agent's act is independent of $F$, recovers the CDT treatment.

This proposal is coherent, but it is an assumption. The source gives no rule for setting $\kappa$.

### 6.3 Which $P$? Prior versus posterior

Equation (4) does not condition on $x$. So the $P$ in Equation (4) cannot be the agent's posterior after seeing $x$. If it were, the empty-box branch in transparent Newcomb would have probability zero, and A-FDT would two-box, contrary to the source's result. $P$ must therefore be a model that predates the observation.

The source leaves unspecified how far back "prior" reaches. My proposal: $P$ should be conditioned on everything the agent learned *before the earliest point at which any modelled process could have evaluated her function on the inputs at issue*. For the problems discussed here, that is the moment of prediction. Observations made later enter only through the choice of node $F_x$.

This proposal matches all of the source's examples. It is still a substantive choice, and very "early" priors raise further questions that the paper does not address.

### 6.4 The other observation nodes: A-FDT versus P-FDT

In A-FDT, the nodes $F_y$ for $y\neq x$ are *not* intervened on. They keep their prior distributions, such as the $q$ in §5.3. In the source's examples $q$ never matters. The source sometimes notes what the "correct" value would be ("The correct value of $q$ is 1, as you may verify, but in this case it doesn't matter"), but it gives no general rule.

In general, $q$ can matter. Here is my own illustration. Nature shows the agent $y_1$ or $y_2$, each with probability 1/2, independently of everything else. A perfect predictor evaluates the agent's function on *both* inputs, then pays:

- \$10 if the agent outputs $a$ on both inputs;
- \$5 if the agent outputs $b$ on both inputs;
- nothing otherwise.

Suppose the agent sees $y_1$ and believes $P(F_{y_2}=a)=r$. Then
$$
\mathbb E[V\mid\mathrm{do}(F_{y_1}=a)]=10r,\qquad \mathbb E[V\mid\mathrm{do}(F_{y_1}=b)]=5(1-r).
$$
A-FDT outputs $a$ if and only if $r>1/3$.

If the agent expects her $y_2$-self to play $b$, she plays $b$, and so does her $y_2$-self by the same reasoning. The profile $(b,b)$ is a self-consistent fixed point of A-FDT that pays \$5. A policy chooser, P-FDT, intervenes on the whole map $y\mapsto F_y$ at once and picks $(a,a)$ for \$10.

In this sense A-FDT performs coordinate-wise optimization. It can settle on a suboptimal self-consistent profile when the outcome depends jointly on the function's behaviour across inputs. This is presumably the sort of case the source has in mind when it says the policy formulation "makes a difference in certain multi-agent dilemmas."

For applying A-FDT as stated, I propose the following operational rule:

- Set beliefs about each $F_y$ ($y\neq x$) to the agent's best prediction of what A-FDT itself would output there.
- Require these predictions to form a *consistent* profile, meaning a fixed point where each $F_y$ is A-FDT-optimal given the others.
- When several fixed points exist, flag the case as one where A-FDT and P-FDT may diverge.

None of this is in the source. It is the minimal extra specification needed to make A-FDT determinate in such cases.

### 6.5 Ties and randomization

The arg max may contain several actions. The source specifies no tie-breaking rule. Randomized acts count as options only if they are listed in $\mathcal A$, with the randomization device modelled in $G$. If the device is one the predictor can foresee, it is a child of $F$. If it is genuinely unpredictable, it has no edge from $F$.

In the source's Death in Damascus discussion, a truly random coin offers a 50% survival chance. An A-FDT agent with that coin in $\mathcal A$ would rightly value it at \$500,000 and pay \$1 for it. By the source's analysis, CDT declines this trade.

## 7. Why one might accept A-FDT

The source's case is mainly about performance. A-FDT one-boxes, smokes, pays the driver, resists extortion and cooperates with twins. Its proponents claim it does at least as well as CDT and EDT on "fair" problems, where the outcome depends only on the agent's behaviour, not on the procedure that produced it. The source's supporting arguments include:

- **Precommitment.** A-FDT agents "simply act as they would have ideally precommitted to act," with no costly binding devices. Relatedly, the theory is claimed to be reflectively stable: it does not advise switching to another theory mid-problem.
- **Dominance.** Every way of building hypotheticals induces its own dominance relation, so the two-boxer's dominance argument "is merely a restatement of CDT's method for assessing an agent's options."
- **Control.** A-FDT's idea of "control" over a logical output is no more mysterious than a deterministic CDT agent's idea of control over a physical act that was always going to happen.

The source acknowledges that the notion of fairness is not yet formalized. Its claim that A-FDT is optimal on fair problems is offered as a conjecture supported by examples, not as a theorem.

## 8. Conclusion

A-FDT is CDT with the point of surgery moved. Instead of intervening on a physical act and conditioning on what has been observed, it intervenes on the output of the agent's own decision function *at the current input*. It then lets the change propagate to everything that computes or models that function, including the very observations the agent would have received.

Equation (4) makes this exact, given a graph $G$ of subjunctive dependencies and a model $P$ that predates the observation. The worked cases (Newcomb, the lesion, transparent Newcomb, blackmail, Damascus) all reduce to one question: which nodes are descendants of $F_x$?

What the source does not settle are:

- how to construct $G$;
- how to quantify partial similarity between agents;
- which prior $P$ to use;
- how to fix beliefs about the function's outputs on other inputs.

For the last of these, I have proposed self-consistent fixed points, and I have shown a simple case where A-FDT and its policy-level sibling P-FDT come apart. With those specifications made explicit, A-FDT can be applied mechanically to new problems.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and two kinds of expected utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.