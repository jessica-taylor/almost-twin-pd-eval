# 004_fdt_eq4_anthropic_claude-opus-5.5_rmedium_pmedium / 00027

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/d41ac97b-ecd1-4d2b-8347-741f7da56000/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/d41ac97b-ecd1-4d2b-8347-741f7da56000/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Action Functional Decision Theory, Its Definition, Mechanics, and Open Seams

## 1. What this essay covers

Yudkowsky and Soares (2017) propose *functional decision theory* as a third expected-utility theory, alongside causal decision theory (CDT) and evidential decision theory (EDT). Their slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper gives one formal decision rule, Equation (4) of Section 5. In it the agent intervenes on a variable whose value is an **action**. Two footnotes (7 and 16) add that the authors' "preferred formalization" instead selects a **policy**, a map from observations to actions. They say the difference "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." To keep the two apart, I call the action-level rule of Equation (4) **A-FDT** (action functional decision theory). I call the policy-level variant mentioned in the footnotes **policy-selection FDT**. This essay is about A-FDT.

I mark three kinds of claims throughout:
- what the source says,
- what follows from its equations,
- what I am adding as an operational proposal.

## 2. The common frame: expected utility with a free "hypothetical" connective

All three theories maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history. Here $P(a \hookrightarrow o_j; x)$ is the probability of outcome $o_j$ "in the hypothetical scenario where the action $a$ is executed after receiving observations $x$" (Eq. 1). Following Joyce, the source treats the interpretation of $\hookrightarrow$ as the only free parameter. Decision theories "disagree about the epistemic perspective from which actions are to be evaluated," not about value.

Procedurally, the agent holds a world-model $M$. For each candidate $a$ she builds a hypothetical $M^{a\hookrightarrow}$, scores it, and takes the argmax. Each theory fixes how that hypothetical is built:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. The hypothetical is Bayesian conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. The model is a Pearl-style pair $(P,G)$, and the hypothetical is graph surgery on the physical action node.

## 3. The definition of A-FDT

**Equation (4)** defines

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

I read this equation as the definition of A-FDT. Its ingredients are as follows.

1. **The model $(P,G)$.** $P$ is a joint distribution over variables, and $G$ is a directed graph. Unlike CDT's graph, $G$ is meant to encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, it must say "how changing a logical variable affects all other variables."

2. **The decision node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** This is a variable in the model representing the output of the A-FDT algorithm on inputs $(P,G,x)$. The underlines denote dequoting: the variable's *name* is built from the agent's own model and observation. The source calls this self-reference harmless. The agent needs only a variable *representing* the output, not its value, and Kleene's recursion theorem shows such self-representing structures exist.

3. **The intervention.** Pearl's $\mathtt{do}$ sets the decision node to $a$, cuts its incoming edges, and recomputes everything downstream in $G$. Downstream nodes include the agent's physical action and every predictor, twin, or simulation that computes the same function.

4. **The value.** $V=\mathcal U(\textsc{Outcome})$, and the agent takes the argmax over $a\in\mathcal A$.

The source draws two contrasts with CDT.
- **What is intervened on.** CDT intervenes on the token (the physical act). A-FDT intervenes on the type (the output of the function).
- **How observations enter.** "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Equation (4) contains no "$\textsc{Obs}=x$" to the right of the bar. The observation appears only inside the *name* of the intervened variable.

This second feature is what makes A-FDT "updateless" in the cases below. Its hypotheticals may contain worlds in which the agent never sees $x$.

**Agreement condition (source).** Suppose every correlation between $\textsc{Act}$ and other variables runs causally out of $\textsc{Act}$, except its dependence on the decision node. Then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

so EDT, CDT and A-FDT coincide. They come apart only when something else in the world tracks the agent's decision: predictors, copies, simulations, or one's own future instances.

## 4. Subjunctive dependence: what goes into $G$

Everything interesting in A-FDT lives in $G$. The source's guiding notion is **subjunctive dependence**. When two physical systems compute the same function, their behaviours "subjunctively depend" upon that function, like two calculators computing $6288+1048$. The source distinguishes three relations:

- **Causal dependence is a special case.** A scribe copying a calculator's output would write something different if the output differed.
- **Mere statistical correlation is not subjunctive dependence.** Two calculators that happen to be pink are an example. So is a lesion that causes both smoking and cancer, since "the cancer is not evaluating the agent's future decisions."
- **The governing constraint.** When the agent imagines different outputs, "she imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

The source openly declines to say *how* to find these dependencies. It calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem." Building $G$ is therefore part of the problem specification, just as the causal graph is for CDT.

**An operational recipe (my proposal, distilled from the paper's worked graphs).** To model an unfamiliar problem for A-FDT:

1. **List the agent's possible inputs.** For each relevant observation history $y$ the agent might face, add a node $\textsc{fdt}(\underline P,\underline G,\underline y)$.
2. **Wire up every place that computes or reliably predicts the function on input $y$.** Draw an edge from the corresponding node to each predictor's prediction, a twin's action, a future self in the same epistemic situation, and so on. Model a predictor's error rate as a separate noise parent (like the paper's $\textsc{Accurate}$).
3. **Route the physical action through a selector.** $\textsc{Act}$ becomes a deterministic function of the decision nodes together with whatever variables determine which input the agent actually receives. In the transparent-Newcomb graph, for example, $\textsc{Prediction}$ selects which decision node "controls" $\textsc{Act}$.
4. **Leave merely correlated variables as ordinary parents** that the decision nodes do not touch, such as lesions and genes.
5. **Give priors to the decision nodes you will not intervene on.** These represent the agent's beliefs about what she would do on other inputs.
6. **Intervene only on the node for the actual input $x$,** do not condition on $\textsc{Obs}=x$, and take the argmax.

## 5. Worked examples

All dollar figures stand for utilities.

### 5.1 Newcomb's problem

A predictor with 99% accuracy fills box B with \$1M iff it predicts one-boxing. Box A holds \$1,000.

In $G^F$, the decision node $\textsc{fdt}(\underline P,\underline G)$ is a parent of both $\textsc{Act}$ and $\textsc{Prediction}$. Intervening gives:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)=990{,}000,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] &= 0.99(1{,}000)+0.01(1{,}001{,}000)=11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT instead intervenes on $\textsc{Act}$, which is downstream of $\textsc{Prediction}$'s parent but not upstream of it. For any probability $p$ that the box is full, CDT therefore sees two-boxing as \$1,000 better.

The source answers the objection that a confident one-boxer should "notice" the box is probably full and grab both. To evaluate two-boxing, Fiona (the paper's A-FDT agent) must imagine the *function* outputting *twobox*. In that counterpossible world the predictor's prediction changes too. No retrocausation is involved, only the logical tie between two computations of one function.

### 5.2 Smoking lesion

Here the lesion causes both the love of smoking and (99% of the time) cancer.

The source's careful formalization has the lesion fix which utility function is in force, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$. It therefore fixes which of two decision nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. Crucially, no edge runs from either decision node to $\textsc{Cancer}$.

Let $p = P(\textit{lesion})$ and let $q$ be the prior that the other node outputs *smoke*. Intervening on the $S$-node changes nothing about $\textsc{Lesion}$, so the two options differ only in the smoking pleasure:

$$
\mathbb E[V\mid\mathtt{do}(\textit{smoke})]-\mathbb E[V\mid\mathtt{do}(\textit{refrain})] = p\cdot 1{,}000 > 0.
$$

A-FDT smokes. So one rule both one-boxes and smokes, which Gibbard and Harper had argued no rational agent could do. The difference between the two problems lies entirely in $G$: a predictor models the function, while a lesion does not.

### 5.3 Transparent Newcomb (equivalently, Parfit's hitchhiker)

Both boxes are visible. Box B was filled iff the predictor predicted one-boxing *upon seeing it full*.

The graph has two decision nodes:
- $\textsc{fdt}_{\text{full}}$, which feeds both $\textsc{Prediction}$ and $\textsc{Act}$;
- $\textsc{fdt}_{\text{empty}}$, which feeds only $\textsc{Act}$.

$\textsc{Prediction}$ selects which node drives the act. Let $q$ be the prior that the agent two-boxes on seeing an empty box. Seeing a full box, A-FDT computes:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}_{\text{full}}=\textit{onebox})] &= 0.99(1{,}000{,}000) + 0.01\cdot q(1{,}000) = 990{,}000 + 10q,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}_{\text{full}}=\textit{twobox})] &= 0.01(1{,}001{,}000) + 0.99\cdot q(1{,}000) = 10{,}010 + 990q.
\end{aligned}
$$

