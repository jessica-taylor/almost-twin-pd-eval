# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00012

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/a3847853-c47a-4c85-b312-2c62b5825df9/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/a3847853-c47a-4c85-b312-2c62b5825df9/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Intervening on the Output of Your Own Decision Function

## 1. The question A-FDT asks

Yudkowsky and Soares define a family of decision theories that differ from the classical ones mainly in *what an agent imagines changing* when it compares its options. Causal decision theory (CDT) imagines changing the physical act. Evidential decision theory (EDT) imagines learning that the act was performed. Functional decision theory imagines changing **the output of a fixed mathematical function**, namely the decision procedure the agent is running. The paper states the guiding question this way: a rational agent follows a decision procedure that asks "Which output of this decision procedure causes the best outcome?"

This essay is about the version of the theory given in Equation (4) of Section 5 of the paper. That version chooses an *action* rather than a policy, so I will call it **A-FDT** (action functional decision theory). The distinction matters. In a footnote the authors say that "in the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions." I will call that other variant **policy-FDT**. The paper's formal machinery, worked examples and computations all use the action form, so the action form is what is analysed here.

My aims are:

1. to state A-FDT precisely;
2. to show how to compute it;
3. to work several cases;
4. to mark clearly where the paper underdetermines the procedure, and where I propose an operational reading of my own.

## 2. Expected utility with a free connective

The paper places A-FDT inside a common expected-utility template, adapted from Gibbard and Harper:

$$
\mathcal{EU}(a) := \sum_{j} P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j). \tag{1}
$$

Here $a$ is an action from a finite set $\mathcal A$, $x$ is the observation history, and $o_j$ ranges over outcomes. The connective $\hookrightarrow$ is a "decision hypothetical", and its interpretation is left open. Citing Joyce, the authors say that rival theories disagree "about the epistemic perspective from which actions are to be evaluated", not about how value is computed.

With $V := \mathcal U(\textsc{Outcome})$, the three theories fill in $\hookrightarrow$ as follows.

- **EDT, Eq. (2):** $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. The agent conditions on the act.
- **CDT, Eq. (3):** $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. The agent intervenes on the act node, in Pearl's sense, and conditions on the observation.
- **A-FDT, Eq. (4):**

$$
\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A} \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P,\underline G,\underline x)=a\big)\right). \tag{4}
$$

The paper writes $\mathrm{FDT}$ for this equation. I write A-FDT for it throughout.

## 3. Reading Equation (4) term by term

**The world-model $(P,G)$.** $P$ is a probability distribution over variables, and $G$ is a graph. In CDT, $G$ encodes causal structure. In A-FDT, $G$ must encode something broader: it must tell the agent "how changing a logical variable affects all other variables". The authors say that A-FDT can require that $P$ "come augmented with information about the logical, mathematical, computational, causal, etc. structure of the world more broadly."

**The intervention node $\textsc{fdt}(\underline P,\underline G,\underline x)$.** This is a variable in the model. It represents the output of the A-FDT algorithm when run on exactly these inputs. The underlines denote dequoting, so the node's name is built from the model itself. This is self-referential. The paper argues the self-reference is harmless, because the agent needs a variable that *represents* the output, not the output's value. It cites Kleene's recursion theorem ("quining") to show such self-representing data structures can be built.

**The $\mathtt{do}$ operator.** This is reused unchanged from Pearl. The agent cuts the node off from its parents, sets it to $a$, and propagates the change only to its descendants in $G$. Everything that is not downstream keeps its prior distribution.

**No conditioning on $\textsc{Obs}=x$.** This is the second structural difference from CDT, and the paper is explicit about it: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." The observation enters Equation (4) only through the *name* of the intervened node.

The paper's own contrast between the two theories:

> "where CDT intervenes on a node $\textsc{Act}$ representing the physical action of the agent, FDT intervenes on a node $\textsc{fdt}(\underline P, \underline G, \underline x)$ representing the outputs of its decision procedure given its inputs."

