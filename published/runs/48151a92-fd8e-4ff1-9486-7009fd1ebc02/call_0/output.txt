# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. Naming and scope

The paper by Yudkowsky and Soares calls its theory "functional decision theory" (FDT). In this essay, **A-FDT** is the procedure given by Equation (4) of Section 5, in which the agent selects an *action*. The paper notes in footnotes 7 and 16 that its "preferred formalization" has the agent select a *policy*, a map from observations to actions, and that the difference "only matters in multi-agent dilemmas so far as we can tell." I treat A-FDT as the action-level theory the paper actually writes down and analyses. I label the policy variant as a separate theory and set it aside, though I come back to it in Section 5.

I also separate three kinds of claim: what the paper says, what follows from it by computation, and what I propose to fill gaps. Anything of the third kind is marked "my proposal."

## 2. The definition

All the theories compared in the paper are expected-utility theories. Following Gibbard and Harper, the paper writes

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $\hookrightarrow$ is a "decision hypothetical" connective. Citing Joyce's representation theorem, the paper treats the interpretation of $\hookrightarrow$ as the free parameter that distinguishes the theories. Joyce says they are not "competing theories of value" but disagree "about the epistemic perspective from which actions are to be evaluated."

The three formal equations are:

- **EDT (Eq. 2):** $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$, where $V = \mathcal U(\mathrm{Outcome})$.
- **CDT (Eq. 3):** $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$, which requires a causal graph $G$.
- **A-FDT (Eq. 4):**

$$\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x) = a\big)\Big)\ }$$

The ingredients are these.

**The world-model $(P,G)$.** $P$ is a probability distribution over variables. $G$ is a graph that records not only causal structure but also *subjunctive dependence*. The paper puts it this way: "FDT can require that $P$ come augmented with information about the logical, mathematical, computational, causal, etc. structure of the world more broadly." Some variables in $P$ stand for outputs of mathematical functions, like a variable for the value of $6288+1048$.

**The intervention node.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents the output of the A-FDT algorithm itself when run on this model and these observations. The underlines indicate dequoting: the variable's name depends on the model, as $Z\underline{x}$ with $x=3$ means $Z3$. This is self-referential, and the paper says the self-reference is harmless: "an FDT agent does not need to know the *value* of $\mathrm{FDT}(M,x)$ in order to have a variable representing that value." Kleene's second recursion theorem (quining) shows that such self-representing structures exist.

**The $\mathrm{do}$ operator.** This is Pearl's operator, reused unchanged. Setting the node to $a$ updates everything downstream of it in $G$ and leaves everything else untouched. The difference from CDT is that the *edges out of the node* encode subjunctive dependence, not just physical causation. In the paper's phrasing, A-FDT is to subjunctive dependence as CDT is to causal dependence.

The paper identifies exactly two differences from Eq. (3):

1. CDT intervenes on a node for the *physical act*. A-FDT intervenes on a node for the *output of the decision procedure*, a logical fact. In Peirce's terms, CDT intervenes on the token and A-FDT on the type.
2. CDT handles observations by *conditioning*: $\mathrm{Obs}=x$ becomes $\mathrm{Obs}=y$. A-FDT handles observations by *changing which node is intervened on*: $\mathrm{fdt}(\ldots,\underline x)$ becomes $\mathrm{fdt}(\ldots,\underline y)$.

The second difference is the less obvious one, and it explains the theory's behavior in transparent problems (Section 4).

## 3. What the intervention preserves

A-FDT is a *surgery* theory. It does not condition, as EDT does, and it does not hold the world fixed apart from physical effects, as CDT does. When evaluating $a$, A-FDT changes the output of the decision function and propagates the change to everything that depends on that function: the agent's own action, a predictor's prediction, a twin's choice. Everything else stays as it was: the lesion, the termites, the past state of the world that is not a function of the agent's algorithm.

The paper separates three kinds of relationship:

- **Statistical correlation** alone does not entail subjunctive dependence. Two pink calculators in Paris and Tokyo are correlated in color, but "if the scribe had bought a green calculator instead, the one in Tokyo would still be pink." A-FDT breaks such correlations.
- **Causal dependence** is a special case of subjunctive dependence. The scribe's note depends on the calculator's output in both senses.
- **Subjunctive dependence** proper arises when two systems compute the same function, or when one contains an accurate model of the other. A predictor with an accurate model of the agent has, in the paper's phrase, a "twin" inside its mind. If the model is imperfect or the agent is stochastic, the dependence is weakened but not eliminated, as with two calculators that may suffer cosmic-ray errors.