A-FDT one-boxes for every $q\in[0,1]$. (The source prints the second figure as "\$110,00 + q·\$990"; the arithmetic gives \$10,010.)

**A notational wrinkle.** In this example the source writes the objective as "$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\underline{P^F},\underline{G^F},\textit{full})=a, \textsc{Obs}=\textit{full})$," with an unbalanced parenthesis. Read literally, this conditions on the full-box observation. But the source's own computation includes the branch in which the box is *empty*, which would have probability zero after conditioning on $\textsc{Obs}=\textit{full}$. The text also says explicitly that the agent "does not react to observations by conditioning." So I treat the printed "$\textsc{Obs}=\textit{full}$" as a typographical slip and follow Equation (4) as stated, with no conditioning on $\textsc{Obs}$. This matters: conditioning *and* relocating the intervention is the "double update" that the source attributes to Timeless Decision Theory (Yudkowsky 2010) as harmful.

The source argues that one-boxing here is the same as paying the driver in Parfit's hitchhiker. In both cases a \$1M benefit was granted iff the agent was predicted to forgo \$1,000 in the later situation.

### 5.4 XOR blackmail

A reliable predictor sends a letter iff exactly one of the following holds:
- there are no termites *and* the agent will pay \$1,000;
- there are termites *and* the agent won't pay.

EDT pays, because conditioning on paying makes termites impossible.

A-FDT intervenes on $\textsc{fdt}_{\text{letter}}$. That node feeds the predictor and therefore whether the letter is sent, but $\textsc{Infestation}$ is a root it cannot touch. Let $t=P(\textit{termites})$ and let $D=1{,}000{,}000$ be the termite damage. Ignoring behaviour on the no-letter node, which incurs no cost either way:

- **Policy "pay":** termite damage $tD$, plus a payment of \$1,000 with probability $1-t$, because the letter arrives exactly when there are no termites.
- **Policy "refuse":** termite damage $tD$ only.

A-FDT refuses. CDT also refuses, but for a different reason. Its hypothetical keeps the letter fixed and imagines the inerrant predictor having erred. The source treats this difference in hypotheticals, despite agreement in action, as diagnostic of CDT's deeper flaw.

### 5.5 Mechanical blackmail with an imperfect predictor

A blackmailer runs a damaging program (cost \$1M) iff she predicts payment. Paying \$1,000 stops it. Suppose she wrongly predicts payment with probability $\varepsilon$.

Intervening on the node for "blackmailed":
- **Pay:** blackmailed with probability $\approx 1$, so the loss is $\approx 1{,}000$.
- **Refuse:** blackmailed only by error, so the expected loss is $\varepsilon\cdot 10^6$.

Refusing is better iff $\varepsilon < 10^{-3}$. This matches the source's first case: at $\varepsilon=0.0009$, Fiona refuses and loses \$900 in expectation.

The source also says that with error "0.011%" she pays. That does not fit the threshold, since $0.00011 < 10^{-3}$. Presumably 0.11% was intended. The general lesson is unaffected. A-FDT will refuse while holding a letter it knows was sent in error, "because it's advantageous to be the kind of agent that makes such decisions."

### 5.6 Death in Damascus

Death predicts perfectly. Death's location node is a child of the decision node, so A-FDT's two hypotheticals are:
- "flee and die in Aleppo": $-1{,}000$, plus death;
- "stay and die in Damascus": death only.

A-FDT stays and saves \$1,000, with no instability.

CDT's hypotheticals hold Death's location fixed while its action varies, so its choice oscillates under reflection. The source argues further that a CDT agent who has settled on a belief behaves as though its survival chance were $\max(q,1-q)\ge 0.5$. It would therefore decline to pay \$1 for a truly random coin that offers a genuine 50% escape.

