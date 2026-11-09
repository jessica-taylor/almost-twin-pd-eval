# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 0. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a decision rule. In their words, the agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper's formal statement is Equation (4) of Section 5. That equation selects an **action** by intervening on a node that represents the output of the agent's decision procedure on the agent's actual inputs.

The authors also say, in footnotes 7 and 16, that their "preferred formalization" iterates over *policies* (maps from observations to actions) rather than actions. They set this aside "for ease of exposition." To keep the two apart, I call the Equation (4) theory **A-FDT** (action functional decision theory) and the footnoted variant **policy-FDT**. Where the paper writes "FDT" in its formal sections, it means A-FDT. Other theories appear under their own names:

- causal decision theory (CDT),
- evidential decision theory (EDT),
- Timeless Decision Theory (TDT),
- Updateless Decision Theory (UDT).

Throughout, I mark which claims come from the source and which are my own interpretation or proposal.

## 1. The common frame: three theories, one free parameter

**Source.** All three theories are expected-utility maximizers. The generic form (Equation 1) is

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $\hookrightarrow$ is the connective for "decision hypotheticals." Following Joyce (1999), the authors treat the interpretation of $\hookrightarrow$ as the only free parameter. Theories do not disagree about value; they disagree about "the epistemic perspective from which actions are to be evaluated."

Write $V := \mathcal U(\textsc{Outcome})$. The three rules are then:

$$
\textbf{EDT:}\quad \operatorname*{argmax}_{a}\ \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}
$$

$$
\textbf{CDT:}\quad \operatorname*{argmax}_{a}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}
$$

$$
\textbf{A-FDT:}\quad \mathrm{A\text{-}FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big) \tag{4}
$$

The paper describes each rule as a way of building a *hypothetical* $M^{a\hookrightarrow}$ from a world-model $M$. EDT builds it by conditioning. CDT builds it by Pearl-style surgery on the physical action node. A-FDT builds it by surgery on a *logical* node. Hypotheticals are "decision-theoretic instruments constructed from beliefs." They are scratch-paper objects, not possible worlds.

## 2. Anatomy of Equation (4)

Equation (4) has four ingredients.

**$P$.** A probability distribution over variables. For A-FDT these include variables standing for the outputs of mathematical functions. One of them is $\textsc{fdt}(\underline P,\underline G,\underline x)$, "the output of FDT when run on inputs" $P, G, x$. The underlines denote dequoting: the node's *name* is built from the model itself.

**$G$.** A graph saying "how changing a logical variable affects all other variables." For CDT, $G$ encodes causal structure. For A-FDT, $G$ must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly."

**$x$.** The observation history.

**$\mathtt{do}$.** Pearl's operator, reused. You set the node's value, recompute everything downstream of it in $G$, and leave everything else at its prior.

The self-reference is deliberate. The authors argue it is harmless: the agent needs a variable *representing* its output, not knowledge of that output's *value*, and Kleene's recursion theorem shows such self-representing structures exist.

**Source: two differences from CDT.**

1. *The intervention point.* CDT intervenes on the token (my physical act). A-FDT intervenes on the type (the output of the function my act implements).
2. *How observations are handled.* CDT conditions on $\textsc{Obs}=x$. A-FDT does not. It "responds to observation by changing which node it intervenes upon." Observing $y$ instead of $x$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is easy to overlook, and it drives A-FDT's distinctive verdicts.

**When the three rules agree.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the decision node itself. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories coincide. They come apart only when something other than the act's own effects tracks the act, as happens with predictors, twins, or copies.

## 3. Subjunctive dependence: what $G$ must encode

**Source.** The relation the graph must capture is *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The guiding slogan is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper's examples fix the boundary of this relation.

- **Two calculators computing $6288+1048$.** Their outputs depend on the same function. This holds even across the universe, where no common cause links them.
- **A scribe copying a calculator's output.** Causal dependence is a *special case* of subjunctive dependence: had the output differed, the scribe would have written something different.
- **Two calculators that happen to share a color.** This is mere correlation, not subjunctive dependence.
- **A predictor and a carcinogenic lesion.** A predictor "builds an accurate model of the agent and reasons about her behavior"; a lesion does not. So the predictor's prediction gets an edge from the $\textsc{fdt}$ node, and the lesion does not.

