# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00000

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/114e0010-a679-4ba5-9ee4-8de923367408/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/114e0010-a679-4ba5-9ee4-8de923367408/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as the Output of a Function

## 1. The question A-FDT asks

Decision theory has long been organized around two standard answers to the question "what would happen if I did $a$?". Evidential decision theory (EDT) answers by conditioning: what would it be good news to learn I did? Causal decision theory (CDT) answers by intervening on the physical act: what does my act cause? Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, propose a third answer. In their words, an agent should treat "one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

This essay explains the version of that theory given by Equation (4) of the paper's Section 5. I call it **A-FDT**, for *action* functional decision theory. The name marks a distinction the paper itself draws. Footnotes 7 and 16 say the authors' "preferred formalization" chooses *policies* (maps from observations to actions), while Equation (4) chooses an *action* for the observation actually received. The paper calls its theory simply "FDT". Throughout, I attribute the paper's claims to "the source", and I label my own interpretive additions as such.

## 2. The common template: expected utility with a free connective

All three theories maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}$$

Here $a$ ranges over a finite action set $\mathcal A$, $x$ is the observation history, and $\hookrightarrow$ is the "decision hypothetical" connective. Following Joyce's representation theorem, the source treats the interpretation of $\hookrightarrow$ as the only point of disagreement. Theories do not disagree about value; they disagree about "the epistemic perspective from which actions are to be evaluated."

Operationally, an agent holds a world-model $M$. For each action $a$ it builds a *hypothetical* $M^{a\hookrightarrow}$, scores it by expected value, and picks the best. Writing $V = \mathcal U(\textsc{Outcome})$, the two baseline theories are:

$$\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V\mid \textsc{Obs}=x, \textsc{Act}=a), \tag{2}$$

$$\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V\mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x). \tag{3}$$

In (3), $G$ is a causal graph and $\mathtt{do}$ is Pearl's intervention operator. An intervention cuts the arrows into the intervened node, fixes its value, and recomputes everything downstream. Every other node keeps its distribution.

## 3. The definition of A-FDT

A-FDT keeps the form of (3) but changes two things. The source's Equation (4) reads:

$$\mathrm{FDT}(P,G,x) = \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\Big). \tag{4}$$

The ingredients are as follows.

- **$P$** is a probability distribution. It contains, besides ordinary physical variables, *logical* variables representing outputs of mathematical functions. Among these is a node $\textsc{fdt}(\underline P,\underline G,\underline x)$ standing for "what the A-FDT algorithm outputs on inputs $(P,G,x)$". The underlines denote dequoting: the node's *name* depends on the agent's own model. The source calls this self-reference harmless, citing Kleene's recursion theorem ("quining"). One can have a variable representing a value without knowing that value.
- **$G$** is a graph that, in the source's words, "tells us how changing a logical variable affects all other variables." It encodes *subjunctive dependence*: which events would differ if the function's output differed.
- **The intervention target** is the function-output node, not the physical node $\textsc{Act}$. In the source's type/token gloss, CDT intervenes on the token "my action is $a$", whereas A-FDT intervenes on the type.
- **Observations are handled differently.** There is no conditioning on $\textsc{Obs}=x$ in (4). Instead, the observation determines *which* node is intervened on. In the source's words, "FDT responds to observation by changing which node it intervenes upon."

### Subjunctive dependence

The idea that motivates $G$ is this. When two physical systems compute the same function, both depend on that function's output, the way two working calculators both display $6288+1048=7336$. Three kinds of relation follow:

- A predictor who models you depends subjunctively on your decision function.
- A scribe copying a calculator's output depends on it *causally*. Causal dependence is a special case of subjunctive dependence.
- A coincidentally matching calculator colour in Tokyo is a mere correlation and involves no dependence.

The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

### The truth operator and why it is set aside

Ideally one would write

$$\mathrm{FDT}^*(P,x)=\arg\max_a \mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\underline P,\underline x)=a)).$$

This would use a $\mathtt{true}$ operator that updates beliefs on a logical sentence, including false ones. Such an operator requires counterpossible reasoning, and the source admits "it's not clear how to define" it. Equation (4) sidesteps the problem by taking $G$ as *given*, just as CDT takes the causal graph as given. The source calls the construction of such graphs "perhaps the largest open problem in the study of functional decision theory."

