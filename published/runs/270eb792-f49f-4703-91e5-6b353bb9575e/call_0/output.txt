# A-FDT: Action Functional Decision Theory

*How to decide by intervening on the output of your own decision procedure*

## 1. The question A-FDT asks

Decision theories in the expected-utility tradition agree that you should pick the act with the highest expected utility. They disagree about which hypothetical you should evaluate when you ask "what if I did $a$?"

- **Evidential decision theory (EDT)** conditions on the act.
- **Causal decision theory (CDT)** intervenes on the physical act.

Yudkowsky and Soares's *Functional Decision Theory* proposes a third answer. The agent treats her decision as the output of a fixed mathematical function and asks "Which output of this very function would yield the best outcome?"

The paper's main formal statement, its Equation (4), selects an **action** for the agent's current input. The authors say their preferred formalization selects **policies**, which are maps from observations to actions. To keep the two apart, this essay uses two names:

- **A-FDT** (action functional decision theory) is the rule in Equation (4).
- **P-FDT** (policy-selecting FDT) is the variant the paper mentions in footnotes but does not formalize.

When I quote the source, its word "FDT" refers to what I call A-FDT, unless the quotation concerns the policy variant.

This essay covers the formal rule, the idea of "subjunctive dependence" behind it, worked examples, and the places where the paper leaves the procedure underdetermined. I mark clearly which claims are the paper's and which are my own interpretation.

## 2. The common frame

The paper starts, following Gibbard and Harper, from a generic expected-utility schema:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is the connective for decision hypotheticals. Following Joyce's representation theorem, the paper treats the rival theories as rival interpretations of $\hookrightarrow$. In Joyce's words they differ about "the epistemic perspective from which actions are to be evaluated."

Write $V = \mathcal U(\textsc{Outcome})$. The two classical interpretations are:

$$
\mathrm{EDT}(P,x) = \arg\max_{a}\ \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big), \tag{2}
$$

$$
\mathrm{CDT}(P,G,x) = \arg\max_{a}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big). \tag{3}
$$

In (3), $G$ is a causal graph over the variables of $P$, and $\mathtt{do}$ is Pearl's intervention operator. The operator severs the incoming edges of the target node, sets its value, and recomputes only its descendants.

The paper describes all three theories procedurally. The agent holds a world-model $M$. For each action she constructs a hypothetical $M^{a\hookrightarrow}$, computes a value $V_a$, and acts on the best one. Hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs themselves. This distinction matters later: an A-FDT agent can believe one thing about the actual world while evaluating hypotheticals that look quite different.

## 3. The definition of A-FDT

A-FDT requires a richer world-model.

- **Logical variables.** $P$ must contain variables for the outputs of mathematical functions. That includes a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ standing for "the output of the A-FDT algorithm when run on inputs $(P,G,x)$." The underlines denote dequoting: the variable's *name* is built from the agent's actual model and observation.
- **A dependence graph.** $G$ must encode not only causal structure but "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, it encodes which variables would change if the output of that function changed.

Given these inputs, the paper defines:

$$
\boxed{\ \text{A-FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).\ } \tag{4}
$$

The paper identifies exactly two differences from CDT.

1. **Point of intervention.** CDT intervenes on the physical act $\textsc{Act}$. A-FDT intervenes on the logical node representing its own algorithm's output. In the paper's Peircean phrasing, CDT intervenes on the *token* and A-FDT on the *type*.
2. **Response to observation.** CDT conditions on $\textsc{Obs}=x$. A-FDT instead changes *which node* it intervenes on: it intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline x)$ when its history is $y$. Equation (4) contains no conditioning on $x$.

The self-reference in (4) is, the paper argues, harmless. The agent needs a variable that *represents* her output, not knowledge of its value. Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.

The paper also mentions an idealized alternative, $\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\ldots)=a))$, where $\mathtt{true}$ updates on a possibly false logical sentence. It sets this aside because "it's not clear how to define a $\mathtt{true}$ operator." The graph $G$ stands in for an account of counterpossible reasoning. Whatever $G$ says would change if the function had a different output is what A-FDT treats as changing.

## 4. Subjunctive dependence

The informal criterion behind $G$ is **subjunctive dependence**. The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper explains this with calculators.

- **Same computation.** Two working calculators computing $6288+1048$ produce matching outputs. Neither causes the other; both depend on the same arithmetic fact. Likewise, a twin who runs the agent's reasoning, or a predictor who models it, has behavior that subjunctively depends on the agent's decision function.
- **Causal dependence as a special case.** A scribe copying the calculator's output depends on it both causally and subjunctively.
- **Mere correlation.** If two calculators in Paris and Tokyo happen to be pink, there is no subjunctive dependence between their colors.

