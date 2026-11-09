# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Decision Function

## 1. What is being explained, and why "A-"

Yudkowsky and Soares (2017) propose a decision theory built around one question. In the abstract's words, the agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper calls this theory *functional decision theory*. Its primary formal statement, Equation (4) of Section 5, maximizes over **actions** drawn from a finite set $\mathcal A$. The authors flag that this is a simplification. Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Because I take Equation (4) as the definition, I call the theory **A-FDT (action functional decision theory)**. Quotations from the paper keep its original label "FDT". The policy-selecting variant that the authors prefer, but do not formalize there, I will call **P-FDT**. That label is mine, not the source's. The rivals are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Throughout, I mark which claims come from the source and which are my own interpretive proposals.

## 2. The common frame: expected utility with a free parameter

All three theories maximize something of the form (the paper's Equation 1)

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $a \hookrightarrow o_j$ is a "decision hypothetical": what would obtain if $a$ were done after observing $x$. Following Joyce (1999), the source treats the interpretation of $\hookrightarrow$ as the only real point of disagreement. The theories share a theory of value and differ in "the epistemic perspective from which actions are to be evaluated."

The paper makes this concrete with *hypotheticals*. The agent holds a world-model $M$. For each option she builds a modified object $M^{a\hookrightarrow}$ representing "how the world might look if she chooses $a$," scores it, and acts on the best score. The theories differ in what $M$ must contain and in how $M^{a\hookrightarrow}$ is constructed from it. Writing $V := \mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2) conditions on the act:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\,[V \mid \textsc{Obs}=x,\ \textsc{Act}=a].$$
- **CDT** (Eq. 3) performs Pearl's surgery on the physical act node of a causal graph $G$, and conditions on the observation:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\,[V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x].$$

## 3. The definition of A-FDT

**Equation (4)** (source):

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left[\,V \;\middle|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right]\;}
$$

Each piece has a specific meaning.

- **$P$** is a probability distribution. Unlike EDT's or CDT's, it contains variables for the *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on $7336$."
- **$G$** is a graph that, in the source's words, "tells us how changing a logical variable affects all other variables." CDT's $G$ encodes only causal structure. A-FDT's $G$ encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly."
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node of the model. It stands for the output of the A-FDT algorithm when run on the agent's own model and observations. The underlines indicate dequoting: the node's *name* is built from the inputs. The construction is self-referential. The source argues this is harmless, because the agent needs a variable *representing* her output, not knowledge of its *value*, and quining (Kleene's recursion theorem) shows such self-representations exist.
- **$do(\cdot)$** is Pearl's intervention, reused as a stand-in for a counterpossible "$\mathtt{true}$" operator that the authors say they cannot yet define. In the resulting hypothetical, everything downstream of the function's output in $G$ is updated, and everything else is held fixed.

The source identifies exactly two differences from CDT:

1. The intervention point is the *logical* node (the output of the decision function), not the *physical* node $\textsc{Act}$. In the paper's type/token phrasing, CDT intervenes on the token and A-FDT on the type.
2. "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." On observing $x$ the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline x)$; on observing $y$, on $\textsc{fdt}(\underline P,\underline G,\underline y)$. The observation appears in Equation (4) *only* inside the node name.

The slogan the source offers: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 4. Subjunctive dependence: what goes in $G$

The edges out of the function node encode **subjunctive dependence**: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The source draws three contrasts.

- **Two calculators computing the same sum** depend subjunctively on the sum, with or without a common cause.
- **Causal dependence is a special case.** A scribe copying a calculator's output would write something different if the output were different.
- **Mere correlation is not subjunctive dependence.** Two coincidentally pink calculators do not depend on each other's color.

Applied to decision problems, a predictor that "builds an accurate model of the agent and reasons about her behavior" depends subjunctively on the agent's decision function. A carcinogenic lesion does not. That asymmetry is the whole difference between Newcomb's problem and the smoking lesion problem under A-FDT.

Imperfection weakens the dependence without eliminating it. A predictor that is right 99% of the time is modeled with a noise node. The prediction is a function of the decision-function node and an independent $\textsc{Accurate}$ variable.

