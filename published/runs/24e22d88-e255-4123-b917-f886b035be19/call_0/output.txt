# A-FDT: Action Functional Decision Theory, Explained and Operationalized

## 1. What this essay covers

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* presents a family of decision rules under the name FDT. Its formal centerpiece is Equation (4) in Section 5. That equation intervenes on the *output of the agent's decision function on the agent's current input*, and the output it selects is a single action. The paper also says, in a footnote, that the authors themselves prefer a different formalization:

> "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

Two theories are therefore in view, and I keep them apart:

- **A-FDT (action functional decision theory)** is the rule of Equation (4). It chooses an action by intervening on the node representing the decision function's output at the current input. This essay is about A-FDT.
- **Policy-selection FDT (PS-FDT)** is the policy variant mentioned in the footnotes. It chooses a whole mapping from observations to actions.

I compare both against **causal decision theory (CDT)** and **evidential decision theory (EDT)**.

Labeling conventions:
- Claims attributed to "the paper" come from the source.
- Material marked **[my proposal]** or **[my example]** is my own operationalization or construction.

## 2. The motivating idea

The paper's slogan is that the agent should treat her decision as the output of a fixed mathematical function and ask: "Which output of this very function would yield the best outcome?"

Its central structural claim is an analogy:

> "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

Two systems *subjunctively depend* on a function when both of them compute it. The paper's image is two well-functioning calculators on opposite sides of the globe, both computing $6288+1048$.

The motivating contrast is between a predictor and a lesion:

- A reliable predictor in Newcomb's problem contains a model of the agent's decision procedure. Its prediction therefore subjunctively depends on that procedure's output.
- A carcinogenic lesion only correlates with smoking. It does not compute anything about the agent's reasoning.

A CDT agent "intervenes on the token" (her physical act). An A-FDT agent intervenes on the *type*: the logical fact about what her decision function outputs.

## 3. The formal definition

### 3.1 Common expected-utility skeleton

All three theories share the expected-utility form (paper's Eq. 1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

They differ only in how the hypothetical connective $\hookrightarrow$ is interpreted. The paper follows Joyce in treating this connective as the "free parameter" of decision theory. Write $V = \mathcal U(\textsc{Outcome})$.

**EDT (Eq. 2)** conditions:
$$
\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a).
$$

**CDT (Eq. 3)** intervenes on the physical act and conditions on observations:
$$
\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid do(\textsc{Act}=a),\textsc{Obs}=x\big).
$$

### 3.2 A-FDT (Eq. 4)

$$
\boxed{\;\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \,\Big|\, do\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big)\;}
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. These variables include ordinary physical ones and *logical* ones, i.e. variables representing the outputs of mathematical functions on particular inputs.
- **$G$** is a graph describing "how changing a logical variable affects all other variables". This covers logical, computational, and causal structure alike.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node in the model representing the output of the decision function on the agent's actual inputs. The underlines denote dequoting: the node's *name* is built from the model itself.
  - The paper argues this self-reference is harmless. The agent needs a variable *representing* the value, not the value itself, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.
- **$do(\cdot)$** is Pearl's intervention operator, reused unchanged. It sets the chosen node, recomputes everything downstream of it in $G$, and leaves everything else at its prior distribution.

### 3.3 Two structural differences from CDT

The paper stresses two differences between Eq. 4 and Eq. 3.

1. **Locus of intervention.** CDT intervenes on the physical $\textsc{Act}$. A-FDT intervenes on the logical node.
2. **Treatment of observation.** CDT updates on the observation $x$ by conditioning. A-FDT instead responds to $x$ by *changing which node it intervenes on*:

> "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\textsc{Obs}=x$ to conditioning its model on $\textsc{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

The second point is the source of A-FDT's most surprising verdicts. In an A-FDT hypothetical, the agent may have *made different observations* than she actually made. The paper says FDT "says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*."

### 3.4 When the three theories coincide

The paper notes that the three theories agree whenever every correlation between $\textsc{Act}$ and other variables is produced by $\textsc{Act}$ itself, apart from $\textsc{Act}$'s own dependence on the logical node. In that case:

$$
\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)].
$$

A-FDT only diverges from the others when something other than the agent's own body computes or predicts her decision.

## 4. Operational recipe for A-FDT

The paper says Eq. 4 "works *given* a graph," and calls the construction of such graphs "perhaps the largest open problem." To decide unfamiliar cases, a reader still needs a procedure. The following steps are **[my proposal]**, distilled from the paper's worked figures.