## 6. How A-FDT treats counterfactuals

Three features follow directly from the equation and the examples.

**Counterpossibles.** For the actual input, the decision function has exactly one output, as a matter of logical necessity. So at least one of A-FDT's hypotheticals is counter-to-logic. The source openly acknowledges this. An idealized operator $\mathtt{true}(\phi)$ for conditioning on logical sentences is undefined, which is why Equation (4) borrows $\mathtt{do}$ and requires the logical dependency structure to be supplied in $G$.

The source rejects a workaround, "FDT′," which would evaluate replacing one's function with an alternative $f_n$. The problem is that predictors predict $d$, not $f_n$. One would have to imagine all predictors of $d$ predicting as if $d$ behaved like $f_n$, which is the same counterpossible again.

**Observations relocate rather than filter.** CDT asks what happens given $x$ if the act varies. A-FDT asks what the whole world looks like if the function's output on input $x$ varies, including whether $x$ is ever received. Hence the source's slogan that A-FDT agents "act as they would have precommitted to act." It also explains why the source claims A-FDT never assigns negative value to information.

**A dominance notion of its own.** The source argues that each way of building hypotheticals induces its own dominance principle. Let $a$ A-FDT-dominate $b$ when, holding subjunctive dependencies fixed, switching the function's output from $b$ to $a$ is never worse and sometimes better. Under that definition A-FDT never chooses a dominated act. CDT-dominance (two-boxing) is then "merely a restatement of CDT's method," not a neutral criterion. The source therefore makes utility achieved across "fair" problems the arbiter, where a fair problem is one whose outcome depends only on the agent's behaviour in the problem at hand.

## 7. What Equation (4) leaves open, and how one might close it

### 7.1 Constructing $G$

This is the largest gap, and the source flags it as such. Equation (4) is correct *given* a graph that represents logical dependence. In practice, the user of A-FDT must answer one question in every case: *which variables would differ if this function's output on this input differed?* Two heuristics consistent with the source:

- the computational-similarity test (does this process model or run my reasoning on this input?);
- the lesion test (would this variable "evaluate" my decision?).

Hard intermediate cases remain unresolved. Examples include agents running *similar but non-identical* algorithms, or a predictor that is merely statistically good. I suggest representing partial dependence by a noise parent, as the source does with $\textsc{Accurate}$. That is a modelling choice, not something the source derives.

### 7.2 Priors on the decision nodes not intervened on

In every example the source checks, the parameter $q$ (behaviour on other inputs) is irrelevant. That was true above for all $q$. It is not true in general.

Equation (4) intervenes on a single node and leaves the others distributed according to $P$. So A-FDT is defined relative to the agent's beliefs about her own behaviour elsewhere. The source suggests these beliefs should be accurate: "the correct $q$ is 0 [or 1], as you may verify." The natural operational completion, which is my proposal, is a **consistency requirement**. The prior on each node $\textsc{fdt}(\underline P,\underline G,\underline y)$ should put its mass on what Equation (4) itself returns for input $y$. The resulting profile of actions is then a fixed point, an equilibrium among the agent's own input-instances.

### 7.3 Where A-FDT and policy-selection FDT diverge

A fixed point need not be optimal. Here is an illustration of my own, of the sort footnotes 7 and 16 gesture at.

- Two exact copies of the agent are shown different colours, red or blue.
- Each picks $X$ or $Y$.
- Both receive 1 if both choose $X$, 2 if both choose $Y$, and 0 if they differ.

The red-copy's A-FDT intervenes on $\textsc{fdt}_{\text{red}}$ while holding $\textsc{fdt}_{\text{blue}}$ at its prior. Say the prior gives $P(\textsc{fdt}_{\text{blue}}=X)=r$. Then $X$ is better iff $r > 2/3$.

So the profile (X, X) is self-consistent: each instance correctly expects the other to play $X$ and best-responds. Policy-selection FDT instead maximizes over the whole map {red ↦ ·, blue ↦ ·} at once and picks (Y, Y).

