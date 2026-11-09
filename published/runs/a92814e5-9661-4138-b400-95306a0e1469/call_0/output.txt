# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea in one paragraph

Suppose an agent is facing a decision. The theory discussed here, **A-FDT** (action functional decision theory), says that the agent's choice is the output of a fixed mathematical function. The function takes her world-model and observations as input. She should ask, in the words of the source's abstract, "Which output of this very function would yield the best outcome?" To answer, she imagines the function returning each candidate action, adjusts everything that *depends on that function's output* (her own body's behaviour, but also any twin, simulation, or predictor that computes or models the same function), holds everything else fixed, and picks the action whose imagined world has the highest expected utility.

This essay follows Equation (4) of Section 5 of Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality". It states the formal definition, explains the moving parts, and works through examples. It also flags where the source leaves things undetermined, and I try to say whether each claim comes from the source or is my own addition. The source calls its theory "FDT". I use **A-FDT** for the theory defined by Equation (4) and call the other theories by their own names: CDT (causal), EDT (evidential), and the variants FDT′ and FDT\* that the source considers and sets aside (§3).

## 2. The formal setting

### 2.1 Expected utility with a pluggable "hypothetical"

The source starts from a schema shared by EDT, CDT and A-FDT (its Equation 1). An agent executes an action $a\in\mathcal A$ maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $o_j$ range over outcomes, $x$ is the observation history, and $P(a\hookrightarrow o_j;x)$ is the probability that $o_j$ obtains "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$". The connective $\hookrightarrow$ is deliberately left open. Following Joyce, the source says the theories differ only in "the epistemic perspective from which actions are to be evaluated", that is, in how they interpret $\hookrightarrow$.

The source adds a procedural reading. The agent keeps a world-model $M$. For each action $a$ she constructs a *hypothetical* $M^{a\hookrightarrow}$, a scratch-paper object rather than a belief or a metaphysical possible world. She computes a value $V_a$ from each hypothetical and takes the argmax. The theories differ in what $M$ contains and how hypotheticals are built from it.

### 2.2 The three equations

The source gives three decision rules. With $V:=\mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a)$. The hypothetical is Bayesian conditionalization.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x)$. The model is a pair $(P,G)$ with $G$ a causal graph, and the hypothetical is Pearl-style surgery on the physical action node.
- **A-FDT** (Eq. 4):

