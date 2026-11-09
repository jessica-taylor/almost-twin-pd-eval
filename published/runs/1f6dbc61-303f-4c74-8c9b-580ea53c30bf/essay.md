# Action Functional Decision Theory (A-FDT): Choosing as the Output of a Function

## 1. What is being proposed

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* begins from one question. When an agent deliberates, what exactly is she choosing? Causal decision theory (CDT) answers: a physical act. Evidential decision theory (EDT) answers: the act that would be the best news to learn of. The paper's answer is that the agent fixes the output of a fixed mathematical decision function. Every physical system that computes that function, or models it accurately, then "moves together" with her choice.

In the paper's words, the agent should follow "a decision procedure that asks 'Which output of this decision procedure causes the best outcome?'" rather than "'Which physical act of mine causes the best outcome?'"

The paper's main formal statement is Equation (4) of Section 5. That equation intervenes on a variable representing the decision function's output **action** for a given input. In this essay I call that rule **A-FDT** (action functional decision theory). The label distinguishes it from a variant the authors mention in footnotes 7 and 16, in which the agent "iterate[s] over *policies* (mappings from observations to actions) rather than actions." I call that variant **policy-FDT**. The paper uses the single name "FDT" and says the policy refinement "will not make a difference in this paper." Section 6 explains why I think the distinction still deserves attention.

Throughout, I separate three things: what the paper says, what follows from Equation (4), and what I add to make the rule usable.

## 2. The common frame: expected utility over hypotheticals

All three theories share an expected-utility template (Equation 1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is a connective for "the hypothetical in which $a$ is executed." The paper cites Joyce's representation theorem, which holds the valuation fixed and treats the interpretation of $\hookrightarrow$ as a free parameter. In Joyce's phrase, the theories disagree "about the epistemic perspective from which actions are to be evaluated."

Operationally, an agent holds a world-model $M$. For each candidate $a$, she builds a *hypothetical* $M^{a\hookrightarrow}$: a modified model describing what the world would look like under that choice. She scores each hypothetical by expected utility and acts on the best one. The paper stresses that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." The theories differ only in how they represent $M$ and how they build $M^{a\hookrightarrow}$. Writing $V = \mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. This is plain conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. This is Pearl-style surgery on the physical action node in a causal graph $G$.
- **A-FDT** (Eq. 4):

$$
\boxed{\;\mathrm{FDT}(P,G,x) \coloneqq \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;}
$$

## 3. Reading Equation (4) term by term

**The world-model $(P, G)$.** $P$ is a probability distribution whose variables include ordinary physical quantities (box contents, termites, the twin's choice). It also includes *logical* variables: the outputs of mathematical functions. The paper's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on 7336." $G$ is a graph that records more than causal structure. According to the paper, it records "how changing a logical variable affects all other variables," that is, the "logical, mathematical, computational, causal, etc. structure of the world."

**The intervention node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** This is a variable in the model that stands for the output of the A-FDT algorithm when it runs on this very model and observation. The underline marks dequoting: the node's name is built from the inputs. The paper admits the self-reference and calls it harmless. The agent needs a variable *representing* her output, not knowledge of its *value*, and Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.

**The operator.** Pearl's $\mathtt{do}$ is reused unchanged. Setting $\textsc{fdt}(\ldots)=a$ cuts the node from its parents. Everything downstream of it in $G$ is then recomputed: the agent's own physical act, a predictor's forecast, a twin's choice. Everything else keeps its prior distribution. The paper's ideal operator would be a $\mathtt{true}(\phi)$ operator that updates on a possibly false logical sentence, but "it's not clear how to define" one. Equation (4) avoids the problem by taking the dependency graph as an input, "in the same way that the relevant causal structure is given as an input to CDT."

**What varies and what is held fixed.** This is the core of the theory. In the paper's phrasing, an A-FDT agent considers "scenarios where the output of her decision function changes, and events that subjunctively depend on her decision function's output change, but everything else is held fixed." Two physical systems *subjunctively depend* on a function when both compute it, like two working calculators summing the same numbers. Causal dependence is a special case: a scribe copying a calculator's output depends on that output both causally and subjunctively. Mere correlation, such as two calculators that happen to share a colour, does not count. The slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In type–token terms, CDT intervenes on the token act and A-FDT intervenes on the type.

**How observations enter.** Unlike Equations (2) and (3), Equation (4) does not condition on $\textsc{Obs}=x$. The paper puts the difference this way: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." After seeing $x$, the agent sets $\textsc{fdt}(\underline P,\underline G,\underline x)$. After seeing $y$, she would set $\textsc{fdt}(\underline P,\underline G,\underline y)$. Her own nodes for other inputs keep their prior distributions. This is why A-FDT can coherently "imagine" that, had she chosen differently, she would have seen something different.

**Agreement with rival theories.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the function node, then the paper shows that

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$

so all three theories agree. A-FDT departs from the others only when something other than the agent's body tracks the agent's decision function.

## 4. A working recipe (my operationalization)

The paper says what to compute once $(P,G)$ is given. It is deliberately silent on how to obtain $G$: it calls this "perhaps the largest open problem." To apply A-FDT to an unfamiliar case, I propose the following procedure. It is consistent with every graph the paper draws, but it is my reconstruction, not the paper's.

1. **Identify the decision inputs.** List each observation history $x$ under which the agent's function might be evaluated in the scenario, including histories the agent did not in fact receive (for example, "box empty" or "no letter"). Create a node $\textsc{fdt}(x)$ for each one.
2. **Draw subjunctive edges.** Draw an edge $\textsc{fdt}(x)\to Z$ exactly when $Z$ is produced by a process that computes, simulates, or reliably models the agent's function *on input $x$*. Examples are a twin's choice, a predictor's forecast, or the agent's own body when it is the one receiving $x$. Model imperfect modelling with a separate noise node, like the paper's $\textsc{Accurate}$.
3. **Route the physical act.** Make $\textsc{Act}$ a deterministic function of the $\textsc{fdt}$ nodes, plus whatever variable determines which input the agent actually receives.
4. **Leave mere correlates alone.** A lesion, a gene, or a population statistic gets no edge from any $\textsc{fdt}$ node. It is an ordinary parent or sibling.
5. **Assign priors.** Give priors to all root nodes, including the $\textsc{fdt}$ nodes for inputs other than the actual one.
6. **Compute.** For each $a$, compute $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(x_{\text{actual}})=a))$ without conditioning on $x_{\text{actual}}$, and take the argmax.

