# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Decision Function

## 1. What this essay covers

Yudkowsky and Soares (2017) introduce a family of decision rules under the name *functional decision theory*. Their single explicit formal definition is Equation (4) of Section 5. It selects an **action** by intervening on a variable that represents the output of the agent's decision function given her current observation. Footnotes 7 and 16 add that the authors' *preferred* formalization selects **policies**, meaning mappings from observations to actions. To keep the two apart, I call the Equation (4) theory **A-FDT** (action functional decision theory) and the policy-selecting variant **policy-FDT**. Inside quotations, the paper's "FDT" refers to what I call A-FDT, unless the quotation is about policies.

The plan is as follows. I set out the shared expected-utility framework, state A-FDT precisely, and explain what its counterfactuals hold fixed and what they vary. I then work through the standard cases. Finally I separate what the paper determines from what it leaves open, and propose operational fixes. Those fixes are labelled as my own.

## 2. The common frame: expected utility with a free "hypothetical" connective

Following Gibbard and Harper, the paper treats evidential decision theory (EDT), causal decision theory (CDT), and A-FDT as rules that each maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective whose interpretation the theories dispute. Citing Joyce's representation theorem, the authors argue that expected-utility theories agree on how to value prospects and disagree only on "the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each action $a$, she builds a *hypothetical* $M^{a\hookrightarrow}$, scores it, and picks the best. The paper stresses that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs." This framing explains why A-FDT is useful even though some of the hypotheticals it builds are impossible.

The two rival rules, with $V := \mathcal U(\textsc{Outcome})$, are:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a), \tag{2}
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x). \tag{3}
$$

In (3), $G$ is a causal graph over the variables of $P$, and $\mathtt{do}$ is Pearl's intervention operator. The operator severs the incoming dependencies of the intervened node and propagates the change only downstream.

## 3. The definition of A-FDT

A-FDT requires the model $P$ to contain variables for the outputs of mathematical functions. In particular it must contain a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ that denotes the output of the A-FDT procedure itself when run on inputs $(P,G,x)$. The underline means dequoting: the variable's *name* is built from the model and the observation. The graph $G$ now encodes more than causal structure. It encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." Equation (4) is:

$$
\boxed{\;\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;} \tag{4}
$$

The paper names two differences from (3):

1. **The intervention target.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the output of the function. Every node that subjunctively depends on that output moves with it, including the agent's own act, a twin's act, and a predictor's prediction.
2. **The treatment of observations.** In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Equation (4) contains no "$\mid \textsc{Obs}=x$." The observation enters only through *which* node is set: on seeing $y$ instead of $x$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The self-reference ($P$ contains a variable naming $\mathrm{FDT}(P,G,x)$) is declared harmless. The agent needs a variable representing the value, not the value itself, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

The philosophical slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" The deliberative question changes from "which act of mine causes the best outcome?" to "Which output of this very function would yield the best outcome?"

### 3.1 Subjunctive dependence: what the graph must encode

Physical systems whose behavior is fixed by the same function "subjunctively depend" on that function. Two well-functioning calculators computing $6288+1048$ are the paradigm. Causal dependence is a special case: a scribe copying a calculator's output depends on it in both senses. Mere correlation, such as two calculators that happen to be pink, does not count.

For a decision problem, the paper gives three rules for building $G$:

- A **predictor** who accurately models the agent's decision function on input $y$ gets an edge from $\textsc{fdt}(\cdot,\cdot,y)$. If the predictor is imperfect, the edge passes through a noise node such as $\textsc{Accurate}$.
- A **twin** running the same function gets an edge from the same node.
- A **lesion**, gene, or other common cause that merely correlates with the act gets *no* such edge, because "the cancer is not evaluating the agent's future decisions."

The resulting counterfactuals are counterpossible. If the function in fact outputs one-box, there is no possible world in which it outputs two-box. The paper concedes that it lacks a general $\mathtt{true}(\varphi)$ operator for conditioning on false logical sentences. Equation (4) avoids that gap by taking the dependency graph $G$ as given input, exactly as CDT takes its causal graph as given.

### 3.2 When A-FDT agrees with CDT and EDT

Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories coincide. Divergence requires something that correlates with the agent's act without being caused by it. Predictors and copies are the cases where A-FDT departs from CDT. Pure common causes are the cases where A-FDT departs from EDT.

