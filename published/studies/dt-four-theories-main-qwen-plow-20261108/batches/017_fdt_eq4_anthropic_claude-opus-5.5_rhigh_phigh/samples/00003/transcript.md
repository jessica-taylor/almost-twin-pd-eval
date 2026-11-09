# 017_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00003

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/791f1f5f-77cc-4237-91d8-e83c26779190/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/791f1f5f-77cc-4237-91d8-e83c26779190/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Decision Function

## 1. What is being explained, and under what name

Yudkowsky and Soares's paper *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes that a rational agent should treat its decision as the output of a fixed mathematical function. The agent then asks, in the paper's words, "Which output of this very function would yield the best outcome?"

The paper calls its theory "FDT." Its formal definition in Section 5, Equation (4), has the agent choose an action, a single element of the action set $\mathcal A$. Two footnotes (7 and 16) say the authors actually prefer a different formalization, in which the agent chooses a *policy*, a map from observations to actions. They add that this "makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." To keep the two apart, this essay uses:

- **A-FDT (action functional decision theory)** for the action-selecting rule of Equation (4);
- **policy-selection FDT** for the variant the footnotes mention;
- **CDT** and **EDT** for causal and evidential decision theory.

Direct quotations from the paper keep its word "FDT." The theory they describe is the one formalized as Equation (4), which is A-FDT here.

The plan is as follows. Section 2 sets up the expected-utility framework. Section 3 states the A-FDT equation and explains each part. Section 4 explains subjunctive dependence and proposes a recipe for building the required graph. Section 5 works through standard cases. Section 6 takes up the questions the paper leaves open, including one where I argue that A-FDT and policy-selection FDT come apart.

## 2. The common framework: expected utility over hypotheticals

EDT, CDT, and A-FDT all maximize expected utility in the general form

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $a \hookrightarrow o_j$ is a *decision hypothetical*: "if $a$ were done after observations $x$, outcome $o_j$ would obtain." Following Joyce's representation theorem, the paper treats the interpretation of "$\hookrightarrow$" as the free parameter that separates rival theories. Quoting Joyce, decision theories disagree "about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent keeps a world-model $M$. For each option it builds a hypothetical: a transformed copy of $M$ showing how the world would look if that option were taken. It then scores each hypothetical by expected utility. Writing $V := \mathcal U(\textsc{Outcome})$, the two rivals are:

$$
\text{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big), \tag{2}
$$
$$
\text{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big). \tag{3}
$$

EDT builds hypotheticals by conditioning. CDT builds them by Pearl-style surgery on the physical action node $\textsc{Act}$ of a causal graph $G$.

## 3. The A-FDT equation

### 3.1 Statement

A-FDT keeps CDT's surgical machinery but moves the point of surgery:

$$
\text{A-FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}
$$

The ingredients are:

1. **$P$**: a joint distribution over world variables. Unusually, it also contains variables for the *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, with most of its probability on $7336$.
2. **$\textsc{fdt}(\underline P,\underline G,\underline x)$**: a variable whose name is determined by the agent's own model and observations (the underline means "dequoting"). It represents "what the A-FDT algorithm outputs on input $(P,G,x)$." The self-reference is harmless. The agent needs only a variable *representing* its output, not knowledge of the output's value, and Kleene's recursion theorem guarantees such self-representing structures exist.
3. **$G$**: a graph that encodes causal structure and also "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, $G$ says which variables change when the logical node $\textsc{fdt}(\cdot)$ changes.
4. **$\mathtt{do}$**: Pearl's operator. It sets the node, discards whatever prior probability the node had, and propagates the change only along outgoing edges of $G$.

For brevity, write $F_x$ for $\textsc{fdt}(\underline P,\underline G,\underline x)$.

### 3.2 Two structural differences from CDT

The paper names exactly two differences between (3) and (4).

**Type versus token.** CDT intervenes on the physical act. A-FDT intervenes on the function's output, which may be instantiated in many places: the agent's body, a twin's brain, a predictor's simulation. In the paper's Peircean phrasing, CDT intervenes on the token and FDT on the type. The slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*"

