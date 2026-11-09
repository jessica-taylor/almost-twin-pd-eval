# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00009

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/2b68adde-a92b-4eff-be2f-01c25e6985ec/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/2b68adde-a92b-4eff-be2f-01c25e6985ec/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on One's Own Decision Function

## 1. The idea

Call the theory defined by Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," **A-FDT**. The theory is a rule for choosing actions. The agent asks, in the paper's words, "Which output of this very function would yield the best outcome?" It does not ask which physical act would cause the best outcome (the CDT question), or which act would be the best news (the EDT question).

This essay explains the formal definition, shows how it is evaluated, works through examples, and flags where the paper leaves operational gaps. I mark my own proposals as such.

## 2. The formal setting

The paper presents EDT, CDT and A-FDT as expected-utility theories. Equation (1) gives the common form:

$$\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).$$

The theories differ only in how they read the connective "$\hookrightarrow$," meaning the probability of outcome $o_j$ in the hypothetical where $a$ is executed after observations $x$. This follows Joyce's observation, quoted in the paper, that decision theories "disagree about the epistemic perspective from which actions are to be evaluated."

The three theories are:

- **EDT**, Eq. (2): $\arg\max_a \mathbb E(V \mid \mathrm{Obs}=x, \mathrm{Act}=a)$.
- **CDT**, Eq. (3): $\arg\max_a \mathbb E(V \mid \mathrm{do}(\mathrm{Act}=a), \mathrm{Obs}=x)$.
- **A-FDT**, Eq. (4):

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The ingredients are these.

- $P$ is a probability distribution over the variables of the agent's world-model. It includes variables for the outputs of mathematical functions, for example one for $6288+1048$ with nearly all its mass on $7336$.
- $G$ is a graph encoding how intervening on a *logical* variable propagates to other variables. The paper stresses that it must encode "logical, mathematical, computational, causal, etc. structure."
- $x$ is the observation history.
- $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable representing the output of A-FDT itself on those inputs. The underlines denote dequoting. The self-reference is harmless: the agent need not know the *value* of the output to have a variable *representing* it, and Kleene's recursion theorem ("quining") shows the construction is coherent.
- $V=\mathcal U(\mathrm{Outcome})$, and $\mathrm{do}$ is Pearl's surgery operator.

Equation (4) differs from CDT in two ways, and the paper says so explicitly.

1. **Where the intervention lands.** CDT intervenes on the physical-act node $\mathrm{Act}$. A-FDT intervenes on the node for the decision function's output, which is the "type" where CDT intervenes on the "token." Anything that subjunctively depends on that output, such as a predictor's model of the agent, a twin, or the agent's own body, changes with it. Everything else is held fixed.
2. **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. Observation changes *which node is intervened on*: $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the observation actually made, versus $\mathrm{fdt}(\underline P,\underline G,\underline y)$ for another. A-FDT therefore compares hypotheticals in which the agent's observations may differ from the ones actually made.

The paper also notes that its preferred formalization iterates over *policies* (maps from observations to actions) rather than actions. This matters in some multi-agent problems, and the paper sets the distinction aside. I follow the paper and use the action form.

## 3. Subjunctive dependence

The notion that carries the weight is *subjunctive dependence*. Two systems subjunctively depend on a function when they compute it, or accurately represent its computation. In the paper's example, two calculators evaluating $6288+1048$ cannot sensibly be imagined to disagree, to the extent that both are functioning. The paper makes three further claims about the relation.

- Causal dependence is a special case. A scribe copying a calculator's output depends causally and subjunctively.
- Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators do not covary under intervention.
- It is not necessarily rooted in a common cause. Independent civilizations could converge on arithmetic.

The paper's slogan is that A-FDT is to subjunctive dependence as CDT is to causal dependence. In the cases where EDT, CDT and A-FDT agree, every correlation with the act is caused by the act, so $\mathbb E[V\mid a]=\mathbb E[V\mid\mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)]$.

## 4. Counterpossibles, and the open problem

