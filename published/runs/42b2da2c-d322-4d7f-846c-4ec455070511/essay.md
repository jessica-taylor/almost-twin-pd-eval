# Action Functional Decision Theory (A-FDT): Deciding as the Output of a Function

## 1. What is being explained, and under what name

Yudkowsky and Soares (2017) introduce *functional decision theory*. Their slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper gives one explicit decision rule, Equation (4) in Section 5. That rule selects a single **action** given the current observation history. A footnote records that the authors' preferred formalization instead selects a **policy**: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

This essay concerns the action-selecting rule of Equation (4). I call it **A-FDT**. I call the footnoted alternative **policy-selecting FDT**. The paper itself writes "FDT" throughout, so quotations below say "FDT" even where they describe what I call A-FDT. The two other theories that appear are **causal decision theory (CDT)** and **evidential decision theory (EDT)**.

## 2. Common skeleton: expected utility with a hypothetical connective

The paper presents EDT, CDT and A-FDT as variants of one template. An agent with observation history $x$ chooses an action $a$ from a finite set $\mathcal A$ to maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

Here $P(a\hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the free parameter that separates the theories. Write $V=\mathcal U(\textsc{Outcome})$.

- **EDT** conditions:
$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a).\tag{2}$$
- **CDT** applies Pearl's intervention to the physical action node in a causal graph $G$:
$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x).\tag{3}$$

The authors describe each formula as a "hypothetical" construction. The agent copies her world-model, performs a surgery, and reads off the expected value. A hypothetical is "a decision-theoretic instrument constructed from beliefs," not a belief and not a metaphysical possible world.

## 3. The definition of A-FDT

A-FDT keeps CDT's machinery but moves the point of surgery. The agent's model $P$ contains variables for the outputs of mathematical functions, including a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ that stands for *the output of this very decision procedure on these very inputs*. The underlines mark dequotation: the variable's name is built from the model it lives in. The authors note that this self-reference is harmless. The agent needs a *variable* for her output, not its *value*, and Kleene's recursion theorem ("quining") shows such self-representing structures exist. The graph $G$ now encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." Equation (4) reads:

$$\boxed{\;\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V\;\middle|\;\mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;}\tag{4}$$

I abbreviate $F_x:=\textsc{fdt}(\underline P,\underline G,\underline x)$. The source identifies two differences from (3):

1. **Locus of intervention.** CDT intervenes on the *token*, the physical act. A-FDT intervenes on the *type*, the logical output of the decision function. Every node that is a child of $F_x$ in $G$ changes in the hypothetical, including predictions, simulations and twins. Everything else is held fixed.
2. **Treatment of observations.** In (4), $x$ is not conditioned on. It only selects *which* node is intervened upon. When the history changes from $x$ to $y$, A-FDT switches from intervening on $F_x$ to intervening on $F_y$.

The paper does not claim that (4) is the only formalization. It calls the $\mathtt{do}$-based version "sufficient for present purposes" but on "shakier philosophical foundations" than (3). The ideal would be an operator $\mathtt{true}(\phi)$ that updates beliefs on a logical counterpossible. No such operator is available, so the dependency structure is supplied as an input $G$, much as CDT receives its causal graph as an input.

### Subjunctive dependence: which edges leave $F_x$

The intended semantics of $G$ is *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper draws three distinctions:

- A twin running the same reasoning, or a predictor holding an accurate model of the agent, depends subjunctively on $F_x$. This is the "two calculators computing $6288+1048$" picture.
- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation does not count. A lesion that correlates with smoking does not evaluate the agent's decision function, so no edge runs from $F_x$ to it.

The governing requirement, in the authors' words, is that the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

A corollary stated in the source: if every correlation between the action and other variables is caused by the action, the three theories agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(F=a)].$$

They come apart only when something else, such as a predictor, a twin or a simulation, tracks the agent's decision function.

## 4. Worked examples

All dollar figures are utilities, as in the paper.

### Twin prisoner's dilemma

One node $F$ has two children, my act and my twin's act. Under $\mathtt{do}(F=\textit{cooperate})$ both cooperate, worth \$1,000,000. Under $\mathtt{do}(F=\textit{defect})$ both defect, worth \$1,000. A-FDT cooperates. CDT intervenes on my act alone, holds the twin fixed, finds that defection dominates, and defects.

