# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 1. The question A-FDT asks

Causal decision theory (CDT) evaluates an option by asking which physical act of mine would cause the best outcome. Evidential decision theory (EDT) asks which act would be the best news to learn I had taken. Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third question. Their agent treats her decision as the output of a fixed mathematical function, and that function asks, in their words, "Which output of this very function would yield the best outcome?"

This essay explains the formal version of that idea given in Equation (4) of Section 5 of the paper. In that version the agent intervenes on a node representing the output of her decision function *on her actual input*, and the values intervened on are *actions*. I call this formulation **A-FDT** (action functional decision theory). The paper itself just says "FDT". It also notes in footnotes 7 and 16 that the authors' preferred formalization intervenes on *policies*, which are maps from observations to actions. I keep that variant separate under the name *policy-FDT*. The two differ in some cases, and Section 7 gives an example.

Throughout, I mark which claims are the source's and which are my own reconstructions or proposals.

## 2. The common expected-utility frame

The paper places EDT, CDT, and A-FDT inside one schema adapted from Gibbard and Harper. Each recommends an action $a \in \mathcal A$ maximizing

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j), \tag{1}
$$

where $x$ is the observation history. The symbol $\hookrightarrow$ is a "decision hypothetical" connective whose interpretation is left open. Following Joyce, the paper holds that the theories do not disagree about value. They disagree about "the epistemic perspective from which actions are to be evaluated." Each theory is a recipe for building, from a world-model $M$, a hypothetical $M^{a\hookrightarrow}$ for each action and then scoring it.

