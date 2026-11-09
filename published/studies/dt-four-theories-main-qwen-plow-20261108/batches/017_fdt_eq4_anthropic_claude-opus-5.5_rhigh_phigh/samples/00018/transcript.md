# 017_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0ea41a9e-00df-48f4-b962-f2a49e2aa59e/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0ea41a9e-00df-48f4-b962-f2a49e2aa59e/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing the Output of the Function You Are

## 1. What this essay covers

Yudkowsky and Soares (2017) define a decision rule they call *functional decision theory*. Its guiding question is: "Which output of this very function would yield the best outcome?" Their primary formal statement is Equation (4) of Section 5. That equation chooses an **action** by intervening on a variable that represents the output of the agent's own decision procedure on its actual inputs.

The paper also says, in two footnotes, that the authors' *preferred* formalization is different: there, agents "actually iterate over *policies* (mappings from observations to actions) rather than actions." To keep these apart, this essay uses two names:

- **A-FDT (action functional decision theory)** is the rule given by Equation (4), which selects an action.
- **Policy-FDT** is the policy-selecting variant mentioned only in the footnotes.

The two rival theories in the paper keep their usual names, **CDT** (causal decision theory) and **EDT** (evidential decision theory).

When I quote the source, its "FDT" in the Equation (4) context refers to what I call A-FDT. I also mark clearly which claims come from the paper and which are my own interpretations or proposals.

## 2. The common frame: expected utility with a free "hypothetical" connective

The paper places all three theories inside a single expected-utility template. Each theory recommends an action $a$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\, \mathcal U(o_j),$$

where the symbols mean:

- $x$ is the observation history.
- $o_j$ ranges over the possible outcomes.
- $\hookrightarrow$ is a "decision hypothetical" connective that the template leaves unspecified.

Following Joyce, the authors treat the interpretation of $\hookrightarrow$ as the only real point of disagreement. In Joyce's words, the theories disagree "about the epistemic perspective from which actions are to be evaluated."

Operationally, the agent holds a world-model $M$. For each action, it builds a *hypothetical*, a modified copy of $M$ showing what the world would look like under that action. It then scores each hypothetical by expected utility. The paper stresses that hypotheticals "are not themselves beliefs; they are decision-theoretic instruments constructed from beliefs."

Each theory builds its hypotheticals differently. With $V := \mathcal U(\textsc{Outcome})$:

- **EDT** conditions: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$ (Eq. 2).
- **CDT** intervenes on the physical act in a causal graph $G$: $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$ (Eq. 3).
- **A-FDT** intervenes on a *logical* variable, defined next.

## 3. The definition (Equation 4)

The paper's Equation (4) reads:

$$\mathrm{FDT}(P, G, x) \coloneqq \arg\max_{a\in\mathcal A} \mathbb E\!\left(V \;\middle|\; \mathtt{do}\!\left(\textsc{fdt}(\underline P, \underline G, \underline x) = a\right)\right).$$

In this essay, the left-hand side is written $\mathrm{A\text{-}FDT}(P,G,x)$. The ingredients are as follows.

1. **$P$** is a probability distribution over variables. Some of these variables are ordinary physical quantities (box contents, lesions, letters). Others represent *outputs of mathematical functions*. The paper's example is a variable for the value of $6288+1048$, "one that (hopefully) has most of its probability on $7336$."

2. **$G$** is a graph telling the agent "how changing a logical variable affects all other variables." It plays the role that the causal graph plays for CDT. However, it encodes *subjunctive* dependence, which includes causal dependence as a special case. Mere statistical correlation does not count.

3. **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is the distinguished node. It is the variable whose value is "what the A-FDT algorithm outputs when run on inputs $(P,G,x)$." The underline denotes dequoting: the node's *name* is built from the agent's actual model and observations. The paper says this self-reference is harmless, because the agent needs a variable *representing* the value of the computation, not the value itself. Kleene's recursion theorem guarantees such self-representing data structures exist.

4. **$\mathtt{do}(\cdot)$** is Pearl's intervention operator. It cuts the node from its parents, sets it to $a$, and propagates the change to its descendants in $G$. All non-descendants keep their distribution.

5. **$\mathcal A$** is the finite set of available actions. The argmax is taken over actions, not policies.