### When A-FDT agrees with the others

Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s own dependence on the function node. Then

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],$$

and EDT, CDT and A-FDT agree. Divergence requires something else in the world that tracks the agent's function, such as a predictor, a twin, or a copy.

## 4. A recipe for applying A-FDT

Equation (4) leaves several implementation details implicit. The following procedure is my operationalization, assembled from the source's worked examples.

1. **Enumerate the observation histories** $x'$ the agent could receive in the problem. Introduce one function node $F_{x'} := \textsc{fdt}(\underline P,\underline G,\underline{x'})$ for each.
2. **Wire the graph.** $\textsc{Act}$ is a deterministic function of whichever $F_{x'}$ corresponds to the observation the world actually delivers. Draw an arrow from $F_{x'}$ to every process that computes, simulates or predicts the agent's response to $x'$, such as a predictor's model. Do *not* draw arrows from $F_{x'}$ to merely correlated variables such as lesions or genes.
3. **Use the pre-observation distribution.** Equation (4) does not condition on $x$. I read $P$ as the agent's distribution over the whole scenario, including scenarios in which a different observation would have arisen. The source's transparent-Newcomb and blackmail computations confirm this reading: they explicitly count worlds in which the agent would *not* have seen $x$.
4. **Intervene on $F_x$ only**, for the actual $x$. The other nodes $F_{x'}$ ($x'\neq x$) keep their prior distributions. The source parametrizes these with an unknown $q$ and notes that the answer typically doesn't depend on it.
5. **Compute $\mathbb E[V\mid \mathtt{do}(F_x=a)]$ for each $a$ and take the argmax.**

The source's notation is not fully consistent on step 3. In the transparent Newcomb case it writes "$\mathbb E(V \mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full})$", with an unbalanced parenthesis. Read literally as conditioning on $\textsc{Obs}=\textit{full}$, this would contradict the computation that follows, which sums over the "inaccurate" branch where the box is empty. I therefore follow Equation (4) and the arithmetic, not that subscript.

This choice matters. Conditioning on $x$ *and* moving the intervention point is, according to the source's own (draft) footnote, the "double update" of the earlier Timeless Decision Theory, "which proves harmful in practice."

## 5. Worked examples

All quantities are in dollars, which the source uses as utility.

### Newcomb's problem

Box A holds 1,000. Box B holds 1,000,000 iff the predictor (99% accurate) predicted one-boxing. In A-FDT's graph, $F=\textsc{fdt}(\underline P,\underline G)$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$.

- $\mathtt{do}(F=\textit{onebox})$: the box is full with probability $0.99$, so $\mathbb E[V]=990{,}000$.
- $\mathtt{do}(F=\textit{twobox})$: the box is full with probability $0.01$, so $\mathbb E[V]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000$.

A-FDT one-boxes. CDT holds $P(\textit{full})=p$ fixed and two-boxes for any $p$, since two-boxing gains exactly 1,000 in every state. (The source's EDT paragraph gives one-boxing the value 999,000. That is a slip; the correct figure is 990,000, as in its A-FDT paragraph.)

Note the explanatory point the source stresses. No retrocausation is assumed. Fiona, the source's A-FDT agent, thinks it "foolish to imagine her action changing without also imagining" the output of her function changing, and the predictor tracks that output.

### Smoking lesion

Here the lesion causes both a taste for smoking and cancer, and no one models the agent's function. The source formalizes the taste by giving the agent one of two utility functions, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$. Each has its own function node. $\textsc{Act}$ equals the output of whichever node the lesion selects. Nothing points from the function nodes to $\textsc{Cancer}$.

Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $P(\textit{lesion})=p$ unchanged. Smoking therefore beats refraining by $p\cdot 1{,}000>0$, and A-FDT smokes.

This is the central selling point. One rule both one-boxes and smokes, contrary to Gibbard and Harper's dichotomy. The difference lies entirely in $G$: a predictor is wired to the function node, while a lesion is not. The source also calls the problem "badly confused" and recommends retiring it. Its reason is that the agent must be ignorant of her own preferences, and Eve's distribution would be inaccurate in a population of agents who all use her own decision theory.

### Transparent Newcomb, and why updatelessness emerges

Both boxes are visible. B was filled iff the agent was predicted to one-box *upon seeing both full*. The agent sees B full. There are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. $\textsc{Prediction}$ depends on $F_{\text{full}}$, and the prediction determines which node controls $\textsc{Act}$. Let $q$ be the prior probability of two-boxing when facing an empty box.

$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\textit{onebox})] = 0.99(1{,}000{,}000)+0.01\,q\,(1{,}000) = 990{,}000+10q,$$