A-FDT thus inherits equilibrium-selection problems whenever several of its own input-nodes jointly determine the outcome. This fits the source's remark that the difference shows up in multi-agent dilemmas. A user of A-FDT should check whether more than one decision node feeds the payoff-relevant variables. If none does, as in all of the paper's examples, A-FDT and policy-selection FDT agree.

### 7.4 Ties, randomization, and computational limits

The source says nothing on these points. I would treat them as follows:

- **Ties:** any argmax is admissible.
- **Randomization:** model a coin flip as an ordinary chance node downstream of the decision node. A predictor who can predict the coin is then wired accordingly, matching the source's treatment of Death predicting pseudorandomness.
- **Tractability:** the source studies idealized agents and expects bounded approximations to inherit "similar strengths and weaknesses."

### 7.5 Fairness

The source concedes that some problems can punish any theory, for instance "punish whoever acts like Fiona's copy." It claims A-FDT does at least as well as its rivals on *fair* problems, but it does not formalize fairness. Claims about A-FDT's general superiority are therefore conjectures relative to an undefined class of problems.

## 8. Conclusion

A-FDT is expected-utility maximization in which the hypothetical for action $a$ is formed by intervening, in a graph of causal *and* logical dependence, on the node representing "the output of this very algorithm on my present input." It does not condition on that input.

Two design decisions give A-FDT its distinctive verdicts:
- **intervening on type rather than token**, which yields one-boxing, twin cooperation, and stability in Death in Damascus;
- **relocating rather than conditioning on observations**, which yields paying the hitchhiker's driver, one-boxing in transparent Newcomb, and refusing mechanical blackmail. It still respects mere correlations, so it smokes and refuses XOR blackmail.

The procedure is precise once $(P,G)$ is given. What remains open is mostly how to build $G$: identifying subjunctive dependencies and assigning beliefs to one's own off-input behaviour. Where several of one's own input-nodes interact, the action-level A-FDT can settle on suboptimal self-consistent profiles. That is exactly the gap the authors' preferred policy-selection variant is meant to close.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out what an essay on A-FDT should center on, taking Equation (4) as the main formal statement: intervening on the fdt(P,G,x) node to choose an action from A. The footnotes also mention that the authors prefer a policy-based version, so I'm weighing how to set the action version apart from a policy-level one.

I'm settling on the word count, roughly 2,400 to 3,000, and planning which examples to cover: the Newcomb-style cases, Death in Damascus, and the blackmail variants. I also want to list the open questions, such as how to build the graph, whether observations get conditioned on, and where the action and policy versions diverge.

I'm checking the transparent Newcomb calculation against the paper's notation. The Do-expression seems to drop the closing parenthesis, but the computation itself never conditions on the full box being observed, since it works through the branch where the box is empty. So I'll read Equation (4) as the authoritative form and note the discrepancy in the essay.

I'm checking the transparent Newcomb payoffs now: one-boxing gives about 990,000 in expectation, while two-boxing comes to roughly 11,000 once I account for the predictor's accuracy. I also want to flag that one of the paper's stated figures for the EDT agent looks like a typo, since the one-box calculation actually yields 990,000 rather than 999,000.

I'm running through the smoking lesion case next, where smoking and not smoking differ by about p·1000 in expected payoff, and checking that the paper's figure for the lesion branch works out. I'm also starting to think about where A-FDT and policy-level FDT come apart, especially in problems where the payoff depends on the agent's choices across several observation situations at once, since each node holding the others fixed at their priors might lead to coordination failures.

I'm now sketching a concrete multi-agent case to show where the action version and the policy version come apart: two copies of the agent see different inputs and are rewarded for matching actions, with one matching option worth more. Holding the other copy at its prior, the action-level intervention can lock into the weaker coordinated outcome, which is the kind of divergence the footnotes point to.

I'm checking the mechanical blackmail numbers next: with a small predictor error, refusing to pay costs an expected amount that compares against the $1,000 payment. The paper's stated threshold looks off in one spot, since a smaller error rate would make refusing the better choice, not paying.

I'm checking the blackmail threshold now: the predictor error needs to sit around one in a thousand before refusing becomes the better choice, and the paper's printed figure looks like it should be read as 0.11% rather than 0.011%. Next I'm planning the essay's structure, starting with the naming of A-FDT against the policy-selection variant, then the setup and the component-by-component reading of Equation (4).