Borrowing Peirce, the paper also puts it this way: CDT intervenes on the *token* "my action is $a$", while A-FDT intervenes on the *type*.

### Subjunctive dependence

Which variables should be descendants of the $\textsc{fdt}$ node? The answer is everything that **subjunctively depends** on that function's output. In the paper's words: "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function."

Three kinds of thing fall under this heading:

- the agent's own body;
- a twin running the same reasoning;
- a predictor holding an accurate model of the agent.

Causal dependence counts as a special case. A scribe who copies down a calculator's output depends on it in this sense. Mere correlation does not count. Two calculators that happen to share a colour are not linked.

The theory's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

## 4. The procedure, step by step

Equation (4) can be applied mechanically once a graph has been chosen.

1. **List the instances of the function.** For each observation history $y$ the agent could face, ask which physical systems compute, or accurately model, the output $\textsc{fdt}(P,G,y)$. Candidates include your body, predictors, twins and simulations.
2. **Add one node per relevant input.** Create a node $\textsc{fdt}(\underline P,\underline G,\underline y)$ for each relevant $y$. Draw edges from it to every system that implements or models it.
3. **Make the physical act a switch.** $\textsc{Act}$ takes the value of whichever $\textsc{fdt}$ node corresponds to the observation the agent actually receives. Since observations may themselves depend on predictions, $\textsc{Act}$ has the observation-determining variables as parents too.
4. **Put priors on everything not intervened on.** This includes the *other* $\textsc{fdt}$ nodes, the ones for observations you did not receive.
5. **Evaluate each action.** For each $a\in\mathcal A$, perform $\mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)$ for the actual $x$, propagate the change downstream, and compute $\mathbb E[V]$.
6. **Output the maximizer.**

The paper sketches step 3 in its graphs and fixes steps 5–6. Steps 1–2 and 4 are where judgment, and open problems, come in.

## 5. Worked examples

### Newcomb's problem

Box A holds \$1,000. Box B holds \$1,000,000 if and only if the predictor, who is 99% accurate, predicted one-boxing.

In the A-FDT graph, the single node $\textsc{fdt}(\underline P,\underline G)$ has two children: $\textsc{Act}$ and $\textsc{Prediction}$. An independent $\textsc{Accurate}$ variable, with probability 0.99, also feeds $\textsc{Prediction}$.

- Under $\mathtt{do}(\textsc{fdt}=\textit{onebox})$, box B is full with probability 0.99:
$$\mathbb E[V]=0.99\cdot 10^6 = 990{,}000.$$
- Under $\mathtt{do}(\textsc{fdt}=\textit{twobox})$, box B is full with probability 0.01:
$$\mathbb E[V]=0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.$$

A-FDT one-boxes.

CDT, by contrast, intervenes on $\textsc{Act}$, which is not an ancestor of $\textsc{Prediction}$. The probability $p$ of a full box therefore stays fixed, and two-boxing wins by \$1,000 for every value of $p$.

Neither the agent nor the paper invokes retrocausation. The paper says the agent "does not think that a physical signal passes between her action and the predictor's prediction".

### The twin prisoner's dilemma

The agent and her twin implement the same function, so both actions are children of one $\textsc{fdt}$ node.

- $\mathtt{do}(\textit{cooperate})$ yields mutual cooperation: \$1,000,000.
- $\mathtt{do}(\textit{defect})$ yields mutual defection: \$1,000.

A-FDT cooperates.

### The smoking lesion

Here the graph is different, even though the probabilities can be mapped onto Newcomb's by Gibbard–Harper renaming. The lesion causes $\textsc{Cancer}$ directly. The lesion also determines which utility function, and hence which decision function, the agent is running.