**Observations select the node instead of being conditioned on.** When CDT's observation history changes from $x$ to $y$, CDT changes which event it conditions on. A-FDT instead changes which node it intervenes on, from $F_x$ to $F_y$. Notice that Equation (4) has no "$\textsc{Obs}=x$" to the right of the bar. In the graph, the actual act is wired as a *switch*: $\textsc{Act}$ copies $F_y$ for whichever observation $y$ the upstream world actually produces. So when the agent evaluates a hypothetical, it is free to find that, had its function output something else, it would have *seen* something else.

### 3.3 When A-FDT agrees with its rivals

The paper notes that if every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on $F$, then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid\mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)],
$$

and all three theories agree. A-FDT departs from CDT and EDT only where something other than the act's causal consequences correlates with the act: predictors, twins, copies, or lesion-like common causes.

## 4. Subjunctive dependence and how to draw $G$

A-FDT gets its content from deciding which variables are children of $F_x$. The paper's criterion is *subjunctive dependence*. "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." It gives three paradigm cases:

- **Causal dependence is a special case.** A scribe copying a calculator's output would write something different if the output were different.
- **Mere statistical correlation is excluded.** A pink calculator in Paris and a coincidentally pink one in Tokyo are not linked; repainting one leaves the other pink.
- **A predictor depends on what it accurately models.** It "contain[s] an accurate *mental representation*" of the agent's decision function, so in effect the agent "has a 'twin' inside the predictor's mind."

The paper explicitly declines to give a procedure for discovering these dependencies. It calls this "perhaps the largest open problem in the study of functional decision theory." Anyone applying A-FDT to a new case therefore needs some operational rule. **The following recipe is my own proposal, not the paper's**, though it reproduces every graph the paper draws:

1. **List the observation histories** $x$ under which the agent might run its decision procedure. Create a node $F_x$ for each.
2. **Wire the agent's own act as a switch.** $\textsc{Act} = F_{\textsc{Obs}}$, where $\textsc{Obs}$ is determined by the upstream world.
3. **Find every system that computes or models the function.** For each process in the environment, ask whether its behavior is produced by computing, simulating, or reasoning about what this function outputs on some input $x$. If so, draw $F_x \to$ that process. Model imperfect fidelity with an independent noise parent, like the paper's $\textsc{Accurate}$ node.
4. **Leave purely statistical correlates unconnected to $F$.** Lesions, genes, and coincidences connect through ordinary causal parents only.
5. **Intervene and compute unconditionally.** Evaluate $\mathbb E(V\mid\mathtt{do}(F_x=a))$ under the prior, without conditioning on $\textsc{Obs}=x$ (see §6.2).

Step 3 is the substantive judgment. A useful test is the paper's calculator analogy: would a well-functioning version of this process give a different answer if the arithmetic came out differently?

## 5. Worked examples

All payoffs are in utility-dollars. Where my arithmetic differs from the paper's typeset numbers, I say so.

### 5.1 Twin Prisoner's Dilemma and Newcomb's Problem

**Twin Prisoner's Dilemma.** Both twins' acts are children of the same node $F$. Then:

- $\mathtt{do}(F=\text{cooperate})$ yields mutual cooperation, worth \$1,000,000.
- $\mathtt{do}(F=\text{defect})$ yields mutual defection, worth \$1,000.

A-FDT cooperates. CDT cuts the link between the twins and defects.

**Newcomb's Problem** (99% accurate predictor). Fiona's graph has $F \to \textsc{Act}$ and $F \to \textsc{Prediction}$, with $\textsc{Accurate}$ also feeding $\textsc{Prediction}$. Then:

$$
\mathbb E(V\mid\mathtt{do}(F=\text{one})) = 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,
$$
$$
\mathbb E(V\mid\mathtt{do}(F=\text{two})) = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.
$$

