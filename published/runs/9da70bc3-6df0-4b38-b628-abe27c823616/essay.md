# Choosing the Function, Not the Act: An Essay on Policy Functional Decision Theory (P-FDT)

## 1. The footnote

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* builds its formal machinery around a decision rule that selects an **action**. Twice, however, the authors note that this is not quite the version they prefer. Footnote 7 says:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Footnote 16, which I take as the primary source for this essay, is more specific:

> "As mentioned earlier, the author's preferred formulation of FDT actually intervenes on the node $\mathrm{FDT}(-)$ to choose not an action but a *policy* which maps inputs to actions, to which the agent then applies her inputs in order to select an action. The difference only matters in multi-agent dilemmas so far as we can tell, so we have set that distinction aside in this paper for ease of exposition."

I will call the theory described here **policy functional decision theory (P-FDT)**. The version the paper actually formalizes in its equation (4) I will call **action-FDT (A-FDT)**. My aims are to:

- state P-FDT precisely enough that it can be applied to new cases;
- work through examples;
- identify where the footnote underdetermines the theory;
- show, with a concrete case, why the policy/action distinction matters.

I mark my own proposals as such throughout.

## 2. Background: action-FDT

Throughout the paper, an agent's world-model is a pair $(P, G)$:

- $P$ is a probability distribution over variables.
- $G$ is a graph saying how changes to some variables propagate to others.

FDT's distinctive move is that $P$ contains variables for the *outputs of mathematical functions*, including the agent's own decision procedure. The variable $\textsc{fdt}(\underline P, \underline G, \underline x)$ represents "what the FDT algorithm outputs when run on model $(P,G)$ and observation history $x$." The graph records which other variables depend on this output, such as a predictor's prediction, a twin's choice, or the agent's own physical act. Pearl's $\mathtt{do}$ operator is then reused, but applied to this logical node rather than to the physical act:

$$
\mathrm{FDT}(P,G,x) := \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{A-FDT}
$$

Two features of A-FDT matter for what follows.

1. **There is no conditioning on $x$.** In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."
2. **There is one logical node per observation.** In the transparent Newcomb problem, the graph contains separate nodes $\textsc{fdt}(\ldots,\textit{full})$ and $\textsc{fdt}(\ldots,\textit{empty})$. When the agent sees a full box she intervenes on the first. The second keeps whatever distribution $P$ assigns it, which the paper calls $q$, "Fiona's prior probability that she two-boxes upon seeing the box empty."

The second feature is where P-FDT departs from A-FDT.

## 3. Defining P-FDT

### 3.1 The policy node

Footnote 16 says P-FDT "intervenes on the node $\mathrm{FDT}(-)$." The dash in the argument slot suggests a node indexed by the model alone, whose value is the whole function from inputs to outputs. I adopt this reading.

**Policy space.** Let $\mathcal X_0\subseteq\mathcal X$ be the set of observation histories the agent could receive in the problem at hand. The policy space is
$$
\Pi := \mathcal A^{\mathcal X_0} = \{\pi : \mathcal X_0 \to \mathcal A\}.
$$

**Policy node.** The model $(P,G)$ contains a variable $\textsc{fdt}(\underline P,\underline G)$ taking values in $\Pi$. I will often abbreviate it as $\Phi$.

**Projections (my interpretive assumption).** Each per-observation node from the paper is a deterministic child of $\Phi$:
$$
\textsc{fdt}(\underline P,\underline G,\underline x) = \Phi(x).
$$
Everything that subjunctively depends on the agent's decision function depends on it through $\Phi$. A predictor that simulates the agent on input $x$ reads off $\Phi(x)$. A predictor that reasons about her whole disposition may read off all of $\Phi$.

### 3.2 The rule

The footnote describes two stages: choose a policy, then "apply her inputs." Formally:

$$
\pi^\ast \in \operatorname*{argmax}_{\pi\in\Pi}\ \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),
\qquad
\text{P-FDT}(P,G,x) := \pi^\ast(x). \tag{P-FDT}
$$

The argmax does not mention $x$. The policy is chosen from the standpoint of the model $(P,G)$, and the observation enters only at the last step, as an argument to $\pi^\ast$.

### 3.3 The procedure, step by step

To apply P-FDT to a new problem:

1. **List the inputs.** Enumerate the observation histories $\mathcal X_0$ the agent could face. Include inputs that are impossible given your actual observation, such as "box empty" when you can see the box is full.
2. **Build the graph.** Introduce the policy node $\Phi$. Draw an arrow from $\Phi$ to every variable that subjunctively depends on the agent's decision function: her own acts at each input (through $\Phi(x)$), predictors' predictions, copies' acts, and so on. Lesion-like correlates get no such arrow.
3. **Evaluate every policy.** For each $\pi\in\Pi$, set $\Phi=\pi$ by intervention, propagate downstream, and compute $\mathbb E[V]$. Note that $P$'s prior over $\Phi$ plays no role, because intervening on $\Phi$ overwrites it.
4. **Act.** Pick an optimal $\pi^\ast$, using a tie-breaking rule that depends only on $(P,G)$ (see §4.4), and output $\pi^\ast(x)$ for the observation you actually have.

## 4. What the footnote leaves open

Footnote 16 is two sentences long. Several choices must be made to turn it into an operational theory. For each, I give my reading and its justification.

### 4.1 Which node is intervened on

The text says "the node $\mathrm{FDT}(-)$." An alternative reading is that the agent still intervenes on her per-observation node $\textsc{fdt}(\underline P,\underline G,\underline x)$, but treats its value as a policy. That reading is odd: a node already indexed by $x$ has no use for a function of $x$. The policy-node reading in §3.1 is the natural one. It also explains why the authors expected the change to matter. The change is precisely that every input's output is varied *jointly*.

### 4.2 Whether to condition on the observation

Someone might write the objective as $\mathbb E(V\mid \mathtt{do}(\Phi=\pi), \textsc{Obs}=x)$. I reject this, for two reasons:

- The main text explicitly says FDT does not respond to observations by conditioning.
- The paper itself warns against the combination. It remarks that Timeless Decision Theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

§5 shows concretely that the conditioning variant reverses P-FDT's verdict in the transparent Newcomb problem.

### 4.3 Which $P$

On my reading, $P$ is the agent's model *before* the observations in $\mathcal X_0$. Within that model, observations are just variables that depend on the world and possibly on $\Phi$.

This matches the paper's notation, in which $(P,G)$ stays fixed while $x$ varies. If $P$ already had $x$ conditioned into it, then the input "box empty" would have probability zero. Evaluating policies on that input would then become meaningless, and the transparent Newcomb analysis would collapse.

One consequence is that P-FDT needs a notion of the "decision problem": a prior over a set of possible inputs. In everyday life, the boundary of the relevant $\mathcal X_0$ is a modelling choice the footnote does not address.

### 4.4 Ties

The argmax may contain several policies that disagree at some input. If several physical instances run the same function on different inputs, they must all apply *the same* $\pi^\ast$. Otherwise the joint optimization is lost.

**My proposal:** the tie-breaker must be a fixed function of $(P,G)$ alone, for example the lexicographically first optimal policy under a canonical encoding. Because it ignores $x$, every instance recovers the same $\pi^\ast$. This requirement has no analogue in A-FDT, and §6 shows it doing real work.

### 4.5 The size of the policy space

$|\Pi| = |\mathcal A|^{|\mathcal X_0|}$. The paper allows $\mathcal X$ to be countable, which would make $\Pi$ uncountable, and the supremum might not be attained.

Operationally, I restrict P-FDT to problems with finitely many relevant inputs. For larger problems, I would treat it as an ideal that bounded agents approximate. The paper takes the same attitude toward its idealized equations.

### 4.6 Randomized policies

The footnote speaks of maps "from inputs to actions." I read these as deterministic maps.

Allowing $\pi:\mathcal X_0\to\Delta(\mathcal A)$ raises a question that a problem statement must settle: do predictors respond to the distribution or to the sampled act? This interacts with the paper's Death in Damascus discussion of true versus pseudo-randomness. I leave it open.

### 4.7 Where $G$ comes from

P-FDT inherits FDT's deepest open problem. The source calls "deduc[ing] the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem in the study of functional decision theory." P-FDT changes the intervention target, not the requirement that the dependency graph be supplied as input.

## 5. Worked example: the transparent Newcomb problem

**Setup.** Both boxes are transparent. Box A contains \$1,000. The predictor, who is 99% accurate, fills box B with \$1,000,000 iff she predicts the agent will one-box upon seeing it full. The inputs are $\mathcal X_0=\{\textit{full},\textit{empty}\}$, so there are four policies. The fill decision depends on $\Phi(\textit{full})$ through the prediction. What the agent actually does depends on which input she receives.

**Evaluating each policy** (in dollars):

| $\pi(\textit{full})$ | $\pi(\textit{empty})$ | $\mathbb E[V\mid\mathtt{do}(\Phi=\pi)]$ |
|---|---|---|
| one | two | $0.99(10^6) + 0.01(1{,}000) = 990{,}010$ |
| one | one | $0.99(10^6) + 0.01(0) = 990{,}000$ |
| two | two | $0.99(1{,}000) + 0.01(1{,}001{,}000) = 11{,}000$ |
| two | one | $0.99(0) + 0.01(1{,}001{,}000) = 10{,}010$ |