Because the intervened node is a logical fact, its alternative values are *counterpossible*. If the function actually outputs `onebox`, no possible world has it output `twobox`. The authors admit that the lack of a theory of counterpossibles is "the main drawback of FDT relative to CDT at this time." They sidestep it by requiring $G$ as an *input*, just as CDT takes a causal graph as input. They also note that the obvious workaround fails. That workaround is FDT′, which asks "what if I used a different function?" It fails because predictors of $d$ would still have to be imagined predicting as if $d$ behaved differently, which reintroduces the counterpossible.

## 4. Working through the canonical cases

Following the paper, all payoffs are in dollars-as-utility, and predictors are 99% accurate unless stated otherwise.

### 4.1 Newcomb's problem

Fiona's graph has an edge from $\textsc{fdt}(\underline P,\underline G)$ to both $\textsc{Act}$ and $\textsc{Prediction}$. A noise node $\textsc{Accurate}$ also feeds $\textsc{Prediction}$.

- Under $\mathtt{do}(\textsc{fdt}=\textit{onebox})$, box B is full with probability 0.99:
$$\mathbb E V = 0.99\cdot 10^6 = 990{,}000.$$
- Under $\mathtt{do}(\textsc{fdt}=\textit{twobox})$, box B is full with probability 0.01:
$$\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.$$

A-FDT one-boxes. The source gives these Fiona figures. Its EDT figure of "\$999,000" for one-boxing appears to be a typo; the same arithmetic gives \$990,000.

CDT gets a different answer. Its surgery on $\textsc{Act}$ leaves $P(\textit{full})=p$ untouched, so two-boxing wins by \$1,000 for every $p$.

**Source: no retrocausation.** Fiona does not believe her choice changes the past. "She just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

### 4.2 The psychological twin prisoner's dilemma

This case has the same structure as Newcomb's problem. The twin's choice is a child of the same $\textsc{fdt}$ node. Intervening on it yields:

- both cooperate: \$1,000,000;
- both defect: \$1,000.

A-FDT cooperates.

### 4.3 The smoking lesion

**Source.** The lesion changes the agent's *utility function*. To model this, the paper introduces two possible models, $P_S$ (which values smoking) and $P_R$ (which values it at −\$1). Correspondingly there are two decision nodes:

$$
\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r .
$$

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged, because there is no edge from the decision node to $\textsc{Lesion}$ or $\textsc{Cancer}$. Let $q$ be the agent's probability that the other node, $\textsc{fdt}(\underline{P_R},\underline G)$, outputs `smoke`. The two hypotheticals are:

- smoke: $\;p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q)$
- refrain: $\;p(10{,}000)+(1-p)(990{,}000+1{,}000q)$

Smoking is better by $p\cdot 1{,}000$, so A-FDT smokes.

The construction carries a lesson for applying the theory. Correctly modelling a case may require *several* $\textsc{fdt}$ nodes, only one of which the agent intervenes on. The others keep their priors.

### 4.4 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Here the observation does real work. Seeing a full box, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\textit{full})$. The prediction determines which observation-node controls $\textsc{Act}$. Let $q$ be the prior that $\textsc{fdt}(\ldots,\textit{empty})=\textit{twobox}$.

- **onebox:**
$$0.99\cdot 10^6 + 0.01\cdot 1{,}000q = 990{,}000+10q.$$
- **twobox:** with probability 0.99 the predictor foresaw two-boxing, the box is empty, and the *empty*-node acts; with probability 0.01 the box is full and the agent two-boxes. So
$$0.99\cdot 1{,}000q + 0.01\cdot 1{,}001{,}000 = 10{,}010+990q.$$

The source prints the second line as "\$110,00 + q·\$990," which I read as a typesetting slip for \$10,010 + 990q. Either way, one-boxing wins for every $q\in[0,1]$.

The striking feature is that the computation weights a world in which the agent sees an *empty* box, even though it has observed a full one. That is exactly what dropping the conditioning on $\textsc{Obs}=x$ means.

**Source.** The authors argue that one-boxing here "is precisely equivalent to paying the driver in Parfit's hitchhiker problem." They support it with arguments from precommitment, from the value of information, and from utility. They treat utility as primary.

### 4.5 XOR blackmail (the infallible-predictor version)

The authors say Fiona refuses and leave the arithmetic to the reader ("as you may verify"). Here it is. Let $p$ be the prior probability of termites. The letter is sent iff (no termites and the agent pays) or (termites and the agent refuses). The agent intervenes on $\textsc{fdt}(\ldots,\textit{letter})$, and the prior on the no-letter node is irrelevant because that node takes no costly action.