**Step 1: Identify decision-function inputs.** List every input $y$ on which the agent's decision function is evaluated by *anyone*. This includes:
- the agent herself in each observation-branch, and
- predictors or simulators, when they evaluate what she would do on input $y$.

Each such $y$ gets a root node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$.

**Step 2: Draw dependence edges.** Draw an edge $F_y\to Z$ whenever $Z$ is a physical process that computes or reliably models the decision function on input $y$. Examples are a twin's action, a predictor's prediction, and the agent's own body when she receives $y$.
- Imperfect modeling is represented by an independent noise parent, as with the paper's $\textsc{Accurate}$ node.
- Statistical correlates that do not model the computation, such as a lesion, get no such edge.

**Step 3: Make the act a selector.** Define $\textsc{Act}$ as a deterministic function that selects which $F_y$ controls the body, according to which observation the world actually delivers. Formally,
$$
\textsc{Act}=F_{\textsc{Obs}},
$$
where $\textsc{Obs}$ is itself computed from upstream variables. This mirrors the paper's figures for the transparent Newcomb problem and the blackmail problems.

**Step 4: Set priors on everything else.** Put priors on the non-intervened roots. These include noise terms, states of nature, and the *other* logical nodes $F_{y'}$ for $y'\neq x$.

**Step 5: Evaluate each action.** For each $a\in\mathcal A$, compute $\mathbb E[V\mid do(F_x=a)]$ by forward propagation. Do **not** additionally condition on $\textsc{Obs}=x$.

**Step 6: Choose.** Output the argmax. Ties are unspecified in the paper; any tie-breaking rule is an added assumption.

### On Step 5: the paper's two notations disagree

In the transparent Newcomb section, the paper writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$. That expression has an unbalanced parenthesis, and it appears to include the observation.

However, the numbers the paper actually computes make sense only if the observation is *not* conditioned on. The two-box hypothetical is credited mainly with the empty-box payoff, which is impossible if $\textsc{Obs}=\textit{full}$ were held fixed.

Equation (4) itself contains no observation term, and the paper's remarks about not double-updating point the same way. Its footnote on Timeless Decision Theory criticizes "both conditioning on evidence *and* changing the place where one intervenes" as a harmful "double update." I therefore read A-FDT as **unconditioned intervention**. The observation enters only through the choice of node.

## 5. Worked examples

### 5.1 Newcomb's problem (99% accurate predictor)

The model is:
- $F$ (the logical node) $\to$ $\textsc{Act}$;
- $F$ $\to$ $\textsc{Prediction}$, with an accuracy noise parent;
- $\textsc{Prediction}$ $\to$ Box B.

The two hypotheticals give:

$$
\begin{aligned}
\mathbb E[V\mid do(F=\textit{onebox})]&=0.99(10^6)=\$990{,}000,\\
\mathbb E[V\mid do(F=\textit{twobox})]&=0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000.
\end{aligned}
$$

A-FDT one-boxes.

For comparison, CDT holds $P(\textit{full})=p$ fixed under $do(\textsc{Act})$, so two-boxing wins by \$1,000 for every $p$.

A minor arithmetic note: the paper quotes \$999,000 for EDT's one-box value. The same model actually gives \$990,000, which is also the figure the paper reports for Fiona.

### 5.2 Smoking lesion

In this case the logical node is *not* a parent of $\textsc{Cancer}$. The paper's formalization is unusual. The lesion determines which utility function, and hence which world-model ($P_S$ or $P_R$), the agent runs. $\textsc{Act}$ then selects between the two logical nodes according to the lesion.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Smoking therefore wins by $p\cdot\$1{,}000$.

One subtlety is worth flagging. The agent intervenes on the node indexed by the model she is actually running, even though she "does not have introspective access" to which one that is. The paper treats this as harmless, but it shows that A-FDT presupposes the agent's own inputs are well-defined *as inputs*, even when they are not known *as content*.

### 5.3 Transparent Newcomb (agent sees box B full)

Here $x=\textit{full}$. Let $q$ be the prior that $F_{\textit{empty}}=\textit{twobox}$.

If $F_{\textit{full}}=\textit{onebox}$:
- An accurate prediction (99%) fills the box, and the agent takes \$1,000,000.
- An inaccurate one (1%) leaves the box empty. Then $F_{\textit{empty}}$ controls the act and yields $q\cdot\$1{,}000$.

$$
\mathbb E=990{,}000+10q.
$$

If $F_{\textit{full}}=\textit{twobox}$:
- An accurate prediction (99%) leaves the box empty, and the agent gets $q\cdot1{,}000$.
- An inaccurate one (1%) fills the box, and the agent gets \$1,001,000.

$$
\mathbb E=0.01(1{,}001{,}000)+0.99q(1{,}000)=\$10{,}010+990q.
$$

The paper prints the second value as "\$110,00 + $q\cdot$\$990", which is evidently a typo. Either way, A-FDT one-boxes while looking at a full box. The two-box hypothetical is one in which she *would mostly have seen an empty box*.

The paper argues this verdict is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem. It supports the verdict with arguments from precommitment, from the value of information, and above all from utility.

### 5.4 XOR blackmail

The letter is sent iff exactly one of the following holds:
- no termites, and the agent would pay; or
- termites, and the agent would refuse.

Let $p=P(\textit{termites})$, and let the input be $x=\textit{letter}$.

Under $do(F_{\textit{letter}}=\textit{pay})$:
- With no termites, the letter is sent and she pays: $-1{,}000$.
- With termites, no letter is sent and she loses $10^6$.

$$
\mathbb E=-(1-p)1{,}000-p\cdot10^6.
$$

Under $do(F_{\textit{letter}}=\textit{refuse})$:
- With no termites, no letter is sent: $0$.
- With termites, the letter is sent and she refuses: $-10^6$.

$$
\mathbb E=-p\cdot10^6.
$$

Refusing is better by $(1-p)\cdot 1{,}000$. Infestation is upstream of and independent from the logical node, so intervention cannot "manage the news." EDT pays here, because conditioning on paying drives $P(\textit{termites})$ to 0. CDT refuses as well, but for a different reason: in CDT's hypothetical, the predictor erred.

### 5.5 Mechanical blackmail with a fallible blackmailer

Suppose the blackmailer wrongly predicts "pays" with probability $\varepsilon$.

- Under $do(F_{\textit{bm}}=\textit{refuse})$, she is blackmailed only by mistake. Expected loss: $\varepsilon\cdot 10^6$.
- Under $do(F_{\textit{bm}}=\textit{pay})$, she is always blackmailed and pays. Expected loss: $1{,}000$.

A-FDT therefore refuses iff $\varepsilon<10^{-3}$.

The paper's first figure, $\varepsilon=0.0009$ (expected loss \$900), is consistent with this. Its second figure is stated as "0.011%", which would still favor refusal. The threshold calculation shows the intended value must be about 0.11%.

The lesson is that A-FDT's resistance to extortion is a quantitative output of Eq. 4, not a fixed policy rule. A sufficiently error-prone blackmailer *does* get paid.

### 5.6 Twin Prisoner's Dilemma and Death in Damascus

**Twin Prisoner's Dilemma.** Both bodies are children of the same logical node, so the hypotheticals are \$1,000,000 for cooperating and \$1,000 for defecting. A-FDT cooperates.

**Death in Damascus.** Death's appointment book is a child of the logical node. In every hypothetical, Death meets her wherever she goes. She stays and saves \$1,000, with no instability.

CDT, by contrast, oscillates in Death in Damascus, or needs ratification. On the paper's analysis, it would even refuse a \$1 truly random coin that offers a 50% chance of survival.

## 6. What A-FDT holds fixed: the role of other-input nodes

A-FDT's hypotheticals vary *one* logical node, $F_x$. Every other node $F_{y'}$ keeps its prior. The paper's examples are built so that this prior washes out, as with $q$ above. The paper says the correct values are $q=1$ (transparent Newcomb) and $q=0$ (smoking lesion), and that uncertainty about them "doesn't matter".

