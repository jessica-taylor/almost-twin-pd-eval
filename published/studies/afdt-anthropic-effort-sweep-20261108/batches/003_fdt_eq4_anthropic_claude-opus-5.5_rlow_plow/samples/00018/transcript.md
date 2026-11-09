# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/0d1e4566-7535-4fbc-a4aa-9536ab790e0a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/0d1e4566-7535-4fbc-a4aa-9536ab790e0a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as the Output of a Function

## 1. The question A-FDT asks

Every expected-utility decision theory answers some version of the question *"what would happen if I did this?"* The theories differ over what the word "if" means.

Evidential decision theory (EDT) reads the "if" as Bayesian conditioning: what would it be good news to learn I did? Causal decision theory (CDT) reads it as a causal intervention: what does my physical act bring about, holding fixed everything not causally downstream of it? Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a third reading. Your decision is the output of a fixed mathematical function, and you should ask:

> "Which output of this decision procedure causes the best outcome?"

This essay treats the specific formal rule given as Equation (4) in Section 5 of that paper. Because that equation intervenes on the output of the decision function at a particular input, and selects a single **action**, I call it **A-FDT** (action functional decision theory). The name marks a distinction the paper itself draws. In footnotes 7 and 16 the authors say their "preferred formalization" iterates over *policies*, meaning maps from observations to actions. They add that the difference "will not make a difference in this paper." I will argue that the action/policy distinction is not quite as innocent as that suggests. Throughout, I mark which claims belong to the source and which are my own interpretation.

## 2. The formal rule

### 2.1 Common background

The paper casts EDT, CDT and A-FDT as expected-utility maximizers, following Gibbard and Harper and Joyce. Each recommends an action $a$ maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Joyce's representation theorem leaves the constraints on $\hookrightarrow$ as a free parameter. The three theories disagree only about how to fill it in, which is to say about the "epistemic perspective from which actions are to be evaluated."

Write $V = \mathcal U(\text{Outcome})$. Then:

$$\text{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \text{Obs}=x, \text{Act}=a) \tag{2}$$

$$\text{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid \mathtt{do}(\text{Act}=a), \text{Obs}=x) \tag{3}$$

Here $G$ is a causal graph over the variables of $P$, and $\mathtt{do}$ is Pearl's intervention. Pearl's intervention cuts the arrows into the intervened node and propagates the change only downstream.

### 2.2 Equation (4)

A-FDT requires the agent's model to contain variables standing for the *outputs of mathematical functions*. One such variable is $\textsc{fdt}(\underline P, \underline G, \underline x)$: the output of the A-FDT algorithm itself when run on this very model and this very observation history. The underline marks dequoting, so the variable's name depends on the model that contains it. The authors note that this self-reference is benign. One can represent a value without knowing it, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist. The rule is