### An operational rule for building $G$ (my proposal)

The source does not give a procedure for constructing $G$. It calls "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment ... perhaps the largest open problem in the study of functional decision theory." For applying A-FDT to new cases, I suggest the following rule, which reproduces every graph in the paper:

> Draw an edge from a node $\textsc{fdt}(\underline P,\underline G,\underline y)$ to a variable $Y$ if and only if the mechanism producing $Y$ evaluates, models, or reliably tracks the output of the agent's decision function *on input $y$*. Model each source of unreliability as an independent exogenous noise parent.
>
> Then make the physical act a deterministic switch:
> $$\textsc{Act} = \textsc{fdt}(\underline P,\underline G,\underline y)\ \text{ where } y \text{ is the observation actually delivered.}$$
> Whatever determines which observation is delivered becomes a parent of $\textsc{Act}$.

The test is functional rather than causal. The question is not "did my choice cause $Y$?" but "would $Y$ differ if *this computation* returned a different value?"

## 5. The recipe

Combining Equation (4) with the source's worked examples gives a procedure. Steps 1, 3 and 5 follow the source. Steps 2 and 4 settle points the source leaves implicit; I discuss them in Section 7.

1. **Model the problem.** Write down the exogenous variables, outcomes, $V$, and, for each possible observation $y$, a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$.
2. **Assign priors to the nodes for observations not received.** Let $x$ be the observation actually received. Every node $F_y$ with $y \neq x$ needs a prior, the source's "$q$". I recommend setting these to what A-FDT would itself output on $y$.
3. **Intervene.** For each $a\in\mathcal A$, apply $do(F_x=a)$ and propagate through $G$.
4. **Do not condition on $\textsc{Obs}=x$.** Compute the unconditional expectation of $V$ in the surgically modified model.
5. **Choose.** Output the maximizing $a$.

## 6. Worked examples

Dollar amounts stand for utilities, and the predictor accuracy is 0.99 unless stated otherwise.

**Twin prisoner's dilemma.** A single node $F$ feeds both the agent's act and her twin's act. The two hypotheticals are:

- $do(F=\textit{cooperate})$: both cooperate, \$1,000,000.
- $do(F=\textit{defect})$: both defect, \$1,000.

A-FDT cooperates. CDT holds the twin's act fixed under surgery, so defection dominates and CDT defects.

**Newcomb's problem.** $F$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$, and the prediction is noisy.

