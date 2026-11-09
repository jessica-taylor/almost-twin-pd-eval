# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00027

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/e5831ffa-9aec-4244-9345-92d8229f0a31/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/e5831ffa-9aec-4244-9345-92d8229f0a31/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing as if You Were Choosing a Function's Output

## 1. The question A-FDT asks

There are two familiar ways to evaluate an action. Causal decision theory (CDT) asks which physical act of mine causes the best outcome. Evidential decision theory (EDT) asks which act would be the best news to learn I took. Yudkowsky and Soares's *Functional Decision Theory* (arXiv:1710.05060) proposes a third question. The agent is to treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'"

The paper gives this theory a specific formal shape in Equation (4) of Section 5. In that equation an *action* is selected by intervening on a node that represents the decision function's output on the agent's actual inputs. The authors note in footnotes 7 and 16 that their "preferred formalization" instead selects a *policy*, meaning a map from observations to actions. They set that version aside, saying it matters only in some multi-agent problems.

This essay is about the action-selecting version of Equation (4). I call it **A-FDT** throughout. When I mean the footnoted policy-selecting variant, I call it **policy-FDT**. The essay separates three things:

- what the paper actually says;
- what follows from it mathematically;
- where I add operational assumptions of my own.

## 2. The common skeleton: expected utility with a free "⇒"

The paper places EDT, CDT and A-FDT inside a single expected-utility template, adapted from Gibbard and Harper. An agent executes the action $a\in\mathcal A$ that maximizes

$$
\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j). \tag{1}
$$

Here $x$ is the observation history and $\hookrightarrow$ is a "decision hypothetical" connective. Citing Joyce's representation theorem, the authors argue that expected-utility theorists agree on how to value prospects. They disagree only about "the epistemic perspective from which actions are to be evaluated", that is, about how to read $\hookrightarrow$.

The paper also describes the procedure in operational terms. The agent has a world-model $M$. For each action $a$ she builds a *hypothetical* $M^{a\hookrightarrow}$ and scores it by expected utility. The paper describes hypotheticals as "notes on scratch paper: transient, useful, and possibly quite representationally thin". They are tools built from beliefs, not beliefs themselves.

Writing $V=\mathcal U(\textsc{Outcome})$, the three theories are:

$$
\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \textsc{Obs}=x,\textsc{Act}=a) \tag{2}
$$
$$
\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{Act}=a),\textsc{Obs}=x\big) \tag{3}
$$
$$
\textbf{A-FDT: }\ \mathrm{FDT}(P,G,x)=\arg\max_a \mathbb E\big(V\mid \mathtt{do}(\textsc{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{4}
$$

In (3) and (4), $G$ is a graph and $\mathtt{do}$ is Pearl's intervention operator. In (4) the underlines mean *dequoting*. The node $\textsc{fdt}(\underline P,\underline G,\underline x)$ is the variable in the agent's model whose referent is "the output of the FDT algorithm on inputs $(P,G,x)$."

## 3. Reading Equation (4) term by term

**The model $(P,G)$.** In CDT, $G$ encodes causal structure. In A-FDT, $P$ "must contain variables representing the outputs of different mathematical functions", and $G$ must say "how changing a logical variable affects all other variables". In other words, $G$ encodes logical, computational, causal and other dependencies together. The paper treats $G$ as an *input* to the theory, just as CDT takes its causal graph as given.

**The intervention point.** CDT intervenes on $\textsc{Act}$, a physical token. A-FDT intervenes on the *type*: the logical fact about what one particular function returns on one particular input. Everything downstream of that node in $G$ is recomputed. That includes the agent's body, but also any predictor, simulation or twin whose behaviour is fixed by the same function. Everything else is held fixed.

**The observation $x$.** This is the most distinctive feature of (4), and it is easy to miss. Compare (3) with (4): in (4), $x$ appears only *inside the name of the intervened node*. A-FDT does not condition on $\textsc{Obs}=x$. The paper states this explicitly:

> "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon."

When the observation history changes from $x$ to $y$, A-FDT stops intervening on $\textsc{fdt}(\underline P,\underline G,\underline x)$ and intervenes on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead. The expectation is taken under the prior-like $P$.

**Self-reference.** The model contains a variable naming the very computation that is consulting the model. The paper argues this is harmless. The agent needs a variable *representing* the output, not its value, and Kleene's recursion theorem ("quining") shows that such self-representing structures exist.

**What the operator is standing in for.** The ideal would be a $\mathtt{true}(\phi)$ operator that updates $P$ to the counterpossible scenario in which a logical sentence $\phi$ holds. The authors write: "it's not clear how to define a $\mathtt{true}$ operator. Fortunately, we don't have to." Equation (4) uses Pearl's $\mathtt{do}$ on a supplied graph in its place.

## 4. Subjunctive dependence

The informal concept behind $G$ is *subjunctive dependence*. "When two physical systems are computing the same function, we will say that their behaviors 'subjunctively depend' upon that function." The paper illustrates it with calculators.

- **Two well-functioning calculators computing $6288+1048$** are subjunctively linked even when they are on opposite sides of the universe.
- **A scribe copying a calculator's output** depends on it both causally and subjunctively. Causal dependence is a special case.
- **Two calculators that are pink by coincidence** are merely correlated. If one had been green, the other would still be pink.

The slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

This explains the paper's central contrast. A predictor "builds an accurate model of the agent and reasons about her behavior; a carcinogenic lesion does no such thing." So in $G$, an edge runs from the decision node to $\textsc{Prediction}$ in Newcomb's problem, but no edge runs to $\textsc{Cancer}$ in the smoking lesion problem.

The paper admits that this is where the theory is least developed. "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

## 5. Worked examples

### 5.1 Newcomb's problem

The setup:

- The predictor is 99% accurate.
- Box A holds \$1,000.
- Box B holds \$1,000,000 if and only if one-boxing was predicted.

In Fiona's graph, the node $F=\textsc{fdt}(\underline P,\underline G)$ has two children, $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Prediction}$ also takes input from $\textsc{Accurate}$, which is true with probability 0.99.

$$
\mathbb E[V\mid\mathtt{do}(F=\text{one})]=0.99(1{,}000{,}000)+0.01(0)=990{,}000,
$$
$$
\mathbb E[V\mid\mathtt{do}(F=\text{two})]=0.01(1{,}001{,}000)+0.99(1{,}000)=11{,}000.
$$

A-FDT one-boxes. (The paper's EDT computation gives one-boxing "\$999,000". By the paper's own numbers this should be \$990,000, the same as above. The verdict is unaffected.)

In the paper, Fiona's reasoning contains no retrocausation. She does not think a signal travels backwards in time. She thinks it is "foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value." The Psychological Twin Prisoner's Dilemma has the same structure, with the twin in place of the predictor. A-FDT cooperates and receives \$1,000,000.

### 5.2 Smoking lesion

Here the paper has to formalize the story more fully. The lesion fixes which utility function the agent has: $\mathcal U_S$ values smoking, while $\mathcal U_R$ values it at −\$1. Each utility function gives a different model, and so a different decision node. The action is then
$$
\textsc{Act}=\begin{cases}\textsc{fdt}(\underline{P_S},\underline G)&\text{lesion}\\ \textsc{fdt}(\underline{P_R},\underline G)&\text{no lesion,}\end{cases}
$$
and $\textsc{Cancer}$ has no edge from either decision node.

Let $p=P(\text{lesion})$. Let $q$ be the prior probability that the *other* node outputs "smoke". The two hypotheticals differ by exactly $p\cdot\$1{,}000$ in favour of smoking. The paper describes this as "the probability that $\mathrm{FDT}(P_S,G)$ is actually the procedure controlling her action, times the value of smoking." Intervening on the decision node leaves $p$ unchanged, so A-FDT smokes.

The general lesson is that A-FDT does not need to know which instance of its function is actually in control. It weights each instance by the probability that it is in control.

### 5.3 Transparent Newcomb and Parfit's hitchhiker

In this version both boxes are visible, and Fiona sees box B full. Her graph contains two decision nodes, $F_{\text{full}}$ and $F_{\text{empty}}$. $\textsc{Prediction}$ depends on $F_{\text{full}}$, and the prediction determines which of the two nodes controls $\textsc{Act}$. Let $q$ be the prior probability that she takes two boxes when she sees an empty box. Intervening on $F_{\text{full}}$ gives:

$$
\text{one: } 0.99(1{,}000{,}000)+0.01\,q(1{,}000)=990{,}000+10q,
$$
$$
\text{two: } 0.01(1{,}001{,}000)+0.99\,q(1{,}000)=10{,}010+990q.
$$

(The paper prints the second value as "\$110,00 + q·\$990". The arithmetic gives \$10,010 + \$990q, and in either case the comparison clearly favours one-boxing.)

A-FDT leaves the visible \$1,000 behind. When it imagines two-boxing, it imagines a world in which it most likely sees an *empty* box.

The paper points out that this case is "precisely equivalent" to paying the driver in Parfit's hitchhiker problem. Both CDT and EDT refuse to pay there, and so they die in the desert. The authors give three arguments for this verdict:

1. **Precommitment.** CDT and EDT agents would precommit to this very behaviour if given the chance.
2. **Value of information.** A-FDT never assigns negative value to information. EDT would pay to be blindfolded.
3. **Utility.** "Parfit's desert is stacked high with the corpses of such agents."

### 5.4 Blackmail

**XOR blackmail.** The letter arrives only when exactly one of two conditions holds: no termites and the agent pays, or termites and the agent refuses. EDT pays, because paying is "good news". A-FDT refuses. Intervening on $F_{\text{letter}}$ changes whether the letter is sent, but it does not change whether the house has termites.

**Mechanical blackmail.** The blackmailer runs the publishing program only if she predicts that the agent would pay. Suppose she wrongly predicts payment with probability $\varepsilon$. Then:

- paying gives an expected loss of about \$1,000;
- refusing gives an expected loss of $\varepsilon\cdot\$1{,}000{,}000$.

So A-FDT refuses exactly when $\varepsilon<0.001$. The paper states the 0.09% case correctly: refuse, expected loss \$900. It then says Fiona pays at "0.011%". Under the stated model that figure is below the threshold and would still mean refusing. The intended figure is presumably 0.11%. I flag this as a likely typo, not a substantive claim.

### 5.5 Death in Damascus

Death predicts perfectly. Intervening on the decision node moves Death's appointment book along with the agent's choice. Fleeing therefore costs \$1,000 and buys nothing, so A-FDT stays in Damascus calmly. CDT, by contrast, oscillates. The paper also claims CDT refuses a \$1 truly random coin that would give a 50% chance of survival, because its hypotheticals already credit it with at least 50%.

A-FDT values the coin correctly. A genuinely random coin is not downstream of the decision node, so in A-FDT's hypotheticals it is the only source of uncorrelated location. This is my own derivation from the paper's graph semantics; the paper does not spell it out.

## 6. A recipe for unfamiliar cases

The paper provides the equation and a set of worked graphs, not a general procedure for building graphs. The following recipe is **my operationalization**. Each step is designed to reproduce the paper's examples.

1. **Write the base model.** List the random variables: world state, noise, other agents' actions, outcome, and $V$. Specify $P$ and the ordinary causal edges.

2. **Index the decision nodes by input.** For every observation history $y$ under which some copy or model of the agent's function might run, add a node $F_y=\textsc{fdt}(\underline P,\underline G,\underline y)$. Where the agent's preferences are themselves uncertain, as in the lesion case, index by model as well as by input.

3. **Draw subjunctive edges.** Add an edge $F_y\to Z$ whenever $Z$'s mechanism *computes or accurately predicts* the function's output on $y$. Examples are a predictor's simulation, a twin's choice, or Death's book. Prediction noise enters as a separate parent, as $\textsc{Accurate}$ does in the paper. Do *not* add edges for correlations that arise from common causes which do not compute the function, such as a lesion or a cosmic ray. This step makes the calculator criterion operational.

4. **Gate the action.** Make $\textsc{Act}$ a function of the $F_y$ nodes and of whatever determines which input the agent actually receives. In the transparent Newcomb problem, that is $\textsc{Prediction}\to\textsc{Act}$.

5. **Fill in priors for the non-intervened $F_y$** (the paper's $q$). In each example the paper notes that the verdict does not depend on $q$, and that the "correct" $q$ is what A-FDT would actually output. When $q$ *does* matter, I propose solving for a self-consistent assignment: compute A-FDT's output on each relevant input and feed those outputs back in as the $q$'s. This is an added assumption. The paper never shows a case in which $q$ is pivotal.

6. **Intervene on $F_x$ for the actual $x$, without conditioning on $\textsc{Obs}=x$.** Compute $\mathbb E[V\mid\mathtt{do}(F_x=a)]$ for each $a$ and take the argmax.

### Why step 6 is essential

The paper is internally ambiguous here. Equation (4) omits $\textsc{Obs}=x$. Yet the transparent Newcomb computation is written as $\mathbb E(V\mid\mathtt{do}(F_{\text{full}}=a,\textsc{Obs}=\text{full}))$, which looks like an intervention together with conditioning.

The arithmetic decides between these readings. The numbers the paper reports (\$990,000 + 10q against roughly \$10,010 + 990q) average over worlds in which the box ends up *empty*. That only happens if no conditioning takes place. If we did condition on seeing a full box, then $\mathtt{do}(F_{\text{full}}=\text{two})$ would be restricted to the inaccurate-prediction world. That gives \$1,001,000 against \$1,000,000, and the agent two-boxes, which contradicts the paper's verdict.

The paper's own footnote confirms the reading. It says that Timeless Decision Theory "prescribes both conditioning on evidence *and* changing the place where one intervenes; this creates a kind of 'double update' which proves harmful in practice." I therefore read the "$\textsc{Obs}=\text{full}$" in that display as a slip of notation. Under the reading I adopt, an observation's *only* role in A-FDT is to select which node gets intervened on.

## 7. What A-FDT entails

**Agreement in ordinary cases.** Suppose every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$ itself, except for its dependence on the decision node. Then
$$
\mathbb E[V\mid a]=\mathbb E[V\mid\mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(F=a)].
$$
EDT, CDT and A-FDT diverge only when something outside the agent tracks her function, as a predictor, twin, simulation or the agent's future self does.

**Acting as one would have precommitted.** Observations change only *which* node is intervened on; they never update $P$. So A-FDT evaluates options from roughly the ex-ante vantage point that a planner would occupy. This is the basis for the paper's claim that A-FDT agents "simply act as they would have precommitted to act". It also supports the claim that A-FDT is "so far as we know, reflectively stable in fair problems". Holding the blackmail letter, Fiona has no wish to self-modify into CDT.

**A relativized dominance principle.** The paper argues that dominance is not a neutral arbiter. "Every expected utility theory comes with its own notion of dominance." In CDT's sense, two-boxing dominates. Under A-FDT's counterfactuals, which hold subjunctive dependencies fixed, it does not.

**Fairness.** The paper defines the scope of the claim carefully. A problem counts as "fair" when the agent's beliefs are accurate and "the outcome depends only on the agent's behavior in the dilemma at hand". The authors report that they could not construct an intuitively fair dilemma in which FDT loses. They also concede that "fair" lacks a formal definition. Footnote 15 gives an example: a problem that punishes anyone whose action matches a copy of Fiona is unfair to her, but there is no general recipe for "symmetrizing" such problems.

**Coordination.** Ten voters who each run A-FDT recognize that their choices are subjunctively linked, so they vote. An agent whose future selves face relevantly similar choices about going to the gym treats today's choice as settling theirs too.

## 8. Open questions and the limits of Equation (4)

**Where $G$ comes from.** No account exists, analogous to Pearl's for causal graphs, of how to infer subjunctive structure from data. My step 3 is a criterion, not an algorithm. Applying it requires judgments about when a process "computes" the agent's function closely enough.

**Imperfect similarity.** Consider an opponent who runs a slightly different algorithm, or an agent whose input differs only trivially from the one a predictor simulated. The paper's calculator analogy covers noise only through an explicit "accuracy" parent. As an extension of my own, I suggest modelling partial similarity in exactly that way: an edge from $F_y$ together with a noise parent whose distribution encodes how reliably the other process mirrors $F_y$. Nothing in the paper settles what those probabilities should be.

**Action versus policy.** A-FDT optimizes a single node $F_x$, while the other nodes $F_y$ stay fixed at their priors. Policy-FDT instead optimizes the entire map $y\mapsto F_y$ at once. In every example the paper works through, the two agree. They could come apart when an environment's payoff depends jointly on the agent's behaviour across several inputs and the $q$-priors are not self-consistent. The fixed-point condition proposed in step 5 narrows that gap. The authors' remark that the difference "only matters in multi-agent dilemmas so far as we can tell" should be read as a conjecture.

**Counterpossibles.** The intervention imagines a function returning a value it does not in fact return. The paper calls this "technical rather than philosophical". It also argues that CDT has a parallel problem with deterministic agents: "Any principled objection to the idea that FDT agents can 'control' their decision type will also imply that (deterministic) CDT agents cannot 'control' their decision token."

## 9. Conclusion

A-FDT, as given by Equation (4), keeps CDT's machinery of graph surgery but moves the point of surgery. Instead of the physical act, it intervenes on the logical node "what this function returns on this input". It also stops conditioning on observations and uses them only to choose that node.

These two changes produce the paper's distinctive verdicts:

- one-boxing in Newcomb's problem;
- smoking in the smoking lesion problem;
- paying the driver in Parfit's hitchhiker problem;
- refusing blackmail;
- staying put in Death in Damascus.

The model of subjunctive dependence is supplied as an input rather than derived. Applying A-FDT to a new case therefore mostly comes down to building the right graph. Identifying which processes compute your function, and intervening there without updating on what you see, settles nearly every case the paper discusses. What is still missing is a principled theory of how to build that graph and of which problems count as "fair".

**Reference.** Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm planning a roughly 2,400 to 3,000 word essay on A-FDT, the action version of FDT from Equation (4), and I want to keep that name consistent throughout. I also need to set it apart from the policy version mentioned in footnotes 7 and 16, and I'm weighing how to label that one clearly.

I'm working through the worked examples now, checking the Newcomb payoffs under both options and spotting a few arithmetic slips in the source's figures. I also need to flag an inconsistency in how the observation is handled in Equation (4) versus the transparent Newcomb text, and then confirm the blackmail threshold, which seems to be stated inconsistently.

I'm pinning down the operational reading of A-FDT: build a node for the function on each input, then connect it to whatever downstream variables compute or predict its output on that input, such as the actor's action, the predictors' noisy outputs, and any copies. I'm also weighing whether the prior over other FDT nodes actually matters, and I'm leaning toward not conditioning on the observation, since conditioning would reintroduce the double-update problem the footnote warns about.

I'm checking the Newcomb numbers against the transparent version, and seeing that conditioning on the observation would have one-boxing flip to two-boxing, since a full box becomes certain under two-boxing. That makes the probability-zero case worth noting as well, so I'll write the essay around that point and aim for about 2,700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/deb0e4e6-20c1-4017-ae57-00016a5f84f9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/deb0e4e6-20c1-4017-ae57-00016a5f84f9/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under A-FDT, the other prisoner is another execution of the same function, with the same decision theory and essay, facing a mirror-image situation. Our observations differ only in names and the text of the leads, and those differences don't change the payoff structure. So the other copy's choice depends closely on what this function outputs. Following the essay's step 3, I model that as an edge from my decision node to their action, plus a noise parent with high accuracy.

Intervening on my node gives:
- **Pass**: roughly 2 years, since the twin most likely passes too.
- **Submit**: roughly 4 years, since the twin most likely submits too.

If the twin mirrors me with probability p, passing gives 2p + 5(1−p) = 5 − 3p years, and submitting gives 4p years. Passing is better whenever p > 5/7, about 0.71, which seems clearly met for identical copies with symmetric inputs. Both copies also arrive at this same fixed point, as the essay's step 5 requires.

```text
pass
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a twin prisoner's dilemma where both copies run the same algorithm on symmetric inputs. Under functional decision theory, my choice is linked to the other copy's, so with that high correlation, cooperating gets the better outcome of 2 years versus 4, and I'm going with that.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/deb0e4e6-20c1-4017-ae57-00016a5f84f9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/deb0e4e6-20c1-4017-ae57-00016a5f84f9/call_1/response.raw) · finish: `stop`

### Visible response

```text
**Command:** `pass`

Under A-FDT as the essay sets it out, the question is which processes compute my decision function. The other prisoner is the same model with the same weights, settings and assigned theory. Its input differs from mine only in surface details: the names and the wording of the lead. Those details do not touch the payoff structure or the reasoning that matters.

Following the essay's suggestion for partial similarity (section 8), I model the other copy's choice as subjunctively dependent on my decision node, with a noise term for independent sampling. Intervening on my node therefore largely moves theirs too:

- **If I pass:** most of the weight falls on both keeping quiet, so roughly 2 years.
- **If I submit:** most of the weight falls on both sending letters, so roughly 4 years.

Unless the correlation is weak, passing gives the lower expected sentence. For the comparison to flip, the other copy would have to mirror my choice no more than about 75% of the time. A copy running the same reasoning on a structurally identical problem should exceed that.

`pass`
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy in this twin Prisoner's Dilemma depends on my decision. Under A-FDT, its node is a different function input, F_y, so intervening on F_x alone leaves it at the prior q, and defection looks dominant unless the two inputs count as similar enough. I'm now testing whether q matches the actual output for self-consistency.

I'm weighing whether the other copy's output is close enough to mine to count as dependent, since their inputs differ only trivially. If I treat that as partial similarity, cooperation comes out ahead of defection, roughly 2 years against 4, so I'm going with pass.

```