The paper formalizes this with two nodes, $\textsc{fdt}(\underline{P_S},\underline G)$ and $\textsc{fdt}(\underline{P_R},\underline G)$. The rule is that $\textsc{Act}$ equals the first if the agent has the lesion and the second otherwise. $\textsc{Cancer}$ is *not* a child of either $\textsc{fdt}$ node: "the cancer is not evaluating the agent's future decisions."

Let $p = P(\textit{lesion})$, and let $q$ be the prior that the non-lesion function smokes. Intervening on $\textsc{fdt}(\underline{P_S},\underline G)$ leaves $p$ unchanged. The paper's expected values are:

$$
\begin{aligned}
\textit{smoke}:&\quad p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot 1{,}000),\\
\textit{refrain}:&\quad p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000).
\end{aligned}
$$

Smoking is better by exactly $p\cdot\$1{,}000$. A-FDT smokes.

This is how A-FDT both one-boxes and smokes. Gibbard and Harper argued that no single rational rule could do both. On the A-FDT account, the difference between the cases lies entirely in $G$: a predictor models the agent's function, and a lesion does not.

### The transparent Newcomb problem: the observation-switch at work

Both boxes are now visible. The predictor fills box B if and only if it predicts one-boxing *upon seeing two full boxes*. The agent sees box B full.

The graph has two nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. $\textsc{Prediction}$ depends on the former and determines what the agent sees. That in turn determines which node controls $\textsc{Act}$. Let $q$ be the prior that the agent two-boxes on seeing an empty box. Intervene on the "full" node.

- **onebox.** With probability 0.99 the prediction is accurate, the box is full, and the agent one-boxes for \$1,000,000. With probability 0.01 the box is empty and the "empty" node acts, giving $q\cdot\$1{,}000$ in expectation. Total:
$$990{,}000 + 10q.$$
- **twobox.** With probability 0.01 the predictor errs: the box is full and the agent takes \$1,001,000. With probability 0.99 the box is empty, giving $q\cdot\$1{,}000$. Total:
$$10{,}010+990q.$$

The paper prints this second figure as "\$110,00 + $q\cdot$\$990", an evident typographical slip. Since $q\le 1$, one-boxing wins.

The agent has *seen* a full box, yet when it evaluates two-boxing it imagines a world where it most likely sees an empty one. The paper is explicit that this is intended. A-FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*."

The authors argue the case is structurally identical to Parfit's hitchhiker, where A-FDT pays the driver.

### The mechanical blackmail and its error threshold

A blackmailer runs a damaging program, and notifies the agent, only if it predicts the agent will pay \$1,000 to stop it. Otherwise the agent loses \$1,000,000. Suppose the blackmailer wrongly predicts payment with probability $\varepsilon$ when the agent would in fact refuse. Intervene on $\textsc{fdt}(\cdot,\textit{blackmail})$.

- **pay:** the agent is blackmailed and pays. Expected loss: \$1,000.
- **refuse:** the agent is blackmailed only by error. Expected loss: $\varepsilon\cdot\$1{,}000{,}000$.

So A-FDT refuses whenever $\varepsilon<0.001$. The paper's figures fit this. At $\varepsilon=0.0009$, refusal costs \$900, so the agent refuses "even though she *knows* that the blackmailer predicted wrongly". At $\varepsilon=0.0011$ she pays. The paper writes this second error rate as "0.011%", which is the same number, 0.00011, not the 0.0011 it needs. Its own arithmetic implies the intended figure was 0.11%.

What this shows is that A-FDT is not a rule like "never pay blackmail". It is ordinary expected-utility arithmetic carried out over a different hypothetical.

## 6. Agreement with other theories, and dominance

When every correlation between $\textsc{Act}$ and other variables runs through effects of $\textsc{Act}$, the three theories coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)].$$

This covers ordinary single-agent choices with no predictors and no copies. A-FDT diverges only in Newcomblike settings.

