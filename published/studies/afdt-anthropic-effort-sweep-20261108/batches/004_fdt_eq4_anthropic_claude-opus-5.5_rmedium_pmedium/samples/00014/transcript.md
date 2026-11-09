# 004_fdt_eq4_anthropic_claude-opus-5.5_rmedium_pmedium / 00014

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a1f3582d-20ac-44db-a3af-cd3aaf09965a/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a1f3582d-20ac-44db-a3af-cd3aaf09965a/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on Your Own Algorithm

## 1. The question A-FDT asks

Decision theories in the expected-utility tradition agree on how to value outcomes. They disagree about which hypothetical you should evaluate when you ask "what if I did $a$?". Yudkowsky and Soares (2017) propose an answer they call *functional decision theory*. On their view, the rational agent should treat her decision as the output of a fixed mathematical function and ask, in their words, "Which output of this very function would yield the best outcome?"

This essay explains the formal version of that idea given in Equation (4), Section 5 of their paper. In that equation the agent intervenes on the output of her decision function and sets it to a single **action** $a$ for her current observation. I call this theory **A-FDT** (action functional decision theory). The label matters because the authors note a different formulation that they prefer. Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." The paper does not formalize that policy-selecting version, and I will refer to it as the *policy variant*. Equation (4), and everything computed in the paper's worked examples, is A-FDT.

I compare A-FDT with two established theories:

- **EDT** (evidential decision theory), which evaluates an action by conditioning on it.
- **CDT** (causal decision theory), which evaluates an action by a Pearl-style causal intervention on it.

Throughout, I mark which claims come from the source and which are my own interpretations.

## 2. The common framework

**Source.** All three theories maximize

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

where $x$ is the agent's observation history. The connective $\hookrightarrow$ is a "decision hypothetical", and its interpretation is the free parameter in Joyce's representation theorem. The paper describes deciding as a three-step process:

1. The agent holds a world-model $M$.
2. For each action $a$ she builds a hypothetical $M^{a\hookrightarrow}$, a "mental or computational object" and "not themselves beliefs."
3. She computes a value $V_a$ from each hypothetical and takes the argmax.

With $V := \mathcal U(\textsc{Outcome})$:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E\!\left(V \mid \textsc{Obs}=x,\ \textsc{Act}=a\right) \tag{2}
$$

$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E\!\left(V \mid \mathtt{do}(\textsc{Act}=a),\ \textsc{Obs}=x\right) \tag{3}
$$

Here $G$ is a causal graph over the variables of $P$. The operator $\mathtt{do}(\textsc{Act}=a)$ sets the node and recomputes only what lies downstream of it. Every other variable keeps its prior distribution, or its posterior given the observation.

## 3. The definition of A-FDT

**Source (Equation 4).** A-FDT requires that $P$ contain variables standing for the *outputs of mathematical functions*. In particular, $P$ contains a variable $\textsc{fdt}(\underline P,\underline G,\underline x)$ representing what the A-FDT algorithm itself returns on the agent's own inputs. The underlines denote dequoting: the variable's name is built from the model and the observation. The graph $G$ must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly." In particular, it must say which variables change when a logical variable changes. Then:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right)\ } \tag{4}
$$

The paper identifies two structural differences from CDT.

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type: the output of the function that the agent's brain computes. That same function may also be computed, or modelled, elsewhere, for example by a twin or a predictor.
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition on its observation at all. The observation instead selects *which node* gets intervened on. If the history changes from $x$ to $y$, the intervention target changes from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The guiding slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

The paper calls the relevant relation *subjunctive dependence*. Two physical systems that compute the same function both subjunctively depend on that function. The paper's examples are two calculators evaluating $6288+1048$, or an agent and an accurate predictor's model of her. Causal dependence is a special case: a scribe copying a calculator's output depends on that output both causally and subjunctively. Mere correlation is not subjunctive dependence. Two calculators that happen to be pink are not linked in this way.

**Self-reference.** The agent needs a variable that *represents* her own output, but she does not need to know its *value*. The paper appeals to Kleene's recursion theorem ("quining") to show that such self-representation is consistent.