When $G$ is such that every correlation between $\mathrm{Act}$ and other variables is caused by $\mathrm{Act}$ (except possibly the $\mathrm{fdt}$ node itself), the paper notes that

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)],$$

so all three theories agree. They diverge only when events correlate with the action without being caused by it, which is typically the work of predictors and copies.

The paper's summary: CDT hypotheticals respect too few action–environment correlations and EDT hypotheticals respect too many. A-FDT keeps the correlations that are logically or subjunctively necessary, and drops the rest.

## 4. Applying A-FDT: worked cases

The recipe is as follows.

1. Build $P$ and $G$, with an $\mathrm{fdt}$ node for each observation the agent might receive.
2. Mark which variables depend on which $\mathrm{fdt}$ node.
3. For each action $a$, set the relevant node to $a$, propagate, and compute $\mathbb E[V]$.
4. Output the best $a$.

### Newcomb's problem

Variables: $\mathrm{fdt}$ (the decision function), $\mathrm{Act}$, $\mathrm{Prediction}$, $\mathrm{Accurate}$ (0.99 / 0.01), $\mathrm{Box\,B}$. Both $\mathrm{Act}$ and $\mathrm{Prediction}$ are children of $\mathrm{fdt}$.

- $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$: $\mathrm{Act}$ is onebox with probability 1, and $P(\text{full}) = 0.99$. So $\mathbb E[V] = 0.99\times\$1{,}000{,}000 = \$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$: $P(\text{full}) = 0.01$. So $\mathbb E[V] = 0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = \$11{,}000$.

A-FDT one-boxes. This agrees with the paper's figures. The paper's EDT figure of \$999,000 for one-boxing looks like a slip. By the same computation, EDT's conditional expectation is \$990,000.

The paper stresses what this does *not* require: "Nowhere in Fiona's reasoning above is there any appeal to a belief in retrocausal physics." The agent merely refuses to imagine her action changing while the output of the function being predicted does not. The objection that she should two-box once she is nearly sure the box is full is answered by the same point. Asked what would happen if she two-boxed, she answers by intervening on the node, so the box is probably empty in that hypothetical.

### Smoking lesion

Here the graph differs, and this shows that A-FDT is not a rule of "always one-box." The lesion causes both the preference for smoking and cancer. It does not depend on the decision function, so $\mathrm{Cancer}$ has no edge from the $\mathrm{fdt}$ node.

The paper's formalization takes an extra step, because the lesion changes the agent's utility function. There are two models, $P_S$ (valuing smoking) and $P_R$ (valuing refraining), and so two nodes, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$. The agent does not know which one is driving her action, and $\mathrm{Act}$ is a function of the lesion and these two nodes. Intervening on $\mathrm{fdt}(P_S,G)$ leaves $P(\text{lesion})=p$ untouched. Then

$$\mathbb E[V\mid \mathrm{do}(\text{smoke})] - \mathbb E[V\mid \mathrm{do}(\text{refrain})] = p\cdot\$1{,}000 > 0,$$

so A-FDT smokes. The paper admits that this setup is contrived. It also points out that the problem is unfair to EDT, since in a population of EDT agents nobody smokes and the correlation would vanish, and it recommends that philosophers abandon the problem. For our purposes the problem shows that one criterion can one-box and smoke, because the dependency graph, and only the dependency graph, differs.

### Transparent Newcomb (and Parfit's hitchhiker)

The agent sees whether box B is full. A-FDT does not condition on the observation. It chooses which node it intervenes on, $\mathrm{fdt}(\cdot,\textit{full})$ here. $\mathrm{Act}$ is governed by $\mathrm{fdt}(\cdot,\textit{full})$ if the prediction was "one-box" (box full) and by $\mathrm{fdt}(\cdot,\textit{empty})$ otherwise. The predictor depends on the node $\mathrm{fdt}(\cdot,\textit{full})$. Let $q$ be the agent's credence that she two-boxes on seeing an empty box.

- Set the node to *onebox*: with probability 0.99, the box is full and she one-boxes (\$1,000,000). Otherwise the box is empty and she acts per $q$. So $\mathbb E[V] = \$990{,}000 + 0.01\,q\cdot\$1{,}000$.
- Set it to *twobox*: with probability 0.01 the box is full and she gets \$1,001,000, and with probability 0.99 the box is empty and she gets \$1,000 with probability $q$. So $\mathbb E[V] = \$10{,}010 + q\cdot\$990$. (The paper prints "\$110,00"; this is my recomputation.)

