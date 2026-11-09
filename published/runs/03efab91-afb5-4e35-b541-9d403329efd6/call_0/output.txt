# A-FDT: Choosing as the Output of a Function

## 0. Scope and naming

Yudkowsky and Soares's paper *Functional Decision Theory* presents a decision rule that, in their words, asks: "Which output of this very function would yield the best outcome?" Its main formal statement, Equation (4) in Section 5, intervenes on a variable whose possible values are **actions**. Two footnotes (7 and 16) report that the authors' "preferred formalization" instead chooses **policies**, meaning maps from observations to actions. They add that the difference "will not make a difference in this paper."

I follow the assignment and call the Equation (4) rule **A-FDT** (action functional decision theory). I call the footnoted variant **policy-selecting FDT**. Other theories keep their usual names: causal decision theory (**CDT**), evidential decision theory (**EDT**), and Timeless Decision Theory (**TDT**).

Throughout, I separate three kinds of claim:

- what the paper says;
- what follows mathematically from Equation (4);
- operational choices that are my own and that the paper leaves open.

## 1. The common frame: expected utility over hypotheticals

All three theories in the paper maximize

$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a\in\mathcal A$ is an action from a finite set, $x$ is the observation history, and $P(a\hookrightarrow o_j;x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$."

Following Joyce, the paper treats the theories as agreeing about value and disagreeing about the connective $\hookrightarrow$. In the paper's terms, they differ in how they build a **hypothetical** from the agent's world-model. A hypothetical is a transient computational object, "like notes on scratch paper," not a metaphysical possible world.

With $V:=\mathcal U(\textsc{Outcome})$, the three rules are:

$$
\mathrm{EDT}(P,x)=\arg\max_a \mathbb E\,(V\mid \textsc{Obs}=x,\ \textsc{Act}=a), \tag{2}
$$

$$
\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E\,(V\mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x), \tag{3}
$$

$$
\text{A-FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}
$$

The paper writes the left side of (4) as $\mathrm{FDT}(P,G,x)$.

## 2. Anatomy of Equation (4)

### 2.1 The decision node

$P$ is a joint distribution over variables. Some variables stand for physical facts, such as the box contents or the agent's bodily action. Others stand for **logical facts**, meaning the outputs of mathematical functions on given inputs.

$\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable for "what the A-FDT algorithm outputs when run on $(P,G,x)$." The underline marks dequoting: the variable's *name* is built from the model itself. The paper notes the self-reference is harmless, because the agent needs a variable *representing* the output, not knowledge of its value. Quining (Kleene's recursion theorem) shows such self-representing structures exist.

### 2.2 The graph $G$

$G$ tells the agent how changing a logical variable propagates. Its edges carry **subjunctive dependence**, which the paper characterizes by analogy: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper gives three reference points:

- **Causal dependence is a special case.** A scribe copying a calculator's output depends on that output.
- **Two systems computing the same function both depend on it.** This covers two calculators, an agent and a twin, or an agent and a predictor's accurate model of her.
- **Mere correlation does not count.** Two calculators that happen to be pink do not depend on each other.

### 2.3 The intervention

Pearl's $\mathtt{do}$ fixes the decision node at $a$, recomputes everything downstream of it in $G$, and leaves everything else at its prior distribution. The resulting hypothetical changes "all and only those things that subjunctively depend on the output of her decision-making procedure." In the paper's type/token language, CDT intervenes on the token (this physical act) while A-FDT intervenes on the type.

### 2.4 How observations enter

Equation (4) does not condition on $\textsc{Obs}=x$. The observation enters *only* through the name of the intervened node. In the paper's words, "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

So when the agent's observation history changes from $x$ to $y$, A-FDT stops intervening on $\textsc{fdt}(\ldots,\underline x)$ and starts intervening on $\textsc{fdt}(\ldots,\underline y)$. The model's link from the decision nodes to the body therefore typically has a **router** form:

$$
\textsc{Act} = \textsc{fdt}(\underline P,\underline G,\underline{X}),
$$

where $X$ is whatever observation the world actually delivers. Since $X$ may itself depend on the intervened node through a predictor, the hypothetical can contain worlds in which the agent never sees $x$ at all.