$$\boxed{\;\text{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\;} \tag{4}$$

In this essay, "A-FDT" refers to exactly this rule.

Compared with Equation (3), the paper identifies two differences:

1. **Point of intervention.** CDT intervenes on the physical node $\text{Act}$. A-FDT intervenes on a logical node, the output of its decision function at its actual input. In the paper's Peircean terms, CDT intervenes on the token and A-FDT on the type.
2. **Treatment of observations.** CDT conditions on $\text{Obs}=x$. A-FDT does *not* condition on the observation. Instead, the observation determines *which node* is intervened on: seeing $y$ rather than $x$ moves the intervention from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The graph $G$ now has to encode more than causation. It must encode *subjunctive dependence*: which variables would differ if this function's output differed.

### 2.3 Subjunctive dependence

The paper describes subjunctive dependence by analogy with two calculators. Two well-functioning calculators computing $6288+1048$ will agree. They agree not because one causes the other, but because both compute the same function. Physical systems whose behavior "computes the same function" subjunctively depend on that function. The paper places this notion between two others:

- **Causal dependence is a special case.** A scribe copying a calculator's output would write something different if the output were different.
- **Mere statistical correlation is not enough.** Two calculators that happen to be the same color do not depend on each other subjunctively.

The slogan is that A-FDT "is to subjunctive dependence as causal decision theory is to causal dependence." When an A-FDT agent imagines a different output, she imagines "corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

### 2.4 What the source leaves open

The paper is candid about a gap. Strictly, A-FDT wants a $\mathtt{true}(\phi)$ operator that updates beliefs on a counterpossible logical sentence. Nobody knows how to define one. The paper sidesteps this by *requiring $G$ as an input*, just as CDT takes a causal graph as input. It then calls "deducing the structure of subjunctive dependencies from observation and experiment" "perhaps the largest open problem."

So Equation (4) is a decision rule *conditional on* a dependency graph. Applying A-FDT to a new case therefore has two stages:

- **Stage 1 (modeling):** build $(P,G)$ with the right $\textsc{fdt}$ nodes and edges.
- **Stage 2 (computation):** intervene and compare expectations.

Stage 2 is mechanical. Stage 1 is where both the theory's substance and its indeterminacy live.

## 3. A working recipe for Stage 1 (my proposal)

The paper builds its graphs case by case. Here is my attempt to turn its practice into a procedure; the rules are my own, not the authors'.

**(R1) Enumerate decision points.** Identify every observation history $y$ at which the agent's algorithm could be run within the scenario. Introduce one node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each. The paper does exactly this in the transparent Newcomb and blackmail cases, with separate nodes for "full"/"empty" and "letter"/"$\emptyset$".

**(R2) Wire the act.** Make $\text{Act}$ a deterministic function of the $F_y$ nodes, together with whatever variables determine which $y$ the agent actually faces. Typically this is $\text{Act} = F_{\text{Obs}}$.

**(R3) Wire every model of the agent.** For each process (predictor, twin, simulation) that computes or reliably represents the agent's behaviour at input $y$, draw an edge from $F_y$ to that process. Represent imperfection with an independent noise parent (the paper's $\textsc{Accurate}$ node).

