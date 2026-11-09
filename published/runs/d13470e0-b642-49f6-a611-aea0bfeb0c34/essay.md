# Policy Functional Decision Theory (P-FDT): Choosing the Function, Not the Act

## 1. The passage and the problem

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* develops functional decision theory mainly in an *action-selecting* form. Twice, though, it notes in passing that the authors prefer a different formulation. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source, is more specific about the mechanism:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node FDT(−) to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described in footnote 16 **policy functional decision theory (P-FDT)**. To keep it distinct, I will call the formulation that the paper actually writes down in its Equation (4) **action-level FDT (A-FDT)**. Other theories (CDT, EDT, and the precursors TDT and UDT) keep their usual names.

Footnote 16 is two sentences long. It tells us what is intervened on (a node written FDT(−)), what is chosen (a policy from inputs to actions), and how the act is obtained (apply the policy to one's inputs). It leaves several things unsaid:

- what exactly "the node FDT(−)" is;
- whether the observation is also conditioned on when policies are evaluated;
- which policies are admissible;
- how ties are broken;
- why the difference from A-FDT should appear only in multi-agent problems.

This essay gives a precise reconstruction of P-FDT, flags where I go beyond the text, and works through examples so that a reader can apply the theory to new cases.

## 2. Background: A-FDT as the paper writes it

All three theories in the paper (EDT, CDT, FDT) maximize expected utility. They differ in how they build the hypothetical for each option. EDT conditions on the act. CDT applies Pearl's $\mathtt{do}$ operator to the physical act node. A-FDT applies $\mathtt{do}$ to a node representing the *logical output of the agent's decision function* on her actual inputs.

The agent's world-model is a pair $(P, G)$. Here $P$ is a probability distribution and $G$ is a graph encoding causal *and* "subjunctive" dependencies, meaning which variables would change if a given mathematical function had a different output. The paper's Equation (4) is

$$
\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\!\left(V \,\middle|\, \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
\tag{A-FDT}
$$

Two features of this formula matter for what follows.

**First, observation selects a node rather than being conditioned on.** The paper says explicitly that "FDT responds to observation by changing which node it intervenes upon." When the observation history changes from $x$ to $y$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead of conditioning on $\textsc{Obs}=y$. Note that Equation (4) contains no conditioning on $\textsc{Obs}=x$.

**Second, outputs at other inputs remain uncertain.** In A-FDT, the function's outputs on *other* inputs are separate nodes, and the agent carries prior uncertainty about them. In the paper's transparent Newcomb analysis, $q$ is "Fiona's prior probability that she two-boxes upon seeing the box empty." The intervention fixes one coordinate of the agent's behaviour and leaves the others distributed according to $P$.

P-FDT changes exactly this second feature.

## 3. Defining P-FDT

### 3.1 The policy node

Let $\mathcal X$ be the set of inputs (observation histories) the decision function might receive in the problem, and $\mathcal A$ the action set. A **policy** is a map $\pi:\mathcal X\to\mathcal A$, and $\Pi=\mathcal A^{\mathcal X}$ is the set of policies.

*Interpretation (mine).* I read "the node FDT(−)" with the blank as an open argument slot. It is a single variable $\Phi := \textsc{fdt}(\underline P,\underline G,-)$ whose value is the whole input–output behaviour of the decision function: a policy, not an action. The per-input nodes of A-FDT, $\textsc{fdt}(\underline P,\underline G,\underline x)$, are then its coordinates, $\Phi(x)$.

In $G$, every system that "runs" or "models" the decision function on some input is a child of $\Phi$:

- the agent's own body: $\textsc{Act}=\Phi(\textsc{Obs})$;
- a predictor's simulation on input $x'$: $\textsc{Prediction}$ depends on $\Phi(x')$;
- a twin's or copy's action on its own input.

### 3.2 The decision rule

**Definition (P-FDT).** Given a world-model $(P,G)$ containing the policy node $\Phi$, and an observation $x$:

$$
\pi^\star \in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb E\big(V \,\big|\, \mathtt{do}(\Phi=\pi)\big),
\qquad
\text{P-FDT}(P,G,x) := \pi^\star(x).
\tag{P-FDT}
$$

The first step is the policy choice the footnote describes. The second is "to which the agent then applies her inputs in order to select an action."

Unlike A-FDT, the intervention sets *every* coordinate of the function's behaviour at once. Nothing about the agent's own behaviour on other inputs is left to a prior like $q$.

### 3.3 Interpretive choices

The footnote does not settle the following points. For each, I give my proposed reading and the reason for it.

**(i) No conditioning on $x$ during evaluation.** One could instead write $\mathbb E(V\mid \mathtt{do}(\Phi=\pi), \textsc{Obs}=x)$. I reject this reading for four reasons.

1. The footnote introduces the inputs only *after* the policy is chosen.
2. Equation (4) already omits conditioning on $x$, so P-FDT inherits that feature.
3. The paper's remark on Timeless Decision Theory warns that conditioning *and* changing the intervention point "creates a kind of 'double update' which proves harmful in practice."
4. Conditioning destroys the theory's signature verdicts. In transparent Newcomb, conditioning on "box B full" gives value $\$1{,}000{,}000$ to any policy that one-boxes on full and $\$1{,}001{,}000$ to any policy that two-boxes on full. The conditioned theory therefore two-boxes, like CDT and EDT.

(The paper's display for transparent Newcomb places "$\textsc{Obs}=\textit{full}$" inside the $\mathtt{do}$ expression, but the computation it then performs is the unconditioned expectation.) So P-FDT is *updateless* in the sense of Wei Dai's UDT: the observation affects *which coordinate of $\pi^\star$ is executed*, not the evaluation.

**(ii) Which $P$?** Because $x$ is not conditioned on, $P$ must describe the whole problem, including how observations are generated. A natural candidate is the agent's model at the point where the problem's structure is fixed but its inputs are not yet known. The source does not say how an agent who already holds an observation should recover such a model. In the paper's worked examples, the problem description supplies it. This is a real open question, and it is the policy-level version of the paper's own "largest open problem," which is how to obtain $G$ at all.

**(iii) Policy space.** I take $\Pi$ to be the deterministic maps on inputs that are possible in the problem. Mixed policies are worth adding only when some process in the environment responds to the *probabilities* the policy assigns, not just to its realized outputs. The footnote is silent on this, so I treat randomization as an optional extension.

**(iv) Ties.** Every instance of the function must arrive at the *same* $\pi^\star$, so ties must be broken by a fixed canonical rule, such as a fixed ordering of $\Pi$. I add this requirement myself. It is harmless in single-instance problems but matters when copies must coordinate (Section 5).

## 4. Applying P-FDT: worked examples

I use the paper's numbers throughout. Dollars stand in for utility, and predictor accuracy is 99% unless stated otherwise.

### 4.1 Newcomb's problem and the twin prisoner's dilemma

With no observation, $|\mathcal X|=1$, so a policy is just an action.

- **Newcomb's problem.** Under $\mathtt{do}(\Phi=\textit{onebox})$, the predictor's model, which depends on $\Phi$, predicts one-boxing with probability 0.99. The expected value is $0.99\times\$1{,}000{,}000=\$990{,}000$. Under $\mathtt{do}(\Phi=\textit{twobox})$ it is $0.01\times\$1{,}001{,}000+0.99\times\$1{,}000=\$11{,}000$. P-FDT one-boxes, just as A-FDT does.
- **Twin prisoner's dilemma.** Both twins receive the *same* input, so only one coordinate of $\Phi$ matters. P-FDT cooperates.

### 4.2 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Now there are two inputs, $\mathcal X=\{\textit{full},\textit{empty}\}$, and four policies. Following the paper's model, the predictor fills box B iff she predicts one-boxing-on-full, and she errs with probability 0.01:

| $\pi(\textit{full})$ | $\pi(\textit{empty})$ | $\mathbb E(V\mid\mathtt{do}(\Phi=\pi))$ |
|---|---|---|
| one | two | $0.99(10^6)+0.01(10^3)=990{,}010$ |
| one | one | $990{,}000$ |
| two | two | $0.01(1{,}001{,}000)+0.99(10^3)=11{,}000$ |
| two | one | $10{,}010$ |

So $\pi^\star=(\textit{one},\textit{two})$. An agent who sees two full boxes applies $\pi^\star$ and leaves the \$1,000 behind.

This matches the paper's A-FDT value $\$990{,}000+0.01q\cdot\$1{,}000$ at $q=1$. The difference is that P-FDT *derives* $q=1$ as part of the optimization, whereas A-FDT has to take it from the agent's prior.

Parfit's hitchhiker has the same structure. With death valued at $-\$1{,}000{,}000$:

- the paying policy is worth $0.99(-1{,}000)+0.01(-10^6)=-\$10{,}990$;
- the refusing policy is worth $0.99(-10^6)=-\$990{,}000$.

P-FDT pays.

### 4.3 Mechanical blackmail and its threshold

Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$.

- The policy "pay if blackmailed" is always blackmailed, so its value is $-\$1{,}000$.
- The policy "refuse" is blackmailed with probability $\varepsilon$ and then loses $\$10^6$, so its value is $-\varepsilon\cdot 10^6$.

P-FDT refuses iff $\varepsilon<10^{-3}$, that is, an error rate below 0.1%. At the paper's $\varepsilon=0.0009$, refusal costs \$900 in expectation and wins. The paper's claim that she pays at a slightly higher error rate is correct once the rate exceeds 0.1%.

The general lesson is that P-FDT's resistance to extortion is a quantitative tradeoff between the cost of complying and the risk of being targeted, not an absolute rule.

### 4.4 XOR blackmail

Let $p$ be the prior probability of termites, and assume an infallible predictor.

- **Policy "pay on letter."** The letter is sent iff there are no termites. The value is $-p\cdot 10^6-(1-p)\cdot 10^3$.
- **Policy "refuse."** The letter is sent iff there are termites. The value is $-p\cdot10^6$.

Refusing is better by $(1-p)\cdot\$1{,}000$. The intervention on $\Phi$ moves the probability of *receiving the letter* but never the probability of termites, because the infestation is not a descendant of $\Phi$. This is the same verdict as A-FDT and CDT, reached through a policy-level counterfactual.

### 4.5 Smoking lesion

The lesion is upstream of the agent's preferences and not downstream of $\Phi$. Intervening on $\Phi$ therefore leaves $P(\textit{lesion})$ unchanged. Smoking adds \$1,000 under every policy in which the agent's action is controlled by the function whose utility function rewards smoking. P-FDT smokes.

Policies add nothing in this case. Its interest is only that it confirms P-FDT inherits A-FDT's refusal to "manage the news" through mere correlations.

## 5. Where P-FDT and A-FDT come apart

### 5.1 A consistency proposition

The following proposition is my own. It makes footnote 16's claim that "the difference only matters in multi-agent dilemmas" more precise.

**Proposition.** Suppose the agent's prior concentrates the coordinates $\Phi(x')$, $x'\neq x$, on $\pi^\star(x')$, so that she correctly predicts her own behaviour elsewhere. Then $\pi^\star(x)$ maximizes the A-FDT objective at input $x$.

*Proof.* Under that prior, A-FDT's intervention $\mathtt{do}(\Phi(x)=a)$ is equivalent to $\mathtt{do}(\Phi=\pi^\star[x\mapsto a])$, where $\pi^\star[x\mapsto a]$ agrees with $\pi^\star$ except at $x$. Since $\pi^\star$ maximizes over all policies, it in particular beats every such single-coordinate deviation. $\square$

So every P-FDT policy is a self-consistent fixed point of A-FDT: a "Nash equilibrium" among the function's own instances at different inputs. The converse fails. A-FDT optimizes one coordinate at a time, holding the rest at their believed values, so it can settle on a *locally* optimal but *globally* worse fixed point. P-FDT optimizes all coordinates jointly.

The two theories therefore diverge exactly when three conditions hold:

1. the utility depends jointly on the function's outputs at *several distinct inputs* that all bear on the outcome;
2. there are multiple self-consistent fixed points;
3. the agent's prior points toward a bad one.

In transparent Newcomb, condition (1) fails in the relevant sense. The empty-box coordinate affects the outcome only additively and slightly, so A-FDT gets the right answer whatever $q$ is. That is presumably why the paper could set the distinction aside.

### 5.2 Example: labeled copies

Here is a minimal case of the multi-agent sort the footnote mentions. An agent is duplicated. One instance is placed in a room labeled R and the other in a room labeled B, so the two instances receive **different inputs**. Each chooses $a$ or $b$. Both instances (whose utility we treat as shared) receive:

- \$10 if both choose $a$;
- \$6 if both choose $b$;
- \$0 otherwise.

**A-FDT.** In room R, the agent intervenes on $\Phi(R)$. The B-instance's choice is the coordinate $\Phi(B)$, which keeps its prior. Suppose $P(\Phi(B)=b)=0.7$. Then $\mathbb E[a]=0.3\times10=3$ and $\mathbb E[b]=0.7\times 6=4.2$, so she picks $b$. The B-instance reasons symmetrically and also picks $b$. The pessimistic prior turns out to be correct, and the copies get \$6. With a uniform prior they would get \$10. A-FDT's verdict depends on the agent's self-prediction, a dependence the paper itself criticizes in EDT.

**P-FDT.** Compare the four policies. $(a,a)$ yields \$10 and dominates the rest, so both instances apply $\pi^\star$ and choose $a$, whatever the prior.

Two remarks:

- **Same input reduces to A-FDT.** Had the copies received *identical* inputs, as in the twin prisoner's dilemma, there would be one relevant coordinate and A-FDT would already coordinate.
- **Tie-breaking now matters.** Change the payoff so that $(a,b)$ and $(b,a)$ are both worth \$10. Then the two instances must break the tie the same way. This is why I require a canonical tie-breaking rule.

I add one hedge. The footnote says "so far as we can tell." The analysis above suggests the operative condition is structural (several instances at different inputs that interact non-separably) rather than literally about multiple agents. A single agent facing a predictor who rewards a *combination* of her behaviours on several inputs would satisfy the same condition. The source neither asserts nor denies this.

## 6. A recipe for unfamiliar cases

To apply P-FDT to a new decision problem:

1. **Inputs and actions.** List the inputs $\mathcal X$ the decision function could receive anywhere in the problem: in the agent's body, in predictors' models, in copies. List the actions $\mathcal A$.
2. **Dependence graph.** Build $G$. Every process whose behaviour is fixed by what the function outputs on some input, whether through literally running it, accurately modelling it, or being caused by an instance of it, becomes a descendant of $\Phi$ through the corresponding coordinate $\Phi(x')$. Processes that are merely correlated with the agent (lesions, coincidences) are *not* descendants of $\Phi$.
3. **Problem-level prior.** Specify $P$ over everything not downstream of $\Phi$, including how inputs are generated, without conditioning on the input actually received.
4. **Evaluate policies.** For each $\pi\in\Pi$, set every coordinate by $\mathtt{do}(\Phi=\pi)$, propagate along $G$, and compute $\mathbb E(V)$. In practice, the coordinates that affect nothing can be dropped.
5. **Choose and apply.** Take $\pi^\star$, breaking ties canonically, and perform $\pi^\star(x)$ for the input $x$ actually received.

Step 2 is the hard part. The paper is candid that "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." P-FDT inherits this problem unchanged and adds nothing to its solution.

## 7. Philosophical motivation and objections

### 7.1 Precommitment without commitment devices

The paper argues that the right decision theory should act "as they would have ideally precommitted to act." P-FDT makes this literal. $\pi^\star$ *is* the plan that is optimal before any inputs arrive, and the agent executes it with no external commitment device. A-FDT achieves the same result only when its self-predictions happen to match the optimal plan. The proposition in Section 5.1 shows that P-FDT never departs from such a matching plan and always selects the best one.

### 7.2 Value of information

The paper credits FDT with assigning non-negative value to information. P-FDT yields a simple argument for this, which I offer as my own, under one assumption: the world responds only to the function's input–output behaviour.

A finer partition of inputs enlarges $\Pi$, and every policy over the coarse partition is reproduced by a fine policy that is constant on the cells of the coarse partition. The maximum over a superset can only be at least as large. So under that assumption, extra observation never lowers P-FDT's ex ante value.

The assumption does real work. A predictor who punishes agents *for having seen something* falls outside it. That is one of the cases the paper would classify as unfair, since the outcome depends on more than the agent's behaviour.

### 7.3 The main objection: acting against what you see

The most natural complaint is that a P-FDT agent holding the blackmail letter, or staring at a full box, acts as though she had not seen it. The source's reply carries over directly. Observation is not discarded; it chooses *which coordinate of the policy is executed*. And the counterfactual "if I paid, I would probably never have been blackmailed" is no stranger than CDT's counterfactual, in which a known-perfect predictor fails exactly once. As the paper puts it, both kinds of hypothetical "contain impossibilities," and the question is which kind leads to better outcomes.

P-FDT does make the bullet visible. In the rare world where the predictor erred, the agent knowingly accepts a large loss, because the policy that accepts such losses is the policy that is rarely placed in that world.

### 7.4 Open questions

Several issues remain open, some from the source and some identified in my reconstruction:

- **Computational cost.** $|\Pi|=|\mathcal A|^{|\mathcal X|}$, so exhaustive policy search is intractable for realistic agents. Bounded P-FDT must approximate it, perhaps by searching only policies that differ from a default plan in a few coordinates.
- **Choice of $P$.** It is unclear how an agent who already has an observation should reconstruct the problem-level prior (Section 3.3(ii)).
- **Randomized policies.** Their role in environments that respond to probabilities, such as cases of imperfect recall, is unsettled.
- **Fairness.** Whether P-FDT does at least as well as any rival on "fair" problems inherits the paper's unresolved question of how to define fairness formally (footnote 15).

## 8. Conclusion

Read carefully, footnote 16 describes a theory that is clean to state:

- intervene on the node $\Phi=\textsc{fdt}(\underline P,\underline G,-)$, whose value is the decision function's whole input–output behaviour;
- choose the policy that maximizes $\mathbb E(V\mid\mathtt{do}(\Phi=\pi))$;
- apply it to one's actual input.

My reconstruction adds four choices: no conditioning on the observation during evaluation, a problem-level prior, deterministic policies by default, and canonical tie-breaking. Each is motivated by the source's own formulas and examples.

On every problem the paper analyses, P-FDT agrees with action-level FDT: one-boxing, smoking, paying the driver, and refusing both blackmails (within the stated thresholds). The difference lies elsewhere. P-FDT's choices are always self-consistent fixed points of A-FDT, and among those fixed points it selects the globally best one. The two come apart when instances of one function, receiving different inputs, must coordinate. That is plausibly the "multi-agent" class the footnote has in mind, though the analysis suggests the true dividing line is structural. The theory's reach is limited by the same thing that limits FDT in general: an adequate account of which processes subjunctively depend on the policy node.

**References**

Gibbard, A. & Harper, W. (1978). Counterfactuals and two kinds of expected utility.
Pearl, J. (2000). *Causality*. Cambridge University Press.
Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.