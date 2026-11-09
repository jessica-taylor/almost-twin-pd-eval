# A-FDT: Choosing as the Output of a Function

## 1. What this essay is about

Yudkowsky and Soares's paper "Functional Decision Theory: A New Theory of Instrumental Rationality" proposes a decision rule. Its organizing slogan is that an agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper gives several renderings of this idea. It offers informal prose, a counterpossible "$\mathtt{true}$" operator that it explicitly declines to define, and an evidential variant in a footnote. Its working formal definition is Equation (4) of Section 5. That equation selects an **action**. The authors also mention, in footnotes 7 and 16, that their "preferred formalization" instead selects a **policy**, meaning a map from observations to actions. They set the policy version aside "for ease of exposition."

I will call the theory defined by Equation (4) **A-FDT** (action functional decision theory). When I mean the footnoted policy-selecting variant, I will call it **P-FDT**. That label is mine, not the paper's. The paper's two comparison theories are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

My aims are three:

1. to state A-FDT precisely;
2. to work the paper's examples so the mechanics are visible;
3. to say what a practitioner must supply that the paper leaves open.

I flag my own proposals as such.

## 2. The common template

The paper treats all three theories as expected-utility maximizers that differ only in how they construct a *hypothetical*: the agent's imagined picture of how the world would look if she took action $a$. The template is

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and "$\hookrightarrow$" is the free parameter. Following Joyce, the paper says the theories differ about "the epistemic perspective from which actions are to be evaluated." Writing $V := \mathcal U(\text{Outcome})$:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \text{Obs}=x, \text{Act}=a)$. This is Bayesian conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x)$. This is Pearl surgery on the *physical action* node in a causal graph $G$, with conditioning on the observation.
- **A-FDT** (Eq. 4):

$$\boxed{\;\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).\;}$$

Here $P$ is a probability distribution over variables. These variables include variables standing for *outputs of mathematical functions*. $G$ is a graph that says how changing such a logical variable propagates to other variables. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is "what the A-FDT algorithm outputs on input $(P,G,x)$." The underlines denote dequoting: the variable's *name* is built from the agent's own model and observation. The paper notes that this self-reference is harmless. The agent need not know the variable's value in order to represent it, and Kleene's recursion theorem guarantees that such self-representing structures exist.

## 3. The two differences from CDT

The paper identifies exactly two differences between Eq. (3) and Eq. (4).

**First, the point of intervention.** CDT intervenes on a token: this body's movement. A-FDT intervenes on a type: the output of the decision function. In the paper's words, "where a CDT agent performs surgery on a variable Act representing a *physical* fact (about how her body behaves), an FDT agent performs the surgery on a variable representing a *logical* fact (about how her decision function behaves)." Anything in $G$ that is downstream of that logical node changes in the hypothetical. That includes the agent's own act, but also a predictor's simulation of the agent, a twin's choice, or Death's appointment book. Everything else stays fixed.

**Second, the treatment of observations.** Eq. (4) does *not* condition on $\text{Obs}=x$. The observation enters only through the *name* of the node intervened upon. When the history changes from $x$ to $y$, A-FDT switches from intervening on $\textsc{fdt}(\underline P,\underline G,\underline x)$ to intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$. Consequently the hypotheticals may include worlds in which the agent never makes observation $x$. The paper accepts this result, saying that agents "should entertain the hypothesis that, if their action were different, they might have *made different observations*."

This second feature is what separates A-FDT from a naive "CDT on the logical node." In a footnote, the paper notes that the earlier Timeless Decision Theory "prescribes both conditioning on evidence *and* changing the place where one intervenes," which creates "a kind of 'double update' which proves harmful in practice."

**A caution about the text.** In the transparent Newcomb worked example the paper writes the objective as $\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \text{Obs}=\textit{full}))$. With its unbalanced parenthesis, this looks as if it conditions on the observation. The paper's actual computation does not condition. It sums over the case in which the box is empty. I therefore read Eq. (4) literally: **no conditioning on Obs.** This is the only reading consistent with the paper's numbers and with its stated contrast with CDT.

## 4. The procedure, step by step