### Newcomb's problem (99% accurate predictor)

The graph is $F\to\textsc{Act}$, $F\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, and $\textsc{Prediction}\to\textsc{Box B}$.

- One-box: $0.99(1{,}000{,}000)+0.01(0)=990{,}000$.
- Two-box: $0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000$.

A-FDT one-boxes. The prior on $F$ is irrelevant because $\mathtt{do}$ overrides it. This answers the objection the paper considers: "won't she decide to take two boxes" once she is nearly certain she one-boxes? She will not. Unlike EDT, A-FDT can evaluate an action it assigns near-zero prior probability, because intervention does not require conditioning on a probability-zero event.

*A small correction to the source.* The paper's EDT computation reports \$999,000 for one-boxing. The same model gives \$990,000, as in its later computation for the A-FDT agent. The verdict is unaffected.

### Smoking lesion

The authors formalize the lesion as also fixing the agent's utility function:

- $\mathcal U_S$ for the lesioned, who like smoking;
- $\mathcal U_R$ for the unlesioned, who value smoking at $-\$1$.

Two decision nodes exist, $F_S=\textsc{fdt}(\underline{P_S},\underline G)$ and $F_R=\textsc{fdt}(\underline{P_R},\underline G)$. The action is $\textsc{Act}=F_S$ if lesioned and $F_R$ otherwise. Crucially, there is *no* edge from either node to $\textsc{Cancer}$. With $P(\textit{lesion})=p$ and $q=P(F_R=\textit{smoke})$, intervening on $F_S$ gives:

$$\text{smoke: } p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),$$
$$\text{refrain: } p(10{,}000)+(1-p)(990{,}000+1{,}000q).$$

Smoking wins by $1{,}000p$. A single rule therefore both one-boxes and smokes, which Gibbard and Harper had argued no coherent rule could do. The structural difference between the two cases is entirely in $G$: the predictor is a child of $F$, while the lesion is a parent of $F$.

### Transparent Newcomb and Parfit's hitchhiker

In the transparent Newcomb problem, the agent sees box B full. Act is $F_{\textit{full}}$ if the prediction was "one-box", else $F_{\textit{empty}}$. The prediction depends on $F_{\textit{full}}$ and on accuracy. Let $q=P(F_{\textit{empty}}=\textit{two-box})$.

- $\mathtt{do}(F_{\textit{full}}=\textit{one-box})$: $0.99(1{,}000{,}000)+0.01(1{,}000q)=990{,}000+10q$.
- $\mathtt{do}(F_{\textit{full}}=\textit{two-box})$: $0.01(1{,}001{,}000)+0.99(1{,}000q)=10{,}010+990q$.

The source prints the second as "\$110,00 + q·\$990", evidently a slip for $10{,}010+990q$. A-FDT one-boxes *while looking at a full box*. In the two-boxing hypothetical, she would most likely have been shown an empty box.

Parfit's hitchhiker has the same structure. Intervening on $F_{\textit{city}}$:

- pay: $0.99(-1{,}000)+0.01(-1{,}000{,}000)=-10{,}990$;
- refuse: $0.99(-1{,}000{,}000)=-990{,}000$.

A-FDT pays.

### XOR blackmail (infallible predictor, prior $p$ of termites)

The letter is sent iff (no termites ∧ the agent would pay) or (termites ∧ she would not). Termites are a parent of the predictor, not a child of $F_{\textit{letter}}$.

- $\mathtt{do}(F_{\textit{letter}}=\textit{pay})$: $-10^6p-1{,}000(1-p)$.
- $\mathtt{do}(F_{\textit{letter}}=\textit{refuse})$: $-10^6p$.

A-FDT refuses, and so does CDT. The hypotheticals differ, though. In the A-FDT "pay" hypothetical, she would not have received the letter at all. In the CDT hypothetical, the infallible predictor erred. EDT pays, since conditioning on paying sends $P(\textit{termites})$ to 0.

### Mechanical blackmail with an error rate

The blackmailer runs the damaging program iff she predicts payment, but wrongly predicts payment with probability $\varepsilon$. Under A-FDT:

- paying yields $-1{,}000$ (blackmailed, pays);
- refusing yields $-10^6\varepsilon$.