**Verdict.** The optimum is $\pi^\ast = (\textit{full}\mapsto\text{one},\ \textit{empty}\mapsto\text{two})$. Seeing a full box, the agent applies her input and one-boxes. This agrees with the paper's A-FDT answer, $\$990{,}000 + 0.01q\cdot\$1{,}000$ with $q=1$. The difference is that P-FDT never needed a prior $q$. The behavior on the empty-box branch is *chosen*, not assumed.

**The conditioning variant from §4.2.** Condition on $\textsc{Obs}=\textit{full}$ after intervening:

- Under any policy with $\pi(\textit{full})=\text{two}$, the conditional world is one where the predictor erred and the box is full anyway. The value is \$1,001,000.
- Under $\pi(\textit{full})=\text{one}$, the value is \$1,000,000.

The conditioning variant therefore two-boxes. Predictors anticipate this, and the agent sees empty boxes 99% of the time. This is the "double update" in action, and it is why I read the footnote's "applies her inputs" as the *only* way observations enter.

**Mechanical blackmail.** The same method handles this case. Suppose the blackmailer errs toward "will pay" with probability $\varepsilon$. Then:

- The policy "pay if blackmailed" costs \$1,000 with certainty, because the agent is always blackmailed.
- The policy "refuse if blackmailed" costs $\varepsilon\cdot 10^6$ in expectation.

P-FDT refuses iff $\varepsilon < 0.001$. At $\varepsilon=0.0009$ refusal costs \$900, matching the paper's figure. The agent refuses even while holding a letter she knows was sent in error, because refusal is the better *policy*.

## 6. Where P-FDT and A-FDT come apart

The authors say the difference "only matters in multi-agent dilemmas so far as we can tell." I first give a general relationship between the two theories, then an example of the gap.

### 6.1 A general relationship (my formulation)

**Assumption.** All dependence on $\Phi$ runs through its components $\Phi(y)$. Write $(a,\pi_{-x})$ for the policy that outputs $a$ at $x$ and agrees with $\pi$ elsewhere.

**Proposition.** If the agent's prior puts probability 1 on $\Phi(y)=\pi^\ast(y)$ for all $y\neq x$, then A-FDT's objective at $x$ equals $\mathbb E[V\mid\mathtt{do}(\Phi=(a,\pi^\ast_{-x}))]$. Since $\pi^\ast$ is jointly optimal, this objective is maximized at $a=\pi^\ast(x)$.

**What this shows.** The P-FDT policy is always a self-consistent profile for A-FDT. Each input's output is a best response to the outputs at the other inputs.

**The converse fails.** A-FDT optimizes one coordinate at a time, holding the others at the agent's *prior* about herself. Its consistent profiles are therefore like Nash equilibria among the instances of her own function, and these can be suboptimal. P-FDT instead finds the global optimum over the whole product space.

In single-agent problems, only one input is ever executed, and the others matter only through predictions. In the paper's examples the off-path prior ($q$) turned out not to affect the verdict. When two inputs are *both* executed, by copies or by the same agent at different times, the joint structure becomes decisive.

### 6.2 An example: copies with different roles

**Setup.** Two physical copies run the same algorithm with the same model $(P,G)$. An announcer tells one copy "you are L" and the other "you are R." Each picks red or blue. Each copy receives:

- \$2M if both pick blue;
- \$1M if both pick red;
- nothing if they differ.

Suppose, perhaps because of past habits, the agent's model gives prior probability $r=0.9$ that her function outputs red on the other input.

**A-FDT.** The L-instance intervenes on $\textsc{fdt}(\ldots,L)$ and holds $\textsc{fdt}(\ldots,R)$ at its prior. Red is worth $0.9\times 1 = 0.9$; blue is worth $0.1\times 2=0.2$. She picks red, and by symmetry so does R. The prior is vindicated: both copies take \$1M. Red beats blue whenever $r>2/3$, so A-FDT's verdict here is hostage to the agent's beliefs about her own behavior. The paper criticizes EDT for exactly this kind of hostage relationship to priors.

**P-FDT.** The policies are evaluated jointly: (blue, blue) yields 2, (red, red) yields 1, and mixed policies yield 0. Both copies select $\pi^\ast=(\text{blue},\text{blue})$ and earn \$2M. The prior $r$ is irrelevant because the intervention overwrites it.

