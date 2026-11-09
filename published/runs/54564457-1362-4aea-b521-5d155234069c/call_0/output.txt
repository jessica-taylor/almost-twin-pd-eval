# A-FDT: Choosing an Action by Intervening on a Function's Output

## 1. The question A-FDT asks

Standard expected-utility theories agree that a rational agent should choose the action that maximizes expected utility. They disagree about which hypothetical scenario an action should be evaluated in. Yudkowsky and Soares, following Joyce, cast this disagreement as a dispute about the "decision hypothetical" connective in

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Evidential decision theory (EDT) reads $a \hookrightarrow o$ as Bayesian conditioning. Causal decision theory (CDT) reads it as a Pearl-style causal intervention on the physical act. The theory examined here reads it as an intervention on the output of the agent's decision procedure, regarded as a fixed mathematical function.

In the paper's words, the agent asks "Which output of this very function would yield the best outcome?" The paper also uses a type–token contrast: CDT "intervenes on the token 'my action is $a$,' whereas an FDT agent intervenes on the *type*."

This essay concerns the specific formal version the paper gives as Equation (4) in Section 5. There the intervened node is set to an **action**. I call this version **A-FDT** (action functional decision theory). The paper's footnotes say the authors' preferred formalization instead "iterate[s] over *policies* (mappings from observations to actions)". I call that variant **policy-FDT** and treat it as a distinct theory. Throughout, I mark which claims belong to the source and which are my own reconstruction.

## 2. The formal definition

### 2.1 Ingredients

An A-FDT agent has a world-model $M = (P, G)$:

- $P$ is a probability distribution over variables. These include ordinary physical variables (box contents, termites, Death's appointment book). They also include **logical variables**: nodes representing the outputs of particular computations on particular inputs.
- $G$ is a graph. It tells the agent how changing the value of a logical variable propagates to the other variables. Formally it plays the role that a causal graph plays for CDT, but its edges encode *subjunctive dependence*, which the source treats as broader than causation (causal dependence is "a special case").
- $V := \mathcal U(\text{Outcome})$ is the utility variable.
- $x$ is the agent's observation history.

The key logical variable is
$$
F_x \;:=\; \textsc{fdt}(\underline{P}, \underline{G}, \underline{x}),
$$
which represents "what the A-FDT procedure outputs when run on inputs $(P, G, x)$." The underlines denote dequoting: the variable's *name* depends on the model and the observation. The source acknowledges the self-reference and dismisses it as harmless. One can hold a variable *representing* an unknown value without knowing the value, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist.

### 2.2 Equation (4)

The source's definition is:

$$
\mathrm{FDT}(P, G, x) \;:=\; \operatorname*{argmax}_{a \in \mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P, \underline G, \underline x) = a\big)\right). \tag{4}
$$

Compare CDT's Equation (3):
$$
\mathrm{CDT}(P,G,x) := \operatorname*{argmax}_{a} \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x\big).
$$

The source identifies exactly two differences:

1. **Point of intervention.** CDT intervenes on the physical node $\textsc{Act}$. A-FDT intervenes on the logical node $F_x$. Everything downstream of $F_x$ in $G$ changes with it. This includes the agent's own body, but also any predictor, simulation, or twin whose behavior subjunctively depends on that function. Everything else is held at its prior distribution.
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, "FDT responds to observation by changing which node it intervenes upon": on observing $y$ rather than $x$, it intervenes on $F_y$ rather than $F_x$.

The second point is the more surprising one. Observations still matter, because they select the intervention node. But the hypotheticals the agent constructs are allowed to contain worlds in which she would have observed something else.

### 2.3 Why a graph rather than a truth operator

The source first sketches an idealized version:
$$
\mathrm{FDT}^*(P,x) = \operatorname{argmax}_a \mathbb E\big(V \mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\big).
$$
Here $\mathtt{true}(\phi)$ would update $P$ to the scenario in which the logical sentence $\phi$ holds, even when $\phi$ is false. Because a deterministic function has only one output on a given input, all but one of these hypotheticals are **counterpossible**. The authors admit "it's not clear how to define a $\mathtt{true}$ operator."