So A-FDT refuses iff $\varepsilon<10^{-3}$. The source's example $\varepsilon=0.0009$ gives refusal with an expected loss of \$900, which matches. Its contrasting case, "0.011%", would still give refusal by this arithmetic (expected loss \$110). The intended figure was presumably 0.11%, which lies above the threshold. The qualitative point stands: A-FDT pays only when being the kind of agent that refuses is too risky.

### Death in Damascus (perfect predictor)

Death's location is a child of $F$.

- Stay: die, value $0$.
- Flee: die, value $-1{,}000$.

A-FDT stays, with no oscillation and no ratification. The following extension is my own calculation; the source treats it only for CDT. Offered a truly random coin for \$1, A-FDT values it at $0.5\cdot 10^6-1$ and buys it. The CDT agent declines the coin, because it already acts as if its survival chance is at least 0.5.

## 5. What the source leaves open, and how one might operationalize it

### 5.1 Building $G$

The source is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) works *given* $G$. The paper does not say how to obtain $G$.

**My operational proposal** follows the paper's informal criterion as closely as possible:

- **(G1) Edges from $F_x$.** Draw an edge $F_x\to Z$ iff the mechanism producing $Z$ evaluates, simulates, or reliably reasons about the agent's decision function *on input $x$*. Model imperfect reliability with exogenous noise parents, such as $\textsc{Accurate}$ or $\textsc{Luck}$, rather than by weakening the edge.
- **(G2) Ordinary causation.** Draw ordinary causal edges as CDT would. The physical act is a deterministic child of the $F_y$ nodes, with a selector determined by whatever fixes which observation the agent actually receives.
- **(G3) Mere correlates.** Variables correlated with the act only through common causes (lesions, genes, upbringing) get *no* edge from any $F_x$. They are parents of the selector or of the utility function, as in the lesion model.

This reproduces every graph in the paper. It leaves genuinely hard cases undecided. Examples are an agent running a *similar* but not identical algorithm, or a predictor using coarse statistics about agents of the agent's "type." Treating such cases requires a notion of partial or approximate logical dependence, which the paper does not supply.

### 5.2 Beliefs about the other decision nodes

Several computations contain the probability $q$ of what the agent does at a *non-intervened* node, such as $F_{\textit{empty}}$ or $F_R$. The source remarks that "it doesn't matter" in its examples and that the "correct" value is obvious. This is true there only because $q$ enters both hypotheticals with small or nearly equal weight. In general, Equation (4) optimizes one node while holding the distribution over the others fixed. So A-FDT's output can depend on those beliefs.

**My proposal** is to require self-consistency. Give each non-intervened $F_y$ the action that A-FDT itself outputs at $y$, and iterate to a fixed point. This mirrors the paper's remark that a predictor "following this very chain of reasoning" knows the agent's outputs. A fixed point is an equilibrium across one's own information states. It need not be unique, and it need not be optimal.

**An illustration of my own.** It shows concretely why the action-versus-policy distinction can bite. A fair coin shows the agent L or R. A predictor simulating both $F_L$ and $F_R$ pays:

- 10 if both output $a$;
- 6 if both output $b$;
- 0 otherwise.

Suppose the agent believes $F_R=b$. At L, A-FDT compares 0 (for $a$) with 6 (for $b$) and chooses $b$. The profile $(b,b)$ is self-consistent but worse than $(a,a)$. Policy-selecting FDT maximizes over the whole map $\{L,R\}\to\{a,b\}$ and picks $(a,a)$. This is the kind of case the footnote presumably has in mind when it says the policy formulation "makes a difference in certain multi-agent dilemmas."

For A-FDT, the reasonable reading is that its verdicts are well-defined relative to beliefs about one's other outputs. Where several self-consistent assignments exist, (4) alone does not choose among them.

### 5.3 Does A-FDT condition on $x$?

Equation (4) contains no conditioning on $\textsc{Obs}=x$. However, the paper's transparent-Newcomb display writes $\mathbb E(V\mid \mathtt{do}(F_{\textit{full}}=a,\textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. Its actual computation is inconsistent with conditioning, because it sums over the branch where the box is empty. The prose is unambiguous: Fiona "does not react to observations by conditioning her distribution."

A further footnote warns that a theory which both conditions and switches the node ("Timeless Decision Theory") suffers a harmful "double update." I therefore read (4) literally:

- $P$ is the agent's model *before* the observations relevant to the problem;
- $x$ enters only through the index of the intervened node.