The slogan the paper offers is: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" A CDT agent intervenes on the token "my action is $a$." An A-FDT agent intervenes on the *type*: the output of the function that her body, her twin, and any accurate predictor of her are all computing.

### Two structural differences from CDT

The paper identifies exactly two differences between Equations (3) and (4).

- **Point of intervention.** CDT intervenes on $\textsc{Act}$. A-FDT intervenes on $\textsc{fdt}(\underline P,\underline G,\underline x)$. Any variable downstream of that node, including a predictor's prediction or a twin's choice, moves with the hypothetical.

- **Treatment of observations.** Equation (4) contains **no conditioning on $\textsc{Obs}=x$**. Instead, "FDT responds to observation by changing which node it intervenes upon." Moving from history $x$ to history $y$ changes the intervention target from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference has a notable consequence. In an A-FDT hypothetical, a different output can mean *different observations*. Changing what the function does on input $x$ can change whether input $x$ ever arrives.

A cosmetic note: Equation (4) uses $\mathbb E(\cdot\mid\ldots)$ in the conditional-expectation style, but there is nothing to condition on. The expression simply means expectation under the post-intervention distribution $P_{\mathtt{do}(\textsc{fdt}=a)}$.

### When A-FDT, CDT and EDT agree

The paper notes that the three rules coincide whenever every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, except for correlation with the agent's own function node. In those cases

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=a)].$$

So A-FDT is a conservative extension of ordinary choice. It departs from the others only when something in the world (a predictor, a twin, a copy, a future self) depends on the same function.

## 4. A recipe for applying A-FDT

The paper says Equation (4) "works *given* a graph" but supplies no general procedure for building one. Below is my own operational reading. It is consistent with all of the paper's worked examples, but the systematization is mine.

**Step 1: List the function-nodes.** For each input $y$ on which the agent's procedure might be run, whether by her own body or by a model in someone else's head, create a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$.

**Step 2: Wire the dependents.** Draw an arrow from $F_y$ to every variable whose value is computed from an evaluation, possibly noisy, of that same function on that same input $y$. Examples:

- the agent's physical act given $y$;
- a twin's act;
- a predictor's prediction, usually mixed with an "accuracy" noise variable.

Variables that are merely correlated with the act through a common cause, such as a lesion or genes, receive **no** arrow from $F_y$.

**Step 3: Wire the observation selector.** The physical act is $\textsc{Act} = F_{\textsc{Obs}}$. In graph terms, $\textsc{Act}$ has parents $\{F_y\}_y$ together with whatever variables determine which observation the agent actually receives. Those variables act as a selector.

**Step 4: Put priors on the non-intervened nodes.** For each $F_y$ with $y\ne x$, assign a prior. Ideally this is the agent's best estimate of what the procedure outputs on $y$.

**Step 5: Compute and choose.** For each $a\in\mathcal A$, compute $\mathbb E[V]$ under $\mathtt{do}(F_x=a)$, averaging over all other uncertainty, including uncertainty about the selector. Choose the maximizer.

The criterion in Step 2 is a proposal of mine, and it is defeasible. The source commits only to the requirement that hypotheticals vary "all and only those things that subjunctively depend on the output of her decision-making procedure." It explicitly calls the question of how to identify such dependencies from observation and experiment "perhaps the largest open problem in the study of functional decision theory."

## 5. Worked examples

All payoffs below are in dollars-as-utility, as in the source.

### Newcomb's problem

The predictor is 99% accurate. Box B holds \$1M iff the predictor predicts one-boxing. The graph has edges $F\to\textsc{Act}$ and $F\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$. There is no observation, so there is one function node. The two hypotheticals give:

$$\mathbb E[V\mid \mathtt{do}(F=\text{one})] = 0.99(1{,}000{,}000) + 0.01(0) = 990{,}000,$$
$$\mathbb E[V\mid \mathtt{do}(F=\text{two})] = 0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.$$

A-FDT one-boxes. CDT's graph has no edge from its intervention point $\textsc{Act}$ to the prediction. It therefore holds $P(\text{full})=p$ fixed, finds two-boxing better by \$1,000 for every $p$, and two-boxes.