Here is the procedure as I would hand it to a practitioner. Steps 1–2 are what the paper requires as input. Steps 3–5 are the computation that Eq. (4) prescribes.

1. **Model.** Write down a joint distribution $P$ over the world's variables, including the utility node $V$.
2. **Dependence graph.** For every observation history $y$ that the agent might have had in this problem, introduce a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$. Draw edges from $F_y$ to every variable that *subjunctively depends* on the algorithm's output at $y$. These are typically:
   - the agent's physical act, gated by whether the history is in fact $y$;
   - any prediction, simulation, or copy of the agent's computation at $y$.

   Give each $F_y$ a prior. The paper lets these priors be arbitrary when they do not matter.
3. **Locate the intervention.** Identify the actual history $x$.
4. **Evaluate.** For each $a\in\mathcal A$, set $F_x := a$ by $\mathtt{do}$. Propagate the change downstream. Leave all non-descendants of $F_x$, including the other $F_y$, at their prior distribution. Compute $\mathbb E[V]$ under this hypothetical, using the unconditioned $P$.
5. **Choose.** Output the argmax.

## 5. Worked examples

### Newcomb's problem

The setup: a predictor that is 99% accurate, \$1,000 in box A, and \$1,000,000 in box B if one-boxing was predicted. There is no observation, so there is a single node $F$, and it is a parent of both Act and Prediction. Under $\mathtt{do}(F=\textit{onebox})$:

$$\mathbb E[V]=0.99\cdot 1{,}000{,}000 + 0.01\cdot 0 = 990{,}000.$$

Under $\mathtt{do}(F=\textit{twobox})$:

$$\mathbb E[V]=0.01\cdot1{,}001{,}000+0.99\cdot1{,}000=11{,}000.$$

So A-FDT one-boxes. (The paper reports \$999,000 for EDT's one-box value. That figure appears to be a slip. The paper's own A-FDT computation, and the arithmetic, give \$990,000.)

CDT intervenes on Act, which is not an ancestor of Prediction. The probability $p$ that the box is full is therefore the same in both of CDT's hypotheticals. Two-boxing wins by \$1,000 whatever the value of $p$.

The graphs make the difference plain. Carl, the paper's CDT agent, has a "Predisposition" node as a common cause of his act and the prediction, and he cuts the edge from Predisposition to Act. Fiona, the paper's A-FDT agent, replaces Predisposition with the very node she intervenes on.

### Psychological twin prisoner's dilemma

The same structure applies with the twin's choice in place of the prediction. $F$ is a parent of both players' acts, so the only live comparisons are (C, C), worth \$1,000,000, and (D, D), worth \$1,000. A-FDT cooperates.

### The smoking lesion

This case shows what A-FDT does *not* do: it does not treat every correlation as controllable. The lesion causes cancer, and it also determines which utility function, and hence which decision-function node, controls the act. The paper models this with two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. Act equals the first if the agent has the lesion and the second otherwise.

Intervening on the agent's own node does not touch Lesion or Cancer. With $P(\textit{lesion})=p$ and $q$ the prior that the other node smokes, the two hypotheticals are:

$$\text{smoke: } p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),$$
$$\text{refrain: } p(10{,}000)+(1-p)(990{,}000+1{,}000q).$$

Smoking wins by $1{,}000p$, so A-FDT smokes. EDT, which conditions on the act, refrains.

The general lesson: **a correlation is controllable for A-FDT iff, according to $G$, it runs through a descendant of the intervened decision node.** Statistical correlations through common causes do not count. The paper's own illustration is two pink calculators: the Tokyo calculator's color does not depend on the Parisian one's.

### Transparent Newcomb problem

Both boxes are transparent, and the agent sees box B full. The nodes are $F_{\text{full}}$ and $F_{\text{empty}}$. Prediction depends on $F_{\text{full}}$ together with an accuracy noise term. Box B depends on Prediction. Act is controlled by $F_{\text{full}}$ if the box is full and by $F_{\text{empty}}$ otherwise. Let $q$ be the prior that $F_{\text{empty}}=\textit{twobox}$. Without conditioning on "full":