A notational wrinkle supports this reading. In the transparent Newcomb example, the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis. Its numerical calculation, however, includes the branch where the box is empty. So the calculation follows (4) with no conditioning on $\textsc{Obs}$, and I treat (4) as authoritative.

### 2.5 Why a graph and not a "true" operator

The paper first writes an idealized rule using a $\mathtt{true}(\phi)$ operator that updates beliefs "to represent the scenario where $\phi$ is true." That would require reasoning from counterpossible antecedents, such as "this function, which in fact outputs $a_1$, outputs $a_2$." The paper admits "it's not clear how to define a $\mathtt{true}$ operator." It therefore requires that the dependency structure $G$ be supplied as an input, "in the same way that the relevant causal structure is given as an input to CDT."

A-FDT as defined by (4) is thus a **conditional** procedure: given $(P,G,x)$, the prescription is fully determined. The hard philosophical work lies in producing $G$.

## 3. A recipe for applying A-FDT

The paper does not state a checklist. The following is my distillation of its worked examples into steps that can be applied to new cases.

1. **List the decision nodes.** Write one node $F_y:=\textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might face in the problem.
2. **Wire the body.** Make $\textsc{Act}$ a function of which observation actually arrives and of the corresponding $F_y$.
3. **Wire the dependents.** For every system that computes, simulates, or reliably predicts the agent's output on input $y$, draw an edge from $F_y$ into that system. Model unreliability with a noise variable, such as "Accurate," with $P(\text{accurate})=r$. Do **not** draw edges for merely statistical correlates such as lesions or cosmic rays.
4. **Set priors on everything not downstream of the node you intervene on.** This includes the *other* decision nodes $F_{y'}$ for $y'\neq x$.
5. **Intervene and compare.** For each $a\in\mathcal A$, compute $\mathbb E(V\mid \mathtt{do}(F_x=a))$, then output the argmax.

## 4. Worked examples

All payoffs are in the paper's dollar-denominated utility.

### 4.1 Psychological twin prisoner's dilemma

Both twins' actions hang off one node $F$. Intervening $F=$ cooperate gives \$1,000,000, and $F=$ defect gives \$1,000, so A-FDT cooperates.

CDT holds the twin's action fixed. Defection then dominates by \$1,000, so CDT defects.

### 4.2 Newcomb's problem (99% reliable predictor)

The node $F$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$:

$$
\mathbb E(V\mid\mathtt{do}(F=\text{one}))=0.99\cdot 10^6 = 990{,}000,
$$

$$
\mathbb E(V\mid\mathtt{do}(F=\text{two}))=0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=11{,}000.
$$

A-FDT one-boxes. The agent believes in no retrocausation. She simply refuses to imagine her output changing while "a sufficiently competent prediction about that action" stays put.

### 4.3 Smoking lesion

This case shows why step 3 matters. The paper models the lesion as determining which utility function the agent has: $\mathcal U_S$ (likes smoking) or $\mathcal U_R$ (values smoking at $-\$1$). There are therefore two decision nodes, $F_S$ and $F_R$, and the action is routed by the lesion:

$$
\textsc{Act}(\text{lesion},s,r)=s, \qquad \textsc{Act}(\text{nolesion},s,r)=r.
$$

Cancer depends on the lesion, not on either node. Intervening on $F_S$ leaves $P(\text{lesion})=p$ unchanged. The smoke hypothetical beats the refrain hypothetical by exactly $p\cdot\$1{,}000$, which is the probability that $F_S$ is the node actually controlling the body, times the value of smoking. A-FDT smokes.

### 4.4 Transparent Newcomb (both boxes visible)

Let $q$ be the prior probability that $F_{\text{empty}}=$ two-box. The agent sees a full box and intervenes on $F_{\text{full}}$.

- **One-box.** If the predictor is accurate (prob. 0.99), the box is full and the agent one-boxes. If it is inaccurate, the box is empty and $F_{\text{empty}}$ governs the action. EU $=990{,}000+10q$.
- **Two-box.** If the predictor is accurate, the box is empty, so the payoff is $\$1{,}000$ with probability $q$. If it is inaccurate, the box is full and the agent two-boxes. EU $=10{,}010+990q$.

For every $q\in[0,1]$, one-boxing wins. (The paper's printed figure "\$110,00" is a typo for \$10,010.) This is the case where A-FDT's counterfactuals are most striking: while staring at a full box, the agent imagines two-boxing as a world in which she would probably have seen an empty one. The paper notes the problem is "precisely equivalent" to paying the driver in Parfit's hitchhiker.

### 4.5 XOR blackmail

Let $p$ be the prior probability of termites, and assume the predictor is infallible. The letter is sent iff exactly one of two things holds: no termites and the agent pays on receiving the letter, or termites and she does not.

- $\mathtt{do}(F_{\text{letter}}=\text{pay})$: the letter arrives iff there are no termites. EU $=-p\cdot10^6-(1-p)\cdot10^3$.
- $\mathtt{do}(F_{\text{letter}}=\text{refuse})$: the letter arrives iff there are termites. EU $=-p\cdot10^6$.

Refusing is better by $(1-p)\cdot\$1{,}000$. The intervention changes *whether the letter is sent*, but not the termites. CDT also refuses, though for a different reason: for CDT, the infestation is causally upstream of the act. EDT pays, because conditioning on paying makes termites impossible.

### 4.6 Mechanical blackmail with predictor error $\varepsilon$

Suppose the blackmailer mistakenly expects payment with probability $\varepsilon$.

- If $F_{\text{blackmail}}=$ pay, the agent is always blackmailed and loses \$1,000.
- If $F_{\text{blackmail}}=$ refuse, she is blackmailed with probability $\varepsilon$ and loses \$1,000,000 when that happens.

So A-FDT refuses iff $10^6\varepsilon<10^3$, that is, iff $\varepsilon<10^{-3}$.

The paper's $\varepsilon=0.0009$ case (refuse, expected loss \$900) matches this threshold. Its "0.011%" pay case does not: $0.011\% = 1.1\times10^{-4}$, which would still mean refusing. Its intended figure was presumably 0.11%. This is a numerical slip that does not affect the theory.

### 4.7 Death in Damascus

Death's appointment book is written from a perfect prediction, so it depends on $F$. Under either intervention the agent dies, and fleeing costs an extra \$1,000. A-FDT therefore stays, with no instability or need for ratification.

Now offer a truly random coin for \$1 that gives a 50% chance of escape. Buying it is a different value of $F$, and its hypothetical yields about \$500,000. On my application of (4), A-FDT buys the coin. The paper emphasizes the contrast: CDT, which imagines its location independent of Death's, values its own unrandomized options at $\max(q,1-q)\ge 0.5$ survival and declines the coin.

## 5. Counterfactuals, dominance, and the "fairness" boundary

**Counterpossibles.** A-FDT's hypotheticals are counterpossible: a deterministic function has only one output on a given input. The paper replies with a parity argument. A deterministic CDT agent's alternative *actions* are equally non-actual, and "any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

The paper also rejects the variant (FDT$'$) that iterates over alternative functions $f_n$. Predictors predict the agent's *actual* function $d$, so that variant would still need to imagine "all predictors of $d$ predict as if $d$ behaved like $f_n$."

**Dominance.** The paper argues that every method of building hypotheticals induces its own dominance relation, so dominance cannot neutrally decide between theories. Under A-FDT's relation, $a$ dominates $b$ if switching the function's output from $b$ to $a$, with subjunctive dependencies held fixed, is never worse and sometimes better. A-FDT never picks a dominated action in this sense, and CDT's two-boxing "dominance" is simply CDT's own counterfactual restated.

**Fair problems.** The paper concedes that one can construct problems that punish any particular algorithm, for example "punish anyone who acts like a copy of Fiona." Its claim is restricted to problems "where the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." It acknowledges that formalizing this notion of fairness is open.

## 6. What Equation (4) leaves open, and how I propose to operationalize it

### 6.1 Where does $G$ come from? (open in the source)

The paper is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

*My operational proposal:* draw an edge $F_y\to Z$ when, in the agent's best model of $Z$'s mechanism, two conditions hold:

1. $Z$ is computed from a representation of the agent's decision procedure evaluated on input $y$, as with predictors, simulators, copies, and twins.
2. Substituting a different input–output behavior into that representation would change $Z$.

Reliability is then a noise node rather than a weakened edge. Pure common-cause correlations, such as lesions, genes, or cosmic rays, do not qualify unless the common cause *computes* the decision.

This is a modeling heuristic, not a definition. Hard cases remain: partial or approximate simulations, and agents running *similar but non-identical* algorithms. For these I would use a mixture. The other agent's output equals $F$ with probability $s$ (my credence that it effectively computes the same function on the same input), and otherwise follows an independent prior. This is an added assumption that the paper does not endorse.

### 6.2 Which $P$? (underdetermined)

Equation (4) never conditions on $x$. That raises the question of what state of information $P$ represents.

If $P$ had already been updated on "box B is full," then intervening on $F_{\text{full}}=\text{two}$ could not make the box empty, and the transparent-Newcomb result would collapse. The paper's footnote on TDT names exactly this hazard: TDT "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

*My reading:* $P$ should be the agent's distribution **before** any observation whose occurrence depends on her decision nodes. Information that is subjunctively independent of $F$ can be conditioned on harmlessly, because the intervention would not change it anyway. Information downstream of $F$ must enter only through the choice of node.

### 6.3 Priors on the non-intervened decision nodes (left free)

In the paper's examples, the priors $q$ on other nodes, such as $F_{\text{empty}}$ or $F_R$, do not affect the answer. The paper says the "correct" values are 1 and 0 respectively, "as you may verify." In general, however, they can matter, because $\mathtt{do}(F_x=a)$ leaves $F_{x'}$ at its prior. Graphically, A-FDT treats its outputs on different inputs as separate variables.

Here is an example of my own construction. Two exact copies of an agent receive different inputs: one sees "red," the other sees "blue." Each picks A or B. The payoffs are 10 to each if both pick A, 5 each if both pick B, and 0 otherwise. Let the red copy's prior be $s=P(F_{\text{blue}}=B)$. Then A-FDT gives

$$
\mathbb E(V\mid\mathtt{do}(F_{\text{red}}=A))=10(1-s),\qquad \mathbb E(V\mid\mathtt{do}(F_{\text{red}}=B))=5s.
$$

So if $s>2/3$, the red copy picks B. By symmetry the blue copy does too, and the belief $s=1$ is then *self-fulfilling*. A-FDT can be stuck at the inferior coordinated outcome, depending on its self-model. Policy-selecting FDT chooses the whole map $\{\text{red},\text{blue}\}\to\{A,B\}$ at once and picks (A, A).

This fits the paper's remark that action versus policy "makes a difference in certain multi-agent dilemmas." It also shows that A-FDT, applied literally, needs a further rule for these priors.

*My proposal* is to require the priors on $F_{x'}$ to be a fixed point: they should equal A-FDT's own output on $(P,G,x')$. Where several fixed points exist, as here, A-FDT alone does not select among them. That is a genuine limitation of the action formulation, and it is one reason to prefer the policy variant.

### 6.4 Smaller details

- **Ties.** Ties in the argmax are unspecified.
- **Zero-probability actions.** Unlike EDT, which "does not consider" actions of probability zero, $\mathtt{do}$ is defined for every $a$. A-FDT therefore does not suffer the Spohn-style problem of being forced into an action by an extreme prior. The paper uses this point against EDT in its cosmic-ray problem.
- **Tractability.** The paper explicitly studies an idealization. Real agents would approximate it.

## 7. Conclusion

A-FDT is Pearl-style CDT with a different intervention point. The agent does not intervene on her physical act. She intervenes on the logical variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ that represents her algorithm's output on her actual input, and she lets the change propagate to everything that computes or predicts that output.

Observations select *which* node to intervene on instead of being conditioned on. As a result, hypotheticals can include worlds in which the agent would have seen something else. This single rule yields:

- one-boxing in Newcomb's problem, including the transparent version;
- smoking in the smoking lesion problem;
- paying the driver in Parfit's hitchhiker;
- refusing both kinds of blackmail;
- cooperating with a twin;
- staying calmly in Damascus.

The prescriptions are exact once $(P,G)$ is fixed. The open questions sit in the inputs, and the paper names the main one itself: how to construct the subjunctive-dependence graph. Applying the action formulation also requires settling the prior state $P$ and the priors on the agent's outputs for other inputs. My proposals are (i) a mechanism-based test for edges, (ii) an observation-independent prior, and (iii) fixed-point priors on the other decision nodes. They make A-FDT usable on unfamiliar cases, but they go beyond the source. The coordination example shows that the action formulation can leave an equilibrium-selection gap that the authors' preferred policy formulation closes.

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.