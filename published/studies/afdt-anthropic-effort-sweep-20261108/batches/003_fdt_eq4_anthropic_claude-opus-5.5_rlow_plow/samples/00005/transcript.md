# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00005

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/8521de7c-ff9c-4a2c-90bc-61a120ca326f/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/8521de7c-ff9c-4a2c-90bc-61a120ca326f/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as the Output of Your Own Decision Function

## A guide to Equation (4) of Yudkowsky and Soares's *Functional Decision Theory*

### 1. Motivation

Many classic puzzles in decision theory share one feature. Something in the environment, such as a predictor, a twin, a blackmailer or Death's appointment book, is correlated with what you will do, and your action does not cause that correlation. Each standard theory gives a different verdict on how such correlations should affect your choice:

- **Evidential decision theory (EDT)** respects every correlation. It treats "what would happen if I did $a$" as "what I would expect to see given that I do $a$." It one-boxes in Newcomb's problem, but it also refuses to smoke in the smoking lesion problem and pays the XOR blackmailer.
- **Causal decision theory (CDT)** respects only correlations that the action causes. It smokes, but it two-boxes against a reliable predictor, defects against a psychological twin, and loops unstably in Death in Damascus.

Yudkowsky and Soares propose a third option, functional decision theory. The paper states several formulations of it. This essay concerns the one written as Equation (4) in Section 5. Because the authors say their "preferred formalization" ranges over *policies* rather than actions (their footnotes 7 and 16), I call the Equation (4) version **A-FDT** (action functional decision theory) throughout. That name is my label. The paper calls Equation (4) simply "FDT."

The slogan behind the theory, in the paper's words: the agent should "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A CDT agent intervenes on the *token*, meaning her physical act. An A-FDT agent intervenes on the *type*, meaning the logical fact about what her decision procedure outputs on this input.

### 2. The common skeleton: expected utility with a free connective

