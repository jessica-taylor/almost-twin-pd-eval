# A-FDT: Action Functional Decision Theory

## 1. The question A-FDT asks

Decision theorists have long disagreed about which hypothetical you should consult when you ask "what if I did $a$?" Evidential decision theory (EDT) conditions on your act and asks what would be good news. Causal decision theory (CDT) intervenes on your act and asks what that act would cause. Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third answer. In their words, the agent should treat "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains the specific formalization given as Equation (4), Section 5 of that paper. There the intervention selects an **action**: the output of the decision function on the agent's actual input. I call this version **A-FDT** (action functional decision theory). The label is my own. The paper calls Equation (4) simply "FDT."

The label separates Equation (4) from a variant that the paper mentions only in footnotes. In that variant the intervention selects a **policy**, a map from observations to actions. The authors write that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* … rather than actions," and that the difference "will not make a difference in this paper." I will call that variant policy-FDT. Section 7 shows that the two can come apart.

Throughout, I mark which claims come from the source and which are my own interpretation.

## 2. Setup: expected utility with a free connective

All three theories, the source says, maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and "$\hookrightarrow$" is the connective for decision hypotheticals. Following Joyce, the authors treat the theories as differing only in "the epistemic perspective from which actions are to be evaluated," which amounts to differing interpretations of $\hookrightarrow$. Write $V := \mathcal U(\textsc{Outcome})$. Then:

- **EDT:** $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT:** $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$, using Pearl's intervention on a causal graph $G$.

## 3. The A-FDT equation

A-FDT keeps CDT's surgical machinery but moves the point of surgery. The agent's world model is a pair $(P, G)$:

- $P$ is a probability distribution that includes variables for the outputs of mathematical functions. In particular it contains a variable $\textsc{fdt}(\underline P, \underline G, \underline x)$ standing for "what the A-FDT algorithm outputs when run on this very model and this observation." Underlining denotes dequoting.
- $G$ is a graph that "tells us how changing a logical variable affects all other variables." It encodes **subjunctive dependence** as well as ordinary causation.

Equation (4) then reads:

$$
\mathrm{A\text{-}FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).
$$

The source identifies two differences from CDT.

1. **Locus of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the output of the function. Every node that the graph makes depend on that output moves with it. These nodes include the agent's own act, a twin's act, and a predictor's prediction.
2. **Handling of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, "FDT responds to observation by changing which node it intervenes upon": a new observation $y$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead.

The self-reference, in which a model contains a variable naming the algorithm's output on that same model, is declared harmless. It is constructible by quining, via Kleene's recursion theorem. The agent needs only a variable *representing* the output, not knowledge of its value.

### What "subjunctive dependence" means

The source's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two physical systems computing the same function both subjunctively depend on that function, much as two calculators computing $6288+1048$ both output $7336$. Causal dependence is a special case. A scribe copying a calculator's display depends on its output in both senses.

Mere correlation is not dependence. Two calculators that happen to be pink are not linked. In graph terms:

- An agent's body, a twin, and an accurate predictor's prediction are children of the $\textsc{fdt}$ node.
- A carcinogenic lesion that statistically correlates with behavior is not.

### The counterpossible problem

If the function outputs $a_1$, then "it outputs $a_2$" is necessarily false. A-FDT therefore evaluates counterpossibles. The ideal tool would be a $\mathtt{true}(\varphi)$ operator, but "it's not clear how to define" one. The paper's workaround is to require that $G$ be supplied as input, just as CDT assumes a causal graph.

The source states this candidly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." For the user of A-FDT, this means **the theory is only as determinate as the graph you give it.** Most of the work in applying it to a new case is building $G$.

## 4. A practical recipe (my operationalization)

The source gives Equation (4) and worked examples but no general procedure. The following steps are my own reading of what the examples do.