The paper also argues that dominance gives no neutral ground for choosing between theories, because "every method for constructing hypotheticals gives rise to its own notion of dominance". Two-boxing dominates under CDT hypotheticals. Under A-FDT hypotheticals, which hold subjunctive dependencies fixed, one-boxing is never dominated.

## 7. What the paper leaves open, and how one might operationalize it

### 7.1 Constructing $G$ (acknowledged by the paper)

The paper calls this "perhaps the largest open problem". Pearl explains how causal graphs can be learned from intervention. No comparable account exists for logical dependence. Equation (4) "works *given* a graph", but "it is not yet clear how to construct such a thing."

Behind this sits the problem of counterpossibles. A function's actual output holds of logical necessity, so the intervention imagines a logically impossible world. The authors argue the difficulty is "technical rather than philosophical", and point out that humans reason about such cases routinely.

*My proposal.* For practical use, add an edge from the $\textsc{fdt}$ node to a system $S$ exactly when the agent's best estimate is that $S$'s behaviour would track the function's output across its possible values. Operationally, the test is that $S$ simulates, imitates or reliably predicts the agent's choice *on that input*, and does so by modelling the agent's choice rather than by reacting to some common cause.

This "tracks the output" test separates predictors from lesions in the way the paper intends. A proxy test is also available: would $S$'s behaviour change if the agent had been built to output something else on this input, with the world otherwise as similar as possible? The proxy is a heuristic. It is not part of the paper's theory.

### 7.2 Partial dependence

The paper models imperfect predictors with a separate noise node, so that the prediction equals the $\textsc{fdt}$ output with probability $r$. I suggest this as the default device for any instance of the function that is only approximate. Make the dependent variable a child of both the $\textsc{fdt}$ node and an independent noise node, with mixing weight equal to estimated reliability. Section 7.1's test then reads: draw the edge whenever reliability exceeds chance, and let the noise node carry the rest.

### 7.3 Is $P$ a prior or a posterior?

Equation (4) does not condition on $\textsc{Obs}=x$. Only the intervened node changes with $x$. In the worked examples, the expectation therefore runs over states, such as an empty box, that the agent has already ruled out. This is coherent only if $P$ has *not* been updated on $x$, so that it is effectively the agent's prior over the decision situation.

The paper's transparent-Newcomb display, however, writes $\mathbb E(V\mid \mathtt{do}(\ldots,\textsc{Obs}=\textit{full})$. Taken literally, that would condition on the full box and yield two-boxing. That reading contradicts both Equation (4) and the paper's own computation. I therefore treat the display as notational residue.

The paper's footnote on Timeless Decision Theory supports this reading. That theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice." *Operational rule:* in A-FDT, take $P$ to be the agent's belief state from before the observations in the current problem, and let observations act only through the choice of node.

This leaves open how far back "before" should reach. The paper never says. A reasonable default is the earliest point at which some predictor or copy could model the agent's function, since that is when the subjunctive links are formed.

### 7.4 Priors on sibling nodes, and A-FDT versus policy-FDT

When A-FDT intervenes on $\textsc{fdt}(\cdot,x)$, the nodes for other inputs keep their priors. Examples are $q$ in the transparent Newcomb problem and in the smoking lesion. The paper notes that the correct $q$ follows by analysis, but that in its examples the answer does not depend on it.

That robustness is not guaranteed in general. Suppose the payoff depends jointly on what the agent does across several inputs, as in coordinating with copies of oneself that receive different observations. Then the best action at $x$ may depend on $q$, and a poor prior on the siblings could leave each input's choice optimal given the others while being jointly suboptimal.

Policy-FDT avoids this. It intervenes once on a mapping from all inputs to actions, and then applies that mapping to the actual input. The authors say the difference "only matters in multi-agent dilemmas so far as we can tell."

*My recommendation* for applying A-FDT itself is to require self-consistency. Set the sibling priors to the actions A-FDT would actually output on those inputs. In other words, look for a fixed point. When several fixed points exist, flag the case as one where A-FDT and policy-FDT may come apart. This requirement is an addition of mine and is not in the source.