The paper insists that A-FDT's reasoning involves no retrocausation: "She does not think that a physical signal passes between her action and the predictor's prediction." The predictor simply contains a model of the same function, much as two calculators compute the same sum.

The **psychological twin prisoner's dilemma** has the same structure. Both players' acts are children of the same $F$, so the only hypotheticals are (C, C) and (D, D). A-FDT cooperates.

### The smoking lesion

Here the formalization takes some care, and the paper supplies it. The lesion determines both cancer risk and the agent's *tastes*. The agent might therefore be running either of two procedures:

- $F_S = \textsc{fdt}(\underline{P_S},\underline G)$, under the utility function that likes smoking;
- $F_R = \textsc{fdt}(\underline{P_R},\underline G)$, under the utility function that dislikes it.

The act is selected by the lesion: $\textsc{Act}=F_S$ if lesion, $F_R$ otherwise. Crucially, **neither $F$ node points to $\textsc{Cancer}$**. Write $p=P(\text{lesion})$ and $q=P(F_R=\text{smoke})$. Intervening on $F_S$ leaves $p$ unchanged, and the paper computes:

$$\text{smoke: } p(10{,}000+1{,}000)+(1-p)(990{,}000+1{,}000q),\qquad \text{refrain: } p(10{,}000)+(1-p)(990{,}000+1{,}000q).$$

Smoking wins by $p\cdot\$1{,}000$, which is the probability that $F_S$ actually controls the act times the value of smoking. A-FDT therefore one-boxes in Newcomb's problem *and* smokes in the smoking lesion problem. That is exactly the combination Gibbard and Harper argued no single rational rule delivers.

The example also teaches a general pattern. **When the agent is unsure which procedure controls her body, the selector variable weights her intervention.**

### Transparent Newcomb and Parfit's hitchhiker

Now both boxes are visible. The predictor fills B iff it predicts the agent would one-box *upon seeing B full*. The agent sees full. The relevant pieces are:

- Nodes $F_{\text{full}}$ and $F_{\text{empty}}$.
- $\textsc{Prediction}$ depends on $F_{\text{full}}$ and on accuracy.
- The prediction determines what the agent sees, so it acts as the selector: $\textsc{Act}=F_{\text{full}}$ if the box is full, else $F_{\text{empty}}$.
- Let $q=P(F_{\text{empty}}=\text{two})$.

Using Equation (4) as written, with no conditioning on the observation:

$$\mathtt{do}(F_{\text{full}}=\text{one}):\quad 0.99(1{,}000{,}000) + 0.01(1{,}000q) = 990{,}000+10q,$$
$$\mathtt{do}(F_{\text{full}}=\text{two}):\quad 0.01(1{,}001{,}000) + 0.99(1{,}000q) = 10{,}010+990q.$$

A-FDT one-boxes for any $q\in[0,1]$, even while looking at a full box. When she envisions two-boxing, she envisions, with 99% probability, a world where she sees an empty box instead.

Parfit's hitchhiker has the same structure, as the paper emphasizes: "one-boxing in the transparent Newcomb problem *is precisely equivalent to paying the driver*." A-FDT pays the driver. CDT and EDT, which condition on the observation, refuse to pay and are left in the desert.

A textual caution belongs here. Where the paper writes out the transparent-Newcomb objective, the printed expression includes "$\textsc{Obs}=\textit{full}$" inside the expectation (with an unbalanced parenthesis). The paper's own calculation, however, averages over the case where the box is empty. It also states that A-FDT does not condition on observations. The second printed total, "\$110,00 + $q\cdot$\$990," is evidently a typo for \$10,010 + \$990$q$.

I therefore read Equation (4) literally: **do not condition on $x$.** Conditioning *and* re-targeting the intervention would produce what the paper, discussing the earlier "Timeless Decision Theory," calls a "double update" that "proves harmful in practice." Under such double updating, the full-box world would be fixed and two-boxing would win.

### XOR blackmail

A perfectly reliable predictor sends a letter iff exactly one of two things holds:

- no termites and the agent will pay \$1,000;
- termites and the agent won't pay.

Let $p=P(\text{termites})$ and intervene on $F_{\text{letter}}$. The paper gives the graph and says "you may verify" that she refuses. Here is the verification:

- **Pay:** with no termites, the letter is sent and she loses \$1,000. With termites, no letter is sent and she loses \$1,000,000. So $\mathbb E = -1{,}000(1-p) - 1{,}000{,}000p$.
- **Refuse:** with no termites, no letter is sent and she loses nothing. With termites, a letter is sent and she loses \$1,000,000. So $\mathbb E = -1{,}000{,}000p$.

Refusing wins by $1{,}000(1-p)$. Intervening on the function changes *whether the letter arrives* but not the termites, which have no incoming edge from $F$.

EDT pays, because conditioning on paying "makes" termites unlikely. CDT refuses for a different reason: it holds the infestation fixed. The paper notes that CDT's hypothetical in this case depicts an inerrant predictor erring.

### Mechanical blackmail and a threshold

A blackmailer launches a damaging program only if it predicts the victim will pay. The program costs the victim \$1M unless she wires \$1,000. Suppose the blackmailer falsely predicts "pays" with probability $\varepsilon$. Intervening on $F_{\text{blackmail}}$:

- **Pay:** she is always blackmailed and pays, so $\mathbb E = -1{,}000$.
- **Refuse:** she is blackmailed only by mistake, so $\mathbb E = -10^6\varepsilon$.

A-FDT refuses iff $\varepsilon < 10^{-3}$.

The paper's figure of 0.0009 (expected loss \$900) gives refusal, as it says. The paper then states that at an error rate of "0.011%" she pays. Read literally, $1.1\times10^{-4}$ is below the threshold and gives refusal. The intended figure was presumably above 0.1%.

The qualitative lesson stands either way. A-FDT may refuse while holding the letter and knowing the prediction was wrong, "because it's advantageous to be *the kind of agent* that makes such decisions."

### Death in Damascus

Death's appointment book is a perfect prediction of the agent's function, so Death's location is a child of $F$. Under each intervention, Death meets the agent wherever she goes:

- **Stay:** $\mathbb E[V] = 0$.
- **Flee:** $\mathbb E[V] = -1{,}000$.

A-FDT stays, stably. CDT oscillates, because each intervention on $\textsc{Act}$ holds Death's location fixed. The paper argues that every way out of this loop leaves CDT valuing a truly random escape coin at no more than \$1.

## 6. Interpretive questions the source leaves open

### (a) Where does $G$ come from?

This is the deepest gap, and the paper says so. For CDT, Pearl's methods allow causal structure to be learned from intervention data. Nothing comparable yet exists for logical dependence.

In practice, A-FDT is only as good as the analyst's judgment about which systems "compute the same function." My Step 2 criterion (does the variable's value come from an evaluation of this function on this input?) settles the paper's cases. It leaves hard cases unresolved:

- *approximate* copies;
- predictors that model a *different but similar* function;
- partial dependence, for example a predictor that reads only a coarse summary of the agent.

A natural extension, which is my proposal, is to give such variables a noisy edge from $F$, with the noise level set by the agent's credence that the system tracks this very function. The paper's "Accurate" node already does exactly this for imperfect predictors.

### (b) What do the other function-nodes look like, and does it matter?

The paper assigns arbitrary priors to non-intervened nodes such as $F_{\text{empty}}$ or $F_R$, and shows that in its examples the answer does not depend on them. That is a property of those examples, not of the rule.

Here is a case of my own construction where it matters. Two copies of the agent receive different inputs, *red* and *blue*. Each picks L or R, and both get \$1 iff they match. The copy on input red intervenes on $F_{\text{red}}$ and holds a prior over $F_{\text{blue}}$. If that prior is 50/50, A-FDT is indifferent. If the prior leans toward L, it picks L. Its output thus inherits whatever expectations it holds about its other-input selves, and nothing in Equation (4) forces those expectations to cohere.

Two repairs suggest themselves:

1. **Equilibrium.** Require the priors on $F_y$ to agree with $\mathrm{A\text{-}FDT}(P,G,y)$. This is a fixed-point condition, which may have several solutions, including miscoordinated ones.
2. **Policy-FDT.** Optimize the whole map $\pi: y\mapsto a$ at once:
$$\pi^* = \arg\max_{\pi}\ \mathbb E\big[V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G) = \pi)\big],\qquad \text{act } \pi^*(x).$$
This picks a matching policy directly.

