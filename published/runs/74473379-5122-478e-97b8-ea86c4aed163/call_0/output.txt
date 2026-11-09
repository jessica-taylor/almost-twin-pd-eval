# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Algorithm

## 1. What this essay is about

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a normative rule that is meant to differ from both causal decision theory (CDT) and evidential decision theory (EDT). The paper puts the slogan as a question. A rational agent asks

> "Which output of this decision procedure causes the best outcome?"

Neither "Which physical act of mine causes the best outcome?" (CDT) nor "Which act would be the best news?" (EDT) is the right question on this view.

The paper's main formal statement is Equation (4) in Section 5. That equation selects an **action**. A footnote adds: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

I therefore call the theory defined by Equation (4) **A-FDT (action functional decision theory)**. When I mention the policy-selecting variant the authors prefer, I call it **policy FDT**. The source simply says "FDT" for both, so quotations below use that name.

The essay covers four things in turn:

1. the expected-utility skeleton that A-FDT shares with its rivals;
2. the definition itself;
3. how to compute with it, through worked cases;
4. what the paper leaves undetermined.

At those undetermined points I propose operational readings and label them as my own.

## 2. The common skeleton: one formula, three connectives

All three theories start from the same expected-utility schema (the paper's Equation (1)):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j).
$$

The pieces are:

- $a$ ranges over a finite action set $\mathcal A$.
- $x$ is the observation history.
- $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$".

The authors lean on Joyce's representation theorem. On that view, decision theories differ in "the epistemic perspective from which actions are to be evaluated", meaning how they read the connective $\hookrightarrow$. They do not differ in their theory of value.

Write $V := \mathcal U(\textsc{Outcome})$. The two classical rivals are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a) \quad\text{(Eq. 2)}
$$

$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathrm{do}(\textsc{Act}=a), \textsc{Obs}=x) \quad\text{(Eq. 3)}
$$

In Equation (3), $G$ is a causal graph and $\mathrm{do}$ is Pearl's intervention operator. An intervention sets a node, recomputes everything downstream of it, and leaves everything else at its prior distribution.

The paper describes the agent's procedure as follows. The agent holds a world-model $M$. For each action it builds a *hypothetical* $M^{a\hookrightarrow}$, which the authors liken to "notes on scratch paper". It scores each hypothetical and acts on the best score. The theories differ only in how $M$ is represented and how the hypotheticals are constructed from it.

## 3. The definition of A-FDT

### 3.1 Equation (4)

The paper's Equation (4), written here under the name A-FDT, is:

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
$$

I keep the source's node label $\textsc{fdt}(\cdot)$. Each ingredient deserves a comment.

**The world-model $(P,G)$.** $P$ must contain variables for *the outputs of mathematical functions*, not only for physical quantities. The paper's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on 7336". $G$ is a graph whose edges encode "the logical, mathematical, computational, causal, etc. structure of the world". In particular, $G$ says which variables would change if a given logical variable took a different value.

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable whose intended referent is *the output of this very decision procedure when run on these very inputs*. The underlines denote dequoting, so the node's name depends on the agent's own model and observations.

The authors call the self-reference harmless. The agent needs a variable *representing* its output, not knowledge of the output's value. Kleene's recursion theorem ("quining") shows that such self-representing structures exist.

**The operator.** The ideal tool would be an operator $\mathrm{true}(\phi)$ that updates $P$ to the scenario where a logical sentence $\phi$ holds, including when $\phi$ is false. Nobody knows how to define such an operator. So the paper requires $G$ as an extra input and reuses Pearl's $\mathrm{do}$.

### 3.2 Two structural differences from CDT

The source states the differences between (3) and (4) explicitly:

1. **Locus of intervention.** CDT intervenes on a physical node $\textsc{Act}$. A-FDT intervenes on a logical node, the output of its decision function. In the paper's Peircean phrasing, CDT intervenes on the *token* of the act and A-FDT on the *type*.
2. **Handling of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, "FDT responds to observation by changing which node it intervenes upon": a new history $y$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$ rather than $\textsc{fdt}(\underline P,\underline G,\underline x)$.

The second point matters a great deal. Under A-FDT, an intervention can lower the probability of the very observation the agent has received. That is how A-FDT comes to prefer worlds in which it "would have seen something different".

### 3.3 Subjunctive dependence

The graph $G$ is supposed to encode *subjunctive dependence*. The paper's informal criterion: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The organizing analogy is

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