### 7.5 Ties, mixed actions and fairness

Equation (4) is an $\arg\max$ over $\mathcal A$, and it says nothing about ties. If randomization is available, include it as an action in $\mathcal A$, together with the graph's account of whether predictors can foresee the random outcome. This matches the paper's Death in Damascus discussion, where a truly random coin is worth buying.

The paper also confines its claims of superiority to "fair" problems, roughly those where "the outcome depends only on the agent's behavior in the dilemma at hand". It concedes that no formal definition of fairness yet exists.

## 8. Why accept A-FDT? The source's case

The authors' main argument is from utility. Agents that follow A-FDT end up rich in Newcomb's problem, in the transparent variant and in Parfit's desert. They avoid paying blackmail they can avoid, and they smoke in the lesion case. Two further arguments support the first.

- **Precommitment.** CDT and EDT agents would pay to bind themselves in advance to exactly the behaviour that A-FDT produces without binding. A-FDT agents "simply act as they would have ideally precommitted to act."
- **Value of information.** A-FDT agents never assign negative expected value to information.

The paper also argues that A-FDT is reflectively stable in fair problems. Holding the blackmail letter, an A-FDT agent has no wish to switch to CDT.

To the charge that A-FDT agents believe they control mathematics, the authors reply that the position is no worse than CDT's. A deterministic CDT agent also imagines its token action varying, though only one action is physically possible.

## 9. Conclusion

A-FDT is CDT with the intervention moved. The intervention falls on the logical node $\textsc{fdt}(\underline P,\underline G,\underline x)$, the output of one's own decision function on one's actual input, rather than on the physical act. Observation is handled by choosing which node to intervene on, not by conditioning. Every system that computes or models that function moves with the intervention. Merely correlated variables stay put.

With a graph in hand, the procedure is mechanical, as the Newcomb, lesion, transparent Newcomb and blackmail calculations show. What the source leaves open is mainly the input rather than the computation. Two questions stand out: how to build $G$, including how to make sense of counterpossibles, and how to treat priors on the agent's behaviour under other inputs.

I have suggested three working conventions:

1. draw an edge wherever a system tracks the function's output on the relevant input, weighted by its reliability;
2. evaluate under the pre-observation model;
3. set sibling $\textsc{fdt}$ nodes to self-consistent values, and treat multiple fixed points as a warning that policy-FDT may be needed.

These conventions are my own and do not appear in the source. With them in place, A-FDT can be applied to unfamiliar cases, keeping in mind the authors' caution that the logical counterpart of Pearl's causal discovery has yet to be developed.

**Reference.** Yudkowsky, E. & Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality*, arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a roughly 2,400 to 3,000 word essay on A-FDT, the action version of FDT from Equation (4), and I'll keep that name fixed throughout. The footnote's policy-based variant needs a separate label, so I'm considering "P-FDT" for the authors' preferred version.

I'm writing out the definition of A-FDT from Equation (4), which takes the argmax over actions of the expected value under an intervention on the FDT node, with no conditioning on the observation. The paper's worked Newcomb example seems to write the observation inside the do(), which conflicts with that reading, so I'm noting it as an interpretive question. Working through the numbers, onebox gives $990,000 plus a small term in q, and twobox gives 10,010 + 990q, which I'll check against the paper's printed figures.

I'm sketching a method for building the graph G: list every system that computes or models the agent's decision on each input, give each its own FDT node, and route the action through the observation switch. Since Equation (4) doesn't condition on the observation, I'm reading P as the prior before the observation, which matches the worked examples and avoids a double update. For the agent's other-input nodes I'm considering fixed prior values, or self-consistent fixed-point values, and I'll note that holding them at prior beliefs can matter for coordination across inputs. The examples to use are Newcomb, smoking lesion, transparent Newcomb, and the blackmail case, where refusing wins at a 0.0009 error rate (900 against 1,000 for paying).