For any $q\in[0,1]$, one-boxing wins. In the imagined two-boxing world she "envisions a scenario where she instead (with high probability) sees that the box is empty." The paper treats Parfit's hitchhiker as structurally the same problem: paying in the city corresponds to one-boxing against two full boxes.

*A note on the formulas.* The paper's text writes the transparent-case objective as $\mathbb E(V\mid \mathrm{do}(\mathrm{fdt}(\ldots,\textit{full})=a,\ \mathrm{Obs}=\textit{full}))$, but its computations average over the predictor's accuracy without conditioning on a full box. Eq. (4) itself contains no $\mathrm{Obs}$ term. I follow the computations and Eq. (4): the observation selects the node and does not condition the model.

### Blackmail

*XOR blackmail.* Infestation is upstream of the predictor and does not depend on the decision function. The decision function determines whether the letter is sent, and what she does on receiving it. Setting $\mathrm{fdt}(\cdot,\textit{letter})$ to *pay* changes the probability of getting a letter but not the probability of termites. Refusing changes whether the letter exists, not whether termites do. A-FDT refuses. EDT pays, because conditioning on paying "sends her probability on termites to 0."

*Mechanical blackmail.* Paying yields blackmail (probability about 1) and a \$1,000 loss. Refusing yields a loss of \$1,000,000 *if* blackmailed, but a blackmail probability near 0. With a blackmailer who wrongly predicts payment with probability $\epsilon$, the comparison is

$$\text{pay: } \$1{,}000 \quad\text{vs.}\quad \text{refuse: } \epsilon\cdot\$1{,}000{,}000 .$$

Break-even is $\epsilon = 0.1\%$. The paper's $\epsilon=0.0009$ gives expected loss \$900 when refusing, so A-FDT refuses. The paper says it pays at "0.011%". By my arithmetic that figure gives \$110 for refusing, so A-FDT would still refuse. The intended figure is probably 1.1%, which gives \$11,000, so A-FDT pays. Either way the lesson is that A-FDT weighs the hypothetical in which the function outputs "refuse," including the consequence that the letter probably never arrives, against the hypothetical in which it outputs "pay."

The paper adds that A-FDT "would not have a desire to self-modify and temporarily follow CDT" on holding the letter, because by its own hypotheticals being a payer makes one a blackmail target.

### Death in Damascus

The agent knows Death's book was written from a perfect prediction of her decision function. Death's location is a child of the $\mathrm{fdt}$ node. Staying yields certain death at cost \$0, and fleeing yields certain death plus the \$1,000 cost. A-FDT stays. CDT treats Death's location as independent of the action, and that produces the unstable "flee, no stay, no flee" dynamics the paper describes, including the absurd refusal to pay \$1 for a truly random coin that would give a 50% chance of survival.

### The cosmic ray problem

