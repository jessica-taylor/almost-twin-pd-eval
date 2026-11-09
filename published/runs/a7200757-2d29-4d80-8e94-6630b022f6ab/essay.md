# A-FDT: Choosing the Output of Your Own Decision Function

## 1. What is being chosen?

Every expected-utility theory answers the same question in the same form: pick the option whose *hypothetical* is best. The theories differ only in how the hypothetical is built. Yudkowsky and Soares, following Joyce, put it this way. Each theory maximizes

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

and each supplies its own reading of the connective "$\hookrightarrow$".

- **Evidential decision theory (EDT)** reads $a \hookrightarrow o$ as Bayesian conditioning.
- **Causal decision theory (CDT)** reads it as a causal intervention on the physical act.
- **Functional decision theory** reads it as an intervention on the *output of the agent's decision function*.

The paper states the core idea as follows: a rational agent treats her decision as the output of a fixed mathematical function that asks, "Which output of this very function would yield the best outcome?"

This essay concerns one precise version of that idea, the rule given as Equation (4) in Section 5 of the paper. I call it **A-FDT** (action functional decision theory). The "A" marks that the rule selects an *action* for the agent's current observation history. It does not select a whole observation-to-action map. The paper itself flags this distinction in a footnote: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I will call that other variant **policy-selecting FDT**. This label is mine, not the paper's.

Throughout, I separate three things:

- what the source claims;
- what follows from its equations;
- what I add as an operational interpretation.

## 2. The formal definition of A-FDT

### Ingredients

An A-FDT agent has three inputs.

- **A probability distribution $P$** over variables describing the world. Crucially, these include variables standing for the outputs of mathematical functions. One such variable might represent the value of $6288+1048$.
- **A graph $G$** that says how changing one variable propagates to others. In CDT the graph encodes causal structure only. In A-FDT the source says it must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly."
- **An observation history $x$.**

### The self-referential node

Among the variables in $P$ is one written $\textsc{fdt}(\underline P, \underline G, \underline x)$. It represents *what the A-FDT procedure outputs when run on exactly these inputs*. The underlines denote dequoting, so the variable's name depends on the model that contains it.

The authors argue that this self-reference is harmless. The agent needs a variable *representing* the output, not knowledge of its *value*. Kleene's recursion theorem ("quining") shows how such self-representing data structures can be built.

For brevity I write

$$F_x \;:=\; \textsc{fdt}(\underline P, \underline G, \underline x).$$

### Equation (4)

The paper's Equation (4), with the theory's name rendered as A-FDT, is:

$$\text{A-FDT}(P,G,x) \;:=\; \operatorname*{argmax}_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(F_x = a\big)\right),$$

where $V = \mathcal U(\textsc{Outcome})$ and $\mathtt{do}$ is Pearl's intervention operator. It is helpful to set this beside the paper's Equation (3) for CDT:

$$\text{CDT}(P,G,x) := \operatorname*{argmax}_{a}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}(\textsc{Act}=a),\, \textsc{Obs}=x\right).$$

### Two differences from CDT

The source identifies exactly two differences.

1. **Point of intervention.** CDT intervenes on the *token*: the physical act. A-FDT intervenes on the *type*: the logical fact about what this function outputs on this input. Every node downstream of $F_x$ in $G$ changes with it. That includes the agent's body, a twin's body, and a predictor's prediction.

2. **Handling of observations.** In the paper's words: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Notice that Equation (4) contains no "$\textsc{Obs}=x$" term. The observation enters only through the subscript of the node $F_x$.

### Subjunctive dependence

The guiding slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." Two systems *subjunctively depend* on a function when both compute it, like two calculators evaluating the same sum.

- Causal dependence is the special case where one system copies the other's output.
- Mere statistical correlation is not subjunctive dependence. The source's example is two calculators that happen to be pink.

### The $\mathtt{true}$ operator and why the paper sets it aside

Intervening on $F_x$ is a *counterpossible*. If the function actually outputs $a_1$, then "$F_x = a_2$" is a logical falsehood. The authors would ideally like an operator $\mathtt{true}(\varphi)$ that updates a distribution on a logical sentence. They concede, "it's not clear how to define a $\mathtt{true}$ operator."

Equation (4) avoids the problem by fiat. The dependence structure is *supplied* as $G$, in the same way that CDT is supplied a causal graph, and Pearl's $\mathtt{do}$ is reused on it.

## 3. A worked procedure

A reader who wants to apply A-FDT to a new case can follow the steps below. Steps 1–3 and 5–6 are directly licensed by the source's examples. Step 4 involves a choice the source leaves open, discussed in §5.

1. **List the information states.** Identify the observation histories the agent might be in, such as "box full" and "box empty", or "letter" and "no letter". Each gets a node $F_y$.