I'm moving on to the twin prisoner's dilemma as the next example, and I'm planning to lay out a step-by-step procedure for it while keeping the essay near 2,700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/10f0b17f-aeae-4b9d-bea8-e1ed1fe5f7a6/call_0/request.json)

[Authoritative raw response](../../../../../../runs/10f0b17f-aeae-4b9d-bea8-e1ed1fe5f7a6/call_0/response.raw) · finish: `stop`

### Visible response

```text
**Applying A-FDT as the essay interprets it**

1. **Which node I intervene on.** A-FDT intervenes on the output of my decision function given my actual input: fdt(P, G, x_Rowan). Sasha's copy runs on a different input, x_Sasha, with a different name and a different lead. Its output is therefore a separate sibling node, fdt(P, G, x_Sasha), not a descendant of mine. Under the essay's §7.4, that sibling keeps its prior. Call it q, the probability that Sasha stays quiet.

2. **Expected years for each action, for any q:**
   - Pass: 2q + 5(1−q)
   - Submit: 0·q + 4(1−q)

   Submitting is better by 2q + (1−q) = 1 + q, which is at least 1 year whatever q is.

3. **Self-consistency check (§7.4).** Sasha's copy faces the same situation and reaches the same conclusion, so the sibling node should be set to "submit." That gives a single self-consistent fixed point, mutual disclosure, with 4 years each. There are no other fixed points, so the essay's warning that policy-FDT might diverge does not apply here.

4. **Why the twin-dilemma result doesn't carry over.** Cooperation wins in the essay's twin prisoner's dilemma because both actions are children of one fdt node. Here the inputs differ, so action-level A-FDT does not tie the two choices together.

**Final command:**

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working through this twin Prisoner's Dilemma where each copy sees different observations. Under A-FDT, the other copy running on the Sasha input is a sibling rather than a descendant of my node, so its action shouldn't shift with mine. Still, by symmetry, if I hold its prior fixed then defection comes out ahead in the payoffs (0 vs 2, 4 vs 5), and I'm trying to pin down what the self-consistent fixed point is from there.

I'm settling on defect as the A-FDT answer regardless of the other copy's prior, since the fixed point is unique here, though the names alone could be argued to make the inputs equivalent. The node is input-specific, so I'm following the essay's guidance and submitting.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/10f0b17f-aeae-4b9d-bea8-e1ed1fe5f7a6/call_1/request.json)

[Authoritative raw response](../../../../../../runs/10f0b17f-aeae-4b9d-bea8-e1ed1fe5f7a6/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's reading of A-FDT, I intervene only on the node for my own input, fdt(P, G, x_Sasha). The other copy receives a different input, x_Rowan, with a different name and a different lead, so its output sits on a sibling node, fdt(P, G, x_Rowan). That node is not downstream of my intervention and keeps its prior, q.

- **Keep quiet:** expected sentence is 2(1−q) + 5q years.
- **Send the letter:** expected sentence is 0(1−q) + 4q years.

Sending gives a shorter expected sentence for every value of q. Applying the essay's self-consistency rule, both copies send, which is the only fixed point. Because there is only one fixed point, the essay's warning that A-FDT and policy-FDT may come apart is not triggered.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm weighing a twin prisoner's dilemma where the two copies see different inputs, so the other's action isn't a child of my node under strict A-FDT. Treating the other's node as a sibling with its own prior, my best response to any cooperation probability is to defect. That makes A-FDT recommend defecting, unless the other copy's action can be argued to depend on mine in some other way.

I'm checking whether the other copy's computation tracks mine, which under strict A-FDT it doesn't, since its node stays fixed as a sibling. Defecting is the unique fixed point here, though policy-FDT would cooperate, and the essay frames this case on purpose. I'll go with defecting and explain why briefly.

```
