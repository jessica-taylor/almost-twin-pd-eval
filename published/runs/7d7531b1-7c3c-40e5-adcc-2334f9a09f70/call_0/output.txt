# A-FDT: Choosing the Output of a Function

## 1. The idea in one sentence

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should not ask "which physical act of mine causes the best outcome?" Instead, it should ask, in the paper's words, "Which output of this very function would yield the best outcome?" The agent treats its decision as the output of a fixed mathematical function. That function may be computed in more than one place: in the agent's brain, in a twin's brain, or in a predictor's model of the agent.

The paper calls its theory simply FDT. Its formal statement, Equation (4) in Section 5, chooses an **action**. Two footnotes (7 and 16) say the authors' preferred formalization chooses a **policy**, meaning a map from observations to actions. In this essay, **A-FDT** means the action-valued rule of Equation (4). I keep it separate from the policy-valued variant, which I call P-FDT where the contrast matters. When I quote the paper, its "FDT" refers to what I am calling A-FDT, unless the quotation concerns policies.

The essay covers five things in order: the formal rule, what its inputs must encode, worked cases, a procedure for unfamiliar problems, and the points where the source leaves the procedure underdetermined. Claims attributed to "the paper" come from the source. Material marked *(my proposal)* or *(my illustration)* is my own.

## 2. The common frame: expected utility with a free connective

The paper places A-FDT among expected-utility theories. All of them maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history and $P(a \hookrightarrow o_j; x)$ is "the probability that $o_j$ will obtain in the hypothetical scenario where the action $a$ is executed after receiving observations $x$". Following Joyce's representation theorem, the paper treats the interpretation of $\hookrightarrow$ as the free parameter that separates rival theories. Writing $V = \mathcal U(\textsc{Outcome})$:

- **EDT** conditions on the action:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a). \tag{2}$$
- **CDT** intervenes on the physical action in a causal model $(P,G)$, using Pearl's $\mathtt{do}$ operator:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x). \tag{3}$$

The paper reads each equation in three ways: as a constraint on hypotheticals, as advice for building hypotheticals from a world-model, and as an executable procedure. A **hypothetical** is a modified copy of the world-model that represents "what the world would look like if" the agent chose $a$. It is a computational tool, not a belief.

## 3. The A-FDT rule

### 3.1 Equation (4)

A-FDT keeps the surgical approach of CDT but moves the point of surgery:

$$
\text{A-FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\right). \tag{4}
$$

The ingredients are as follows.

- $P$ is a probability distribution over variables. For A-FDT it must include variables standing for the **outputs of mathematical functions**. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336".
- $G$ is a graph saying how changing such a logical variable affects the others. It extends a causal graph to "the logical, mathematical, computational, causal, etc. structure of the world more broadly."
- $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is the output of the A-FDT algorithm on exactly these inputs. Underlining means dequoting: the variable's *name* is built from the actual model and observation. I abbreviate this node as $F_x$.
- $\mathtt{do}(F_x = a)$ is Pearl's intervention. It sets $F_x=a$, cuts $F_x$ off from its parents, and recomputes every descendant of $F_x$ in $G$. Everything not downstream of $F_x$ keeps its prior distribution.

The self-reference is deliberate. The model contains a variable that represents the very computation using the model. The paper argues that this is harmless: the agent need only *represent* the value, not know it, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist.

### 3.2 Two differences from CDT

The paper itself identifies the two differences between (3) and (4).

1. **What is intervened on.** CDT intervenes on the token $\textsc{Act}$, the physical behaviour of the agent's body. A-FDT intervenes on the type $F_x$, the output of the decision function. Every physical system whose behaviour depends on that output then varies together in the hypothetical. This includes the agent's body, a twin running the same computation, and a predictor's simulation.

2. **How observations enter.** Equation (4) contains no $\textsc{Obs}=x$ conditioning. In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." After seeing $x$, the agent intervenes on $F_x$. After seeing $y$, it intervenes on $F_y$. As a result, A-FDT hypotheticals may contain worlds in which the agent *did not* observe $x$, for example because a predictor responded to $F_x$'s value by showing it something else.

### 3.3 Why "action"

The rule maximizes over $a \in \mathcal A$, a single action for the current input. The same function's outputs on *other* inputs, $F_y$ for $y\neq x$, are not set by the intervention. They stay at whatever prior distribution $P$ assigns them. Footnote 7 says that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions," and that this "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Section 7 below makes this difference concrete.