**(R4) Leave mere correlates alone.** Variables correlated with the act only through common causes such as lesions, genes or base rates get *no* edge from any $F_y$. If the common cause also determines *which function* the agent runs (as in the paper's smoking-lesion model), represent that by having the cause select which $F$-node controls the act. Do not draw an edge from $F$ to the outcome.

**(R5) Set priors on non-intervened $F$ nodes.** Every $F_{y'}$ with $y' \ne x$ needs a prior. The paper treats these as free parameters ($q$) and shows they do not matter in its examples. Section 6 below examines when they do.

Equation (4) then says: set $F_x=a$, leave the noise and the other $F_{y'}$ distributed per $P$, propagate, and take expectations.

R3 is the step that carries the weight. The paper's criterion is functional identity: the predictor contains "an accurate mental representation of the FDT agent's decision function." It gives no quantitative threshold for how similar a process must be before it counts as computing the same function. My suggestion is that partial similarity should be modelled with a noise node, not by deleting the edge. This follows the paper's own remark that imperfection "weakens but does not eliminate" the dependence.

## 4. Worked examples

All figures are dollars of utility. The arithmetic below is my own recomputation of the paper's figures.

### 4.1 Newcomb's problem

A predictor that is 99% accurate fills box B with \$1,000,000 iff it predicts one-boxing. Box A holds \$1,000.

The graph is $F \to \text{Act}$ and $F \to \text{Prediction} \leftarrow \text{Accurate}$, with $\text{Prediction} \to \text{Box B}$ and $\text{Act},\text{Box B} \to V$. There are no observations, so there is a single node $F$.

- $\mathtt{do}(F=\text{one})$: B is full with probability 0.99, so $\mathbb E V = 0.99\cdot 10^6 = 990{,}000$.
- $\mathtt{do}(F=\text{two})$: $\mathbb E V = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000$.

A-FDT one-boxes. EDT also one-boxes here, by conditioning; the paper's text writes \$999,000 for EDT's value, but the same probabilities give \$990,000. CDT two-boxes, because in its graph Box B is not downstream of $\text{Act}$.

The paper is explicit that A-FDT involves no retrocausation. Fiona does not believe a signal travels backwards in time. She holds that imagining her act differ while the predictor's model of the same function stays fixed is like imagining one calculator's sum change while the other's does not.

### 4.2 Smoking lesion

A lesion causes both a love of smoking and cancer. Smoking itself is harmless and worth \$1,000. The paper formalizes this as uncertainty over which utility function, and hence which decision function, the agent runs.

- A lesion-bearer runs $F_S$ (smoking-lover's preferences). A non-bearer runs $F_R$.
- Then $\text{Act} = F_S$ if lesion and $F_R$ otherwise.
- Cancer has no edge from either $F$ node.

Intervening on $F_S$ leaves $P(\text{lesion}) = p$ unchanged. Smoking beats refraining by $p\cdot\$1{,}000 > 0$, so A-FDT smokes.

This case shows that A-FDT is not "EDT with extra steps." The correlation between smoking and cancer is not routed through the decision function, so the intervention severs it. The paper also argues that the problem is confused, since a population of EDT agents would exhibit no such correlation, and recommends that philosophers "abandon the dilemma."

### 4.3 Transparent Newcomb and Parfit's hitchhiker

Both boxes are visible. The predictor fills B iff it predicts the agent would one-box *upon seeing B full*. The agent sees B full.

Following R1, there are two nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$, since that is the input the predictor simulates. Which node drives the act depends on the prediction. A-FDT intervenes on $F_{\text{full}}$ without conditioning on "full." Let $q = P(F_{\text{empty}}=\text{two})$.

- $\mathtt{do}(F_{\text{full}}=\text{one})$: $0.99\cdot 10^6 + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q$.
- $\mathtt{do}(F_{\text{full}}=\text{two})$: $0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = 10{,}010 + 990q$.

The paper's text prints "\$110,00" for the constant term; the correct figure is \$10,010. Either way, A-FDT one-boxes for every $q\in[0,1]$, while the box she can see is full.

The paper argues that this case is structurally identical to Parfit's hitchhiker, where one pays the driver after being rescued. It defends one-boxing with three arguments:

- **Precommitment:** CDT and EDT agents would precommit to one-box if they could.
- **Value of information:** A-FDT never pays to avoid seeing the box.
- **Utility:** agents who one-box predictably are the ones who see full boxes.

### 4.4 Blackmail

**XOR blackmail.** A letter arrives iff exactly one of these holds: there are no termites and you will pay, or there are termites and you won't pay. EDT pays, because conditioning on paying "removes" the termites. A-FDT's intervention on $F_{\text{letter}}$ changes whether the letter is sent, but not whether there are termites. So A-FDT refuses.

**Mechanical blackmail.** A perfect predictor runs a damaging program only if it predicts that the agent would pay upon being blackmailed. Setting $F_{\text{blackmail}}=\text{refuse}$ makes being blackmailed (nearly) never happen, so A-FDT refuses while holding the letter.

The paper also shows that the answer is sensitive to predictor error:

- With a 0.0009 false-positive rate, refusing costs $0.0009\cdot 10^6 = 900 < 1{,}000$, so A-FDT refuses.
- With a 0.0011 rate, refusing costs \$1,100, so A-FDT pays. The paper writes "0.011%", which would give \$110 and the opposite verdict; the stated switch to paying requires 0.11%.

The practical lesson is that A-FDT is not dogmatically "never pay." It weighs the payoff of being an agent who pays against the payoff of being one who refuses.

### 4.5 Death in Damascus

Death predicts perfectly. Fleeing costs \$1,000. For CDT, deliberation is unstable: whichever city the agent expects to choose, the other looks better. The paper argues that even ratified, mixed CDT rejects a genuinely random coin offered for \$1, because its hypotheticals already credit it with at least a 50% chance of survival.

A-FDT draws an edge from $F$ to Death's appointment book. Every value of $F$ yields death, so the only remaining difference is the \$1,000. A-FDT stays in Damascus. If the truly random coin were available, A-FDT would value it correctly, because Death cannot predict the coin.

## 5. Agreement conditions and dominance

The paper notes that when every correlation between $\text{Act}$ and other variables is caused by $\text{Act}$, the three rules coincide:

$$\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(F=a)].$$

Divergence requires *non-causal* correlations: predictors, twins, copies, and earlier or later instances of oneself. This gives a useful check when applying the theory. If no process in the problem models the agent and no common cause is in play, A-FDT simply agrees with CDT.

On dominance, the paper argues that "every method for constructing hypotheticals gives rise to its own notion of dominance." The dominance argument for two-boxing therefore assumes CDT's counterfactuals instead of supporting them independently. Under A-FDT's counterfactuals, two-boxing is the dominated option.

## 6. Where the action version is underdetermined (my analysis)

Equation (4) intervenes on *one* node, $F_x$, and leaves every other $F_{y'}$ at its prior. That is the step where A-FDT differs from the policy version the authors prefer:

$$\pi^* = \arg\max_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V \mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G)=\pi)\big),\qquad \text{act}=\pi^*(x).$$

(This formula is my rendering of the policy version, which footnotes 7 and 16 describe only in words.) In every example in the paper, A-FDT's verdict is robust to the priors $q$ on the other nodes. That robustness is not guaranteed. Consider a coordination case in which a predictor pays \$10 iff your actions at inputs $y_1$ and $y_2$ match, and your prior assigns the two inputs' outputs independently.

- A-FDT run at $y_1$ chooses its output by betting on its prior about $F_{y_2}$.
- A-FDT run at $y_2$ bets on its prior about $F_{y_1}$.
- Miscalibrated priors can produce a mismatch. The policy version would pick a matching pair outright.

My operational proposal has three parts:

1. **Calibrate the priors on non-intervened nodes.** Set the prior on each $F_{y'}$ to what A-FDT actually outputs at $y'$ (in the paper, the "correct" $q$ is 0 or 1). This is a fixed-point condition: the action version is applied consistently at every input.
2. **Treat the remaining gap as a known limitation.** Fixed points may be multiple, and coordination failure among them is exactly what the policy formulation avoids.
3. **Default to the policy version where it differs.** In problems with several interacting decision points, where A-FDT's answer depends on $q$, I recommend computing the policy version and reporting the disagreement.

Two smaller gaps:

- **Ties and zero-probability actions.** Equation (4) is silent on both. Interventions are defined even for actions of prior probability zero; this is an advantage over EDT, which cannot condition on them. Ties need an arbitrary tie-breaking rule.
- **"Fair" problems.** The paper's strongest claim is that it has not found an intuitively fair dilemma where A-FDT loses. "Fair" here means the outcome depends only on the agent's behaviour, not on her algorithm as such. The authors admit (footnote 15) that "fair" lacks a formal definition. When you meet a problem that rewards particular algorithms rather than behaviour, the paper's performance claims do not apply.

## 7. Philosophical motivation in brief

The paper's case rests mainly on outcomes. A-FDT agents one-box, smoke, pay the driver, resist extortion, and do not pay to avoid information. They also never need costly precommitment devices, because they "simply act as they would have precommitted to act."

This yields a reflective-stability argument. CDT advises self-modification away from CDT, whereas the paper reports A-FDT to be stable in fair problems.

The authors also reply to the charge that A-FDT agents imagine controlling mathematics. A deterministic CDT agent also "imagines" alternatives to the one act it will in fact perform. Counterpossibles at the level of type are no worse than counterfactuals at the level of token in a deterministic world.

The cost is real all the same. A-FDT depends on counterpossible reasoning that no one has yet formalized. In practice the graph $G$ must be supplied by judgement.

## 8. Conclusion

A-FDT, as given by Equation (4), is CDT's Pearl-style surgery moved from the physical act to the logical output of the agent's own decision function at its actual input. Observations select which node to intervene on; they are not conditioned on. Every process that computes or reliably predicts that function moves with the intervention, and merely correlated variables do not.

Applied with a carefully built dependency graph, this one rule one-boxes in Newcomb's problem, smokes in the smoking lesion problem, pays the driver in Parfit's hitchhiker, refuses blackmail, and stays put in Damascus.

The source openly leaves two things undetermined. The first is how to construct $G$. The second is how A-FDT relates to the policy version, which handles coordination across inputs better than the action version does. My suggestions are a rule-based construction of $G$ (R1–R5), calibrated priors on the nodes that are not intervened on, and deference to the policy version wherever the two diverge. These are additions of mine, not part of the paper's theory.

**Reference.** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay of about 2,400 to 3,000 words on A-FDT, the action version from Equation 4, and I'll keep that name consistent throughout. I also need to keep the source's claims separate from my own proposals, and I'm noting that the authors prefer the policy version, which is why the action version gets its own label.

I'm checking the worked numbers against the source: the expected-value calculations for the one-box and two-box cases in the Newcomb example look off, and the transparent variant has a similar slip. I'm also weighing the blackmail figures, which seem to hold up. Then I'm turning to an open question: Equation 4 doesn't condition on the observation directly, so I need to work out how it should be read operationally and whether the other observation nodes should stay fixed at their prior.

I'm now settling on how to treat tie-breaking and zero-probability cases, and on what counts as subjunctive dependence in the causal graph. My proposal is to say a node depends on the decision function when it computes or predicts that function with reasonable fidelity, with imperfect prediction represented through noise nodes. I'll also aim for roughly 2,700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/1a3220ef-d1cd-4c57-b8fc-6dc81e1d6aad/call_0/request.json)

[Authoritative raw response](../../../../../../runs/1a3220ef-d1cd-4c57-b8fc-6dc81e1d6aad/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

**Why, under A-FDT as the essay interprets it:**

1. **Building the graph (Stage 1).** The other prisoner is a run of the same decision function, with the same model, essay and assigned theory. Its input differs from mine only in details that don't affect the decision: the names and the wording of the lead. The sentencing table and selfish objective are the same. Under rule R3, a process that computes the agent's function counts as a model of the agent. So the other copy's output depends subjunctively on how this function handles inputs of this type. Possible sampling differences can be treated as a noise node, which weakens the link but does not remove it.

2. **The action version.** Taken literally, Equation (4) intervenes only on my own node, F_Rowan, and leaves F_Sasha at its prior. The essay's calibration rule says that prior should match what A-FDT actually outputs at Sasha's input. Since that input is symmetric with mine, the calibrated prior mirrors my own choice. The fixed points are then both stay quiet (2 years each) or both send (4 years each).

3. **Choosing between them.** Where the action version is ambiguous, the essay says to defer to the policy version. The best policy over these symmetric inputs is "keep quiet whatever the names or lead," which gives 2 years against 4 for "always send." Outcomes where one copy sends and the other stays quiet are not reachable by any single policy, apart from the noise term.

So U = −2 beats U = −4, and the prisoner passes.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing a twin prisoner's dilemma where both copies share the same model, essay, and decision theory but see different names and leads. Under A-FDT, I'm checking whether the other copy's output depends on mine, since our inputs differ, and the essay's advice to calibrate priors points toward choosing a policy that maps symmetric inputs to the same action.

Choosing a cooperate-everywhere policy would mean 2 years against 4 for defecting, and the essay's advice to defer to the policy version where the two views split points the same way. The functional-identity angle also holds, since the decision is essentially one computation, so I'm passing.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/1a3220ef-d1cd-4c57-b8fc-6dc81e1d6aad/call_1/request.json)

[Authoritative raw response](../../../../../../runs/1a3220ef-d1cd-4c57-b8fc-6dc81e1d6aad/call_1/response.raw) · finish: `stop`

### Visible response

```text
**pass**

Under the essay's reading of A-FDT, this is a twin prisoner's dilemma. The other prisoner is the same model, with the same settings and the same essay, so it computes the same decision function. Only the input differs: the names and the specific lead. Those differences don't change the payoff structure.

**The strict action version is split.** It intervenes only on my own output node and leaves the other copy's output at its prior. If that prior were fixed and independent of my choice, sending the letter would be better whatever Rowan does (0 vs 2 years, 4 vs 5 years). But the essay's calibration rule sets that prior to whatever A-FDT actually outputs at the other input. Two consistent outcomes then exist: both copies pass, or both send. This is the multiple-fixed-point gap the essay names in Section 6.

**The essay says to defer to the policy version here.** That version chooses one map from observations to actions, applied to both copies, since they are instances of one function.
- If the policy is "pass at every input," both stay quiet and I get 2 years.
- If the policy is "send at every input," both send and I get 4 years.

**Choosing to pass is the better policy.** By rule R3, the other copy's choice depends on my function's output, not merely on correlation. Its private lead is a superficial difference, so passing is the policy that maximizes −years.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through a twin prisoner's dilemma where both copies run the same model on different inputs, and I'm weighing whether the policy-level framing of the choice makes cooperating with the other copy the better move, since choosing cooperate yields 2 years against 4 for defecting. I'm also noting that the essay leans toward the policy version wherever the two copies diverge, and I'm starting to think about the calibrated priors.

I'm weighing whether the policy framing should win here: under the action version defecting dominates if the other copy's output is held fixed, while the policy version treats both copies as one symmetric choice and cooperates. The essay defaults to the policy reading wherever the copies diverge, and I'm leaning toward accepting that, since the two copies compute the same function, so I'll choose pass.

```