What counts as "before" is itself unspecified. The paper's models build in background knowledge, such as the problem description, but not the decision-relevant observation. In practice one must choose a reference prior. I suggest the beliefs held when the agent could first have been modeled by the relevant predictors.

### 5.4 Counterpossibles

If $F_x=a_1$ is in fact true, then $\mathtt{do}(F_x=a_2)$ asks what would follow if a mathematical fact were otherwise. The source concedes this is A-FDT's "main drawback relative to CDT." It argues that the difficulty is "technical rather than philosophical," and points out that CDT faces the parallel problem of imagining a deterministic agent's token act differing. In Equation (4), $G$ quarantines the problem: the graph stipulates what changes. The account is complete relative to $G$, and only relative to $G$.

## 6. Applying A-FDT to an unfamiliar case: a procedure

1. **List the agent's possible information states.** Create a node $F_y$ for each relevant one, and identify the actual state $x$.
2. **Build the world-model $(P,G)$.**
   - Add ordinary causal structure.
   - Add edges from $F_y$ to every predictor, simulator, twin, or copy that computes the agent's output on input $y$ (G1).
   - Model mere correlates as non-descendants of every $F_y$ (G3).
   - Make the act a selector over the $F_y$ (G2).
3. **Do not condition on $x$.**
4. **Assign beliefs to the non-intervened $F_y$.** Ideally use the self-consistent assignment, and check whether the verdict is robust to it.
5. **Evaluate each candidate action.** For each $a$, compute $\mathbb E(V\mid \mathtt{do}(F_x=a))$ by propagating along $G$, including the possibility that you would have observed something other than $x$.
6. **Output the arg max.**

If no node other than the act descends from $F_x$, step 5 reduces to CDT. If, in addition, all correlations with the act are causal, it also coincides with EDT.

## 7. Philosophical motivation (the source's arguments)

The paper's case rests mainly on **utility achieved** in what it calls "fair" problems. These are problems where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor qualifies: "she punishes *two-boxers*," not reasoning styles. The authors admit that this notion of fairness is not yet formalized. A footnote also shows the difficulty: an environment that punishes whoever matches a copy of the FDT agent always defeats that agent.

Further arguments in the source:

- **Precommitment.** A-FDT "act[s] as [it] would have precommitted to act," so it needs no binding devices. CDT and EDT agents would pay for such devices.
- **Value of information.** EDT can assign negative value to information, for example by paying to blindfold itself in transparent Newcomb. FDT agents, the authors say, "do not assign negative expected value to information."
- **Reflective stability.** CDT recommends self-modifying away from CDT. The authors claim FDT is "reflectively stable in fair problems."
- **Dominance is not neutral.** Every way of constructing hypotheticals induces its own dominance relation. Two-boxing "dominates" only under CDT counterfactuals. Under FDT counterfactuals, which hold subjunctive dependencies fixed, one-boxing is not dominated.

The diagnosis is symmetric:

- EDT's hypotheticals respect too many correlations. It cannot break the merely statistical ones, as the cosmic-ray problem shows.
- CDT's hypotheticals respect too few. It imagines perfect predictors failing exactly at the moment of its choice.
- A-FDT keeps exactly the correlations that run through the decision function.

How one weighs the source's arguments is a separate matter from understanding the rule. The defining move is precise in any case: change the type, not the token.

## 8. Conclusion

A-FDT is CDT with the surgery relocated. The agent intervenes on the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$ that represents her decision procedure's output on her actual input. She does not condition on that input. Everything subjunctively downstream of the node changes in the hypothetical: her act, her twin's act, a predictor's forecast, and even which observation she would have received.

Given a dependency graph, this single rule one-boxes, smokes, pays the driver, refuses blackmailers when their error rate is low, and does not flee Death. Three things the source leaves undetermined are where an applied A-FDT needs extra assumptions:

- how to build the dependency graph, which the paper calls its central open problem;
- how to set beliefs about one's own outputs at other inputs;
- how to choose the reference prior.

I have proposed edge rules (G1–G3), a self-consistency condition, and a literal non-conditioning reading of (4). I have also shown that A-FDT can settle into suboptimal self-consistent profiles that policy-selecting FDT avoids. This is the cost of selecting actions rather than policies.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.* Cambridge UP.
- Pearl, J. (2000). *Causality.* Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.