Step 2 is the substantive judgment, and it is where disagreements about A-FDT verdicts will live.

## 5. Worked examples

### 5.1 Newcomb's problem and the twin

The predictor is 99% accurate. Box A holds \$1,000, and box B holds \$1,000,000 iff the predictor foresaw one-boxing. The graph has $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate}$:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\text{one})] &= 0.99(1{,}000{,}000)=990{,}000,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\text{two})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT's graph has no edge from its intervention point to $\textsc{Prediction}$, so it holds $P(\text{full})=p$ fixed. Two-boxing then gains exactly \$1,000 whatever $p$ is, and CDT two-boxes. The psychological-twin prisoner's dilemma has the same structure, because the twin's choice is another child of the shared $\textsc{fdt}$ node. A-FDT therefore cooperates. The paper notes that A-FDT involves no belief in retrocausation: the agent "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

### 5.2 The smoking lesion

Here the dependency structure differs. The lesion causes cancer and also shapes the agent's preferences. The paper models this with two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$, and hence two possible decision functions $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Lesion}$ selects which of them drives $\textsc{Act}$. Crucially, there is no edge from either function node to $\textsc{Cancer}$. Intervening on $\textsc{fdt}(P_S)$ therefore leaves $P(\text{lesion})=p$ unchanged. Smoke beats refrain by $p\cdot\$1{,}000$: the probability that this function actually controls the act, times the value of smoking. A-FDT smokes. One rule thus one-boxes and smokes, the combination the paper says Gibbard and Harper argued no rational agent could consistently display.

### 5.3 The transparent Newcomb problem

Both boxes are visible. Box B was filled iff the predictor foresaw one-boxing *upon seeing it full*. The agent sees it full. There are nodes $\textsc{fdt}(\text{full})$ and $\textsc{fdt}(\text{empty})$. The prediction depends on $\textsc{fdt}(\text{full})$ and determines which node controls $\textsc{Act}$. Let $q$ be the prior probability that the agent two-boxes on seeing an empty box. Intervening on $\textsc{fdt}(\text{full})$ without conditioning on "full" gives:

$$
\begin{aligned}
\text{one: }&\ 0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,\\
\text{two: }&\ 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
\end{aligned}
$$

For every $q\in[0,1]$ one-boxing wins, so A-FDT leaves the \$1,000 behind even while looking at a full box.

This example shows a point about the text itself. In this section the paper's displayed objective reads, with a parenthesis left unclosed, "$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\text{full})=a, \textsc{Obs}=\text{full})$." That suggests conditioning on the observation. Conditioning on $\textsc{Obs}=\text{full}$ would force $\textsc{Prediction}$ to be "one-boxer" in both hypotheticals and restore the \$1,000 advantage of two-boxing. The paper's own arithmetic does *not* condition; it sums over $\textsc{Accurate}$ with prior weights. Equation (4) and the prose ("Fiona does not react to observations by conditioning her distribution") agree with the arithmetic. I therefore read the displayed $\textsc{Obs}$ term as a typographical slip. The canonical reading of A-FDT is: never condition on the current observation; use it only to select the intervention node. (Separately, the paper prints the two-box value as "\$110,00 + q·\$990"; the correct figure is $10{,}010+990q$, as above.)

The paper argues that this verdict is equivalent to paying the driver in Parfit's hitchhiker case. It supports the verdict with arguments from precommitment (A-FDT agents "simply act as they would have ideally precommitted to act"), from the non-negative value of information, and above all from utility, since predictors show A-FDT agents full boxes.

### 5.4 Blackmail and an explicit threshold

In the mechanical blackmail, the blackmailer runs a program that will cost the agent \$1,000,000 unless she pays \$1,000. She runs it iff she predicts payment. Suppose that with probability $\varepsilon$ she wrongly predicts payment by a refuser. Intervening on $\textsc{fdt}(\text{blackmail})$:

- **pay:** the agent is always blackmailed and loses \$1,000;
- **refuse:** she is blackmailed with probability $\varepsilon$ and loses $\varepsilon\cdot\$1{,}000{,}000$.

So A-FDT refuses iff $\varepsilon<0.001$. The paper's figure of $\varepsilon=0.0009$ gives an expected loss of \$900, so the agent refuses, as stated. The paper then says she pays if the error chance is "0.011%." That figure lies *below* the threshold, so the printed value is probably a slip for 0.11%. Either way, the general rule is the threshold just derived. Note what the rule says: the agent refuses "even though she *knows* that the blackmailer predicted wrongly." In the XOR blackmail, intervening on $\textsc{fdt}(\text{letter})$ changes whether the letter arrives but not whether there are termites, so A-FDT refuses there as well.

### 5.5 Death in Damascus

Death predicts perfectly. The edge $\textsc{fdt}\to\textsc{DeathLocation}$ means death is certain in both hypotheticals, so staying (\$0) beats fleeing (−\$1,000). A-FDT stays immediately. CDT, which holds Death's location fixed, oscillates; this is Gibbard and Harper's instability. The paper adds that CDT can even refuse a truly random coin offering a 50% chance of survival for \$1.

## 6. Where the source leaves room, and how I would fill it

**(a) Constructing $G$.** This is the central gap, and the paper acknowledges it: "no such formal treatment has yet been given to the problem of deducing the structure of other kinds of subjunctive dependence." The recipe in Section 4 is a heuristic, not a theory. Hard cases include partial similarity (a colleague who reasons *somewhat* like me) and predictors that model a *different* input from the one I received. A practical extension, which is my proposal, is to give such cases a mixture node. A copy computes my function with probability $\rho$ and something else otherwise. The degree of subjunctive dependence then becomes a parameter to estimate, as $\textsc{Accurate}$ is in Newcomb.

**(b) Updating, or the lack of it.** Section 5.3 showed that the absence of conditioning is load-bearing. One consequence is that A-FDT evaluates hypotheticals under the prior $P$ the model was built with. The paper does not settle what $P$ should be. It could be a prior from birth, from the start of the problem, or something else. Its examples quietly use the distribution "at the start of the dilemma." I recommend making this choice explicit when applying the theory. The verdicts above are robust to it, but in problems with long histories they need not be.

