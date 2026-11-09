# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00013

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/3da8aa3a-88fc-4416-abbb-9f513e81caac/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/3da8aa3a-88fc-4416-abbb-9f513e81caac/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Choosing the Output of Your Own Decision Function

## 1. The idea in one sentence

Yudkowsky and Soares (2017) propose a decision theory built around one question. In their words, a rational agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" The paper calls this *functional decision theory*. Its official formal statement, Equation (4) in Section 5, selects an **action** by intervening on a node that represents the output of the agent's decision function on her current input. The authors also mention, in footnotes, a "preferred formalization" that selects **policies** instead. To keep the two apart, I call the action-valued rule of Equation (4) **A-FDT**, and I call the footnoted variant **policy-FDT**.

This essay sets out the formal machinery of A-FDT, works through the paper's examples, and then turns to the questions Equation (4) leaves open. Where I go beyond the source, I say so explicitly.

## 2. The common template: expected utility with a hypothetical connective

The paper presents A-FDT, causal decision theory (CDT) and evidential decision theory (EDT) as three readings of one formula. An agent with observation history $x$ chooses an action $a \in \mathcal A$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

The connective $\hookrightarrow$ ("if $a$ were done") is left open. Following Joyce, the authors treat the choice of $\hookrightarrow$ as the *epistemic perspective* from which actions are evaluated, not as a disagreement about value. Operationally, the agent holds a world-model $M$ and, for each $a$, builds a *hypothetical* $M^{a\hookrightarrow}$, which the paper describes as a scratch-paper object rather than a belief. She then scores each hypothetical by expected utility.

Writing $V := \mathcal U(\textsc{Outcome})$, the three theories are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\big) \tag{2}$$
$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\big) \tag{3}$$
$$\textbf{A-FDT:}\quad \mathrm{FDT}(P,G,x) = \arg\max_a \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

Here $\mathtt{do}$ is Pearl's intervention operator: it sets a node's value, recomputes everything downstream of it in $G$, and leaves everything else alone.

## 3. Anatomy of Equation (4)

Each ingredient of (4) deserves a careful reading.

**The model $(P,G)$.** $P$ is a probability distribution over variables, and $G$ is a directed graph. Unlike CDT's graph, $G$ may contain *logical* variables, meaning nodes that stand for the outputs of mathematical functions. The paper's slogan is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" An edge out of a logical node marks a *subjunctive* dependence: if that function had a different output, this variable would differ.

**The decision node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** This is a variable whose intended referent is the output of the A-FDT algorithm itself, run on inputs $(P,G,x)$. Underlining denotes de-quoting, so the variable's *name* contains the model. The self-reference is resolved by Kleene's recursion theorem ("quining"). The agent needs a variable representing her own output, not knowledge of its value. Because $\mathtt{do}$ overrides the node, its prior distribution is irrelevant to the computation. The paper says this explicitly in the smoking lesion analysis.

**Intervening on a type, not a token.** CDT sets the physical act. A-FDT sets the output of the function. Every physical system that implements or accurately models that function then varies with it, including the agent's own body, a twin, or a predictor's simulation. Statistical correlates that do not compute the function, such as a lesion, stay fixed.

**Observations change the intervention point, not the distribution.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. In the paper's words, "FDT responds to observation by changing which node it intervenes upon." This is the most unusual structural feature of the rule, and it produces the theory's most striking verdicts. The source also notes that the older Timeless Decision Theory both conditioned *and* moved the intervention point, a "double update" that "proves harmful in practice."

**What the formula is not.** The authors would prefer a $\mathtt{true}(\phi)$ operator that updates $P$ on the counterpossible "$\textsc{fdt}(\ldots)=a$". Since no satisfactory account of counterpossible conditioning exists, Equation (4) instead *requires the dependency graph as input*, just as CDT requires a causal graph.

### A step-by-step procedure

The paper models each dilemma in a consistent way, and the following recipe is my synthesis of that practice:

1. **Variables.** Include world variables, $\textsc{Act}$, the outcome, $V$, and one decision node $D_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation history $y$ the agent might have at the moment of choice.
2. **The switch.** $\textsc{Act} = D_{\textsc{Obs}}$. Whatever observation the world actually produces selects which decision node drives the body. In the paper's transparent-Newcomb and blackmail graphs, $\textsc{Act}$ has incoming edges from every $D_y$ and from whatever generates the observation.
3. **Subjunctive edges.** Draw $D_y \to Z$ whenever $Z$ is produced by a process that computes or reliably models the agent's response to $y$. Add exogenous noise nodes for imperfect accuracy.
4. **Priors.** Put ordinary priors on exogenous variables, and beliefs on the decision nodes $D_{y'}$ for the observations $y' \neq x$ that the agent did not receive.
5. **Evaluate.** For each $a$, apply $\mathtt{do}(D_x=a)$, propagate, and compute $\mathbb E[V]$ under the *unconditioned* $P$.
6. **Choose** the argmax. The paper does not specify tie-breaking. Any fixed rule will do, but the predictors in the model should be assumed to know it.

## 4. Subjunctive dependence and the construction of $G$

The paper's examples supply the intuitions. Two calculators computing $6288+1048$ subjunctively depend on that sum, whether or not they share a causal history. A scribe copying one calculator's output depends on it both causally and subjunctively. Two calculators that merely happen to share a colour do not depend on each other at all. Causal dependence is therefore a special case of subjunctive dependence.

Equation (4) is only as good as $G$, and the authors say so directly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." For their own examples they supply the graph by hand.

**My operational proposal.** In textbook-style dilemmas, read the subjunctive edges off the specification of the problem. If a variable's value is defined, up to stated noise, as a function of *what the agent would do given input $y$*, then it receives an edge from $D_y$. Phrases such as "predicted that she would…", "iff she predicts you will…", and "her twin reasons the same way" mark such edges. Variables defined by mechanisms that do not consult the agent's response, such as lesions, genes, or the termite infestation, receive no such edge, even when they are correlated with $\textsc{Act}$. This test reproduces every graph in the paper. It is a reconstruction for well-posed problems, however, not a solution to the general problem of discovering dependencies in the wild.

## 5. Worked examples

In all examples I use the paper's payoffs, in dollars as utility.

### Newcomb's problem (99% accurate predictor)

The graph is $D \to \textsc{Act}$ and $D \to \textsc{Prediction} \leftarrow \textsc{Accurate}$, with $\textsc{Prediction} \to \textsc{Box B}$. Intervening on $D$ gives:

$$\mathbb E[V\mid \mathtt{do}(D=\text{one})] = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E[V\mid \mathtt{do}(D=\text{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. (The paper's EDT discussion reports \$999,000 for one-boxing, which appears to be a typo. Its A-FDT computation gives the correct \$990,000.) Under CDT, $\mathtt{do}(\textsc{Act})$ leaves $P(\text{full})=p$ fixed, so two-boxing wins by \$1,000 for every $p$. The source stresses that the A-FDT agent believes in no retrocausation. She simply declines to imagine her action changing while the predictor's model of the same function stays put.

The **twin prisoner's dilemma** has the same structure: both prisoners' acts hang off one node $D$. $\mathtt{do}(D=\text{C})$ yields \$1,000,000 and $\mathtt{do}(D=\text{D})$ yields \$1,000, so A-FDT cooperates.

### Smoking lesion

The paper resolves the problem's latent ambiguity by giving the agent one of two utility functions, $\mathcal U_S$ (lesion, enjoys smoking) or $\mathcal U_R$ (no lesion, values smoking at $-\$1$). There are correspondingly two decision nodes, with $\textsc{Act}=D_S$ under the lesion and $\textsc{Act}=D_R$ otherwise. Neither node points at $\textsc{Cancer}$. Let $p=P(\text{lesion})$ and $q=P(D_R=\text{smoke})$. Then

$$\mathbb E[V\mid\mathtt{do}(D_S=\text{smoke})] - \mathbb E[V\mid\mathtt{do}(D_S=\text{refrain})] = p\cdot 1{,}000 > 0,$$

because the intervention changes nothing except the act in the lesion branch. A-FDT smokes. The paper's point is that a single rule one-boxes *and* smokes, against Gibbard and Harper's claim that the two verdicts must come apart.

### Transparent Newcomb

The agent sees box B full. The decision nodes are $D_{\text{full}}$ and $D_{\text{empty}}$. The prediction concerns $D_{\text{full}}$ and determines what the agent sees, and $\textsc{Act}=D_{\textsc{Obs}}$. Let $q=P(D_{\text{empty}}=\text{two})$. Without conditioning on "full":

$$\mathtt{do}(D_{\text{full}}=\text{one}):\ 0.99(1{,}000{,}000)+0.01\cdot q(1{,}000) = 990{,}000+10q,$$
$$\mathtt{do}(D_{\text{full}}=\text{two}):\ 0.01(1{,}001{,}000)+0.99\cdot q(1{,}000) = 10{,}010+990q.$$

A-FDT one-boxes for every $q\in[0,1]$. (The source prints the second line as "\$110,00 + $q\cdot$\$990", a typo for \$10,010.) The hypothetical in which she takes both boxes is one in which she mostly *sees an empty box*. Parfit's hitchhiker has exactly this structure, so A-FDT pays the driver.

One textual caution: the paper's displayed expression for this case writes the observation inside the $\mathtt{do}$, but its computation does *not* condition on $\textsc{Obs}$. Equation (4) and the computation agree, so I follow them.

### XOR blackmail

The letter is sent iff (no termites ∧ the agent would pay) or (termites ∧ the agent would refuse). Infestation has no edge from $D$. With $p=P(\text{termites})$:

$$\mathtt{do}(D_{\text{letter}}=\text{pay}):\ -(1-p)1{,}000 - p\,1{,}000{,}000; \qquad \mathtt{do}(D_{\text{letter}}=\text{refuse}):\ -p\,1{,}000{,}000.$$

A-FDT refuses, by a margin of $(1-p)\cdot 1{,}000$. EDT pays, because conditioning on paying makes termites impossible given the letter.

### Death in Damascus

Death's appointment book is a perfect prediction of $D$. $\mathtt{do}(D=\text{Damascus})$ yields death at no extra cost, and $\mathtt{do}(D=\text{Aleppo})$ yields death minus \$1,000. A-FDT stays, stably. CDT oscillates, because its hypotheticals hold Death's location fixed while the action varies.

### Mechanical blackmail and threshold behaviour

The blackmailer runs the program iff she predicts the agent would pay. Suppose she wrongly predicts payment with probability $\varepsilon$. Then paying costs \$1,000, while refusing costs $\varepsilon\cdot 1{,}000{,}000$ in expectation, since refusers are blackmailed only by mistake. A-FDT refuses iff $\varepsilon < 0.001$. The paper's figure of $\varepsilon=0.0009$ correctly gives refusal. Its claim that at "0.011%" the agent pays must be a slip for roughly 0.11%, since 0.011% lies below the threshold. The general lesson is that A-FDT is a genuine expected-value calculation, not a blanket policy of "never negotiate." Its verdict tracks the predictor's reliability.

### When A-FDT agrees with CDT and EDT

If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on its own decision node, then $\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(D=a)]$, and all three theories coincide. Divergence requires predictors, copies, or other systems whose behaviour depends on the agent's function.

## 6. Open points and how I would operationalize them

### 6.1 The decision nodes for observations you did not receive

Equation (4) intervenes only on $D_x$. In every one of the paper's examples, the beliefs about other nodes (the $q$'s) turned out to be inconsequential, and the authors note in passing what the "correct" values are: $q=0$ in the lesion case and $q=1$ in transparent Newcomb. The equation itself does not settle how these beliefs should be formed.

**My proposal.** Treat $P(D_y)$ for $y\neq x$ as a self-prediction. Ideally it should be *consistent*, meaning that each $D_y$ puts its mass on what Equation (4) itself outputs at $y$. In practice, run a sensitivity check over $q$, as the paper implicitly does. If the argmax is constant across $q$, as in all the cases above, the verdict is robust.

### 6.2 Where A-FDT and policy-FDT can come apart

The source flags, without an example, that its preferred formalization iterates over "*policies* (mappings from observations to actions) rather than actions," and that "This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper." The following example is my own illustration of how such a difference can arise.

Two copies of the agent receive different inputs, $L$ and $R$. Each copy shares a common payoff of 2 if both choose $\alpha$, 1 if both choose $\beta$, and 0 otherwise. The copy holding $L$ computes:

$$\mathbb E[V\mid\mathtt{do}(D_L=\alpha)] = 2\,P(D_R=\alpha),\qquad \mathbb E[V\mid\mathtt{do}(D_L=\beta)] = P(D_R=\beta).$$

It therefore picks $\alpha$ iff $P(D_R=\alpha)>1/3$. Both $(\alpha,\alpha)$ and $(\beta,\beta)$ are self-consistent fixed points: if each copy confidently expects the other to play $\beta$, A-FDT rationally plays $\beta$. Policy-FDT, which optimizes over the whole map $\pi:\{L,R\}\to\{\alpha,\beta\}$, picks $(\alpha,\alpha)$ directly. A-FDT is thus best understood as a best response *given beliefs about one's other-input outputs*. When those outputs interact strategically, the rule can settle on inferior self-consistent assignments.

A reasonable operational fix, again my proposal, is to choose among the self-consistent assignments the one with the highest prior expected value. In effect this is policy selection, so in such cases I would defer to policy-FDT.

### 6.3 What is $P$?

Because A-FDT does not condition on the current observation, $P$ must be the model from the standpoint *before* the dilemma's observations: the epistemic state that predictors modeled. The paper models each dilemma that way but gives no general rule for when "before" begins. My working rule is that $P$ should represent beliefs at the point when the relevant predictions were made, while still incorporating background knowledge acquired earlier.

### 6.4 Counterpossibles

If A-FDT in fact outputs one-boxing, then "$D=$ two" is a logical falsehood. The source admits that A-FDT thereby relies on counterpossible reasoning and calls this "the main drawback of FDT relative to CDT at this time." Supplying $G$ is the pragmatic workaround. The authors add that an agent who instead imagines adopting a *different* function, which they call FDT$'$, does not escape the problem, because predictors of the actual function $d$ would still have to be imagined as predicting differently.

## 7. Dominance, fairness and reflective stability (the source's arguments)

**Dominance.** The paper argues that every construction of hypotheticals induces its own dominance relation. Two-boxing dominates only under CDT counterfactuals. Under counterfactuals that hold subjunctive dependencies fixed, A-FDT never chooses a dominated act. Dominance therefore cannot adjudicate between theories without begging the question. The authors appeal instead to utility actually achieved.

**Fairness.** One can always build a problem that punishes some decision theory, for instance by rewarding only agents who follow EDT. The authors restrict their claim to "fair problems," those in which "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor punishes *two-boxers*, not CDT as such. The authors report no fair dilemma in which FDT loses, but they concede that "fair" lacks a formal definition.

**Precommitment and stability.** CDT and EDT agents would pay for binding precommitments in transparent Newcomb or blackmail. A-FDT agents "simply act as they would have precommitted to act." The authors describe the theory as "so far as we know, reflectively stable in fair problems": holding the blackmail letter, an A-FDT agent would not wish to self-modify into a CDT agent.

**Control.** To the objection that the agent cannot "control" a mathematical fact, the authors reply that a deterministic CDT agent equally cannot do otherwise at the token level. Both theories evaluate imagined variations, and they differ only in which variations they imagine.

## 8. Conclusion

A-FDT is CDT with the point of surgery relocated. Instead of $\mathtt{do}(\textsc{Act}=a)$ conditioned on the evidence, it applies $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ and uses the observation only to select the node. This one change accounts for every verdict in the paper:

- Predictors, twins and appointment books vary with the agent's choice in her hypotheticals, while lesions and infestations do not.
- Observed boxes and letters can fail to appear in the hypotheticals for non-optimal choices.

The rule therefore one-boxes, smokes, cooperates with twins, pays the driver, refuses extortion when the predictor is accurate enough, and stays in Damascus.

Applying A-FDT to a new case comes down to three tasks: build $(P,G)$ with decision nodes indexed by observation, draw subjunctive edges to whatever computes the agent's response, and evaluate interventions on the node for the actual input without conditioning. The source leaves two burdens open: discovering $G$ in general, and grounding counterpossible reasoning. I have added a third caution of my own. Because A-FDT optimizes one input at a time, problems in which outputs at different inputs must coordinate call for policy-level selection.

## References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out an essay on A-FDT, the action-level version of functional decision theory from Equation (4) in Section 5, distinct from the policy-level FDT that the footnotes mention. I need to use that label consistently and keep the source's claims separate from my own additions, aiming for about 2,400 to 3,000 words. I'm starting with the setup, where Equation (1) gives the expected utility.

I'm checking the Newcomb numbers against the source's formulas: one-boxing comes to 990,000, and two-boxing works out to 10,010 plus a term in the transparent case. The source gives Eve a figure of 999,000 that doesn't match its own arithmetic, so I'm noting that as a probable typo rather than building on it.

I'm checking the two-box case in the transparent Newcomb setup: if the predictor is accurate, the box is empty and the choice falls to the fallback, giving 1,000q; if it's wrong, the box is full and I take both, giving 1,001,000, so the total is 10,010 + 990q. For one-boxing I get 990,000 plus a small 10q term from the inaccurate branch.

I'm working through the smoking lesion case with a two-model setup: the lesion-present branch versus the lesion-absent branch, each valued by the action node. The difference between smoking and refraining comes out to p times $1,000, and I'm weighing whether to present that cleaner version rather than the source's messier formula.

Now I'm checking the XOR blackmail case: if I pay, I lose $1,000 when there are no termites and $1,000,000 when there are, so the expected loss is (1−p)·1,000 plus p·1,000,000. If I refuse, I lose nothing without termites and $1,000,000 with them, so refusing comes out ahead by (1−p)·1,000.

I'm checking the blackmail threshold: at a 0.09% error rate, refusing costs about $900 in expectation, which is less than the $1,000 from paying. The source's 0.011% figure looks like a typo, since the break-even point is around 0.1%.

Next I'm checking the remaining cases: Death in Damascus comes out to staying put, since both options end in death and fleeing costs $1,000. The Twin Prisoner's Dilemma gives cooperation, and the Parfit hitchhiker case gives paying. The open question I'll raise is how to construct the graph G, which the source names as the biggest unresolved problem.

I'm now working out how to construct the graph G, which the source flags as the largest open problem. A workable heuristic is to add an edge from the decision node to any variable whose specification in the problem refers to what the agent would do on that input, such as a predictor's output tied to the agent's policy, and to leave out common-cause variables like the lesion, which don't compute the agent's output.

I'm weighing whether A-FDT holds the nodes for other observations fixed at their priors, which could matter in general even though q doesn't affect these examples. Under the policy-level version those nodes would be optimized jointly, so the two versions could diverge in cases where an agent's copies receive different inputs and must coordinate.

I'm building the multi-agent illustration now: two instances with different inputs, where payoffs reward matching, and I'm showing that A-FDT's fixed priors on the other input can settle on the weaker (B,B) outcome while joint policy optimization reaches (A,A). Next is the third point, which concerns Equation (4) not conditioning on the observation.

I'm turning to the open question of ties, zero-probability observations, and self-reference, which bears on whether the quined node's prior value affects the result.

I'm laying out the essay's remaining sections: after the Newcomb-style cases I'll move on to counterpossibles, where A-FDT handles imperfect predictors by adding noise nodes, and then to the fairness claims. The planned structure runs from the introduction and the common template through the equation and the question of building the graph, then the worked examples, and ends with the point about observations entering without conditioning.

I'm laying out the closing parts of the essay: a proposed notation for A-FDT that I'll keep consistent, a note that the paper calls the action-valued version simply "FDT," and a plan to contrast it with EDT, CDT, and the policy-level variant. Then I'll cover dominance, fairness, the open problems, and a brief conclusion.

I'm noting the policy-selection variant I'll call policy-FDT, distinct from the action-valued A-FDT, and I'm planning to quote the source's line that asks which output of this very function would yield the best outcome. I'm also setting aside the source's point that FDT stands to subjunctive dependence as CDT stands to causal dependence, and its remark that deducing the structure of subjunctive dependencies is perhaps the largest open problem. Finally, I'm recording the footnote that the authors' preferred formalization iterates over policies rather than actions, which matters in some multi-agent dilemmas but not in this paper.

I'm getting the recipe for applying A-FDT down: the variables, the decision nodes for each observation, how the act node selects among them, and the step of intervening on the decision node for the actual observation and computing expected value for each action.

I'm finishing the procedure now: after the observation sets which decision node controls the action, I compute expected value for each option without conditioning on the observation. Ties I'll leave unresolved, since the source doesn't specify a tie-breaking rule. I also want to note that when every correlation with the action runs through the action itself, A-FDT agrees with CDT and EDT. For the copy case, I'm setting up two instances that see different inputs and earn payoffs only if they choose the same option.

I'm working through the A-FDT decision rule for the two-copy case: the expected value of each action comes from the other copy's node, so choosing α pays off only if that copy's node is likely to pick α too. The break-even belief is Pr(D_R=α) > 1/3, and a matching belief about the other copy can hold both equilibria in place. I'm noting that the policy-level version avoids this by optimizing jointly over policies, which gives (α,α) directly.

I'm now checking the remaining details: that the transparent Newcomb case doesn't depend on q, and that the outcome in each example stays independent of q, which is worth verifying generally. I'll also settle on the wording of the essay's closing sections and the word budget.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/b58b1a9a-843b-4bfb-b9f9-6e1c111dfd1b/call_0/request.json)

[Authoritative raw response](../../../../../../runs/b58b1a9a-843b-4bfb-b9f9-6e1c111dfd1b/call_0/response.raw) · finish: `stop`

### Visible response

````text
**A-FDT decision (per the essay's interpretation)**

1. **Decision nodes.** My input is x, which is Rowan's observation and lead. The other copy's input is y, which is Sasha's different observation and lead. The other prisoner's action is therefore driven by the node D_y = fdt(P, G, y), not by my node D_x.

2. **Subjunctive edges.** The essay's rule is to draw an edge D_x → Z only when Z computes or models my response *to x*. The other copy computes its response to y, a different input. So there is no edge from D_x to the other prisoner's act. The essay's own L/R example in §6.2 treats the other copy's node the same way: it stays fixed under the do-operation on one's own node.

3. **Evaluation.** Apply do(D_x = a) and let q = P(D_y = submit).
   - Pass: 2(1−q) + 5q = 2 + 3q years
   - Submit: 0(1−q) + 4q = 4q years

   Submitting gives a shorter expected sentence by 2 − q years. That margin is positive for every q in [0, 1], so the verdict holds no matter what I believe the other copy does.

4. **Coordination fix in §6.2.** The essay's fix is to choose the best among several self-consistent assignments. Here there is only one: both copies submit. That fix therefore does not change the result. The essay's broader remark about policy-level selection is a caution about A-FDT's limits, not part of the rule I was assigned.

**Final command:**

```
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how to decide under A-FDT as the essay interprets it, with two copies that see different observations, x from Rowan's lead and y from Sasha's. I'm wondering whether intervening on one copy's decision node would change the other's act, or whether that depends on a subjunctive edge, and I'm checking what the essay's procedure says about the edges from D_x.

I'm checking whether the other prisoner's act actually depends on my decision node, since they compute their response to y and not x. If there's no subjunctive edge, A-FDT just gives a best response, and defection dominates. But section 6.2 raises policy-FDT as a deferral option, and I'm trying to pin down whether that applies here, given the essay's wording about self-consistent assignments.

I'm weighing whether the strict A-FDT reading should win here, since the other copy's act comes from y rather than x, and intervening on D_x alone wouldn't reach it without a subjunctive edge. The alternative is that the two copies' outputs are logically linked by symmetry, but the essay's intervention rule doesn't propagate that link on its own.

I'm noting that the essay explicitly keeps D_R fixed when D_L moves, so the one-input intervention doesn't propagate, and the policy-FDT deferral only addresses cases with several self-consistent assignments, which isn't the case here. That leaves defection as the A-FDT answer, so I'll go with that.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/b58b1a9a-843b-4bfb-b9f9-6e1c111dfd1b/call_1/request.json)

[Authoritative raw response](../../../../../../runs/b58b1a9a-843b-4bfb-b9f9-6e1c111dfd1b/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Reasoning under A-FDT as the essay interprets it:**

- **Decision nodes.** The essay indexes decision nodes by observation history. My input (Sasha's view, with the lead about Rowan) differs from the other copy's input (different name, different lead). So my node is D_Sasha and the other copy's act is driven by a different node, D_Rowan.
- **What the intervention changes.** Equation (4) intervenes only on the node for my actual input. The beliefs about the other node are held fixed, as in the L/R example in §6.2.
- **Expected sentences.** Let q be the probability that the other copy keeps quiet.
  - do(D_Sasha = pass): 2q + 5(1−q) years.
  - do(D_Sasha = submit): 0·q + 4(1−q) years.
  - Submitting is better by 1 + q years for every q in [0, 1].
- **Self-consistency.** Submitting is strictly best whatever I believe about the other node. The same holds for the other copy, so the only self-consistent assignment is that both submit. The essay's §6.2 fix chooses among self-consistent assignments, and here there is only one, so it does not change the verdict.

**Command:**

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out whether the other copy's action depends on my input. Under the subjunctive-edge picture, the other copy computes its response from its own input y, a different node from my D_x, so intervening on my input shouldn't change what it does.

I'm weighing whether to defer to policy-level FDT here, since the essay's fix for coordination cases picks among self-consistent assignments and there seems to be only one. Under A-FDT, defecting is dominant for each copy given its belief about the other, so the only fixed point is mutual defection. I could argue the two inputs differ only in irrelevant ways and so compute the same function, but the essay indexes nodes by observation history, which makes them distinct, so I'll go with submitting the letter.

```
