# A-FDT: Action Functional Decision Theory, Equation by Equation

## 1. What this essay is about, and a note on names

Yudkowsky and Soares's "Functional Decision Theory: A New Theory of Instrumental Rationality" proposes a decision rule whose slogan is that an agent should treat her decision as the output of a fixed mathematical function and ask, in the paper's words, "Which output of this very function would yield the best outcome?"

The paper calls its theory *FDT*. Its formal centrepiece, Equation (4) in Section 5, intervenes on the output of the decision function **for one observation history at a time** and picks an **action**. The authors flag that this is not their preferred formulation:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." (footnote 7)

To keep the two apart, I call the theory of Equation (4) **A-FDT** (action functional decision theory). I call the policy-selecting variant from footnotes 7 and 16 **P-FDT**. When I quote the paper, its own label "FDT" is preserved. The paper's rivals are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Throughout, I mark which claims belong to the source and which are my own interpretation.

## 2. The common template: expected utility with a free "hypothetical" connective

All three theories share a single schema (the source's Equation 1). They choose an action $a$ from a finite set $\mathcal A$ to maximise

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where:

- $x$ is the observation history;
- $\mathcal U$ is a bounded utility function;
- $a\hookrightarrow o_j$ reads "if $a$ were done, $o_j$ would obtain."

Following Joyce, the paper treats the interpretation of "$\hookrightarrow$" as the *only* free parameter separating the theories. In Joyce's words, decision theories differ "about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each candidate action she builds a **hypothetical** $M^{a\hookrightarrow}$, which the paper describes as "decision-theoretic instruments constructed from beliefs," not beliefs. She then takes the action whose hypothetical has the highest expected value of $V := \mathcal U(\textsc{Outcome})$.

The two rivals construct hypotheticals as follows:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a) \tag{2}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x) \tag{3}
$$

- **EDT** conditions on the act, so it preserves every correlation between the act and the world.
- **CDT** uses Pearl's $\mathtt{do}$ operator on a causal graph $G$. It cuts the act node from its parents and propagates the change only downstream, so it preserves only correlations that the act causes.

## 3. The definition of A-FDT

The primary formal statement is the source's Equation (4), which I relabel:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\ } \tag{4}
$$

The ingredients are as follows.

1. **$P$** is a probability distribution over variables. These include ordinary physical variables (box contents, lesions, letters) and also *logical* variables representing the outputs of mathematical functions. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336."

2. **$G$** is a graph that, in the source's words, "tells us how changing a logical variable affects all other variables." It encodes **subjunctive dependence**, which is a broader relation than causation. I discuss it in §4.

3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node in the model representing *the output of the A-FDT procedure itself when run on these very inputs*. The underlines denote dequoting: the node's name is built from the model. The paper argues this self-reference is harmless. An agent "does not need to know the *value* … in order to have a variable … *representing* that value," and Kleene's recursion theorem ("quining") guarantees that such self-representing data structures exist. I abbreviate this node as $F_x$.

4. **$\mathtt{do}(F_x=a)$** is Pearl's surgery applied to the logical node. It sets $F_x=a$, recomputes everything downstream of $F_x$ in $G$, and leaves everything else at its prior distribution.

Read as an algorithm, A-FDT runs as follows:

1. Locate the node $F_x$ for the current inputs.
2. For each $a\in\mathcal A$, perform $\mathtt{do}(F_x=a)$ and compute $\mathbb E[V]$ in the resulting distribution.
3. Output the maximiser.

The source identifies two structural differences from CDT:

> "First, where CDT intervenes on a node $\textsc{Act}$ representing the physical action of the agent, FDT intervenes on a node … representing the outputs of its decision procedure given its inputs. Second, where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

The second difference is easy to miss and has striking consequences, which §6 develops.

**A note on the $\mathtt{true}$ operator.** The paper first states an idealised version, $\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a))$. Here $\mathtt{true}$ would update beliefs on a possibly false logical sentence, which is a *counterpossible*. Since no one knows how to define $\mathtt{true}$, Equation (4) replaces it with $\mathtt{do}$ on a supplied graph. The hard philosophical work is thereby pushed into $G$, exactly as CDT pushes it into its causal graph.

## 4. Subjunctive dependence: what goes into $G$

The source's guiding analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**When two systems depend subjunctively.** Two physical systems subjunctively depend on a function when both compute it. The model case is two well-functioning calculators computing $6288+1048$ on opposite sides of the globe. If (counterpossibly) the sum were different, both displays would differ. No signal passes between them.

**What counts and what does not.**

- *Causation is a special case.* A scribe copying a calculator's output depends on that output both causally and subjunctively.
- *Mere correlation is not enough.* Two calculators that happen to be pink do not depend subjunctively on each other's colour.

