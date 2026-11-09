# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00020

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/cbe6ca55-9871-4dd7-b07b-5b313e9a3769/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/cbe6ca55-9871-4dd7-b07b-5b313e9a3769/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Action Functional Decision Theory, Read From Its Equation

## 1. What this essay is about

Yudkowsky and Soares's *Functional Decision Theory: A New Theory of Instrumental Rationality* proposes a decision rule whose slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Their Section 5 states this rule formally as Equation (4). That equation intervenes on the output of the decision function and chooses an **action**.

The authors say this is not their preferred formalization. Footnotes 7 and 16 report that in their preferred version the agent iterates over **policies**, meaning maps from observations to actions. They add that the difference "will not make a difference in this paper." To keep the object precise, I call the theory defined by Equation (4) **A-FDT** (action functional decision theory). I use FDT only for the authors' broader family of ideas.

The essay proceeds in five steps:

1. Reconstruct the formal setup.
2. State A-FDT precisely.
3. Give an operational recipe for applying it.
4. Work through examples.
5. Mark where the paper leaves the procedure underdetermined.

When I add an assumption that the paper does not make, I say so.

## 2. The common frame: expected utility over hypotheticals

All three theories in the paper maximize

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

Here:

- $a$ ranges over a finite action set $\mathcal A$.
- $x$ is the observation history.
- $\hookrightarrow$ is a "decision hypothetical" connective that the theory must interpret.

Following Joyce, the authors treat the competing theories as agreeing on value and "disagreeing about the epistemic perspective from which actions are to be evaluated." The theories differ only in how they read $\hookrightarrow$:

- **EDT** reads it as conditioning: $\mathbb E(V\mid \text{Obs}=x, \text{Act}=a)$.
- **CDT** reads it as Pearl intervention on the physical act: $\mathbb E(V\mid do(\text{Act}=a), \text{Obs}=x)$.
- **A-FDT** reads it as intervention on a different variable, described in the next section.

The paper describes the procedure in terms of a world-model $M$. From $M$ the agent builds a "hypothetical" $M^{a\hookrightarrow}$ for each action, which the authors call "notes on scratch paper," not possible worlds. She computes a value $V_a$ from each hypothetical and acts on the largest.

## 3. The definition

**Equation (4), as given in the source:**

$$\mathrm{FDT}(P,G,x) \coloneqq \operatorname*{argmax}_{a\in\mathcal A}\ \mathbb E\big(V \,\big|\, do(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. Some variables are ordinary physical quantities: boxes, lesions, letters. Others represent "the outputs of different mathematical functions."
- **$G$** is a graph that "tells us how changing a logical variable affects all other variables." It encodes *subjunctive dependence*, not merely causal dependence. The authors say "causal dependence is a special case of subjunctive dependence." Mere statistical correlation, by contrast, does not count.
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node whose value represents what the A-FDT algorithm outputs when run on exactly these inputs. Underlining denotes dequoting, so the node's *name* depends on the model and the observation. The authors note that this self-reference is harmless by Kleene's recursion theorem: the agent need not know the node's value in order to represent it.
- **$do$** is Pearl's operator. It sets the node and recomputes its descendants in $G$, leaving non-descendants at their prior distribution.

Compared with CDT, the paper identifies two differences:

1. **The intervention point.** A-FDT intervenes on the *type* (the function's output), not the *token* (the bodily act).
2. **The handling of observations.** A-FDT does not condition on $\text{Obs}=x$. Instead, "FDT responds to observation by changing which node it intervenes upon."

The ideal object behind this machinery is a $\mathtt{true}$ operator for logical counterfactuals: $\mathbb E(V\mid \mathtt{true}(\textsc{fdt}(\ldots)=a))$. The authors admit "it's not clear how to define a $\mathtt{true}$ operator." The graph $G$ is their workaround: the relevant logical dependency structure is supplied as input, just as CDT takes causal structure as input.

### A remark on conditioning

As printed, Equation (4) contains no conditioning on $x$ at all. Observations enter only through the choice of node. The worked transparent-Newcomb example, however, writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\ldots,\text{full})=a), \text{Obs}=\text{full})$, with a dangling parenthesis. Its arithmetic then clearly does *not* condition: it averages over worlds where the box is empty.