Equation (4) avoids the problem by requiring $G$ as an input: "Given a graph $G$ that tells us how changing a logical variable affects all other variables, we can re-use Pearl's $\mathtt{do}$ operator." The cost is clear. A-FDT is only as well defined as the dependence graph supplied to it, and "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem."

## 3. A working recipe

The source applies Equation (4) case by case and gives no general procedure. The following recipe is my operationalization of what the worked examples do.

**Step 1: Enumerate the inputs at which your procedure is evaluated.** List every observation history $y$ at which some process in the world, whether your own brain, a predictor's model, or a twin, computes or tracks $\textsc{fdt}(P,G,y)$. Create a node $F_y$ for each.

**Step 2: Write structural equations.**
- The physical action is a function of the relevant $F$ nodes. Typically $\textsc{Act} = F_{\textsc{Obs}}$: whichever observation actually arises determines which function-output controls the body.
- A predictor of your behavior at input $y$ is a child of $F_y$. Its accuracy is modeled with an independent noise node.
- Merely statistical correlates of your action, such as a lesion or a cosmic-ray coincidence, are **not** children of any $F$ node.

**Step 3: Place priors on all exogenous nodes.** This includes the non-intervened $F_{y}$, $y \ne x$.

**Step 4: Intervene and evaluate.** For each $a\in\mathcal A$, compute $\mathbb E(V\mid \mathtt{do}(F_x=a))$, propagating only along $G$. Do not additionally condition on $\textsc{Obs}=x$.

**Step 5: Output the argmax.**

Step 4 needs a comment. In the transparent-Newcomb section, the source writes the target as "$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$" with an unmatched parenthesis. Read literally, that would condition on the observation. However, the computation actually performed there assigns weight $0.01$ to worlds in which box B is *empty*, which is impossible if one has conditioned on $\textsc{Obs}=\textit{full}$. Equation (4) itself contains no observation term. I therefore take the unconditioned reading as authoritative.

The source supports this reading elsewhere. Its draft footnote says that conditioning *and* moving the intervention point creates "a kind of 'double update' which proves harmful in practice."

## 4. Worked examples

All payoffs are in dollars-as-utility, and predictors are 99% accurate unless stated otherwise.

### 4.1 Newcomb's problem

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$. Both $\textsc{Act}$ and $\textsc{Box B}$ feed into $V$.

Under $\mathtt{do}(F=\textit{onebox})$, box B is full with probability $0.99$:
$$
\mathbb E V = 0.99\cdot 1{,}000{,}000 = 990{,}000.
$$
Under $\mathtt{do}(F=\textit{twobox})$:
$$
\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$
A-FDT one-boxes.

In the source's words, the agent "does not imagine that there can be a difference between her action today and a sufficiently competent prediction about that action yesterday." No retrocausation is involved. The predictor's box-filling and the agent's hand both depend on the same function's output, "much like the outputs of two perfectly functioning calculators calculating the same sum."

The **twin prisoner's dilemma** works the same way. The twin's choice is a child of the same $F$ node, so the comparison is $(C,C)\mapsto 1{,}000{,}000$ against $(D,D)\mapsto 1{,}000$, and A-FDT cooperates.

### 4.2 The smoking lesion

Here the correlation between smoking and cancer runs through a common cause, the lesion. It does not run through anyone's model of the agent's decision procedure, so $\textsc{Cancer}$ is not a child of any $F$ node.

The source's formalization is more delicate than one might expect. The lesion determines the agent's *utility function*, either $\mathcal U_S$ (likes smoking) or $\mathcal U_R$, and hence which of two functions, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls the action:
$$
\textsc{Act}(\textit{lesion},s,r)=s,\qquad \textsc{Act}(\textit{nolesion},s,r)=r.
$$

Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. The two hypotheticals therefore differ only in the lesioned branch, where smoking adds \$1,000. Smoking wins by $p\cdot 1{,}000$, and A-FDT smokes.