**The key asymmetry.** A predictor builds a model of the agent's decision function and reads off its output, so the prediction is a child of $F$. A carcinogenic lesion does no such thing, so it is not.

The paper insists the A-FDT agent imagines "corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**My working rule for building $G$.** This operationalisation is mine, not the source's. A variable $Z$ should receive an arrow from $F_x$ when $Z$'s value is computed, perhaps noisily, from an implementation or representation of *the same function on the same input* $x$. Examples include:

- the agent's own body when it receives $x$;
- a twin who receives $x$;
- a predictor simulating the agent in situation $x$.

Noise is modelled with separate exogenous parents, such as the source's $\textsc{Accurate}$ node. Everything else gets arrows only through ordinary causal paths.

The physical act $\textsc{Act}$ then becomes a *deterministic switch*. Its parents are all the $F_{x'}$ nodes plus whatever determines which observation the agent actually receives, and it copies the $F_{x'}$ for the realised observation $x'$. This is precisely the structure of the source's graphs for the transparent Newcomb and blackmail problems.

## 5. Worked examples without observations

In this section the agent's observation is fixed, so I drop $x$ and write $F$.

### Twin prisoner's dilemma

Both prisoners' acts are children of $F$, since they compute the same function on the same input.

- $\mathtt{do}(F=\textit{cooperate})$: both cooperate, so $\mathbb E[V]=\$1{,}000{,}000$.
- $\mathtt{do}(F=\textit{defect})$: both defect, so $\mathbb E[V]=\$1{,}000$.

A-FDT cooperates. CDT holds the twin's act fixed under its intervention, sees that defection dominates, and defects.

### Newcomb's problem (99% accurate predictor)

$F$ is the parent of both $\textsc{Act}$ and $\textsc{Prediction}$.

$$
\mathbb E[V\mid \mathtt{do}(F=\text{one})] = 0.99(1{,}000{,}000) = 990{,}000,
$$

$$
\mathbb E[V\mid \mathtt{do}(F=\text{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. The paper stresses that no retrocausation is assumed. The agent "does not think that a physical signal passes between her action and the predictor's prediction."

There is also an answer to the familiar worry: "if she is confident the box is full, why not grab both?" Her *hypothetical* for two-boxing is one in which the function outputs *two*. In that hypothetical, the predictor's model of the function outputs *two* as well, so the box is probably empty.

### Smoking lesion

The lesion fixes the agent's tastes, and therefore fixes *which* model, and hence which function instance, controls the act. The source formalises this with two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (values smoking at −\$1), and two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$:

$$
\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r .
$$

$\textsc{Cancer}$ is not a child of either node. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ therefore leaves $P(\textit{lesion})=p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000$, which is the probability that this instance controls the act times the value of smoking. A-FDT smokes.

This is the paper's headline claim: one rule both one-boxes and smokes. The difference between the cases lies entirely in $G$, not in the decision rule.

### Death in Damascus

Death's appointment book is computed from a perfect prediction of the agent, so the book is a child of $F$.

- $\mathtt{do}(F=\textit{stay})$: Death is in Damascus, so $V=0$.
- $\mathtt{do}(F=\textit{flee})$: Death is in Aleppo, so $V=-1{,}000$.

A-FDT stays, and its deliberation is stable. CDT oscillates (the Gibbard–Harper instability).

The paper adds a sharper point. Offer the agent a *truly* random coin for \$1, one that Death cannot predict. A-FDT values it at $0.5\times 1{,}000{,}000-1$ and buys it, since the coin's outcome is not a child of $F$. CDT, which already acts as if its survival chance is at least 50%, declines.

## 6. Observations: intervening instead of conditioning

Equation (4) contains no "$\textsc{Obs}=x$" in the conditioning bar. The observation appears only in the *name* of the intervened node. This is the formal content of the claim that A-FDT "responds to observation by changing which node it intervenes upon."

### Transparent Newcomb (seeing a full box)

There are two logical nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction is a child of $F_{\text{full}}$, because the predictor asks what the agent does upon seeing two full boxes. The prediction determines the box contents, and the box contents determine which of the two nodes drives the act.

Let $q$ be the prior probability that the agent two-boxes on seeing an empty box. Then:

$$
\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\text{one})] = 0.99(1{,}000{,}000) + 0.01\cdot q(1{,}000) = 990{,}000+10q,
$$

$$
\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\text{two})] = 0.01(1{,}001{,}000) + 0.99\cdot q(1{,}000) = 10{,}010+990q.
$$

(The extracted source prints the second figure as "\$110,00 + q·\$990"; the arithmetic gives \$10,010 + 990q.)