2. **Find every system that computes or models the agent's decision function.** Examples are the agent's own body, a twin, a predictor's simulation, or a driver's lie detector. Draw an edge from the relevant $F_y$ to each such system. The agent's physical act $\textsc{Act}$ is a child of *all* the $F_y$ nodes. Which one actually governs it depends on which observation is realized, and that may itself be downstream of predictions.

3. **Do not draw such edges for merely correlated processes.** Examples are lesions, genes, and coincidences. They connect to $\textsc{Act}$ only through ordinary causal or statistical structure, if at all.

4. **Assign priors.** Give probabilities to exogenous variables, such as predictor accuracy, lesion presence, or termites. Also give probabilities to the *non-intervened* nodes $F_y$ with $y\neq x$.

5. **For each action $a$**, compute $\mathbb E(V\mid \mathtt{do}(F_x=a))$ by setting $F_x$ and recomputing everything downstream. The prior on $F_x$ itself is irrelevant, because $\mathtt{do}$ overwrites it.

6. **Take the argmax.**

The rest of the essay runs this procedure on the paper's cases, then examines the places where it is underdetermined.

## 4. Examples

### Newcomb's problem (no observation)

A 99%-accurate predictor puts \$1,000,000 in opaque box B iff she predicts one-boxing. Box A holds \$1,000.

In the graph, $F$ has two children: $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Prediction}$ also depends on a noise node with $P(\textit{accurate})=0.99$.

$$\mathbb E(V\mid\mathtt{do}(F=\textit{onebox})) = 0.99\cdot 10^6 = 990{,}000,$$
$$\mathbb E(V\mid\mathtt{do}(F=\textit{twobox})) = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.$$

A-FDT one-boxes. (The paper reports Eve's EDT value for one-boxing as \$999,000. The arithmetic gives \$990,000, and the conclusion is unaffected.)

CDT's graph instead routes the prediction through a $\textsc{Predisposition}$ node. Its intervention on $\textsc{Act}$ leaves that node fixed. So two-boxing wins by \$1,000 whatever $P(\textit{full})$ is.

The difference is not retrocausation. In the source's words, the A-FDT agent "does not think that a physical signal passes between her action and the predictor's prediction." She simply refuses to imagine her output changing while a competent model of that same output stays fixed.

### The twin prisoner's dilemma

Here $F$ is a parent of both prisoners' acts. Under $\mathtt{do}(F=\textit{cooperate})$, both cooperate and each gets \$1,000,000. Under $\mathtt{do}(F=\textit{defect})$, both defect and each gets \$1,000. A-FDT cooperates.

### Smoking lesion

The lesion causes both a taste for smoking and cancer. Smoking does not cause cancer. The source formalizes the problem with two possible utility functions: $\mathcal U_S$ (lesion, likes smoking) and $\mathcal U_R$. This yields two decision nodes, $F_S := \textsc{fdt}(\underline{P_S},\underline G)$ and $F_R$. The act is governed by

$$\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r.$$

There is no edge from either $F$ node to $\textsc{Cancer}$. So intervening on $F_S$ leaves $P(\textit{lesion})=p$ unchanged. The only difference between the hypotheticals is the \$1,000 smoking bonus, which arrives in the $p$-fraction of worlds where $F_S$ actually controls the act. Smoking wins by $p\cdot\$1{,}000$.

So the same rule that one-boxes also smokes. That combination is exactly what Gibbard and Harper had argued no consistent rule could deliver. All the work is done by the *graph*: predictors get edges from $F$, lesions do not.

### Transparent Newcomb: updatelessness in action

Both boxes are transparent. The predictor fills B iff she predicts the agent would one-box *on seeing B full*. The agent sees B full.

There are now two decision nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. $\textsc{Prediction}$ is a child of $F_{\text{full}}$. The prediction determines which observation occurs, and hence which $F$ node drives $\textsc{Act}$.

Let $q$ be the prior probability that $F_{\text{empty}}=\textit{twobox}$. Then:

$$\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=\textit{onebox})) = 0.99\cdot 10^6 + 0.01\cdot q\cdot 1{,}000,$$
$$\mathbb E(V\mid \mathtt{do}(F_{\text{full}}=\textit{twobox})) = 0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = 10{,}010+990q.$$