$$\boxed{\;\text{A-FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\textsf{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}$$

### 2.3 Reading Equation (4) carefully

**The model.** $P$ is a probability distribution over variables of the agent's model. These include ordinary variables and variables for the outputs of mathematical functions. The source's example is a variable for $6288+1048$ that has most of its probability on $7336$. $G$ is a graph that "tells us how changing a logical variable affects all other variables". It is richer than a causal graph: it records "the logical, mathematical, computational, causal, etc. structure of the world more broadly."

**The intervened node.** $\textsf{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model representing the output of A-FDT itself on inputs $P$, $G$ and $x$. The underlines denote dequoting. If $x:=3$ then $\textsf{Z}\underline{x}$ names the variable $\textsf{Z}3$. So the node's *name* depends on the model that contains it.

**Self-reference.** This looks circular, but the source argues it is harmless. The agent need not know the *value* of $\text{A-FDT}(P,G,x)$ to have a variable *representing* that value, and Kleene's second recursion theorem ("quining") shows how a data structure can contain an accurate representation of itself.

**Observation.** In CDT, an observation changes what one conditions on. In A-FDT, "FDT responds to observation by changing which node it intervenes upon." Seeing $y$ rather than $x$ means intervening on $\textsf{fdt}(\underline P,\underline G,\underline y)$ rather than $\textsf{fdt}(\underline P,\underline G,\underline x)$. The agent does not condition the model on $\textsf{Obs}=x$ in the Eq. (3) manner. This is the "updateless" feature. A policy is a map from observations to actions. A-FDT treats the whole family of nodes $\{\textsf{fdt}(\cdot,\cdot,x')\}_{x'}$ as part of the model. The graph decides which of them controls the agent's body in a given world, and which of them are copied by predictors.

**The $\mathtt{do}$ operator.** $\mathtt{do}$ is Pearl's surgery. Set the chosen node to the value, sever its incoming edges, and recompute everything downstream, leaving everything else untouched. What changes is that "downstream" is read in $G$, and $G$ may contain edges from the logical node to things that merely *model* or *copy* it.

**Comparison with CDT.** The source lists exactly two differences: the intervention point is the decision function's output instead of the physical act, and observations select a node instead of being conditioned on.

**A consistency check.** When all correlations between $\textsc{Act}$ and other variables are caused by $\textsc{Act}$, the source shows all three theories agree:
$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsf{fdt}=a)]$. They come apart only when something correlates with the action without being caused by it, as when another agent predicts you.

## 3. Subjunctive dependence and counterpossibles

The source's organizing slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." (The source's "functional decision theory" is what I call A-FDT.)

**Subjunctive dependence.** "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Two calculators computing $6288+1048$ are the stock example. Observing one output $7336$ licenses an inference about the other, even if the dependence is imperfect, because of cosmic rays or hallucination. Three clarifications from the source:

1. Causal dependence is a special case. A scribe copying a calculator's output both causally and subjunctively depends on it.
2. Mere statistical correlation is not subjunctive dependence. Two pink calculators on different continents share a colour by coincidence. Had the scribe bought a green one, the other would still be pink.
3. The dependence need not trace to a common cause. Two civilizations might independently converge on arithmetic or on a decision theory.

**Type versus token.** CDT intervenes on the token "my action is $a$". A-FDT intervenes on the *type*, the function's output.

**Counterpossibles.** If the function does output *cooperate* on this input, then it does so of logical necessity, so imagining it outputting *defect* is a counterpossible. The source concedes this "is the main drawback of FDT relative to CDT at this time". It offers three mitigating points:

- Mathematicians reason sensibly under logical uncertainty (the twin prime conjecture, say).
- The agent needs only narrow counterpossible questions, such as how a particular predictor's prediction would change if the function's output changed.
- Humans do this tolerably.

The source considers a variant, "FDT′", in which the agent asks "what if I used a different decision function $f_n\in\mathcal F$?" It argues this does not avoid the problem. The predictor still predicts $d$, so the agent must imagine all predictors of $d$ predicting as if $d$ behaved like $f_n$, which brings back the counterpossible. It also mentions an evidential "$\text{FDT}^*$" with a $\mathtt{true}(\cdot)$ operator that conditions on logical sentences. It says we "currently lack a formal definition of conditional probabilities that can be used with false logical sentences". That is why Equation (4) takes $G$ as an *input*.

**What is missing.** The source states it plainly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables", but "it is not yet clear how to construct such a thing—nor even whether it can be done in a satisfactory manner within Pearl's framework."

## 4. A usable procedure, and what it presupposes

Here is the algorithm that Equation (4) specifies when everything is supplied.

1. Take the world-model $(P,G)$ and the observation $x$ as given.
2. Locate the node $\textsf{fdt}(\underline P,\underline G,\underline x)$ in $G$.
3. For each action $a$: perform $\mathtt{do}(\textsf{fdt}(\underline P,\underline G,\underline x)=a)$, propagate along all edges leaving the node, compute $\mathbb E(V)$.
4. Output the maximizing $a$.

What follows from the source is only this: the graph must encode all decision-relevant subjunctive dependencies, and the source treats this as input. My additions below are operational suggestions, not claims of the paper.

**Heuristic for drawing the graph (mine).** For each variable $Z$ in the problem, ask: *if the computation I am running returned a different output on this input, would $Z$ be different?* There are three cases.

- The variable $Z$ is produced by something that runs, models, or simulates this computation: a twin, a predictor, a record produced by reliable prediction, or the agent's own later selves. Then draw an edge from the node to $Z$.
- The variable $Z$ is downstream of my action causally (the box contents *after* I take them, say). The edge comes through $\textsc{Act}$, as in CDT.
- The variable $Z$ is merely correlated with my action through a process that does not compute my decision: a lesion, a shared upbringing, a pink calculator. Then draw no edge.

**Imperfect dependence (mine, in the source's spirit).** The source's Newcomb graph handles a 99%-accurate predictor by a noise node $\textsc{Accurate}$ feeding $\textsc{Prediction}$, so that the dependence is strong but not deterministic. For a dependence of fidelity $\rho$, introduce a noise variable with probability $\rho$ of "copy works". This keeps the graph a standard probabilistic model and keeps Eq. (4) well defined.

**Beliefs about my own behaviour elsewhere.** The graph often contains *other* A-FDT nodes (for other observations). The agent needs priors on their values. In the examples below such priors enter (the source's $q$) but turn out not to affect the decision. I would add that in general this can matter, and the source does not give a recipe.

**Policy versus action.** Footnotes 7 and 16 say the authors' *preferred* formalization intervenes on a *policy* (a map from observations to actions) rather than an action. They say the difference matters only in certain multi-agent dilemmas and is set aside. Equation (4) as printed intervenes on the observation-indexed node. I follow the printed equation. A reader doing multi-agent problems should know the preferred version differs.

## 5. Worked examples

### 5.1 Newcomb's problem

Let the model be as in the source: a node $F=\textsf{fdt}(\underline P,\underline G)$ with edges to $\textsc{Act}$ and to $\textsc{Prediction}$; $\textsc{Accurate}$ is accurate with probability 0.99 and feeds $\textsc{Prediction}$; $\textsc{Prediction}$ determines $\textsc{Box B}$; $\textsc{Act}$ and $\textsc{Box B}$ determine $V$. The "inaccurate" branch flips the prediction.

- $\mathtt{do}(F=\text{onebox})$: action is onebox; box full with probability 0.99. $\mathbb E V = 0.99\times 1{,}000{,}000 = \$990{,}000$.
- $\mathtt{do}(F=\text{twobox})$: box full with probability 0.01. $\mathbb E V = 0.01\times 1{,}001{,}000+0.99\times 1{,}000=\$11{,}000$.

A-FDT one-boxes. The source's text prints the first figure for EDT as $\$999{,}000$. By the stated 0.99 and payoffs it should be $\$990{,}000$, and I take that to be a typo.

CDT's graph differs: its intervened node is $\textsc{Act}$, and $\textsc{Act}$ has no edge into $\textsc{Prediction}$. Whatever the probability $p$ of a full box, two-boxing gains $\$1{,}000$. EDT's reasoning gets one-boxing for a different reason: it conditions on the action, and the action is correlated with a "predisposition".

The source emphasizes that A-FDT uses no retrocausal physics: "she just thinks it is foolish to imagine her action changing without also imagining $\text{FDT}(P^F,G^F)$ taking on a different value". Also, the objection "she is nearly certain she is a one-boxer and box B is probably full, so shouldn't she take both?" fails. Asked what would happen if she two-boxed, she imagines the A-FDT function itself outputting *twobox*, and in that scenario the box is likely empty.

### 5.2 The smoking lesion

Here the graph must differ, and that is the point. A lesion is not a predictor: it "is not evaluating the agent's future decisions". The correlation between the lesion and smoking runs through the lesion's effect on *desires*. Formalizing as the source does, the lesion determines which of two utility functions governs the agent, so there are two nodes, $\textsf{fdt}(\underline{P_S},\underline G)$ and $\textsf{fdt}(\underline{P_R},\underline G)$, and $\textsc{Act}$ copies one or the other depending on $\textsc{Lesion}$. Intervening on the relevant node does not change $\textsc{Lesion}$, with probability $p$ of the lesion held fixed in both hypotheticals. Smoking therefore beats refraining by $p\cdot\$1{,}000$, and A-FDT smokes.

The lesson is that one rule yields one-boxing in Newcomb's problem and smoking here. The difference comes entirely from the graph, which marks one dependence as subjunctive and the other as merely statistical. The source adds that this problem is contrived (the agent is uncertain about her own desires) and recommends dropping it.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

The agent sees a full box B and must choose. CDT and EDT two-box: "given that box B is full, an agent does better by taking both boxes."

A-FDT's graph has two nodes: $\textsf{fdt}(\ldots,\textit{full})$ and $\textsf{fdt}(\ldots,\textit{empty})$. The *full-box node* feeds $\textsc{Prediction}$ (the predictor predicts what the agent does on seeing a full box) and $\textsc{Act}$. $\textsc{Prediction}$ then selects which node controls $\textsc{Act}$. With $q$ the prior probability that she two-boxes on an empty box:

- $\mathtt{do}(\textsf{fdt}(\ldots,\textit{full})=\text{onebox})$: $\mathbb E V = 0.99\times1{,}000{,}000+0.01\,q\times 1{,}000 = 990{,}000+10q$.
- $\mathtt{do}(\textsf{fdt}(\ldots,\textit{full})=\text{twobox})$: $\mathbb E V = 0.01\times1{,}001{,}000+0.99\,q\times1{,}000 = 10{,}010+990q$.

(The source prints "$\$110{,}00+q\cdot\$990$", which is garbled; the arithmetic gives $10{,}010+990q$.) One-boxing wins for any $q\in[0,1]$. Notice that in these calculations the expectation is taken over worlds in which the agent would have seen an empty box. The text writes "$\mathtt{do}(\ldots),\textsc{Obs}=\textit{full}$" but the numbers do not condition on that observation, which matches Equation (4) as printed. The source also notes that this is exactly the same structure as paying in Parfit's hitchhiker. An A-FDT agent pays at the ATM, and, being predictably such an agent, is rescued.

### 5.4 Blackmail

*Mechanical blackmail.* The blackmailer runs the program iff she predicts the agent would pay upon receiving the letter. Given the letter, A-FDT compares $\mathtt{do}(\textsf{fdt}(\ldots,\textit{blackmail})=\text{pay})$ with $=\text{refuse}$. Paying makes the blackmail near-certain and costs \$1,000. Refusing makes blackmail near-impossible. Refusing wins, even though in the actual world she holds the letter. In the source's words, the agent imagines "worlds in which her observations were different".

With imperfect prediction (error $\varepsilon$ in the "wrongly predicts she will pay" direction), refusing costs $\varepsilon\times\$1{,}000{,}000$ in expectation and paying costs a certain \$1,000. So A-FDT refuses iff $\varepsilon<0.1\%$. The source's two cases are $0.09\%$ (refuse, expected loss \$900) and a "$0.011\%$" case in which it says she pays. By my computation $0.011\%$ gives an expected loss of \$110 from refusing, so she would still refuse. I suspect that figure is a slip for something above $0.1\%$, and the threshold is what matters.

*XOR blackmail.* The infestation is not downstream of the A-FDT node, but the letter-sending is. Changing the node changes the probability of receiving the letter, not the probability of termites. A-FDT refuses. EDT pays, because conditioned on paying the letter implies no termites.

### 5.5 Death in Damascus

Death's appointment-book entry depends on a prediction of the agent's decision procedure. $\mathtt{do}(\text{flee})$ puts Death in Aleppo: $-\$1{,}000$ and death. $\mathtt{do}(\text{stay})$ puts Death in Damascus: death with no travel cost. Stay wins, with no instability. CDT, by contrast, holds Death's location fixed when varying the act, so whichever place it currently expects to be, it wants the other.

Add a fair coin that Death truly cannot predict (my modelling): a node independent of the A-FDT node feeds $\textsc{Act}$. Then $\mathtt{do}(\textsf{fdt}=\text{flip})$ gives survival probability $0.5$ for \$1, and A-FDT buys it. The source argues a CDT agent declines the coin, because CDT's hypotheticals treat her own randomness as independent of Death's location.

### 5.6 A twin prisoner's dilemma with imperfect twin (my extension)

Let the twin copy the agent's output with probability $\rho$ and otherwise do the opposite. With payoffs as in the source:

- cooperate: $\rho\cdot 1{,}000{,}000+(1-\rho)\cdot 0$;
- defect: $\rho\cdot1{,}000+(1-\rho)\cdot 1{,}001{,}000$.

Cooperating wins iff $2{,}000{,}000\,\rho>1{,}001{,}000$, i.e. $\rho>0.5005$. The source says the dependence is "weakened, but not eliminated" with imperfection but gives no such threshold. In the limit $\rho=1$ this recovers the source's cooperation; at $\rho=1/2$ the twin is independent and A-FDT defects like CDT.

## 6. Why one should believe it: the source's arguments

**Utility.** The primary case is performance: A-FDT agents are predictably one-boxers, hitchhikers who pay, and blackmail-proof, and so, in the source's view, get rich. The source says "we would expect the correct decision theory to endorse its own use", and CDT does not, since by its own lights an agent should self-modify away from it. A-FDT agents "always act as they would have precommitted to act", so they need no costly precommitment.

**Value of information.** Because A-FDT chooses the same way ex ante and ex post, it does not assign negative expected value to information, unlike EDT, which would pay to avoid seeing a full box.

**Dominance.** Two-boxing "dominates" only if dominance is defined with CDT counterfactuals. The source's rebuttal is that "every method for constructing hypotheticals gives rise to its own notion of dominance". It defines an analogue: $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies, switching the output of the agent's algorithm from $b$ to $a$ is sometimes better (and never worse)". In Newcomb's problem the CDT version is like asking us to imagine a working calculator that outputs $3159$ for $6288+1048$ "holding constant the fact that $6288+1048=7336$". Under the A-FDT notion, A-FDT never takes a dominated action.

**Balance of hypotheticals.** The source's diagnosis: EDT's hypotheticals "respect too many correlations" (the cosmic ray problem: Eve takes \$1 because taking \$100 would be evidence of a ray); CDT's "respect too few" (it imagines predictors failing exactly when it decides). A-FDT keeps those correlations that are logically or computationally grounded and drops merely statistical ones.

**No delusion of control.** A-FDT is no more delusional than CDT: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token." Both are devices for evaluating options in a deterministic world.

## 7. Limits and open questions

1. **The graph is the theory.** Equation (4) is only as good as $G$. Different graphs for the same story give different answers, as the lesion and Newcomb cases show. The source offers no method for learning subjunctive structure. My heuristic in §4 is a way to apply the idea in clear cases, not a solution. It presupposes that we can tell when something "runs the same computation", and degrees of similarity (a coarse model of me, a person who reasons similarly) are not covered.
2. **Counterpossibles remain informal.** Taking $G$ as given hides rather than solves the problem of what it means for a necessarily-fixed function to output something else.
3. **Fairness.** The source's claim is that A-FDT does at least as well as CDT and EDT "in all dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand". It admits this has no formal definition. Footnote 15 gives a counterexample showing the difficulty. If a copy of an A-FDT agent punishes anyone who does what the copy does, the A-FDT agent always loses while CDT and EDT agents may win. The source calls such problems unfair but cannot formalize how to compare across theories. Newcomb is fair because the predictor "punishes *two-boxers*". A mind-reader that rewards or punishes a *decision procedure* as such is not.
4. **Beliefs about oneself.** The $q$-terms show A-FDT needs priors on its own behavior at other observations. They did not matter in the source's examples, but the general case is not treated. The source also notes that EDT has a problem of its own with self-referential priors, which is why it needs ratification.
5. **Evidence of oddness.** One-boxing on seeing two full boxes, or refusing the blackmailer while holding the letter, may seem to show that A-FDT's notion of rationality diverges from ours. The source accepts these implications and answers with the utility argument. A reader who gives more weight to intuitions about such cases will not be moved.
6. **Evaluation.** The source's evidence is a set of selected dilemmas. It says it does not know "whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."

## 8. Conclusion

A-FDT, as given by Equation (4), keeps the expected-utility skeleton shared with CDT and EDT and changes only the epistemic perspective. The agent intervenes with $\mathtt{do}$ on a node representing the output of her own decision function, evaluated at her actual observations. A graph encoding all decision-relevant dependencies, causal and logical, propagates the change. Because predictors, twins and records of one's behaviour live downstream of that node, A-FDT cooperates with its twin, one-boxes, pays the hitchhiker, refuses blackmail and stays in Damascus. Because lesions and coincidental correlations do not, it smokes and takes the \$100 in the cosmic ray problem. Observation works by changing which node is intervened on, which is why A-FDT acts as it would have precommitted to act.

The cost is that the theory needs a graph of subjunctive dependencies and a workable account of reasoning about "what if this computation returned something else", and the source supplies neither in general. My operational suggestions (the three-way dependence test, noise nodes for imperfect copying, explicit priors on other nodes) make the equation usable in clear cases, but they are additions. The source's own verdict is that the theory is a promising advance, not a finished one.

## References

- Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (the source for all definitions and quotations here).
- Joyce, J. M., *The Foundations of Causal Decision Theory* (1999).
- Pearl, J., *Causality* (2000).
- Gibbard, A. & Harper, W., "Counterfactuals and Two Kinds of Expected Utility" (1978).
- Soares, N. & Fallenstein, B., "Toward Idealized Decision Theory" (2015).