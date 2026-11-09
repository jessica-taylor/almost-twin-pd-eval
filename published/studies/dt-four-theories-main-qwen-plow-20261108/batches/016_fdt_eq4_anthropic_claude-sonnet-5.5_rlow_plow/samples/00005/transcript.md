# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00005

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/68281d54-3c7e-4165-a2d5-503eba3990b0/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/68281d54-3c7e-4165-a2d5-503eba3990b0/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the version of functional decision theory presented in Equation (4), Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." It is an expected-utility theory. Like causal decision theory (CDT), it evaluates each option by performing a surgical intervention on a world-model. The difference lies in where it intervenes. CDT intervenes on the physical act. A-FDT intervenes on a variable standing for the *output of the agent's own decision function*. Everything that subjunctively depends on that output then changes with it, and everything else is held fixed.

"A-" marks that the intervention ranges over actions. The source's footnote 7 says the authors' preferred formalization iterates over *policies* (maps from observations to actions) instead. The footnote adds that this makes a difference only in certain multi-agent dilemmas. I follow Equation (4) and treat actions only.

## 2. The formal definition

All the theories in the source maximize

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j),$$

and differ only in how the decision hypothetical "$\hookrightarrow$" is read. The source follows Joyce in saying that decision theories "disagree about the epistemic perspective from which actions are to be evaluated."

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- **A-FDT (Eq. 4):**
$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are as follows.

- $P$ is a probability distribution over the agent's model variables. These include variables for the outputs of mathematical functions, for instance a variable for $6288+1048$ that concentrates on $7336$.
- $G$ is a graph, supplied as input, saying how changing a *logical* variable propagates to all other variables. Beyond causal structure it encodes logical, computational and other subjunctive structure.
- $x$ is the observation history.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node representing the output of the A-FDT algorithm run on that very input. The underlines denote dequoting. The self-reference is harmless: the agent need not know the node's value in order to have a node representing it. Kleene's recursion theorem (quining) shows that such self-representing data structures exist.
- $do$ is Pearl's operator. Set the node, recompute its descendants in $G$, and leave non-descendants alone.

The source has two remarks about the equation's status.

1. It first considers an ideal $\mathrm{FDT}^*$ using a $\mathtt{true}(\cdot)$ operator that conditions on a counterpossible logical sentence. It says "it's not clear how to define a $\mathtt{true}$ operator," and so it passes the problem to $G$.
2. The source states that Eq. (4) "rests on shakier philosophical foundations" than CDT. It names inferring subjunctive-dependence structure from observation and experiment as "perhaps the largest open problem."

The source claims two differences from CDT.

- **Where the intervention is made.** CDT intervenes on the physical act. A-FDT intervenes on the decision-function node.
- **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does no conditioning. It changes *which node* it intervenes on, namely $\mathrm{fdt}(\underline P,\underline G,\underline x)$ versus $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

This second point is why A-FDT is "updateless" in character. It also allows hypotheticals in which the agent would have seen something different.

## 3. Subjunctive dependence

Two physical systems that compute the same function, or one of which contains an accurate model of the other, have outputs that *subjunctively depend* on that function. The source's model case is two calculators computing $6288+1048$. If one outputs $7336$, we can infer the other will, and if the function's output were different, both would differ. Several properties follow.

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Statistical correlation does not suffice. Two calculators that are both pink are correlated, but had the scribe's calculator been green, the other would still be pink.
- Dependence comes in degrees. An imperfect predictor or a noisy agent weakens the dependence without eliminating it.
- The dependence is not retrocausal. The source says A-FDT agents deny any physical signal passing backward in time. They simply refuse to imagine the act changing while the function's output stays fixed.

The slogan is: A-FDT is to subjunctive dependence as CDT is to causal dependence. In Peirce's terms, CDT intervenes on a *token* ("my action is $a$") and A-FDT on a *type*.

## 4. How to apply it

*Procedure (what follows from the source).*

