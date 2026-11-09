# A-FDT: Choosing as the Output of a Function

## 1. The question A-FDT asks

Standard decision theory has two main options. **Causal decision theory (CDT)** asks which physical act of mine *causes* the best outcome. **Evidential decision theory (EDT)** asks which act would be the best *news* to learn I had taken. Yudkowsky and Soares's paper *Functional Decision Theory* proposes a third question. In their words, a rational agent "follows a decision procedure that asks 'Which output of this decision procedure causes the best outcome?'"

This essay explains the formal version of that idea given in **Equation (4), Section 5** of the paper. I call it **A-FDT** (action functional decision theory). The "A" marks that Equation (4) intervenes on a node whose value is an *action*. The authors say (footnotes 7 and 16) that their preferred formalization instead chooses *policies*, meaning mappings from observations to actions. They set that version aside because the difference "will not make a difference in this paper." I keep the two separate. When I mean the policy-level variant, I call it **policy-FDT**. The paper writes "FDT" throughout. When I report what the source claims, I attribute those claims to its analysis of Equation (4), which is A-FDT.

My aim is a reader's working manual. It covers:

- the definition;
- how to build the inputs;
- how to compute in standard cases;
- where the paper leaves gaps, and what operational choices fill them.

I label my own proposals as such.

## 2. The common framework

The paper treats EDT, CDT, and A-FDT as expected-utility theories that differ only in how they build hypotheticals. All three maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here $x$ is the observation history, and $a\hookrightarrow o_j$ is "the probability that $o_j$ will obtain in the hypothetical scenario where the action $a$ is executed after receiving observations $x$." Following Joyce, the paper holds that the theories disagree "about the epistemic perspective from which actions are to be evaluated." Each theory supplies a different reading of $\hookrightarrow$.

Write $V = \mathcal U(\textsc{Outcome})$. The three readings are:

- **EDT (Eq. 2):** $\displaystyle \arg\max_a \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a)$.
- **CDT (Eq. 3):** $\displaystyle \arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x)$, with $\mathtt{do}$ Pearl's intervention on a causal graph $G$.
- **A-FDT (Eq. 4):**
$$\boxed{\ \text{A-FDT}(P,G,x) \coloneqq \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\ }$$

The underlining means *dequoting*. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the name of a variable inside the agent's own model. That variable represents "what the A-FDT algorithm outputs when run on inputs $P,G,x$."

The paper itemizes two differences from CDT.

1. **Locus of intervention.** CDT intervenes on the token physical act. A-FDT intervenes on the logical output of the decision function, which is the *type*, in the paper's Peircean phrase. Anything else that computes or models that function moves with it.
2. **Treatment of observations.** A-FDT does not condition on $\textsc{Obs}=x$. Instead, "FDT responds to observation by changing which node it intervenes upon." On observation $y$ it would intervene on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second point matters more than it looks, and I return to it below.

## 3. Inputs: what $P$ and $G$ must contain

Equation (4) presupposes a world-model with three features.