1. **List decision-function nodes.** For each information state $x'$ in which some instance of your algorithm might find itself, create a node $F_{x'} := \textsc{fdt}(\underline P,\underline G,\underline{x'})$. "Instance" covers your own body, your copies, and simulations of you in others' heads.
2. **Wire dependencies.** Draw an arrow from $F_{x'}$ to anything whose value is computed from, or accurately predicts, your output in state $x'$. Draw no arrow to things that are merely correlated, such as lesions or genes. Ordinary causal arrows stay as in CDT.
3. **Route the physical act.** Your act $\textsc{Act}$ is a function of whichever $F_{x'}$ is "active," selected by upstream variables that determine what you will observe. The transparent Newcomb graph is the model: $\textsc{Prediction}$ decides whether $F_{\text{full}}$ or $F_{\text{empty}}$ drives $\textsc{Act}$.
4. **Assign priors to inactive nodes.** For $F_{x'}$ with $x'\neq x$, use your prior beliefs about how you would act there. The source calls these priors $q$.
5. **Intervene and compute.** For each $a$, apply $\mathtt{do}(F_x=a)$, propagate the change through $G$ without conditioning on $x$, compute $\mathbb E[V]$, and take the argmax.

Two features of Equation (4) need comment.

**The observation does not appear as a conditioning event.** In the transparent Newcomb calculation, the source writes $\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=a, \textsc{Obs}=\textit{full}))$, which seems to put the observation inside the intervention. The arithmetic the authors then do, however, averages over worlds where the box is empty. So I read Equation (4) literally: the observation enters only through the choice of node.

An unresolved subtlety follows. Should beliefs about variables that are *not* downstream of any decision node be updated on $x$? Examples would be facts learned incidentally, such as the weather. The paper's examples never test this. A cautious operational proposal, which is mine, is to condition on parts of $x$ that are independent of every $F$ node and to refrain from conditioning on parts that the $F$ nodes influence.

**The priors $q$ on other nodes are free parameters.** In the paper's examples the results are insensitive to $q$, and the authors note the "correct" values (for example $q=1$ for two-boxing on an empty box). In general, though, A-FDT's output can depend on $q$. That is precisely where the policy version differs (Section 7).

## 5. Worked examples

### Newcomb's problem

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction}$, with a predictor that is 99% accurate and payoffs as standard.

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(F=\text{one})] &= 0.99(1{,}000{,}000) = 990{,}000,\\
\mathbb E[V\mid \mathtt{do}(F=\text{two})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes.

The source answers a common objection: an agent confident that the box is full should still not two-box, because "for her to two-box, the FDT algorithm would have to output twobox". In that hypothetical the box is probably empty. No retrocausation is assumed. CDT holds $\textsc{Prediction}$ fixed under $\mathtt{do}(\textsc{Act})$ and two-boxes.

### Twin prisoner's dilemma

Both prisoners' acts are children of the same $F$. So $\mathtt{do}(F=C)$ yields $(C,C)$, worth \$1,000,000, and $\mathtt{do}(F=D)$ yields $(D,D)$, worth \$1,000. A-FDT cooperates.

### Smoking lesion

Here the graph lacks the arrow that Newcomb's has. $\textsc{Lesion}$ causes $\textsc{Cancer}$ and also influences which utility function, and hence which decision-function node ($F_S$ or $F_R$), controls the act. Intervening on $F_S$ does not touch $\textsc{Lesion}$. With $p=P(\text{lesion})$, the source computes that smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes.

The source's point is that one rule can both one-box and smoke. This contradicts Gibbard and Harper's suggestion that rational agents must either two-box and smoke or one-box and refrain. The difference between the two problems lies entirely in $G$: "the cancer is not evaluating the agent's future decisions."

### Transparent Newcomb and Parfit's hitchhiker

Box B is visibly full, so $x=\textit{full}$. In the graph, $F_{\text{full}}$ feeds the prediction, and the prediction selects which of $F_{\text{full}}$ or $F_{\text{empty}}$ drives the act. Let $q$ be the prior that $F_{\text{empty}}$ two-boxes. My computation is:

$$
\begin{aligned}
\text{one-box: } &0.99(1{,}000{,}000)+0.01\,q(1{,}000) = 990{,}000+10q,\\
\text{two-box: } &0.01(1{,}001{,}000)+0.99\,q(1{,}000) = 10{,}010+990q.
\end{aligned}
$$

(The paper's printed figure for the two-box line, "\$110,00 + q\$990," appears to be a typo for \$10,010 + 990q.) One-boxing wins for every $q\in[0,1]$.

So A-FDT leaves the \$1,000 even while looking at \$1,000,000. When it imagines two-boxing, it imagines a world in which it would have seen an empty box. The source notes this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." A-FDT pays, and survives because the driver predicts that it pays.

### XOR blackmail

The letter is sent iff exactly one of these holds: (no termites and the agent pays) or (termites and the agent refuses). In A-FDT's graph, $F_{\text{letter}}$ affects whether the letter is sent but not whether there are termites. A natural formalization (mine; the paper writes "as you may verify"):

- Under $\mathtt{do}(F_{\text{letter}}=\text{pay})$, the agent loses \$1,000 whenever there are no termites and loses \$1,000,000 whenever there are.
- Under $\mathtt{do}(F_{\text{letter}}=\text{refuse})$, the agent loses \$1,000,000 whenever there are termites and nothing otherwise.

Refusing therefore dominates by \$1,000 times the probability of no termites. A-FDT refuses. EDT pays, because conditional on paying, the letter means there are no termites.

A useful contrast from the source: A-FDT and CDT both refuse, but they report different counterfactuals. Asked "what if you had paid?", the A-FDT agent says "I would not have received the letter." The CDT agent says "the infallible predictor would have erred."

### Mechanical blackmail

The blackmailer runs the program iff she predicts the agent pays. Under $\mathtt{do}(F_{\text{blackmail}}=\text{pay})$, the agent is blackmailed and pays \$1,000. Under refuse, she is essentially never blackmailed. A-FDT refuses even while holding the letter.

The source adds a threshold. Suppose the blackmailer errs with probability $\epsilon$. Then refusing costs $\epsilon\cdot\$1{,}000{,}000$ in expectation and paying costs \$1,000.

- At $\epsilon = 0.0009$, refusing costs \$900, so A-FDT refuses.
- At $\epsilon = 0.0011$, refusing costs \$1,100, so it pays.

(The paper's text writes "0.011%"; the figure that makes the comparison work is 0.11%.) This shows that A-FDT is not a dogmatic "never pay" rule. It weighs what kind of agent is profitable to be.

### Death in Damascus

Death's appointment book depends on $F$. Under $\mathtt{do}(F=\text{Aleppo})$, Death is in Aleppo. Under $\mathtt{do}(F=\text{Damascus})$, Death is in Damascus. Death occurs either way, so A-FDT stays and saves the \$1,000.

There is no instability, because the hypotheticals never decorrelate the act from the prediction. CDT, by contrast, oscillates, or ratifies to a near-50/50 mixture and then declines a genuinely random coin worth a 50% chance of survival.

## 6. Why do this? The source's arguments

The authors give several reasons to prefer A-FDT.

- **Utility.** The paper's central claim is that A-FDT agents walk away richer. The authors treat this "argument from utility" as giving the other arguments "their teeth."
- **Precommitment.** CDT and EDT agents would pay to bind themselves to one-box in transparent Newcomb or to refuse blackmail. The authors argue that it should be rational to behave as one would have precommitted. A-FDT does so "on the fly," with no binding devices.
- **Reflective stability.** CDT recommends self-modifying away from CDT for future problems. A-FDT, the authors claim, does not want to switch to CDT even mid-blackmail. They describe it as "reflectively stable in fair problems."
- **Value of information.** EDT agents can expect information to hurt them, and would pay to blindfold themselves. The authors claim A-FDT agents never assign negative value to information.
- **Dominance is theory-relative.** The CDT dominance argument for two-boxing holds the prediction fixed, which already assumes CDT's hypotheticals. "Every expected utility theory comes with its own notion of dominance." Under A-FDT's own notion, holding subjunctive dependencies fixed, A-FDT never chooses dominated acts.
- **Fairness.** No theory wins every conceivable problem. A predictor can simply punish followers of a named theory. The authors restrict their claim to "fair" problems, in which "the outcome depends only on the agent's behavior in the dilemma at hand," and not on the procedure that produced it. Newcomb's predictor "punishes *two-boxers*," not FDT-haters. The authors admit that formalizing fairness is open. For instance, a game that punishes whoever matches a copy of Fiona is intuitively unfair to her.
- **Agreement in ordinary cases.** When every correlation between the act and the world is caused by the act, the three expectations coincide:
  $$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].$$
  A-FDT diverges only when predictors, twins, or copies are present.

On the charge of "controlling the past," the source answers with a parity argument. A deterministic CDT agent also imagines its fixed token act varying. Any principled objection to imagining a function's output varying applies equally to CDT.

## 7. Action versus policy: where A-FDT is underdetermined

This section is my own analysis.

Equation (4) intervenes on a single node $F_x$. All other nodes $F_{x'}$ keep their prior distribution. Policy-FDT instead chooses an entire map $\pi:\mathcal X\to\mathcal A$:

$$
\pi^*=\arg\max_\pi \mathbb E\big[V \mid \mathtt{do}(F_{x'}=\pi(x')\ \forall x')\big],\qquad \text{act } \pi^*(x).
$$

In every example in Section 5, the two coincide. The authors claim the difference matters only in "certain multi-agent dilemmas." A small example shows how it can matter.

**Example (asymmetric copies).** Two copies of the agent receive different observations: copy 1 sees $x=\text{red}$, copy 2 sees $x'=\text{blue}$. Each chooses $L$ or $R$. Each copy receives 1 if both choose $L$, 2 if both choose $R$, and 0 if they mismatch.

The best policy is $(\text{red}\mapsto R,\ \text{blue}\mapsto R)$, which yields 2. Now run A-FDT in copy 1, with prior $q=P(F_{\text{blue}}=R)$:

- choosing $R$ yields $2q$;
- choosing $L$ yields $1-q$.

Copy 1 chooses $R$ iff $q>1/3$. If the agent's prior says its blue-seeing self probably plays $L$, then A-FDT plays $L$. If both copies reason this way, they lock into the inferior equilibrium worth 1.

Equation (4) thus behaves like a best response to fixed beliefs about one's other instances, and it can inherit equilibrium-selection problems. Policy-FDT optimizes all instances jointly and avoids this.

The source does not tell us how to fix $q$, and A-FDT's verdicts can depend on it. Two reasonable operational answers:

1. Set $q$ by assuming that every instance of A-FDT runs this same calculation, and look for a self-consistent fixed point. This can have multiple solutions, as above.
2. Adopt policy-FDT whenever several decision nodes interact. The authors' footnote suggests they would favor this.

Either is an addition to Equation (4), not part of it.

## 8. Other open questions

- **Building $G$.** The theory has no analogue of Pearl's causal discovery for subjunctive dependence. When does an imperfect predictor or a "similar" agent count as instantiating your function? The paper's gym-going example treats this week's and next week's selves as instances of the same function "if there are no relevant differences." That condition does real work, and it is left informal.
- **Partial dependence.** The source handles noisy predictors through a separate accuracy variable, so dependence remains all-or-nothing at the function node with noise downstream. Whether a merely similar algorithm should get a weighted arrow is unspecified.
- **Bounded agents.** The calculations are idealized. The authors simply expect that approximations will inherit the same comparative strengths.

## 9. Conclusion

A-FDT is CDT with a relocated intervention. Instead of $\mathtt{do}(\textsc{Act}=a)$ conditioned on observations, it performs $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$. Observations select which logical node is intervened on, rather than being conditioned on. The resulting hypotheticals move everything that subjunctively depends on the agent's algorithm, including twins, predictors, and blackmailers' forecasts, and leave merely correlated variables like lesions alone.

On the source's account, this single rule one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker, refuses both kinds of blackmail, and stays home in Damascus.

The price is an input the theory cannot yet supply: a graph of logical dependencies, which amounts to a usable theory of counterpossibles. Two further gaps fall to the user. Equation (4) leaves the treatment of non-active decision nodes to priors, and it says little about how observations bear on variables outside the dependency structure. To apply A-FDT to a new case, do the modeling carefully: identify every instance of your function, wire only genuine dependencies, and note where policy-level reasoning would give a different answer.

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.