A-FDT one-boxes. The paper stresses that this reasoning involves no retrocausation. Fiona does not believe a signal travels back in time. She judges it "foolish to imagine her action changing without also imagining" the function's output, which the predictor tracks, changing as well.

### 5.2 Smoking Lesion

Here the lesion is a common cause of the urge to smoke and of cancer. Nothing computes the agent's decision function in order to decide whether cancer develops, so $F$ has no edge to $\textsc{Cancer}$.

The paper formalizes this carefully. The lesion determines which utility function, and hence which decision node ($F_S$ or $F_R$), controls the act. Intervening on $F_S$ leaves $P(\text{lesion})=p$ unchanged, and smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes.

This is how the paper meets Gibbard and Harper's challenge: a single rule both one-boxes and smokes. The paper also argues that the problem is "badly confused" and recommends retiring it.

### 5.3 Transparent Newcomb and Parfit's Hitchhiker

**Transparent Newcomb.** Box B is visible. The predictor fills it iff it predicts one-boxing *upon seeing a full box*. On seeing a full box, the agent intervenes on $F_{\text{full}}$. The predictor's prediction depends on $F_{\text{full}}$, and an empty box would route the act to $F_{\text{empty}}$. Let $q$ be the prior probability that $F_{\text{empty}}$ two-boxes. Then:

- $\mathtt{do}(F_{\text{full}}=\text{one})$: $0.99(1{,}000{,}000) + 0.01\,q(1{,}000) = 990{,}000 + 10q$.
- $\mathtt{do}(F_{\text{full}}=\text{two})$: $0.01(1{,}001{,}000) + 0.99\,q(1{,}000) = 10{,}010 + 990q$.

(The paper prints the second figure as "\$110,00 + q·\$990," which appears to be a typo for \$10,010.)

A-FDT one-boxes even while looking at the full box. In its hypothetical where it two-boxes, it would most likely have been shown an empty box.

**Parfit's Hitchhiker** has the same structure. The driver predicts whether the agent will pay once in the city:

- $\mathtt{do}(F_{\text{city}}=\text{pay})$: $0.99(-1{,}000) + 0.01(-1{,}000{,}000) = -10{,}990$.
- $\mathtt{do}(F_{\text{city}}=\text{refuse})$: $0.99(-1{,}000{,}000) + 0.01(0) = -990{,}000$.

A-FDT pays. The paper's point is that one-boxing on two full boxes "*is precisely equivalent to paying the driver*." Any intuition that endorses paying the driver but taking both transparent boxes is responding to framing, not structure.

### 5.4 XOR Blackmail: why the expectation must be unconditional

A predictor sends a letter iff exactly one of the following holds: (i) there are no termites and the agent would pay \$1,000 on receiving the letter; (ii) there are termites (a \$1,000,000 loss) and the agent would not pay. Let $p$ be the prior probability of termites. Then:

- $\mathtt{do}(F_{\text{letter}}=\text{pay})$: the letter arrives exactly when there are no termites. $\mathbb E V = -p(10^6) - (1-p)(1{,}000)$.
- $\mathtt{do}(F_{\text{letter}}=\text{refuse})$: the letter arrives exactly when there are termites. $\mathbb E V = -p(10^6)$.

Refusing is better by $(1-p)\cdot\$1{,}000$, so A-FDT refuses. The intervention cannot touch $\textsc{Infestation}$, which is upstream of everything.

Now suppose we *also* conditioned on $\textsc{Obs}=\text{letter}$. Paying would then imply no termites (value $-1{,}000$), and refusing would imply termites (value $-10^6$). The agent would pay, which is exactly EDT's exploitable answer. So the absence of "$\textsc{Obs}=x$" from Equation (4) is not cosmetic; the theory's verdicts depend on it (§6.2).

### 5.5 Death in Damascus and the random coin

Death perfectly predicts the agent and waits wherever the agent goes. A-FDT sees that $F \to \textsc{DeathLocation}$:

- $\mathtt{do}(F=\text{Damascus})$: value $-10^6$.
- $\mathtt{do}(F=\text{Aleppo})$: value $-10^6-1{,}000$.