**A variant showing why ties matter.** Change the payoffs so the copies win \$1M iff they pick *different* colors.

- Under A-FDT with a 50/50 prior, each instance is exactly indifferent. Any input-independent tie-break, such as "pick the alphabetically first color," sends both copies to blue and they fail.
- Under P-FDT, two policies are optimal: (red, blue) and (blue, red). The rule in §4.4 picks one of them as a function of $(P,G)$ alone. Both copies compute the same $\pi^\ast$ and play its two different coordinates. They succeed.

**What this reveals about A-FDT.** A defender of A-FDT might reply that $\textsc{fdt}(\ldots,L)$ and $\textsc{fdt}(\ldots,R)$ are outputs of the *same* function, so a sufficiently rich $G$ should link them. But nothing in equation (4) says how intervening on one input's output should change another's. P-FDT answers by making the whole function the object of choice. This is, I think, the cleanest way to understand what the footnote is getting at.

The paper's closing examples of voting coalitions and coordinating with one's future self are natural further applications. When the instances face differing inputs, P-FDT chooses the coordinated *policy* rather than relying on each instance to guess what the others will do.

## 7. Philosophical motivation

Three themes from the paper bear especially directly on P-FDT.

**Acting as one would have precommitted.** The paper argues that "FDT agents always act as they would have precommitted to act." A precommitment is literally a policy: a rule fixed before observations arrive, specifying what to do on each input. P-FDT makes this argument structural rather than incidental. The agent at input $x$ executes the very rule she would have chosen to bind herself to, evaluated from the model that predates $x$. A-FDT only reproduces this behavior when its priors about off-path behavior happen to be right.

**Reflective stability.** The paper claims FDT does not wish to self-modify mid-problem, since an algorithm that "connived to pay up upon receiving blackmail" would be blackmailed more. Under P-FDT the claim is close to definitional, relative to a fixed $(P,G)$. Any rule she might self-modify into is itself a member of $\Pi$, already evaluated and found no better than $\pi^\ast$.

**The global perspective.** The paper describes FDT as asking "What would the entire universe look like if the FDT algorithm behaved differently?" P-FDT takes this literally. "The FDT algorithm behaving differently" means a different *function*, with different outputs on every input, not a different output on one input while the rest of the algorithm stays frozen.

**The counterpossible cost.** None of this removes FDT's reliance on counterpossible reasoning. If anything, P-FDT asks for more: the agent must imagine her decision function being any of $|\mathcal A|^{|\mathcal X_0|}$ different functions. But the paper's point that this difficulty is "technical rather than philosophical" applies equally.

## 8. Limitations and honest uncertainty

**How far the source goes.** It says the difference matters only in multi-agent dilemmas "so far as we can tell," and offers no example. The coordination example and the proposition in §6 are my reconstruction, not the authors'.

**The choice of prior.** P-FDT makes the prior model $(P,G)$ carry great weight. If an agent's prior over inputs is badly misspecified, she will faithfully execute a policy optimized for the wrong problem. The footnote is silent on when the "policy-selection standpoint" should be re-anchored as the agent learns. Re-anchoring after every observation would turn P-FDT back into something like the conditioning variant I rejected.

**Fairness.** P-FDT inherits the paper's open problem about what makes a dilemma fair. A problem that punishes whoever plays the same policy as a copy of a P-FDT agent defeats P-FDT, just as footnote 15's "act differently from Fiona" game defeats FDT.

## 9. Conclusion

As I reconstruct it from footnote 16, P-FDT is A-FDT with a single change of target. The agent intervenes on a node representing her entire decision function, a policy from inputs to actions. She chooses the policy with the highest expected utility in the resulting hypothetical, without conditioning on her observations, and then applies her actual input to it.

In the paper's single-agent examples (transparent Newcomb, blackmail) this gives the same verdicts as A-FDT, while removing the need for priors about one's own off-path behavior. It differs where several instances of the same function act on different inputs. There A-FDT can settle into a self-confirming but suboptimal profile, or fail through input-independent tie-breaking, while P-FDT selects the jointly optimal rule.

Making P-FDT operational requires decisions the footnote leaves open. I have argued for these:

- intervene on the whole function;
- do not condition on the observation;
- evaluate policies from the pre-observation model;
- break ties as a function of the model alone.

The question of randomized policies, and the open problem of where the dependency graph comes from, remain unresolved. Even so, the core idea is simple: deciding well means choosing *which function to be*.

### References

- Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (esp. footnotes 7 and 16, §§5–6, 9).
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Pearl, J. (2000). *Causality*.
- Dai, W. (2009). "Towards a New Decision Theory," *Less Wrong*.