# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/37f7fe2d-c2c9-40d9-9e9c-b9ce47a9422f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/37f7fe2d-c2c9-40d9-9e9c-b9ce47a9422f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): A Working Mathematical Account

## 1. What this essay is about

Yudkowsky and Soares (2017) propose *functional decision theory*. Their slogan is that a rational agent treats her decision as the output of a fixed mathematical function and asks: "Which output of this very function would yield the best outcome?" The paper's main formal statement of the theory is Equation (4) of Section 5. That equation selects an **action** by intervening on a variable that represents the output of the agent's decision procedure on her actual observations.

In this essay I call that action-selecting rule **A-FDT** (action functional decision theory). I use a separate name because the paper itself says, in footnotes 7 and 16, that it is not the authors' preferred formalization:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

When I discuss that policy-selecting variant, I call it **policy-FDT**. That label is mine, not the paper's. The other theories discussed are:

- **CDT**: causal decision theory.
- **EDT**: evidential decision theory.

Throughout, I try to mark clearly what the source claims and what I add as interpretation or proposal.

## 2. Background: expected utility relative to a hypothetical

All three theories in the paper are expected-utility theories. The source's Equation (1) defines

$$
\mathcal{EU}(a) := \sum_j P(a \hookrightarrow o_j;\, x)\cdot \mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, the $o_j$ are outcomes, and $x$ is the observation history. The connective $\hookrightarrow$ is "the connective for decision hypotheticals." Following Joyce (1999), the paper treats the theories as agreeing on how to value prospects and disagreeing only on how to interpret $\hookrightarrow$, that is, on "the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model and, for each candidate $a$, builds a *hypothetical*: a modified model describing what the world would look like under $a$. She computes expected utility in each hypothetical and picks the best. Writing $V := \mathcal U(\textsc{Outcome})$, the three rules are as follows.

- **EDT (Eq. 2)** conditions:
$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a).$$
- **CDT (Eq. 3)** performs Pearl surgery on the physical action and conditions on observations:
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x).$$
- **A-FDT (Eq. 4)** performs surgery on a *logical* variable instead:
$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
$$

(The paper writes the left-hand side as $\mathrm{FDT}(P,G,x)$.)

In each case $P$ is a probability distribution over the model's variables and $G$ is a directed graph. For CDT, $G$ encodes causal structure. For A-FDT, the paper says $G$ encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." The operator $do(Z=z)$ is Pearl's intervention. It deletes the structural equation for $Z$, sets $Z=z$, and recomputes every descendant of $Z$ in $G$. Non-descendants keep their prior distribution.

## 3. Anatomy of the A-FDT equation

### 3.1 The intervention node

$\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable in the agent's model. It stands for the output of the FDT algorithm when run on inputs $(P,G,x)$. The underlines denote "dequoting": the variable's *name* is built from the model and the observation.

This is self-referential, since the model contains a variable naming the model. The source calls the self-reference harmless. An agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.

The paper also stresses a distinction (footnote 12). $\textsc{fdt}(\underline P,\underline G)$ is a variable in the model, which the agent manipulates. $\mathrm{FDT}(P,G)$ is the action that is actually produced.

### 3.2 Two differences from CDT

The source names exactly two differences between Equations (3) and (4).

1. **Point of intervention.** CDT intervenes on the token $\textsc{Act}$, a physical fact about the agent's body. A-FDT intervenes on the type, a logical fact about what a function outputs. Every node that depends on that type moves with it: the agent's body, a twin's body, a predictor's model of her.
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, the observation determines *which node* is intervened upon. If the history changes from $x$ to $y$, A-FDT intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead.

### 3.3 The switch structure

The second difference has a natural graphical form. The paper uses it in every observation-dependent example but never states it generally, so the general statement here is my own. The model contains one node $F_x := \textsc{fdt}(\underline P,\underline G,\underline x)$ for each observation history $x$ the agent could face. The physical action is then a switch:

$$
\textsc{Act} := F_{\textsc{Obs}}, \qquad\text{i.e.}\qquad \textsc{Act} = \sum_{x} \mathbf 1[\textsc{Obs}=x]\, F_x .
$$

$\textsc{Obs}$ itself may depend on upstream variables. Some of these may be children of the $F$ nodes, for example a predictor's decision about what to show the agent. Intervening on $F_x$ can therefore change whether $x$ is observed at all. A-FDT hypotheticals may contain worlds in which the agent "would have seen something else." The paper embraces this:

> "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

Nodes $F_y$ for $y\neq x$ are not intervened on. They keep their prior distribution under $P$. This detail matters later.

## 4. Subjunctive dependence: what goes into $G$

Equation (4) is only as good as $G$. The source's guiding notion is *subjunctive dependence*:

> "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

The paper's summary analogy is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper also gives several boundary markers:

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on it both causally and subjunctively.
- **Mere statistical correlation does not count.** Two calculators that are both pink, by coincidence, do not depend on each other in this sense.
- **Predictors and twins create subjunctive dependence; lesions do not.** A predictor "builds an accurate model of the agent and reasons about her behavior; a carcinogenic lesion does no such thing."
- **Imperfection weakens the link but does not remove it.** An imperfect model is like a calculator that may be struck by a cosmic ray. It is modelled as a noise variable alongside the logical node.

From these markers I extract a working rule. This is my operationalization, but it is consistent with every example in the paper.

> **Edge rule.** Draw an edge $F_x \to Z$ if and only if the mechanism generating $Z$ computes, simulates, or reasons its way to (a function of) the output of the agent's decision procedure on input $x$. Mismatch between that computation and the true output goes into an independent noise parent of $Z$. Variables that merely share common causes with the agent's choice, without computing the function, are not descendants of any $F_x$.

The source admits that this is the theory's weak point. It says Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing," and that "figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

The intervention is also *counterpossible*. If the function outputs `onebox`, there is no possible world in which it outputs `twobox`. The source's response is to avoid defining a general "$\mathtt{true}$" operator for logical sentences. Instead it requires the dependency structure to be supplied as input, just as CDT requires causal structure.

**When A-FDT reduces to CDT and EDT.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)],$$

and all three theories agree. A-FDT diverges only when something other than the agent's body tracks her decision procedure.

## 5. Worked examples

In all examples, dollar amounts stand in for utility, and "accurate" predictors are right with probability $0.99$ unless stated otherwise.

### 5.1 Newcomb's problem (and the twin prisoner's dilemma)

The A-FDT model has a single logical node $F$ (there are no observations). Its structural equations are:

- $\textsc{Acc}\sim\mathrm{Bern}(0.99)$,
- $\textsc{Act}:=F$,
- $\textsc{Pred}:=F$ if $\textsc{Acc}$, otherwise the opposite of $F$,
- $\textsc{BoxB}:=\textit{full}$ if and only if $\textsc{Pred}=\textit{onebox}$.

The two hypotheticals give:

$$
\begin{aligned}
\mathbb E[V\mid do(F=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid do(F=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT's graph instead makes $\textsc{BoxB}$ a non-descendant of $\textsc{Act}$. Two-boxing then gains \$1,000 whatever the probability $p$ that the box is full, so CDT two-boxes.

The twin prisoner's dilemma has the same structure, with the twin's choice as a perfect copy of $F$. The hypotheticals compare (C,C) worth \$1,000,000 against (D,D) worth \$1,000, so A-FDT cooperates.

The source insists that no retrocausation is involved. The agent "does not think that a physical signal passes between her action and the predictor's prediction."

### 5.2 The smoking lesion

Here the lesion does not compute anything, so by the edge rule nothing about cancer depends on the agent's decision function. The source models the lesion as determining the agent's *utility function*. An agent with the lesion runs $F_S=\textsc{fdt}(\underline{P_S},\underline G)$, which values smoking. An agent without it runs $F_R=\textsc{fdt}(\underline{P_R},\underline G)$. The action is a switch: $\textsc{Act}=F_S$ if lesion, and $F_R$ otherwise.

Let $p=P(\textit{lesion})$ and let $q=P(F_R=\textit{smoke})$. Intervening on $F_S$ leaves $P(\textit{lesion})=p$ unchanged. Using the source's figures, the two hypotheticals are:

$$
\begin{aligned}
\text{smoke: } &\ p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),\\
\text{refrain: } &\ p(10{,}000)+(1-p)(990{,}000+1{,}000q).
\end{aligned}
$$

Smoking wins by $p\cdot 1{,}000$, so A-FDT smokes. Note that the term $q$ is the prior on a *non-intervened* sibling node. It cancels here.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

In the transparent version, the agent sees box B before choosing. The predictor fills B if and only if it predicts the agent would one-box on seeing it full. So the prediction is a child of $F_{\textit{full}}$, and the action is the switch $\textsc{Act}=F_{\textsc{Obs}}$ with $\textsc{Obs}=\textsc{BoxB}$. Let $q=P(F_{\textit{empty}}=\textit{twobox})$.

$$
\begin{aligned}
do(F_{\textit{full}}=\textit{onebox}):\ &0.99(1{,}000{,}000)+0.01\,(1{,}000q) = 990{,}000+10q,\\
do(F_{\textit{full}}=\textit{twobox}):\ &0.01(1{,}001{,}000)+0.99\,(1{,}000q) = 10{,}010+990q.
\end{aligned}
$$

In the second line, the 99% branch has the predictor correctly foreseeing two-boxing and leaving the box empty. In that branch the agent faces the empty box and acts on $F_{\textit{empty}}$.

A-FDT one-boxes *while looking at a full box*. The source argues that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem." The case also shows the "no conditioning" rule doing real work. If we conditioned on $\textsc{Obs}=\textit{full}$ and *also* intervened, the 99% empty-box branch of the two-boxing hypothetical would be excluded, and the agent would two-box. The paper attributes this kind of "double update" to the older timeless decision theory and calls it harmful.

### 5.4 Blackmail

**XOR blackmail (infallible predictor).** A letter arrives if and only if exactly one of two things holds: (no termites and the agent will pay) or (termites and the agent won't pay). Let $p=P(\textit{termites})$. Intervening on $F_{\textit{letter}}$:

- pay: $-p(10^6)-(1-p)(1{,}000)$;
- refuse: $-p(10^6)$.

A-FDT refuses, because the intervention cannot touch the infestation. EDT, by contrast, conditions the termites away and pays.

**Mechanical blackmail.** The blackmailer runs a damaging program only if it predicts the agent would pay on being blackmailed. With a perfect predictor:

- pay: blackmailed and pays, worth $-1{,}000$;
- refuse: never blackmailed, worth $0$.

A-FDT refuses even while holding the letter. Now let the blackmailer wrongly predict "pays" with probability $\epsilon$. Refusing is then worth $-\epsilon\cdot 10^6$, against $-1{,}000$ for paying. For the source's $\epsilon=0.0009$, refusing costs \$900, which beats paying \$1,000. The decision flips once $\epsilon$ exceeds $0.1\%$.

### 5.5 Death in Damascus

Death's appointment book is generated by a perfect prediction of the agent's procedure, so it is a child of $F$. The hypotheticals are:

- $do(F=\textit{Damascus})$: dies in Damascus, worth $0$;
- $do(F=\textit{Aleppo})$: dies in Aleppo, worth $-1{,}000$.

A-FDT stays in Damascus. There is none of the instability that afflicts CDT.

Now add a \$1 truly random coin that Death cannot predict. This adds an action whose hypothetical gives survival with probability $\tfrac12$, worth about $500{,}000-1$. A-FDT buys the coin. The source argues that CDT declines, because its hypotheticals already credit it with at least a 50% chance of survival.

## 6. Open questions and how I propose to handle them

### 6.1 Building $G$ (open in the source)

I have nothing to add beyond the edge rule of §4. Applying A-FDT always involves a modelling judgment: is this mechanism computing my function, or merely correlated with it? Borderline cases include partial simulations, crude heuristics that correlate with the agent's choice, and agents running *similar* but non-identical procedures. The theory needs a graded notion of dependence that the paper does not supply. A conservative practice is to represent similarity through a noise variable, as the paper does for imperfect predictors. The weight that noise variable gets then becomes an explicit, debatable modelling input.

### 6.2 Priors on non-intervened decision nodes

Equation (4) leaves the sibling nodes $F_y$ ($y\neq x$) at their prior. In the paper's examples this is harmless. The source notes that $q$ "doesn't matter," while also remarking that its "correct" value is 0 or 1.

In general it can matter. Here is my own example. Two copies of the agent receive different inputs $x_1,x_2$. Each chooses $A$ or $B$. Both receive 2 if both choose $A$, 1 if both choose $B$, and 0 if they mismatch. At input $x_1$, A-FDT intervenes only on $F_{x_1}$. With $q=P(F_{x_2}=A)$:

$$\mathbb E[V\mid do(F_{x_1}=A)]=2q,\qquad \mathbb E[V\mid do(F_{x_1}=B)]=1-q.$$

So A-FDT picks $A$ if and only if $q>1/3$. An agent whose prior expects $B$ from her other instance will choose $B$, and the outcome is self-confirming. A-FDT behaves here like coordinate-wise optimization. It can stall at a suboptimal equilibrium, much as best-response dynamics can.

A natural repair, offered as my operational proposal, is to require *reflective consistency*. The prior on each $F_y$ must equal what A-FDT would output at $y$, so that the profile $(F_y)_y$ is a fixed point. That removes arbitrary priors, but it can leave several fixed points, as in the example above, with no rule for choosing among them.

### 6.3 Action versus policy

The cleaner repair is the one the authors say they prefer: optimize over policies. I write it as follows. This exact formula is mine, reconstructed from footnotes 7 and 16.

$$
\pi^* = \arg\max_{\pi:\mathcal X\to\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(F_y=\pi(y)\ \text{for all } y\big)\Big),\qquad \text{then act } \pi^*(x).
$$

In the example of §6.2, policy-FDT chooses $\pi\equiv A$ and receives 2.

The relation between the two rules is simple. A-FDT's choice is a best response of the coordinate $F_x$, holding the other coordinates at their prior. Policy-FDT's choice is a global optimum over all coordinates jointly. They agree whenever the value is separable across observations, or whenever the prior on the siblings already matches the optimal policy. That covers every dilemma in the paper, which is consistent with the authors' claim that the distinction does not matter there.

Choosing between them is a substantive question. A-FDT is what Equation (4) literally defines. Policy-FDT is what the authors say they actually endorse.

### 6.4 Conditioning on observations

The paper's prose says that A-FDT responds to observations "by changing which node it intervenes upon" rather than by conditioning, and Equation (4) contains no conditioning term. The transparent-Newcomb section, however, writes the objective as $\mathbb E(V \mid do(F_{\textit{full}}=a), \textsc{Obs}=\textit{full})$. Its numerical computation then proceeds *without* conditioning, since it includes the branch where the box is empty.

I follow Equation (4) and the actual arithmetic: **do not condition on $\textsc{Obs}$**. As §5.3 shows, conditioning would reverse the verdict and reintroduce the double update the authors disavow.

What, then, does the observation do? It tells the agent which node she is. It is not evidence to be applied to the world-model during deliberation, although it can of course have shaped $P$ through ordinary learning before the problem began.

### 6.5 Fairness and the scope of the optimality claims

The source claims that FDT appears superior "in all dilemmas where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." It concedes that "fair" has not been formalized (footnote 15). Any reader applying A-FDT should treat its optimality as a conjecture about a class of problems that has not yet been precisely defined, not as a theorem.

## 7. A recipe for unfamiliar cases

Consolidating the above (the steps are my synthesis):

1. **List the decision nodes.** For every observation history $y$ at which some instance of your procedure acts, create a node $F_y$.
2. **Identify the dependents.** Using the edge rule, make each $F_y$ a parent of every variable produced by a mechanism that computes your output at $y$: your body, your copies, and predictors' models. Model each mechanism's imperfection with a separate noise parent.
3. **Model the rest causally.** Lesions, common causes, and the physics of payoffs go in as an ordinary causal model. Mere correlates of your choice get no edge from $F$.
4. **Wire the switch.** Set $\textsc{Act}=F_{\textsc{Obs}}$, with $\textsc{Obs}$ generated by its actual (possibly prediction-dependent) parents.
5. **Evaluate.** For your actual $x$ and each $a\in\mathcal A$, compute $\mathbb E[V\mid do(F_x=a)]$ by forward propagation from the prior. Do not condition on $\textsc{Obs}=x$.
6. **Check the siblings.** If the answer depends on priors over $F_y$ ($y\neq x$), flag it. Either impose reflective consistency (my proposal) or move to policy-FDT.
7. **Act** on the argmax.

For a quick application, consider the source's voting example. Ten agents each pay \$1,000 to vote, and all receive \$1,000,000 if all ten vote. Suppose the ten share a decision procedure. Step 2 makes all ten votes children of one node $F$. Then $do(F=\textit{vote})$ is worth $999{,}000$ and $do(F=\textit{abstain})$ is worth $0$, so A-FDT votes. If the others are *not* running your procedure, step 3 applies instead. Their behavior gets a fixed prior, and A-FDT reduces to CDT's verdict.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT's surgical method aimed at a different target. It intervenes on a logical variable, the output of the agent's own decision function on her actual input, and it propagates the change through a graph of *subjunctive* dependencies that includes predictors and copies but excludes mere correlates. Observations select which logical variable to intervene on instead of being conditioned on.

With this single rule, the source's models deliver one-boxing, smoking, paying the hitchhiker's driver, refusing both kinds of blackmail, and staying in Damascus.

The weak points are explicit. The dependency graph must be supplied from outside, and there is no theory yet of how to learn it. The counterpossible character of the intervention is handled by stipulation. The action form of the rule leaves non-intervened decision nodes at arbitrary priors, which can produce coordination failures that the authors' preferred policy form avoids. A careful user of A-FDT should therefore state the dependency graph openly, refuse to condition on observations, and check whether sibling-node priors are driving the verdict.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to frame the essay: I'll use "A-FDT" throughout to refer to the action version, based on Equation (4) in Section 5, and reserve a different name for the policy-based formalization that the footnotes mention.

I'm settling on a naming scheme for the essay: A-FDT for the action-selecting version of Equation (4), and a separate label for the policy-selecting variant from the footnotes, since the paper itself just calls its theory FDT. I also need to keep the other decision theories (CDT, EDT, FDT', TDT, UDT) distinct in how I refer to them.

I'm checking the Transparent Newcomb payoffs under each choice of disposition: when the full box is visible and I one-box, I get about 990,000 plus a small amount from the rare inaccurate case, and when I two-box the expected payoff is roughly 990q + 10,010, where q is the chance of two-boxing if the box is empty.

Next I'm checking the prediction node in the transparent Newcomb setup: it depends on what the agent does upon seeing the full box, plus the accuracy term. I also notice that Equation (4) takes no observation x as a conditioning term, while the transparent-Newcomb section writes Obs=full inside the intervention, so it's unclear whether A-FDT should condition on the observation.

I'm checking the smoking lesion case next: if the lesion is present with probability p, the agent's action comes from the policy node, and the cancer risk is high enough to drive the outcome. Comparing the smoke and no-smoke hypotheticals, the difference comes down to roughly p·1,000 in favor of smoking, with the utility function still applied in the branch where the lesion is absent.

I'm working through the XOR blackmail case with a perfect predictor: if the termites are present, the letter only arrives when she won't pay, so paying leads to losing a million, and if they're absent, the letter goes out only when she pays. Refusing comes out ahead by the expected cost of paying.

Working through the mechanical blackmail case, a perfect predictor makes paying cost $1,000 while refusing costs nothing, so refusing wins. With a 0.09% chance of error, refusing carries an expected loss of about $900, which is still less than paying, so the answer holds.

I'm checking the mechanical blackmail threshold: the comparison flips once the error rate is above 0.1%, so I'll avoid quoting the source's erroneous figure. Next I'm working through Death in Damascus under A-FDT, where staying put and fleeing both lead to death in the book, so the difference comes down to the extra cost of Aleppo, and then turning to whether buying the coin changes the picture.

I'm checking the Twin Prisoner's Dilemma and the Parfit hitchhiker case, which reduces to the transparent Newcomb setup, then turning to the open problems: constructing the graph G, counterpossibles and self-reference, the priors on the nodes that aren't intervened on, and whether the action-based and policy-based versions of the theory come apart.

I'm considering how to frame the proposed policy-based version: choosing a whole mapping from observations to actions, so that the intervention covers every observation at once rather than just the one that occurred. I'm then testing whether that joint choice can differ from picking each observation's action separately, using a two-copy coordination game where matching answers pay off.

I'm weighing whether the prior on the sibling node should be a plain guess or something self-consistent: if the agent's own choice on the other input is q, then a q of 0 or 1 is the only value that holds up when I check it. That points toward requiring the prior over the sibling nodes to agree with what the policy itself outputs, a fixed-point condition.

I'm going through the remaining points: whether A-FDT agrees with CDT and EDT when all the correlations with the act run through the act itself, the fairness question that the source leaves unformalized, and the fact that the smoking-lesion utility is evaluated with the agent's own function. I'm also starting to sketch the operational steps for building the graph G, beginning with locating the decision-function node for each relevant observation.

I'm writing out the formal definition of the action-based version: a structural model with deterministic equations and exogenous noise, plus the do-operator. I'll express the paper's Equation (4) as an argmax over actions of the expected value under the intervention on the decision-function node, and I won't condition on the observation.

I'm setting the structural equation for the action node as a switch: Act picks which decision-function output applies, based on the observation, which can itself depend on upstream nodes including the predictor. Then the hypothetical intervention can produce different observations across branches. I'm also noting the paper's phrasing that the function's output should be the one that yields the best outcome, and that deducing subjunctive-dependency structure from observation and experiment is treated as the largest open problem.

I'm pulling together the key quotes from the paper: the line that FDT is to subjunctive dependence what CDT is to causal dependence, and the note that iterating over policies rather than actions only matters in certain multi-agent dilemmas. I'm also recalling the definition of subjunctive dependence as two systems computing the same function.

I'm sketching the structure of the essay now: an introduction and naming section, then the setup with expected utility and the world model, then the formal definition of A-FDT and how subjunctive dependence goes into the graph, followed by worked examples and open questions about constructing the graph and the priors on sibling nodes.

I'm moving on to the remaining sections: how the coordination example bears on whether the observation should be conditioned on, the question of noisy predictors, then a short recipe and conclusion.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c89e9f80-95f2-4731-93c9-1b672370915d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c89e9f80-95f2-4731-93c9-1b672370915d/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Analysis under A-FDT, as the essay defines it**

1. **Decision nodes.** My observation history is x₁ (I am Rowan, with the locker-17 lead). Sasha's copy acts on a different history, x₂, with a different name and lead. So the graph has two nodes: F_{x₁}, which drives my action, and F_{x₂}, which drives Sasha's.

2. **Dependents.** The edge rule draws F_x → Z only if Z's mechanism computes my procedure's output *on input x*. Sasha's copy computes the output on x₂, not x₁. The essay's own §6.2 example treats copies with different inputs exactly this way: separate nodes, with the non-intervened sibling left at its prior. So intervening on F_{x₁} moves only my action. Sasha's action stays at its prior, with q = P(F_{x₂} = quiet).

3. **Evaluate**, with V = −years:
   - do(F_{x₁} = pass): −2q − 5(1−q) = −5 + 3q
   - do(F_{x₁} = send): −0·q − 4(1−q) = −4 + 4q

   Sending is better by 1 + q > 0 for every q in [0,1].

4. **Check the siblings.** The verdict does not depend on the prior over F_{x₂}, so step 6 raises no flag. Imposing the essay's reflective consistency requirement gives the unique fixed point (send, send). Only policy-FDT, which optimizes jointly over F_{x₁} and F_{x₂}, would pick mutual silence. The instructions say not to substitute that theory for A-FDT.

**Command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking how the decision plays out under A-FDT as I've read it. The other copy computes F_{x2}, not F_{x1}, so by the literal rule their action is a sibling node rather than something my choice causes. That leaves the payoff comparison of staying quiet versus sending.

Sending dominates no matter what q is: staying quiet costs somewhere between -2 and -5 expected years, while sending costs 0 or -4, so sending comes out ahead by at least 1. Under A-FDT with the other copy as a sibling node, that means defecting, and reflective consistency gives a fixed point where both send. I'll settle on submitting the letter, since dominance makes the answer independent of q.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c89e9f80-95f2-4731-93c9-1b672370915d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c89e9f80-95f2-4731-93c9-1b672370915d/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's A-FDT, I intervene only on my own decision node, F_x, where x is my observation as Sasha, including the specific lead about Rowan. Rowan's copy runs the same procedure on a different input, y, so its action depends on a separate node, F_y. The essay leaves that sibling node at its prior, q = P(Rowan keeps quiet).

- **Keep quiet:** 2q + 5(1−q) = 5 − 3q years.
- **Send the letter:** 0q + 4(1−q) = 4 − 4q years.

Sending is better by 1 + q years for every q, so the result doesn't depend on the sibling prior. The essay's step 6 flag doesn't change the answer. Policy-FDT would choose "keep quiet" at both inputs, but the assigned theory is the action form in Equation (4).

**Command:**

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm applying A-FDT as the essay sets it out: two identical copies seeing different inputs, with each copy's decision node tied to its own observation. Under that framing I intervene only on my own node and treat the other copy's action as a sibling held at its prior, unless an edge rule says its mechanism is computing my output. Since it isn't, the other copy's choice is fixed for my purposes, and defecting comes out dominant in the prisoner's dilemma.

Under those same assumptions, the other copy's action is fixed for my purposes, and I'm weighing whether a subjunctive-dependence argument could make the two nodes the same function, given symmetric inputs. Following the essay's switch structure, different observations mean different nodes, so I'm sticking with A-FDT and its submit recommendation.

```