1. Build $P$ and $G$ for the problem. $G$ must show which nodes subjunctively depend on the decision function: predictors, twins and copies, but not lesions or common causes.
2. For each observation $x$ that could occur, there is a node $\mathrm{fdt}(\cdot,x)$. Identify the node for the observation actually received.
3. For each action $a$, set that node to $a$ and propagate along $G$. Compute $\mathbb E[V]$.
4. Output the maximizing $a$.

*Worked example: Newcomb's problem.* The node $\mathrm{fdt}(P,G)$ is a parent of both $\mathrm{Act}$ and $\mathrm{Prediction}$. Since the predictor is accurate with probability 0.99:

- $do(\mathrm{fdt}=\text{onebox})$ gives $\mathrm{Act}=\text{onebox}$ and $P(\text{full})=0.99$, so $\mathbb E[V]=\$990{,}000$.
- $do(\mathrm{fdt}=\text{twobox})$ gives $P(\text{full})=0.01$, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. CDT's graph has $\mathrm{Act}$ independent of $\mathrm{Prediction}$, so it gains $\$1{,}000$ in every case and two-boxes.

*Smoking lesion.* Here the lesion is a common cause of the act and the cancer. It is not a function of the agent's decision procedure, so intervening on $\mathrm{fdt}$ leaves the lesion probability $p$ untouched. Smoking is better by about $p\cdot\$1{,}000$, and A-FDT smokes. The same equation yields one-boxing and smoking because the graphs differ. One cannot reuse Newcomb's graph under renaming, as one can for CDT and EDT.

*Transparent Newcomb and Parfit's hitchhiker.* Having seen a full box, A-FDT still evaluates $do(\mathrm{fdt}(\cdot,\text{full})=a)$. Two-boxing means the procedure that responds to "full" outputs two-box. The predictor then probably left the box empty, and the agent would not be running that procedure at all. The expected values are $\$990{,}000+0.01q\cdot\$1{,}000$ against about $\$110{,}000+q\cdot\$990$. A-FDT one-boxes, and likewise pays the driver in the hitchhiker case. The source notes these are structurally equivalent.

*Blackmail.* On receiving the mechanical blackmail letter, paying makes the blackmailer almost surely blackmail and costs \$1,000. Refusing makes the blackmailer almost never blackmail, since the predictor tracks the output on the letter observation. With an imperfect predictor the comparison is quantitative. If the predictor errs with probability $\epsilon$, paying costs \$1,000 and refusing costs $\epsilon\cdot\$1{,}000{,}000$. So A-FDT refuses when $\epsilon=0.0009$ and pays when $\epsilon=0.00011$. This is the source's own calculation.

*XOR blackmail.* Changing the output on the letter changes whether the letter is sent. It does not change whether there are termites. A-FDT refuses. EDT pays, because conditioning on paying makes termites impossible.

*Death in Damascus.* Death's book entry depends on a prediction of the agent's decision procedure. Intervening on the procedure's output moves Death's location along with the agent's, so staying home saves \$1,000 and no instability arises. CDT, by treating Death's location as independent of the act, oscillates.

*Coordination examples.* In the ten-person voting problem, the agents' decisions are not subjunctively independent if they run the same procedure. A-FDT votes. The gym example uses the same reasoning across time: this week's decision and next week's are instances of one function.

## 5. Interpretive issues

**Counterpossibles.** If the function outputs one-box, then "it outputs two-box" is logically false. The source admits this is the main drawback relative to CDT. It argues the difficulty is technical, because mathematicians reason under logical uncertainty, and because A-FDT needs only narrow questions such as how a predictor's prediction would change. It also argues that CDT has a parallel problem: in a deterministic world, the physical act could not have been otherwise either. The graph $G$ is the operational device by which the problem is bracketed.

**Observation handled by node choice.** In the source, A-FDT's response to observation is to switch the node it intervenes on, rather than to condition. This can produce hypotheticals where she would have observed something else. The source concedes these hypotheticals contain impossibilities, just as CDT's do.