This is the paper's headline claim against Gibbard and Harper: a single rule that both one-boxes and smokes. The difference between the two problems lies entirely in $G$. The decision rule is the same.

### 4.3 Transparent Newcomb, and the role of the off-path node

Both boxes are visible. B is filled iff the predictor predicts one-boxing *upon seeing B full*. The agent sees B full.

The graph contains $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$ and selects which node drives $\textsc{Act}$. Let $q$ be the prior that $F_{\text{empty}}=\textit{twobox}$.

Under $\mathtt{do}(F_{\text{full}}=\textit{onebox})$:
- With probability $0.99$ (accurate), the box is full, the agent one-boxes, and she gets $1{,}000{,}000$.
- With probability $0.01$, the box is empty and $F_{\text{empty}}$ acts, giving $1{,}000q$ in expectation.

So
$$
\mathbb E V = 990{,}000 + 10q.
$$

Under $\mathtt{do}(F_{\text{full}}=\textit{twobox})$:
- With probability $0.99$, the box is empty and $F_{\text{empty}}$ acts.
- With probability $0.01$, the box is full and the agent two-boxes.

So
$$
\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000q = 10{,}010 + 990q.
$$

(The extracted source prints "$\$110,00$" here, which appears to be a typo for $10{,}010$.) For every $q\in[0,1]$, one-boxing wins. A-FDT leaves the visible \$1,000 behind, "even when the agent knows for sure that box B is full."

The source argues this is structurally identical to paying in **Parfit's hitchhiker**, where A-FDT pays the driver. The defense it offers rests on three arguments:
- **Precommitment:** CDT and EDT agents would precommit to exactly this behavior.
- **Value of information:** A-FDT never pays to avoid information.
- **Utility, which the authors treat as decisive:** "in 99 cases out of 100, *the kind of agent* that is inclined to conditionally give in to that temptation will actually find herself staring at an empty box B."

### 4.4 XOR blackmail and mechanical blackmail

In **XOR blackmail**, the letter is sent iff exactly one of these holds: (no termites and the agent will pay) or (termites and she will not pay). Intervening on $F_{\text{letter}}$ changes whether the letter arrives. It does not change whether there are termites, since termites are upstream and independent. Refusing therefore costs nothing in expectation, and A-FDT refuses.

EDT, by contrast, pays: conditional on paying, there are no termites. CDT also refuses, but for a different reason. The two theories produce the same action from different hypotheticals.

The **mechanical blackmail** case shows A-FDT diverging from both rivals. The blackmailer runs the damaging program only if she predicts the agent would pay. Given the letter in hand, EDT and CDT pay \$1,000 to avert a \$1,000,000 loss.

A-FDT evaluates two hypotheticals:
- $\mathtt{do}(F_{\text{blackmail}}=\textit{pay})$: she is almost surely blackmailed and pays, so $\mathbb E V\approx -1{,}000$.
- $\mathtt{do}(F_{\text{blackmail}}=\textit{refuse})$: she is almost never blackmailed. With error rate $\varepsilon$, $\mathbb E V = -\varepsilon\cdot 1{,}000{,}000$.

So A-FDT refuses iff $\varepsilon < 0.001$. The source's example $\varepsilon = 0.0009$ ("0.09%") gives $-900 > -1{,}000$, so she refuses. The source then states that at "0.011%" she pays. Taken literally that is below the threshold, so I suspect $0.11\%$ was intended. Either way, the threshold computation is what a reader should apply.

### 4.5 Death in Damascus

Death's appointment book is a child of $F$. Hence $\mathtt{do}(F=\textit{aleppo})$ places Death in Aleppo, and $\mathtt{do}(F=\textit{damascus})$ places Death in Damascus. Survival is impossible either way, and staying saves \$1,000, so A-FDT stays.