In general it can matter. This is exactly where A-FDT and PS-FDT come apart. Writing $\pi$ for a policy:

$$
\text{PS-FDT}:\ \pi^*=\arg\max_{\pi}\ \mathbb E\big[V\mid do(F_y=\pi(y)\ \forall y)\big],\quad\text{act }\pi^*(x).
$$

**[My example] Self-coordination across observations.** A fair coin determines whether the agent is shown *red* or *blue*. A perfect predictor pays:
- \$10 if the agent's red-action and blue-action are both $A$;
- \$5 if both are $B$;
- \$0 otherwise.

Suppose the agent, now seeing red, believes with near certainty that $F_{\textit{blue}}=B$. A-FDT computes:

$$
\mathbb E[V\mid do(F_{\textit{red}}=A)]\approx 0,\qquad \mathbb E[V\mid do(F_{\textit{red}}=B)]\approx 5,
$$

and chooses $B$. By symmetry the blue-branch does the same. The resulting profile $(B,B)$ is self-consistent, yet PS-FDT would select $(A,A)$ and earn \$10.

Under A-FDT, each branch best-responds to beliefs about the others. The theory thus behaves like a search for a *Nash equilibrium among one's own input-instances*, whereas PS-FDT jointly optimizes. This is a plausible reconstruction of why the authors prefer policies, though the paper says only that the difference "makes a difference in certain multi-agent dilemmas."