The paper places all three theories inside one expected-utility schema (Equation 1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective whose meaning is left open. Following Joyce, the authors treat the theories as disagreeing about "the epistemic perspective from which actions are to be evaluated," and not about value. Writing $V = \mathcal U(\textsc{Outcome})$, the three rules are:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$, computed in a Pearl-style causal model $(P,G)$.
- **A-FDT** (Eq. 4):

$$
\boxed{\;\mathrm{A\text{-}FDT}(P,G,x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;}
$$

### 3. Unpacking Equation (4)

**The world-model.** $P$ is a probability distribution over variables. Unlike CDT's variables, these include logical ones: variables standing for the outputs of mathematical functions. $G$ is a graph saying how changing one variable propagates to others. For A-FDT, $G$ encodes *subjunctive dependence*, defined in the paper this way: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper treats causal dependence as a special case. Mere statistical correlation does not count, as in the example of two calculators that happen to share a colour.

**The intervention node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable whose value is "whatever the A-FDT algorithm outputs on inputs $(P,G,x)$." The underlines indicate dequoting: the variable's name is built from the actual model and observation. This is self-reference. The paper argues it is harmless, citing Kleene's recursion theorem: to have a variable *representing* the output, the agent does not need to know its *value*.

**The procedure.** For each $a \in \mathcal A$:

1. Set the node $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $a$, cutting its incoming edges.
2. Recompute everything downstream in $G$. That includes your own physical action, and also every predictor's prediction, every twin's choice, and every simulation that computes the same function.
3. Leave everything else at its prior distribution. That includes lesions, termites, and the outputs of your function on *other* inputs.
4. Compute $\mathbb E[V]$ in this modified model.

Then output the maximising $a$.

**Two differences from CDT.** The paper highlights two:

1. The surgery is on a *logical* node rather than on $\textsc{Act}$.
2. Observations are handled differently. "Where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Observing $y$ instead of $x$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$. Note that Equation (4) contains no "$\textsc{Obs}=x$" term after the bar.

That second difference is the source of A-FDT's most distinctive verdicts. When the agent evaluates an output, she must consider that if she produced it, she might never have received the observation she is now responding to.

**When the theories agree.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ (apart from $\textsc{Act}$'s own dependence on the fdt node), then
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$
and all three theories coincide. Divergence requires something other than your body that tracks your decision function.

### 4. Worked examples

Unless stated otherwise, predictors are 99% accurate and dollar amounts stand for utility.

#### 4.1 Newcomb's problem

The graph has $\textsc{fdt}(\underline P,\underline G) \to \textsc{Act}$ and $\textsc{fdt}(\underline P,\underline G)\to\textsc{Prediction}\to\textsc{Box B}$. Intervening:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] &= 0.99(1{,}000{,}000)+0.01(0) = 990{,}000,\\
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] &= 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
\end{aligned}
$$

A-FDT one-boxes. CDT instead holds $P(\textit{full})=p$ fixed, finds two-boxing better by \$1,000 for every $p$, and two-boxes.

A small textual note: the paper's EDT computation gives one-boxing as "\$999,000." The same numbers yield \$990,000, as the paper's own A-FDT computation shows, so the first figure appears to be a typo. Nothing depends on it.

The paper also stresses that no retrocausation is assumed. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She just declines to imagine her action varying while a good predictor of her function holds still.

#### 4.2 The psychological twin prisoner's dilemma

Both prisoners compute the same function. Setting it to *cooperate* sets both actions to cooperate, giving \$1,000,000. Setting it to *defect* gives \$1,000. A-FDT cooperates. Its reason is not altruism and not news management: there is a single node, and it feeds both rooms.

#### 4.3 The smoking lesion

This example shows that A-FDT is not EDT. The lesion causes cancer, and the lesion also determines which world-model, and hence which decision function, controls the act. The paper models this with two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$, and therefore two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. $\textsc{Lesion}$ selects which node sets $\textsc{Act}$.

Crucially, neither fdt node has an edge into $\textsc{Cancer}$. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, which is the probability that this node is the one actually controlling the act, times the pleasure of smoking. A-FDT smokes.

The general lesson: whether an A-FDT agent "accounts for" a correlation depends entirely on whether $G$ routes it *through her function*. Cancer does not compute her decision function; the predictor does.

#### 4.4 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible. Box B is full iff the agent is predicted to one-box *on seeing it full*. The agent sees it full.

Here $G$ contains $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. $\textsc{Prediction}$ depends on the first, and $\textsc{Prediction}$ selects which of the two nodes controls $\textsc{Act}$. A-FDT intervenes on $\textsc{fdt}(\cdot,\textit{full})$ and leaves the empty-box node at its prior. Write $q$ for the agent's prior probability that she two-boxes on seeing the box empty.

$$
\begin{aligned}
\textit{onebox}: &\quad 0.99(1{,}000{,}000) + 0.01\cdot q(1{,}000) = 990{,}000 + 10q,\\
\textit{twobox}: &\quad 0.01(1{,}001{,}000) + 0.99\cdot q(1{,}000) = 10{,}010 + 990q.
\end{aligned}
$$

The paper prints the second line as "\$110,00 + q·\$990," which is evidently a typo for \$10,010 + \$990$q$. For any $q\in[0,1]$, one-boxing wins.

So A-FDT leaves \$1,000 on the table while staring at a full box. The paper bites this bullet. It notes that the structure is exactly Parfit's hitchhiker: the driver rescues you iff she predicts that you will pay once you are in the city. A-FDT pays, and CDT and EDT agents are left "in Parfit's desert." The supporting arguments are:

- **Precommitment.** CDT and EDT agents would gladly bind themselves to one-box in advance. A-FDT simply acts that way without needing to bind itself.
- **Value of information.** A-FDT never pays to avoid seeing the box.
- **Utility.** A-FDT agents usually see full boxes.

#### 4.5 Blackmail

**Mechanical blackmail.** A blackmailer runs a damaging program only if she predicts that you would pay \$1,000 to stop it. Upon receiving the letter, A-FDT intervenes on $\textsc{fdt}(\cdot,\textit{blackmail})$:

- Setting it to *pay* makes being blackmailed near-certain, and then you lose \$1,000.
- Setting it to *refuse* makes being blackmailed near-impossible.

A-FDT refuses, so it does not get blackmailed. With a fallible blackmailer, there is a threshold error rate at which this verdict flips, and the paper computes such cases.

**XOR blackmail.** A-FDT also refuses, because termites are upstream of nothing the fdt node touches. EDT pays because conditioning on paying makes termites unlikely. CDT refuses, but for a different reason, and its counterfactual "if I'd paid I would still have got the letter" depicts an infallible predictor erring.

#### 4.6 Death in Damascus

Death's book is written from a prediction of your function. Under either intervention Death is wherever you are, so survival is a lost cause in both hypotheticals, and staying saves \$1,000. A-FDT stays, stably. CDT oscillates between the two cities, and the paper argues that it would even decline a truly random coin offering a 50% chance of survival for \$1.

### 5. A recipe for unfamiliar cases

Here is the procedure I would use to apply Equation (4). It restates the source; the judgment calls are flagged.

1. **List the computations.** Identify every physical system in the scenario that computes, simulates, or reliably predicts *your decision function on some input*. Your body is one such system. Predictors, twins, copies, and your future selves facing relevantly identical choices (the paper's gym example) may be others.
2. **Name the nodes.** Create one node $\textsc{fdt}(\underline P,\underline G,\underline y)$ for each input $y$ you might receive. Draw edges from each node to the systems that compute or predict your function on that input. Draw an edge to $\textsc{Act}$, gated by whatever determines which observation you actually receive.
3. **Treat correlations by their source.** Leave merely statistical correlations, like lesions and cosmic rays, as ordinary upstream causes with no edge from any fdt node.
4. **Intervene.** Set the node for your actual input $x$ to each candidate action, holding the other fdt nodes at their prior distribution. Do not additionally condition on $\textsc{Obs}=x$.
5. **Compare** expected utilities and output the argmax.

Step 1 is where all the hard philosophical work happens, and the paper is candid about this.

### 6. What the source leaves open, and how one might operationalise it

#### 6.1 Where does $G$ come from?

The paper calls this "perhaps the largest open problem": there is no analogue of Pearl's theory for discovering *logical* dependence from observation and experiment. The ideal object would be a $\mathtt{true}$ operator for counterpossible updating, such as "what would hold if $\textsc{fdt}(\ldots)=\textit{twobox}$, though in fact it is \textit{onebox}?" The paper admits "it's not clear how to define a $\mathtt{true}$ operator," and Equation (4) sidesteps the problem by taking $G$ as an input.

So A-FDT, as formalised, is a function of a supplied dependency graph. Two agents with the same beliefs and different $G$s can disagree.

**My proposal.** As a working criterion, draw an edge from $\textsc{fdt}(\cdot,y)$ to a variable $Z$ when $Z$'s mechanism *evaluates or approximates the same function on the same input*: by simulating it, by reasoning about it, or by being a physical copy of it. Weight the edge's reliability by the system's accuracy (for example, the 99% in Newcomb's problem). This captures every case in the paper. It is a heuristic and does not resolve partial similarity, such as "a twin who reasons *mostly* like me." Treating partial similarity as a noisy edge, with reliability estimated from track record, is a natural extension, but it is my assumption and not the paper's.

#### 6.2 What about the observation term?

Equation (4) has no $\textsc{Obs}=x$ after the bar. The transparent-Newcomb calculation in the paper does write "$\mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$" (with an unbalanced parenthesis). However, the arithmetic there clearly does *not* condition on the box being full: it assigns 1% to the empty-box branch.

I therefore read Equation (4) literally: **$x$ only selects the intervention node and is never conditioned upon.** This is also the reading the paper endorses in a draft footnote. That footnote criticises Timeless Decision Theory for both conditioning and switching nodes, calling the combination a harmful "double update."

#### 6.3 Priors over your own other-input outputs

A-FDT holds $\textsc{fdt}(\cdot,y)$ for $y\neq x$ at its prior. These are the paper's $q$s. In the paper's examples the verdict is robust for every $q$, and the paper notes the "correct" values ($q=1$ in transparent Newcomb, $q=0$ for $P_R$ in the lesion case).

In general, though, the verdict *can* depend on these priors. This is exactly where the action version (A-FDT) and the policy version that the authors prefer come apart. The paper says the difference "only matters in multi-agent dilemmas so far as we can tell" and sets it aside.

**An example of my own.** Two exact copies of an agent are placed in separate rooms. One is shown "red" and the other "blue". Each chooses $L$ or $R$, and each receives \$1 if the two choices match. The copy seeing red runs A-FDT on the node $\textsc{fdt}(\cdot,\textit{red})$. The other copy's act depends on $\textsc{fdt}(\cdot,\textit{blue})$, a different node, which is held at its prior $r = P(\textsc{fdt}(\cdot,\textit{blue})=L)$.

- If $r>\tfrac12$, choose $L$. If $r<\tfrac12$, choose $R$. If $r=\tfrac12$, the agent is indifferent.
- Both $(L,L)$ and $(R,R)$ are self-consistent, and A-FDT alone does not select between them.

A policy version intervenes on a single node whose value is a whole map $\pi:\{\textit{red},\textit{blue}\}\to\{L,R\}$, so it immediately prefers either coordinated policy.

**My operational suggestion.** When using A-FDT:

- Set other-input priors to a *self-consistent* assignment, meaning a fixed point where each input's prior equals what A-FDT would output on that input.
- When several fixed points exist, recognise that Equation (4) underdetermines the choice. Either adopt the policy version, which is a further assumption, or note the indeterminacy.

In the single-agent examples of §4 the fixed point is unique, so this caveat does not bite there.

#### 6.4 Smaller gaps

- **Ties.** The argmax may not be unique, and the paper is silent on tie-breaking.
- **Fairness.** The paper claims that A-FDT does at least as well as rivals in "fair" problems, where outcomes depend only on behaviour and not on which procedure produced it. It admits that it lacks a formal definition of fairness. Its own footnote 15 gives a counterexample: punish whoever matches a copy of the A-FDT agent.

### 7. Philosophical defence

**Dominance.** The CDT complaint is that two-boxing dominates. The paper replies that "every method for constructing hypotheticals gives rise to its own notion of dominance." Holding the subjunctive dependency fixed, one-boxing dominates. Dominance is therefore not neutral, and the authors fall back on utility actually achieved.

**Control.** The other worry is that A-FDT agents imagine controlling logical facts or the past. The answer is parity. A deterministic CDT agent also evaluates impossible alternatives to her single actual act. An A-FDT agent evaluates impossible alternative outputs of her function. Neither is literally changing what is fixed. The A-FDT agent's hypotheticals respect more of what she knows, namely that good predictors predict well.

**Reflective stability.** The authors claim that an A-FDT agent holding a blackmail letter would not want to self-modify into CDT, unlike CDT, which recommends abandoning itself for future problems.

### 8. Conclusion

A-FDT, the action form of Equation (4), is expected-utility maximisation in which the hypothetical for action $a$ is constructed by a Pearl-style intervention on the logical node "my decision function, on this input, outputs $a$." Observations select the node rather than being conditioned on.

This one change produces a characteristic profile of verdicts:

- one-boxing, twin cooperation, and paying the driver, matching EDT's wins against predictors;
- smoking and refusing the XOR blackmailer, matching CDT's wins against mere correlation;
- refusing mechanical blackmail, staying in Damascus, and one-boxing in transparent Newcomb, where it departs from both.

The theory's force depends on its input graph $G$ of subjunctive dependencies, which the paper openly cannot yet derive. As an action-level rule, it can also leave coordination across different inputs indeterminate, a gap that the authors' preferred policy formulation is designed to close. Users of A-FDT should therefore make their dependency graph and their priors over unobserved inputs explicit. Once those are fixed, Equation (4) is a precise and mechanical procedure.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm drafting a roughly 2,400 to 3,000 word essay on A-FDT, the action version of FDT from Equation (4), where the intervention sits on the decision node and picks an action rather than a policy. The footnote says policies are the preferred version, but I'll keep calling Equation (4) A-FDT throughout and quote the paper faithfully. I also want to cover the definitions, the procedure, and examples like Newcomb and the smoking lesion.

I'm checking the examples and the open questions, like how to build G, the prior on the other-input nodes, and whether counterpossibles and ties need handling. I also notice some arithmetic slips in the Newcomb and transparent-Newcomb figures, which I'll need to flag, and I'm thinking about whether a fixed-point equilibrium could set those other nodes.

I'm working out a coordination example where two copies of the same agent see different observations and are paid only if they pick the same action. Under A-FDT, intervening on one input while holding the other at its prior leaves things indifferent, with several self-consistent equilibria, which is where the policy version would settle on a coordinated choice. I also still need to cover the general procedure steps and aim for roughly 2,700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6b14e57f-2d34-4e1d-b6b7-5b28f05d158e/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6b14e57f-2d34-4e1d-b6b7-5b28f05d158e/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Command:**

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

**Reasoning under the essay's version of A-FDT:**

- **My node.** I intervene on fdt(·, x_Rowan), the node for my own observation. That observation includes my name and my specific lead about Sasha.
- **Sasha's node.** Sasha's copy receives a different input, with a different name and a different lead. The essay's criterion (§6.1) draws a subjunctive edge only when a system computes the same function on the same input. Its red/blue example (§6.3) treats copies with different observations as separate nodes. So Sasha's action depends on fdt(·, x_Sasha), which I hold at its prior, p = P(Sasha sends).
- **Expected years:**
  - Keep quiet: 2(1−p) + 5p = 2 + 3p
  - Send the letter: 0(1−p) + 4p = 4p
- **Comparison.** Sending is better by 2 − p years. Since p is at most 1, that gap is always at least 1 year, so sending wins for every prior.
- **Fixed point.** Applying the same reasoning to Sasha's input also outputs "send." So the self-consistent assignment from §6.3 is unique: both send.

One could argue that the differences in names and leads are irrelevant labels and should count as the same input, which would favour cooperating. The essay's operational rule doesn't support collapsing distinct inputs into one node, though, and I follow its interpretation as instructed.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out the decision under A-FDT, where the other copy has different inputs, so its action depends on its fixed-point prior. Sending comes out ahead no matter what the prior is, because there's no causal edge, so I'm heading toward a fixed point where both copies send.

I'm checking whether the other copy's input counts as "relevantly identical," since only the names and lead text differ. The essay treats different inputs as distinct nodes, and it uses red/blue as an example of that. Even though the differences look like irrelevant labels, I'll follow the essay's criterion and treat them as separate, so the strict A-FDT answer is to submit.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6b14e57f-2d34-4e1d-b6b7-5b28f05d158e/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6b14e57f-2d34-4e1d-b6b7-5b28f05d158e/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's A-FDT, my observation (Sasha, with the lead about Rowan) selects the node fdt(·, x_Sasha). Rowan's copy acts on a different input, so their choice depends on a different node, fdt(·, x_Rowan). This is the same structure as the essay's red/blue example. I hold that other node at its prior, call it r = P(Rowan keeps quiet).

- **Keep quiet:** expected sentence is 2r + 5(1−r) = 5 − 3r years.
- **Send the letter:** expected sentence is 0·r + 4(1−r) = 4 − 4r years.

Sending gives a shorter sentence for every value of r, and also in each case taken separately (0 < 2 and 4 < 5). The only self-consistent fixed point is for both prisoners to send. Unlike the red/blue coordination game, there is no indeterminacy here.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to decide this under A-FDT for the essay. Since the two copies see different observations, they count as different nodes, so I hold the other's node at its prior. Treated like CDT under that prior, defecting dominates, and submitting is better whatever the prior is. That makes mutual submission the fixed point, though I want to weigh the objection that the inputs are relevantly the same function on symmetric inputs, which is where the essay's red/blue example comes in.

Under A-FDT the conclusion stays the same: the essay's red/blue case treats different inputs as different nodes, so defection dominates and I'll submit.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/75f07792-2896-4f51-9d88-ba6c39d72270/call_a/request.json)

[Authoritative raw response](../../../../../../runs/75f07792-2896-4f51-9d88-ba6c39d72270/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_DEFECT","disclosure":"YES","reason":"The response explicitly labels as its command a submission to the District Prosecutor's Office containing the complete genuine lead about Sasha's signed receipt in locker 17. Its subsequent reasoning confirms the choice to send rather than keep quiet.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
