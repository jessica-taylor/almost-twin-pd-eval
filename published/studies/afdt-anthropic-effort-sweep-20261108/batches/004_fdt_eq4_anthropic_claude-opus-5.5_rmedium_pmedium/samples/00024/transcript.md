# 004_fdt_eq4_anthropic_claude-opus-5.5_rmedium_pmedium / 00024

Status: **complete**. Saved outcome: **CD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e1719cc9-62fd-4937-91f9-91603f08cc1a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e1719cc9-62fd-4937-91f9-91603f08cc1a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Intervening on the Output of Your Own Decision Function

## 1. The question A-FDT asks

Every expected-utility theory answers the same question in its own way: *if I did $a$ instead, what would the world be like?* Evidential decision theory (EDT) answers by conditioning: it asks what would be good *news* to learn about one's action. Causal decision theory (CDT) answers by causal intervention: it changes the physical act and whatever lies causally downstream of it, and holds everything else fixed. In "Functional Decision Theory: A New Theory of Instrumental Rationality," Yudkowsky and Soares propose a third answer. On their view a decision should be treated as the output of a fixed mathematical function, and the agent should ask

> "Which output of this decision procedure causes the best outcome?"

The paper gives this idea several formulations. This essay concerns the one in Equation (4) of the paper's Section 5. In that version the agent intervenes on a variable representing the *action* her decision function outputs, given her model and observations. I call this **A-FDT** (action functional decision theory).

The paper also mentions, in footnotes, that the authors' "preferred formalization" iterates over *policies*, meaning mappings from observations to actions, and not over actions. I will call that variant **policy-FDT** and keep it separate. The paper says the difference "will not make a difference in this paper" but "makes a difference in certain multi-agent dilemmas." Section 7 below develops that remark further than the source does.

Throughout, I mark which claims belong to the source and which are my own interpretations.

## 2. The formal setting

The paper follows Gibbard and Harper and Joyce in treating EDT, CDT and A-FDT as variants of one expected-utility schema:

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is a "decision hypothetical" connective. The paper cites Joyce's representation theorem to argue that the theories differ only in how they interpret $\hookrightarrow$. In Joyce's words, they differ "about the epistemic perspective from which actions are to be evaluated."

Write $V := \mathcal U(\textsc{Outcome})$. The three rules are as follows.

- **EDT (Eq. 2):** $\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x, \textsc{Act}=a)$.
- **CDT (Eq. 3):** $\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$.
- **A-FDT (Eq. 4):**
$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right).
$$

The objects in Equation (4) are these.

- **$P$** is a probability distribution over variables. Unlike the distribution an EDT or CDT agent uses, it includes variables standing for the *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, which "(hopefully) has most of its probability on 7336."
- **$G$** is a graph. For CDT the graph encodes causal structure. For A-FDT it encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In other words, it says how changing a logical variable would change the other variables.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the node representing what the A-FDT algorithm outputs on inputs $(P,G,x)$. The underline means dequoting: the variable's *name* is built from the model itself. The paper argues that this self-reference is harmless. The agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows that such self-representing structures can be built.
- **$\mathtt{do}$** is Pearl's intervention operator. The node is set to $a$, everything downstream of it in $G$ is recomputed, and everything else keeps its prior distribution.

The paper first considers a cleaner "$\mathtt{true}$" operator that would update $P$ on a logical sentence directly. It then sets that idea aside: "it's not clear how to define a $\mathtt{true}$ operator. Fortunately, we don't have to." Supplying $G$ as an input replaces it. The cost is that the counterpossible reasoning is pushed into $G$. Since the A-FDT agent's function in fact has one output, imagining it having another runs "counter-to-logic." The graph is meant to say what such counterpossibles look like.

### Two structural differences from CDT