CDT is "unstable" in this problem because its hypotheticals hold Death's location fixed while varying the act. The source adds a sharper charge. A CDT agent who has settled on some belief state acts as if his survival chance were $\max(q,1-q)\ge 0.5$. He would therefore refuse to pay \$1 for a truly random coin that offers a genuine 50% chance of escape.

## 5. Dependence, counterfactuals, and dominance

The conceptual core of A-FDT is a three-way classification of correlations between the agent's action and the world:

| Correlation type | EDT | CDT | A-FDT |
|---|---|---|---|
| Causal (act → effect) | kept | kept | kept |
| Subjunctive (predictor/twin computes same function) | kept | **severed** | kept |
| Merely statistical (common cause, coincidence) | **kept** | severed | severed |

The source summarizes: "EDT respects too many action-environment correlations, while CDT respects too few."

The **cosmic ray problem** illustrates the bottom row. An EDT agent who almost always takes \$1 infers that taking \$100 signals a costly cosmic-ray strike, so she keeps taking \$1. CDT and A-FDT simply ignore the statistical link.

Dominance arguments are relativized accordingly. "Two-boxing dominates" holds only under CDT-style counterfactuals that vary the act while holding the function's output fixed. The source compares this to imagining a calculator output 3159 "holding constant the fact that $6288+1048=7336$." Under A-FDT's counterfactuals, which hold subjunctive dependencies fixed, two-boxing is dominated. The source's general moral is that "Every expected utility theory comes with its own notion of dominance," so dominance cannot neutrally adjudicate between theories.

The source also addresses the metaphysics of "control." A-FDT agents "suffer from no delusion; or, at least, they are no more deluded than their counterpart CDT agents." A deterministic CDT agent also has only one possible act and evaluates impossible alternatives. The difference is which impossibilities one entertains. CDT agents imagine that predictors err. A-FDT agents imagine that they made different observations.

## 6. Where Equation (4) underdetermines the answer

### 6.1 Constructing $G$

This is the open problem the source flags most prominently. Equation (4) presupposes that the agent can tell which processes compute or track her function. The examples rely on clean stipulations ("reliable predictor," "perfect twin"). In practice, three judgments are needed:

1. **Similarity.** Does an agent running a *similar but not identical* procedure count as a child of $F$?
2. **Accuracy.** How much noise should the edge carry?
3. **Directness.** Is a given correlation mediated by modeling, or only by a shared cause?

The source supplies a criterion, not an algorithm. Predictor-like processes "build an accurate model of the agent and reason about her behavior," whereas lesion-like ones do not.

My proposal is to treat partial similarity as a noisy edge. If another agent's procedure agrees with yours with probability $r$ in the relevant situation, model its output as a copy of $F$ passed through a channel with reliability $r$, exactly as the source models predictor accuracy. This reduces the similarity question to an estimate of $r$. It also makes A-FDT's verdicts continuous in $r$: in the twin dilemma, cooperation wins whenever the expected gain from correlated cooperation exceeds the defection bonus. That conclusion is an added assumption, not a claim the source makes.

### 6.2 Priors on off-path function nodes

Equation (4) intervenes on $F_x$ alone. Every other $F_y$ keeps its prior: $q$ in the transparent Newcomb and smoking lesion analyses, and the probability that the agent would pay in other branches. In the source's examples the verdict is independent of these priors, and the source notes what the "correct" values would be ($q=1$ and $q=0$ respectively).

That independence is a feature of those examples, not of A-FDT in general. My proposal is to require **self-consistency**: each $F_y$'s prior should concentrate on the value A-FDT would itself output at $y$. One finds these values as a fixed point, by solving the easy branches first or iterating.

### 6.3 A-FDT versus policy-FDT

