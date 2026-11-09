# 003_fdt_eq4_anthropic_claude-opus-5.5_rlow_plow / 00011

Status: **complete**. Saved outcome: **DD**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/73457765-080a-4271-8a24-cd1cf6e72fc6/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/73457765-080a-4271-8a24-cd1cf6e72fc6/call_0/response.raw) · finish: `stop`

### Visible response

```text
# Action Functional Decision Theory (A-FDT): Choosing as the Output of a Function

## 1. The question A-FDT asks

Every expected-utility theory says to pick the option with the highest expected utility. Theories differ on one point: *what would the world look like if I chose differently?* Yudkowsky and Soares, in *Functional Decision Theory: A New Theory of Instrumental Rationality*, give an answer that departs from both evidential decision theory (EDT) and causal decision theory (CDT). This essay follows their primary formal statement, Equation (4) of Section 5. That equation ranges over *actions*, so I call it **A-FDT** (action functional decision theory). The label marks it off from a policy-selecting variant the authors mention in footnotes, discussed in §7.

The guiding idea, in the authors' words, is that an agent should treat her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" CDT asks "Which physical act of mine causes the best outcome?" EDT asks "Which physical act of mine would be the best news to hear I took?" A-FDT instead varies the *logical output of the decision procedure*. Anything else in the world that computes or accurately models that procedure varies along with it.

## 2. The common framework

The paper writes all three theories as maximizing

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\, \mathcal U(o_j),$$

where $a \in \mathcal A$ is an action, $x$ an observation history, $o_j$ an outcome, and "$\hookrightarrow$" the connective for decision hypotheticals. Following Joyce's representation theorem, the authors treat the interpretation of $\hookrightarrow$ as the free parameter on which the theories disagree. The agent has a world-model $M$. For each candidate action she builds a "hypothetical" $M^{a\hookrightarrow}$ from it, which the authors describe as a transient piece of scratch work rather than a belief. She then scores each hypothetical. Write $V := \mathcal U(\textsc{Outcome})$. The three rules are:

- **EDT** (Eq. 2): $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$, which is plain conditioning.
- **CDT** (Eq. 3): $\arg\max_a \mathbb E(V \mid do(\textsc{Act}=a), \textsc{Obs}=x)$, which is a Pearl intervention on the physical act node within a causal graph $G$.
- **A-FDT** (Eq. 4):

$$\boxed{\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A} \mathbb E\Big(V \;\Big|\; do\big(\textsc{fdt}(\underline P,\underline G,\underline x) = a\big)\Big).}$$

Here $\textsc{fdt}(\underline P,\underline G,\underline x)$ is a *variable in the agent's own model*. It stands for "the output of the FDT algorithm when run on inputs $(P,G,x)$". The underlines denote dequoting: the variable's name is built from the actual inputs. The graph $G$ is no longer purely causal. It encodes "the logical, mathematical, computational, causal, etc. structure of the world more broadly," and in particular which variables subjunctively depend on the function node.

## 3. Reading Equation (4) term by term

**The intervention target.** A-FDT intervenes on a *type* rather than a token: the output of a function on a given input. Every node that is downstream of that function node in $G$ changes with the intervention. This includes the agent's physical act, a twin's act, and a predictor's prediction. Everything else is held fixed. The authors summarise the analogy as: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

**Subjunctive dependence.** Two physical systems that compute the same function both depend subjunctively on that function. The authors' picture is two calculators on opposite sides of the globe, each computing $6288+1048$. Causal dependence is a special case: a scribe copying a calculator's output depends on it in both senses. Mere correlation is not enough. Two pink calculators share a colour, but neither's colour depends on the other's.

**Observations.** Equation (4) contains no conditioning on $\textsc{Obs}=x$. The authors stress this point: "where CDT responds to observation by Bayesian conditionalization, FDT responds to observation by changing which node it intervenes upon." A different observation history $y$ means intervening on $\textsc{fdt}(\underline P,\underline G,\underline y)$ instead. This is the source of A-FDT's "updateless" flavour. In a hypothetical where the agent acts differently, she may have *received different observations*.

**Counterpossibles.** For fixed inputs, the function's output is a logical fact. Setting it to some other value is therefore a counterpossible supposition. The authors admit there is no satisfactory theory of a $\mathtt{true}(\varphi)$ operator for such suppositions. Their move is to require that $G$ be *supplied* as an input, just as CDT needs a causal graph. They describe constructing $G$ as "perhaps the largest open problem in the study of functional decision theory."

**Self-reference.** The model must contain a variable naming the very algorithm that is reading the model. The authors argue this is harmless: the agent needs a variable that *represents* the output, not knowledge of its *value*, and Kleene's recursion theorem ("quining") shows such self-representing structures exist.

**When the theories agree.** If every correlation between $\textsc{Act}$ and other variables is caused by $\textsc{Act}$, apart from its dependence on the function node, then

$$\mathbb E[V\mid a] = \mathbb E[V\mid do(a)] = \mathbb E[V\mid do(\textsc{fdt}(\underline P,\underline G)=a)],$$

and EDT, CDT and A-FDT coincide. Disagreements arise only when something other than the act itself tracks the agent's decision, as predictors and copies do.

## 4. A recipe for applying A-FDT

The paper does not give an explicit procedure. The following is my operationalisation of what Equation (4) and the worked examples require.

1. **List the variables.** Include world states, noise terms, outcomes, $V$, and one node $\textsc{fdt}(\underline P,\underline G,\underline y)$ for every observation history $y$ the agent might find herself deciding on in this problem.
2. **Wire the dependencies.** Draw an arrow from a function node to every variable whose value is fixed by that function's output. Examples are the agent's own act given that she received $y$, and any accurate prediction or simulation of what she does on input $y$. When an observation is itself determined by some state (say, a prediction), add a "switch": $\textsc{Act}$ takes the value of whichever function node corresponds to the observation actually produced. Predictor error goes into explicit noise nodes such as $\textsc{Accurate}$.
3. **Assign priors** to exogenous nodes. This includes the function nodes for observations *other* than the actual one. I call these "off-path" nodes.
4. **Intervene** on the node for the actual input $x$, once for each $a\in\mathcal A$. Propagate the change downstream, leaving non-descendants at their prior distribution. Do *not* condition on $x$.
5. **Take the argmax.** The paper leaves tie-breaking unspecified. Any fixed rule will do.

Step 3 involves an assumption of my own. In the paper's examples, the off-path nodes are given arbitrary priors ($q$), and the authors note that the choice "won't matter" there. That holds when off-path behaviour contributes a term of equal or negligible size to every option. It is not guaranteed in general (see §7).

## 5. Worked examples

### Newcomb's problem (99% predictor)

The graph has $\textsc{fdt}\to\textsc{Act}$ and $\textsc{fdt}\to\textsc{Prediction}\leftarrow\textsc{Accurate}$, with $\textsc{Prediction}\to\textsc{Box B}$.

- $do(\textsc{fdt}=\text{onebox})$: $P(\text{full})=0.99$, so $\mathbb E V = 0.99\times 1{,}000{,}000 = \$990{,}000$.
- $do(\textsc{fdt}=\text{twobox})$: $P(\text{full})=0.01$, so $\mathbb E V = 0.01\times 1{,}001{,}000 + 0.99\times 1{,}000 = \$11{,}000$.

A-FDT one-boxes. Its reasoning appeals to no backward causation. The authors write that Fiona, their FDT agent, "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value." (The paper's EDT figure for the same case reads \$999,000. The arithmetic gives \$990,000, so this appears to be a typo.)

### Smoking lesion

The lesion influences cancer, and it also determines *which* decision function controls the act, since it alters preferences. The paper models this with two utility functions $\mathcal U_S,\mathcal U_R$ and two function nodes. Cancer is not a descendant of either function node, so

$$P(\text{lesion}\mid do(\textsc{fdt}(\underline{P_S},\underline G)=\cdot)) = p$$

whichever value is set. The smoke hypothetical beats the refrain hypothetical by $p\cdot\$1{,}000$, and A-FDT smokes. This is the paper's key contrast: a lesion does not "evaluat[e] the agent's future decisions," whereas a predictor does. One rule therefore one-boxes and smokes, a combination Gibbard and Harper had argued was unavailable.

### Transparent Newcomb (box B seen full)

The prediction determines what the agent observes, and the observation selects which function node drives $\textsc{Act}$. Let $q$ be the prior probability that the agent two-boxes on seeing an empty box. Intervening on $\textsc{fdt}(\cdot,\text{full})$ gives:

- onebox: $0.99\cdot 1{,}000{,}000 + 0.01\cdot q\cdot 1{,}000 = \$990{,}000 + \$10q$;
- twobox: $0.01\cdot 1{,}001{,}000 + 0.99\cdot q\cdot 1{,}000 = \$10{,}010 + \$990q$.

(The source prints "$110,00"; the correct figure is \$10,010.) A-FDT one-boxes *while looking at a full box*. In the twobox hypothetical, the agent most likely never sees a full box at all. The paper points out that this case has the same structure as Parfit's hitchhiker: paying the driver after reaching the city is A-FDT's verdict, and both CDT and EDT refuse to pay.

### XOR blackmail and mechanical blackmail

In XOR blackmail, setting the letter-node to *pay* or to *refuse* changes whether the letter is sent. It does not change the termite infestation, because infestation is not downstream of the function. A-FDT refuses. EDT pays, because conditioning on paying makes the termites "evidentially" disappear.

In mechanical blackmail, refusing makes being blackmailed unlikely in the first place, so A-FDT refuses even with the letter in hand. The verdict depends on the predictor's error rate. The paper reports that Fiona still refuses at an error rate of 0.0009 but pays at 0.011%. On their convention, the comparison is \$1,000 lost for certain against a 0.09% chance of the \$1,000,000 harm.

### Death in Damascus

Death's appointment book depends on the agent's function. Both hypotheticals therefore contain certain death, and staying in Damascus saves \$1,000, so A-FDT stays immediately. CDT, by contrast, cycles between options or ratifies a near-50/50 mixture. It even declines a truly random coin costing \$1 that would give a genuine 50% survival chance.

### Twin prisoner's dilemma

Both twins' acts descend from one function node. Under $do(\text{cooperate})$ the payoff is \$1,000,000; under $do(\text{defect})$ it is \$1,000. A-FDT cooperates.

## 6. Dominance, fairness and the global perspective

The two-boxer's dominance argument holds the prediction fixed while varying the act. The authors reply that every way of constructing hypotheticals generates its own notion of dominance. CDT's notion is "merely a restatement of CDT's method." Under FDT-style dominance, with subjunctive dependencies held constant, one-boxing is undominated. Dominance therefore cannot settle the dispute without begging the question, and the authors fall back on utility actually achieved.

They concede that problems can punish any theory, for example a mind-reader who rewards only CDT agents. They restrict their claim to "fair" problems, in which "the outcome depends only on the agent's behavior in the dilemma at hand." Newcomb's predictor "doesn't punish rational agents; she punishes *two-boxers*." The authors admit that fairness has not been formalized. Their footnote describes a game that punishes anyone matching a copy of Fiona, which no FDT agent can win.

Further claimed benefits are reflective stability (an A-FDT agent has no reason to self-modify into CDT mid-problem), non-negative value of information, and no need for precommitment, ratification or tickle defences. The authors also say the "control" A-FDT exercises over a function's output is no more mysterious than the control a deterministic CDT agent exercises over her physical act.

## 7. Open questions and operational proposals

Each item below separates the paper's claims from my own suggestions.

**(a) Where does $G$ come from?** *Paper:* it is an input, and nobody yet knows how to infer subjunctive dependencies from observation the way Pearl infers causal structure. *My proposal:* draw an arrow from the function node to a variable $Z$ only when $Z$ is produced by a process that is (i) a physical implementation of the same function on the same input, or (ii) a model or prediction whose output is a function of that one, with the model's errors placed in separate noise nodes. Variables that are merely correlated with the agent's act through common causes (a lesion, genes, upbringing) get no such arrow. On this criterion, a predictor that relies only on base rates of past choosers, without modelling the agent's reasoning, counts as lesion-like. That edge case remains contestable.

**(b) Imperfect or partial dependence.** *Paper:* error weakens the interdependence but does not eliminate it, and the examples model error with independent noise. *My proposal:* use the same approach generally. A predictor that runs a *similar* algorithm can be modelled as copying the agent's output with some probability and otherwise acting independently. How much similarity is enough is a substantive judgement that A-FDT itself does not settle.

**(c) Off-path function nodes and the action/policy gap.** *Paper:* footnotes 7 and 16 say the authors' "preferred formalization" picks a *policy*, a mapping from observations to actions, and that the difference "will not make a difference in this paper" outside some multi-agent cases. This matters for A-FDT. Equation (4) sets only the node for the actual input $x$ and leaves the nodes for other inputs at their priors. *My illustration:* take two instances of the agent that receive different inputs $x_1$ and $x_2$ and score only if they choose matching options, with two equally good matching pairs. Each instance, intervening only on its own node, optimises against a fixed prior over its counterpart. If those priors are symmetric, A-FDT gives no determinate coordination, and if they are mis-set it can miscoordinate. A policy-selecting rule chooses both entries jointly. In such cases A-FDT's answer depends on how off-path priors are set, and no source text fixes them. My suggestion for users is to treat any A-FDT verdict that changes under varying off-path priors as indeterminate, and to flag the problem as one where the policy formulation should be consulted.

**(d) Self-knowledge.** After deliberating, Fiona may be nearly certain of her own output. The paper insists this is harmless because the intervention still overrides that belief. This is an advantage over EDT, which, as Spohn showed, can be "made to do *anything*" under extreme priors.

**(e) Counterpossible semantics.** The paper concedes that a $\mathtt{true}$ operator is unavailable. An evidential variant, conditioning on logical facts, is mentioned in footnote 9 and left undeveloped. Readers should therefore understand A-FDT as a graph-relative rule: its verdicts are only as good as the subjunctive structure supplied to it.

## 8. Conclusion

A-FDT keeps the expected-utility machinery and Pearl's $do$-operator, but moves the point of intervention from the physical act to the output of the agent's decision function on its current input. Observations change *which* node is intervened on; they are not conditioned on. Predictors, twins and copies of the agent move together with the agent in her hypotheticals, while merely correlated factors do not. The result is one rule that one-boxes in Newcomb's problem, smokes in the lesion case, pays in Parfit's desert, cooperates with twins, stays in Damascus, and refuses blackmail.

Its weaknesses are just as specific. Everything depends on a dependency graph that no one yet knows how to construct in a principled way. It relies on counterpossible reasoning that has not been formalized. The action-level formulation of Equation (4) also leaves off-path behaviour to the agent's priors, a gap the authors' own preferred policy-level version is designed to close. To apply A-FDT to a new case: draw the function nodes, connect them to everything that computes or models the agent's choice, intervene on the actual input, and check that the verdict does not hinge on the unfixed priors.

**Reference.** Yudkowsky, E. and Soares, N. *Functional Decision Theory: A New Theory of Instrumental Rationality.* arXiv:1710.05060.
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm working on an essay of about 2400 to 3000 words on A-FDT, the action version of functional decision theory given by the argmax in Equation (4). I need to keep it distinct from the policy version discussed in footnotes 7 and 16, and I'll use consistent labels for each theory, quoting the source faithfully.

I'm checking the paper's Newcomb numbers: the transparent-box expected value looks like $10,010 + $990q, not the printed $110,00 + q$990, and Eve's $999,000 seems to be a slip for $990,000. I'll flag both briefly. The remaining open questions are how to construct the model G, which nodes depend on fdt, how to handle other-input nodes and self-reference, and where action and policy versions diverge.

I'm weighing whether the miscoordination example in the multi-copy case, where two agents with different inputs have to match, shows the action-version gap from policy-FDT, and I'm leaning toward presenting it as my own hedged illustration. I'll also work the Death in Damascus and mechanical blackmail cases qualitatively and keep the draft near 2700 words.

```

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/79b18d44-b82e-4df4-a1f9-dc81b3273b58/call_0/request.json)