The paper uses this criterion to separate Newcomb's predictor, which "builds an accurate model of the agent and reasons about her behavior," from the smoking lesion, which "does no such thing." In graph terms the rule is:

> In $G$, draw an edge from the node $\textsc{fdt}(\underline P,\underline G,\underline x)$ to every variable that is computed by, or is a model of, the agent's decision function on input $x$. Mere statistical correlates get no such edge.

## 5. Worked examples

All numbers below follow the paper's models. Dollars stand for utility.

### 5.1 Twin prisoner's dilemma

Both the agent's act and her twin's act are children of the same $\textsc{fdt}$ node. Setting the node to *cooperate* yields mutual cooperation and \$1,000,000. Setting it to *defect* yields mutual defection and \$1,000. So A-FDT cooperates.

CDT defects, because by dominance the twin's act is held fixed. EDT also cooperates, but by conditioning, which is the mechanism that fails in the cases below.

### 5.2 Newcomb's problem

Fiona is the paper's A-FDT agent. In her graph, $\textsc{fdt}(\underline P,\underline G)$ has two children:

- $\textsc{Act}$;
- $\textsc{Prediction}$, which also has an independent noise parent $\textsc{Accurate}$ with $P(\textit{accurate})=0.99$.

Box B is full iff the prediction is "one-box."

$$
\begin{aligned}
\mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})\big) &= 0.99\times \$1{,}000{,}000 = \$990{,}000,\\
\mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})\big) &= 0.01\times\$1{,}001{,}000 + 0.99\times\$1{,}000 = \$11{,}000.
\end{aligned}
$$

So A-FDT one-boxes. CDT's surgery on $\textsc{Act}$ leaves $P(\textit{full})=p$ unchanged, and two-boxing then wins by \$1,000 for every $p$.

The paper anticipates an objection: once Fiona is confident that the box is full, shouldn't she grab the extra \$1,000? Her hypotheticals answer no. To two-box, her algorithm would have to output *twobox*, and the predictor models that algorithm. She needs no retrocausation, only the claim that her act and the prediction are "two well-functioning calculators" running the same function.

### 5.3 Smoking lesion

Here $\textsc{Cancer}$ hangs off $\textsc{Lesion}$, not off any $\textsc{fdt}$ node.

The paper formalizes the problem carefully. The lesion settles which of two utility functions the agent has ($\mathcal U_S$, liking smoking, or $\mathcal U_R$). It therefore settles which of two algorithm nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. Fiona does not know which node is hers.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by exactly $p\cdot\$1{,}000$, so A-FDT smokes.

This is the paper's central claim against Gibbard and Harper: a single rule can both one-box and smoke. A-FDT does so because the predictor depends on the agent's algorithm and the lesion does not.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible, and the agent sees box B full. Fiona's graph has two nodes:

- $\textsc{fdt}(\ldots,\textit{full})$, which feeds the prediction;
- $\textsc{fdt}(\ldots,\textit{empty})$.

The prediction determines which of the two controls $\textsc{Act}$. Let $q$ be her prior probability that she two-boxes on seeing an empty box. Intervening on the *full* node gives:

$$
\begin{aligned}
\textit{onebox}:&\quad 0.99\times\$1{,}000{,}000 + 0.01\cdot q\cdot\$1{,}000 = \$990{,}000 + \$10q,\\
\textit{twobox}:&\quad 0.01\times\$1{,}001{,}000 + 0.99\cdot q\cdot \$1{,}000 = \$10{,}010 + \$990q.
\end{aligned}
$$

(The extracted source prints the second line garbled as "\$110,00 + q·\$990"; the value above is the correct one.) One-boxing wins for every $q\in[0,1]$. So A-FDT leaves the \$1,000 behind *while looking at a full box*.

The paper argues this is equivalent to paying the driver in Parfit's hitchhiker problem. It backs that verdict with three arguments:

- **Precommitment:** CDT and EDT agents would both precommit to one-boxing.
- **Value of information:** A-FDT never assigns negative value to information.
- **Utility:** predictors fill the boxes of agents who reason this way.

### 5.5 Blackmail

**XOR blackmail.** The letter arrives iff exactly one of two things holds: no termites and the agent will pay, or termites and the agent will not pay. EDT pays, because conditioning on paying makes termites impossible. A-FDT refuses. Intervening on $\textsc{fdt}(\ldots,\textit{letter})$ changes whether the letter is sent, but not whether the house has termites.