The self-consistency requirement exposes the real gap between A-FDT and policy-FDT, which computes
$$
\pi^* = \operatorname*{argmax}_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),\qquad \text{then acts on } \pi^*(x).
$$
A-FDT optimizes one coordinate of the policy at a time. Policy-FDT optimizes all coordinates jointly. When the payoff depends jointly on outputs at several inputs, A-FDT can be stuck at a suboptimal fixed point.

Here is a toy case of my own construction. A predictor will place the agent in room $x$ or room $y$. It pays \$10 if it predicts she would choose $L$ in *both* rooms, \$5 if it predicts $R$ in both, and \$0 otherwise.

- The policy $(R,R)$ is self-consistent under A-FDT. At $x$, holding $F_y=R$, choosing $R$ yields 5 and choosing $L$ yields 0. The same holds at $y$.
- The policy $(L,L)$, worth 10, is also self-consistent.
- Policy-FDT selects $(L,L)$ directly.

The source acknowledges the distinction only in passing: it "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." My example involves a predictor, which is presumably the kind of second agent meant.

The operational lesson is this. When off-path priors do not affect the argmax, A-FDT is fully determinate. When they do, one must either fix them by an explicit self-consistency or equilibrium-selection rule, which is an additional assumption, or move to policy-FDT.

### 6.4 Fairness and scope

The source restricts its optimality claims to "fair problems," where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." A predictor that punishes *A-FDT agents as such* is unfair; one that punishes two-boxers is not.

The source admits that no formal fairness criterion exists. Its footnote gives a puzzle: a problem that punishes whoever matches a copy of the A-FDT agent defeats A-FDT, and it is unclear how to construct "the analogous" problem for rival theories. Applying A-FDT to an unfamiliar case therefore includes a judgment about whether the dependence on the agent runs through her *outputs*, which Equation (4) handles, or through her *procedure*, which falls outside its intended scope.

## 7. Claimed implications

The source draws several consequences from Equation (4):

- **No precommitment needed.** A-FDT agents "simply act as they would have precommitted to act." They one-box in the transparent Newcomb problem, pay the hitchhiker's driver, and refuse mechanical blackmail.
- **Non-negative value of information.** Unlike EDT, A-FDT never pays to blindfold itself.
- **Reflective stability "in fair problems."** A blackmailed A-FDT agent has no wish to self-modify into CDT. By her own hypotheticals, a decision function that connives to pay would be blackmailed more often.
- **Coordination.** Ten A-FDT voters whose decisions are subjunctively linked each pay the \$1,000 cost to vote and win the \$1,000,000 jointly. An agent can also "coordinate with herself over time," for example by going to the gym today because next week's identical decision depends on the same function.
- **Agreement with CDT and EDT in ordinary cases.** When every correlation between the act and the world is caused by the act,
  $$
  \mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)],
  $$
  so the three theories coincide. They diverge only where predictors, twins, or other modelers are present.
- **Within Joyce's framework.** A-FDT is an expected-utility theory satisfying Joyce's representation theorem. It differs from CDT only in "the constraints on how agents think about the hypothetical outcomes of their actions."

## 8. Conclusion

A-FDT, as given by Equation (4), takes Pearl's machinery and applies the $\mathtt{do}$ operator to a different node: the logical variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ rather than the physical act. Observations change *where* the agent intervenes, not *what she conditions on*.

To apply it to a new case:
1. Build a graph in which every process that computes or reliably predicts your procedure at input $y$ hangs off a node $F_y$, while merely statistical correlates do not.
2. Intervene on $F_x$ for your actual observation $x$, without further conditioning on $x$.
3. Choose the best resulting expected utility.

Run on the classic problems, this procedure one-boxes, smokes, pays the driver, and refuses blackmail.

The source leaves two things underdetermined, and the reader should know about both. The first and deepest is how to construct the dependence graph $G$, which is supplied as an input rather than derived. The second is how to set priors on off-path function nodes. In the source's examples these do not matter. In general they can, and then A-FDT needs either a self-consistency rule, as proposed above, or replacement by its policy-selecting relative.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.