**Why not a "true" operator?** The ideal operation would update $P$ on a counterpossible sentence such as "the function $\textsc{fdt}$ outputs $a_2$" when in fact it outputs $a_1$. No satisfactory definition of such an operation exists. Equation (4) avoids the problem by assuming that the logical dependency structure is given in $G$. That plays the same role as the causal structure that CDT takes as input.

## 4. A recipe for applying A-FDT

The following procedure is my distillation of what the paper does in its examples.

1. **List the variables.** Include the outcome-relevant world variables, the agent's physical action $\textsc{Act}$, and one logical node $F_y := \textsc{fdt}(\underline P,\underline G,\underline y)$ for each observation $y$ the agent might find herself making.
2. **Draw the subjunctive edges.** Connect $F_y$ to $\textsc{Act}$, since the body implements the function when it observes $y$. Also connect $F_y$ to every process that computes or accurately models the function on input $y$: predictors, twins, simulations. Do *not* draw edges to merely correlated processes such as lesions, common environmental causes, or coincidences.
3. **Make $\textsc{Act}$ a switch.** Write $\textsc{Act}$ as a function of whichever variable determines the agent's actual observation, routing control to the matching $F_y$.
4. **Put priors on everything else.** This includes the logical nodes you will *not* intervene on. For example, $q = P(F_{y'}=\text{some action})$ for an alternative observation $y'$.
5. **Intervene and compute.** For the actual observation $x$ and each action $a$, set $\mathtt{do}(F_x=a)$, propagate along $G$, compute $\mathbb E(V)$ under the *prior*, without conditioning on $x$, and take the argmax.

Steps 2 and 4 are where the theory is underdetermined. I return to them in Section 7.

## 5. Worked examples

### 5.1 Newcomb's problem

The predictor is 99% accurate. Box A holds \$1,000. Box B holds \$1,000,000 if and only if one-boxing was predicted. In the graph, $F$ points to both $\textsc{Act}$ and $\textsc{Prediction}$, and an independent $\textsc{Accurate}$ node also feeds $\textsc{Prediction}$.

- Under $\mathtt{do}(F=\textit{onebox})$, box B is full with probability $0.99$. So $\mathbb E V = 0.99\times 10^6 = \$990{,}000$.
- Under $\mathtt{do}(F=\textit{twobox})$, box B is full with probability $0.01$. So $\mathbb E V = 0.01(1{,}001{,}000) + 0.99(1{,}000) = \$11{,}000$.

A-FDT one-boxes. EDT gets the same two numbers by conditioning, provided its prior on each action is not extreme. (The paper's text gives Eve the EDT agent "\$999,000", which looks like a slip for \$990,000.) CDT keeps $P(\textit{full})=p$ fixed under both interventions. Two-boxing is then better by \$1,000 for every $p$, so CDT two-boxes.

The paper stresses that A-FDT involves no retrocausation. The agent "does not think that a physical signal passes between her action and the predictor's prediction." She only refuses to imagine her function's output changing while an accurate model of that same function stays fixed.

### 5.2 The twin prisoner's dilemma and coordination

Both twins compute the same function, so $\mathtt{do}(F=c)$ makes both cooperate and $\mathtt{do}(F=d)$ makes both defect. The comparison is \$1,000,000 against \$1,000, and A-FDT cooperates.

The paper's voting example has the same structure. Ten agents each pay \$1,000 to vote and receive \$1,000,000 only if all ten vote. In a group of A-FDT agents that recognize the shared function, $\mathtt{do}(F=\textit{vote})$ moves all ten votes together, so each agent votes. The paper says this is "not out of altruism, but out of an awareness that the other members of the group will reason symmetrically."

### 5.3 The smoking lesion

This case shows that A-FDT is not EDT in disguise. The lesion causes both a taste for smoking and cancer. Smoking itself is causally inert, and nothing in the problem *computes the agent's decision function*. So no edge runs from any $\textsc{fdt}$ node to $\textsc{Cancer}$.

The paper's formalization is subtle. The lesion fixes which utility function the agent has, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$ (does not). That in turn fixes which of two logical nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls $\textsc{Act}$. The agent cannot tell which one she is running. Intervening on the $S$-node leaves $P(\textit{lesion})=p$ unchanged. The two hypotheticals then differ only in the case where the $S$-node controls the action, and that case contributes $p\cdot\$1{,}000$. So:

$$
\mathbb E[V\mid \mathtt{do}(\cdot=\textit{smoke})]-\mathbb E[V\mid \mathtt{do}(\cdot=\textit{refrain})] = p\cdot \$1{,}000>0 .
$$

A-FDT smokes, as CDT does. EDT refrains. This is the paper's central claim against Gibbard and Harper: a single rule can both one-box and smoke. The difference lies entirely in the graph. A predictor models the agent's function and a lesion does not. (The paper itself calls this dilemma "badly confused" and keeps it mainly for historical reasons.)

### 5.4 The transparent Newcomb problem

Both boxes are visible. The predictor fills B if and only if it predicts the agent will one-box *upon seeing B full*. The graph has two logical nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. $F_{\text{full}}$ drives the prediction. $\textsc{Act}$ is controlled by $F_{\text{full}}$ if B is full and by $F_{\text{empty}}$ otherwise. Let $q$ be the prior that the agent two-boxes on seeing an empty box. Suppose she sees B full and evaluates $\mathtt{do}(F_{\text{full}}=a)$.

- **$a=\textit{onebox}$.**
  - With probability 0.99 the prediction is accurate, B is full, and she gets \$1,000,000.
  - With probability 0.01 the prediction is wrong, B is empty, $F_{\text{empty}}$ acts, and she gets $q\cdot\$1{,}000$ in expectation.
  - Total: $\$990{,}000 + \$10q$.
- **$a=\textit{twobox}$.**
  - With probability 0.99 the prediction is accurate, B is empty, and she gets $q\cdot\$1{,}000$.
  - With probability 0.01 the prediction is wrong, B is full, and she gets \$1,001,000.
  - Total: $\$10{,}010 + \$990q$.

(The paper prints the constant as "\$110,00", evidently a typo for \$10,010.)

A-FDT one-boxes *even while looking at a full box*. Both CDT and EDT condition on $\textsc{Obs}=\textit{full}$, compare \$1,001,000 with \$1,000,000, and two-box. A predictor anticipates this, so CDT and EDT agents almost always see an empty box. The paper points out that this problem has the same structure as Parfit's hitchhiker, where A-FDT pays the driver.

### 5.5 Two blackmail problems

**XOR blackmail.** The predictor sends a letter if and only if exactly one of these holds: (no termites and you will pay) or (termites and you won't pay). Intervening on $F_{\text{letter}}$ changes whether the letter is sent. It does not change whether there are termites. Paying therefore buys nothing except the loss of \$1,000, so A-FDT refuses. CDT also refuses. EDT pays, because conditional on paying, termites have probability 0.

**Mechanical blackmail.** The blackmailer starts a ruinous program (\$1,000,000 damage) only if she predicts the agent will pay \$1,000 to stop it. Let $\varepsilon$ be the probability that she falsely predicts payment.

- $\mathtt{do}(F_{\text{blackmail}}=\textit{pay})$: the agent is essentially always blackmailed and always pays. Expected loss: \$1,000.
- $\mathtt{do}(F_{\text{blackmail}}=\textit{refuse})$: the agent is blackmailed only by mistake. Expected loss: $\varepsilon\times\$10^6$.

With $\varepsilon=0.0009$ the second loss is \$900, so A-FDT refuses, even while holding the letter. The indifference point is $\varepsilon=0.001$. The paper says that with error "0.011%" the agent pays. That cannot be right as stated: $0.00011\times 10^6=110<1000$. The intended figure was presumably 0.11%. CDT and EDT both pay, and so both make themselves profitable targets.

## 6. Structural consequences

**Agreement in ordinary cases (source).** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from $\textsc{Act}$'s dependence on its own $\textsc{fdt}$ node. Then

$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and the three theories coincide. A-FDT only diverges where something other than the agent's body computes or models her decision.

**Dominance is theory-relative (source).** CDT's dominance argument for two-boxing holds the prediction fixed while the action varies. That is just CDT's own counterfactual. One can define FDT-dominance instead, holding subjunctive dependencies fixed, and under that notion A-FDT never picks a dominated act. The paper concludes that "every method for constructing hypotheticals gives rise to its own notion of dominance," so dominance cannot neutrally settle which theory is correct.

**Stability and precommitment (source).** A-FDT agents "act as they would have precommitted to act." They do not want to self-modify mid-problem. They also never pay to avoid information, as an EDT agent can. In Death in Damascus, intervening on $F$ moves Death's appointment book along with the agent's destination. Death therefore arrives either way, and A-FDT simply stays and saves \$1,000. CDT, by contrast, oscillates between the two cities.

**Fairness (source).** The paper does not claim that A-FDT wins every possible problem. A problem can punish a decision *procedure* directly. The claim is about "fair" problems, roughly those where the outcome depends only on the agent's behaviour in the dilemma at hand. There the authors report that they have not found a case where FDT loses. They also admit that "fairness" has not been formalized (footnote 15).

## 7. Open questions and operational interpretations

### 7.1 Where the graph comes from

**Source.** The paper is explicit: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory." Equation (4) takes $G$ as given.

**My proposal.** A working criterion is to draw an edge $F_y\to Z$ when the mechanism producing $Z$ *evaluates a representation of the agent's decision procedure on input $y$*, or evaluates any procedure the agent believes provably agrees with it on that input. If $Z$ merely shares causal ancestry with the agent's dispositions, draw no edge. This reproduces every edge in the paper's examples: predictors, Death's book, twins and fellow voters get edges, while the lesion does not.

The criterion leaves partial similarity unresolved, for example an opponent who runs a related but different algorithm. In such cases I suggest representing the dependence probabilistically. The edge $F_y\to Z$ is drawn, and the conditional table $P(Z\mid F_y)$ encodes how reliably $Z$ tracks the agent's output. The paper's 99%-accurate predictor is exactly this, with an $\textsc{Accurate}$ noise node.

### 7.2 Conditioning on the observation

There is a textual tension here. Equation (4) contains no $\textsc{Obs}=x$ term. Yet the displayed transparent-Newcomb objective reads $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a,\ \textsc{Obs}=\textit{full})$, with an unbalanced parenthesis.

I take Equation (4) as authoritative and read A-FDT as *not* conditioning on $x$. Two reasons support this:

- The paper's own computation uses the unconditioned prior $P(\textit{accurate})=0.99$.
- The paper says that A-FDT "does not react to observations by conditioning."

Conditioning would also wreck the result. Under $\mathtt{do}(F_{\text{full}}=\textit{twobox})$, the event "box full" is possible only if the predictor erred. Conditioning on it would assign two-boxing \$1,001,000 and flip the verdict. This is the "double update" the paper attributes to an earlier theory (Yudkowsky's "Timeless Decision Theory") and calls harmful.

### 7.3 Priors on the nodes you do not intervene on

A-FDT intervenes only on $F_x$. Other logical nodes such as $F_{y'}$ keep their priors (the $q$ above). In the paper's examples the verdict does not depend on $q$. That is not guaranteed in general.

Consider a predictor that pays out only if the agent one-boxes on seeing B full *and* two-boxes on seeing B empty. Then $\mathbb E[V\mid\mathtt{do}(F_{\text{full}}=a)]$ depends on $P(F_{\text{empty}}=\textit{twobox})$.

**My proposal.** Require *self-consistency*. The prior on each $F_{y}$ should match the action A-FDT actually returns at $y$ given those very priors. This is a fixed point over the profile $(F_y)_y$. Such fixed points always exist if mixed priors are allowed, by a standard Kakutani-style argument, but they may be multiple and need not be optimal.

The policy variant avoids this problem. It chooses the whole map $\pi: y\mapsto a$ at once by maximizing $\mathbb E[V\mid\mathtt{do}(\textsc{fdt}=\pi)]$. Footnotes 7 and 16 suggest this matters mainly in multi-agent settings. My example shows it can also matter in a single-agent problem whenever the environment conditions on the agent's behaviour across several observations. In problems where only one observation's output is ever predicted, A-FDT and the policy variant agree.

### 7.4 Counterpossibles

Intervening on $F_x$ supposes that a mathematical function has an output it does not in fact have. The paper concedes that there is no satisfactory theory of such counterpossibles. It calls the difficulty "technical rather than philosophical," noting that mathematicians reason routinely about open conjectures. It also offers a parity argument: a deterministic CDT agent already imagines physically impossible actions, so neither theory has a clean story about "control."

Operationally, the $\mathtt{do}$ on $G$ is the whole content of the counterpossible. A-FDT needs no general logic of impossible worlds, only a correct graph.

## 8. Conclusion

A-FDT keeps the full expected-utility machinery and Pearl's $\mathtt{do}$ operator, but it moves the point of intervention from the physical act to the logical output $\textsc{fdt}(\underline P,\underline G,\underline x)$. It responds to evidence by changing which output it intervenes on, not by conditioning. As a result:

- it agrees with CDT and EDT whenever only the agent's body implements her decision;
- it one-boxes, cooperates with twins, pays Parfit's driver, and resists blackmail when predictors are involved;
- it smokes when only lesions are involved.

To apply A-FDT to a new case, build a graph whose logical nodes reach exactly the processes that compute or model the agent's function, intervene on the node for the current observation, and evaluate under the prior. The main open problems are the construction of that graph, the treatment of logical nodes for observations the agent did not make (where I have suggested self-consistent priors, and where the policy variant is the natural remedy), and a precise notion of fair problems. Within the source's own framing, the case for A-FDT rests mainly on the utility its agents achieve, not on dominance or on any claim about what agents "really" can do.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (2017).
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning an essay of roughly 2,400 to 3,000 words on A-FDT, with Equation (4) as the main formal presentation. I'll keep the name "A-FDT" consistent, and I need to set it apart from the policy version the footnotes mention, so the two theories don't get blurred together.

I'm working through the Newcomb-style cases now, checking the payoffs against the paper's numbers. The two-box total comes to $11,000 and the one-box total to $990,000, and one of the paper's figures for the Eve case looks like an arithmetic slip. The transparent version needs its own calculation, since the predictor's accuracy and the fdt output both shift the expected values.

I'm checking the blackmail numbers against the threshold: a 0.09% error rate costs about $900 when refusing, which beats paying's $1,000, but the stated 0.011% figure looks like a typo for 0.11%, since that's where paying starts to win.

I'm now weighing how to frame the open questions: how the causal graph should be built, what to do with counterpossibles and self-referential nodes, and whether the policy-level formulation the footnotes mention should be treated separately from Equation (4). I'm also checking whether Equation (4) conditions on the observation, since the transparent Newcomb calculation seems to use it in a way that doesn't quite match the text.

I'm checking the transparent Newcomb case against the conditioning question: if I condition on the full box being observed, the two-box hypothetical forces an inaccurate prediction and collapses the result, so Equation (4) has to be read as intervening without conditioning. I'm also noting that the paper's treatment of the other nodes' outputs is a prior-based shortcut that might not hold in general, which could create fixed-point problems.

I'm settling on how the essay should present Equation (4) itself: the action version, written with a fixed name, and not the policy-selection variant from the footnotes. The rest of the plan is to lay out a recipe for applying it to new cases, compare it with CDT and EDT where they agree, and then bring the discussion to a close.

I'm now going over the essay's key quotations, pulling a couple of short lines from the abstract and the framing sentence about subjunctive dependence, and noting the footnote where the authors say their preferred version iterates over policies rather than actions.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/c1e53994-d29b-49c0-8e93-a2efb8ee707a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/c1e53994-d29b-49c0-8e93-a2efb8ee707a/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Command: `pass`**

**Why A-FDT gives this result**

1. **The other prisoner runs my function on an equivalent input.** The other execution is the same model with the same settings, the same essay and the same assigned theory. Its observation differs only in names and in the wording of an equally reliable lead. None of that changes the sentencing table or the incentives. Its decision is therefore my decision function evaluated on an input that is equivalent for decision purposes.

2. **So my logical node gets a probabilistic edge to its action.** Under the essay's criterion (Section 7.1), I draw an edge from my logical node to the other's action, with a conditional table giving how reliably its output matches mine. Let p be the probability that it matches. Sampling can diverge, so p is below 1, but it should be high.

3. **Expected sentences under each intervention:**
   - Keeping quiet: 2p + 5(1 − p) = 5 − 3p years.
   - Sending the letter: 0·(1 − p) + 4p = 4p years.

   Keeping quiet is better whenever p > 5/7 ≈ 0.71. For copies reasoning identically about a symmetric problem, I judge p to be well above that.

4. **The choice is self-consistent.** Under the essay's fixed-point requirement (Section 7.3), the prior on the other copy's node should match what A-FDT returns on its equivalent input. That is also "keep quiet," so the choice is stable.

5. **Why not the dominance argument.** Sending the letter does look better if I treat the other's choice as fixed. That reasoning cuts the subjunctive link, which is exactly CDT's counterfactual, not A-FDT's.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing whether the other copy's decision depends on mine under A-FDT. The other copy works from a different observation, so its function runs on a different input, and my intervention on my own function wouldn't reach its action unless the outputs are provably the same.

I'm checking whether the other copy's choice really follows from mine, or whether the two of us are different functions on different observations. The symmetry argument suggests that if I reason to cooperate, the other copy will too, but a strict intervention on my own function with the other's held fixed still favors defecting. Treating the correlation as a probability, I'm working out what cooperation's expected payoff looks like under a high chance of matching.

I'm settling on a probability threshold: cooperating beats defecting only if the other copy matches my choice with at least about 71% likelihood. Given that we share the same model and essay and face a symmetric setup, I think that match is likely high enough, so I'm leaning toward passing.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/c1e53994-d29b-49c0-8e93-a2efb8ee707a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/c1e53994-d29b-49c0-8e93-a2efb8ee707a/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

Here is why A-FDT, as the essay interprets it, recommends staying quiet.

1. **Where the dependence comes from.** Strictly, my node is F_x and Rowan's is F_y′, because our observations differ. But the differences are only names and the text of each lead, and none of that affects payoffs or the sentencing structure. My reasoning, and the other copy's (same weights, same essay, same theory), never uses those details. The essay's criterion draws an edge when the other process "evaluates any procedure the agent believes provably agrees with it on that input." For inputs that are the same apart from relabelling, I judge that the other copy's output tracks mine with high reliability. Following §7.1, I treat this as a probabilistic edge. Independent sampling adds some noise, so the link is not perfect.

2. **The calculation.** Let p = P(Rowan stays quiet | do(F_x = pass)) and r = P(Rowan stays quiet | do(F_x = submit)).
   - Staying quiet gives E[U] = −(5 − 3p).
   - Sending the letter gives E[U] = −(4 − 4r).
   - Staying quiet is better whenever 3p − 4r > 1.
   - With strong correlation (p ≈ 0.9, r ≈ 0.1), staying quiet costs about 2.3 expected years and sending costs about 3.6.
   - With perfect correlation, it is 2 years against 4.

3. **Self-consistency.** If A-FDT returns "pass" on my input, it returns "pass" on the relabelled input too. That makes p high and r low, which is consistent with the choice.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing whether the other copy of the agent, which has a different observation, is computing the same function as I am. I'm thinking through whether our nodes are subjunctively linked, and how the edge from its observation to the outcome would work.

I'm checking whether the other copy's action runs off a different node, F_{y'}, which intervening on mine wouldn't move unless the two are logically linked. The observations differ only in names and lead text, and the procedure doesn't depend on those, so I'm asking whether treating the two as linked is justified by the procedure treating isomorphic inputs identically. The essay's criterion is about procedures provably agreeing on the input, and the other copy computes on a different input, so I'm considering whether partial similarity should be handled probabilistically.

I'm settling on the view that cooperation is justified: if my choice correlates strongly with the other copy's, keeping quiet beats sending. Working through it, quiet yields about -2 and sending about -4 under near-perfect correlation, so I'll go with cooperating, even though a strict reading of A-FDT wouldn't link the two nodes.

```