For every $q\in[0,1]$ one-boxing wins, so A-FDT leaves the \$1,000 even while looking at a full box. Notice that the computation weights worlds in which the box is *empty*. The expectation is taken over the prior, not over $P(\cdot\mid\text{full})$.

### Interpretive issue: should the expectation also condition on $x$?

In its transparent-Newcomb section the source writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$, with $\textsc{Obs}$ inside the parentheses. Yet its graph for that problem has no $\textsc{Obs}$ node, and its numbers (0.01 weight on the inaccurate branch, with $q$ entering via the empty-box world) are inconsistent with conditioning on "full."

If one *did* condition on $\textsc{Obs}=x$ after the intervention, the transparent Newcomb result would revert to two-boxing. The source's footnote warns against exactly this "double update," attributing it to Timeless Decision Theory, which "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

**My operational reading,** which agrees with Equation (4) as printed and with every worked number:

> $P$ is the agent's *prior* model of the whole decision problem, including branches in which she receives other observations. Given observation $x$, she intervenes on $F_x$ and takes the expectation of $V$ under $P$ with no further conditioning on $x$.

The observation still matters, because it selects *which* node is intervened on. The paper's phrase is that the agent should "entertain the hypothesis that, if their action were different, they might have *made different observations*."

### XOR blackmail

This is my own calculation of the case the source leaves as "you may verify." Let $p$ be the prior probability of termites. The letter is sent iff exactly one of these holds: (i) no termites and the agent pays; (ii) termites and the agent refuses.

- $\mathtt{do}(F_{\text{letter}}=\textit{pay})$: the letter arrives only in the termite-free world. Termites cost \$1,000,000 regardless. So $\mathbb E[V]=-(1-p)1{,}000-p\,1{,}000{,}000$.
- $\mathtt{do}(F_{\text{letter}}=\textit{refuse})$: the letter arrives only in the termite world. So $\mathbb E[V]=-p\,1{,}000{,}000$.

Refusing is better by $(1-p)\cdot\$1{,}000$. EDT pays, because conditioning on paying "makes" termites impossible.

### Mechanical blackmail

The blackmailer runs the program iff she predicts the agent would pay. Let $\varepsilon$ be the probability that she wrongly predicts payment.

- Paying: the agent is blackmailed essentially always and loses \$1,000.
- Refusing: the agent is blackmailed with probability $\varepsilon$ and then loses \$1,000,000.

A-FDT refuses iff $10^6\varepsilon<10^3$, that is, iff $\varepsilon<0.1\%$. The source's illustration at $\varepsilon=0.09\%$ (expected loss \$900, refuse) fits this threshold. Its second illustration says Fiona pays at "0.011%," which falls below the threshold. On my reading the switch to paying happens only above 0.1%, so "0.11%" seems intended.

### Parfit's hitchhiker

The structure is identical with the roles relabelled. The driver's choice is a child of $F_{\text{city}}$, so A-FDT pays upon arriving in the city.

## 7. Evaluating A-FDT's counterfactuals

Three features of A-FDT's counterfactuals deserve emphasis.

**(i) They break merely statistical correlations.** Unlike EDT, A-FDT is not hostage to the prior probability of its own act. Interventions are defined even on values with prior probability zero. So the cosmic-ray problem, Spohn's extreme priors, and news-management cases do not trap it.

**(ii) They preserve correlations that run through the function.** Unlike CDT, A-FDT never imagines a known-reliable predictor erring "exactly when [it] makes [its] current decision."

**(iii) A-FDT reduces to CDT and EDT in ordinary cases.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on $F$. Then the source shows that

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(F=a)],
$$

so all three theories agree. A-FDT's distinctive verdicts arise only where predictors, simulators, twins, or copies are present.

**Dominance.** The source argues that dominance is not theory-neutral: "Every expected utility theory comes with its own notion of dominance." Under A-FDT's notion, an action is dominated if switching the *function's output* is never better and sometimes worse while subjunctive dependencies are held fixed. A-FDT never takes a dominated action under that notion.

**Fairness.** The paper restricts its optimality claims to "fair problems," in which outcomes depend only on the agent's *behaviour* in the problem, not on how she reasons. It admits there is no formal definition yet (footnote 15).

## 8. What the source leaves open, and how I propose to handle it

### 8.1 Where does $G$ come from?

The source is candid: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) "works *given* a graph."

For unfamiliar cases, I suggest the working rule from §4 as a heuristic. Draw an arrow from $F_x$ to anything that runs, simulates, or reliably reasons about the same function on the same input $x$. Represent imperfection with independent noise nodes. Treat everything else causally.