- **pay:** The letter arrives exactly when there are no termites. So $\mathbb E V = -p\cdot 10^6 - (1-p)\cdot 1{,}000$.
- **refuse:** The letter arrives exactly when there are termites. So $\mathbb E V = -p\cdot 10^6$.

Refusing is better by $(1-p)\cdot 1{,}000$. The intervention changes *whether the letter arrives*, never whether there are termites.

EDT pays, because conditioning on the letter and on paying sends $P(\textit{termites})$ to zero. CDT refuses, but its hypothetical treats an infallible predictor as having erred.

### 4.6 Mechanical blackmail with an imperfect predictor

Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$. Then:

- refusing costs $\varepsilon\cdot 10^6$ in expectation;
- paying costs \$1,000, since the agent is always blackmailed and always pays.

The indifference point is $\varepsilon = 0.1\%$.

**Source.** At $\varepsilon=0.0009$ the agent refuses, losing an expected \$900. The text then says that at "0.011%" the agent pays. By the paper's own arithmetic this should read 0.11%, above the 0.1% threshold. I flag it as a likely typo, not a substantive claim.

The broader point stands. A-FDT can refuse even while holding a letter it *knows* was sent in error, "because it's advantageous to be *the kind of agent* that makes such decisions."

### 4.7 Death in Damascus

Death's appointment book is a child of the $\textsc{fdt}$ node. Under either intervention Death is wherever the agent is, so the \$1,000,000 is lost in both hypotheticals. Staying in Damascus saves \$1,000, and A-FDT stays.

CDT behaves differently. Its hypotheticals keep breaking the correlation between its act and Death's location, so its deliberation oscillates. The paper argues that even when CDT settles, through Joyce's ratification, it refuses to pay \$1 for a truly random coin offering a 50% chance of survival.

## 5. An operational recipe for new cases

The paper never states a step-by-step procedure for building $(P,G)$ in a new problem. What follows is my reconstruction from its worked examples. Each step is labelled by how closely it tracks the source.

1. **Identify the decision-relevant computations** *(source-grounded).* List every process whose behavior is an accurate representation of your decision function: the predictor's model, a twin, Death's book, your future self facing an identical choice. Exclude processes merely correlated with your act, such as lesions, genes, or coincidences.

2. **Index decision nodes by input** *(source practice).* For each observation history $y$ you could have had in the problem, introduce $\textsc{fdt}(\underline P,\underline G,\underline y)$. Wire $\textsc{Act}$ so that the node matching the realized observation controls it. Where your preferences are uncertain, also index by model, as in $P_S$ and $P_R$.

3. **Draw subjunctive edges** *(source-grounded).* Add an edge from a decision node to every process that computes or predicts that node. Represent imperfect accuracy with independent noise parents, as the $\textsc{Accurate}$ node does.

4. **Intervene, do not condition** *(Equation 4).* For each $a$, apply $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ on the node matching your actual input. Propagate downstream, average $V$ under the prior over everything else, and choose the argmax.

5. **Set priors on non-intervened decision nodes consistently** *(my proposal).* The paper says these priors often "won't matter," and remarks that "the correct $q$ is 0 [or 1], as you may verify." I suggest requiring that these priors match what A-FDT would actually output at those inputs. This is a fixed-point condition, discussed in §6.3.

**A note on step 4.** In the transparent Newcomb discussion the source writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. Read literally, that might suggest conditioning on the observation. But the calculation actually performed gives weight to the empty-box branch, and Equation (4) contains no $\textsc{Obs}$ term. The paper also says (in a footnote on TDT) that conditioning on evidence *and* switching the intervention node creates a "double update which proves harmful in practice." I therefore take the operationally correct reading to be: **do not condition on $x$; let $x$ select the node.**

## 6. Open questions and how one might settle them

### 6.1 Where does $G$ come from?

**Source.** The authors write: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph." For CDT, Pearl's methods supply the causal graph from observation and experiment. A-FDT has no analogue.

In practice, step 1 of the recipe rests on judgments of the form "this process models my decision function." Those judgments are clear in stylized dilemmas and murky elsewhere.

### 6.2 Partial similarity

The paper's voting and gym examples involve agents that are *similar*, not identical. The FDT agent should assume she will keep going to the gym if she goes today "if there are no relevant differences." The source gives no rule for degrees of similarity.