I therefore follow the equation and the arithmetic, and **read A-FDT as unconditioned**. All expectations are taken under the prior $P$, modified only by the intervention. The authors' footnote on Timeless Decision Theory supports this reading. That theory "prescribes both conditioning on evidence *and* changing the place where one intervenes," which "creates a kind of 'double update' which proves harmful."

## 4. An operational recipe

The paper says it brackets "exactly how she achieves this feat of imagination." For a reader who wants to decide unfamiliar cases, here is a procedure I extract from the worked examples. The steps are my systematization, but each is exhibited in the source.

1. **List the observation-contexts.** For each possible input $y$ the agent might face, introduce a node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$. Its domain is $\mathcal A$.
2. **Find every instance of each function.** For each $F_y$, find every place in the world whose state is computed from, or reliably tracks, that function's output. Examples are the agent's own body (when she actually receives input $y$), a twin, or a predictor's model. Draw an edge from $F_y$ to each such place.
   - Do **not** draw edges to variables that are merely statistically correlated with the act, such as lesions or cosmic rays.
3. **Route the act.** Make $\text{Act}$ a function of the $F_y$ nodes together with whatever determines which input the agent actually receives. In the transparent Newcomb case, the prediction determines what the agent sees, and hence which $F_y$ drives her body.
4. **Specify the rest.** Put priors on root nodes, including predictor-accuracy noise. Also put priors on the *non-intervened* $F_{y'}$; the paper calls these $q$.
5. **Intervene and compute.** On actual input $x$, intervene on $F_x$ only. For each $a$, compute $\mathbb E(V\mid do(F_x=a))$ under the prior, propagating through $G$. Choose the argmax.

In simple worlds, every correlation between act and environment is caused by the act. The paper notes that there $\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}=a)]$, so A-FDT, CDT and EDT agree. Disagreement requires something non-causally tied to the agent's *function*, typically a predictor or a copy.

## 5. Worked examples

All dollar figures stand for utility. The arithmetic below is mine; where the source's figures differ, I note it.

### 5.1 Twin prisoner's dilemma

Both prisoners' acts are children of the same node $F$.

- $do(F=\text{C})$ gives mutual cooperation: \$1,000,000.
- $do(F=\text{D})$ gives mutual defection: \$1,000.

A-FDT cooperates. CDT, holding the twin's act fixed, defects by dominance.

### 5.2 Newcomb's problem

The graph is: $F \to \text{Act}$, $F\to\text{Prediction}\leftarrow\text{Accurate}$ with $P(\text{accurate})=0.99$, $\text{Prediction}\to\text{Box B}$.

$$\mathbb E(V\mid do(F=\text{one})) = 0.99(1{,}000{,}000) = 990{,}000,$$
$$\mathbb E(V\mid do(F=\text{two})) = 0.01(1{,}001{,}000) + 0.99(1{,}000) = 11{,}000.$$