## 4. Worked examples

All dollar figures are utilities. I reproduce the paper's numbers and flag two arithmetic slips along the way.

### 4.1 Psychological Twin Prisoner's Dilemma

The node $\textsc{fdt}$ feeds both the agent's act and the twin's act. Intervening sets both values together:

- $\mathtt{do}(\textsc{fdt}=C)$ gives $1{,}000{,}000$.
- $\mathtt{do}(\textsc{fdt}=D)$ gives $1{,}000$.

A-FDT cooperates. CDT sees the twin's act as causally independent of its own and defects by dominance.

### 4.2 Newcomb's Problem (99% accurate predictor)

The graph is $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\text{one})] = 0.99(1{,}000{,}000) = 990{,}000,
$$
$$
\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\text{two})] = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.
$$

A-FDT one-boxes. (The paper gives EDT's one-box value as \$999,000. That is a slip; it is \$990,000, which does not change the verdict.)

The paper heads off an objection here. Suppose the agent is nearly certain she one-boxes, and so nearly certain the box is full. Why doesn't she then take both boxes? Because her hypothetical for two-boxing is not "my body grabs both while everything else stays fixed." It is "the function outputs *two*," and that hypothetical carries an empty box with it. No retrocausation is claimed.

### 4.3 Smoking Lesion

The paper formalizes the lesion as fixing which utility function the agent has:

- $\mathcal U_S$ (lesion; values smoking at \$1,000);
- $\mathcal U_R$ (no lesion; values smoking at $-\$1$).

There are therefore two candidate decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Act}$ copies whichever node the lesion selects. The agent cannot introspect which node is hers.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\text{lesion})=p$ unchanged, since the lesion is upstream. Let $q$ be the agent's belief that the other node outputs *smoke*. The two values are:

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q)$;
- refrain: $p(10{,}000)+(1-p)(990{,}000+1{,}000q)$.

The difference is $1{,}000p > 0$, so the agent smokes. A-FDT thus one-boxes *and* smokes. Gibbard and Harper had argued that no rational agent could consistently make that pair of choices.

### 4.4 Transparent Newcomb

The agent sees box B full. Her graph has two decision nodes, $\textsc{fdt}(\cdot,\text{full})$ and $\textsc{fdt}(\cdot,\text{empty})$. $\textsc{Prediction}$ determines which observation occurs, and hence which node controls $\textsc{Act}$. The predictor's prediction depends on $\textsc{fdt}(\cdot,\text{full})$.

Let $q$ be the agent's belief that she two-boxes on seeing an empty box. Intervening on the *full* node gives:

- one-box: $0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000 + 10q$;
- two-box: $0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010 + 990q$.

(The paper prints the second figure as "\$110,00".) A-FDT one-boxes even while looking at \$1,000,000.

The key feature is that the hypothetical for two-boxing is one in which she would *probably have seen an empty box*. Because the observation is not conditioned on, it can vary inside the hypothetical. The paper presents Parfit's hitchhiker as the same structure: pay the driver.

### 4.5 Blackmail

**XOR blackmail.** The letter is sent iff exactly one of these holds: (no termites and you pay) or (termites and you refuse). EDT pays, because conditioning on paying makes termites impossible given the letter. A-FDT intervenes on $\textsc{fdt}(\cdot,\text{letter})$. That changes whether the letter arrives but leaves $\textsc{Infestation}$ alone, which is upstream. Paying merely costs \$1,000, so A-FDT refuses.

**Mechanical blackmail.** The blackmailer runs the damaging program iff she predicts the agent would pay. A-FDT refuses even with the letter in hand, because under $\mathtt{do}(\textsc{fdt}(\cdot,\text{blackmail})=\text{refuse})$ she would almost surely never have been blackmailed.

With predictor error rate $\varepsilon$:

- refusing costs $\varepsilon\cdot 10^6$ in expectation;
- paying costs $10^3$.

The threshold is therefore $\varepsilon = 0.1\%$. The paper's $0.09\%$ case (refuse, expected loss \$900) fits this. Its statement that she pays at "0.011%" must be a slip for something above 0.1%, such as 0.11%.

### 4.6 Death in Damascus