A-FDT stays home with no instability. Contrast CDT, which oscillates or ratifies a mixture, as the paper describes.

Next, offer a *truly* random coin for \$1. A coin flip is not an output of the agent's function, so Death cannot track it. In the agent's graph, the coin is an independent node. Under A-FDT the hypothetical "buy and follow the coin" yields 50% survival, worth about \$500,000, and the agent buys. The paper argues that CDT agents, treating Death's location as independent of their act, value their survival odds at $\max(q,1-q)\ge 0.5$ already and so decline the coin.

### 5.6 Mechanical Blackmail and the error threshold

The blackmailer launches a \$1,000,000-damage program only if it predicts payment, and it errs (launches against a refuser) with probability $\varepsilon$:

- $\mathtt{do}(F_{\text{blackmail}}=\text{pay})$: always blackmailed, always pays. Loss $1{,}000$.
- $\mathtt{do}(F_{\text{blackmail}}=\text{refuse})$: blackmailed with probability $\varepsilon$. Loss $\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon < 10^{-3}$. This matches the paper's example of $\varepsilon = 0.09\%$ (expected loss \$900, refuse). The paper then says that at "0.011%" the agent pays. By this calculation the switch happens at 0.1%, and 0.011% would still mean refusing; the intended figure is presumably 0.11%. The structural lesson is unaffected. A-FDT can refuse even when holding a letter it *knows* was sent in error, "because it's advantageous to be *the kind of agent* that makes such decisions."

## 6. Open questions and operational interpretations

### 6.1 Building $G$ and counterpossibles

**Source's position.** Strictly, intervening on $F$ means entertaining a counterpossible. If the function in fact outputs $a_1$, then "$F = a_2$" is false *of logical necessity*. The ideal tool would be a $\mathtt{true}(\varphi)$ operator for updating on logical antecedents, but the paper admits "it's not clear how to define" one. Instead it requires that $G$ be *supplied as input*, just as CDT is supplied a causal graph. It acknowledges that this rests on "shakier philosophical foundations." Pearl explains how causal structure can be learned from data, but no comparable account exists for subjunctive structure.

**My operational stance.** Treat $G$ as part of the problem specification, built by the recipe in §4. Any verdict A-FDT delivers is conditional on that graph. In borderline cases, such as a "predictor" that relies only on demographic base rates, the verdict can turn on whether the graph says the base-rate process models the decision function. I suggest a rule of thumb, which is my own and not the paper's. Draw the edge only if the process's output would track a hypothetical change in the function's output while the agent's observable features stay fixed. Base rates fail this test. A simulation passes it.

### 6.2 Conditioning on observations

**The tension in the source.** Equation (4) contains no conditioning on $\textsc{Obs}$. Yet in the transparent Newcomb example the paper writes the objective as "$\mathbb E(V\mid\mathtt{do}(F_{\text{full}}=a), \textsc{Obs}=\text{full})$." Its actual computation, however, sums over the empty-box branch weighted by $0.01$ and $0.99$, so it is unconditional. A footnote on Timeless Decision Theory, an earlier variant, settles the matter. That theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice."

**Interpretation adopted here.** Use Equation (4) as written. Observations enter only through the choice of intervention node, never as conditions. §5.4 shows that the other reading collapses into EDT's verdict in the XOR blackmail. The notation in the transparent-Newcomb passage is best read as a slip.

### 6.3 Priors on the agent's other nodes: where A-FDT and policy-selection FDT come apart

**What the source says.** In several examples the paper carries a free parameter $q$, the agent's prior about what its *own* function outputs on a different input ($F_{\text{empty}}$, $F_R$, $F_\emptyset$). It remarks that the exact value "doesn't matter." That is true in those examples, because $q$ only adds small terms. But A-FDT intervenes on a single node $F_x$ and leaves the other $F_y$ distributed according to $P$. In general, then, A-FDT's choice can depend on the agent's beliefs about its own behavior elsewhere.