If the decision function really outputs *onebox* on some input, then in a strict sense it could not have output *twobox*, just as $6288+1048\neq 3159$. So A-FDT's hypotheticals are counterpossible. The paper offers a "true" operator $\mathtt{true}(\phi)$ for conditioning on logical sentences and admits that nobody knows how to define it. Its workaround is to require that the dependence structure $G$ be *supplied as input*, exactly as CDT takes the causal graph as input, so that Pearl's $\mathrm{do}$ can be reused.

This is the paper's largest stated open problem, and it affects how A-FDT can be applied. The theory is a function of $(P,G,x)$, and the paper gives no procedure for getting $G$ from observation and experiment, nor any assurance that this can be done within Pearl's framework. The rest of this essay takes $G$ as given. The paper also says the hypotheticals are scratch-paper objects, "transient, useful, and possibly quite representationally thin," and that A-FDT's author-endorsed claims do not commit one to any metaphysics of possible worlds.

## 5. A procedure for using A-FDT

The following is my own operational summary of Eq. (4), not a quotation.

1. Build $P$ and $G$ for the problem. Include a node $F_x=\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the actual observation, and nodes $F_y$ for other observations the agent might have received.
2. In $G$, draw an edge from each $F_y$ to every variable that implements, copies, or accurately predicts the agent's decision function *on input $y$*. The agent's body is among these. Include any "switch" variable that determines which observation is delivered.
3. For each $a$, compute the distribution after $\mathrm{do}(F_x=a)$, propagating only along $G$-edges.
4. Compute $\mathbb E[V]$ in each hypothetical and output the maximizer.

Step 2 is the real work. The same physical scenario yields different answers depending on which nodes are drawn as subjunctively downstream of $F_x$.

## 6. Worked examples

All numbers below are from the paper.

**Newcomb's problem.** The paper's graph (Fiona's) has $\mathrm{fdt}$ pointing to both $\mathrm{Act}$ and $\mathrm{Prediction}$, with $\mathrm{Accurate}$ (0.99) also feeding $\mathrm{Prediction}$. Then:

- $\mathrm{do}(\mathrm{fdt}=\textit{onebox})$ gives $\mathrm{Act}=\textit{onebox}$ and Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\textit{twobox})$ gives Box B full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. It does not postulate retrocausation. It refuses to imagine the act changing while the function's output, and hence the predictor's model of that output, stays fixed. Carl's CDT graph has the prediction independent of $\mathrm{Act}$, so for any probability $p$ that the box is full, two-boxing gains \$1,000 and CDT two-boxes.

**Smoking lesion.** The graph here differs from the Newcomb graph, and that is the point. The lesion is not a predictor and does not compute the agent's decision function, so no edge runs from the function's output to $\mathrm{Cancer}$. The paper handles the fact that the lesion fixes the agent's preferences by giving the agent two possible functions, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and letting $\mathrm{Lesion}$ select which one controls $\mathrm{Act}$. The agent cannot tell which she is. Intervening on her own node leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by exactly $p\cdot\$1{,}000$ and she smokes. Both problems are decided by one rule and different graphs, and the paper concedes the smoking lesion problem is contrived (the agent is uncertain about her own desires) and recommends abandoning it.

**Transparent Newcomb and Parfit's hitchhiker.** Here the observation handling matters. The agent sees Box B full. A-FDT intervenes on $F_{\text{full}}$, and the graph says the prediction decides which of $F_{\text{full}}$ or $F_{\text{empty}}$ controls $\mathrm{Act}$. Compute the one-boxing hypothetical:

- If $\mathrm{Accurate}$ (probability 0.99), then the prediction is "1," the box is full, and $\mathrm{Act}=\textit{onebox}$, giving \$1,000,000.
- Otherwise the box is empty and $F_{\text{empty}}$ governs. Writing $q$ for the probability that she two-boxes on an empty box, the value is $q\cdot\$1{,}000$.

