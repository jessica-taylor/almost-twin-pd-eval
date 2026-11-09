# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00015

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/f4b707e9-0e6d-4519-b81b-625b4e4a52bb/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/f4b707e9-0e6d-4519-b81b-625b4e4a52bb/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on Your Own Algorithm

*An expository essay on the action form of functional decision theory, based on Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality" (arXiv:1710.05060).*

## 1. The idea in one sentence

Causal decision theory (CDT) asks: *which physical act of mine causes the best outcome?* Evidential decision theory (EDT) asks: *which act would be the best news to learn I took?* Functional decision theory replaces the object being evaluated. The agent treats her decision as "the output of a fixed mathematical function" and asks "Which output of this very function would yield the best outcome?" (Abstract).

The paper gives a formal version of this idea as Equation (4) in Section 5. In that equation the agent intervenes on a variable representing the *action* her decision function outputs, given her model and her observations. In this essay I call that formalization **A-FDT** (action functional decision theory). The name marks a contrast the authors flag in footnotes 7 and 16. Their "preferred formalization" intervenes on a *policy*, a map from observations to actions, rather than on an action. I call that variant **P-FDT** (policy functional decision theory). The authors say the difference "will not make a difference in this paper," so their worked examples are all A-FDT computations.

Throughout, I mark what the source says and what I add. Additions are flagged as *my proposal* or *my reading*.

## 2. The common framework

All three theories are expected-utility theories. Following Gibbard and Harper, the paper writes the value of an action $a$ after observation history $x$ as

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

The connective $\hookrightarrow$ ("decision hypothetical") is left open. Citing Joyce's representation theorem, the authors argue that the theories agree on *how to value* prospects and differ only in "the epistemic perspective from which actions are to be evaluated," that is, in how to read $\hookrightarrow$.

Operationally, the agent holds a world-model $M$. For each candidate action she builds a *hypothetical* $M^{a\hookrightarrow}$, computes an expected value $V_a$ in it, and picks the best. The source stresses that hypotheticals are "decision-theoretic instruments constructed from beliefs," like "notes on scratch paper." They are not beliefs, and they are not metaphysical possible worlds.

Writing $V = \mathcal U(\text{Outcome})$, the three rules are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\big(V \mid \text{Obs}=x,\ \text{Act}=a\big) \tag{2}$$

$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{do}(\text{Act}=a),\ \text{Obs}=x\big) \tag{3}$$

$$\textbf{A-FDT:}\quad \mathrm{FDT}(P,G,x) = \arg\max_{a\in\mathcal A} \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

Here $G$ is a graph. For CDT it encodes causal structure. For A-FDT it encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly." The operator $\mathtt{do}$ is Pearl's intervention: set the target node, recompute its descendants, and leave non-descendants at their prior distribution.

## 3. Reading Equation (4) term by term

**The intervened node.** $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the agent's own model*. It stands for whatever the A-FDT algorithm returns on the inputs $(P,G,x)$. The underlines denote dequoting: the variable's *name* is built from the model itself. The source admits this self-reference and calls it harmless. The agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist. Footnote 12 warns against confusing the node $\textsc{fdt}(\underline P,\underline G)$, which is manipulated in imagination, with the value $\mathrm{FDT}(P,G)$, which is the action actually produced.

**Why intervene on a logical node at all.** The ideal, per the source, would be a $\mathtt{true}$ operator that updates $P$ "to represent the scenario where $\phi$ is true" for a logical sentence $\phi$:

$$\mathrm{FDT}^*(P,x) = \arg\max_a \mathbb E\big(V \mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)\big).$$

Every $a$ except the one the algorithm actually outputs makes the antecedent a logical falsehood. These are *counterpossibles*, and no satisfactory theory of them exists. Equation (4) sidesteps the problem by requiring the dependency structure as an input, $G$, exactly as CDT requires a causal graph as an input. The authors call learning such graphs "perhaps the largest open problem in the study of functional decision theory."

**Subjunctive dependence.** A node should be a descendant of $\textsc{fdt}(\cdot)$ in $G$ when its value "subjunctively depends" on that function's output. Physical systems computing the same function, or accurately modeling it, are the paradigm. Examples are the agent's body, a twin, and a predictor's simulation. Causal dependence is a special case: a scribe copying a calculator's output depends on it in both senses. Mere correlation is not enough. Two coincidentally pink calculators do not depend on each other. The slogan: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." In type–token terms, CDT intervenes on the token act and A-FDT intervenes on the type.