## 4. What $G$ must encode: subjunctive dependence

Everything in A-FDT depends on which arrows leave the $F_x$ node. The paper's organizing slogan is:

> *Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*

Two physical systems **subjunctively depend** on a function when both compute it. The paper uses calculators to build intuition:

- Two well-functioning calculators computing $6288+1048$ on opposite sides of the globe depend on the same arithmetic fact, even without any causal link between them.
- A scribe in Paris copying a calculator's output is both causally and subjunctively dependent on it. Causal dependence is "a special case of subjunctive dependence."
- Two calculators that happen to be pink are merely correlated. If one had been green, the other would still be pink.

Applied to decisions, a reliable predictor contains a "twin" of the agent's decision function, so its prediction subjunctively depends on $F_x$. A carcinogenic lesion that statistically correlates with an action "is not evaluating the agent's future decisions," so it does not.

The paper notes a useful consequence. If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the decision node, then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)],
$$

and EDT, CDT, and A-FDT all agree. They come apart only when something other than the agent's own action carries information about, or computes, the agent's choice.

## 5. Worked cases

All payoffs below are in dollars-as-utility, as in the paper.

### 5.1 Newcomb's problem

The predictor is 99% accurate. Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor predicted one-boxing.

In the agent's graph, $F$ has two children: $\textsc{Act}$, and $\textsc{Prediction}$, which also depends on an independent $\textsc{Accurate}$ node. Then:

$$
\begin{aligned}
\mathbb E[V\mid\mathtt{do}(F=\textit{onebox})] &= 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,\\
\mathbb E[V\mid\mathtt{do}(F=\textit{twobox})] &= 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT instead holds $P(\textit{full})=p$ fixed across its interventions, so two-boxing comes out \$1,000 better for every $p$.

The paper stresses that the A-FDT agent believes in no retrocausation. She simply declines to imagine her decision function's output changing while an accurate model of that same function stays fixed.

### 5.2 Smoking lesion

The lesion causes both a taste for smoking and, 99% of the time, cancer. The paper formalizes the taste as two possible utility functions, $\mathcal U_S$ for those who like smoking and $\mathcal U_R$ for those who do not. These give two possible decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The lesion determines which of the two controls $\textsc{Act}$.