If the agent takes \$1 with high probability, then "whenever she takes \$100" EDT reads this as evidence of a cosmic ray and a \$1,000 hospital bill. A-FDT intervenes on the decision node, which has no edge to the ray-induced flip, and takes the \$100. (This is the paper's account; the \$900 net loss figure is its own.)

## 5. Where Eq. (4) underdetermines the answer

The paper is candid that A-FDT "rests on shakier philosophical foundations than" the CDT equation. These are the main gaps, with what the source supplies and what I propose.

**(a) Where $G$ comes from.** The paper says: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem." In footnote 9 it says it "require[s] that the relevant logical dependency structure be given as an input." So A-FDT, like CDT, is conditional on a graph supplied from outside.

*My proposal for practitioners (an operational heuristic, not the paper's).* For each variable $Z$ in the problem, ask the *swap test*: if the function this agent is computing (with these inputs) returned a different value, would $Z$ have been different?

- Yes, because $Z$ is computed by a predictor, copy, or simulation of the agent: add an edge from the $\mathrm{fdt}$ node to $Z$. This is the Newcomb predictor, the twin, Death's book.
- No, because $Z$ is a fixed fact of the environment that merely correlates with the output: do not add an edge. This is the lesion, the termites.
- The dependency passes through a model whose accuracy is itself uncertain: add an edge from an accuracy noise node, as in the paper's $\mathrm{Accurate}$ variable.

This test is only as reliable as one's story about how the predictor works. The paper's "fair problem" idea guides it. The test is meant to be applied to dependence on the agent's *output*, not on the agent's implementation details.

**(b) Counterpossibles.** If the function deterministically outputs $a_1$, then "it outputs $a_2$" is, per the paper, a counterpossible, "any more than there are possible worlds where $6288+1048\ne7336$." The paper concedes that "[t]his lack [of an account] is the main drawback of FDT relative to CDT." Its response is that the difficulty is "technical rather than philosophical," that human mathematicians reason under logical uncertainty, and that the agent needs only narrow counterpossibles ("How would this predictor's prediction of my action change if the FDT algorithm had a different output?"). The paper also considers a variant that varies the *function* the agent implements, not its output, and shows it faces the same problem, since predictors of the original function must be made to predict as if it behaved differently. Using $\mathrm{do}$ on a graph is a way of sidestepping the issue: the $\mathrm{do}$ operator does not ask how the counterpossible arises, only which variables move.

**(c) Priors on the other nodes.** In the transparent case, the value of $\mathrm{fdt}(\cdot,\textit{empty})$ was left as an unspecified $q$, and the paper notes the result is insensitive to it in these examples. In general it need not be. *My proposal:* assign these credences by running A-FDT itself on the other observations. That is a fixed-point construction, and the paper does not claim it is always well-defined. It is the sense in which the action-level theory behaves like a policy: a per-observation computation that implicitly assumes consistent values for the others.

**(d) Actions versus policies.** The paper says the action/policy distinction matters only in multi-agent dilemmas. A policy variant would intervene on the whole observation-to-action map at once. A-FDT as written makes no commitment on situations where one observation's best action depends on how *other* observations are answered in ways not captured by those nodes' priors. In such cases I would defer to the paper's preferred policy formulation, but I flag that the paper does not work out an example.

**(e) Fairness.** The paper claims A-FDT does best on "fair" problems, where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." It concedes that it has no formal criterion. Footnote 15 gives an example: a problem that punishes anyone who acts like a copy of A-FDT's agent is unfair to A-FDT, and the analogous problem for CDT is hard to define. The paper's own list of what it can't yet guarantee is brief: "We do not yet know whether FDT is optimal among decision theories, or even (on a formal level) what optimality consists in."

## 6. Why the theory is supposed to be right

The paper's main defense is empirical in spirit: the *argument from utility*. A-FDT agents tend to leave Newcomb's problem and Parfit's desert richer, and they do better than CDT and EDT agents in blackmail. A decision theory that predictably does worse than another in fair problems is a poor candidate for the theory of rational choice. The paper supports this with two further arguments:

- *Precommitment:* A-FDT acts as it would have precommitted to act, without paying for binding mechanisms.
- *Value of information:* because A-FDT's hypotheticals are chosen before the observation selects a node, it never expects information to hurt it. EDT agents will pay to avoid seeing the box.

The dominance argument for two-boxing is rejected as question-begging. Dominance depends on a method of constructing hypotheticals, and every such method yields its own dominance relation. EDT's yields "refrain" in the smoking lesion, CDT's yields "two-box," and A-FDT's yields "one-box," because with the subjunctive dependency held fixed, switching from one box to two makes the agent worse off.

A final objection is that A-FDT agents are deluded about causality. The paper's reply is a parity argument. A deterministic CDT agent "imagines" that her physical action could differ, and an A-FDT agent imagines that her function's output could differ. Both are useful fictions, and any principled objection to "controlling" a decision type would equally remove the control CDT claims over a decision token.

## 7. Conclusion

A-FDT, as given by Eq. (4), is a small modification of CDT with large consequences. It keeps expected-utility maximization and Pearl-style surgery, but moves the intervention from the physical act to the output of the decision function. Observations select which node is intervened on, instead of conditioning the model. Where a graph correctly records the dependence of predictors, twins, and copies on that output, one rule one-boxes in Newcomb's problem, smokes in the smoking lesion, pays in Parfit's hitchhiker, refuses blackmail, and stays in Damascus.

The theory's weak points are those the paper itself identifies, and I have tried to say honestly where I add to it. Eq. (4) presupposes a graph $G$ of subjunctive dependencies, and nothing yet plays the role for it that Pearl's methodology plays for causal structure. It also presupposes some way of reasoning about counterpossibles, and about the agent's credences concerning her own output in other situations. The swap test and the fixed-point reading of the priors are my attempts at operational interpretations. They are reasonable, but they go beyond the source. A user of A-FDT must supply the graph and be prepared to defend it, and the quality of the decisions is no better than the quality of that graph.