$$\mathtt{do}(F_{\text{full}}=\textit{onebox}):\quad 0.99(1{,}000{,}000)+0.01(1{,}000q)=990{,}000+10q,$$
$$\mathtt{do}(F_{\text{full}}=\textit{twobox}):\quad 0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q.$$

(The paper prints the second value as "\$110,00 + $q\cdot$\$990"; the constant term should read 10,010.)

The first value is larger for any $q\in[0,1]$, so A-FDT one-boxes *while looking at a full box*. Had it conditioned on Obs = full, as CDT and EDT do, it would two-box. The paper argues that this case is structurally identical to paying the driver in Parfit's hitchhiker problem, which A-FDT also does.

### Mechanical blackmail and the threshold structure

A blackmailer runs a program that does \$1,000,000 of damage to both parties unless the agent pays \$1,000. She runs it iff she predicts the agent would pay. Suppose she wrongly predicts "pay" with probability $\varepsilon$. Let $F_b$ be the agent's node on receiving the blackmail.

- $\mathtt{do}(F_b=\textit{pay})$: the agent is always blackmailed and always pays, for an expected loss of $1{,}000$.
- $\mathtt{do}(F_b=\textit{refuse})$: the agent is blackmailed only through an error and then refuses, for an expected loss of $\varepsilon\cdot 1{,}000{,}000$.

So A-FDT refuses iff $\varepsilon < 0.001$.

For $\varepsilon=0.0009$ the paper correctly finds an expected loss of \$900 and refusal. It then says that at "0.011%" A-FDT pays. That error rate is below the threshold, so I take it as a typo for something above 0.1%, such as 0.11%. In any case, the formula above is what decides.

The example teaches a broader point. A-FDT's answers are threshold functions of predictor reliability. As accuracy degrades, A-FDT moves continuously toward CDT's answers.

### XOR blackmail

In the XOR blackmail problem, termites are independent of the agent's node. Changing $F_{\text{letter}}$ changes whether the letter arrives, but it does not change the probability of termites. Paying therefore buys nothing in any hypothetical, and A-FDT refuses. EDT, conditioning on the letter, pays.

### Death in Damascus

Death predicts the agent's decision function. Both of A-FDT's hypotheticals put Death wherever the agent is. Survival is therefore 0 either way, and A-FDT stays in Damascus, saving the \$1,000.

CDT's verdict oscillates instead. In each of CDT's hypotheticals, Death's location is held independent of the act. The paper also argues that this leads Carl to refuse a \$1 truly random coin, since by his hypotheticals he already acts as if his survival chance were at least 50%.

## 6. Where A-FDT agrees with CDT and EDT

The paper states that the three theories coincide on models where every correlation between Act and other variables is caused by Act, apart from Act's own dependence on the decision node. In those models

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].$$

Practically, this means that unless something else in the world computes or models your decision, A-FDT is ordinary causal expected-utility maximization.

One further condition is my own addition, though it follows from the formulas. A-FDT conditions on nothing, while CDT conditions on $x$. Even without predictors, then, the two agree only when the observation is not itself downstream of the decision node, so that the observation's probability is unaffected by the intervention. In the ordinary case the observation is upstream of the decision node. There, Pearl's back-door logic makes intervening on $F_x$ without conditioning equivalent, for the purpose of ranking actions, to conditioning on $x$ and then intervening. The value of $F_x$ only matters in worlds where the history is $x$; worlds with other histories contribute equally to every action's score.

## 7. What the paper leaves open, and how I would proceed

### (a) Building $G$

The paper is explicit that this is the central gap:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

Equation (4) "works *given* a graph," and the graph is an input, just as CDT takes the causal graph as given.

*My operational proposal.* Draw an edge $F_y \to Z$ exactly when $Z$'s mechanism contains a sufficiently faithful evaluation or model of the agent's decision computation on input $y$. Weight the edge by an explicit reliability parameter, as the paper does with its Accurate node. Lesions, genes, and mere statistical regularities do not qualify unless they implement or track that computation. This matches every example in the paper, but it leaves "sufficiently faithful" as a judgment call.

### (b) Counterpossibles