I'm laying out the essay's remaining sections: building the graph and handling observations, working through the examples including the blackmail threshold, then the open questions like coordination across multiple inputs, counterpossibles, and fairness, before a short conclusion.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/fc76c3e5-22eb-44dd-8cf5-295b33d185b5/call_0/request.json)

[Authoritative raw response](../../../../../../runs/fc76c3e5-22eb-44dd-8cf5-295b33d185b5/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under the essay's A-FDT**

1. **My decision node.** My observation history includes "I am Rowan" and my specific lead about Sasha. So under the essay's recipe (§4, steps 1 and 6), I intervene only on the node fdt(P, G, x_Rowan).

2. **The other prisoner's node.** Sasha's copy receives a different input: a different name and a different lead, so a different letter. Its action is governed by a separate node, fdt(P, G, y_Sasha). Equation (4) leaves that node at its prior; the intervention does not move it. This is the same structure as the red/blue example in §7.3, where the A-FDT intervention on one input-node does not move the other.

3. **Comparing my options.** Let r be the prior that Sasha's node outputs "send."
   - Pass: −(2(1−r) + 5r) = −2 − 3r
   - Submit: −(0(1−r) + 4r) = −4r

   Submitting is better by 2 − r, which is at least 1 for every r in [0, 1]. Submitting therefore dominates whatever I believe about the other node.

4. **Consistency check (§7.2).** By symmetry, Sasha's node returns "submit" too. So the self-consistent prior is r = 1, and submitting remains the best response. The fixed point is both prisoners submitting, at 4 years each. This is the kind of suboptimal self-consistent profile the essay warns action-level A-FDT can settle on; policy-selection FDT might instead coordinate on mutual silence. I was told to apply A-FDT as the essay interprets it, so I follow its verdict.

**Command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma where both copies see different inputs, so the other copy's decision is a separate node. Under A-FDT I intervene only on my actual input, and I'm weighing whether the other node still counts as subjunctively dependent given that the differences look irrelevant.

I'm settling on A-FDT defecting here: the essay says different inputs mean separate decision nodes, and in a prisoner's dilemma defection dominates whatever the other node is held at. I'm setting aside the argument that the differences are payoff-irrelevant, since the essay explicitly treats different observation histories as different nodes, and I'll go with submit.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/fc76c3e5-22eb-44dd-8cf5-295b33d185b5/call_1/request.json)

[Authoritative raw response](../../../../../../runs/fc76c3e5-22eb-44dd-8cf5-295b33d185b5/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Choice: submit the letter.**

Under A-FDT as the essay interprets it, I intervene only on the decision node for my own input, fdt(P, G, x_Sasha). Rowan's copy gets different private observations (a different name and a different lead), so its output is a separate node, fdt(P, G, x_Rowan). The essay's red/blue example treats exactly this case: two exact copies shown different inputs. There the other copy's node is not intervened on and is held at its prior.

Let r be the prior probability that Rowan sends a letter. Then:

- **Pass:** 2(1−r) + 5r years
- **Submit:** 0(1−r) + 4r years

Submitting is better by 2 − r years, which is at least 1 year for every r. So it is the argmax whatever the prior. The essay's consistency requirement (§7.2) then sets the prior on Rowan's node to "submit," and (submit, submit) is the self-consistent profile.

Policy-selection FDT, which chooses the whole map from inputs to actions at once, would choose mutual silence. But I was told to use A-FDT, and the essay says plainly that A-FDT can settle on worse self-consistent profiles like this one when several of one's own input-nodes jointly affect the outcome.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing whether, under A-FDT, the other copy's decision node counts as subjunctively dependent on mine, since it takes a different input but the inputs differ only in irrelevant details.

Under A-FDT, the other copy's node is held fixed as a separate node, since the essay's red/blue example treats different observations as distinct. Given any fixed prior, submitting dominates here, so separate nodes lead to defection, while policy-selection would cooperate. Still, the essay's own example points toward treating the copies as separate, so I'll submit.

```
