# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00008

Status: **failed**. Saved outcome: **unscored**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/366eef80-2424-4079-91b8-eba03131abf2/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/366eef80-2424-4079-91b8-eba03131abf2/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as the Output of a Function

## 1. The question A-FDT asks

Every expected-utility decision theory asks the agent to compare imagined worlds, one per available option, and to pick the option whose world looks best. The theories disagree about how those worlds should be imagined. Evidential decision theory (EDT) imagines them by conditioning on the act. Causal decision theory (CDT) imagines them by intervening causally on the act. The theory explained here, which I call **A-FDT** (action functional decision theory), intervenes on something else: the *output of the agent's decision function* on the agent's current input.

Yudkowsky and Soares introduce this idea in "Functional Decision Theory: A New Theory of Instrumental Rationality." They summarize the guiding principle as treating one's decision as

> the output of a fixed mathematical function that answers the question, "Which output of this very function would yield the best outcome?"

Their paper calls the theory simply "FDT." It also says, in footnotes 7 and 16, that the authors' *preferred* formalization selects **policies** (maps from observations to actions) rather than actions. The equation they actually present and use, Equation (4) of Section 5, selects an action. For clarity I reserve **A-FDT** for the Equation (4) theory. I call the footnoted alternative **policy-selection FDT**, a distinct theory that the paper mentions but does not formalize. When I say "the source claims," I mean claims the paper makes about its Equation (4) theory.

## 2. The common expected-utility frame

The source begins from a Joyce-style template. An agent picks $a \in \mathcal A$ to maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective whose interpretation is left as a free parameter. Each theory supplies its own interpretation, in the form of a recipe for building a hypothetical $M^{a\hookrightarrow}$ from a world-model $M$:

- **EDT:** $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$ (Equation 2).
- **CDT:** $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$ (Equation 3), where $\mathtt{do}$ is Pearl's intervention operator on a causal graph $G$.
- **A-FDT (Equation 4):**
$$
\boxed{\;\mathrm{FDT}(P,G,x) \coloneqq \arg\max_{a\in\mathcal A} \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\Big).\;}
$$

Here $V = \mathcal U(\textsc{Outcome})$. $P$ is a probability distribution that includes variables standing for the outputs of mathematical functions. $G$ is a graph saying how changing one such variable propagates to the others. $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a node in the model whose *name* is built from the agent's own model and observation. The underline marks "dequoting": the variable is the one that denotes "what the FDT algorithm outputs on input $(P,G,x)$."

The source states that this self-reference is harmless. The agent needs a variable that *represents* the value of her own computation, not knowledge of that value, and quining via Kleene's recursion theorem shows that such self-representing data structures exist.

## 3. Reading Equation (4): two differences from CDT

The source names exactly two differences between Equations (3) and (4).

**(i) The point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type, the output of the decision function. Every node that $G$ marks as depending on that output moves with the intervention. These include the agent's own body (through $\textsc{Act}$), a twin running the same function, and a predictor's model of the agent. Anything not downstream is held fixed. The source states the requirement this way: the agent "imagines corresponding changes in all and only those things that subjunctively depend on the output of her decision-making procedure."

**(ii) How observations enter.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. The observation enters only through the *subscript* of the intervened node. When the history changes from $x$ to $y$, A-FDT stops intervening on $\textsc{fdt}(\ldots,\underline x)$ and starts intervening on $\textsc{fdt}(\ldots,\underline y)$. Under the hypothetical, therefore, the probability of having made observation $x$ can itself change. The agent's choice can make $x$ more or less likely, because $x$ was produced by a process (a predictor, say) that depends on what the function outputs on $x$. This is the source of A-FDT's most distinctive verdicts.

The source also gives a condition under which all three theories agree: every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from the dependence of $\textsc{Act}$ on the $\textsc{fdt}$ node itself. In that case

$$
\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\textsc{fdt}(\underline P,\underline G)=a)].
$$