Writing $V = \mathcal U(\textsc{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. Hypotheticals are built by conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$. Hypotheticals are built by Pearl-style surgery on the physical act node of a causal graph $G$.
- **A-FDT** (Eq. 4):

$$
\boxed{\;\mathrm{FDT}(P,G,x) \;=\; \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;} \tag{4}
$$

The underlines mark dequoting. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the *name of a variable* in the agent's own model. That variable stands for "whatever the A-FDT algorithm outputs when run on exactly these inputs." The model contains a representation of its own decision procedure. The paper argues this self-reference is harmless: the agent needs a variable that *represents* the output, not the output's value, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist.

## 3. Two structural differences from CDT

Compared with Equation (3), Equation (4) changes two things. The paper states both explicitly.

**(i) Where the surgery happens.** CDT intervenes on $\textsc{Act}$, which is a physical, token-level fact about the agent's body. A-FDT intervenes on a *logical*, type-level fact: the output of a function on an input. Any variable in $G$ downstream of that logical node changes in the hypothetical. This includes the agent's own physical act, but also a twin's act, a predictor's prediction, and anything else whose value is fixed by computing or modeling the same function. Everything not downstream keeps its prior distribution. The source summarizes the slogan as: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**(ii) What observation does.** In Equation (4), $x$ does not appear as a conditioning event. Observation changes *which node is intervened on*. Moving from history $x$ to history $y$ shifts the surgery from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The consequence of (ii) is easy to miss and does real work. In an A-FDT hypothetical, the agent may find that if her function had output something else, she would *not have received the observation she in fact received*. This is how A-FDT handles transparent Newcomb and blackmail.

## 4. Subjunctive dependence and the graph $G$

The source defines the relevant relation informally. Physical systems that compute the same function have behaviors that "subjunctively depend" on that function. Examples include two calculators computing $6288+1048$, an agent and a twin, or an agent and a predictor's accurate model of her.

The paper gives two contrasts:

- **Causal dependence is a special case.** A scribe copying a calculator's output would have written something different had the output differed.
- **Mere correlation is not subjunctive dependence.** Two calculators that happen to be pink are an example. So is the smoking lesion, which "is not evaluating the agent's future decisions."

The governing requirement, in the paper's words, is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The formal output of A-FDT depends entirely on $G$, which says which variables lie downstream of the logical node. The paper does not say how to build $G$: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." The intended ideal is a $\mathtt{true}(\phi)$ operator that updates beliefs as if a logical sentence held, even a false one. Such counterpossible reasoning is not defined. Equation (4) therefore takes the dependency structure as *given*, in the same way CDT takes the causal structure as given.

**Operational guideline (my proposal).** For practical use, an edge $\textsc{fdt}(\cdot,\cdot,\underline{x'}) \to Z$ belongs in $G$ when $Z$'s value is produced by a process that computes, simulates, or reliably models what the agent's decision function outputs on input $x'$. The model's inaccuracy is represented as a separate exogenous noise node, as with $\textsc{Accurate}$ in the paper's figures.

Correlations that arise only from shared *inputs*, such as preferences, a lesion, or a population base rate, do not create such an edge. This matches every example in the paper, but it is a heuristic, not a theorem.

## 5. A procedure for applying A-FDT

Collecting the source's examples into a recipe, here is how to decide a new case. Steps 2 and 4 involve modeling choices the source makes case by case rather than by rule.

1. **Outcomes and utility.** Specify $\textsc{Outcome}$ and $V$.
2. **Instances of the function.** List every input $x'$ on which the agent's decision function is computed or modeled anywhere in the scenario. This includes inputs the agent might *not* actually receive, such as "empty box" or "no letter". Create a node $\textsc{fdt}(\underline P,\underline G,\underline{x'})$ for each.
3. **Routing.** Make $\textsc{Act}$ a function of whichever of these nodes is "in control." The controlling node is determined by the variables that fix what the agent observes.
4. **Dependents.** Draw edges from each $\textsc{fdt}$ node to the predictors, twins, and other variables that model it. Add noise nodes for imperfect reliability.
5. **Priors.** Put priors on all exogenous nodes. This includes the *non-intervened* $\textsc{fdt}$ nodes, whose values matter when control is routed to them in the hypothetical.
6. **Evaluate.** For each $a$, set $\textsc{fdt}(\underline P,\underline G,\underline x)=a$ for the *actual* $x$, propagate downstream, and compute $\mathbb E[V]$. Do not separately condition on $\textsc{Obs}=x$. Output the argmax.

The worked examples below follow these steps.

## 6. Worked examples

### Newcomb's problem

A predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A holds \$1,000.

The single node $\textsc{fdt}(\underline P,\underline G)$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$. A noise node $\textsc{Accurate}$ (0.99) also feeds $\textsc{Prediction}$.

- $do(\textsc{fdt}=\textit{onebox})$: box B is full with probability 0.99, so $\mathbb E[V] = 0.99 \cdot 1{,}000{,}000 = \$990{,}000$.
- $do(\textsc{fdt}=\textit{twobox})$: $\mathbb E[V] = 0.01 \cdot 1{,}001{,}000 + 0.99 \cdot 1{,}000 = \$11{,}000$.

A-FDT one-boxes.

Retrocausation plays no part. The intervened variable is logical, and the prediction was produced by modeling that logical variable. CDT intervenes on $\textsc{Act}$, which is downstream of nothing the predictor sees, so it holds the box probability $p$ fixed. Two-boxing then wins by \$1,000 for every $p$.

The paper also notes a point about fixed priors. Even if the A-FDT agent is nearly certain she will one-box, this does not tempt her to two-box. Her hypothetical for two-boxing changes the logical node, and the prediction changes with it.

### Smoking lesion

Here the paper's modeling becomes subtle. The lesion causes both cancer and a taste for smoking. Formally, the agent is uncertain whether her utility function is $\mathcal U_S$ (values smoking at +\$1,000) or $\mathcal U_R$, and so uncertain which of two functions she runs: $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Lesion}$ routes control between them, and $\textsc{Lesion}$ causes $\textsc{Cancer}$. There is no edge from either $\textsc{fdt}$ node to $\textsc{Cancer}$.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Let $q$ be the prior probability that the other node, $\textsc{fdt}(\underline{P_R},\underline G)$, outputs *smoke*. Then the two hypotheticals differ by exactly $p \cdot \$1{,}000$, and the agent smokes.

The general lesson is that a correlation passing through *inputs* to the decision function (preferences, a lesion) is not routed through the logical node. Intervening on the logical node does not carry it.

### Transparent Newcomb

Both boxes are transparent. The predictor fills B iff it predicts the agent leaves A behind *upon seeing B full*. The agent sees B full.

Following the recipe, there are two logical nodes: $\textsc{fdt}(\ldots,\textit{full})$ feeds the prediction, and $\textsc{Prediction}$ routes control of $\textsc{Act}$ between the *full* node and the *empty* node. Let $q$ be the prior probability that the *empty* node outputs *twobox*.

- One-box: $0.99 \cdot 1{,}000{,}000 + 0.01 \cdot q \cdot 1{,}000 = 990{,}000 + 10q$.
- Two-box: $0.01 \cdot 1{,}001{,}000 + 0.99 \cdot q \cdot 1{,}000 = 10{,}010 + 990q$.

One-boxing wins for every $q \in [0,1]$.

*A note on the source.* The paper's displayed objective here writes "$do(\ldots=a), \textsc{Obs}=\textit{full}$", with an unbalanced parenthesis. But its calculation evaluates branches in which the box is empty, so it does *not* condition on $\textsc{Obs}=\textit{full}$. Had it conditioned, the result would be two-boxing. The calculation agrees with Equation (4) as stated, and I treat Equation (4) as authoritative. (The source's "\$110,00" is a typo for the \$10,010 above.)

Parfit's hitchhiker has the same structure. Paying in the city corresponds to one-boxing, so A-FDT pays.

### Blackmail

**XOR blackmail.** A perfect predictor sends a letter iff exactly one of these holds: (i) no termites and you would pay; (ii) termites and you would not pay. A-FDT intervenes on $\textsc{fdt}(\ldots,\textit{letter})$. This changes whether the letter is sent but not the infestation, which is upstream. Paying only buys a letter in the termite-free world, so A-FDT refuses.

EDT pays. Conditioning on paying pushes the probability of termites to 0, so the letter works as "good news" that can be manufactured.

**Mechanical blackmail.** A predictor runs a damaging program iff it predicts you would pay \$1,000 to stop it. Suppose the predictor wrongly predicts payment with probability $\varepsilon$.

- Refuse: you are blackmailed with probability $\varepsilon$ and lose \$1,000,000, for an expected loss of $\varepsilon \cdot 10^6$.
- Pay: you are always blackmailed and lose \$1,000.

The source reports that A-FDT refuses at $\varepsilon = 0.0009$ and pays at $\varepsilon = 0.0011$. The arithmetic gives a break-even point at $\varepsilon = 10^{-3}$. A-FDT can therefore refuse while holding a letter it knows came from a mistaken prediction. This is the sense in which it chooses "from a global perspective."

### Death in Damascus

Death predicts the agent perfectly, and fleeing costs \$1,000. Intervening on the logical node moves Death's appointment book along with the agent, so the only remaining difference is the \$1,000. A-FDT stays, without CDT's instability. The paper also argues that CDT, after settling into any belief state, would refuse to pay \$1 for a truly random coin offering a 50% chance of survival.

### When A-FDT, CDT, and EDT agree

The paper notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except for $\textsc{Act}$'s own dependence on the logical node, then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)].
$$

Divergence requires something in the world, such as a predictor, twin, or copy, that tracks the agent's decision function.

## 7. Questions the source leaves open

### (a) Action versus policy

Equation (4) intervenes on a single node, the one for the actual input. All other $\textsc{fdt}(\ldots,\underline{x'})$ nodes keep their priors. The paper's footnotes say the authors prefer intervening on a policy $\pi: \mathcal X \to \mathcal A$, which differs from A-FDT "in certain multi-agent dilemmas."

Here is an illustration of my own. Two copies of the agent run the same function. One observes *red*, the other *blue*. Each picks L or R. Both receive 10 if both choose L, 1 if both choose R, and 0 otherwise.

Suppose the agent's prior says $\textsc{fdt}(\ldots,\textit{blue}) = R$ with high probability. A-FDT at *red* then compares L, worth about 0, with R, worth about 1, and picks R. That prior is self-consistent, so the poor outcome (R, R) is a stable equilibrium.

Policy-FDT maximizes $\mathbb E[V \mid do(\textsc{fdt}=\pi)]$ jointly over the outputs on both inputs, so it selects (L, L).

The general point: the two nodes are separate variables, so A-FDT treats the function's outputs on *other* inputs as fixed background, not as things it controls. Whenever payoffs couple the function's behavior across inputs, A-FDT can settle into equilibria that policy-FDT avoids. In the transparent Newcomb and blackmail examples, the result happened to be robust to $q$, so the difference did not arise.

### (b) Priors over the non-intervened nodes

The source treats $q$ as arbitrary and notes its "correct" value (for example, $q=1$ in transparent Newcomb). It shows the answer is insensitive to $q$ there, but it gives no general rule.

My proposal: require *reflective consistency*. The prior on each $\textsc{fdt}(\ldots,\underline{x'})$ should equal what A-FDT actually outputs on $x'$, which makes the solution a fixed point. Solutions can be found by iterating: guess outputs on all inputs, recompute each node's argmax, and repeat. Example (a) shows that fixed points need not be unique. Choosing among them is effectively a step toward policy-FDT.

### (c) The surgery is counterpossible

The logical node has a single true value, so every other hypothetical is a logical impossibility. The paper calls this the main drawback of the theory relative to CDT. Its responses are:

- the difficulty is "technical rather than philosophical";
- deterministic CDT agents face the same issue, since they too must imagine acts that cannot occur;
- humans manage such reasoning heuristically.

It also notes that a variant which imagines *using a different function* does not avoid the problem. Predictors model the agent's actual function, so the variant would still need to imagine how that actual function behaves counterpossibly.

### (d) Ties, granularity, and fairness

**Ties.** Equation (4) is silent on breaking ties.

**Granularity.** It is also silent on how coarse a function counts as "the same." Does a predictor using a cruder model of my reasoning track my node? My guideline in Section 4 answers by reliability: a crude but reliable model counts, with its errors placed in the noise node.

**Fairness.** The paper's superiority claim is limited to "fair" problems, those where "the outcome depends only on the agent's behavior in the dilemma at hand." It admits that a problem which punishes whoever acts like a copy of the A-FDT agent defeats it, and that fairness has not been formalized.

## 8. The philosophical case

The source rests mainly on an **argument from utility**. Across the problems above, A-FDT agents end up richer than CDT agents, EDT agents, or both. Two further arguments are given teeth by this one:

- **Precommitment.** A-FDT acts as CDT and EDT agents would have *precommitted* to act, without needing a binding mechanism.
- **Value of information.** A-FDT does not, like EDT in transparent Newcomb, pay to avoid learning.

On dominance, the paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." CDT's dominance argument for two-boxing restates CDT's own counterfactuals and does not support them independently. Relative to subjunctive-dependence counterfactuals, A-FDT never chooses a dominated act.

The paper also claims that A-FDT is, as far as the authors know, reflectively stable in fair problems: an A-FDT agent holding a blackmail letter has no wish to self-modify into CDT. By contrast, CDT endorses switching away from itself for future problems.

The diagnosis in one sentence: EDT keeps too many correlations in its hypotheticals, CDT keeps too few, and A-FDT keeps exactly those that are subjunctive dependencies.

## 9. Conclusion

A-FDT, as given by Equation (4), is CDT with two changes. The point of surgery moves from the physical act to the logical output of the agent's own decision function on its actual input. Observation selects which logical node is intervened on, rather than being conditioned upon. Given a probability model and a graph of subjunctive dependencies, these changes yield a definite procedure. It one-boxes in Newcomb's problem, smokes in the smoking lesion, pays in Parfit's desert, refuses blackmail, and stays in Damascus.

The procedure depends on inputs the source does not supply:

- a theory of counterpossible dependence that would let $G$ be learned rather than stipulated;
- a principled treatment of priors over the function's outputs on other inputs, for which I proposed a fixed-point consistency condition;
- a resolution of the action-versus-policy gap, where my coordination example shows A-FDT can lock into inferior equilibria that policy-FDT escapes.

A reader with a model and a graph can apply A-FDT mechanically. Building the graph is where the open questions lie.

### References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.