**Operational proposal (mine).** Treat partial similarity like an imperfect predictor. Give the other process an edge from your $\textsc{fdt}$ node plus a noise parent, where the noise represents the chance that its reasoning diverges from yours. This keeps the $\mathtt{do}$-calculus intact and turns "how similar?" into an accuracy parameter. It does not answer the deeper question of *when* a different algorithm counts as computing the same function.

### 6.3 Where A-FDT and policy-FDT diverge

The source says the action/policy distinction "makes a difference in certain multi-agent dilemmas" but gives no example. Here is one of my own construction showing the structural gap.

A predictor examines the agent's outputs on two possible inputs $x$ and $y$, then shows the agent one of them at random. It pays \$10 if the agent outputs $L$ on both inputs, \$5 if $R$ on both, and nothing otherwise.

Seeing $x$, A-FDT intervenes only on $\textsc{fdt}(\ldots,x)$. It holds the $y$-node at its prior, $P(\textsc{fdt}(\ldots,y)=L)=q$. Then

$$
\mathbb E[V\mid \mathtt{do}(L)] = 10q, \qquad \mathbb E[V\mid \mathtt{do}(R)] = 5(1-q),
$$

so A-FDT chooses $L$ iff $q>1/3$.

Now impose my consistency requirement from step 5, by symmetry at both inputs. Both "always $L$" with $q=1$ and "always $R$" with $q=0$ are self-confirming. A-FDT therefore has a suboptimal fixed point, where it gets \$5. Policy-FDT avoids this because it intervenes jointly on the whole map and picks $(L,L)$ outright.

This mirrors the familiar gap between equilibrium and joint optimization. It explains why the authors prefer the policy formulation, and it shows that A-FDT's verdicts can depend on beliefs about one's own behavior at other inputs. In every example the paper works, those beliefs drop out of the comparison.

### 6.4 Fairness

**Source.** FDT is claimed to be superior "in all dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." The authors admit there is no formal definition of fairness. A copy of Fiona that punishes anyone who matches its action already shows the difficulty.

So the claim of optimality is conjectural. The authors themselves "do not yet know whether FDT is optimal."

### 6.5 Control and counterpossibles

**Source.** The authors answer the charge that FDT agents believe they "control" mathematical facts with a symmetry argument. A deterministic CDT agent likewise "controls" only one possible act token. Both theories use hypotheticals that are impossible in the actual world. On this view the difference is practical, not metaphysical.

## 7. Dominance, regret, and reflective stability

**Source.** The dominance argument for two-boxing presupposes CDT's hypotheticals. It holds the prediction fixed while varying the act, which is "akin to handing us a well-functioning calculator calculating 6288+1048 and asking us to imagine it outputting 3159."

The authors define an A-FDT analogue: $a$ dominates $b$ if switching the *algorithm's output* from $b$ to $a$, with subjunctive dependencies held fixed, is sometimes better and never worse. Under this definition A-FDT never picks a dominated act. The general moral is that "every method for constructing hypotheticals gives rise to its own notion of dominance," so dominance cannot neutrally adjudicate between theories.

The paper also claims that A-FDT is reflectively stable in fair problems. Holding a blackmail letter, Fiona would not self-modify to CDT, because an algorithm disposed to pay would be blackmailed more often. CDT, by contrast, recommends self-modifying away from CDT for future problems.

## 8. Conclusion

A-FDT is CDT with the surgery moved. Equation (4) intervenes on $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of one's own decision procedure on one's actual inputs, rather than on the physical act. It treats observations as selecting *which* node to intervene on rather than as evidence to condition on. Two consequences follow:

- Predictors, twins, and copies move together with the agent's choice inside its hypotheticals.
- Mere statistical correlates, such as lesions, stay fixed.

That is why A-FDT one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus.

Applying A-FDT to a new case comes down to building the right graph. You need decision nodes indexed by input, subjunctive edges to every process that computes or predicts them, and noise wherever that tracking is imperfect. Then you compare $\mathtt{do}$-interventions without conditioning on what you saw.

The theory's weak points are those its authors name. There is no account of how to learn $G$, no semantics for counterpossibles, and no formal notion of fairness. To these I add one gap the action formulation specifically creates: its dependence on beliefs about one's own outputs at other inputs, which can lock it into a suboptimal self-consistent policy that the policy formulation avoids.

## References

- Gibbard, A. & Harper, W. (1978). *Counterfactuals and Two Kinds of Expected Utility.*
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.* Cambridge UP.
- Nozick, R. (1969). *Newcomb's Problem and Two Principles of Choice.*
- Pearl, J. (2000). *Causality.* Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.