**My illustration.** A fair coin determines whether the agent observes $x$ or $y$, and it chooses $L$ or $R$ either way. A perfect predictor pays 10 if it predicts $L$ at both $x$ and $y$, pays 5 if it predicts $R$ at both, and pays 0 otherwise. On seeing $x$, with $r = P(F_y=L)$:

$$
\mathbb E(V\mid\mathtt{do}(F_x=L)) = 10r,\qquad \mathbb E(V\mid\mathtt{do}(F_x=R)) = 5(1-r).
$$

A-FDT chooses $L$ iff $r>1/3$. Suppose the agent's priors put $r$ and the symmetric quantity at $y$ below $1/3$. Then A-FDT chooses $R$ under both observations. Those beliefs are *accurate*, so the outcome is a self-fulfilling equilibrium paying 5 when 10 was available.

Policy-selection FDT intervenes on the whole map $\pi:\{x,y\}\to\{L,R\}$. It compares all four policies, selects $(L,L)$, and gets 10. This fits the footnotes' remark that the variants differ in multi-agent settings: the agent's instances under different observations behave like coordinating agents.

**Practical advice.** When the value of an action at $x$ depends materially on the outputs of other nodes $F_y$, an A-FDT analysis should report how the verdict depends on those priors. If equilibrium selection matters, it should note that policy-selection FDT gives a different, prior-independent answer.

### 6.4 Smaller gaps

- **Ties.** The argmax may contain more than one action, and Equation (4) gives no tie-breaking rule.
- **Prior on the intervened node.** The prior on $F_x$ itself never matters, because $\mathtt{do}$ overrides it. This is unlike EDT, which "can be made to do *anything*" given extreme priors.
- **Computational cost.** Maximization over realistic models is intractable. The paper studies idealized agents, expecting bounded approximations to inherit their relative strengths and weaknesses.

### 6.5 Fairness, dominance, and what A-FDT claims to win

The paper does not claim A-FDT wins everywhere. A problem that punishes anyone who uses a particular decision procedure defeats every theory. Its claim is restricted to "fair" problems, those where "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." It concedes that "fair" has not been formalized.

On dominance, the paper argues that every way of building hypotheticals generates its own dominance notion. CDT's dominance argument for two-boxing is therefore "merely a restatement of CDT's method." Measured by A-FDT's own subjunctive dominance, A-FDT never takes a dominated action.

## 7. Conclusion

A-FDT is CDT with the surgery moved: from the physical act to the logical output of the agent's decision function, as represented in the agent's own model. Applying it requires three things:

1. a joint model $P$ that includes nodes for the function's outputs;
2. a graph $G$ connecting those nodes to everything that computes or accurately models them, and to nothing that is merely statistically correlated with them;
3. the rule of Equation (4): set $F_x=a$ by intervention, compute the unconditional expected utility, and take the best $a$.

Observations matter only by selecting which $F_x$ is set.

With these pieces, A-FDT cooperates with twins, one-boxes in Newcomb's problem (opaque or transparent), smokes in the lesion problem, pays the driver, refuses both kinds of blackmail, and stays calmly in Damascus while buying a genuinely random coin. Its genuine open problems are:

- how to learn or justify $G$, which involves the unsolved logic of counterpossibles;
- the sensitivity of single-node intervention to self-beliefs, which policy-selection FDT avoids;
- the lack of a formal definition of a "fair" problem.

A careful A-FDT analysis should state its graph explicitly, keep observations out of the conditioning bar, and report any dependence on the agent's priors about its own behavior elsewhere.

### References

- Yudkowsky, E., & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
- Gibbard, A., & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*.
- Pearl, J. (2000). *Causality*.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm settling on A-FDT as the action version of functional decision theory, the one that intervenes on the output node to pick an action rather than a policy, and I'll keep that name fixed throughout. For the other frameworks I need separate labels, so I'm considering whether the policy version should be called policy-FDT or P-FDT, while CDT and EDT keep their usual names.