(The paper prints the latter's constant as "\$110,00", an evident typo for \$10,010.)

The first expression is larger for every $q\in[0,1]$, so A-FDT one-boxes *while looking at a full box*. When it imagines two-boxing, it imagines a world where it most likely sees an empty box. This is the precise sense in which Equation (4) omits conditioning on $\textsc{Obs}=x$.

If the agent first conditioned $P$ on "B is full" and *then* intervened, the box would stay full in both hypotheticals and two-boxing would win. The source mentions in passing that Timeless Decision Theory did both, a "double update" that "proves harmful in practice."

The paper argues that this case is structurally identical to Parfit's hitchhiker. Paying the driver once in the city is the analogue of leaving the \$1,000. Neither CDT nor EDT pays, and so neither gets rescued.

### Two kinds of blackmail

**XOR blackmail.** A predictor sends a letter iff exactly one of these holds:

- no termites, and the agent will pay on receiving the letter;
- termites, and the agent won't pay.

Intervening on $F_{\text{letter}}$ changes *whether the letter is sent*. It does not change the termites. So paying merely buys a letter in termite-free worlds. A-FDT refuses, as CDT does but EDT does not.

**Mechanical blackmail.** The blackmailer launches the damaging program only if she predicts payment. Intervening on $F_{\text{blackmail}}$:

- **pay** means you are almost surely blackmailed and lose \$1,000;
- **refuse** means you are almost never blackmailed.

A-FDT refuses even while holding the letter. Here it beats both CDT and EDT.

The source's imperfect-predictor variant is instructive. Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$. Then refusing costs $\varepsilon\cdot 10^6$ in expectation, and paying costs \$1,000. The threshold is therefore $\varepsilon = 0.001$.

- At $\varepsilon=0.0009$, refusing costs \$900, so A-FDT refuses, as the paper says.
- Above 0.1%, A-FDT pays.

(The paper's "0.011%" is presumably intended as 0.11%. As printed, 0.011% would still favor refusal.)

### Death in Damascus

Death, a perfect predictor, books an appointment wherever the agent will be. Under A-FDT, Death's book is a child of $F$. Every hypothetical therefore has Death meeting the agent. The only difference between staying and fleeing is the \$1,000 cost of fleeing, so A-FDT stays.

CDT oscillates instead. Whichever action it expects, it prefers the other, because it holds Death's location fixed. The source adds a sharper point: CDT would even decline to pay \$1 for a truly random coin that offers a 50% survival chance. A-FDT values the coin correctly, because a genuinely random coin is a process that does *not* depend on $F$, so it really can break the correlation.

## 5. Where Equation (4) underdetermines the answer

The paper is candid that A-FDT is only as good as $G$. It calls "deduc[ing] the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem in the study of functional decision theory." Below I separate four gaps and give my proposed operationalization for each.

### (a) Which systems get edges from $F_x$?

The source gives paradigm cases:

- **Yes:** twins, accurate simulators, and mental models of the agent.
- **No:** lesions and coincidentally correlated objects.

It gives no criterion for intermediate cases, such as a predictor who uses demographic statistics rather than modelling the agent's reasoning, or a "twin" who runs a slightly different algorithm.

My proposal is a working test: draw an edge $F_x\to Z$ to the extent that the agent's credence is that $Z$'s value is *computed from* a faithful representation of the function the agent is running on input $x$. Inaccuracy is then modelled with a noise parent, as with $\textsc{Accurate}$ in Newcomb. This test does not dissolve the counterpossible problem. It only localizes it to the question of whether the system models *me*.

A predictor that looks only at, say, my birth year correlates with my choice without subjunctively depending on it. It should be treated like the lesion.

### (b) What is $P$: prior or posterior?

Equation (4) has no conditioning on $x$. The transparent Newcomb calculation evaluates the two-boxing hypothetical with box B empty with probability 0.99. That is only possible if $P$ has *not* been conditioned on the observation "full."

This creates a small notational wrinkle. The paper's displayed transparent-Newcomb expression places "$\textsc{Obs}=\textit{full}$" inside the $\mathtt{do}$ term, and its parentheses are unbalanced. But the computation it carries out treats the observation solely as the choice of node.

My operational reading: $P$ is the agent's model of the decision problem *prior to the observations that the decision function itself takes as input*, that is, prior to anything that might be downstream of $F$. Information that cannot depend on $F$ can be folded into $P$ harmlessly, since conditioning on a non-descendant of $F$ commutes with $\mathtt{do}(F=a)$. I think this is the cleanest consistent reading of the source's examples. But the paper never states it as a rule.

### (c) What values do the other decision nodes take?

In transparent Newcomb and the smoking lesion, the expected utilities depend on the agent's credence about her *own* outputs at other inputs: $q$ for $F_{\text{empty}}$ and for $F_R$. The source notes the "correct" values (respectively $q=1$, and $q=0$ for the lesion case) but says that in those problems "it won't matter" if the agent is uncertain.

In general it *does* matter. Here is my own example. An agent is told that a copy of her will be shown *green* while she is shown *red*. Each chooses A or B:

- both A: 10 each;
- both B: 5 each;
- mismatch: 0.

In state red, A-FDT intervenes on $F_{\text{red}}$ and leaves $F_{\text{green}}$ at its prior, with $r = P(F_{\text{green}}=A)$:

$$\mathbb E(V\mid\mathtt{do}(F_{\text{red}}=A)) = 10r,\qquad \mathbb E(V\mid\mathtt{do}(F_{\text{red}}=B)) = 5(1-r).$$

So A-FDT picks A iff $r>1/3$. If the agent's self-model predicts that "green-me" plays B, then red-me also plays B. That belief is then confirmed, giving the self-consistent but inferior outcome (B, B).

Policy-selecting FDT instead maximizes over maps $\pi:\{\text{red},\text{green}\}\to\{A,B\}$, intervening on the whole function at once. It finds $(A,A)$.

I take this to be the kind of case the paper means by "makes a difference in certain multi-agent dilemmas." The lesson for practitioners is twofold:

- A-FDT is fully determined only once the priors on non-intervened $F_y$ nodes are fixed.
- The natural requirement is *self-consistency*: these priors should match what A-FDT actually outputs at those inputs. That requirement is a fixed-point condition and may have multiple solutions.

When the choice matters, as in coordination across information states, A-FDT's answer is genuinely sensitive to the agent's self-predictions, and the policy-selecting variant is the principled repair.

### (d) Ties and degenerate priors

A positive feature, implied by the source, is that A-FDT does not suffer EDT's zero-probability problem. $\mathtt{do}$ is well-defined even when $P(F_x=a)=0$, so a confident self-prediction never removes an option from consideration.

Ties are not addressed. Any tie-breaking rule must itself be part of the function the predictor models, since predictors are modelling *that* function.

## 6. Philosophical motivations and the objection from "control"

### The source's three arguments

The source defends A-FDT's verdicts with three arguments.

- **Precommitment.** CDT and EDT agents would pay to bind themselves to the A-FDT action in transparent Newcomb, the hitchhiker case, and mechanical blackmail. A-FDT "simply act[s] as [it] would have precommitted to act." Relatedly, A-FDT does not wish to self-modify mid-problem. The authors call it "reflectively stable in fair problems," though "so far as we know."
- **Value of information.** A-FDT never pays to avoid learning, unlike EDT in some cases.
- **Utility.** Over the distribution of agents a predictor faces, A-FDT agents end up richer. The authors regard this as the argument that "gives the precommitment and value-of-information arguments their teeth."

### Dominance

The two-boxer's dominance argument holds the prediction fixed while varying the act. On this view it is just CDT's counterfactual restated. An A-FDT-style dominance notion holds subjunctive dependencies fixed instead, and one-boxing never loses under it. The source concludes that "every method for constructing hypotheticals gives rise to its own notion of dominance," so dominance cannot neutrally adjudicate between the theories.

### Fairness

Some problems reward or punish a *decision procedure* directly, such as "punish all A-FDT agents." These defeat every theory. The authors restrict their claim to "fair" problems, in which outcomes depend only on the agent's behaviour in the dilemma. They concede that "fair" has not been formalized, and their footnote shows why: a copy of the agent that punishes matching behaviour defeats A-FDT specifically.

### Control

The objection is that A-FDT agents falsely believe they control logical facts or the past. The reply is a parity argument. A deterministic CDT agent equally "controls" only an imagined variation in her physical token. In the authors' words, any principled objection here "will also imply that (deterministic) CDT agents cannot 'control' their decision token." On this view hypotheticals are scratch-paper tools for choosing, not claims about real alternative worlds.

## 7. Conclusion

A-FDT is CDT with the intervention moved from the physical act to the node representing the agent's decision function evaluated on its current observations. That node is $\textsc{fdt}(\underline P,\underline G,\underline x)$, and observations select which node is intervened on rather than being conditioned upon.

Given an accurate dependence graph, this single rule produces the following verdicts:

- one-boxes in Newcomb's problem;
- cooperates with twins;
- smokes in the lesion case;
- pays the driver in Parfit's hitchhiker;
- one-boxes in transparent Newcomb;
- refuses both kinds of blackmail;
- stays in Damascus.

Its weaknesses lie where the source places them, and in one place it mentions only briefly:

- The graph $G$ must encode subjunctive dependencies, and there is no theory yet of how to learn it.
- The interventions are counterpossible.
- Because A-FDT optimizes one input at a time, its verdicts can depend on its own self-predictions at other inputs. This is the gap the policy-selecting FDT variant is designed to close.

For applying A-FDT to new cases, the practical recipe is: identify every system that models your decision function, wire those systems to the appropriate decision nodes, leave mere correlates unwired, intervene on the current node, and choose the best resulting world.

**References.** Yudkowsky, E. & Soares, N., *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060. Works cited within it: Gibbard & Harper (1978); Joyce (1999); Pearl (2000).