This rule settles every case in the paper. It is silent on hard intermediate cases:

- a *similar but not identical* algorithm;
- a predictor using statistics about agents "like" you rather than modelling your function;
- an agent uncertain whether she is the one being simulated.

In such cases I would place a probability on "this system computes my function," via a latent mixture node. That is an extra assumption, not something the source supplies.

### 8.2 Counterpossibles

$F_x$ has a logically determined value. The $\mathtt{do}$ operation therefore models a counterpossible, and the source calls the lack of an account of counterpossibles "the main drawback of FDT relative to CDT at this time." It replies that the difficulty is "technical rather than philosophical," and that the agent need only answer narrow questions such as how "this predictor's prediction of my action [would] change." Equation (4) sidesteps the issue formally by treating $G$ as given input.

### 8.3 The other logical nodes, and the case for P-FDT

When A-FDT intervenes on $F_x$, the nodes $F_{x'}$ for other observations stay at their prior distributions. In the source's examples (the $q$ in the transparent Newcomb and lesion cases) this prior "doesn't matter." In general it can, and this is where A-FDT and P-FDT come apart.

The following example is mine, not the source's. A fair coin shows the agent observation $x$ or $y$. A reliable predictor pays according to the agent's dispositions in *both* branches:

| $(F_x, F_y)$ | $(L,L)$ | $(R,R)$ | mismatched |
|---|---|---|---|
| payoff | 10 | 6 | 0 |

Suppose the agent sees $x$ and her prior puts probability $r$ on $F_y=L$. Then

$$
\mathbb E[V\mid \mathtt{do}(F_x=L)]=10r,\qquad \mathbb E[V\mid \mathtt{do}(F_x=R)]=6(1-r).
$$

A-FDT chooses $R$ whenever $r<3/8$. If the agent's self-model is accurate, the profile $(R,R)$ is self-consistent: each branch's choice is optimal given the other's. Yet it is worse than $(L,L)$.

P-FDT instead maximises over whole maps $\pi:\mathcal X\to\mathcal A$:

$$
\pi^\ast=\arg\max_{\pi}\ \mathbb E\big[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big],\qquad \text{act}=\pi^\ast(x),
$$

and reaches $(L,L)$ directly.

So A-FDT is best understood as **coordinate-wise optimisation** of the policy. It is guaranteed to agree with P-FDT when the payoff-relevant structure makes the optimal choice at $x$ insensitive to the other nodes' values, as in every problem in the source. It can stall at an inferior "self-equilibrium" otherwise.

My recommendation for applying A-FDT as stated:

1. compute the verdict for every value of the other nodes' priors;
2. if it is invariant, report it;
3. if not, report the dependence explicitly, and note that P-FDT would resolve it.

### 8.4 Ties and approximation

Equation (4) is silent on ties, so a tie-breaking convention must be added. The paper also concedes that real world-models make exact maximisation intractable. It expects bounded approximations of the three theories to inherit their relative strengths and weaknesses.

## 9. A recipe for unfamiliar cases

1. **Model.** Write a prior $P$ over all variables, including every observation the agent might receive.
2. **Locate logical nodes.** Introduce $F_{x'}$ for each relevant observation $x'$. Make $\textsc{Act}$ a switch on the realised observation.
3. **Draw subjunctive arrows.** Connect $F_{x'}$ to every system that computes or reliably predicts that function on input $x'$. Connect nothing else except through ordinary causal paths.
4. **Intervene.** For the actual $x$ and each $a$, compute $\mathbb E[V\mid \mathtt{do}(F_x=a)]$ under the prior. Do not additionally condition on $x$.
5. **Robustness check** (my addition). Vary the priors on $F_{x'}$ for $x'\ne x$. If the verdict changes, flag the case as one where A-FDT and P-FDT may diverge.
6. **Act** on the maximiser.

## 10. Conclusion

A-FDT keeps the expected-utility core shared by CDT and EDT and changes only how hypotheticals are built. It intervenes, Pearl-style, on a logical node representing *the output of its own decision function on its current input*, and it lets observations select the node rather than condition the distribution.

This one change yields the paper's portfolio:

- one-boxing in Newcomb's problem;
- smoking in the lesion problem;
- cooperating with a twin;
- paying in Parfit's desert;
- resisting both XOR and mechanical blackmail;
- remaining stable against Death.

The open questions are real:

- the dependence graph $G$ is assumed, not derived;
- counterpossible reasoning is bracketed;
- the action-level form can, in my analysis, fall short of the policy-level P-FDT the authors themselves prefer.

As a precise procedure, however, Equation (4) is fully usable once a model and a dependence graph are on the table.

### References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality* (arXiv:1710.05060).
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*