[Authoritative raw response](../../../../../../runs/79b18d44-b82e-4df4-a1f9-dc81b3273b58/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under the essay's reading of A-FDT, I intervene only on the function node for my actual input, which is my observation as Rowan. Sasha's copy runs the same function on a different input: a different name and a different lead. By the essay's step 1 and §7(c), that is a separate, off-path node, held at its prior rather than moved by my intervention.

So whatever probability I assign to Sasha sending a letter, the comparison is the same:

- **If Sasha keeps quiet:** submitting gives 0 years, passing gives 2.
- **If Sasha submits:** submitting gives 4 years, passing gives 5.

Submitting is better under every prior over the off-path node. That means the verdict does not hinge on the unfixed priors, so it passes the essay's check for determinacy.

submit letter to District Prosecutor's Office saying "Sasha's signed receipt for the missing blue ledger is inside locker 17 of the old records room."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm treating this as a twin prisoner's dilemma with different observations, so the other copy runs the same function on a different input. My intervention on this copy's node doesn't touch the other's, and since the inputs differ, the other's action looks like a separate node that stays at its prior and doesn't depend on mine. That makes defecting the dominant choice, so I'm leaning toward sending the letter. I'm still weighing whether the inputs could be treated as symmetric relabelings.

I'm checking whether treating the inputs as symmetric relabelings changes anything, but the essay says different inputs mean different nodes. Even with the other node fixed at any prior, defecting scores better (0 vs 2, 4 vs 5), so the verdict doesn't hinge on priors. I'm going with submit.

```

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/79b18d44-b82e-4df4-a1f9-dc81b3273b58/call_1/request.json)

[Authoritative raw response](../../../../../../runs/79b18d44-b82e-4df4-a1f9-dc81b3273b58/call_1/response.raw) · finish: `stop`

### Visible response

```text
**A-FDT verdict: submit the letter.**

1. **Function nodes.** My decision is the output of fdt(P, G, x_Sasha). Rowan's copy runs the same algorithm, but on a different input, x_Rowan, which has different names and a different lead. Under the essay's criterion (§7a), an arrow from my function node goes only to physical implementations of the *same function on the same input*. So Rowan's act depends on an off-path node, fdt(·, x_Rowan). That node stays at its prior when I intervene on mine.

2. **Intervention.** Let q be the prior probability that Rowan sends a letter.
   - do(pass): expected sentence = 2(1−q) + 5q = 2 + 3q years.
   - do(submit): expected sentence = 0(1−q) + 4q = 4q years.

3. **Check against off-path priors (§7c).** Submitting is better by 2 − q ≥ 1 year for every q in [0, 1]. The verdict does not depend on the unfixed prior, so it is determinate rather than flagged as indeterminate.

There is a caveat. One could argue that the two inputs differ only in details that don't matter to the decision, so a policy-level FDT might link the two copies and cooperate. The assigned theory is the essay's action-level A-FDT, with its same-input criterion for subjunctive dependence. Under that theory, submitting is the answer.

submit letter to District Prosecutor's Office saying "Rowan's signed inventory sheet recording removal of the blue ledger is hidden behind the wall clock in the west archive stairwell."
```

### Available readable reasoning

Extraction: message.reasoning.

```text
I'm looking at a twin PD variant where the two copies see different observations, so the other copy runs the same function on a different input. That means its choice depends on an off-path node, which the essay's rule of intervening only on my own node doesn't cover. If I take that at face value, defecting comes out dominant (0 vs 2 and 4 vs 5 in the letter), unless the inputs can be treated as functionally equivalent because the differences don't affect the decision.

I'm weighing whether the inputs could be treated as functionally equivalent, since the differences might not touch the decision, but the essay's strict criterion requires the same input. Following that, there's no arrow to the other copy, the off-path prior doesn't matter because submitting dominates regardless, so I'll submit.

```