- **Logical nodes.** $P$ "must contain variables representing the outputs of different mathematical functions." It must, in particular, contain one node $\textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might be in. The self-reference is meant to be harmless. The agent needs a variable *representing* the output, not its value, and quining (Kleene's recursion theorem) shows how such self-representing structures can be built.
- **A dependency graph $G$.** $G$ encodes "how changing a logical variable affects all other variables." Its edges go from $\textsc{fdt}$-nodes to every variable that *subjunctively depends* on that function's output. That includes the agent's own physical act, a twin's act, and a predictor's prediction. It excludes merely correlated variables such as a lesion.
- **Ordinary causal structure** everywhere else, so that $\mathtt{do}$ propagates downstream exactly as in Pearl's framework.

The paper defines subjunctive dependence by example. Two calculators computing $6288+1048$ both depend on that sum. A scribe copying one calculator depends on it causally, which the paper treats as a special case. Two calculators that happen to be pink do not depend on each other. Causal dependence is thus a special case of subjunctive dependence, and statistical correlation does not imply it. The summary slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

The paper does not say how to construct $G$. The authors call "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem." Equation (4) "works *given* a graph," but no procedure produces the graph. An ideal $\mathtt{true}$ operator for conditioning on counterpossible logical sentences would avoid needing $G$, but "it's not clear how to define" one. A-FDT is therefore a function of $(P,G,x)$, and all the substantive modelling work sits in $G$.

## 4. The procedure

Here is A-FDT written as an algorithm. Steps 1–4 follow the paper. Step 5 is my operational addition.

1. **Model.** List the decision-relevant variables, including $\textsc{Act}$, $V$, and an $\textsc{fdt}$-node for each possible observation $y$.
2. **Wire.** Draw edges from $\textsc{fdt}(\cdot,y)$ to $\textsc{Act}$ and to every predictor, twin, or simulation of the agent-in-situation-$y$. Make $\textsc{Act}$ a switch: whichever observation the world actually delivers selects which $\textsc{fdt}$-node sets the act.
3. **Intervene.** For each $a\in\mathcal A$, apply $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ for the *actual* $x$. Recompute every descendant, and leave non-descendants at their prior distributions.
4. **Evaluate.** Compute $\mathbb E(V)$ under each intervention, with **no** conditioning on $\textsc{Obs}=x$. Output the argmax.
5. **Fill in the other nodes (my proposal).** The $\textsc{fdt}$-nodes for observations other than $x$ are not intervened on. They retain prior probabilities, such as the paper's $q$. The paper notes that in its examples the result is insensitive to $q$ and remarks that "the correct $q$" is the value A-FDT would actually output. I recommend making this a consistency requirement: set the priors on the other nodes to the A-FDT outputs for those inputs, and iterate to a fixed point when necessary.

## 5. Worked examples

All utilities are in dollars. "Predictor accuracy 0.99" means that a noise node flips the prediction with probability 0.01.

### 5.1 Twin prisoner's dilemma

Both twins' acts are children of one node $F=\textsc{fdt}(\cdot)$. The two interventions give:

- $\mathtt{do}(F=\textit{cooperate})$: both cooperate, so $V=1{,}000{,}000$.
- $\mathtt{do}(F=\textit{defect})$: both defect, so $V=1{,}000$.

A-FDT cooperates. CDT holds the twin fixed, finds that defection dominates, and defects.

### 5.2 Newcomb's problem

The graph is $F \to \textsc{Act}$ and $F \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

$$\mathbb E(V\mid \mathtt{do}(F=\textit{1box})) = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E(V\mid \mathtt{do}(F=\textit{2box})) = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. The paper's text gives \$999,000 for Eve's one-box value. Since $0.99\times 10^6 = 990{,}000$, that figure appears to be a typo; nothing turns on it.

The paper stresses that this reasoning involves no retrocausation. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She only refuses to imagine her action changing without the predictor's model of her function changing too.

### 5.3 Smoking lesion

This case shows that A-FDT is not EDT under another name. The lesion causes both the desire to smoke and cancer. The paper formalizes this with two possible utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (indifferent or averse). It then uses two function-nodes:

- $\textsc{fdt}(\underline{P_S},\underline G)$ controls $\textsc{Act}$ if the agent has the lesion;
- $\textsc{fdt}(\underline{P_R},\underline G)$ controls $\textsc{Act}$ if she does not.

There is *no* edge from either node to $\textsc{Cancer}$. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ therefore leaves $P(\textit{lesion})=p$ unchanged. Smoking comes out ahead by $p\cdot 1{,}000$, so A-FDT smokes.

Newcomb and the lesion have identical *statistics*. They differ in *graph*. The predictor computes a model of the agent's function, and the lesion does not.

### 5.4 Transparent Newcomb and Parfit's hitchhiker

Now the observation matters. Suppose the agent sees box B full. The graph contains $\textsc{fdt}(\cdot,\textit{full})$, which feeds the prediction and the act, and $\textsc{fdt}(\cdot,\textit{empty})$, which feeds only the act. The prediction determines which observation occurs and hence which node controls the act. Let $q$ be the prior that the agent two-boxes on seeing an empty box. Intervening on the *full*-node gives:

$$\text{1box: } 0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000+10q,$$
$$\text{2box: } 0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q.$$

The paper prints the second value as "\$110,00", which looks like a typo for \$10,010. One-boxing wins for every $q\in[0,1]$.

This example only works because Equation (4) does **not** condition on $\textsc{Obs}=\textit{full}$. If we condition on a full box *and* intervene, the empty branch disappears and two-boxing wins by \$1,000. The paper notes in a passing remark that this "double update" was a flaw of the earlier Timeless Decision Theory.

There is a slip in the paper here. Its displayed formula for this case appends "$\textsc{Obs}=\textit{full}$" inside the conditional, but its own calculation sums over the empty-box branch. I follow Equation (4) and the calculation, and treat the displayed conditioning as an error.

Parfit's hitchhiker has the same structure. The driver's 99%-accurate lie detection plays the predictor, and paying in the city plays one-boxing. A-FDT pays. The paper adds three supporting considerations:

- an argument from precommitment: A-FDT acts as CDT and EDT agents would *precommit* to act;
- an argument from the value of information: A-FDT never pays to avoid information;
- an argument from utility, which the authors treat as primary.

### 5.5 XOR blackmail

A letter arrives if and only if exactly one of these holds: (i) there are no termites and you will pay \$1,000; (ii) there are termites and you won't pay.

- **EDT** pays. Conditioning on paying, given the letter, makes termites impossible.
- **A-FDT** sees that $\textsc{fdt}(\cdot,\textit{letter})$ affects whether the letter is sent but has no edge into $\textsc{Infestation}$. Let $p$ be the prior probability of termites.
  - $\mathtt{do}(\textit{pay})$: letter iff no termites. Expected loss is $(1-p)\,1{,}000 + p\,10^6$.
  - $\mathtt{do}(\textit{refuse})$: letter iff termites. Expected loss is $p\,10^6$.
  - Refusing is better by $(1-p)\,1{,}000$, so A-FDT refuses.
- **CDT** also refuses, but for a different reason. Its hypothetical has the predictor err.

### 5.6 Mechanical blackmail

The blackmailer runs the damaging program only if she predicts payment. Let $\epsilon$ be the probability that she wrongly predicts payment from a refuser. Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})$ gives:

- pay: the agent is always blackmailed and loses 1,000;
- refuse: the agent is blackmailed with probability $\epsilon$ and loses $10^6\epsilon$.

A-FDT refuses iff $\epsilon<0.001$.

The paper says refusing is right at $\epsilon=0.0009$, which matches this threshold. It then says that at an error rate of "0.011%" the agent pays. But $0.00011<0.001$, so that sentence is inconsistent with the model. It presumably means 1.1% or 0.11%. A reader applying A-FDT should compute the threshold directly rather than rely on the quoted figure.

### 5.7 Death in Damascus

Death's appointment book is a perfect prediction, so it is a child of $F$. Under either intervention Death is wherever the agent is. The only remaining difference is the \$1,000 travel cost, so A-FDT stays in Damascus.

CDT, by contrast, is "unstable." It holds Death's location fixed while varying its own act. It also turns down a truly random coin offered for \$1, because its hypotheticals already credit it with at least a 50% survival chance.

## 6. Dominance and fairness

A-FDT violates CDT-style dominance in Newcomb's problem. The paper's reply is that "every method for constructing hypotheticals gives rise to its own notion of dominance." Under A-FDT dominance, which holds subjunctive dependencies fixed, A-FDT never chooses a dominated act. Dominance therefore cannot adjudicate between theories without begging the question. The authors appeal instead to utility achieved.