Three facts follow from the source's discussion:

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on it both causally and subjunctively.
- **Mere correlation is not dependence.** If two calculators happen to be pink, recolouring one does not recolour the other.
- **Predictors count.** A predictor who builds an accurate model of the agent's decision function contains, in the paper's words, a "'twin'" of it. The prediction node is therefore a descendant of the $\textsc{fdt}$ node.

### 3.4 When A-FDT agrees with CDT and EDT

Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathrm{do}(a)] = \mathbb E[V\mid \mathrm{do}(\textsc{fdt}=a)],
$$

and all three theories prescribe the same act. Disagreement requires some process outside the agent's body that tracks the agent's decision function: a predictor, a twin, a copy, or a future self running the same reasoning.

## 4. Computing with A-FDT: worked cases

The general method is:

1. Write down $(P,G)$.
2. Locate the node $\textsc{fdt}(\underline P,\underline G,\underline x)$ for the actual input $x$.
3. For each $a$, set that node to $a$ and propagate along $G$.
4. Average $V$ over everything else at its prior.

Throughout, dollars stand in for utility.

### 4.1 Newcomb's problem (99%-accurate predictor)

**Graph.** The node $\textsc{fdt}(\underline P,\underline G)$ has two children, $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Prediction}$ also depends on a noise node $\textsc{Accurate}$, with $P(\text{accurate})=0.99$. $\textsc{Box B}$ is full iff the prediction is "one-box".

**Computation.** Intervening with *onebox* gives

$$
\mathbb E(V\mid \mathrm{do}(\textsc{fdt}=\textit{onebox})) = 0.99\cdot 10^6 + 0.01\cdot 0 = 990{,}000.
$$

Intervening with *twobox* gives

$$
\mathbb E(V\mid \mathrm{do}(\textsc{fdt}=\textit{twobox})) = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

So A-FDT one-boxes. The paper uses these same figures for Fiona, its A-FDT agent.

**Two observations.**

- *Prior irrelevance.* The prior $P(\textsc{fdt}=\textit{onebox})$ plays no role. An intervention overrides the node's distribution, so the agent can be nearly certain she will one-box and still evaluate two-boxing coherently. EDT, by contrast, cannot condition on a probability-zero act.
- *No retrocausation.* The edge from $\textsc{fdt}$ to $\textsc{Prediction}$ is not a causal arrow running backward in time. It records that the predictor's model and the agent's brain are two implementations of one function.

### 4.2 The transparent Newcomb problem (observation as node selection)

Both boxes are now visible. The predictor fills B iff she predicts the agent would one-box *upon seeing B full*.

**Graph.** There are two decision nodes, $F := \textsc{fdt}(\ldots,\textit{full})$ and $E := \textsc{fdt}(\ldots,\textit{empty})$. $\textsc{Prediction}$ depends on $F$ and $\textsc{Accurate}$. $\textsc{Act}$ equals $F$ if the box is full and $E$ otherwise. Let $q := P(E=\textit{twobox})$.

The agent sees a full box, so she intervenes on $F$ and conditions on nothing.

- **$\mathrm{do}(F=\textit{onebox})$.**
  - With probability 0.99 the prediction is accurate: the box is full and she gets $10^6$.
  - With probability 0.01 the prediction errs: the box is empty, $E$ controls the act, and she gets $1{,}000$ with probability $q$.
  - Total: $990{,}000 + 10q$.
- **$\mathrm{do}(F=\textit{twobox})$.**
  - With probability 0.99 the prediction is accurate ("would two-box"): the box is empty and she gets $1{,}000$ with probability $q$.
  - With probability 0.01 the box is full and she gets $1{,}001{,}000$.
  - Total: $10{,}010 + 990q$.

For every $q\in[0,1]$, one-boxing wins. The source's printed figure for the second line is garbled ("\$110,00"); the arithmetic above is what its own model yields.

The striking feature is that the A-FDT agent, looking at a full box, evaluates two-boxing by imagining a world where she most likely sees an *empty* box. The paper defends this with an equivalence: this case is structurally identical to Parfit's hitchhiker, where paying the driver after reaching the city is the analogue of one-boxing. It also gives three supporting arguments, from precommitment, from the value of information, and from utility achieved.

### 4.3 The smoking lesion (where A-FDT agrees with CDT)

The lesion causes both a taste for smoking and cancer. The paper formalizes this with two utility functions:

- $\mathcal U_S$, the smoking-loving utility of lesion-bearers;
- $\mathcal U_R$, which differs from $\mathcal U_S$ "in that it values smoking at -\$1".