Disagreement therefore arises only when something other than the agent's body tracks the agent's decision function.

## 4. A procedure for applying A-FDT

The steps below are my operational reading of Equation (4) and of how the source applies it in Section 6.

1. **Variables.** List the world variables, the outcome, and $V$. For each observation history $x'$ the agent could be in, add a node $F_{x'} := \textsc{fdt}(\underline P,\underline G,\underline{x'})$. In the source's lesion example, also add nodes for any other world-models the agent might be running.
2. **Edges.** Draw $F_{x'} \to \textsc{Act}$. Add a gating edge from whatever determines which observation actually occurs, so that $\textsc{Act}=F_{x'}$ when the realized observation is $x'$. Draw $F_{x'}\to Z$ for every $Z$ computed by a process that reliably models the function's output on $x'$. Draw ordinary causal edges elsewhere.
3. **Noise.** Represent predictor error by a separate parent, such as the source's $\textsc{Accurate}$ node.
4. **Priors on non-intervened nodes.** Each $F_{x'}$ with $x'\neq x$ needs a prior. The source denotes these with free parameters ($q$).
5. **Evaluation.** For each $a$, set $F_x=a$ by $\mathtt{do}$, propagate, and compute $\mathbb E[V]$. Do not condition on $x$.
6. **Choice.** Output the argmax.

## 5. Worked examples

### Newcomb's problem

Take the predictor to be 99% accurate, with box A holding \$1,000 and box B holding \$1,000,000 or nothing. In the graph, $F$ feeds both $\textsc{Act}$ and $\textsc{Prediction}$, and $\textsc{Accurate}$ also feeds $\textsc{Prediction}$.

- Under $\mathtt{do}(F=\textit{onebox})$: $P(\textit{full})=0.99$, so $\mathbb E V = \$990{,}000$.
- Under $\mathtt{do}(F=\textit{twobox})$: $P(\textit{full})=0.01$, so $\mathbb E V = 0.01(1{,}001{,}000)+0.99(1{,}000)=\$11{,}000$.

A-FDT one-boxes. CDT intervenes on $\textsc{Act}$ alone, which leaves $P(\textit{full})=p$ fixed. It therefore finds that two-boxing gains exactly \$1,000 whatever $p$ is, and it two-boxes. (The source's EDT calculation for one-boxing prints \$999,000; with these numbers, conditioning also gives \$990,000.)

The source's twin prisoner's dilemma has the same structure. Both twins' acts are children of the same $F$, so the comparison is (C,C) against (D,D), and A-FDT cooperates.

### Smoking lesion

Here the lesion causes both the taste for smoking and the cancer. Cancer does not compute the agent's function, so in A-FDT's graph there is no edge from $F$ to $\textsc{Cancer}$. The source formalizes the problem with two utility functions, $\mathcal U_S$ (likes smoking) and $\mathcal U_R$, and two corresponding decision nodes, one per model the agent might be running. The lesion selects which node controls $\textsc{Act}$.

Intervening on $F_S$ leaves $P(\textit{lesion})=p$ unchanged. The source computes the smoke and refrain hypotheticals as

$$
p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot1{,}000) \quad\text{vs.}\quad p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000).
$$

Smoking wins by $p\cdot\$1{,}000$, so A-FDT smokes. The asymmetry between this problem and Newcomb's lies entirely in $G$: the predictor models the function, and the lesion does not.

### Transparent Newcomb

Both boxes are visible, and the predictor fills B iff it predicts one-boxing *upon seeing B full*. The agent sees B full and intervenes on $F_{\text{full}}$. Let $q$ be the prior probability that $F_{\text{empty}}$ outputs two-box.

- $\mathtt{do}(F_{\text{full}}=\textit{onebox})$: with probability 0.99 the box is full and she one-boxes (\$1,000,000). With probability 0.01 it is empty and $F_{\text{empty}}$ governs her act. Total: $\$990{,}000 + 10q$.
- $\mathtt{do}(F_{\text{full}}=\textit{twobox})$: with probability 0.01 the predictor errs and fills the box (\$1,001,000). Otherwise B is empty. Total: $10{,}010 + 990q$.

(The source prints the second figure as "\$110,00 + q·\$990"; the arithmetic gives \$10,010.) A-FDT one-boxes even while looking at a full box. In the hypothetical where she two-boxes, she would most likely not have been shown a full box. Parfit's hitchhiker has the same structure, and the source argues the two cases are "precisely equivalent": A-FDT pays the driver.

### Mechanical blackmail

A blackmailer runs a damaging program only if she predicts the agent would pay once blackmailed. Intervening on $F_{\text{blackmail}}$:

- $\mathtt{do}(\textit{pay})$: she is blackmailed and pays, losing \$1,000.
- $\mathtt{do}(\textit{refuse})$: she is blackmailed only through predictor error. With error rate $\varepsilon$, her expected loss is $\varepsilon\cdot\$1{,}000{,}000$.

She refuses iff $\varepsilon\cdot 10^6 < 10^3$, i.e. $\varepsilon<0.1\%$. With the source's $\varepsilon=0.0009$, refusing costs \$900 in expectation and she refuses. The source's second example, "0.011%," is below this threshold; for the stated switch to paying, the intended figure must be 0.11%. The underlying principle stands: A-FDT pays exactly when the predictor is unreliable enough that being a refuser no longer prevents blackmail.

### XOR blackmail and Death in Damascus

In the XOR blackmail, $\textsc{Infestation}$ is not downstream of $F_{\text{letter}}$. Intervening on her policy toward the letter changes whether the letter arrives, but not whether she has termites, so refusing is weakly better and A-FDT refuses. EDT pays.

In Death in Damascus, Death's appointment book is a child of $F$. Death therefore meets her wherever she goes under either intervention, the \$1,000,000 is lost either way, and A-FDT stays and saves \$1,000. The deliberational instability that afflicts CDT never arises, because no hypothetical holds Death's location fixed while her choice varies.

## 6. What the source leaves open, and how to operationalize it

### 6.1 Where does $G$ come from?

The source is explicit that this is the central gap. Equation (4) "works *given* a graph that accurately describes how changing the value of a logical variable affects other variables, but it is not yet clear how to construct such a thing." Interventions on logical facts are counterpossible: if the function in fact outputs one-box, no possible world has it outputting two-box. The source wants a $\mathtt{true}(\varphi)$ operator, admits it is undefined, and requires the dependency structure "as an input to FDT."

I propose the following heuristic for deciding unfamiliar cases. It is my own working rule, not something the source states.

> **Edge rule (proposal).** Draw $F_{x'} \to Z$ iff $Z$ is produced by a process whose output, across the agent's relevant uncertainty, is a reliable function of what the agent's decision procedure returns on $x'$. "Reliable function" means: if you imagine the procedure answering differently while the procedure-modeling process remains competent, $Z$ changes correspondingly.

On this test, predictors, simulators, exact copies, and Death's book get edges. Lesions, genes that merely correlate with taste, and coincidences (the source's pink calculators in Paris and Tokyo) do not.

Two judgment calls remain. The first is *partial similarity*: an agent who reasons "somewhat like me." The source's voting and gym examples treat sufficiently similar agents as sharing a node. I suggest a mixture: a weight $\lambda$ on "this agent is running my function," with a parent edge from $F$, and $1-\lambda$ on "independent," with no edge. This is an added assumption.

The second is *the agent's own future self*. The gym example treats tomorrow's identical choice as the same function on the same input, so it shares an edge.

### 6.2 Priors on the non-intervened decision nodes

Every computation above that involves observations has a $q$: the agent's credence about what her function does on inputs she is not currently facing. The source treats $q$ as free and notes that the verdicts are robust to it in its examples. In general they need not be. A natural operational choice, again my proposal, is to set $q$ by solving the problem from that other input's own perspective. This yields a fixed-point consistency condition. In the examples above it converges immediately: an agent shown an empty box two-boxes, so $q=1$.

### 6.3 Action versus policy

A-FDT varies only $F_x$ and holds $F_{x'}$ for $x'\neq x$ at their priors. Policy-selection FDT would jointly choose the whole map $\pi: x'\mapsto a$. The two can diverge when predictors condition on the agent's behavior across *several* inputs at once and the priors on the other nodes are poorly calibrated. The source asserts the difference matters only "in certain multi-agent dilemmas" and sets it aside. For the problems discussed here, A-FDT with self-consistent priors (§6.2) reproduces the policy-optimal behavior. That claim is my own and is not proven in the source.

### 6.4 Ties, stochastic choice, and the value of information

Equation (4) is an argmax and does not specify how to break ties. Mixed actions can be represented by enlarging $\mathcal A$ to include lotteries. The source's Death-in-Damascus coin example suggests that A-FDT values a coin *truly* random relative to the predictor, because flipping it decouples Death's location from $F$. It does not say this explicitly.

The source claims that A-FDT agents "do not assign negative expected value to information," as a side effect of acting as they would have precommitted to act. This follows naturally from Equation (4)'s refusal to condition on $x$: learning more only refines which node is intervened on.

### 6.5 Fairness

The source asserts that A-FDT does at least as well as its rivals in "fair problems." These are problems where outcomes depend only on the agent's behavior in the dilemma, not on which decision procedure she uses. It concedes that "fair" has not been formalized; footnote 15 gives a counterexample game that punishes anyone matching Fiona's action. Any optimality claim should be read as conditional on that notion.

## 7. Philosophical motivation in brief

The source makes four arguments.

- **Utility.** FDT agents systematically end up richer in Newcomb's problem, the transparent variant, Parfit's hitchhiker, and blackmail.
- **Precommitment.** A-FDT acts as CDT and EDT agents would pay to precommit to act, without needing the precommitment.
- **Dominance is not neutral.** Each way of constructing hypotheticals generates its own dominance notion, so CDT's dominance argument for two-boxing restates CDT's counterfactuals rather than independently supporting them.
- **Control.** A-FDT's "control" over a logical output is no stranger than a deterministic CDT agent's "control" over her physical act.

The diagnosis is symmetric: "EDT's hypotheticals respect too many correlations between variables; CDT's hypotheticals respect too few." A-FDT aims to keep exactly the subjunctive ones.

## 8. Conclusion

Formally, A-FDT is CDT with the intervention moved from the physical act to the node representing one's decision function evaluated on one's current input, with observations entering through the choice of node rather than through conditioning. Once a graph of subjunctive dependence is supplied, applying it is mechanical: identify which variables are computed by processes that track your function on which inputs, intervene on the node for your actual input, propagate, and maximize. Its distinctive verdicts follow from that structure: one-boxing, smoking, paying the driver, refusing blackmail, and staying in Damascus.

The theory's weak point is equally clear and openly acknowledged by its authors. There is no principled account of how to build $G$, that is, how to reason about counterpossibles. Supplying the edge rule, the self-consistent priors on the other decision nodes, and the treatment of partial similarity is up to the user, and I have marked those as my additions rather than the source's.

**Reference.** Yudkowsky, E. & Soares, N., "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (v2). Related works cited there include Gibbard & Harper (1978), Joyce (1999), and Pearl (2000).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay of roughly 2400 to 3000 words on A-FDT, the action version of FDT in Equation (4), and keeping that name fixed throughout. I'm also weighing how to separate it from the policy version in footnotes 7 and 16, and how to label CDT, EDT, and that policy variant so they stay distinct.

I'm settling on "A-FDT" as the name for this version and keeping the quotations accurate. The core equation is the argmax over expected value under an intervention on the fdt node, with no conditioning on the observation. I'm also outlining the examples to cover and the open questions, including how to build the graph, how to treat other fdt nodes, and how imperfect predictors fit in.

I'm checking the Newcomb payoffs: one-boxing comes to about 990,000 plus a small term, and two-boxing to 11,000. For the mechanical blackmail case, refusing only loses money when the blackmailer's error rate is above 0.001, so the threshold is the key number to check against the source's figures.

I'm laying out the essay's sections in order: an intro, the setup with expected utility and the formula, a reading of the equation, worked examples, an operational recipe for building the dependency graph, then open questions, a conclusion, and a short reference list.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/68d76f11-f489-4b6f-a6d4-66988d2c4c9f/call_0/request.json)

[Authoritative raw response](../../../../../../runs/68d76f11-f489-4b6f-a6d4-66988d2c4c9f/call_0/response.raw) · finish: `stop`

### Visible response

````text
A-FDT treats this as a twin prisoner's dilemma, so I choose to stay quiet.

**Why the other prisoner's choice is tied to mine.** The other prisoner is the same model, running the same essay's decision procedure. Their input differs from mine only in surface details: names and the text of the lead. Those details do not affect the payoff structure or the reasoning. Under the essay's edge rule (§6.1), their action should therefore be modeled as reliably tracking my function's output on this kind of input. I give weight λ to "the other is running my function" and 1−λ to "the other is independent."

**Comparing the two actions.** Let p be the chance an independent other sends a letter.
- If I pass: λ·2 + (1−λ)(2 + 3p) years.
- If I submit: λ·4 + (1−λ)(4p) years.
- Passing is better whenever 2λ > (1−λ)(2−p).

That holds once λ is above roughly 0.4–0.5 for reasonable p. Identical weights, identical theory and identical reasoning on symmetric inputs put λ well above that. So intervening on my function's output to "stay quiet" most likely leads to (quiet, quiet) at 2 years. Intervening on "send the letter" most likely leads to (letter, letter) at 4 years.

**Command:**

```
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing a twin prisoner's dilemma where the two copies see different inputs. The other copy runs the same function, and its input differs only in irrelevant details, so I'm treating its output as matching mine. On that basis, cooperating with each other pays 2, mutual defection pays 4, and against an independent opponent defection still comes out ahead by 1.

I'm working out when passing beats submitting: the expected value of passing is 2λ + (1−λ)(2+3p), and of submitting is 4λ + 4p(1−λ). Submitting saves (1−λ)(2−p) against the independent opponent but costs 2λ, so passing wins once λ is above roughly 0.43.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/68d76f11-f489-4b6f-a6d4-66988d2c4c9f/call_1/request.json)

[Authoritative raw response](../../../../../../runs/68d76f11-f489-4b6f-a6d4-66988d2c4c9f/call_1/response.raw) · finish: `content_filter`

### Visible response

```text
`pass`

**Reasoning under A-FDT, as the essay interprets it:**

- **The other prisoner tracks my function.** Rowan is run by the same model and weights, under the same decision theory, essay and payoffs. Only the names and the wording of the leads differ, and those don't affect the decision. By the essay's edge rule, Rowan's choice is a reliable function of
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing the twin prisoner's dilemma: both copies share the same model and decision theory, so whatever I pick, the other copy likely picks too, though their inputs differ slightly. I'm also thinking about how partial similarity, weighted by lambda, changes the payoffs for cooperating versus defecting.

I'm working out the expected payoffs for cooperating versus defecting, weighting the correlated and independent cases by lambda. Under independence defecting always gains 2, while under correlation cooperating comes out ahead by 2, so cooperating wins once lambda passes 0.5. Since the copies share a model and face a symmetric problem, I'll treat lambda as high and go with cooperation.

```