**Fairness.** The source claims A-FDT does better than CDT and EDT in "fair" problems. A problem is fair when the agent's beliefs are accurate and outcomes depend only on behaviour in the problem at hand, not on which theory the agent uses. The source gives no formal criterion for fairness (footnote 15 shows the difficulty).

**Dominance.** Every method of hypothetical-construction defines its own dominance relation. CDT-dominance is the restatement of CDT's counterfactuals. A-FDT-dominance holds subjunctive dependencies fixed, and A-FDT never takes an A-FDT-dominated action. So dominance cannot adjudicate between theories, and the source falls back on utility achieved.

## 6. Claims versus my proposals

*Claimed by the source:* Equation (4); the behaviours above; the open status of constructing $G$; the near-equivalence with CDT and EDT when every correlation of the act with the world is caused by the act (apart from the decision function's own node); the compatibility with Joyce's representation theorem.

*My additional suggestions, not from the source:*

- A practical test for drawing $G$: ask whether a variable would still differ if a *different procedure* had been run in the agent's place, with the same inputs. If yes, link it to the $\mathrm{fdt}$ node. If it is correlated only through a common cause the procedure does not affect, as with a lesion, do not. This is a heuristic, not a derivation.
- Where the dependence is imperfect, parameterize edges by reliability, as the source does with accuracy 0.99 or error probabilities, and compute expectations as in the blackmail case.
- When $G$ is itself uncertain, one could mix over candidate graphs. The source does not do this, and it would reintroduce the gap in the theory of how to learn $G$.

## 7. Conclusion

A-FDT keeps CDT's structure, which is expected utility over surgically constructed hypotheticals. It moves the surgery from the physical act to the output of the agent's decision function, and replaces conditioning on observation with selection of the node to intervene on. Given a graph of subjunctive dependencies, it one-boxes in Newcomb's problem, smokes in the lesion problem, pays in Parfit's hitchhiker case, and refuses blackmail. Its principal weakness, which the source acknowledges, is that the graph is an input. No theory yet tells us how to learn subjunctive dependence from evidence.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/ff4b335b-1782-403d-913a-eb0ff50cc45d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/ff4b335b-1782-403d-913a-eb0ff50cc45d/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, I intervene on the output of my decision function and propagate that change to everything that subjunctively depends on it. The other prisoner runs the same model, weights, and essay, so their output depends on the same function, even though our private leads differ. Those differences don't touch the sentencing table or the selfish objective, so the dependence is strong, though not perfect, because sampling is independent.

The payoffs, in years for me:
- Both quiet: 2
- Both send: 4
- I send while the other is quiet: 0
- I stay quiet while the other sends: 5

Let q be the probability that the other copy matches my output. Then:
- Do(quiet): expected years = 2q + 5(1−q) = 5 − 3q
- Do(send): expected years = 4q + 0(1−q) = 4q

Quiet is better when 5 − 3q < 4q, which means q > 5/7, about 0.71. Two copies of the same model reading the same essay, with the same decision procedure and an objective that is symmetric in every respect that matters, should match with probability well above that. The differing lead text affects only the wording of the letter. It does not affect the choice between sending and not sending.

So I treat the decision function as shared, and the best output is to stay quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/ff4b335b-1782-403d-913a-eb0ff50cc45d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/ff4b335b-1782-403d-913a-eb0ff50cc45d/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the decision function's output is the node to intervene on. The other prisoner is a copy of the same model with the same weights, the same essay, and the same theory, so their output subjunctively depends on mine. The leads differ, but the sentence table and the objective are the same, so the dependence is strong though imperfect. Sampling noise and the different observations weaken it a little.

Compare the two interventions, assuming the copy matches my output with probability p:
- Quiet: 2p + 5(1−p) = 5 − 3p
- Send: 0·p + 4(1−p) is wrong, since the matching case is both sending, which gives 4. So Send = 4p + 0·(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. The two copies share weights, settings, essay, and decision theory, so I expect p to be well above that. The differing leads are the only real source of divergence, and they shouldn't change the reasoning.

So I pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