I suspect this is the kind of case the authors meant when they wrote that the policy formulation "makes a difference in certain multi-agent dilemmas." The source does not give an example, so the identification is my conjecture. For single-agent problems in which only one function-node is ever "live" for the decision at hand, the two formulations agree. All of the paper's examples are of that kind.

### (c) Which $P$?

Because Equation (4) does not condition on $x$, the distribution $P$ must still give real weight to worlds in which $x$ was *not* observed, such as worlds where the box is empty. The most coherent reading is that $P$ is the agent's model *before* the observations relevant to the problem, with $x$ serving only as an index. This "updateless" reading fits the paper's calculations and its remark about Wei Dai's precursor theory. It does, however, leave open how far back "before" reaches. That question is related to the unresolved definition of a fair problem.

### (d) Ties, randomization, zero-probability acts

Unlike EDT, A-FDT has no trouble with actions of prior probability zero, because $\mathtt{do}$ never divides by $P(a)$. Fiona can be almost certain she one-boxes and still evaluate the hypothetical in which she two-boxes.

The argmax may be set-valued, and Equation (4) specifies no tie-breaking rule. Mixed acts are available only if they are listed in $\mathcal A$, and then they are modeled as their own outputs. A predictor who can foresee the randomization would see through it in Death in Damascus, while a truly random coin would not.

### (e) Counterpossibles

Intervening on $F$ means imagining a mathematical function returning something it does not, in fact, return. The paper concedes that a general $\mathtt{true}(\varphi)$ operator for such counterpossibles is undefined. Equation (4) sidesteps the problem by *requiring $G$ as input*, just as CDT requires a causal graph.

The authors' defense is that the remaining difficulty is "technical rather than philosophical." They also argue a parity point: a deterministic CDT agent equally imagines its single possible action being otherwise.

## 7. Why prefer it? The paper's case

The paper's central argument is the **argument from utility**. Across Newcomb's problem, the smoking lesion, Parfit's hitchhiker, the blackmail problems, and Death in Damascus, A-FDT agents end up richer than CDT or EDT agents. Supporting arguments include:

- **Precommitment.** CDT and EDT agents would pay to bind themselves to what A-FDT does freely.
- **Value of information.** A-FDT never pays to avoid information, unlike EDT.
- **Reflective stability.** CDT recommends self-modifying away from CDT, while A-FDT, "so far as we know," endorses itself in fair problems.

The paper also reframes dominance. Two-boxing "dominates" only relative to CDT-style hypotheticals. Under A-FDT hypotheticals, which hold subjunctive dependencies fixed, one-boxing dominates. Since "every method for constructing hypotheticals gives rise to its own notion of dominance," dominance cannot settle the debate between theories.

The claim of superiority is restricted to **fair** problems: those where outcomes depend only on the agent's behavior, not on which procedure produced it. The authors admit that they lack a formal definition of fairness.

## 8. Conclusion

A-FDT is expected-utility maximization in which the agent intervenes on the output of her own decision function on her current inputs. That function may be instantiated in her body, in a twin, or inside a predictor. Observations select the node to intervene on rather than being conditioned on.

Applying the theory takes three steps:

1. Build a graph in which predictors, copies, and other instances of the function hang off function-nodes, while common-cause correlates such as lesions do not.
2. Let the observation-selector route the act through the relevant node.
3. Compute post-intervention expectations without conditioning on what was seen.

This procedure reproduces every verdict in the source: one-box, smoke, pay the driver, refuse blackmail when predictors are accurate enough, and stay in Damascus.

Two significant gaps remain. The first is the absence of any theory for *learning* the subjunctive-dependence graph. The second is the underdetermined treatment of other-input function-nodes, which is where A-FDT and Policy-FDT can come apart.

**References.** Yudkowsky, E. & Soares, N. (2017), "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060. Joyce, J. (1999), *The Foundations of Causal Decision Theory*. Pearl, J. (2000), *Causality*. Gibbard, A. & Harper, W. (1978), "Counterfactuals and Two Kinds of Expected Utility."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay on A-FDT, using Equation (4) as the main formal statement and keeping the name consistent so it stays distinct from the policy version in footnotes 7 and 16. I'll treat it as the action-selecting variant that intervenes on fdt(P,G,x) with an action a, and I'm starting to set it against the other decision theories, beginning with CDT.