**(c) Priors on one's own other nodes.** A-FDT needs a prior $q$ over $\textsc{fdt}(x')$ for inputs $x'\ne x$. In the paper's examples $q$ washes out. The paper notes that the "correct" values are 0 or 1 but "it doesn't matter if Fiona has some uncertainty." This is the point where A-FDT and policy-FDT can come apart. Here is an illustration of my own. Two copies of the agent are told "red" and "blue" respectively, and each picks L or R. Both receive 10 if both pick L, 1 if both pick R, and 0 if they mismatch. The red copy intervenes on $\textsc{fdt}(\text{red})$ and holds $\textsc{fdt}(\text{blue})$ at its prior. If that prior puts 0.95 on R, then L yields $0.05\times 10=0.5$ and R yields $0.95\times 1=0.95$, so red picks R. Blue reasons symmetrically. The prior fulfils itself, and the pair lands on the inferior (R, R). Policy-FDT chooses the whole map $\{\text{red},\text{blue}\}\to\{L,R\}$ at once and selects (L, L). This matches the authors' remark that the policy formulation "makes a difference in certain multi-agent dilemmas." The lesson for applying A-FDT is to treat the paper's stipulation of *accurate* self-models seriously. If the agent's priors about her other-input behaviour are themselves derived from A-FDT, a fixed-point requirement, the trap above is avoided only if the fixed point selected is the good one. A-FDT as stated in Equation (4) does not guarantee that.

**(d) Zero-probability actions.** EDT cannot evaluate an act of prior probability 0. The paper notes that "given extreme priors, Eve can be made to do *anything*." A-FDT's $\mathtt{do}$ is defined regardless of the prior on the intervened node. Even when Fiona is nearly certain she one-boxes, she can evaluate two-boxing by imagining the counterpossible world in which her function outputs "two-box." This is the paper's answer to the objection that a confident one-boxer should "notice" the full box and defect.

**(e) Ties and randomization.** Equation (4) returns an argmax set and is silent on ties and on whether mixed acts belong to $\mathcal A$. A natural convention is to allow randomization only via sources that the relevant predictors cannot model, represented as nodes with no edge from $\textsc{fdt}$. This is my assumption. It matters in Death-in-Damascus variants with a genuinely random coin, where such a coin is worth buying.

**(f) Scope: "fair" problems.** The paper claims superiority only in problems where "the outcome depends only on the agent's behavior in the dilemma at hand," as opposed to problems that punish a named algorithm. It admits that a formal criterion of fairness is still lacking, and footnote 15 gives a case that is hard to classify.

## 7. Dominance, regret, and "control"

A standard objection is that two-boxing dominates. The paper's reply is that dominance is defined relative to a way of building hypotheticals. Under CDT's surgery two-boxing dominates. Under A-FDT's surgery, "holding constant all relevant subjunctive dependencies," one-boxing never does worse. Under EDT's conditioning, refraining "dominates" in the lesion problem. Dominance therefore cannot adjudicate between the theories; it restates each one. The paper's alternative criterion is utility achieved across fair problems.

On control, the paper argues that A-FDT is "no more deluded" than CDT. A deterministic CDT agent cannot really do otherwise either. Both theories use imagined variation as an instrument: one varies the token act, the other varies the type.

## 8. Conclusion

A-FDT, as given by Equation (4), is expected-utility maximization with a particular choice of counterfactual. The agent intervenes, Pearl-style, on the node representing her decision function's output for her actual input. She propagates the change to everything the dependency graph says computes or models that function, and she uses her observation only to choose which node to intervene on, never to condition. The resulting verdicts follow by direct computation: one-box, smoke, cooperate with a twin, pay in Parfit's desert, one-box in transparent Newcomb, refuse blackmail below an explicit error threshold, and stay in Damascus.

The theory's force lies in its single rule. Its weak points are the inputs to that rule: a principled method for building subjunctive-dependence graphs, a specified prior, and a treatment of one's own behaviour on other inputs. The last of these is where the action-based formulation A-FDT can fall short of its policy-based refinement.

---

**References.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060). Pearl, J., *Causality* (2000). Joyce, J., *The Foundations of Causal Decision Theory* (1999). Gibbard, A. & Harper, W., "Counterfactuals and Two Kinds of Expected Utility" (1978).