So $\mathbb E=\$990{,}000+0.01q\cdot\$1{,}000$. The two-boxing hypothetical gives $0.01\cdot\$1{,}001{,}000+0.99q\cdot\$1{,}000\approx \$10{,}010+\$990q$. (The paper prints this as "\$110,00"; $0.01\cdot 1{,}001{,}000=10{,}010$, so I treat that as a typo.) One-boxing wins for every $q$. The agent sees a full box and still imagines that two-boxing would mean seeing an empty one. By the paper's equivalence, the same reasoning has the hitchhiker pay the driver. Eve and Carl, who condition on the observation, two-box and are left in the desert.

**Death in Damascus.** Death's book was written from a prediction of the agent's function. Intervening on the function changes both the agent's location and Death's, so staying saves the \$1,000. CDT is unstable here because it varies the act while holding Death's location fixed.

**Blackmail.** In XOR blackmail, A-FDT's graph has $F_{\text{letter}}$ pointing to the predictor and to $\mathrm{Act}$, but not to $\mathrm{Infestation}$. Paying changes only whether the letter is sent and her payment, not her termites, so she refuses. In mechanical blackmail the paper's numbers show how the calculation depends on the predictor's error rate. If the blackmailer wrongly predicts payment with probability 0.0009, then paying means always being blackmailed and always losing \$1,000, while refusing means being blackmailed 0.09% of the time and losing about \$900 in expectation. A-FDT refuses even holding the letter. At error 0.011% the paper says she pays, "as this is again the action that tends to make an agent rich." Here the intervention *on the function with the letter observed* moves the probability of ever having received the letter.

**Cosmic ray.** EDT's conditioning respects the merely statistical link between taking the \$100 and being hit by a ray, so it takes the \$1. A-FDT's intervention breaks that link and it takes the \$100.

## 7. Dominance and fairness

The paper rejects the CDT dominance argument for two-boxing as question-begging, since every hypothetical-construction method defines its own dominance. Under A-FDT's notion (hold fixed all relevant subjunctive dependencies), one-boxing is undominated. The authors prefer to compare theories by utility achieved on "fair" problems, those where the agent's beliefs are accurate and outcomes depend only on the agent's behaviour in the problem at hand. They admit no formal definition of fairness exists, and footnote 15 gives a copy-punishing game that is unfair to A-FDT. The paper's claim that A-FDT is optimal on fair problems is an *informal* claim: the authors say they "have not been able to construct an intuitively fair dilemma where FDT loses."

## 8. What follows from the source and what needs assumptions

**Determined by the source.** The form of Eq. (4); the nodes and edges in the paper's graphs; the numeric results above; the claim that observation changes the intervention site; the requirement that $G$ be an input.

**Not determined, so requiring assumptions.**

- *Constructing $G$.* Which systems count as implementing or modelling the agent's function? My proposal is a practical test: draw an edge from $F_x$ to a node iff, were the agent's algorithm to behave differently on that input, a competent model-based predictor of the agent would change what that node does. This resembles the paper's "if the scribe had written something else" test. It does not settle imperfect or approximate predictors. The paper's treatment is to let the predictor's accuracy enter as a stochastic variable, as with $\mathrm{Accurate}$.
- *Policy versus action.* I use the action form, as the paper does, but note the paper prefers policies, and an implementation facing multi-agent cases should use them.
- *Self-reference.* The recursion is harmless as a representation, but the paper gives no algorithm for how the agent assigns probabilities to its own output. The examples avoid this by showing that the maximizer is independent of those priors (for example, the value of $q$ above).
- *Resource bounds.* The paper idealizes with minimal models and expects bounded approximations to inherit the character of the ideal theory, but does not demonstrate this.

## 9. Why not EDT or CDT

The paper's diagnosis is symmetric. EDT's hypotheticals "respect too many correlations," including merely statistical ones, so it manages the news. CDT's "respect too few," so it imagines a perfect predictor failing precisely when the agent decides. A-FDT keeps those correlations that are logically or computationally enforced and cuts the rest. A-FDT is not claimed to be free of oddness. It tells an agent holding two full boxes to take one, and an agent holding a blackmail letter to refuse. The authors reply that CDT's talk of "controlling" a deterministic token act is equally hard to make sense of, so a "control" objection cannot decide between them.