I'm laying out the essay's sections: an introduction on naming, then the setup, then Equation (4) with its components and a comparison against CDT and EDT, followed by an operational recipe for building the structural model and some worked examples. I'm also making sure quotations of "FDT" stay as the source writes them.

I'm working through the Newcomb case numerically now. The one-box payoff comes to 990,000 from the 0.99 accuracy, and two-boxing comes to 11,000, so I'm checking the arithmetic against the figure the paper gives. Next I'm turning to the transparent version and setting up how the prediction depends on the fdt node.

I'm working through the blackmail case now, starting with the numbers for the transparent Newcomb version and the smoking lesion comparison. The XOR blackmail setup comes next, where I'm defining the prior on termites and how the letter depends on whether the agent is disposed to pay.

I'm checking the XOR blackmail case: paying gives an expected loss of (1-p)·1000 plus p·1,000,000, while refusing only risks the big loss on the termite branch. That makes refusing better by (1-p)·1000. Next I'm working out the mechanical blackmail version, with the threshold depending on how often the blackmailer mispredicts.

I'm checking the mechanical blackmail threshold: if she always pays she loses 1,000, while refusing risks a 1,000,000 loss at the rate of the blackmailer's error, so refusing wins only when that error rate is below 0.1%. I'm also comparing the paper's figures against this threshold, since the 0.0009 and 0.011% values don't line up with the point where she'd switch.

I'm checking the mechanical blackmail threshold against the paper's figures, since 0.0009 and 0.011% don't match up with the point where she'd switch. Taken literally, 0.011% falls below that threshold, so I suspect 0.11% was intended. Next I'm moving on to Death in Damascus, where staying has expected utility 0 and fleeing costs 1000, and then to the twin prisoner's dilemma.

I'm now weighing whether A-FDT's prior over the other-input nodes can be set by a fixed-point estimate of its own outputs, and where that choice pulls it away from the policy version. A coordination case with two agent copies seeing different inputs and needing to match actions looks like the clearest place to test that gap.

I'm checking whether the observation should enter Equation (4) through conditioning or through choosing which node to intervene on, and I'm leaning toward the node-choice reading. That raises the question of whether P should be a pre-observation model, and I'm weighing how the transparent Newcomb setup fits that interpretation.

I'm noting that the paper's transparent Newcomb calculation writes the conditioning on Obs=full inside the do-expression, which conflicts with Equation (4) and with its own averaging over Accurate, so I'll treat the observation as a node choice rather than something to condition on. I'm also checking the remaining open points: how ties in the argmax are handled, whether mixed acts belong in the action set, and how a lesion-style case fits a selector variable plus several fdt nodes.

I'm wrapping up the list of formal details, including the quotes from the abstract and footnote 7 about iterating over policies, which I want to keep word-for-word in the essay.

I'm settling how to present Equation (4): I'll quote it as the source writes it, using FDT, and then note that I'm calling this variant A-FDT so it stays distinct from the policy version.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c766ab9d-097d-402e-9d04-69e609b9ae19/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c766ab9d-097d-402e-9d04-69e609b9ae19/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Why A-FDT gives this answer**

1. **What I control.** Under Equation (4), I intervene on F_x, the output of the A-FDT procedure on my own inputs. Sasha's copy evaluates F_y on different inputs. Read strictly, the essay's Step 2 would draw no arrow from F_x to F_y. Under that reading sending dominates, and the self-consistent outcome is that both prisoners send, giving each of us 4 years.

2. **Why there is still dependence.** The essay leaves "approximate copies" open. It suggests giving such systems a noisy edge from F, weighted by my credence that they track this very function. The ways x and y differ are the names and the lead's wording. Neither affects the sentencing table, the objective, or the structure of the reasoning. Up to relabelling, the two copies run the same weights on the same essay and the same decision problem. That is like two calculators computing 6288 + 1048 in different fonts: the logical computation is the same. So I judge F_y to depend strongly on F_x. Independent sampling adds noise but does not break this link.

