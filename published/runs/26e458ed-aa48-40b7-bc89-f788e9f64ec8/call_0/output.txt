# A-FDT: Choosing as if You Were Choosing a Function's Output

## 1. What this essay covers

Yudkowsky and Soares (2017) define *functional decision theory* by one principle: treat your decision as the output of a fixed mathematical function, and ask "Which output of this very function would yield the best outcome?" Their Section 5 makes this precise with a graphical, Pearl-style formula, Equation (4). That formula intervenes on a node whose value is an **action**. The authors say in footnotes 7 and 16 that their *preferred* formalization instead has agents "iterate over *policies* (mappings from observations to actions) rather than actions." They also say the two differ only "in certain multi-agent dilemmas."

To keep the two versions apart, I call the action-valued theory of Equation (4) **A-FDT** (action functional decision theory). I call the policy version mentioned in the footnotes **policy-FDT**. Causal decision theory (**CDT**) and evidential decision theory (**EDT**) appear only as contrasts.

Throughout, I separate three kinds of claim:

- what the paper states;
- what follows from Equation (4) by calculation;
- what I add as an operational interpretation where the paper is silent.

## 2. The common frame: expected utility over hypotheticals

The paper treats EDT, CDT and A-FDT as expected-utility theories that differ only in how they build hypotheticals. The shared template is its Equation (1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective that each theory interprets differently. Citing Joyce's representation theorem, the authors argue that "decision theories should not be seen as offering competing theories of value, but as disagreeing about the epistemic perspective from which actions are to be evaluated."

Concretely, the agent holds a world-model $M$. For each candidate action she builds a hypothetical $M^{a\hookrightarrow}$, evaluates the expected value of $V = \mathcal U(\textsc{Outcome})$ in it, and takes the best action. The paper insists hypotheticals are "decision-theoretic instruments constructed from beliefs," not beliefs. The two rival constructions are:

- **EDT** (Equation 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. The hypothetical is built by conditioning.
- **CDT** (Equation 3): $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$. The hypothetical is built by intervening on the physical act, given a causal graph $G$.

## 3. The definition of A-FDT

A-FDT's world-model is a pair $(P, G)$. Its distinctive features are these:

1. $P$ contains **logical variables**: nodes whose values are the outputs of mathematical functions on particular inputs. One such node is the output of the A-FDT algorithm itself on the agent's own model and observation. The paper writes it $\textsc{fdt}(\underline P, \underline G, \underline x)$, with underlining meaning dequotation. I abbreviate it $F_x$.
2. $G$ is a graph saying how changing such a logical variable changes other variables. It covers logical and computational dependence as well as causal dependence.

The rule is Equation (4):

$$
\textbf{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

The paper names two differences from CDT:

- A-FDT intervenes on $F_x$ (the output of the decision procedure on its inputs) rather than on $\textsc{Act}$ (the bodily act).
- A-FDT "responds to observation by changing which node it intervenes upon" rather than by Bayesian conditioning.

The self-reference in the definition is, according to the paper, harmless. The agent needs a variable *representing* her output, not knowledge of its value. Kleene's recursion theorem ("quining") shows such self-representing structures exist.

**Subjunctive dependence.** The edges leaving $F_x$ encode what the paper calls *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper adds that causal dependence is a special case, while mere statistical correlation does not qualify. Its slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

In graph terms, $F_x$ gets an arrow into every variable that represents something in the world computing or accurately modelling the A-FDT function on input $(P,G,x)$. Examples are the agent's body, a twin, or a predictor's simulation. A lesion that merely correlates with behaviour gets no such arrow.

**Why the graph is supplied rather than derived.** The paper first writes an idealized rule using a $\mathtt{true}(\phi)$ operator that updates on a logical sentence counterpossibly. It then admits "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) sidesteps the problem by requiring $G$ as input, just as CDT requires a causal graph. The cost is acknowledged openly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

## 4. How observations enter

This is the feature most worth getting right. Equation (4) contains **no** "$\textsc{Obs}=x$" term. The observation selects *which node* is intervened on, and the expectation is then taken over the full prior model, including worlds where the agent sees something other than $x$.

In those other worlds, the physical act is determined by a *different* logical node $F_{x'}$, which is not intervened on. Its value is distributed according to the prior. The structure of the model is:

$$
\textsc{Act} = F_{\textsc{Obs}}, \qquad \textsc{Obs} \text{ itself possibly downstream of } F_x \text{ (e.g. via a predictor).}
$$

There is a small inconsistency in the source that readers should know about. In the transparent-Newcomb example, the paper writes the objective as $\mathbb E(V \mid do(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$. The parenthesis is unbalanced, and the expression contains an Obs term. Yet the numbers it then computes average over the branch where the box is *empty*, which is incompatible with conditioning on $\textsc{Obs}=\textit{full}$. I therefore read Equation (4) literally: no conditioning on observation.

The paper's own remark supports this reading. It describes Timeless Decision Theory as conditioning *and* moving the intervention point, creating "a kind of 'double update' which proves harmful in practice." A-FDT is meant to update only once, by moving the intervention point.

## 5. An operational recipe (my reconstruction)

The paper decides cases by drawing a graph per problem. To decide unfamiliar cases, I propose the following procedure. The steps are my systematization, but each corresponds to a move the paper makes in its examples.

1. **Outcomes and utility.** Specify $V$. If the agent is uncertain about her own utility function, use one model per candidate utility, as the paper does in the smoking lesion problem.
2. **Logical nodes.** For every observation history $x'$ the agent might face in the scenario, add a node $F_{x'}$. Set $\textsc{Act} = F_{\textsc{Obs}}$.
3. **Subjunctive edges.** For every physical process that computes or reliably predicts the agent's output on input $x'$, draw an edge from $F_{x'}$ into it. Model predictor error with an exogenous noise node (the paper's $\textsc{Accurate}$). Draw no edges into mere correlates such as lesions or genes.
4. **Priors.** Assign priors to exogenous variables and to the logical nodes that will not be intervened on.
5. **Intervene and evaluate.** For each $a$, apply $do(F_x = a)$, propagate along $G$, and compute $\mathbb E[V]$ over the whole model. Do not condition on $x$.
6. **Choose** the arg max.

The theory's real content lies in steps 2–4. Steps 5–6 are mechanical.

## 6. Worked examples

All payoffs are in dollars-as-utility, and predictors are 99% accurate unless stated otherwise.

**Twin prisoner's dilemma.** One node $F$ feeds both the agent's act and the twin's act. Intervening $F=\textit{cooperate}$ gives \$1,000,000; $F=\textit{defect}$ gives \$1,000. A-FDT cooperates. EDT also cooperates, but by conditioning rather than by intervention.

**Newcomb's problem.** $F$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$:

$$
\begin{aligned}
\mathbb E[V\mid do(F=\textit{one})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(F=\textit{two})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT holds the probability $p$ that the box is full fixed under $do(\textsc{Act})$, so two-boxing beats one-boxing by \$1,000 for every $p$, and CDT two-boxes.

The paper answers the worry that a confident one-boxer should "notice" the box is full and two-box. Her hypothetical for two-boxing is one in which the algorithm itself outputs *two*, so the prediction changes with it. She is not asking what happens if her body deviates from her algorithm. No retrocausation is involved: "she just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

**Smoking lesion.** Structurally this is Newcomb's problem with the lesion in place of the predictor. The difference is that the lesion computes nothing, so there is no edge from $F$ to $\textsc{Cancer}$.

The paper formalizes the lesion as fixing the agent's utility function. With the lesion she uses $\mathcal U_S$ (likes smoking) and runs $F_S$; without it she uses $\mathcal U_R$ and runs $F_R$. The act is $F_S$ if she has the lesion and $F_R$ otherwise. Intervening on $F_S$ leaves $P(\textit{lesion})=p$ unchanged. Smoking therefore wins by $p\cdot\$1{,}000$: the probability that $F_S$ is actually in control, times the value of smoking. A-FDT smokes.

This is the paper's headline result: one rule both one-boxes and smokes.

**Transparent Newcomb (box B seen full).** The nodes are $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$, and the prediction determines which node controls the act. Let $q$ be the prior probability that $F_{\text{empty}}=\textit{two}$. Then:

$$
\begin{aligned}
do(F_{\text{full}}=\textit{one}):&\quad 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000+10q,\\
do(F_{\text{full}}=\textit{two}):&\quad 0.01(1{,}001{,}000)+0.99\,q(1{,}000) = 10{,}010+990q.
\end{aligned}
$$

The paper prints the second figure as "\$110,00", which is a typo. A-FDT one-boxes for every $q\in[0,1]$, while staring at a full box. CDT and EDT both two-box once they are shown the full box. The paper argues this is the same structure as paying the driver in Parfit's hitchhiker problem.

**XOR blackmail.** Let $p$ be the prior probability of termites. The letter is sent iff (no termites and the agent pays) or (termites and the agent refuses).

- $do(F_{\text{letter}}=\textit{pay})$: with termites there is no letter and a \$1,000,000 loss; without termites there is a letter and a \$1,000 payment. $\mathbb E[V]=-p\cdot 10^6-(1-p)\cdot 10^3$.
- $do(F_{\text{letter}}=\textit{refuse})$: $\mathbb E[V]=-p\cdot 10^6$.

A-FDT refuses. CDT also refuses, for a different reason: the infestation is causally upstream of its act. EDT pays.

**Mechanical blackmail with a fallible blackmailer.** The blackmailer runs the program iff she predicts the agent would pay, but with probability $\varepsilon$ she wrongly predicts payment.

- If $F_{\text{blackmail}}=\textit{pay}$, the agent is always blackmailed and loses \$1,000.
- If it is $\textit{refuse}$, she is blackmailed with probability $\varepsilon$ and loses $\varepsilon\cdot\$10^6$.

So A-FDT refuses iff $\varepsilon<0.001$. The paper's example of $\varepsilon=0.0009$ (refuse) checks out. Its second figure, "0.011%", would by the same formula still give refusal, since \$110 < \$1,000. The intended value was presumably 0.11%, which gives payment. The threshold logic is unambiguous even though the printed number is not.

**Death in Damascus.** Death's appointment book depends on $F$. Staying yields death and keeps the \$1,000; fleeing yields death and loses it. A-FDT stays, with no instability and no need for ratification. CDT, by contrast, oscillates between the two options because it holds Death's location fixed under intervention.

## 7. Structural properties

**Agreement in ordinary cases.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on $F$. Then the paper notes

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(F=a)],
$$

so all three theories agree. Disagreement requires something besides the agent's body that tracks her decision function.

**Dominance is theory-relative.** CDT's dominance argument for two-boxing holds the prediction fixed while the act varies. The paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." Under FDT-style counterfactuals, which hold subjunctive dependencies fixed, A-FDT never takes a dominated action. The paper therefore prefers utility achieved in "fair" problems as the criterion. It defines fair problems informally as those in which "the outcome depends only on the agent's behavior in the dilemma at hand" and the agent's beliefs are accurate. It admits that a formal definition is open (footnote 15).

**Reflective stability.** The paper claims FDT agents "act as they would have precommitted to act," assign non-negative value to information, and are "so far as we know, reflectively stable in fair problems." The precommitment claim is easiest to check where the agent's choice at one observation is all that matters, as in the examples above. Section 8 shows why it needs qualification for A-FDT specifically.

## 8. What Equation (4) leaves open

**(a) Constructing $G$.** This is the paper's acknowledged central gap. Everything turns on which edges leave $F_x$.

My working criterion is to draw an edge into a process $Y$ when counterfactually varying the output of the A-FDT algorithm on input $x$ would vary $Y$. This covers $Y$ because $Y$ runs the same computation, simulates it, or reliably reasons about it. Correlation with a common upstream cause is not enough.

The criterion is a heuristic, not a derivation. Imperfect similarity remains genuinely indeterminate: a "twin" who runs a slightly different algorithm, or a predictor that reasons only coarsely. The paper's calculator analogy suggests modelling partial similarity as a dependence edge combined with a noise node, but it does not settle how strong the edge should be.

**(b) Priors on the non-intervened logical nodes.** In every example in the paper, the prior on sibling nodes ($q$ above) "won't matter." This is not true in general, and it is exactly where A-FDT can come apart from policy-FDT. The following example is my own construction.

*Coordination across observations.* A fair coin shows the agent L or R. Beforehand, a perfect predictor computed both $F_L$ and $F_R$ and set the prize:

- \$10 if both outputs are $a$;
- \$6 if both are $b$;
- \$0 if they differ.

The physical act is otherwise irrelevant.

Suppose the agent sees L, and her prior gives $F_R=a$ probability $r$. Then:

- $do(F_L=a)$ gives $10r$;
- $do(F_L=b)$ gives $6(1-r)$.

So A-FDT outputs $b$ whenever $r<0.375$. If she believes, accurately, that her R-self outputs $b$, then $(b,b)$ is a self-consistent fixed point worth \$6. Policy-FDT optimizes over the pair $(F_L,F_R)$ jointly and selects $(a,a)$, worth \$10.

In general, A-FDT outcomes with accurate self-priors are equilibria among the agent's observation-indexed "selves," while policy-FDT picks the globally best policy. When the equilibrium is unique, as in all the paper's examples, the two coincide. This plausibly explains footnote 16's remark that the difference matters only in special (there, "multi-agent") settings. Here the "agents" are the agent's own counterparts across observations.

Two operational remedies are available. Both are my proposals, not the paper's:

- *Symmetry edges.* If $F_L$ and $F_R$ are the same algorithm on inputs the agent judges decision-equivalent, draw a subjunctive edge between them. Intervening on one then moves the other.
- *Policy-FDT.* Adopt the authors' preferred formalism and intervene on a policy node.

Either way, A-FDT as literally given by Equation (4) requires the agent to supply sibling priors. A reasonable default is to set them to her best estimate of what A-FDT actually outputs on those inputs. This makes the result a self-consistent fixed point, but it does not guarantee an optimal one.

**(c) Ties and randomization.** The arg max may be a set. The paper says nothing about tie-breaking or mixed actions. With perfect predictors, randomizing over a decision that is itself predictable gains nothing in A-FDT hypotheticals. The paper notes that a *truly* random coin a predictor cannot foresee is valued correctly by A-FDT, at a 50% chance of escaping Death, whereas CDT undervalues it. I would treat genuinely unpredictable randomizers as exogenous nodes with no edge from $F$, and leave ties to an arbitrary fixed rule.

**(d) Counterpossibles.** $F_x$ has one actual value, so every other intervention is counter-logical. The paper concedes that a theory of counterpossible reasoning is missing. It argues the problem is "technical rather than philosophical," and that CDT faces the same issue in deterministic worlds, since a deterministic agent also has only one possible act. Equation (4) avoids the issue only by outsourcing it to $G$.

## 9. Conclusion

A-FDT is CDT with the intervention point moved. Instead of performing $do(\textsc{Act}=a)$ and conditioning on observations, the agent performs $do(F_x=a)$ on the logical node "the output of this algorithm on my actual input," and evaluates over the unconditioned model. Observations only choose which node to set.

Given a correct dependence graph, this single rule one-boxes in Newcomb's problem, smokes in the smoking lesion problem, cooperates with a twin, pays the driver in Parfit's hitchhiker problem, refuses both kinds of blackmail, and stays put in Damascus. In ordinary problems, where nothing else tracks the agent's decision function, it agrees with CDT and EDT.

Its weaknesses are equally clear. It cannot yet derive its dependence graph from evidence. It depends on priors over its own outputs on other inputs. In coordination problems across observations, those priors can trap it in a suboptimal equilibrium that policy-FDT avoids. A user applying A-FDT to a new case should therefore draw the subjunctive edges explicitly, state the sibling priors, and check whether the policy-level optimum agrees with the action-level choice.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
- Pearl, J. (2000). *Causality*. Cambridge University Press.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.