$$
\begin{aligned}
\mathbb E[V\mid do(F=\textit{onebox})] &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(F=\textit{twobox})] &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. (The paper's EDT computation reports \$999,000 for one-boxing; the same arithmetic gives \$990,000, which is the figure the paper uses for the FDT agent.)

The source stresses that no retrocausation is involved. The hypothetical "$F=\textit{twobox}$" is a counterpossible world in which the algorithm itself behaves differently, so the predictor's model of it behaves differently too. The source also rejects CDT's dominance argument. It treats dominance as relative to a way of building hypotheticals: holding the subjunctive dependencies fixed, switching to two-boxing makes the agent worse off.

**Smoking lesion.** Here the lesion fixes which utility function, and so which world-model $P_S$ or $P_R$, the agent is running. The physical act is

$$
\textsc{Act} = \begin{cases}\textsc{fdt}(\underline{P_S},\underline G) & \text{if lesion},\\[2pt] \textsc{fdt}(\underline{P_R},\underline G) & \text{otherwise.}\end{cases}
$$

$\textsc{Cancer}$ has no edge from either function node. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ therefore leaves $P(\text{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes.

The lesson is that A-FDT does *not* respect every correlation between act and world. It respects only those that run through the function node.

**Transparent Newcomb problem.** This is the most instructive case. There are two function nodes, $F_{\text{full}}$ and $F_{\text{empty}}$:

- The predictor predicts $F_{\text{full}}$, with accuracy 0.99.
- Box B is full iff the prediction is "onebox".
- $\textsc{Act} = F_{\text{full}}$ if the box is full, and $F_{\text{empty}}$ otherwise.
- Let $q$ be the prior probability that $F_{\text{empty}}=\textit{twobox}$.

The agent sees a full box, so she intervenes on $F_{\text{full}}$:

$$
\begin{aligned}
do(F_{\text{full}}=\textit{onebox}):&\quad 0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000 + 10q,\\
do(F_{\text{full}}=\textit{twobox}):&\quad 0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010 + 990q.
\end{aligned}
$$

One-boxing wins for every $q\in[0,1]$. (The source prints the second line as "\$110,00 + $q\cdot$\$990", an evident typo for \$10,010 + \$990$q$.)

So even while looking at \$1,000,000 in box B, the A-FDT agent evaluates two-boxing by imagining a world where the box is probably empty. The source argues this is the same structure as paying the driver in Parfit's hitchhiker problem.

**Mechanical blackmail.** The blackmailer runs the incriminating program iff she predicts the agent would pay. Let $\varepsilon$ be her probability of wrongly predicting payment. The agent has received the letter and intervenes on $F_{\text{blackmail}}$:

$$
\mathbb E[V\mid do(F=\textit{pay})] \approx -1{,}000, \qquad \mathbb E[V\mid do(F=\textit{refuse})] = -10^{6}\,\varepsilon .
$$

A-FDT refuses iff $\varepsilon < 10^{-3}$. This matches the source's example: with $\varepsilon=0.0009$, the agent refuses even "even though she *knows* that the blackmailer predicted wrongly." The source also says that at "0.011%" she pays. That figure lies below the threshold, so it is presumably a typo for something like 1.1%. The threshold computed here is the reliable guide.

**XOR blackmail and Death in Damascus.** In the XOR blackmail, $\textsc{Infestation}$ is not downstream of $F_{\text{letter}}$. Paying changes whether the letter arrives but not whether there are termites, so A-FDT refuses.

In Death in Damascus, Death's appointment book is downstream of $F$:

- $do(F=\textit{aleppo})$ puts Death in Aleppo, at a cost of \$1,000 for the trip.
- $do(F=\textit{damascus})$ puts Death in Damascus, at no extra cost.

A-FDT stays, and stays stably. CDT's "unstable" deliberation never arises, because no hypothetical has a perfect predictor erring.

**Simple problems.** The source notes that when every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the act's own dependence on the function node,

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)],$$

and the three theories agree. Disagreement requires predictors, copies, or other replicators of the agent's computation.

## 7. Where the source leaves things open, and how I would settle them

**(a) Whether to condition on the observation.** As typeset, Equation (4) contains no conditioning on $\textsc{Obs}=x$. In the transparent Newcomb section, however, the paper writes the objective as "$\mathbb E(V \mid do(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$", with an unclosed parenthesis. Read literally, that conditions on what was seen.

The paper's own arithmetic does *not* condition: the 0.01 "inaccurate" branch, in which the box is empty, contributes to the totals. The choice matters. Conditioning on $\textsc{Obs}=\textit{full}$ inside $do(F_{\text{full}}=\textit{twobox})$ leaves only the inaccurate branch, which yields \$1,001,000 against \$1,000,000 for one-boxing, and the agent two-boxes.

I therefore read Equation (4) as written: no conditioning on the observation. This reading is supported by four things:

- the displayed definition;
- the explicit statement that observation acts by changing the intervention node;
- every numerical example in the paper;
- the remark (in an editorial note in the source) that Timeless Decision Theory, which both conditions and moves the intervention point, suffers a harmful "double update".

**(b) Priors on nodes for observations not received.** The paper leaves $q$ free and shows that it does not matter in its examples. In general it can matter. My proposal is to require *self-consistency*: set $P(F_y=b)$ to reflect what A-FDT would output when run on input $y$.

Such a consistent assignment is not obviously unique, which leads to the next point.

**(c) A-FDT versus P-FDT.** Under A-FDT, intervening on $F_x$ holds every $F_y$ with $y\neq x$ at its prior. If the environment rewards *coordination across inputs*, this can go wrong. Here is my illustration, consistent with but not taken from the source.

> Two exact copies of the agent receive different labels, "red" and "blue". Each chooses $A$ or $B$. Both receive \$10 if they match on $A$ and \$1 if they match on $B$, and nothing if they mismatch.

The red copy intervenes on $F_{\text{red}}$, holding $F_{\text{blue}}$ at its prior. If that prior puts most of its weight on $B$, choosing $B$ is A-FDT-optimal. The blue copy reasons the same way, so the inferior equilibrium is self-confirming.

P-FDT instead intervenes on the whole map $\pi:\mathcal X\to\mathcal A$:

$$\pi^\ast = \arg\max_\pi \mathbb E\,[V\mid do(\textsc{fdt}(\underline P,\underline G)=\pi)],\qquad \text{then act } \pi^\ast(x).$$

It picks "always $A$" directly. This is presumably the kind of "multi-agent dilemma" in which footnote 7 says the difference shows up. In the single-agent problems above, every relevant dependency runs through one input node, and the two variants agree.

**(d) Counterpossibles.** The function's output is a logical fact, so "$F=a$" is false of necessity for all but one $a$. The source openly admits it lacks a $\mathtt{true}$ operator for conditioning on such sentences. It substitutes $do$ on a supplied graph and calls the difficulty "technical rather than philosophical."

Practically, this means A-FDT is only as well-defined as the $G$ the agent is handed. Two analysts who disagree about whether some process "models" the agent will get different prescriptions. My rule from Section 4 narrows that disagreement but does not eliminate it.

**(e) Fairness.** The source claims that FDT does at least as well as its rivals in "fair problems": those where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." It concedes that this notion has not been formalized. Footnote 15 notes that a problem which punishes anyone matching a copy of the FDT agent defeats FDT, and that it is unclear how to construct the corresponding unfair problem for a rival theory.

## 8. Philosophical motivation (as the source presents it)

The paper's case for the theory rests on several arguments.

- **Utility.** FDT agents end up richer in Newcomb, the transparent Newcomb problem, Parfit's hitchhiker, and the blackmail problems, and it would be "great news to hear that a beloved daughter adheres to FDT." The authors treat this argument as the one that gives the others their force.
- **Precommitment.** CDT and EDT agents would pay to bind themselves to the FDT action. FDT "simply act[s] as they would have precommitted to act," with no binding device needed.
- **Value of information.** FDT agents never pay to avoid information. EDT agents, by contrast, would blindfold themselves in the transparent Newcomb problem.
- **Reflective stability.** An FDT agent holding the blackmail letter has no wish to switch to CDT. Doing so would make FDT the kind of algorithm that gets blackmailed.
- **Parity on "control".** A deterministic CDT agent can no more "really" vary its act token than an FDT agent can vary its function's output. Both theories evaluate imagined variations that do not occur, so the metaphysics of control does not favor CDT.
- **The diagnosis.** EDT's hypotheticals "respect too many correlations", which is why EDT pays in XOR blackmail and fears cosmic rays. CDT's respect "too few": it imagines perfect predictors failing exactly when it decides, which leads to instability in Death in Damascus and to refusing to pay \$1 for a coin that would give it a real 50% chance against Death. FDT keeps exactly the correlations that run through the agent's computation.

## 9. Conclusion

A-FDT, as given by Equation (4), is a CDT-shaped expected-utility rule with two changes. It intervenes on a logical node, the output of the agent's own decision function on her actual input, instead of the physical act. And it incorporates observations by choosing *which* such node to intervene on, not by conditioning.

Applying it requires three things:

1. a world-model containing nodes for the function's outputs;
2. a graph $G$ that marks which processes compute or predict those outputs, which is the theory's central open problem;
3. priors for the function's behavior on inputs not received.

With these in hand, the theory one-boxes, smokes, cooperates with twins, pays the driver, refuses blackmail below an error threshold that can be computed in each case, and stays put in Damascus. The open questions are how to construct $G$, how to give counterpossibles a principled semantics, and where the action-level A-FDT and the policy-level P-FDT come apart. They mark where the theory is still incomplete, not where it is incoherent.

---

**References**

Joyce, J. M. (1999). *The Foundations of Causal Decision Theory*. Cambridge University Press.
Pearl, J. (2000). *Causality*. Cambridge University Press.
Yudkowsky, E., & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.