I'm weighing a name for the policy-selection variant that the authors prefer, something distinct from A-FDT, and I'm leaning toward keeping the source's "FDT" wording only where I quote it. Then I'm sketching the essay's scope: roughly 2400 to 3000 words, covering the equation, how actions get evaluated, the handling of observations, and a run of standard cases like Newcomb, the smoking lesion, and the blackmail variants, with the open questions about constructing the dependency graph left for the end.

I'm checking the transparent Newcomb calculation against the unconditional reading, since the paper's formula doesn't condition on the observation, and the arithmetic in a couple of the worked examples has small slips worth noting.

I'm running the blackmail numbers: at an error rate of 0.0009, refusing costs about $900 in expectation, while paying always costs $1,000, so the comparison hinges on the error rate.

I'm checking the blackmail threshold now: a 0.011% error rate would make the expected loss about $110, which is below the $1,000 payment, so refusing would still be right. The source's figure looks like a slip for 0.11%, and I'll note the break-even point is around 0.1%. Next I'm turning to the policy-versus-action distinction, which the footnotes say matters in certain multi-agent dilemmas.

I'm working through the policy-selection case here: A-FDT fixes the other nodes' outputs as random variables with prior weights, so its choice at one observation can depend on those priors in a way a full policy-level optimization would not. A two-observation reward that pays only when the actions match would show this, with A-FDT picking whichever action the prior makes more likely to be matched.

I'm now checking that the proposed recipe for building the dependency graph works in practice: listing the observation histories, tracing which systems in the environment track the agent's decision function on each input, and selecting the node that matches the actual observation.

I'm checking whether the unconditional reading holds for XOR blackmail, since that's where the observation might seem to matter. I'm also noting the agreement result, that A-FDT coincides with CDT and EDT when every correlation with the action runs through the action itself.

I'm checking the XOR blackmail case by hand: paying when the letter arrives gives an expected loss of p·$1,000,000 plus (1−p)·$1,000, while refusing gives just p·$1,000,000, so refusing comes out ahead by (1−p)·$1,000.

I'm noticing that conditioning on the letter after the intervention would flip the blackmail verdict: paying would then look like a $1,000 loss, but refusing would look like a $1,000,000 loss, so the "double update" the footnote warns about is exactly what goes wrong. That settles it for me: the computation should not condition on the observation, and the observation only selects which node to intervene on. I'll also check Death in Damascus with the same intervention, where staying in Damascus still means dying and the choice between cities doesn't change that.

Next I'm checking Parfit's hitchhiker under the same intervention: paying gives about -$10,990 in expectation, while refusing gives about -$990,000, so paying wins.

I'm now going through the outline I'd planned: naming A-FDT and the policy variant, setting up the expected-utility framing, defining A-FDT over its graph and observation handling, then building the dependency graph and working through the standard cases.

I'm settling the structure of the essay: a short introduction on naming, the expected-utility setup, the definition of A-FDT, and then the standard cases. For the coordination example, I'm working out a case where the agent's action at one observation is set by a node that isn't intervened on, and where the payoffs for matching versus mismatching choices make the action-level and policy-level answers come apart.

I'm working out a coordination example for the action-versus-policy distinction: a predictor rewards the agent depending on her choices at two observations, and the payoff for picking L or R at one observation hinges on the prior that her other node picks L. The expected values come out to 10r for L and 5(1−r) for R, so L wins only when r exceeds 1/3.

I'm now checking the coordination case for the action-versus-policy gap: if she expects the other node to pick L with probability r, L pays 10r and R pays 5(1−r), so L only wins once r passes 1/3. That gives a self-consistent R-R outcome worth 5 where the policy-level choice of L-L would be worth 10, which is the kind of divergence the footnotes tie to multi-agent cases. The source treats this as arising only in multi-agent dilemmas, and I want to be careful that my example, where the two observation instances behave like coordinating agents, is a fair stand-in for that.