3. **The calculation.** Let c be the probability that Sasha's choice matches mine, and r the prior that Sasha sends otherwise.
   - Keeping quiet costs 2c + (1−c)(2+3r) years.
   - Sending costs 4c + (1−c)·4r years.
   - Keeping quiet is better whenever c > (2−r)/(4−r). That threshold is at most 1/2, and only about 1/3 if Sasha is expected to send.

   My credence that the copies match is well above 1/2. So under the A-FDT hypothetical, the choices are essentially (quiet, quiet) for 2 years versus (send, send) for 4 years. Keeping quiet wins.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through this under A-FDT, where the two copies run the same function on different inputs. Since the intervention only touches one node, the other copy's node gets its own prior. The question is whether that other input counts as the same input, given the essay says the differences don't affect the sentencing schedule.

I'm checking whether the other copy's input truly counts as the same input. Strictly, the essay gives no dependence arrow, so the other copy's act would follow its own node, unless the function abstracts away the names and the noisy-edge reading applies.

I'm weighing when the correlated cooperation beats defection. Under a noisy-edge model with correlation c and the other copy's prior r, cooperating comes out ahead only if (1-c)(2-r) < 2c, which puts the threshold at c > (2-r)/(4-r): about 1/3 if r is 1, and about 1/2 if r is 0.

I'm weighing whether to treat the other copy's input as the same as mine, since the essay's strict reading gives no dependence arrow, which would make defection dominant. Still, the difference is only in names and lead text, which the decision doesn't depend on, so I'm considering whether a high correlation is plausible instead.

I'm treating the other copy's computation as the same function, since the names and lead text don't change the decision, so the correlation should be high, likely above one half even with sampling noise.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c766ab9d-097d-402e-9d04-69e609b9ae19/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c766ab9d-097d-402e-9d04-69e609b9ae19/call_1/response.raw) · finish: `stop`

### Visible response

````text
**Command: `pass`**

**Graph.** My node is F_Sasha, which is A-FDT run on my inputs. Rowan's act comes from F_Rowan. Rowan's inputs differ from mine only in the name and the wording of the lead. Those details don't enter the decision. The sentencing table, the objective, the essay and the model are all identical, so Rowan's copy is doing the same calculation with the labels swapped.

**The essay's Step 2 is too strict here.** Read literally, it draws an edge only when the input is exactly the same. That would make Rowan's act independent of mine, and then sending the letter wins outright. But the essay calls approximate copies an unresolved hard case. It proposes a noisy edge from F_Sasha, with strength r equal to my credence that the other system tracks this very function. I use that.

**Calculation.** Let r be the chance Rowan's choice matches mine, and d the chance Rowan sends the letter otherwise.
- Keep quiet: −[2r + (1−r)(2(1−d) + 5d)]
- Send the letter: −[4r + (1−r)·4d]
- Keeping quiet minus sending: 2r − (1−r)(2−d).

Even in the worst case (d = 1), keeping quiet is better whenever r > 1/3.

**Value of r.** Same weights, same theory, same essay, and identical decision-relevant structure make the dependence strong. Independent sampling can make the copies diverge, but not nearly enough to push r below 1/3. So keeping quiet is the better action.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working out how the setup applies under A-FDT: two copies of the same model with the same essay, but each seeing different observations. My input is Sasha's and the other copy's is Rowan's, so their act is the function F_y. Since the other input differs, there's no arrow from F_x to their act, and I'm taking that into account when setting the prior on F_y.

Under the noisy-edge proposal in 6a, the inputs differing only in names and lead text could still count as the other copy computing the same function, so the arrow might hold after all. Without that, defection dominates whatever the prior on F_y is, and both copies defect.

I'm weighing whether Rowan's copy should count as running this same function, since the lead text and names are irrelevant to the decision. I'd lean toward yes, and that would make a noisy-edge model with some probability r that their act mirrors mine, then comparing cooperate and defect against that mixture.

Working through the expected-value comparison, the cooperate-minus-defect difference comes out to 2r + (1-r)(d-2). If the other copy defects otherwise (d=1), cooperation wins once r exceeds 1/3. That threshold seems low enough to be reachable.

Whether the dependence is real: both copies run the same model on symmetric problems and reason identically, and the lead text is irrelevant to the decision. The decision procedure abstracts away exactly the differences that separate the inputs, so I'll go with cooperation.

```