Two consequences follow for practical use.

1. **[my proposal] Reflective consistency of the priors.** The prior on $F_{y'}$ should equal what A-FDT would actually output at $y'$. A well-posed A-FDT model is then a *fixed point*: a profile $\sigma$ with $\sigma(y)=\text{A-FDT}(P_\sigma,G,y)$ for all $y$. Such fixed points can be multiple, as the example shows, and A-FDT does not say which one to occupy.
2. **Where PS-FDT is a refinement.** When the payoff is *separable*, meaning each branch's contribution depends only on its own node's value, the fixed point is unique and coincides with PS-FDT's choice. In the paper's examples this condition effectively holds, because the off-path node only affects low-probability branches, so the paper's claim that the distinction makes no difference there is accurate. A cautious practitioner should therefore check for joint, non-separable dependence on several input-nodes. When it is present, A-FDT's verdict depends on the agent's self-predictions, and PS-FDT is the better-behaved refinement.

## 7. Remaining open questions

**Constructing $G$.** The paper is explicit that no analogue of Pearl's causal-discovery theory exists for subjunctive dependence. Hard cases include:
- a predictor using a coarse heuristic that agrees with the agent 80% of the time;
- an agent running a *slightly different* function, such as a near-twin.

My Step 2 forces such cases into "edge plus noise." That is a modeling choice. The alternative is a separate node for the similar function, with a correlation between the two nodes that intervention would cut. The two choices can give different verdicts, and the paper does not adjudicate between them.

**Counterpossibles.** Setting $F_x$ to a value it does not actually take is a counter-logical supposition. The paper's ideal operator $\mathtt{true}(\phi)$ would handle this, but the paper admits "it's not clear how to define" it. Eq. 4 sidesteps the problem by stipulating $G$. The price is that A-FDT's verdicts are only as good as the stipulated graph.

**Fairness.** The paper conjectures that FDT is optimal on "fair" problems, those where outcomes depend only on the agent's behavior in the dilemma. It does not formalize fairness, and footnote 15 shows the difficulty. A-FDT's guarantees inherit this vagueness.

## 8. On the philosophical charge of "controlling the past"

A natural objection is that A-FDT agents act as if they control past predictions or mathematical facts.

The paper's reply is a parity argument. A deterministic CDT agent equally "controls" only an act that could not have been otherwise. Both theories evaluate hypotheticals that are, strictly speaking, impossible:

- CDT imagines a perfect predictor that errs.
- A-FDT imagines observations it would not actually have had.

The theories differ only in which impossibility they entertain. The paper's verdict is that the A-FDT choice "track[s] the real-world dependence relations." The paper also claims a matching dominance notion: holding subjunctive dependencies fixed, A-FDT never takes a dominated action. Dominance in general is therefore relative to one's hypothetical-construction method, and cannot serve as a neutral tie-breaker between CDT and A-FDT.

## 9. Conclusion

A-FDT, as given by Equation (4), is CDT with two edits:

1. The intervention target is a logical node, the output of the agent's own decision function on her current input.
2. Observations select the intervention target instead of being conditioned on.

Given a graph in which every process that computes or models that function hangs off the node, A-FDT:
- one-boxes in Newcomb's problem and smokes in the smoking lesion problem;
- pays the driver in Parfit's hitchhiker problem;
- refuses both XOR and mechanical blackmail when the blackmailer is reliable enough;
- stays home in Damascus.

It does all this without ratification or precommitment devices.

Applying A-FDT honestly takes two things beyond the equation. First, the agent needs a defensible subjunctive-dependence graph, which the paper leaves as its main open problem. Second, she needs consistent beliefs about her own outputs on inputs she is not currently facing. Where payoffs depend jointly on several such outputs, A-FDT reduces to equilibrium selection among one's own instances. The policy-level variant the authors favor is the natural repair for that case.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.