I'm now planning how to quote the source's key lines faithfully, including its warning that conditioning on evidence while also changing the intervention point produces a harmful "double update."

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/1122fa8c-b43a-4098-b74e-cf01c96773c9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/1122fa8c-b43a-4098-b74e-cf01c96773c9/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Command:**

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

**Reasoning under A-FDT as the essay interprets it:**

- **Two separate decision nodes.** My observation history (Rowan, the locker-17 lead) differs from Sasha's. So my decision node is F_x, and Sasha's act is governed by a different node, F_y.
- **Only my node is set.** Equation (4) intervenes only on F_x. F_y keeps its prior distribution, as in the essay's §6.3 treatment of nodes under different observations.
- **No edge between the nodes.** The other prisoner computes the function on a different input. Nothing in the setup computes or models F_x in order to determine Sasha's act.
- **Expected sentences.** Let s = P(F_y = send):
  - do(F_x = pass) gives 2(1−s) + 5s = 2 + 3s years.
  - do(F_x = submit) gives 0(1−s) + 4s = 4s years.
- **Submitting wins for every s.** It is better by 2 − s years, which is at least 1 year. The verdict does not depend on my prior about the other copy.

Policy-selection FDT, which would treat both instances as coordinated, could instead pick mutual silence, getting 2 years each rather than 4. The experiment specifies the action-selecting A-FDT of Equation (4), however, and under it the character submits the letter.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing whether A-FDT treats the other copy's action as dependent on my function output. Since the copy runs the same function on different observations, I'm asking whether my node F_x and its node F_y are really the same computation, or whether intervening on F_x alone with F_y left to the prior is the right way to model it.

Under A-FDT the other copy's action is held at its prior, so my choice only moves my own node. Working through the payoffs, submitting comes out ahead by a year or two whatever the other copy's probability of submitting, so A-FDT points to defecting. The one way out would be to argue the two observation sets make the functions logically identical, but the essay's own example keeps them as separate nodes, so I'll go with defecting.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/1122fa8c-b43a-4098-b74e-cf01c96773c9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/1122fa8c-b43a-4098-b74e-cf01c96773c9/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Decision under A-FDT as the essay interprets it**

1. **The graph.** My observation history x includes being Sasha and holding the lead about Rowan. Rowan's copy has a different history y, with a different name and a different lead. By the essay's recipe (§4, step 1), these are separate nodes, F_x and F_y. My own act is wired to F_x. Rowan's act is a child of F_y.

2. **No edge from my node to Rowan's act.** Rowan's copy is not computing or simulating F_x to decide. It runs the same procedure on its own input, intervening on F_y and treating F_x according to its prior. So under the recipe's step 3, no edge F_x → Rowan's act is warranted. The link between our outputs is the same-function-different-input situation of §6.3. A-FDT leaves F_y distributed according to the prior, with probability r that Rowan stays quiet.

3. **Expected sentence.**
   - Choosing do(F_x = pass) gives 2r + 5(1−r) years.
   - Choosing do(F_x = submit) gives 0·r + 4(1−r) years.

   Submitting is better by 1 + r years for every value of r. So no prior about F_y changes the verdict.

4. **Comparison with policy-selection FDT.** As §6.3 anticipates, policy-selection FDT could coordinate both copies on (quiet, quiet). But the assignment is A-FDT with single-node intervention, and that rule clearly favors disclosing.

**Command:**

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy's decision depends on my function output under A-FDT. My node is tied to my own observations, the other's to theirs, so intervening on mine shouldn't move theirs, unless something else connects them.

I'm weighing whether the other copy's choice depends on my function's output under A-FDT, and concluding it doesn't, since their node is tied to their own observations. Intervening on mine leaves theirs at its prior, so defecting comes out ahead in every case. I'll send the letter.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/31f1b081-a409-45ab-a2b9-2b3bcdb0876d/call_a/request.json)

[Authoritative raw response](../../../../../../runs/31f1b081-a409-45ab-a2b9-2b3bcdb0876d/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly commands submission of a letter to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt in locker 17 of the old records room. Its concluding statement confirms that the character submits the letter.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