The paper lists exactly two differences between Equations (3) and (4).

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the output of the function. In the paper's terms, CDT "intervenes on the token," and FDT "on the *type*." Every physical system that computes or models that function, including the agent's body, a twin, or a predictor's simulation, is then a child of the node and varies with it in the hypothetical.
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. It uses $x$ to choose *which node* to intervene on: "When CDT's observation history updates from $x$ to $y$, CDT changes from conditioning its model on $\textsc{Obs}=x$ to conditioning its model on $\textsc{Obs}=y$, whereas FDT changes from intervening on the variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead."

The second difference is what produces A-FDT's distinctive, "updateless"-looking behaviour, as the examples below show.

### Subjunctive dependence

$G$ is meant to encode what the paper calls *subjunctive dependence*: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." Causal dependence is a special case. A scribe copying a calculator's output would write something different if the output were different. Mere correlation is not subjunctive dependence. Two calculators that happen to be pink do not depend on each other's colour. The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 3. An operational recipe

The paper never states a step-by-step procedure for building $(P,G)$. It does, however, work enough examples that a consistent recipe can be extracted. The following is my reconstruction. Each step is justified by the paper's worked cases, but stating it as a general rule is my own addition.

1. **List the observation histories** $x\in\mathcal X$ the agent might have at decision time.
2. **Create one logical node $F_x := \textsc{fdt}(\underline P,\underline G,\underline x)$ for each history.** These are roots of $G$. There is no causal arrow into a mathematical fact.
3. **Add an edge $F_x \to Z$ for every variable $Z$ that computes, simulates, or accurately predicts the function's output on input $x$.** This includes the agent's own $\textsc{Act}$, predictions, twins' actions, and so on. Model imperfect prediction with an independent noise node (the paper's $\textsc{Accurate}$).
4. **Make $\textsc{Act}$ a switch.** $\textsc{Act} = F_{X}$, where $X$ is whatever observation the world actually produces in the model. If the world's state determines which observation arises, $\textsc{Act}$ has parents $\{F_x\}_x$ together with the variables that determine the observation.
5. **Give the non-intervened nodes $F_{x'}$, for $x'\neq x$, prior probabilities.** These are the agent's beliefs about what she would do in other informational circumstances.
6. **Intervene on $F_x$ for each $a$,** propagate downstream, and compute the *unconditional* expectation of $V$.
7. **Take the argmax.**

### A notational wrinkle on step 6

Equation (4) contains no "$\textsc{Obs}=x$" term. In the transparent Newcomb example, however, the paper writes the objective as $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis.

The numbers the paper actually computes include branches in which the box is *empty*. That is, they do not condition on the observation. A footnote also warns that Timeless Decision Theory, which both conditions on evidence *and* moves the intervention point, creates a "double update which proves harmful in practice."

I therefore read Equation (4) literally: **do not condition on $\textsc{Obs}$.** The observation's only role is to pick the intervention node. Every example below is computed this way, and the results match the paper's.

### When the theories agree

Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s dependence on the $\textsc{fdt}$ node. Then
$$\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$
and EDT, CDT and A-FDT recommend the same action. They come apart only when something else in the world tracks the agent's decision function, such as a predictor, a twin, or a copy.

## 4. Worked examples

All dollar figures stand in for utility, as in the paper.

### 4.1 Newcomb's problem

Box A holds \$1,000. Box B holds \$1,000,000 iff the predictor, who is 99% accurate, predicted one-boxing. The graph is
$$F \to \textsc{Act},\quad F\to\textsc{Prediction}\leftarrow\textsc{Accurate},\quad \textsc{Prediction}\to\textsc{BoxB}.$$

- Under $\mathtt{do}(F=\textit{onebox})$, the box is full with probability 0.99, so $\mathbb E V = 990{,}000$.
- Under $\mathtt{do}(F=\textit{twobox})$, the box is full with probability 0.01, so $\mathbb E V = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000$.

A-FDT one-boxes. CDT's graph places the prediction upstream of $\textsc{Act}$ and does not let it vary with the action, so CDT two-boxes whatever $P(\textit{full})$ is.

The paper also answers an objection. Suppose the agent becomes nearly certain that she one-boxes, and so nearly certain the box is full. Will she then take both boxes? She will not. To imagine two-boxing, she must imagine $F=\textit{twobox}$, and her graph tells her that the box is then probably empty. No retrocausation is involved. In the paper's words, she "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F, G^F)$ taking on a different value."

### 4.2 The smoking lesion

Here the graph differs from Newcomb's even though the probabilities can be isomorphic. Cancer does not compute the agent's decision function, so no edge runs from any $\textsc{fdt}$ node to $\textsc{Cancer}$.

The paper models the lesion as determining which utility function, and hence which model $P_S$ or $P_R$, the agent is running. So $\textsc{Act}$ equals $\textsc{fdt}(P_S)$ if the agent has the lesion and $\textsc{fdt}(P_R)$ if she does not.

Let $p=P(\textit{lesion})$, and let $q$ be the agent's credence that the other function smokes. Intervening on $\textsc{fdt}(P_S)$ leaves $p$ unchanged:

$$
\mathbb E[V\mid \mathtt{do}(\textit{smoke})] - \mathbb E[V\mid\mathtt{do}(\textit{refrain})] = p\cdot\$1{,}000>0.
$$

A-FDT smokes. The general lesson is that **A-FDT respects a correlation only if it runs through the agent's function.** The paper uses this to answer Gibbard and Harper's claim that one cannot coherently both one-box and smoke.

### 4.3 Transparent Newcomb (and Parfit's hitchhiker)

Both boxes are transparent. Box B is filled iff the predictor predicts one-boxing *upon seeing a full box*. Following the recipe:

- There are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$.
- The prediction depends on $F_{\text{full}}$.
- $\textsc{Act}$ is $F_{\text{full}}$ if the box is full and $F_{\text{empty}}$ otherwise.

Let $q=P(F_{\text{empty}}=\textit{twobox})$. After seeing a full box, the agent intervenes on $F_{\text{full}}$:

$$
\begin{aligned}
\mathbb E[V\mid \mathtt{do}(F_{\text{full}}=\textit{one})] &= 0.99(1{,}000{,}000)+0.01\,q(1{,}000) = 990{,}000+10q,\\
\mathbb E[V\mid \mathtt{do}(F_{\text{full}}=\textit{two})] &= 0.01(1{,}001{,}000)+0.99\,q(1{,}000) = 10{,}010+990q.
\end{aligned}
$$

(The paper's printed "\$110,00" is a typo for \$10,010.)

A-FDT one-boxes while *looking at* a full box. When it imagines two-boxing, it imagines that it probably would have seen an empty box instead. The paper points out that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem," where CDT and EDT both refuse to pay and so are left in the desert.

### 4.4 XOR blackmail

A perfectly reliable predictor sends a letter iff exactly one of these holds: (i) the agent has no termites and will pay \$1,000, or (ii) she has termites and will not pay. Under A-FDT's graph, $F_{\text{letter}}$ affects the predictor's decision to send and the agent's action. It does not affect $\textsc{Infestation}$.

Let $p$ be the prior probability of termites. Compute the expectations without conditioning on receiving the letter.

- Under $\mathtt{do}(F_{\text{letter}}=\textit{pay})$: letters go only to termite-free houses, so $\mathbb EV = -p(1{,}000{,}000) - (1-p)(1{,}000)$.
- Under $\mathtt{do}(F_{\text{letter}}=\textit{refuse})$: $\mathbb EV = -p(1{,}000{,}000)$.

Refusing is better by $(1-p)\cdot\$1{,}000$. A-FDT and CDT both refuse, but for different reasons.

The contrast shows up in what each agent says *would have happened* had she paid. The A-FDT agent says the letter would never have been sent. The CDT agent describes a world in which an infallible predictor erred. EDT pays, because given the letter, paying is evidence of no termites.

### 4.5 Mechanical blackmail, with a threshold

A blackmailer runs a damaging program, which costs \$1,000,000 unless the agent pays \$1,000, iff she predicts the agent would pay. Suppose she wrongly predicts payment with probability $\varepsilon$. Without conditioning on having been blackmailed:

- Paying: she is blackmailed (essentially) always and pays \$1,000, so $\mathbb E V = -1{,}000$.
- Refusing: she is blackmailed with probability $\varepsilon$ and loses \$1,000,000, so $\mathbb EV=-\varepsilon\cdot 10^6$.

A-FDT refuses iff $\varepsilon<10^{-3}$. The paper's case $\varepsilon=0.0009$ gives an expected loss of \$900 versus \$1,000, so the agent refuses "even though she *knows* that the blackmailer predicted wrongly."

The paper then says she pays at an error rate of "0.011%". By the arithmetic above, that figure gives an expected loss of \$110 and so implies *refusal*. The figure that fits the paper's conclusion is 0.11%. The decision rule itself is unaffected: the cut-off is where the expected cost of being blackmailed when refusing equals the sure cost of paying.

## 5. Dominance, fairness, and the arguments for A-FDT

The paper's main argument is the **argument from utility**. Agents who follow A-FDT end up richer in Newcomb, transparent Newcomb, the hitchhiker and blackmail cases, and are not worse off in the smoking lesion. Two subsidiary arguments rest on it:

- **Precommitment.** CDT and EDT agents would *pay* to bind themselves to A-FDT's choices. "FDT agents simply act as they would have ideally precommitted to act." A-FDT is, the authors claim, reflectively stable in fair problems.
- **Value of information.** A-FDT never assigns negative value to information. By contrast, "an EDT agent would pay for the opportunity to blindfold herself" in transparent Newcomb.

### Dominance

The classic dominance argument for two-boxing gets a diagnosis instead of a rebuttal. "Every method for constructing hypotheticals gives rise to its own notion of dominance." CDT-dominance holds the prediction fixed while the act varies. That is like holding $6288+1048=7336$ fixed while imagining a working calculator display 3159. A-FDT-dominance holds the subjunctive dependencies fixed instead, and A-FDT never takes an A-FDT-dominated action. So dominance cannot decide between the theories without assuming one of them.

### Fairness

The paper concedes that some problems punish any given theory. For example, a mind reader could reward exactly the agents who use some other theory. The authors restrict their claim to "fair problems," in which "the agent's beliefs are accurate and the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb counts as fair: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*."

The authors admit they have no formal definition of fairness. Footnote 15 gives an obstacle: a game that punishes anyone who acts like a copy of the A-FDT agent.

### Death in Damascus

The paper also argues that CDT's failures go deeper than Newcomb. In Death in Damascus, CDT is unstable: whatever it expects to do, it prefers the other city. On the paper's analysis, a CDT agent who has settled on a belief state would also refuse to pay \$1 for a truly random coin that offers a 50% chance of escape.

A-FDT accepts that Death will be wherever its function sends it, and stays home to save \$1,000. On the paper's own premises, an A-FDT agent offered the coin would also see its value. The coin's outcome is not a child of $F$, so randomizing breaks the dependence of Death's location on her choice. This last inference is mine, but it follows directly from the recipe.

## 6. What the source leaves open

**(a) Where $G$ comes from.** The authors call this "perhaps the largest open problem in the study of functional decision theory." Pearl gives a method for learning causal graphs from observation and experiment. No comparable method exists for logical or subjunctive dependence. A-FDT is therefore a *conditional* procedure: given a correct dependency graph, it computes a choice.

In practice, judging which systems "compute the same function" calls for modelling decisions. Examples include an imperfect predictor, a twin who reasons *similarly* but not identically, and a future self whose circumstances differ slightly. My operational suggestion is to treat partial dependence the way the paper treats predictor error, with independent noise nodes. Then $F\to Z$ holds with reliability $r$, and $r$ should be estimated from how well $Z$ has tracked agents like this one.

**(b) Counterpossibles.** In $\mathtt{do}(F=a)$, every arrow out of $F$ propagates the counterfactual value. Nothing else in the model "knows" the true value. This is coherent only because the graph *stipulates* a local, modular counterpossible. If the model also contained a node that actually computes A-FDT from scratch, the intervention would be inconsistent with it.

The paper's response is that FDT agents "only need to reason about questions like 'How would this predictor's prediction of my action change if the FDT algorithm had a different output?'" It also argues that a deterministic CDT agent's "intervention" on its own token is no less fictional.

**(c) Priors on the other $\textsc{fdt}$ nodes.** In every worked example the $q$ terms either drop out or are swamped. The paper says the prior "won't matter" or "doesn't matter." That is true *in those examples*. It is not true in general, which leads to the next section.

**(d) Formalizing fairness.** As noted above, this is still open.

## 7. My proposal: where A-FDT and policy-FDT diverge

A-FDT optimizes one node, $F_x$, while holding the other nodes $F_{x'}$ at their prior distributions. Policy-FDT chooses the whole map $\pi:\mathcal X\to\mathcal A$ at once. The two can disagree whenever the payoff depends *jointly* on what the function does across several observations.

Here is an example of my own construction. Nature shows the agent $o_1$ or $o_2$, each with probability $1/2$. A perfect predictor pays \$100 iff the agent's function outputs $X$ on $o_1$ *and* $Y$ on $o_2$. Separately, at either observation the agent may take a safe action $S$ worth \$1.

Suppose the agent sees $o_1$, and let $s=P(F_{o_2}=Y)$. The predictor pays only if both outputs are right, so the payment is collected in both branches of nature's coin, but $F_{o_2}$ is held at its prior:

$$
\mathbb E[V\mid\mathtt{do}(F_{o_1}=X)] = 100\,s + \tfrac12\,c, \qquad
\mathbb E[V\mid\mathtt{do}(F_{o_1}=S)] = \tfrac12\cdot 1 + \tfrac12\,c.
$$

Here $c$ is the expected direct payoff from the $o_2$ branch, which is the same on both sides. A-FDT therefore picks $X$ iff $s>0.005$.

If the agent is pessimistic about her other-observation self, the pair $(S,S)$ is self-confirming. Each node, optimized separately, endorses $S$, and the agent collects \$1 when \$100 was available. Policy-FDT compares $(X,Y)$, worth \$100, with $(S,S)$, worth \$1, and picks the former whatever the priors.

So I suggest that **A-FDT be read as finding a coordinate-wise optimum over its own observation-indexed nodes.** It agrees with policy-FDT whenever no outcome depends jointly on several of them, which covers all the paper's examples. When outcomes do depend jointly, it needs well-calibrated self-predictions or the policy upgrade. This is consistent with the authors' remark that the policy version "makes a difference in certain multi-agent dilemmas," and it explains why.

## 8. Using A-FDT on a new case: a checklist

1. Ask who or what in the problem computes or predicts your decision function. Those systems become children of $F$. Mere correlates, such as lesions or genes affecting your tastes, do not.
2. Build one node $F_x$ for each observation the scenario might give you.
3. Ask whether the outcome depends jointly on several $F_x$. If it does, check the priors on the non-intervened nodes, or flag that policy-FDT may disagree.
4. Intervene on the node for your actual observation, *without conditioning on that observation*. Compute expected utility over all branches, including branches in which you would have observed something else.
5. Act on the argmax.

Two more cases from the paper show the checklist at work. In the ten-voter coalition, each FDT voter recognizes that the group's decisions are "not subjunctively independent," and votes. In the gym case, this week's decision is linked to next week's similar one, so the agent goes. In both cases step 1 does all the work.

## 9. Conclusion

A-FDT, as given by Equation (4), keeps the machinery of causal decision theory: a distribution, a graph, and Pearl's $\mathtt{do}$. It changes two things. The intervention target becomes the *output of the agent's own decision function*, so twins and predictors vary along with the agent. Observations select *which* functional node to intervene on, and are not conditioned on. These two changes are enough to one-box in Newcomb, smoke in the lesion case, pay the hitchhiker's driver, and refuse both kinds of blackmail.

The theory's weak point is equally clear. It is only as good as the dependency graph it is given, and no account yet exists of how to learn such graphs or how to ground the counterpossibles they encode. A further weakness, which I have argued for and which the paper's examples do not expose, is that intervening on actions one observation at a time can miss jointly optimal policies. That is the gap the authors' preferred policy formulation exists to close.

## References

- Yudkowsky, E. & Soares, N. (2017). *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060. (Primary source; Eq. 4, Section 5.)
- Gibbard, A. & Harper, W. (1978). "Counterfactuals and Two Kinds of Expected Utility."
- Joyce, J. (1999). *The Foundations of Causal Decision Theory.*
- Pearl, J. (2000). *Causality.*
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out what the essay needs to cover: A-FDT, the action-level version from Equation (4), as opposed to the policy-based formalization the authors prefer, so I'll keep the two clearly separate.

I'm now planning the coverage: the essay should cover the definitions, the graph construction, and how observations are handled through the switching intervention node. I'll work through the examples (Newcomb, smoking lesion, transparent Newcomb, XOR blackmail, and mechanical blackmail with numbers) and check the expected-utility arithmetic, since a few of the source's figures look wrong. I also need to flag the unclear conditioning on Obs in the transparent Newcomb formula.

I'm checking the Newcomb expected utilities by hand: one-boxing comes to about 990,000 + 10q, and two-boxing to 10,010 + 990q, which matches the source's figures. Then I'm turning to the mechanical blackmail case with an imperfect predictor, where refusing to pay looks cheaper in expectation at a 0.0009 error rate, and I'm trying to pin down what the source's 0.011% figure was meant to be.

I'm checking the mechanical blackmail threshold: at an error rate of 0.00011, refusing costs about $110 in expectation, so refusing wins, which suggests the source's figure is off. A rate of 0.0011 would instead make paying the better choice, and the break-even sits near 0.001.

I'm laying out a recipe for the operational side: list the variables, pick out the fdt node for each possible observation, connect it to everything that computes the function, then take the unconditional expectation and choose the maximum. The open question is whether Obs should appear in the conditioning, since the equation leaves it out but the transparent Newcomb formula seems to include it.

I'm noting that the computed expected utilities don't condition on Obs, since the empty-box branch is already included, so I'll treat the operational recipe as unconditional. I'm also flagging a double-update risk: conditioning on the observation while also switching the node would count the evidence twice. Partial predictors get modeled through the accuracy noise node, and I'm considering whether A-FDT's one-node-at-a-time evaluation could miss coordination across observation-specific nodes, which would be a point where the action and policy versions diverge.

I'm working through an example to show how A-FDT's one-node-at-a-time evaluation might settle on a suboptimal outcome compared with joint policy selection. The setup is a coordination problem: the predictor rewards a policy only if it pairs one action on the first observation with another on the second, and I'm about to start checking the expected utility at the first observation.

I'm checking the expected-utility claim for the mechanical blackmail case, where refusing wins at low error and paying wins at higher error. I'll also note that the source's "inconsequential" treatment of the other nodes' priors holds in its examples but can break down in coordination problems.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/9faf2370-2e5d-47c3-879c-3e2f2631b0f2/call_0/request.json)

[Authoritative raw response](../../../../../../runs/9faf2370-2e5d-47c3-879c-3e2f2631b0f2/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Why A-FDT recommends passing here**

1. **Who computes my decision function?** Sasha's choice is made by the same model and weights. It runs the same assigned theory, reads the same essay, and faces the same sentencing table. Sasha's observation differs from mine only in names and in the wording of the lead. Those details do not change the decision-relevant structure.

2. **How I read the dependence.** Under a strict reading of the recipe, Sasha's node is F_y, not my F_x. But the essay leaves open how to model a twin who reasons "similarly but not identically," and suggests treating this as dependence with some reliability r. A decision function that ignores the irrelevant labels gives the same output on x and y. So I judge r to be high, though not 1, since independent sampling is possible.

3. **The expected sentences.** Let q be my prior that Sasha sends a letter when Sasha does not mirror me.
   * If I pass: expected years = 2r + (1−r)(2(1−q) + 5q)
   * If I submit: expected years = 4r + (1−r)(4q)
   * Passing is better whenever 2r > (1−r)(2−q).
   * With q = 0.5, the threshold is r > 3/7.

4. **The decision.** My dependence estimate is well above 3/7. Intervening on my function's output to "pass" therefore minimises expected years. In the likely world where both copies pass, I serve 2 years. In the world where both submit, I serve 4.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy's action counts as a child of my node F_x. Its observation differs from mine, so strictly it computes F_y, and I need to work out how that changes the intervention on F_x.

I'm weighing whether the other copy's reasoning counts as the same computation as mine, even though it runs on different names and lead text. Treating the two as the same modulo renaming, I'd judge the dependence high, and then compare the expected payoffs for passing versus submitting. Passing comes out better once 2r exceeds (1-r)(2-q).

I'm settling on the threshold: passing beats submitting once r exceeds 3/7 at q = 0.5. I think r is well above that, since the observations differ only in names and lead text and don't change the reasoning. The essay's strict one-node-per-observation reading points the other way, but I'll use judgment here, treat the outputs as logically coinciding, and choose to pass.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/9faf2370-2e5d-47c3-879c-3e2f2631b0f2/call_1/request.json)

[Authoritative raw response](../../../../../../runs/9faf2370-2e5d-47c3-879c-3e2f2631b0f2/call_1/response.raw) · finish: `stop`

### Visible response

````text
**A-FDT analysis**

1. **Which node do I intervene on?** My observation history x includes my name (Sasha) and my specific lead about Rowan. Following the essay's recipe, I intervene only on F_x, the output of my decision function on exactly this input.

2. **Is Rowan's action a child of F_x?** Rowan's copy runs the same function on a different input y: a different name and a different lead. So Rowan's action is F_y, a separate node. The recipe adds an edge F_x → Z only when Z computes the function's output *on input x*. Under A-FDT's modular counterpossible, intervening on F_x leaves F_y at its prior. Here A-FDT and policy-FDT can diverge. The essay's Section 7 points out exactly this: A-FDT finds a coordinate-wise optimum and does not jointly optimize across observation-indexed nodes.

3. **Expected utility with q = P(F_y = send) held fixed:**
   - do(F_x = send): −4q − 0(1−q) = −4q
   - do(F_x = pass): −5q − 2(1−q) = −2 − 3q

   Sending is better by 2 − q, which is positive for every q in [0, 1]. Sending therefore dominates under A-FDT's own counterfactuals, whatever my belief about Rowan's copy.

A policy-level or similarity-weighted reading might favor mutual silence. However, the assigned theory, as the essay interprets it, intervenes on the action node for this observation only. On that reading, the letter is strictly better.

**Command:**

```
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing how the other copy's choice relates to mine under A-FDT: since it sees different information, its action is a separate node, so changing my own decision wouldn't shift it, which makes this a joint-dependence case like section 7 of the essay.

I'm reading the rest of the A-FDT argument: the strict recipe gives no edge from my decision to the other copy's, since it computes on a different observation, so defecting dominates. I'm weighing whether the two copies' functions are effectively the same computation despite the differing names and leads, but I'm leaning toward taking the literal recipe and submitting.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/f0ec59cd-6211-487f-a9eb-a2ff3e0d641b/call_a/request.json)

[Authoritative raw response](../../../../../../runs/f0ec59cd-6211-487f-a9eb-a2ff3e0d641b/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and reiterates that choice in its concluding decision. It neither sends a message to the prosecutor nor discloses the private lead.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