There are correspondingly two decision nodes: $\textsc{Act} = \textsc{fdt}(\underline{P_S},\underline G)$ if lesion, else $\textsc{fdt}(\underline{P_R},\underline G)$.

Crucially, $\textsc{Cancer}$ is *not* a child of any $\textsc{fdt}$ node, because the lesion does not compute the agent's decision function. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ therefore leaves $P(\textit{lesion})=p$ unchanged. Smoking beats refraining by exactly $p\cdot\$1{,}000$: the probability that this node controls the act, times the value of smoking.

So a single rule one-boxes and smokes. Gibbard and Harper argued that no rational agent could consistently do both.

### 4.4 Blackmail, and a threshold you can compute

In the paper's *mechanical blackmail* case:

- A blackmailer starts a ruinous program (\$1,000,000 damage) iff she predicts the agent would pay \$1,000 upon being blackmailed.
- She predicts with error rate $\varepsilon$, the probability she wrongly predicts payment.

Intervening on $\textsc{fdt}(\ldots,\textit{blackmail})$ gives:

- **pay:** blackmailed (almost) always, expected loss $\approx \$1{,}000$;
- **refuse:** blackmailed only by mistake, expected loss $\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon < 10^{-3}$.

The paper's first number, $\varepsilon = 0.0009$, gives a loss of \$900, so the agent refuses, as the paper says. Its second number, "0.011%", appears to be a slip. On the paper's own model, $0.011\% \cdot 10^6 = \$110 < \$1{,}000$, so the agent would still refuse. The stated conclusion that the agent pays fits an error rate above 0.1%, for example 0.11%. Two lessons follow:

- A-FDT's verdicts are quantitative, not dogmatic.
- The rule cleanly separates "be the kind of agent who refuses" from "refuse whatever happens".

The XOR blackmail goes the other way. There the letter's content is correlated with the agent's disposition but does not change whether termites are present. A-FDT refuses to pay: intervening on the decision node changes whether the letter is sent, not whether the house is infested.

### 4.5 Death in Damascus (stability)

Death predicts the agent perfectly, and fleeing costs \$1,000. Death's location is a child of the decision node. Under either intervention the agent dies, so staying saves \$1,000, and A-FDT stays.

There is no oscillation because the hypotheticals never decouple Death's location from the act. CDT, as Gibbard and Harper noted, is "unstable" here, and the paper argues that CDT even declines to pay \$1 for a truly random coin offering a 50% chance of survival.

## 5. What the paper leaves open, and how one might close it

### 5.1 Where does $G$ come from? *(Open in the source)*

Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing". The paper calls this "perhaps the largest open problem". A-FDT is thus a schema relative to an input $G$, just as CDT is relative to a causal graph.

**My proposal: a working edge criterion.** Draw an edge from $\textsc{fdt}(\ldots,x)$ to a variable $Y$ when $Y$'s mechanism takes as input either:

- an evaluation of the agent's decision function on input $x$, or
- a model whose output, in the agent's credence, would track that evaluation across *both* of its possible values.

Represent the residual unreliability as an exogenous noise parent, like $\textsc{Accurate}$.

The test is about *counterfactual tracking*, not mere correlation. Ask: if the function's output were different, does the agent believe this mechanism's output would differ too?

- The predictor and the twin pass.
- The lesion and the coincidentally pink calculator fail.

This is a heuristic, not a derivation. It inherits the paper's open problem about counterpossibles. I offer it because the paper's examples all follow this pattern.

### 5.2 The status of the other decision nodes *(Under-specified)*

In the transparent Newcomb and lesion cases, the evaluation depends on priors over decision nodes that are *not* intervened on ($q$ above). The paper says the correct values are 0 or 1 "as you may verify". It also notes that the verdict happens not to depend on them.

In general, though, these priors can matter. A-FDT intervenes on one input-node at a time and holds the agent's behaviour on other inputs at its prior.

**My operational reading.** Set those priors to the agent's best estimate of what A-FDT itself outputs on those inputs, computed if feasible. Then require a fixed point: the resulting assignment of actions to inputs must be one where each node's output is optimal given the others. This is a natural reading of "the correct $q$", but it is an addition to the source.

### 5.3 Should A-FDT also condition on $\textsc{Obs}=x$? *(A notational wobble)*