Death predicts perfectly, so $\textsc{fdt}$ feeds both $\textsc{Act}$ and Death's appointment book:

- $\mathtt{do}(\textsc{fdt}=\text{stay})$ means dying in Damascus, value $0$;
- $\mathtt{do}(\textsc{fdt}=\text{flee})$ means dying in Aleppo, value $-1{,}000$.

A-FDT stays, and its verdict does not oscillate the way CDT's does.

The paper also offers a truly random coin for \$1 that Death cannot predict. It shows that CDT declines the coin, but does not explicitly compute A-FDT's response. Here is my reading. The coin's outcome is not downstream of $\textsc{fdt}$, so the hypothetical "buy and follow the coin" yields roughly a 50% survival chance, worth about $500{,}000-1$. A-FDT therefore buys the coin.

## 5. A procedure for unfamiliar cases

Collecting the paper's practice gives the following recipe. The steps are faithful to the examples, but the ordering and phrasing are mine.

1. **Fix the decision point.** Identify the action set $\mathcal A$ and the actual observation $x$.
2. **Enumerate decision nodes.** Include $\textsc{fdt}(\cdot,x)$ and $\textsc{fdt}(\cdot,y)$ for every alternative input $y$ the agent might have faced *within the problem*: other observations, or other preference profiles as in the lesion case.
3. **Draw dependence edges.** Every system that computes or accurately models the decision function on input $y$ gets an edge from $\textsc{fdt}(\cdot,y)$, with noise nodes for imperfect accuracy. Merely correlated factors get no such edge. Ordinary causal edges stay as in CDT.
4. **Wire the act.** $\textsc{Act}$ is a switch: it copies whichever decision node is selected by the variables that generate observations (or preferences).
5. **Intervene, do not condition.** For each $a$, set $\textsc{fdt}(\cdot,x)=a$, propagate downstream, and leave the other decision nodes at their prior distributions. Do *not* condition on $\textsc{Obs}=x$.
6. **Maximize** $\mathbb E[V]$ over $a$.

A notational trap sits at step 5. In the transparent Newcomb section the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\cdot,\text{full})=a,\ \textsc{Obs}=\text{full})$. That expression has an unbalanced parenthesis and an observation term that Equation (4) lacks. The paper's own computation, which averages over the *empty-box* branch, is consistent only with *no* conditioning. Conditioning on $\textsc{Obs}=\text{full}$ would make two-boxing win by \$1,000. I therefore read the displayed term as a typo and treat Equation (4) as authoritative. The paper's remark that the earlier timeless decision theory "prescribes both conditioning on evidence *and* changing the place where one intervenes," producing a harmful "double update," supports this reading.

## 6. What the source leaves open, and how one might close it

### 6.1 Where does $G$ come from?

The paper is candid: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) is a function *of* $G$. Disagreements about whether some process "really" models the agent are disagreements about input, not about the rule.

An operational heuristic of my own: draw an edge from $\textsc{fdt}(\cdot,y)$ to a variable $Z$ when, in the agent's model, $Z$ is computed from a representation of the agent's decision procedure that would track changes in its output. Predictors, simulations, and copies meet this test. Mere common causes do not, because nothing in the lesion consults the procedure. Graded or partial modelling is handled by noise nodes. This makes the edges answer a question about mechanisms ("does $Z$ consult a model of this procedure?") rather than about counterpossible truth. Hard cases remain, such as a predictor that models a *similar but non-identical* procedure. There one must judge how strongly that procedure's output co-varies with this one's; the paper offers no metric for that.

### 6.2 Priors on the non-intervened decision nodes

In 4.3 and 4.4 the result depends on the agent's prior $q$ over the *other* decision nodes. The paper says the correct $q$ is $0$ (lesion) or $1$ (empty box) "as you may verify," and that uncertainty does not matter in those cases. In general it can matter. Equation (4) does not say how these priors are formed. Like EDT's prior over its own act, they involve self-prediction.

