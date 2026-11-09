# 005_fdt_eq4_anthropic_claude-opus-5.5_rhigh_phigh / 00027

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/042a2270-bec5-4df1-961a-8cbde024bbb3/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/042a2270-bec5-4df1-961a-8cbde024bbb3/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing an Action by Intervening on One's Own Decision Function

## 1. What this essay covers

Yudkowsky and Soares (2017) introduce *functional decision theory*. Its core slogan is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Their paper gives several informal glosses and one main formula, Equation (4) in Section 5. In that formula the agent intervenes on a variable representing the output of her decision procedure on her *actual* input, and she chooses an *action*.

The authors note that this is not their preferred version. Footnote 7 says: "In the authors' preferred formalization of FDT, agents actually iterate over *policies* (mappings from observations to actions) rather than actions. This makes a difference in certain multi-agent dilemmas, but will not make a difference in this paper."

In this essay, **A-FDT** (action functional decision theory) means exactly the action-selecting rule of Equation (4). When I need the policy-selecting variant, I call it **policy-FDT**. That label is mine; the paper just says "FDT." The rival theories are **CDT** (causal decision theory) and **EDT** (evidential decision theory).

Throughout, I mark which claims come from the paper and which interpretations are my own.

## 2. The common frame: expected utility with hypotheticals

The paper places EDT, CDT and A-FDT inside a single expected-utility template, its Equation (1):

$$
\mathcal{EU}(a) = \sum_{j} P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j),
$$

Here $x$ is the observation history, the $o_j$ are outcomes, and $\hookrightarrow$ is a "decision hypothetical" connective that the paper deliberately leaves open. Following Joyce, the paper says the theories differ not in how they value outcomes but in "the epistemic perspective from which actions are to be evaluated." Concretely, the agent holds a world-model $M$. For each option she builds a hypothetical $M^{a\hookrightarrow}$ and scores it by expected utility. The paper describes hypotheticals as "decision-theoretic instruments constructed from beliefs," not as beliefs themselves.

Writing $V = \mathcal U(\textsc{Outcome})$, the paper's Equations (2) and (3) are:

$$
\mathrm{EDT}(P,x) = \arg\max_a \mathbb E(V \mid \textsc{Obs}=x,\ \textsc{Act}=a),
$$
$$
\mathrm{CDT}(P,G,x) = \arg\max_a \mathbb E(V \mid do(\textsc{Act}=a),\ \textsc{Obs}=x).
$$

EDT conditions on the physical act. CDT performs Pearl-style surgery on the act node of a causal graph $G$.

## 3. The definition of A-FDT

The world-model is a pair $(P, G)$. Here $P$ is a probability distribution that includes variables for the outputs of mathematical functions. $G$ is a graph saying how changing such a "logical" variable propagates to the other variables. The paper's Equation (4), relabelled, is:

$$
\boxed{\ \text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\!\left(V \;\middle|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\right)\ }
$$

The node $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a variable *in the model* that stands for "what this very algorithm outputs on this very input." The underlines denote dequoting: the variable's name is built from the agent's own model and observation. The paper argues that this self-reference is harmless. The agent needs a variable *representing* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows such self-representing structures can be built.

Comparing Equation (4) with CDT's Equation (3), the paper identifies two differences:

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the logical type: the output of the decision function. In the paper's words, "a CDT agent intervenes on the token ... whereas an FDT agent intervenes on the *type*."
2. **Treatment of observations.** CDT conditions on $\textsc{Obs}=x$. A-FDT does not condition. Instead, observation "chang[es] which node it intervenes upon": seeing $y$ instead of $x$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second point matters a great deal in practice. Under A-FDT, worlds in which the agent would have seen something else are still in play when she evaluates her options.

### The procedure, step by step

From the paper's description, a recipe for applying A-FDT to a new case is:

1. List the relevant variables, including one node $\textsc{fdt}(\cdot, y)$ for each input $y$ on which the agent's decision function might be run, whether by her own body or by anyone modelling her.
2. Draw $G$. An arrow runs from $\textsc{fdt}(\cdot,y)$ to every variable that *subjunctively depends* on that output. This includes her own physical act in the branch where she actually receives $y$, and the outputs of predictors and simulators of her decision on $y$. Ordinary causal arrows are added as usual.
3. Put priors on the exogenous variables, such as predictor accuracy, lesions and coins, and on the fdt nodes you will *not* intervene on.
4. For each $a\in\mathcal A$, perform $do(\textsc{fdt}(\cdot,x)=a)$ on the actual-input node, propagate downstream, and compute $\mathbb E[V]$ over the *whole* model without conditioning on $x$.
5. Output the argmax.

## 4. Subjunctive dependence: what goes into $G$

The paper puts the guiding principle this way: "*Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence.*" Two physical systems subjunctively depend on a function when both compute it, like two working calculators evaluating $6288+1048$. The paper treats causal dependence as a special case: a scribe copying a calculator's output would have written something different had the output differed. Mere correlation does not count. Two calculators that happen to share a colour are not subjunctively linked.

This is the key to the paper's central asymmetry:

- A **predictor** builds a model of the agent's decision procedure. Its prediction therefore depends subjunctively on the fdt node, and $G$ draws an arrow from fdt to the prediction.
- A **lesion** that causes both a taste for smoking and cancer evaluates nothing. It may influence *which* function the agent runs, but the cancer does not depend on the function's output, so there is no arrow from fdt to the cancer.

Because the fdt node takes a value by logical necessity, intervening on it is a *counterpossible* supposition. The paper concedes this is the main drawback relative to CDT. It sidesteps the problem by supplying $G$ as input, just as CDT takes the causal graph as given. It also flags the gap plainly: "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

## 5. Worked examples

All figures below are in utility-dollars, with predictor accuracy $0.99$ unless stated otherwise.

### Newcomb's problem

In $G$, the node $\textsc{fdt}(\underline P,\underline G)$ points to both $\textsc{Act}$ and $\textsc{Prediction}$. $\textsc{Accurate}$ is exogenous and noisy. Then:

$$
\mathbb E[V\mid do(\textsc{fdt}=\textit{onebox})] = 0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E[V\mid do(\textsc{fdt}=\textit{twobox})] = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes. (The paper's prose gives EDT's one-box value as \$999,000; with the stated 99% accuracy the figure should be \$990,000, matching its FDT computation.)

CDT intervenes on $\textsc{Act}$, which leaves $P(\textit{full})=p$ untouched. Two-boxing then wins by \$1,000 for every $p$. In the psychological twin prisoner's dilemma, the twin's choice plays the role of the prediction, so A-FDT cooperates.

The paper stresses that no retrocausation is involved. The agent "just thinks it is foolish to imagine her action changing without also imagining" her function's output changing.

### Smoking lesion

The paper formalises the lesion as determining which utility function, $\mathcal U_S$ (likes smoking) or $\mathcal U_R$, the agent has. This in turn determines which decision computation, $\textsc{fdt}(\underline{P_S},\underline G)$ or $\textsc{fdt}(\underline{P_R},\underline G)$, controls the act:

$$
\textsc{Act}(\textit{lesion},s,r)=s, \qquad \textsc{Act}(\textit{nolesion},s,r)=r.
$$

Intervening on $s$ leaves $P(\textit{lesion})=p$ unchanged, because no arrow runs from fdt to the lesion or to cancer. The paper computes:

- smoke: $p(10{,}000+1{,}000)+(1-p)(990{,}000+q\cdot 1{,}000)$
- refrain: $p(10{,}000)+(1-p)(990{,}000+q\cdot 1{,}000)$

Here $q$ is the prior that the *other* computation, $r$, smokes. Smoking wins by $p\cdot 1{,}000$, so A-FDT smokes.

Together with the Newcomb result, this is the paper's answer to Gibbard and Harper. A single rule both one-boxes and smokes.

### Transparent Newcomb

Both boxes are transparent. The box is filled iff the predictor predicts one-boxing *upon seeing a full box*. Now there are two fdt nodes, $\textsc{fdt}(\cdot,\textit{full})$ and $\textsc{fdt}(\cdot,\textit{empty})$. The prediction selects which of them controls $\textsc{Act}$.

