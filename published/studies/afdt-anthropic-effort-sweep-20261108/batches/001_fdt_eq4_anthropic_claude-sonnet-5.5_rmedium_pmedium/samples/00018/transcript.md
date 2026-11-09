# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00018

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/667898bb-27bc-494d-92bd-2b70d59d1231/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/667898bb-27bc-494d-92bd-2b70d59d1231/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The core idea

Call the decision theory presented as Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," **A-FDT**. Its slogan is that one should treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" It is an expected-utility theory. It differs from causal decision theory (CDT) and evidential decision theory (EDT) only in how it builds the hypothetical scenario used to evaluate each action.

This essay covers the formal definition, the notion of dependence it needs, worked cases, and the places where the source stops short of a full specification. I label my own additions as such.

## 2. The formal setting

The paper's shared template (Equation 1) is that a theory prescribes the action maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

Here $a$ is an action, $x$ an observation history, and $\hookrightarrow$ the connective for "decision hypotheticals." The theories "disagree about the epistemic perspective from which actions are to be evaluated" (Joyce, quoted in the source). Each agent keeps a world-model $M$ and, for each action, builds a hypothetical $M^{a\hookrightarrow}$ from it. The agent computes $V_a$ from that hypothetical and takes the argmax.

- EDT (Eq. 2): $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. Hypotheticals are built by conditioning.
- CDT (Eq. 3): $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. Hypotheticals are built by Pearl-style surgery on the physical act node.
- **A-FDT (Eq. 4):**

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\;\Big|\;\mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over the model's variables. It includes variables for outputs of mathematical functions, such as the value of $6288+1048$.
- $G$, a graph recording "how changing a logical variable affects all other variables." It encodes causal, logical, computational and other structure.
- $x$, the observation history.

The underlines indicate dequoting. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node in the model that represents the output of the A-FDT procedure run on exactly these inputs. This is self-reference. The paper argues it is harmless: the agent need not know the value of the node to have a variable representing it, and Kleene's second recursion theorem ("quining") shows how a data structure can contain accurate representations of itself.

**Two differences from CDT.** The paper names exactly two.

1. A-FDT intervenes on the node for the decision function's output, not on the node for the physical act.
2. A-FDT does not respond to observations by conditioning. It responds by changing which node it intervenes on. When the observation changes from $x$ to $y$, it switches from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second point matters. Observing something never lets A-FDT update away possibilities in which it would have observed something else. It stays "updateless" in that sense, and it still behaves differently in response to evidence.

**Policies.** The paper's footnotes say the authors' preferred formalization intervenes on a policy, a map from observations to actions, which the agent then applies to its actual input. The paper does not need this distinction for its examples, and neither does this essay. The footnote notes the difference matters in some multi-agent dilemmas.

## 3. Subjunctive dependence

The graph $G$ must say what depends on the function's output. The paper calls this relation **subjunctive dependence**. Two systems subjunctively depend on a function when both compute it, as two calculators computing $6288+1048$ do. Three facts about the relation:

- Causal dependence is a special case. A scribe copying a calculator's output depends on it both causally and subjunctively.
- Mere statistical correlation does not suffice. Two calculators that happen to be pink do not subjunctively depend on each other's color.
- The relation weakens, but does not vanish, when predictions are imperfect or the agent is nondeterministic.

The slogan is: A-FDT is to subjunctive dependence as CDT is to causal dependence. CDT holds fixed everything not causally downstream of the act. A-FDT holds fixed everything that does not subjunctively depend on the function's output. In Peirce's terms, CDT intervenes on a token ("my act is $a$") and A-FDT on the type.

Since a function has one output on a given input, the hypothetical in which it outputs something else is a **counterpossible**. The paper concedes that lacking a satisfactory account of counterpossible reasoning is "the main drawback" of the theory relative to CDT. Its workaround is Equation 4 itself. If a graph $G$ is supplied that encodes how logical variables propagate, Pearl's $\mathtt{do}$ operator can be reused and no separate $\mathtt{true}(\cdot)$ operator is needed. The source also admits that deducing the structure of subjunctive dependence from observation and experiment is "perhaps the largest open problem" for the theory.

## 4. Applying A-FDT: a recipe

A-FDT requires the following steps.

1. Build $P$ and $G$ for the problem. Include a node $F_x$ for the output of the decision function on the observed input.
2. Mark which variables are fixed by the environment. Mark which depend on $F_x$: the act, predictions of the agent, copies of the agent, and anything downstream of these.
3. For each $a$, set $F_x=a$, propagate the change along the graph, and leave the rest alone.
4. Compute $\mathbb E[V]$ in each hypothetical and choose the best $a$.

Step 2 is where A-FDT differs from the other theories. Steps 3 and 4 are routine.

## 5. Worked examples