**Mechanical blackmail.** The blackmailer runs the incriminating program only if she predicts the agent would pay. A-FDT refuses even while holding the letter, because "refusing corresponds to a world where I never get blackmailed."

The paper adds an imperfect-predictor variant with error rate $\varepsilon$, the probability that the blackmailer wrongly predicts payment.

- Under *pay*, the agent is always blackmailed and loses \$1,000.
- Under *refuse*, she is blackmailed with probability $\varepsilon$ and loses \$1,000,000 in that case.

So A-FDT refuses iff $\varepsilon\cdot 10^6 < 10^3$, that is, iff $\varepsilon < 0.1\%$. The paper's $\varepsilon = 0.09\%$ correctly yields "refuse." Its second figure ("0.011%, then she pays") contradicts this threshold and looks like a typo for something above 0.1%. The rule itself is unambiguous: compare the two hypotheticals.

### 5.6 Death in Damascus

Death's appointment book is a perfect prediction of the agent's algorithm. Intervening on the $\textsc{fdt}$ node moves Death along with the agent. Survival is therefore impossible either way, and A-FDT stays in Damascus to save the \$1,000.

CDT oscillates instead. The paper notes that it even refuses to pay \$1 for a truly random coin that would give a 50% chance of survival. A-FDT values such a coin correctly, because only an output the predictor cannot track breaks the dependence.

## 6. When A-FDT agrees with CDT and EDT

The paper states an agreement condition. Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories prescribe the same act. In ordinary single-agent problems with no predictors, twins, or common-cause confounders, A-FDT is simply expected-utility maximization. Disagreements arise only when something other than the agent's body computes or models her decision function.

The paper also reframes **dominance**. Every way of building hypotheticals induces its own dominance relation. Two-boxing dominates under CDT's surgery; one-boxing dominates under A-FDT's. Dominance therefore cannot settle the dispute neutrally, and the authors fall back on utility achieved in "fair" problems. They define these as problems where the agent's beliefs are accurate and the outcome depends only on her behavior in the dilemma, not on *how* she reaches it.

## 7. An operational recipe (my reconstruction)

The paper gives Equation (4) and worked graphs but no general algorithm for building $(P,G)$. The following procedure is my interpretation. It reproduces every example above.