Crucially, no arrow runs from either decision node to $\textsc{Cancer}$. Intervening therefore leaves $P(\textit{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, which is positive, and the agent's prior $q$ on the other node's output cancels out. A-FDT smokes, as CDT does and EDT does not.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

In this version both boxes are transparent. Box B is full iff the predictor predicted one-boxing *upon seeing it full*.

The graph contains $F_{\textit{full}}$ and $F_{\textit{empty}}$. $\textsc{Prediction}$ depends on $F_{\textit{full}}$, and $\textsc{Prediction}$ determines which of the two nodes drives $\textsc{Act}$. Seeing a full box, the agent intervenes on $F_{\textit{full}}$. Let $q$ be the prior probability that $F_{\textit{empty}}=\textit{twobox}$. Then:

$$
\begin{aligned}
\text{onebox:}&\quad 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000 + 10q,\\
\text{twobox:}&\quad 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.
\end{aligned}
$$

For every $q\in[0,1]$, one-boxing wins. (The extracted source prints the second line as "\$110,00 + q·\$990"; the constant should be \$10,010.)

A-FDT leaves \$1,000 on the table *while looking at a full box*. When it imagines two-boxing, it imagines a world in which it would probably have seen an empty box. The paper argues this is exactly isomorphic to paying the driver in Parfit's hitchhiker problem. It defends the verdict with three arguments:

- **Precommitment.** CDT and EDT agents would precommit to this behaviour if they could.
- **Value of information.** A-FDT never assigns negative value to information.
- **Utility.** "Parfit's desert is stacked high with the corpses of" agents disposed to defect.

### 5.4 Blackmail and a threshold

In the mechanical blackmail problem, the blackmailer launches a ruinous program (\$1,000,000 in damage) only if she predicts the agent will pay \$1,000 to stop it. On receiving the letter, A-FDT intervenes on $F_{\textit{blackmail}}$:

- $\mathtt{do}(F=\textit{pay})$: blackmail almost surely occurs, and the agent pays \$1,000.
- $\mathtt{do}(F=\textit{refuse})$: blackmail occurs only through predictor error, with probability $\varepsilon$, and then costs \$1,000,000.

So A-FDT refuses iff $10^6\varepsilon < 10^3$, that is, iff $\varepsilon < 10^{-3}$. This threshold is my derivation; the paper illustrates the switch with error rates on either side of it. Refusal is recommended even when the agent knows it is in an error case. In the paper's phrasing, this is "because it's advantageous to be *the kind of agent* that makes such decisions."

The XOR blackmail problem works similarly. Intervening on $F_{\textit{letter}}$ changes whether the letter is sent but not whether there are termites, so A-FDT refuses, as CDT does and EDT does not.

### 5.5 Death in Damascus

Death predicts the agent perfectly and waits wherever the agent will be. In the A-FDT graph, Death's appointment book depends on $F$. Both interventions therefore yield death, and staying in Damascus saves the \$1,000 cost of fleeing. A-FDT stays.

The paper contrasts this with CDT. CDT's hypotheticals hold Death's location fixed, which makes its deliberation unstable, and in a ratified state it even declines to pay \$1 for a genuinely random coin that would give a 50% chance of survival.

### 5.6 A note on dominance

Two-boxing "dominates" one-boxing only if counterfactuals are CDT's. The paper defines an A-FDT-relative notion: $a$ dominates $b$ if, holding subjunctive dependencies fixed, switching $F$ from $b$ to $a$ is never worse and sometimes better. In that sense A-FDT never picks a dominated act. The paper's conclusion is that dominance is not theory-neutral, because "every expected utility theory comes with its own notion of dominance."

## 6. Applying A-FDT to unfamiliar cases *(my proposal)*

The paper deliberately brackets how $G$ is obtained. To use the theory on new cases, I suggest the following procedure. It is consistent with every worked example in the source, but it goes beyond what the source states.

1. **Fix the input.** Identify the agent's current information $x$ and name the node $F_x$.

2. **Find the copies of $F_x$.** For each variable $X$, ask whether $X$ is produced by a process that evaluates the agent's decision function, or an accurate model of it, *on this same input*. Examples are the agent's body, a twin in the same informational state, a predictor simulating the agent at this choice point, or a later self facing an identical decision (the paper's gym example). If so, draw $F_x \to X$. Model imperfect reliability with independent noise parents, as $\textsc{Accurate}$ does in Newcomb's problem.

3. **Find the same function on other inputs.** If some process depends on what the agent *would* do after a different observation $y$, add a node $F_y$. Such processes include a predictor who conditions on a hypothetical observation and an environment that chooses which observation to show. Under A-FDT, $F_y$ is *not* intervened on and keeps its prior.

4. **Route mere correlations through common causes.** Lesions, genes, and population statistics become ancestors of $\textsc{Act}$, never descendants of $F_x$.

5. **Do not condition on $x$.** Let the intervention propagate to $\textsc{Obs}$, including to worlds where $x$ is not observed.

6. **Compute and maximize.** Evaluate $\mathbb E[V\mid \mathtt{do}(F_x=a)]$ for each $a$ and take the argmax. Then check whether the verdict is sensitive to the priors on $F_y$ nodes. If it is, treat it as fragile (see Section 7).

The test in step 2 is my operational reading of the calculator analogy. "Same function, same input" stands in for "same logical fact." The test is clear for exact copies and accurate predictors. It becomes vague for partial similarity, which is discussed below.

## 7. Where the source leaves A-FDT underdetermined

### 7.1 Constructing $G$

The paper is candid: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph," and it "rests on shakier philosophical foundations than" CDT. For causal graphs, Pearl offers a theory of how to learn them. For logical dependence there is no comparable theory, and every A-FDT verdict inherits whatever judgement produced $G$.

### 7.2 Counterpossibles

A deterministic function has only one output. Imagining a different output is therefore counterpossible: it supposes something logically false. The paper's ideal is a $\mathtt{true}$ operator, writing $\mathrm{FDT}^*(P,x)=\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a))$. It concedes that "it's not clear how to define" such an operator. Equation (4) sidesteps the problem by taking $G$ as given.

The paper also rejects a tempting alternative, FDT$'$, which would simulate *switching* to a different function. Predictors of the actual function $d$ would then have to be imagined as predicting "as if $d$ behaved like $f_n$," which brings the counterpossible back. The paper further argues that A-FDT is no worse off than deterministic CDT, which also imagines a single physically determined act being otherwise.

### 7.3 Conditioning on observations: an inconsistency in the source

Equation (4) omits $\textsc{Obs}=x$. However, the in-text formula for transparent Newcomb writes $\mathbb E(V\mid\mathtt{do}(\textsc{fdt}(\dots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. The paper's own numbers ($990{,}000+10q$ against $10{,}010+990q$) average over empty-box worlds, so they are computed *without* conditioning.

The difference matters. If one also conditioned on $\textit{full}$, the intervention $\mathtt{do}(F_{\textit{full}}=\textit{twobox})$ would be restricted to the predictor-error world. There two-boxing yields \$1,001,000 against \$1,000,000, so the verdict reverses. The paper's footnote on an earlier variant, Timeless Decision Theory, describes exactly this failure: "conditioning on evidence *and* changing the place where one intervenes ... creates a kind of 'double update' which proves harmful in practice."

My reading is that Equation (4) is authoritative and the in-text formula is a typographical slip.

### 7.4 Priors on sibling nodes: action versus policy

In the paper's examples, the prior $q$ on $F_y$ "doesn't matter." That is a feature of those examples, not of A-FDT in general.

*(My illustration.)* Consider two exact copies of an agent with the same $(P,G)$:

- One copy observes $L$, the other observes $R$, and each knows the other sees the other label.
- Each presses button 0 or 1.
- Both receive \$100 if both press 1, \$50 if both press 0, and nothing otherwise.

The $L$-copy intervenes on $F_L$ and holds $F_R$ at its prior, with $r=P(F_R=1)$. Then

$$
\mathbb E[V\mid\mathtt{do}(F_L=1)] = 100r,\qquad \mathbb E[V\mid\mathtt{do}(F_L=0)] = 50(1-r).
$$

So it presses 1 iff $r>1/3$. If both copies begin pessimistic about each other, both press 0. That is a self-confirming but inferior outcome. If their priors are asymmetric, they can miscoordinate entirely.

A policy-level rule fares better. It chooses $\pi:\{L,R\}\to\{0,1\}$ to maximize $\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\pi)]$, selects $\pi=(1,1)$ regardless of priors, and both copies compute it. This is presumably the kind of "multi-agent dilemma" the footnotes mean.

The practical lesson: **A-FDT verdicts are robust only when they are insensitive to the priors on $F_y$ for $y\neq x$.** Step 6 of my procedure checks for this.

### 7.5 Imperfect similarity, ties, and fairness

Three further gaps remain.

- **Partial similarity.** The paper handles noisy predictors through noise nodes. It says nothing about agents running *similar but different* functions, such as a near-twin with slightly different utilities. Whether such an agent gets an arrow from $F_x$, a weakened arrow, or none is left to $G$.
- **Ties.** Equation (4) specifies no tie-breaking rule. Where ties arise, as in the symmetric version of 7.4, some deterministic convention must be added.
- **Fairness.** The paper claims superiority only on "fair problems," where outcomes depend on the agent's behaviour rather than on its decision procedure as such. It admits that no formal criterion of fairness exists. Its footnote gives the example of a game that punishes anyone who matches a copy of the A-FDT agent; A-FDT loses that game by construction.

## 8. Conclusion

A-FDT is CDT with the point of intervention moved from the body to the algorithm. It chooses $a$ to maximize $\mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)]$, and it lets observations change *where* it intervenes rather than *what* it conditions on.

The resulting verdicts differ from the standard theories:

- It one-boxes in Newcomb's problem, where CDT does not.
- It smokes in the smoking lesion problem, where EDT does not.
- It pays the driver in Parfit's hitchhiker problem and resists blackmail, where neither CDT nor EDT does both.
- It never needs ratification or precommitment, because it already acts as it would have precommitted to act.

Its weaknesses are real, and the paper names most of them. Everything depends on a graph of subjunctive dependence that no one yet knows how to learn, and on counterpossible reasoning that no one yet knows how to formalize. The action-valued form adds a further gap of its own: by holding its other-input outputs at their priors, it can fail to coordinate with copies of itself, which is the gap the authors' preferred policy-level version is meant to close.

The workable guide for practice is the one the paper itself recommends. Ask what the whole world would look like if this very computation returned a different answer, change "all and only those things that subjunctively depend on" that answer, and choose the best such world.

## References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060v2. Primary source; Equation (4), §5.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.