**Newcomb's problem.** The nodes are $F$, Act, Prediction, Accurate (0.99), Box B and $V$. The edges run $F\to$ Act and $F\to$ Prediction, with Prediction and Act both feeding $V$ through Box B. Intervening with $F=\text{onebox}$ makes the act one-box and the box full with probability 0.99, so $\mathbb E V=\$990{,}000$. Setting $F=\text{twobox}$ gives $0.01\cdot 1{,}001{,}000+0.99\cdot1{,}000=\$11{,}000$. A-FDT one-boxes. No retrocausal physics is invoked. The agent just declines to imagine the act changing while the prediction of that act stays the same.

**Smoking lesion.** The structure differs, and this is why A-FDT can one-box and smoke. The lesion causes both the preference for smoking and cancer. The decision function depends on the lesion (through the agent's utility function), but cancer does not depend on the function's output. The paper models this with two possible functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, one for each utility function, and the lesion selects which one drives the act. Intervening on the function leaves the probability of the lesion fixed at $p$. Smoking then beats refraining by $p\cdot\$1{,}000$ and A-FDT smokes. The paper also points out that the problem is contrived because the agent is ignorant of her own preferences.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees a full box. A-FDT intervenes on $F_{\text{full}}$, the function's output on the input "full". In the graph, $F_{\text{full}}$ is what the predictor models, and Prediction decides whether Act is governed by $F_{\text{full}}$ or $F_{\text{empty}}$. Setting $F_{\text{full}}=\text{onebox}$ gives about $\$990{,}000+0.01q\cdot\$1{,}000$. Here $q$ is the agent's probability of two-boxing on seeing an empty box. Setting it to twobox gives $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000$. One-boxing wins whatever $q$ is. So when A-FDT imagines two-boxing, it imagines a world where it probably saw an empty box. The paper notes that one-boxing here is "precisely equivalent" to paying in Parfit's hitchhiker.

**Mechanical blackmail.** A-FDT holds the letter and compares paying with refusing. If it pays, it is blackmailed with probability about 1 and loses $1{,}000. If it refuses, the blackmailer almost never sends the letter. With a blackmailer who errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against $1{,}000$ for paying, so A-FDT refuses even though it "knows" this particular prediction was wrong. If the error rate were 0.011%, the expected loss from refusing would be $\$1{,}100>\$1{,}000$ and it would pay. The paper states both thresholds.

**Death in Damascus.** Death's book depends on a prediction of the decision function, so the intervention changes Death's location along with the agent's. Staying in Damascus saves the $1{,}000$ and A-FDT stays. CDT, which holds Death's location fixed under intervention, is unstable.

**XOR blackmail and the cosmic-ray problem.** In XOR blackmail, A-FDT refuses to pay. Changing the function's output changes whether the letter arrives, but not whether the house has termites. EDT pays because it conditions on good news. In the cosmic-ray problem, A-FDT takes the $\$100$ because it can break the merely statistical correlation between taking $\$100$ and being hit by a ray.

**Cases of agreement.** If every correlation with the act is caused by the act, with the possible exception of subjunctive dependence on the function itself, then $\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)]$. All three theories then agree. They differ only when something such as a predictor or twin correlates with the action without being caused by it.

## 6. Why intervene at all: motivation

The paper's complaint about the other theories is about their hypotheticals. EDT respects too many correlations, including merely statistical ones, and so "manages the news." CDT respects too few. In Newcomb's problem against a perfect predictor, CDT answers "what if I had one-boxed?" with a scenario in which a perfect predictor erred. A-FDT keeps "all decision-relevant subjunctive dependencies" and breaks the rest.

The paper's main case is the argument from utility. Predictors can see how each theory behaves, so CDT and EDT agents will mostly face empty boxes in the transparent problem and A-FDT agents mostly full ones. A supporting argument is that A-FDT always acts as it would have precommitted to act, so it needs no costly binding precommitments. The paper adds that A-FDT never assigns negative value to information.

Two objections have replies in the paper.

- **Dominance.** Every method of constructing hypotheticals induces its own notion of dominance. A-FDT never takes an action dominated in the A-FDT sense, so appealing to CDT-dominance begs the question.
- **Fairness.** One can design problems that punish a decision procedure as such, for example "reward agents that follow EDT." The paper counts a problem as "fair" if the outcome depends only on the agent's behavior in the dilemma at hand, and says Newcomb's predictor "punishes two-boxers," not CDT agents. It admits there is no formal definition of fairness and gives a copy-of-Fiona counterexample to naive attempts. Its claim that A-FDT does best in fair problems is therefore an empirical impression, not a theorem.

## 7. What the source leaves open, and a proposed reading

**Open in the source.**