My proposal is a **consistency condition**. Beliefs about $\textsc{fdt}(\cdot,y)$ should put mass on $\text{A-FDT}(P,G,y)$, computed by the same rule. A full specification is then a fixed point, a profile $\{a_y\}$ such that each $a_y$ maximizes (4) when the other nodes are believed to take their $a_{y'}$ values. In the paper's examples this fixed point is unique, and the answers are insensitive to $q$ anyway.

### 6.3 A-FDT versus policy-FDT: where action-selection can fall short

The fixed-point proposal shows why the choice between actions and policies matters. The paper says it "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." Here is an illustration of my own construction.

> A fair coin shows the agent *red* or *green*. Earlier, a perfect predictor paid \$1,000,000 into her account iff it predicted she would press **A** under *both* colours. Pressing **B** instead adds \$1.

Consider A-FDT on seeing *red*:

- If the agent believes she presses B on green, then setting the red node to A brings no million. B is better by \$1, so B wins.
- If she believes she presses A on green, then A on red secures the million, so A wins.

Both "always A" and "always B" are self-consistent profiles. A-FDT, intervening on one node at a time with the others held at their believed values, cannot by itself select between them.

Policy-FDT intervenes on the whole mapping $\pi:\{\text{red},\text{green}\}\to\{A,B\}$ and directly compares:

- "always A": $1{,}000{,}000$;
- "always B": $1$;
- mixed policies: $0.5$.

It picks "always A."

So A-FDT is best understood as **node-wise** optimal given beliefs about one's other-input behaviour. Policy-FDT is **jointly** optimal across inputs. A natural tie-breaking supplement is my suggestion and goes beyond Equation (4): when several self-consistent profiles exist, an A-FDT agent should adopt beliefs matching the profile with the highest ex ante expected utility. This recovers policy-FDT's verdict without changing Equation (4). It also matches the paper's claim that such agents "act as they would have precommitted to act."

### 6.4 Smaller gaps

- **Ties and mixing.** The $\arg\max$ may be a set. The paper does not specify tie-breaking, and A-FDT never needs mixed strategies in the paper's examples.
- **Zero-probability actions.** Unlike EDT, A-FDT is unaffected by a prior of zero on an action, since $\mathtt{do}$ is defined regardless.
- **Approximation.** The paper analyses idealized agents with minimal models. It expects bounded approximators to inherit the same qualitative differences, but gives no theory of this.

## 7. Dominance, fairness, and the philosophical case

The traditional argument for two-boxing appeals to dominance. The paper replies that dominance always presupposes a way of building counterfactuals. Holding the prediction fixed while the act varies is CDT's counterfactual, so the argument assumes what it sets out to prove. Under A-FDT counterfactuals, which hold the subjunctive dependencies fixed, A-FDT never takes a dominated action.

The positive case is mainly performance in "fair" problems. These are problems in which "the outcome depends only on the agent's behavior in the dilemma at hand" and the agent's beliefs are accurate. Newcomb's predictor "punishes *two-boxers*," not CDT agents as such. The authors report no fair dilemma in which a rival beats FDT. They admit, however, that "fair" lacks a formal definition, and footnote 15 shows the difficulty: a problem that punishes whoever matches Fiona's copy is intuitively unfair, but it is not obvious how to rule it out in a principled way.

Two further arguments support the performance case:

- **The argument from precommitment.** CDT and EDT agents would pay to bind themselves to A-FDT's choices.
- **The argument from reflective stability.** A-FDT does not wish to self-modify mid-problem, whereas CDT recommends abandoning itself for future problems.

On "control," the paper argues for parity. A deterministic CDT agent also "imagines" varying a token that cannot vary. Any objection to intervening on a logical output therefore applies equally to intervening on a determined physical act.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT with two substitutions. The intervention target is the output of the agent's own decision function on her actual input, not her physical act. And observations are handled by choosing which function-node to intervene on, never by conditioning. Given a model $P$ and a graph $G$ that records which processes compute or model that function, the rule is fully mechanical. It cooperates with twins, one-boxes, smokes, pays the hitchhiker's driver, refuses both blackmails, and stays in Damascus.

What the paper does not supply is equally clear:

- a method for constructing the subjunctive-dependence graph;
- a rule for the agent's beliefs about her own behaviour on other inputs;
- an account of when action selection falls short of the authors' preferred policy selection.

I have proposed treating the second as a self-consistency fixed point, and resolving multiple fixed points by ex ante value, which reproduces policy-level optimality. These are additions, not claims of the source. With them, a reader can take an unfamiliar dilemma, draw the nodes, intervene, and compute.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.