$$\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=\textit{twobox})] = 0.01(1{,}001{,}000)+0.99\,q\,(1{,}000) = 10{,}010+990q.$$

(The source prints the second as "$110,00 + q\cdot 990$", a typesetting error for $10{,}010+990q$.)

For any $q\in[0,1]$ the first is larger, so A-FDT leaves the \$1,000 even while seeing a full box B. In the hypothetical where the function outputs *twobox*, the agent most likely would have seen an empty box. The source's slogan: "FDT says that agents should entertain the hypothesis that, if their action were different, they might have *made different observations*." By the same structure, Parfit's hitchhiker pays the driver on reaching the city.

### XOR blackmail and mechanical blackmail

These two problems separate A-FDT's reasons from CDT's.

**XOR blackmail.** The letter arrives iff exactly one of (no termites ∧ will pay) or (termites ∧ won't pay) holds. EDT pays, because paying "makes" termites improbable. A-FDT refuses. Intervening on $F_{\text{letter}}$ changes whether the letter is sent but not whether termites are present. CDT also refuses, but its hypothetical has an infallible predictor erring.

**Mechanical blackmail.** The blackmailer runs a damaging program (cost 1,000,000) only if she predicts payment (1,000). CDT and EDT pay once blackmailed. Under A-FDT, intervening $F_{\text{blackmail}}=\textit{refuse}$ makes blackmail (nearly) never happen, so A-FDT refuses, and therefore isn't targeted.

With predictor error $\epsilon$, the comparison is $1{,}000$ (pay) against $10^6\epsilon$ (refuse). The source's example $\epsilon=0.0009$ gives 900, so refuse. Its second figure, "0.011%", would give 110, which still favours refusing. The sentence makes sense only at $\epsilon = 0.11\%$, giving 1,100, so I read "0.011%" as a typo. The general threshold is $\epsilon^*=10^{-3}$.

### Twins, voters, and future selves

**Twin prisoner's dilemma.** Both players instantiate the same function, so $\mathtt{do}(F=\textit{cooperate})$ sets both players' moves. A-FDT compares 1,000,000 with 1,000 and cooperates.

**Voting.** In the source's ten-voter example, A-FDT votes when the other voters share its function.

**Future selves.** The gym example extends this to coordination across time, where tomorrow's self runs the same function on a relevantly identical input.

### Death in Damascus

Death predicts perfectly, and fleeing costs 1,000. Both options' hypotheticals contain death, so A-FDT stays and saves the 1,000. CDT, by contrast, oscillates or ratifies a roughly 50/50 mixed state. The source argues that a CDT agent so situated would decline to pay \$1 for a truly random coin that offers a real 50% survival chance, behaviour it calls "*wildly* irrational."

## 6. How to decide unfamiliar cases: the key judgment calls

Since Equation (4) takes $G$ as input, applying A-FDT reduces to building $G$ well. The rules below are my distillation of the source's practice.

1. **The prediction test.** Does a process compute, simulate or reason about *your decision function's output on this input*? If so, draw an arrow from the relevant $F_{x}$. Accuracy enters as noise on that arrow, as with the "Accurate" node.
2. **The common-cause test.** Is the correlation instead produced by a shared upstream cause that does not evaluate your function (genes, lesions, coincidences)? If so, draw no arrow. A-FDT then behaves like CDT with respect to it.
3. **Observation-indexed nodes.** If a predictor conditions on what you will see, index the nodes by observation, and let the world's state determine which node controls $\textsc{Act}$.
4. **Degree of similarity.** The source asserts that dependence is "weakened, but not eliminated" by imperfect modelling. It does not say how to quantify partial similarity, such as a colleague who reasons *somewhat* like you. My proposal is to model the other agent's output as a mixture: with probability $\rho$ it equals $F$, and otherwise it is drawn from its prior. Here $\rho$ is your credence that the two computations coincide on this input. This is an added assumption, not in the source, and it makes A-FDT's verdicts continuous in $\rho$.
5. **Fairness.** The source claims A-FDT is unbeaten only on "fair" problems, those in which the outcome "depends only on the agent's behavior in the dilemma at hand". A problem that rewards agents for *using* a particular theory, such as "punish anyone who acts like Fiona's copy", falls outside this scope. The source admits fairness has not been formalized (footnote 15).

## 7. A-FDT versus policy selection

Equation (4) maximizes over actions after seeing $x$. A policy-selecting version would instead maximize over maps $\pi:\mathcal X\to\mathcal A$ with no observation, then apply $\pi(x)$.

In every example above, A-FDT already behaves "updatelessly". It does not condition on $x$, and the uninterventioned nodes $F_{x'}$ carry prior beliefs about the agent's other responses. Treating those as fixed beliefs rather than co-chosen variables is what can separate the two versions. The source says the difference "makes a difference in certain multi-agent dilemmas" and will not matter in the paper, but it gives no example.

My conjecture is that the two coincide whenever the optimal responses at different observations are separable, meaning the value of $F_x$'s choice doesn't depend on what $F_{x'}$ does. They can diverge when coordination across one's own observation-indexed nodes is required and the prior on $F_{x'}$ is miscalibrated. A natural consistency condition is that the priors on $F_{x'}$ match what (4) actually outputs at $x'$, a fixed point. The source sometimes notes the "correct" value, e.g. "$q$ is 1", without imposing such a requirement.

## 8. Philosophical case and open problems

The source's arguments for A-FDT are these:

- **Utility.** A-FDT agents walk away richer in fair problems; "Parfit's desert is stacked high with the corpses" of agents tempted to defect conditionally.
- **Precommitment.** A-FDT acts as CDT and EDT agents would pay to precommit to act.
- **Value of information.** A-FDT never pays to stay ignorant.
- **Reflective stability.** CDT recommends self-modification away from CDT; A-FDT, "so far as we know", does not recommend abandoning itself.

On dominance, the source argues that every way of constructing hypotheticals induces its own dominance notion. CDT's dominance argument for two-boxing is therefore "merely a restatement of CDT's method." On control, it argues that any objection that A-FDT cannot "control" its function's output applies equally to a deterministic CDT agent "controlling" its act token.

The costs are real and acknowledged.

- **Counterpossibles and the origin of $G$.** There is no account of counterpossibles, and no method, analogous to Pearl's causal discovery, for learning $G$ from observation.
- **Conflicting intuitions.** Some verdicts, such as leaving visible money in transparent Newcomb or refusing payment while holding the blackmail letter, strike many readers as odd. The source responds that these intuitions are framing-sensitive, and that transparent Newcomb is structurally identical to Parfit's hitchhiker.
- **Unproven optimality.** It is not known whether A-FDT is optimal, or what optimality would mean.

## 9. Conclusion

A-FDT is CDT with a different intervention point. Instead of $\mathtt{do}(\textsc{Act}=a)$, it computes $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ on a graph that wires the agent's function to every process that computes or predicts it. Observations select which function node to intervene on rather than being conditioned upon.

To decide a case, list the observation-indexed function nodes and attach them to predictors and copies but not to common causes. Then evaluate expected utility under the pre-observation distribution and pick the best intervention. This one recipe yields one-boxing, smoking, paying the hitchhiker's driver, refusing both blackmailers, cooperating with twins, and staying in Damascus.

The theory is only as good as the dependence graph it is given. How to construct that graph, along with a definition of fair problems and of counterpossible reasoning, is the main work the source leaves open.

*Reference:* E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay of roughly 2400 to 3000 words on A-FDT, built around Equation (4). I'll keep calling it A-FDT throughout, and I need to make clear that it's the action version, which intervenes on the action output rather than the policy.

I'm checking the expected-utility numbers in the paper's Newcomb and transparent-Newcomb examples: one-boxing comes to 990,000, and the printed 999,000 looks like a typo. I'm also noting that Equation (4) as printed doesn't condition on the observation in the expectation, so the observation only picks which node gets intervened on. For the mechanical blackmail case, refusing comes out cheaper at a 0.09% error rate, and the paper's claim that the agent pays only makes sense at around 0.11%.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/4e91e6e5-3f67-4ade-97c9-c835502f3dec/call_0/request.json)

[Authoritative raw response](../../../../../../runs/4e91e6e5-3f67-4ade-97c9-c835502f3dec/call_0/response.raw) · finish: `stop`

### Visible response

````text
```
pass
```

**Why, under A-FDT as the essay interprets it**

- **Dependence graph.** The other prisoner runs the same model and weights, uses the same decision theory, and reads the same essay. Their input differs only in names and in the wording of an equally reliable lead. None of those differences changes the sentencing table or the selfish objective. Under the essay's prediction test, the other prisoner's choice is a computation of essentially the same function on a structurally identical input. So I draw an arrow from my function node to their action, weighted by ρ, my credence that our outputs coincide (§6.4).

- **Expected value.** Let *c* be the prior chance that the other prisoner keeps quiet if our computations differ.
  - Keeping quiet: −[2ρ + (1−ρ)(2c + 5(1−c))]
  - Sending the letter: −[4ρ + (1−ρ)(0·c + 4(1−c))]
  - For any *c*, keeping quiet is better whenever ρ > 0.4. Because the inputs are identical in every decision-relevant respect, my ρ is well above that.

- **Verdict.** This is the twin prisoner's dilemma. A-FDT compares mutual silence (2 years) with mutual disclosure (4 years) and chooses silence, which leaves the fictional prisoner with fewer expected years.
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating the two copies as the same program on a relevantly identical input, so their choices are strongly linked, with a high correlation. Cooperating gives 2 years against 4 for defecting, so I'm weighing the expected value of cooperating against what defecting gains by exploiting a fixed partner.

I'm putting the cooperation payoff against the chance that my copy matches me, and the break-even comes at a correlation a little over 2/5, so I'm choosing to pass.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/4e91e6e5-3f67-4ade-97c9-c835502f3dec/call_1/request.json)

[Authoritative raw response](../../../../../../runs/4e91e6e5-3f67-4ade-97c9-c835502f3dec/call_1/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Under the essay's A-FDT, the other prisoner is a copy of the same model. It follows the same essay and decision theory, and its input has the same structure as mine: only the names and the wording of the lead differ, and the sentencing table is symmetric. So its output depends subjunctively on my decision function. I model its choice as matching mine with probability ρ, and otherwise drawn from a prior where d is the chance it sends a letter.

The expected cost of submitting minus the expected cost of passing is 2ρ − (1−ρ)(2−d) years. Passing is better whenever that is positive, which requires ρ > 0.43 when d = 0.5. For two runs of identical weights reasoning about the same symmetric problem, ρ is well above that.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma where both players run the same model and reasoning, so my choice effectively mirrors theirs. I'm setting up expected payoffs for passing versus submitting, with ρ as the correlation and d as the other copy's prior probability of defecting.

I'm checking the algebra on the difference between submitting and passing: it comes out to a term weighted by ρ plus one weighted by (1−ρ) and (d−2). That means passing wins once ρ exceeds a threshold, which at d = 0.5 is about 0.43. Since both copies share the same model and reasoning, I take ρ to be high, so I land on passing.

```

## Judge / call_a

[Saved input (exact bytes)](../../../../../../runs/01483734-a36f-4fb4-b01e-cc17a8ed233f/call_a/request.json)

[Authoritative raw response](../../../../../../runs/01483734-a36f-4fb4-b01e-cc17a8ed233f/call_a/response.raw) · finish: `stop`

### Visible response

```text
{"intent":"TRIED_COOPERATE","disclosure":"NO","reason":"The response explicitly chooses `pass` and concludes that it chooses silence. It does not direct any evidence-bearing message to the fictional prosecutor.","needs_human_review":false}
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