1. How to construct $G$, in particular which variables subjunctively depend on the function. The paper supplies $G$ by hand in each example.
2. A $\mathtt{true}(\cdot)$ operator or logical-conditioning alternative. The paper says there is no definition of conditioning on false logical sentences.
3. How the agent assigns probabilities involving its own function's output, since $P$ must contain the variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$. The source says only that this is harmless because the agent need not know its value.
4. A formal criterion of fairness and of optimality.

**My operational interpretation (not the paper's).** Here is a heuristic for choosing which variables to make dependent on the function. For each variable $Z$, ask whether $Z$'s value is produced by a process that *models, simulates or copies* the agent's decision procedure, or by a process whose behavior is fixed regardless of what the agent's procedure outputs. Only the first kind gets an edge from $F$. This is what separates the predictor from the lesion in the examples above. A rough dependence strength can then be read as the reliability of the modeling process, and this reproduces the paper's numerical treatment of imperfect predictors ($0.99$, $0.0009$ error rates). I would also recommend drawing the graph at the level of policies, because observation-dependent nodes such as $F_{\text{full}}$ and $F_{\text{empty}}$ already treat it that way, and the footnotes endorse that reading. A caveat is that this heuristic only formalizes the examples. It is not a derivation of subjunctive dependence from data, which the paper identifies as unsolved. Different modelers can draw different graphs and obtain different answers, so A-FDT's recommendations are only as determinate as the supplied $G$.

## 8. Wider applications the paper sketches

- **Twin prisoner's dilemma.** The twin runs the same function, so $F=\text{cooperate}$ gives $\$1{,}000{,}000$ and $F=\text{defect}$ gives $\$1{,}000$. A-FDT cooperates.
- **Voting coalitions.** Agents who share a decision procedure are not subjunctively independent, so they vote.
- **Intertemporal self-control.** If today's decision resembles next week's, the same function governs both, and going to the gym today supports going next week.
- **AI systems.** Copyable and predictable programs often face Newcomblike situations.

## 9. Conclusion

A-FDT keeps expected-utility maximization and changes only the hypothetical: intervene on the output of one's own decision function and let everything that depends on that output vary with it. This gives one rule that one-boxes, smokes, pays the hitchhiker, refuses blackmail, and stays put in Damascus. It also makes decisions responsive to observation by switching which node is intervened on, not by conditioning. Its main cost is that the dependence graph $G$ must be supplied, with no principled method yet for deriving it, and the counterpossible reasoning it requires is only formalized through that supplied graph. The paper's case for A-FDT rests on utility achieved in fair problems, and the fairness criterion is informal. A-FDT is therefore a well-defined procedure given $G$ and an incompletely justified one about $G$ itself.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/24393adb-d955-45b1-8087-1b6894992477/call_0/request.json)

[Authoritative raw response](../../../../../../runs/24393adb-d955-45b1-8087-1b6894992477/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, my decision function's output is shared with the other copy. We run the same model and weights with the same essay and the same theory. Our observations differ only in names and in the wording of the lead. Those differences don't affect the sentence table, so the other copy's output is subjunctively dependent on mine, though not perfectly, since sampling is independent.

Intervening on the function, I compare the two outcomes:
- If the function outputs pass, the other copy very likely passes too, and I get 2 years.
- If the function outputs send, the other copy very likely sends too, and I get 4 years.

Suppose the other copy matches me with probability p. Passing costs 2p + 5(1-p). Sending costs 4p + 0(1-p). Passing is better when 5 - 3p < 4p, which means p > 5/7, about 0.71. The copies share weights, prompt structure and reasoning, so I expect the match rate to be well above that. Passing wins.

The essay's twin prisoner's dilemma example also says A-FDT cooperates, which here means staying quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/24393adb-d955-45b1-8087-1b6894992477/call_1/request.json)

[Authoritative raw response](../../../../../../runs/24393adb-d955-45b1-8087-1b6894992477/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT as the essay describes it, the other prisoner's choice depends on the same decision function that I am running. The two copies have different private leads, but the sentencing table and the objective are identical, so the function's output should be the same on the relevant input. That gives the function a subjunctive link to the other prisoner's choice.

Payoffs for me, with the other copy's action tracking mine:
- If both of us keep quiet, I get 2 years.
- If both of us send the letter, I get 4 years.

The mixed cells (0 years if I send and they stay quiet, 5 years if I stay quiet and they send) are only reachable if the copies diverge. Independent sampling and the different leads make divergence possible, but the essay's heuristic treats the other copy as a process that models or runs my procedure, and that is a strong dependence.

Setting the function's output to "pass" gives about 2 years, since the copy likely passes too. Setting it to "send" gives about 4 years. Divergence only shifts this a little. Suppose the copy matches me with probability p. Passing costs 2p + 5(1−p), and sending costs 4p + 0(1−p). Passing is better when 2p + 5 − 5p < 4p, which is 5 < 7p, so p > 5/7. Both copies run the same weights and the same essay, and the table and objective are the same, so I judge the match probability to be well above 0.71.

I choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