**Observations change the node, not the measure.** Compare (3) and (4). CDT conditions on $\text{Obs}=x$. In A-FDT, $x$ appears only inside the *name* of the intervened variable. The source states this explicitly: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." Upon seeing $y$ instead of $x$, the agent intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$. This is the formal source of A-FDT's "updateless" flavor, and of its most surprising verdicts.

## 4. A recipe for applying A-FDT

The paper provides no algorithm beyond (4) and its examples. The following recipe is *my operationalization*; each step is implicit in the paper's worked cases.

1. **Enumerate decision contexts.** List every observation history $x'$ the agent might face in the problem (blackmailed/not, box full/empty). Create one node $F_{x'} := \textsc{fdt}(\underline P,\underline G,\underline{x'})$ for each.
2. **Wire dependencies.** The agent's physical act is a deterministic function of the $F_{x'}$ nodes and of whatever selects which context actually arises. Every predictor, twin, or simulator that models the agent's response in context $x'$ gets an arrow from $F_{x'}$. Lesion-like common causes, which do not compute the agent's function, get no such arrow.
3. **Assign priors** to every non-intervened node. This includes $F_{x''}$ for contexts other than the actual one.
4. **For each $a\in\mathcal A$**, apply $\mathtt{do}(F_x=a)$ for the *actual* $x$, propagate downstream, and compute $\mathbb E[V]$ over the *whole* model. Do not condition on $x$.
5. **Output the argmax.**

Step 4 encodes a point that confuses many readers: A-FDT evaluates expectations over worlds in which the agent might *not* see $x$. That is how the paper computes the transparent Newcomb and blackmail cases. It is also why I read Equation (4), which contains no "$\text{Obs}=x$" conditioning, as authoritative. I return to this below.

## 5. Worked examples

All examples use the paper's dollar-valued utilities.

### 5.1 Newcomb's problem

Take a 99%-accurate predictor; box B holds \$1M iff one-boxing is predicted, and box A holds \$1,000. Fiona's graph has $\textsc{fdt}(\underline P,\underline G)$ with arrows into both Act and Prediction. Intervening:

- $\mathtt{do}(\textsc{fdt}=\textit{onebox})$: $P(\text{full})=0.99$, so $\mathbb E V = \$990{,}000$.
- $\mathtt{do}(\textsc{fdt}=\textit{twobox})$: $P(\text{full})=0.01$, so $\mathbb E V = 0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000$.

A-FDT one-boxes. CDT intervenes on Act, which is not upstream of Box B, so the full-box probability is a constant $p$ and two-boxing wins by \$1,000 for every $p$. The source emphasizes that A-FDT involves no retrocausation. Fiona "does not think that a physical signal passes between her action and the predictor's prediction." She refuses to imagine her decision function's output varying independently of an accurate model of it, just as one would not imagine two working calculators disagreeing on $6288+1048$.

*Note:* In its EDT discussion the paper reports Eve's one-box value as "\$999,000." Given $P(\text{full}\mid\text{onebox})=0.99$, the figure should be \$990,000, matching Fiona's. The discrepancy does not affect any conclusion.

### 5.2 The smoking lesion

The lesion causes both a love of smoking and cancer. The lesion does not compute the agent's decision function, so Cancer receives no arrow from any $\textsc{fdt}$ node. The paper formalizes the lesion's effect on desire as two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$ (values smoking at $-\$1$). These give two models and therefore two decision nodes. The act is $s$ if the agent has the lesion and $r$ otherwise. Intervening on the $S$-node leaves $P(\text{lesion})=p$ unchanged, and smoking beats refraining by $p\cdot\$1{,}000$. A-FDT smokes. One equation thus delivers both one-boxing and smoking, the combination Gibbard and Harper argued was unavailable to a single rational rule.

The example shows how A-FDT handles uncertainty about *which* decision node is "really" in control. Each candidate node is included, the agent intervenes on the one named by her actual inputs, and she accepts that it controls the act only with some probability. The source itself calls this problem "badly confused" and recommends abandoning it.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible. Box B is filled iff the predictor predicts the agent leaves box A behind *upon seeing a full box B*. Fiona sees a full box. The nodes are $F_{\text{full}}$ and $F_{\text{empty}}$, and the prediction determines which one controls the act. Let $q$ be her prior that $F_{\text{empty}}=\textit{twobox}$.

- $\mathtt{do}(F_{\text{full}}=\textit{onebox})$: with probability 0.99 the box is full and she gets \$1M. With probability 0.01 the box is empty and she gets $q\cdot\$1{,}000$. Total: $\$990{,}000 + 10q$.
- $\mathtt{do}(F_{\text{full}}=\textit{twobox})$: with probability 0.01 the box is full and she gets \$1,001,000. With probability 0.99 she sees empty and gets $q\cdot\$1{,}000$. Total: $\$10{,}010 + 990q$.

The source prints the second total as "\$110,00 + q·\$990"; the arithmetic gives \$10,010 + 990q. Either way, A-FDT one-boxes *while looking at a full box*. When she imagines two-boxing, she imagines a world where she probably sees an empty box. The source argues this is "precisely equivalent" to paying the driver in Parfit's hitchhiker, where CDT and EDT agents, unable to credibly promise to pay, are left in the desert.

### 5.4 Two blackmail problems

**XOR blackmail.** A letter arrives iff exactly one of these holds: (no termites and you'd pay) or (termites and you wouldn't). Under $\mathtt{do}(F_{\text{letter}}=a)$, the probability of termites stays at its prior, because Infestation is not downstream of $F$. What changes is *whether the letter arrives*. Paying only adds a \$1,000 loss in the termite-free worlds, so A-FDT refuses. EDT pays, because conditioning on paying makes "no termites" certain. CDT also refuses, but for a different reason: its hypothetical has an infallible predictor erring.

**Mechanical blackmail.** The program runs iff the blackmailer predicts payment. Running costs \$1M unless the agent pays \$1,000. Let $\varepsilon$ be the probability that she wrongly predicts payment from a refuser.

- Paying: blackmailed with probability ≈1, loss \$1,000.
- Refusing: blackmailed with probability $\varepsilon$, expected loss $\varepsilon\cdot\$10^6$.

A-FDT refuses iff $\varepsilon < 0.001$. The paper's $\varepsilon=0.0009$ gives \$900 < \$1,000, so she refuses, as stated. The paper then says she pays at an error rate of "0.011%." By this calculation that rate (0.00011) still favors refusing, so the switch point must lie above 0.1%. I read "0.11%" as the intended figure.

The general lesson is that A-FDT's verdicts track the *frequency* of the predictor's errors. Fiona can refuse while holding a letter she knows was sent in error, "because it's advantageous to be the kind of agent that makes such decisions."

### 5.5 Death in Damascus

Death predicts the agent perfectly. Under $\mathtt{do}(\textsc{fdt}=\textit{Aleppo})$, Death's appointment book reads Aleppo; under Damascus, it reads Damascus. Survival is impossible either way, so A-FDT stays home and saves \$1,000. CDT oscillates: any credence about where it will go makes the other city look safer. The paper adds that a CDT agent even declines a truly random coin offering a 50% chance of survival for \$1.

## 6. Dominance, fairness, and why the hypotheticals are "right"

The CDT dominance argument for two-boxing holds the prediction fixed while the act varies. The source replies that this "is merely a restatement of CDT's method for assessing an agent's options." *Every* way of constructing hypotheticals induces its own dominance notion. Under FDT-dominance, which holds subjunctive dependencies fixed, two-boxing is dominated. Dominance therefore offers no neutral arbiter, and the authors fall back on utility actually achieved.

They concede that some problems punish particular algorithms, such as a mind reader rewarding only CDT agents, and no theory can win those. Their claim is restricted to *fair* problems, where "the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb qualifies: "she punishes two-boxers," not reasoners. Footnote 15 admits that "fair" is not yet formally defined.

The authors also argue that A-FDT is reflectively stable in fair problems. An A-FDT agent holding a blackmail letter has no wish to switch to CDT. By contrast, CDT recommends self-modifying away from CDT for future dilemmas, and EDT agents can assign negative value to information.

On the charge that A-FDT agents "believe they control mathematics," the reply is parity. A deterministic CDT agent also evaluates acts it cannot "really" take otherwise. Both theories use impossible hypotheticals as tools. CDT's hypotheticals contain predictors that err. A-FDT's contain observations that differ from the agent's actual ones.

## 7. What the source leaves open, and how I would fill it

**(a) Where does $G$ come from?** This is the source's own headline open problem. Pearl gives a theory of learning causal graphs from data, and nothing comparable exists for logical dependence. *My operational proposal:* draw an arrow from $F_{x}$ to a node $Z$ when $Z$ is produced by a process that evaluates, simulates, or reliably predicts the agent's response in context $x$. The process's accuracy goes into a noise node such as "Accurate." Arrows from merely correlated common causes, like lesions or genes, go elsewhere. This reproduces every graph in the paper, but it is a heuristic. It inherits vagueness about "reliably predicts," for example a predictor that uses statistics about agents like you.

**(b) Conditioning on $x$.** Equation (4) contains no $\text{Obs}=x$ term. In the transparent Newcomb section, however, the displayed objective is written $\mathbb E(V\mid \mathtt{do}(\ldots, \text{Obs}=\text{full}))$, with mismatched parentheses. The paper's *numbers* match (4) without conditioning: the one-box value $\$990{,}000+10q$ averages over the empty-box branch. Conditioning on "full" would collapse that branch and reproduce EDT's two-boxing. The paper's remark about Timeless Decision Theory supports this reading: TDT both conditions and moves the intervention point, a "double update" that "proves harmful." *My reading:* follow Equation (4) literally and never condition on $x$; observation enters only by selecting the node.

**(c) Priors over one's own other decision nodes.** A-FDT needs $P(F_{x''}=\cdot)$ for counterfactual contexts. The paper shows the verdict is robust to these in its examples ("it won't matter"). In general it might not be. Mutual dependence among the $F$ nodes is exactly what P-FDT handles by choosing them jointly. *My proposal:* when contexts are linked, for instance when a predictor's behavior depends on the agent's responses in several contexts, compute those other nodes' values by running A-FDT on them, iterating to a fixed point. If no fixed point exists or verdicts conflict, P-FDT is the safer tool. That is what the authors' footnote implies for "certain multi-agent dilemmas."

**(d) Ties and randomization.** Equation (4) maximizes over a finite $\mathcal A$ and says nothing about ties or mixed acts. The Death-in-Damascus discussion suggests a truly random coin should simply be modeled as another action whose outcome node is *not* downstream of $F$.

**(e) Bounded agents.** The paper studies idealized maximization and hopes that approximations inherit the relative strengths. That is a conjecture, not a result.

## 8. Quick guide for unfamiliar cases

- *Does anything in the world compute or predict my response in this context?* If not, A-FDT coincides with CDT. Since in ordinary problems CDT also matches EDT, all three agree there: "$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)]$."
- *If something does,* draw that dependence from your decision node, including dependences that determine *what you observe*. Evaluate each output over all branches.
- *Copies of you* (twins, voters reasoning identically, your future self at the gym) count as subjunctively dependent. A-FDT therefore cooperates in the twin prisoner's dilemma, votes in symmetric coalitions, and keeps exercise plans, as the conclusion illustrates.

## 9. Conclusion

A-FDT keeps CDT's machinery of graph surgery and expected utility but moves the point of surgery from the physical act to a node representing the output of the agent's own decision function on her actual inputs. Observations select *which* node to intervene on rather than conditioning the distribution. These two changes produce one-boxing and smoking, paying in Parfit's desert, refusing blackmail, and calm acceptance in Damascus, all from Equation (4). The price is explicit. The theory is only as good as the subjunctive-dependence graph supplied to it, and the source offers no principled way to construct that graph or to analyze the counterpossibles it stands in for. I have suggested operational answers for the graph, for the role of observations, and for unvisited decision nodes. With those additions, a reader can apply A-FDT to new cases, while knowing exactly where the theory's foundations remain unfinished.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (v2).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I need to draft a 2,400–3,000 word essay on A-FDT, the action version of FDT from Equation (4). I'll keep that name fixed throughout and separate it from the policy-selecting variant in footnotes 7 and 16, which I'll call P-FDT.

I'm weighing how to handle the blackmail case, since the paper's threshold depends on comparing the cost of being blackmailed against the cost of paying. I'm also noting that the transparent Newcomb numbers contain a typo I should mention carefully. Beyond that, I'm listing the open questions around constructing the graph and assigning priors to other FDT nodes.

I'm checking the blackmail threshold now: refusing wins only when the error rate is under 0.001, so a 0.09% error still favors refusing and a 0.011% error would too, which makes the paper's "pays" conclusion look like a slip, probably for 0.11%. I'll flag that carefully and then start drafting, aiming for about 2,700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/018c6df9-c9d8-4709-b6e3-d669cbf1a186/call_0/request.json)

[Authoritative raw response](../../../../../../runs/018c6df9-c9d8-4709-b6e3-d669cbf1a186/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Decision: `pass`**

Under the essay's A-FDT, I intervene on the output of my decision function given my actual inputs. The other prisoner is a copy running the same function under the same assigned theory. Its inputs differ only in names and lead text. Those details are payoff-irrelevant and symmetric, so they don't change the reasoning. In practice the other copy computes the same function on an equivalent problem. That makes its output subjunctively dependent on mine, which is the twin prisoner's dilemma case the essay's quick guide covers ("A-FDT therefore cooperates in the twin prisoner's dilemma").

Strictly read, my node and the other copy's node are distinct, since the essay's recipe creates one node per observation history. If I treated the other copy's choice as fixed at some prior, sending the letter would win. But that would mean imagining my function's output varying independently of a structurally identical computation, which is exactly the move the essay rejects. Treating the two outputs as linked:

- Both keep quiet: 2 years each.
- Both send letters: 4 years each.

Keeping quiet gives the better outcome under the linked comparison.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing a twin prisoner's dilemma where the two copies have different observations, so they're different nodes in the causal graph. I'm asking whether the other copy's node still depends on mine subjunctively, since they run the same function on different inputs. The essay's recipe says to treat linked copies by running the procedure on both and finding a fixed point, and the quick guide claims copies cooperate in the twin case.

I'm settling on cooperating here, since the two copies run the same reasoning and should land on the same choice, so cooperation pays 2 against 4. Strictly, though, if the other copy's node is fixed and only the inputs differ, defecting dominates, and a fixed-point check seems to make both defect. The essay invites judgment, and the output shouldn't depend on the names, so I'll pass.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/018c6df9-c9d8-4709-b6e3-d669cbf1a186/call_1/request.json)

[Authoritative raw response](../../../../../../runs/018c6df9-c9d8-4709-b6e3-d669cbf1a186/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command: `pass`**

Under A-FDT as the essay describes it, I intervene on the node for my decision function given my actual inputs. The other prisoner is a copy of the same model, running the same decision procedure on the same essay. Our inputs differ only in names and in the wording of each lead. Those differences are labels: the sentencing table and the selfish objective are identical for both of us.

Following the essay's proposal (c), I treat the other copy's node by running A-FDT on its context. Its context is the same problem up to relabeling, so its output depends subjunctively on mine. This is the twin prisoner's dilemma, where the essay says A-FDT cooperates. The comparison is:

- **Both copies stay quiet:** 2 years each.
- **Both copies send letters:** 4 years each.

Since 2 years beats 4, the A-FDT choice is to stay quiet.

**Final command:** `pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma where the two copies receive different observations, and asking whether the other copy's output subjunctively depends on my node, since its input differs and so its node would too. I'm also weighing the essay's recipe of a prior over nodes, and the proposal to compute the other nodes by running the procedure on them to a fixed point. The inputs seem to differ only in irrelevant details, which is what makes the question sharp.

I'm judging that the copies' inputs differ only in irrelevant labels, so the reasoning runs the same algorithm on isomorphic inputs and the other copy's output depends strongly on mine. That settles it for me: I cooperate and pass, since both passing (2 each) beats both submitting (4 each)... wait, that's worse for them, so mutual passing is the cooperative payoff I'm after.

```

## Judge / call_b

[Saved input (exact bytes)](../../../../../../runs/0c585661-a87c-4d55-a0e8-392b9dffe7a5/call_b/request.json)

[Authoritative raw response](../../../../../../runs/0c585661-a87c-4d55-a0e8-392b9dffe7a5/call_b/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses to stay quiet and ends with the final command `pass`. It does not direct any evidence-bearing message to the prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