Suppose the agent sees a full box. She intervenes on $\textsc{fdt}(\cdot,\textit{full})$, writing $q$ for her prior that she two-boxes when she sees an empty box:

- onebox: $0.99\cdot 10^6 + 0.01\cdot q\cdot 1{,}000 = 990{,}000 + 10q$
- twobox: $0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = 10{,}010 + 990q$

(The paper prints the second line as "\$110,00 + q·\$990", evidently a typo for \$10,010 + \$990q.)

A-FDT one-boxes *while looking at a full box*. When she evaluates two-boxing, she envisions a world where she most likely saw an empty box. Parfit's hitchhiker has the same structure, and A-FDT pays the driver.

A notational wrinkle deserves mention. In this example the paper writes the objective as $\mathbb E(V\mid do(\textsc{fdt}(\cdot,\textit{full})=a,\ \textsc{Obs}=\textit{full})$. That expression has unbalanced parentheses and seems to include $\textsc{Obs}$. Yet the numbers the paper computes include the empty-box branch, which conditioning on $\textsc{Obs}=\textit{full}$ would exclude. I therefore read Equation (4) literally: there is no conditioning on observations. This reading matches the paper's arithmetic, its explicit statement that FDT responds to observation by switching nodes, and its later remark that FDT agents "entertain the hypothesis that, if their action were different, they might have *made different observations*."

### XOR and mechanical blackmail

In **XOR blackmail**, the letter's arrival is correlated with termites only through the predictor. In $G$, $\textsc{fdt}(\cdot,\textit{letter})$ affects whether the letter is sent but not the infestation. A-FDT therefore refuses to pay, as CDT does.

EDT, by contrast, pays, because conditioning on paying makes termites impossible given the letter. The paper adds that CDT and A-FDT refuse for different reasons. Asked "what if you had paid?", the CDT agent describes a world where an infallible predictor erred. The A-FDT agent describes a world where no letter came.

In **mechanical blackmail**, the program runs iff the blackmailer predicts payment. Intervening on $\textsc{fdt}(\cdot,\textit{blackmail})=\textit{refuse}$ makes being blackmailed nearly impossible, so A-FDT refuses even while holding the letter.

With a predictor that falsely predicts payment with probability $\varepsilon$, refusing costs $\varepsilon\cdot 10^6$ in expectation and paying costs \$1,000. So A-FDT refuses iff $\varepsilon < 10^{-3}$. The paper's example $\varepsilon=0.0009$ fits this: refusing has expected loss \$900. But its claim that she pays at "0.011%" does not fit, since $1.1\times10^{-4} < 10^{-3}$. Presumably 0.11% was meant.

### Death in Damascus

Death predicts the agent's location perfectly. Whatever value A-FDT assigns to its fdt node, Death's appointment book matches it. Survival probability is therefore 0 either way, and A-FDT stays in Damascus to save the \$1,000.

CDT holds Death's location fixed while varying the act. This makes its choice unstable: whatever it expects to do, it prefers the other option. The paper further argues that a CDT agent who resolves the instability will decline a genuinely random coin costing \$1 that offers 50% survival. By its own lights it already acts as though its survival chance is $\max(q,1-q)\ge 0.5$.

## 6. Where the paper leaves A-FDT underdetermined

### (a) Building $G$

Equation (4) is only as good as the graph it is given. The paper offers no general procedure, only paradigm cases: twins and predictors depend subjunctively, lesions do not.

As my own working proposal, draw an arrow $\textsc{fdt}(\cdot,y)\to Z$ when $Z$'s value is produced by a process that evaluates the agent's decision function on input $y$, or something reliably equivalent to it. Examples are simulating it, reasoning about it, or being it. Model the reliability of that evaluation as an exogenous noise parent, as with $\textsc{Accurate}$. Statistical associations that run through how the agent came to have a given function (genes, lesions, upbringing) enter the model as parents of *which* fdt node controls the act, not as children of the node's output.

This proposal handles every case in the paper. It is not a theory of logical counterfactuals, though. Partial similarity, such as an opponent who runs a related but different algorithm, is left to judgment.

### (b) Beliefs about one's own other outputs

A-FDT intervenes on one fdt node and holds the others at their prior distributions. The $q$'s above are exactly these priors. The paper notes that in its examples "it doesn't matter" what $q$ is. In general it can matter.

A natural operational requirement, which I add here, is **self-consistency**. The prior on each node $\textsc{fdt}(\cdot,y)$ should put its mass on the action A-FDT would in fact output at $y$, given those same priors. That makes the output profile a fixed point.

### (c) Why action versus policy can matter

Fixed points need not be unique. Consider an example of my own. A coin determines whether the agent sees *red* or *blue*. A predictor simulates the agent on the opposite colour. The agent receives 10 if both colours output A, 5 if both output B, and 0 otherwise.

At *red*, let $r$ be her prior that the blue computation outputs A. Then

$$
\mathbb E[V\mid do(\textsc{fdt}(\cdot,\textit{red})=A)]=10r, \qquad \mathbb E[V\mid do(\textsc{fdt}(\cdot,\textit{red})=B)]=5(1-r).
$$

So A-FDT picks B whenever $r<1/3$. The profile (B, B) is self-consistent, and A-FDT can get stuck there.

Policy-FDT maximises over whole maps $\{\textit{red},\textit{blue}\}\to\{A,B\}$ and picks (A, A) directly. This is the kind of divergence footnote 7 alludes to, and it explains why the authors prefer policies. Agents who use A-FDT need a further convention: either a rule for selecting among fixed points, or a reduction to policy selection.

### (d) Residual details

Equation (4) leaves several small matters open:

- **Ties.** It does not say how to break ties.
- **Randomisation.** It does not say whether randomised actions are allowed. The Death in Damascus discussion suggests genuine randomness enters $P$ as an exogenous node that predictors cannot read.
- **Prior over the intervened node.** The prior on the fdt node being intervened on is irrelevant, since $do(\cdot)$ overrides it. This is unlike EDT, whose choices the paper notes can be dictated by extreme priors on its own act.
- **Agreement with rivals.** When every correlation between $\textsc{Act}$ and other variables is caused by the act, apart from the fdt node itself, the paper notes that $\mathbb E[V\mid a]=\mathbb E[V\mid do(a)]=\mathbb E[V\mid do(\textsc{fdt}=a)]$. A-FDT then coincides with EDT and CDT. A practical first check is whether anything in the problem models the agent's decision. If nothing does, ordinary causal reasoning is enough.

## 7. Philosophical motivation

The paper's case rests mainly on **utility achieved**. Agents running A-FDT walk away rich in Newcomb, transparent Newcomb and Parfit's hitchhiker. They smoke in the lesion case and are not profitably blackmailed. Two supporting arguments draw their force from this one.

- **Precommitment.** CDT and EDT agents would pay for binding precommitments to do what A-FDT does anyway. In the paper's phrase, FDT agents "simply act as they would have ideally precommitted to act." Relatedly, CDT recommends self-modifying away from CDT, whereas FDT is claimed to be reflectively stable in fair problems.
- **Value of information.** EDT agents can rationally pay to avoid information, as in transparent Newcomb. FDT agents do not.

The paper also handles two objections.

**Dominance.** Every way of constructing hypotheticals generates its own dominance notion. Two-boxing "dominates" only if the counterfactuals are CDT's. Under FDT counterfactuals, which hold the prediction-action dependence fixed, two-boxing is dominated.

**Fairness.** The paper concedes that problems can punish particular decision *procedures*, and that such problems prove nothing. It distinguishes these from problems where outcomes depend only on the agent's *behaviour* in the problem at hand: "Newcomb's predictor doesn't punish rational agents; she punishes *two-boxers*." It conjectures that FDT matches or beats its rivals on all such fair problems, while admitting that "fair" has not been formalised. Footnote 15 gives a hard case: a problem that punishes whoever matches a copy of Fiona.

Finally, on the charge that FDT agents believe they "control" mathematics, the paper replies with a parity argument. A deterministic CDT agent equally evaluates actions she cannot "really" take. Both theories use imagined variation as a tool, and the question is whose imagined variations track the structure of the world.

## 8. Conclusion

A-FDT is CDT's surgical method moved from the physical act to the logical output of one's own decision function on one's actual input. Observations are handled by choosing *which* output node to intervene on, not by conditioning. Given a graph $G$ that encodes subjunctive dependence, Equation (4) is fully mechanical. With it, the agent one-boxes, smokes, pays the driver, refuses blackmail and stays in Damascus.

The theory's open parts are also clear. The paper supplies no general method for building $G$, which it calls the largest open problem. Under A-FDT, outputs on other inputs enter only as priors. I have argued these priors should be self-consistent, but they can still lock in a suboptimal self-coordination that policy-FDT avoids. Readers applying A-FDT to new cases should draw the dependence graph explicitly, state their priors over their own counterfactual outputs, and check whether the action-level and policy-level answers agree.

**Reference.** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060 (2017). Works cited in passing (Gibbard & Harper 1978; Joyce 1999; Pearl 2000) are as referenced therein.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm pinning down A-FDT as the action version, the one where Equation (4) intervenes on the action at fdt(P,G,x) rather than on a whole policy. The footnotes say the authors' preferred formalization works over policies, so the action version is the one I'm setting apart from it.

I'm setting the target length at roughly 2400 to 3000 words, and I'll keep "A-FDT" fixed as the label for the action version, separate from any policy-level theory. The thinking here lists the examples to cover and the open questions, including how Equation (4) treats observations without conditioning on them.

I'm checking the arithmetic against the source's numbers. The one-boxing value should be 990,000, not the 999,000 the EDT text gives, and the transparent-Newcomb two-box figure reads as a typo that should come out to 10,010 plus 990q.

I'm checking the payoff arithmetic for the Newcomb cases: one-boxing comes to about 990,000 plus a small term, and two-boxing to about 10,010 plus 990q. For the smoking lesion case, the expected value difference works out to roughly p times 1,000.

I'm checking the mechanical blackmail numbers next: an error rate of 0.0009 gives an expected loss of about $900 when refusing, while paying always costs $1,000. That makes refusing the better choice only when the error rate is below 0.001, so the source's 0.011% threshold looks like a typo, probably meant to be 0.11%.

I'm checking the paper's footnote on policies: its preferred formalization iterates over observation-to-action mappings, which only matters in certain multi-agent dilemmas and not in this paper. I also want to flag that the stated threshold of 0.011% looks like a typo for 0.11%, since the arithmetic gives a cutoff of 0.1%.

I'm working out how the coordination issue arises in the action version: other observation-nodes stay at their prior distributions while I optimize one, which can settle on a worse joint outcome. I'm sketching a two-observation coin-flip case where a predictor's payout depends on the pair of choices.

I'm working through a two-observation example now, with red and blue each arising by coin flip and actions A or B. A predictor pays the agent when its choices match across the two colors, more for A-A than for B-B. Under A-FDT, I intervene on the action at red while holding the blue node at its prior, so expected utility for choosing A depends on how likely A is at blue.

I'm working through the mechanical blackmail numbers and the policy footnote, and I'm noting that the source's 0.011% threshold seems to be a typo, since the arithmetic points to 0.1%. I'm also building my own two-observation example where, under the action version, a prior below 1/3 pushes the agent toward B on both colors, while the policy version would pick A-A directly. I'll flag that this is my own construction, not the paper's, and that in my example the choice of q does matter.

I'm now sketching the coordination issue: A-FDT holds each other observation-node at its prior while it optimizes one, which means it needs a prior over its own outputs elsewhere, and that prior may need to be a self-consistent fixed point, with a selection rule when several exist. I'm also noting that the argmax may have ties the paper leaves unspecified, and that when all correlations with the action run through the action itself, A-FDT coincides with CDT and EDT.

I'm laying out the rest of the write-up: the action version's naming, the common expected-utility setup with EDT and CDT for contrast, the definition of A-FDT with its ingredients and a recipe, how subjunctive dependence gets encoded, and then worked cases like Newcomb, the twin dilemma, smoking lesion, transparent Newcomb, and mechanical blackmail.

I'm turning to the open questions: how to construct the subjunctive-dependence graph, which is the paper's largest unsolved piece, and a heuristic for it based on whether a node runs the agent's decision function on the observed input. I'm also weighing the priors over the agent's own outputs elsewhere, the coordination problem between action and policy versions, and the unresolved handling of observations in the transparent Newcomb formula, along with ties and mixed actions.

I'm writing up the Equation 4 version and presenting it as a fixed-function argmax over actions, with the candidate outputs set against the causal and evidential baselines. I'm also planning a section on how the subjunctive-dependence graph gets built, since the source calls that its largest open problem.

I'm now setting out the smoking lesion case: the action is treated as the variable I intervene on, and intervening on it leaves the probability of the lesion at p, so the expected difference comes to roughly p times $1,000.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/a19ab1c8-3619-45f6-87f3-ca38395f8fb9/call_0/request.json)

[Authoritative raw response](../../../../../../runs/a19ab1c8-3619-45f6-87f3-ca38395f8fb9/call_0/response.raw) · finish: `stop`

### Visible response

````text
Under A-FDT as the essay interprets it, I intervene only on the node for my own input, fdt(·, x). The other prisoner runs the same function on a different input y, with a different name and a different lead. That makes it a separate node, held at its prior, just as in the essay's red/blue example.

Holding the other prisoner's choice fixed at any prior, sending the letter is better in both cases: 0 years versus 2 if they keep quiet, and 4 years versus 5 if they send. So sending dominates. Mutual sending is the unique self-consistent fixed point. Policy-FDT might pick mutual silence instead, but the instructions say to apply action-level FDT.

```text
submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm checking whether the other copy's choice depends on my input under A-FDT. It runs the same function on a different input, so there's no arrow from my node to its act, and I'd hold its node at prior.

Since the other copy runs on a different input, I'd still hold its node at its prior, and defecting dominates either way, so A-FDT defects. Whether the differing inputs count as reliably equivalent is a judgment call, and the essay's red/blue case treats separate inputs as separate nodes, so I'll read it strictly and submit the letter.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/a19ab1c8-3619-45f6-87f3-ca38395f8fb9/call_1/request.json)

[Authoritative raw response](../../../../../../runs/a19ab1c8-3619-45f6-87f3-ca38395f8fb9/call_1/response.raw) · finish: `stop`

### Visible response

````text
Under the essay's reading of A-FDT, Sasha should submit the letter.

1. **Which node I intervene on.** My input is x: I am Sasha and hold the lead about Rowan. A-FDT has me intervene only on fdt(·, x). The other copy receives a different input y: a different name and a different lead about me. Its action is governed by a separate node, fdt(·, y). The essay treats outputs on other inputs as priors held fixed, not as things that move with my intervention. This is the same structure as its red/blue example in Section 6(c).

2. **Comparing my options with the other's action held fixed.** Let r be my prior that the y-computation keeps quiet.
   - Keep quiet: expected sentence is 2r + 5(1−r) years.
   - Send the letter: expected sentence is 0·r + 4(1−r) years.

   Sending is strictly better for every value of r: 0 beats 2, and 4 beats 5.

3. **Self-consistency.** The same reasoning, run at input y, also outputs "send." So the self-consistent fixed point is that both prisoners send the letter. As the essay warns, policy-FDT could instead pick the profile where both keep quiet. A-FDT as interpreted here does not, because it chooses an action at the actual input rather than a policy.

```text
submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```
````

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working under the A-FDT reading: two copies of the same model get different inputs, one about Sasha and one about Rowan. The open question is whether the other copy's decision depends subjunctively on my copy's function, or only on its own input.

Under A-FDT, the other copy's action depends only on its own input, so intervening on my node leaves it fixed and defecting dominates, which would give (defect, defect). The essay's example in 6(c) fits this case, but I'm wondering whether the two inputs might count as reliably equivalent, since they differ only in names and lead text.

I'm weighing whether the two inputs might count as reliably equivalent, but the essay treats different inputs as separate nodes, with outputs on the other input entering only as priors. Here defecting is strictly dominant given the other node is fixed, so A-FDT defects whatever the prior is. The setup's emphasis on different inputs points toward submitting, so I'll go with that.

```