1. **List the variables:** world states, the agent's act, outcomes, $V$, and every agent or artifact whose behavior is generated by a model of the agent.
2. **Index decision nodes by input.** For each input $y$ on which some process consults the agent's function (her actual observation $x$, or a counterfactual observation a predictor simulates), add a node $\textsc{fdt}(\ldots,y)$.
3. **Wire the subjunctive edges.** Draw an edge from $\textsc{fdt}(\ldots,y)$ to every variable that computes or models the function's output on $y$. Model a predictor's imperfection as an independent noise parent, like $\textsc{Accurate}$. Wire $\textsc{Act}$ so that the *realized* observation selects which node controls it. This "switch" structure appears in the transparent Newcomb and blackmail graphs.
4. **Put priors on everything else,** including the nodes for inputs other than $x$ (the paper's $q$ parameters).
5. **Intervene on $\textsc{fdt}(\ldots,x)$ only, without conditioning on $\textsc{Obs}=x$.** Compute $\mathbb E(V)$ for each $a$ and take the argmax.

Step 5 needs defending, because the source is internally inconsistent here. Equation (4) contains no conditioning on $x$, and the paper says A-FDT "responds to observation by changing which node it intervenes upon" rather than by conditioning. Yet in the transparent Newcomb section the target expression is written $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis.

The accompanying arithmetic shows the formula was not applied that way. The computation sums over worlds in which the box is *empty*, which conditioning on *full* would rule out. I therefore read the $\textsc{Obs}$ term as a notational slip, and treat $P$ as the agent's model *before* conditioning on the observation the node is indexed by.

Two further considerations support this reading.

- A draft footnote in the source says that conditioning on evidence *and* changing the intervention point "creates a kind of 'double update' which proves harmful in practice."
- The un-conditioned reading is exactly what lets A-FDT entertain that "if their action were different, they might have *made different observations*."

## 8. Open questions and what they imply

**Constructing $G$.** The paper is frank here: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Equation (4) is a function of $G$, so A-FDT's verdicts are only as determinate as the dependence graph. The hard cases are partial similarity:

- a predictor who models a *simplified* version of you;
- an agent who runs a *related* but non-identical algorithm.

The paper's calculator analogy suggests treating such cases as noisy copies, with a noise node between the $\textsc{fdt}$ node and the copy. How much noise to assign, and when a different algorithm counts as "the same function," is not settled by the source. Any answer is an additional modeling assumption.

**Counterpossibles.** The intervention sets a logical variable to a value it cannot actually take. The paper concedes this is "the main drawback of FDT relative to CDT at this time," but calls the difficulty "technical rather than philosophical." Its reasons are that humans reason fluently under logical uncertainty, and that A-FDT needs only narrow counterpossibles of the form "how would this predictor's prediction change if my algorithm output $a$?"

The paper also defends A-FDT against the charge of "delusion." A deterministic CDT agent equally entertains hypotheticals in which her act differs from what physics fixes. Any objection to type-level control applies with equal force to token-level control.

**Actions versus policies.** This is where the A-FDT label matters. The paper's footnote reads: "In the authors' preferred formalization of FDT, agents actually iterate over policies (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

The paper gives no example of the difference. Here is one of my own, showing where A-FDT's dependence on the $q$ parameters becomes decisive.

- A fair coin determines whether the agent observes $x_1$ or $x_2$.
- In either case she chooses $A$, which pays \$1, or $B$, which pays \$0.
- A perfect predictor independently pays \$10 iff the agent's function outputs $B$ on *both* $x_1$ and $x_2$.

Observing $x_1$ and letting $q$ be her credence that $\textsc{fdt}(\ldots,x_2)=B$, A-FDT computes:

$$
\mathbb E\big(V\mid\mathtt{do}(\textsc{fdt}(\ldots,x_1)=B)\big)=10q, \qquad \mathbb E\big(V\mid\mathtt{do}(\textsc{fdt}(\ldots,x_1)=A)\big)=1.
$$

So A-FDT chooses $B$ iff $q>0.1$. The same holds symmetrically at $x_2$. Both profiles are self-consistent:

- an agent certain she plays $A$ elsewhere ($q=0$) plays $A$ and earns \$1;
- an agent who expects $B$ elsewhere plays $B$ and earns \$10.

P-FDT instead maximizes over the four policies at once and picks $(B,B)$ outright.

The general structure is that A-FDT optimizes one coordinate of the policy at a time while holding beliefs about the other coordinates fixed. Its verdicts are therefore equilibria among the agent's own input-indexed instances, not necessarily global optima. In the paper's own examples, $q$ never mattered: the source explicitly notes this for the smoking lesion and the transparent Newcomb problem. My example shows that this is a feature of those examples, not of A-FDT in general.

For applied work, this suggests a practical rule:

- when only the agent's actual input is consulted by the environment, A-FDT and P-FDT coincide;
- when the environment rewards *joint* behavior across inputs, A-FDT needs a specified, ideally reflectively consistent, prior over its own off-input outputs, and P-FDT is the safer formalization.

I also note an irony. This sensitivity to self-prediction mildly resembles the prior-dependence the paper criticizes in EDT, though A-FDT's priors here concern only its *other* outputs, never the one being chosen.

**Fairness.** The paper's superiority claim is limited to "fair" problems. It admits that a formal criterion is missing. For instance, "punish anyone who acts like a copy of Fiona" is intuitively unfair, but there is no general recipe for mapping it to an analogous problem unfair to CDT. The authors state only that they "have not been able to construct an intuitively fair dilemma where FDT loses to a rival decision theory."

## 9. Conclusion

A-FDT is an expected-utility theory with a distinctive interpretation of the decision hypothetical. Given a probability model $P$ and a graph $G$ of causal and logical dependence, it intervenes with Pearl's $\mathtt{do}$ on the node representing its own algorithm's output for the current input. It then takes the act whose hypothetical world is best, responding to observations by changing which node it intervenes on rather than by conditioning.

The result:

- It one-boxes in Newcomb's problem and smokes in the smoking lesion problem.
- It pays in Parfit's hitchhiker problem, and one-boxes even in the transparent Newcomb problem.
- It refuses blackmail, cooperates with twins, and avoids CDT's instability in Death in Damascus.
- It agrees with CDT and EDT whenever nothing in the world models the agent.

Applying it to new cases is mostly a modeling task. The agent must find every process that computes or predicts her function, on which inputs, and with what noise. The procedure leaves three things open:

- how to construct $G$;
- whether to condition on observations, which I have argued against;
- how to handle environments that reward coordinated behavior across inputs, where action selection and policy selection can come apart.

These are the main points on which A-FDT, as given by Equation (4), needs supplementary assumptions.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.