That appeal needs a restriction, because any theory can be punished by a problem that rewards a rival *procedure*. The paper restricts the claim to "fair problems." These are problems in which "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb counts as fair because the predictor "punishes *two-boxers*," not CDT reasoners.

The authors state their superiority claim only tentatively. They have "not been able to construct an intuitively fair dilemma where FDT loses." Footnote 15 concedes that fairness has not been formalized. A problem that punishes anyone who matches a copy of the A-FDT agent defeats A-FDT, and it is unclear how to define fairness so as to exclude it uniformly.

## 7. Open questions and operational answers

**(a) Where do the edges in $G$ come from?** The source leaves this open. My working rule is to draw an edge $F\to Z$ when $Z$ is produced by a process that evaluates, simulates, or reliably infers the output of the agent's decision function on the relevant input. That covers predictors, twins, and recorded copies. Do not draw the edge when the correlation runs only through common causes of the agent's *inputs*, such as preferences or a lesion.

Imperfect modelling goes into a noise node, as with $\textsc{Accurate}$, rather than into a weaker edge. This rule reproduces every verdict in the paper. It does not settle partial similarity. Suppose an opponent runs a *related* but not identical algorithm. Then one must decide how much of its behavior hangs off $F$, and the paper gives no guidance. One defensible approach is a mixture: the opponent's act equals $F$ with probability $\rho$ and is independent otherwise, with $\rho$ the agent's credence that the two computations coincide on this input. That is my assumption, not the paper's.

**(b) Priors on non-actual $\textsc{fdt}$-nodes.** In the paper's examples the verdict does not depend on these priors. In general it might. As noted in §4, I recommend fixed-point consistency: the prior on $\textsc{fdt}(\cdot,y)$ should be degenerate on A-FDT's own output at $y$.

**(c) Action versus policy.** Because A-FDT intervenes on one node and holds the others at their priors, it optimizes one entry of the policy at a time. Policy-FDT would choose the whole map $\pi:\mathcal X\to\mathcal A$ jointly:

$$\pi^* = \arg\max_{\pi}\ \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),$$

and then act on $\pi^*(x)$.

When the other nodes' priors are set by the fixed-point rule, A-FDT's choices form a policy from which no single-entry deviation improves. That is a local optimum, and it need not be the global optimum. The two theories can diverge when entries interact, for instance in coordination across observation-copies or in multi-agent settings, which the paper flags. This analysis is mine. The paper says only that the difference matters "in certain multi-agent dilemmas."

**(d) Ties and zero-probability acts.** Equation (4) gives no tie-breaking rule. Interventions are always well defined, so A-FDT does not inherit EDT's problem with probability-zero acts.

**(e) Counterpossibles.** In a deterministic setting the intervened value is logically impossible. The paper argues this is no worse than CDT's predicament. A deterministic CDT agent also imagines acts it cannot take, and "any principled objection" to controlling a decision type applies equally to controlling a decision token.

## 8. Conclusion

A-FDT is CDT's surgical method, $\mathtt{do}$ on a graph, aimed at a different target. It intervenes on the logical output of the agent's own decision function on her actual input. Observations do not enter by conditioning. They select which function-node is intervened on.

Given a graph that records which variables subjunctively depend on that output, the recipe is mechanical. Intervene, propagate, compute expected utility without conditioning on the observation, and take the argmax. The recipe yields one-boxing in Newcomb, smoking in the lesion case, paying in Parfit's desert, refusal of both kinds of blackmail, and staying in Damascus.

The theory's weight rests on that graph, which the paper does not show how to construct. It also rests on a fairness criterion that remains unformalized. Using A-FDT on new cases therefore requires explicit modelling choices about dependence, priors on other observation-nodes, and the action/policy distinction. I have proposed defaults for each and labelled them as additions to the source.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060v2.