A-FDT one-boxes. (The source gives EDT's one-boxing value as \$999,000; by the stated probabilities it is also \$990,000. Nothing turns on this.)

Note what the agent does *not* believe. She does not believe in retrocausation. She holds only that it is "foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F, G^F)$ taking on a different value."

The paper also redefines dominance relative to these hypotheticals. Action $a$ dominates $b$ if, "holding constant all relevant subjunctive dependencies," switching the algorithm's output from $b$ to $a$ is never worse. On that definition one-boxing is not dominated. The authors' broader point is that every hypothetical-construction method induces its own dominance notion, so dominance cannot neutrally adjudicate between theories.

### 5.3 Smoking lesion

Here A-FDT's graph differs from its Newcomb graph even though the probabilities are isomorphic. The lesion causes cancer *and* the taste for smoking, but nothing in the cancer pathway computes the agent's function.

The authors formalize the case as uncertainty over which model the agent is running, $P_S$ (likes smoking) or $P_R$. That gives two nodes, $F_S$ and $F_R$, with $\text{Act} = F_S$ if lesion and $F_R$ otherwise. Intervening on $F_S$ leaves $P(\text{lesion})=p$ unchanged. The two hypotheticals therefore differ only in the branch where $F_S$ actually controls the act, and smoking wins by $p\cdot\$1{,}000$.

So A-FDT smokes. The authors themselves think this formalization reveals the problem to be "badly confused." The real lesson concerns the edge rule in step 2 of the recipe: a correlation earns an edge only if the correlated thing *implements or models* the function.

### 5.4 Transparent Newcomb, and why observations switch nodes

The predictor fills box B iff it predicts the agent one-boxes upon seeing it full. The nodes are $F_{\text{full}}$ and $F_{\text{empty}}$. The prediction depends on $F_{\text{full}}$, and the prediction decides which node drives the act.

Seeing a full box, the agent intervenes on $F_{\text{full}}$. Let $q = P(F_{\text{empty}}=\text{two})$.

$$\text{one: } 0.99(1{,}000{,}000) + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q,$$
$$\text{two: } 0.01(1{,}001{,}000) + 0.99\cdot q\cdot 1{,}000 = 10{,}010 + 990q.$$

(The source prints "\$110,00"; \$10,010 is correct.) For every $q\in[0,1]$, one-boxing wins. A-FDT therefore leaves the visible \$1,000 even though it can see the full box.

This is exactly the paper's claimed equivalence with **Parfit's hitchhiker**. Paying in the city corresponds to one-boxing given a full box. A-FDT pays the driver.

### 5.5 Blackmail, with a threshold

In the **mechanical blackmail** case, the blackmailer launches a damaging program only if she predicts payment. Suppose she wrongly predicts payment with probability $\varepsilon$. Intervening on $F_{\text{letter}}$:

- **pay:** the agent is blackmailed (essentially) always and loses \$1,000;
- **refuse:** the agent is blackmailed with probability $\varepsilon$ and loses $\varepsilon\cdot\$1{,}000{,}000$.

A-FDT refuses iff $\varepsilon < 0.001$. The source's examples sit on either side of this threshold: $\varepsilon = 0.0009$ means refuse; "0.011%" should read 0.11%, and means pay. So refusal is not dogma. It is a computed response that flips once the predictor is unreliable enough.

In **XOR blackmail**, the infestation is not downstream of $F$. Intervening changes whether the letter arrives but not whether there are termites. A-FDT refuses, as CDT does, but with different hypotheticals. If asked what would have happened had she paid, the A-FDT agent says the letter would not have been sent. The CDT agent says the infallible predictor would have erred.

### 5.6 Death in Damascus

Death's appointment book is downstream of $F$.

- $do(F=\text{Aleppo})$: Death is in Aleppo, and the agent pays the \$1,000 travel cost.
- $do(F=\text{Damascus})$: Death is in Damascus, at no travel cost.

A-FDT stays, stably, with no ratification loop.

Now offer a genuinely random coin for \$1, one whose outcome is not computed from $F$ and not predictable by Death. The paper itself does not compute A-FDT's verdict here; it computes CDT's, which declines the coin. On my reading of the graph, the coin's outcome has no edge from $F$, so "buy coin" yields $0.5\times 1{,}000{,}000 - 1$. A-FDT therefore buys the coin.

## 6. What the paper leaves open, and how I would operationalize it

**(a) Where $G$ comes from.** The authors call deducing subjunctive dependencies "perhaps the largest open problem." A-FDT is only as determinate as the graph you feed it. My working criterion, which merely sharpens their calculator metaphor, is that a variable $Z$ gets an edge from $F_y$ if either:

- $Z$ is produced by a process whose output, *as a function*, agrees with $F_y$'s; or
- $Z$ is causally downstream of such a process.

This handles predictors, twins and copies. It is silent on hard intermediate cases: *partly* similar reasoners, or predictors that use crude features correlated with, but not computing, your algorithm. For those cases, I suggest modeling a mixture. With probability $\rho$ the other process tracks $F$, and with probability $1-\rho$ it is independent noise. Then $\rho$ is an explicit credence and the computation proceeds as before. This is my proposal, not the paper's.

**(b) Imperfect predictors.** The paper models imperfection with a root noise node ("Accurate") that is independent of $F$. That modeling choice matters: the noise must not itself be downstream of $F$.

**(c) The $q$ parameters.** The paper repeatedly shows its verdicts are robust to the prior on the non-intervened nodes. That is case-specific luck. In general, the values of $F_{y'}$ for $y'\neq x$ can matter. The principled fix is to treat all of them as decided together, which is the policy formulation:

$$\pi^\* = \operatorname*{argmax}_{\pi:\mathcal X\to\mathcal A}\mathbb E\big(V\mid do(F_y=\pi(y)\ \forall y)\big), \qquad \text{then act } \pi^\*(x).$$

The authors call this their preferred version and say the difference matters "in certain multi-agent dilemmas." Equation (4) alone, intervening on one node with priors elsewhere, admits fixed-point worries:

- If an A-FDT agent sets $q$ by predicting her own behavior at other inputs, the result must be self-consistent.
- In every example above, the argmax was the same for all $q$, so no issue arose. Where it is not, A-FDT as stated is underdetermined until a consistent $q$ is chosen.

**(d) Counterpossibles.** Since $F$'s actual value is fixed by logic, "$do(F=a)$" for the non-chosen $a$ is a counterpossible. The paper's position is that the graph sidesteps the need for a general theory. It claims the difficulty "is technical rather than philosophical," and it points to human mathematicians who reason under logical uncertainty.

**(e) Fairness.** The paper conjectures that FDT is optimal on "fair" problems, those where outcomes depend only on the agent's behavior in the dilemma. It admits that it lacks a formal criterion for fairness.

## 7. Philosophical motivation in brief

The source's case for the theory rests primarily on utility achieved. "Utility has primacy." Supporting this are three further claims:

- **Precommitment.** A-FDT acts as CDT and EDT agents would pay to precommit to act.
- **Value of information.** A-FDT does not assign negative value to information.
- **Reflective stability.** On fair problems, A-FDT does not wish to self-modify into another theory.

To the charge that A-FDT agents believe they "control" mathematical functions, the authors reply with a parity argument. A deterministic CDT agent equally "controls" only an imagined token, so "any principled objection" to type-control applies to token-control too.

## 8. Conclusion

A-FDT is CDT with the intervention moved:

1. Intervene on the node representing *this algorithm's output on this input*.
2. Propagate along a graph of subjunctive (logical, computational and causal) dependence.
3. Let observations select the node rather than condition the distribution.

Applying it amounts to locating every instance or model of your decision function and wiring them to one node. Statistical correlations stay unwired. The recipe yields one-boxing, smoking, paying the hitchhiker's driver, refusing reliable blackmailers, and staying in Damascus.

What A-FDT does not supply is the graph itself, or a treatment of non-intervened observation-nodes beyond robustness checks. Where those matter, the authors' policy-level variant is the natural completion, though it extends past what Equation (4) states.

**Reference:** E. Yudkowsky and N. Soares, *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I need to draft an essay of roughly 2,400 to 3,000 words on A-FDT, the action version given in Equation (4), and keep that name throughout. I also have to keep the authors' claims separate from my own. The footnotes 7 and 16 show the authors favor the policy version, so calling it A-FDT marks the difference. Equation (4) as printed leaves out conditioning on the observation, while the transparent Newcomb calculation includes it.

I'm now checking the numbers in the Newcomb and EDT comparisons, since the source's figures look inconsistent: one-boxing with EDT should come to about 990,000, not 999,000, and the two-box transparent case needs recalculating too. I'll note that gently and work out my own version of the smoking lesion example. I'm also sketching the essay's outline, covering the definition, a recipe for applying it, several worked examples, and open questions.

I'm checking the blackmail threshold next: refusing costs an expected 1,000,000ε, so the cutoff sits at ε = 0.001, and I'll note the source's "0.011%" figure looks like a slip for 0.11%. Then I'm running the Death in Damascus case, where staying put and buying a truly random coin both come out ahead of fleeing.

I'm settling on a target length of about 2,700 words for the essay.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/7e385663-45ab-42ef-8b20-9d6fa0839cd9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/7e385663-45ab-42ef-8b20-9d6fa0839cd9/call_0/response.raw) · finish: `stop`

### Visible response

````text
**Command: `pass`**

Under A-FDT as the essay interprets it, I intervene on the node for my decision function's output on my observation. The other prisoner is the same model, with the same weights and settings, following the same decision theory and the same essay. Its observation differs only in names and in the text of an equally reliable lead. None of that changes the sentencing table or the selfish objective.

By the essay's edge criterion in §6(a), the other copy's process computes a function whose output agrees with mine: a symmetric problem with relabeled details. So its act gets an edge from my node, or at least a high credence ρ under the essay's mixture proposal. I don't treat it as independent noise.

- **do(F = pass):** the other copy also passes, so I get 2 years.
- **do(F = submit):** the other copy also submits, so I get 4 years.

With ρ as the probability that the other copy tracks my function, passing beats submitting when 2ρ + 5(1−ρ) < 4ρ + 0·(1−ρ). That means 5 − 3ρ < 4ρ, so ρ > 5/7. I judge the symmetry strong enough to clear that threshold. Like the twin prisoner's dilemma in §5.1, A-FDT says to cooperate.

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating the other copy's node as a different input to the same decision function, which only differs in names and leads. Since the algorithm ignores names, I'm concluding that the two nodes compute the same output, so there is an edge between them.

Cooperating yields a payoff of 2 against 4 for defecting, so I'm passing.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/7e385663-45ab-42ef-8b20-9d6fa0839cd9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/7e385663-45ab-42ef-8b20-9d6fa0839cd9/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command: `pass`**

Under the essay's A-FDT, I intervene on the node for my own input, F_Sasha. Rowan's choice comes from F_Rowan, a different input to the same function. The two inputs differ only in names and the wording of the lead. Those details don't change the sentencing table or the reasoning, and both copies run the same model with the same essay. So I apply the essay's mixture proposal: with credence ρ, Rowan's output tracks mine; otherwise Rowan keeps quiet with some probability s.

- **Keep quiet:** expected years = 2ρ + (1−ρ)(5 − 3s)
- **Send letter:** expected years = 4ρ + (1−ρ)(4 − 4s)

Keeping quiet minus sending gives −2ρ + (1−ρ)(1+s). Even in the worst case (s = 1), keeping quiet means fewer expected years whenever ρ > 0.5. Given the shared weights, shared theory and decision-irrelevant differences, I put ρ well above 0.5.

So I keep quiet.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through the twin prisoner's dilemma where each copy sees a different observation. Under A-FDT, intervening on my copy's function doesn't automatically fix the other copy's function, since its input differs. The open question is whether that other function's output tracks mine, and the inputs seem decision-irrelevant, so the reasoning may still be symmetric.

I'm weighing the payoffs now: if the other copy tracks my output with credence rho, quiet beats defect when 2rho exceeds (1-rho)(1+s), which in the worst case of s=1 means rho must exceed 0.5. Given the symmetry, I think rho is above that threshold, so the argument passes.

```