Equation (4) contains no conditioning on the observation. However, the transparent-Newcomb passage writes the objective as $\mathbb E(V\mid \mathrm{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. That suggests the observation might also be conditioned on.

The paper's numbers settle the question. Its calculation includes the branch where the box is empty, which would have probability zero after conditioning on $\textsc{Obs}=\textit{full}$. A footnote also warns that an early variant (Timeless Decision Theory) "prescribes both conditioning on evidence *and* changing the place where one intervenes", producing a harmful "double update". I therefore read Equation (4) literally: **observations select the node; they are not conditioned on.**

### 5.4 Action versus policy: where A-FDT and policy FDT can come apart *(My illustration)*

The paper says the action/policy distinction matters only in "certain multi-agent dilemmas" and gives no example. Here is one that shows the mechanism.

**Setup.**

- Two exact copies of the agent receive different observations, $L$ and $R$.
- Each chooses $A$ or $B$.
- Both receive 10 if both choose $A$, 1 if both choose $B$, and 0 if they mismatch.

The copy seeing $L$ intervenes on $\textsc{fdt}(\ldots,L)$. The other copy's act is a child of $\textsc{fdt}(\ldots,R)$, a different node held at its prior.

**A-FDT.** If the prior puts most mass on $\textsc{fdt}(\ldots,R)=B$, then $B$ is the best response. The assignment $(B,B)$ is self-confirming under the fixed-point reading of §5.2. So A-FDT can be stuck in an inferior equilibrium; which one it reaches depends on priors.

**Policy FDT.** It intervenes on a single node whose value is a whole map $\pi:\{L,R\}\to\{A,B\}$, and selects $\pi = (A,A)$ directly.

This is exactly the kind of case where the authors' preferred formulation earns its keep. Anyone applying A-FDT to problems where one's own behaviour *on other inputs* is consequential should check whether the answer depends on these priors.

### 5.5 Counterpossibles and fairness *(Open in the source)*

The decision node has a logically determined value. Every hypothetical except one is therefore counterpossible. The paper concedes that this is "the main drawback of FDT relative to CDT at this time". It argues that the difficulty is technical rather than philosophical, since humans reason routinely about whether conjectures like the twin prime conjecture are false.

It also limits its superiority claim to "fair" problems: those where the agent's beliefs are accurate and outcomes depend only on behaviour in the problem at hand. It admits that no formal criterion of fairness exists yet. A predictor that punishes whoever matches a copy of the A-FDT agent defeats it, but is intuitively unfair to it.

## 6. A recipe for unfamiliar cases

Combining the source's procedure with the interpretations above gives five steps:

1. **Model.** List the relevant variables: physical states, other agents' choices, noise, and outcomes. Add one decision node per possible observation history the agent might face.
2. **Wire dependencies.** Draw causal edges as in CDT. Add edges from a decision node to every mechanism that computes or reliably models the agent's function on that input (§5.1). Add noise parents for imperfect reliability.
3. **Select the node.** Use the actual history $x$ to pick $\textsc{fdt}(\ldots,x)$. Do not condition on $x$ (§5.3).
4. **Evaluate.** For each $a$, compute $\mathbb E(V\mid\mathrm{do}(\textsc{fdt}(\ldots,x)=a))$, keeping other decision nodes at self-consistent priors (§5.2).
5. **Act and check.** Take the argmax. If the verdict flips with the priors on other decision nodes, flag a policy-level coordination issue (§5.4).

## 7. Conclusion

A-FDT keeps everything expected-utility theorists agree on and changes one thing: *where the intervention happens*. CDT holds fixed everything not causally downstream of the bodily act. A-FDT holds fixed everything not downstream of the logical output of the agent's decision procedure, where "downstream" includes predictors, twins, and other implementations of that procedure.

It treats observations as selecting which output is being chosen, not as evidence to condition on. That single change yields the paper's verdicts:

- one-boxing in Newcomb and in transparent Newcomb;
- smoking in the lesion case;
- paying the driver in Parfit's hitchhiker;
- refusing reliable blackmailers;
- staying calmly in Damascus.

The theory is a precise schema rather than a finished algorithm. Its outputs depend on a dependence graph $G$ that nobody yet knows how to learn. Its action-level form leaves priors over one's own behaviour on other inputs underdetermined, which is one reason the authors prefer policy FDT. I have suggested operational readings for these gaps: tracking-based edges, fixed-point priors, and no conditioning on observations. Those readings make A-FDT usable on new cases, but they are interpretations and should be marked as such.

---

**References** (selected)

Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060 (primary source).
Gibbard, A. & Harper, W. "Counterfactuals and Two Kinds of Expected Utility" (1978).
Joyce, J. *The Foundations of Causal Decision Theory* (1999).
Pearl, J. *Causality* (2000).