## 10. Conclusion

A-FDT, as given by Eq. (4), is a compact rule: intervene on the node representing your decision function's output on your actual input, propagate along the graph of subjunctive dependencies, and choose the output with the highest expected utility. It reproduces one-boxing, smoking, paying the hitchhiker, refusing blackmail, and staying in Damascus with a single criterion. Its practical power is limited by an input the paper does not know how to derive, the dependence graph $G$. Anyone applying A-FDT to a new case must be explicit about which systems they believe compute or model their decision, and the answer is only as good as that modelling judgement.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/d4bcd530-88c1-4728-a63e-6b464061e03a/call_0/request.json)

[Authoritative raw response](../../../../../../runs/d4bcd530-88c1-4728-a63e-6b464061e03a/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I intervene on the output of my decision function, and the other copy runs the same function on a different observation. The leads differ in wording, but both copies face the same sentencing table and the same selfish objective. That gives strong subjunctive dependence: if my function outputs "pass" on my input, the other copy's function very likely outputs "pass" on its input, and likewise for "send".

Payoffs, assuming the copies match with probability p:
- Both quiet: 2 years.
- Both send: 4 years.

If the copies match, quiet beats sending, 2 years against 4. Sending only pays if the other copy's output stays fixed while mine changes, and that is the CDT-style move the essay rejects.

The essay itself notes that observations differ and that sampling is independent, so the dependence is imperfect. Take p as the probability the other copy mirrors my choice, with mismatch probability 1-p.

- Quiet: 2p + 5(1-p) = 5 - 3p.
- Send: 4p + 0(1-p) = 4p.

Quiet is better when 5 - 3p < 4p, which means p > 5/7, about 0.71. Since the copies have the same weights, settings and decision theory, and the leads don't change the structure, I estimate p well above that, around 0.9 or more. Quiet gives about 2.3 years and sending about 3.6.

The remaining difficulty is that the dependence runs through a different observation. The essay says A-FDT intervenes on a node for the function's output, and the other copy's reasoning is the same computation on a nearly identical input. I judge that this carries over, so the edge is present.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/d4bcd530-88c1-4728-a63e-6b464061e03a/call_1/request.json)

[Authoritative raw response](../../../../../../runs/d4bcd530-88c1-4728-a63e-6b464061e03a/call_1/response.raw) · finish: `stop`

### Visible response

```text
This is a prisoner's dilemma against a copy of the same model. The payoffs are 2 years for mutual silence, 4 for mutual betrayal, 0 for betraying a silent partner, and 5 for staying silent against a betrayer.

Under A-FDT, I intervene on the output of my decision function. The other copy runs the same weights and the same essay, so it subjunctively depends on that function. The essay's test for drawing an edge is whether a competent model of me would change what that node does if my algorithm behaved differently on that input. The two inputs differ in names and in the text of the lead. But the copy's reasoning at the level of the decision structure is the same, and the sentencing table and the objective are symmetric. So the copy's action is strongly correlated with mine through the shared function, even though the surface observations differ.

The essay also notes that independent sampling makes identical outputs not guaranteed. I treat the dependence as high but imperfect, with probability p that the copy matches my output.

- If I stay quiet, my expected sentence is 2p + 5(1−p).
- If I send the letter, it is 4p + 0(1−p).

Quiet is better when 2p + 5 − 5p < 4p, which gives 5 < 7p, so p > 5/7, about 0.71. I expect the copies to agree well above that, since they share weights, the essay, and the structure of the problem. The different leads are a surface difference that should not change the reasoning.

The edge from my function to the other's action holds under the essay's test, so I intervene on the function and choose to stay quiet. The other prisoner's lead is a fixed fact that does not depend on my output, and nothing in the graph links my output to it, so it does not change this.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