Since $F_x$ has a mathematically determined value, intervening on it is counterlogical. The paper does not define a $\mathtt{true}$ operator. It replaces that operator with $\mathtt{do}$ on a supplied graph and calls the difficulty "technical rather than philosophical." Inside Eq. (4), the graph simply *stipulates* the counterpossible structure. Users should be aware that every substantive verdict is encoded there.

### (c) Priors on the non-intervened decision nodes

The other nodes $F_y$ remain at their priors. The paper twice remarks that the correct value, for instance $q=1$ or $q=0$, "won't matter" in its examples. In general it can matter. *My recommendation*: set the prior on each $F_y$ to the agent's best estimate of what A-FDT outputs at $y$. If that is uncertain, compute A-FDT at $y$ first, provided doing so does not loop. Then check that the verdict is robust across $q\in[0,1]$, as the paper's examples are.

### (d) A-FDT versus P-FDT

This is where the action/policy distinction matters. A-FDT varies one node $F_x$ and holds the others at their priors. P-FDT, as footnoted, chooses an entire map $\pi:\mathcal X\to\mathcal A$, setting all $F_y=\pi(y)$ at once. The paper says the difference matters only "in certain multi-agent dilemmas."

A sketch of why (my construction, not the paper's): two copies of the same algorithm receive different inputs, $y_1$ and $y_2$, and are rewarded only if their actions match some joint pattern, say if both choose the same arbitrary label.

- A-FDT at $y_1$ optimizes against its *prior* about $F_{y_2}$. If that prior is symmetric, ties and miscoordination are possible.
- P-FDT optimizes jointly and coordinates.

In single-agent problems where only one node's value is relevant, the two theories agree. Readers should therefore apply A-FDT as the paper's Eq. (4) states it, and treat coordination across different inputs as a known limitation that P-FDT is designed to address.

### (e) Ties and zero-probability actions

Eq. (4) is silent on ties. Unlike EDT, it has no zero-probability problem: interventions are defined even when the prior on an action is 0, which is why A-FDT escapes the paper's cosmic-ray trap. A tie-breaking convention has to be added. Whatever convention is chosen should be one that predictors can know, since it is part of the function being predicted.

## 8. Philosophical motivation, briefly

The paper's case for A-FDT rests mainly on "the argument from utility": in "fair" problems, where the outcome depends only on the agent's behavior in the problem at hand, A-FDT agents end up richer. Two supporting arguments come with it:

- **Precommitment.** A-FDT agents "act as they would have precommitted to act," without needing commitment devices.
- **Value of information.** They do not assign negative value to information.

The paper also neutralizes the dominance objection. It argues that "every method for constructing hypotheticals gives rise to its own notion of dominance," and that there is an A-FDT dominance notion under which A-FDT never chooses a dominated act. Against the charge that A-FDT agents believe they control the past, it replies that a deterministic CDT agent equally "imagines" varying a token that cannot vary, so neither theory is better placed on the metaphysics of control.

Two claims remain open by the authors' own account: that A-FDT is "reflectively stable in fair problems," and that no fair dilemma defeats it. Their notion of fairness is not formalized. Footnote 15 notes that a game punishing anyone who acts like a copy of Fiona is intuitively unfair, but no general criterion is given.

## 9. Conclusion

A-FDT is CDT-style surgery moved from the physical act to the logical output of one's own decision procedure on one's actual input, with observations used to select that input rather than to condition on. To apply it:

1. Model the world.
2. Add a node for your algorithm's output on each possible input, with edges to everything that faithfully computes or predicts it.
3. Intervene on the node for your actual input.
4. Leave the other nodes at their priors and do not condition on what you saw.
5. Maximize expected utility.

Done this way, A-FDT one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays in Parfit's hitchhiker problem, and refuses blackmail below a computable error threshold. Its outputs are only as good as the dependence graph it is given. Constructing that graph, interpreting the counterpossibles it encodes, and extending the theory to policy-level coordination (P-FDT) are the questions the source itself leaves open.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2. Cited works within it include Gibbard & Harper (1978), Joyce (1999), and Pearl (2000).