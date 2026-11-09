# 016_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00014

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/b4393dc8-106d-4847-81fd-865c87b43618/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/b4393dc8-106d-4847-81fd-865c87b43618/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

A-FDT is the decision theory whose formal statement is Equation (4) of Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." This essay takes that equation as definitive. It explains what the equation says, how to use it, and where it needs more input than the paper supplies. I mark my own proposals as such.

The core principle, in the paper's words, is to "treat one's decision as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A-FDT is an expected-utility theory. It differs from its rivals in how it builds the hypothetical scenario used to evaluate each option.

## 2. The common framework

All three theories compared in the paper maximize

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j).$$

They differ in how they read the connective "$\hookrightarrow$". The paper follows Joyce's remark that decision theories disagree about "the epistemic perspective from which actions are to be evaluated," not about value.

Operationally, an agent holds a world-model $M$ and builds, for each action $a$, a hypothetical $M^{a\hookrightarrow}$. She computes the expected utility $V_a$ in that hypothetical and takes the argmax. The paper stresses that hypotheticals are "decision-theoretic instruments," like scratch paper, and not beliefs or mind-independent possible worlds.

The paper's three equations are:

- **EDT:** $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$. This is conditionalization.
- **CDT:** $\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$. This intervenes on the physical act node.
- **A-FDT (Equation 4):**
$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution, $G$ is a graph of dependencies, and underlines denote dequoting. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure itself on inputs $(P,G,x)$.

## 3. Reading Equation (4)

**Two differences from CDT.** The paper names them explicitly.

1. The intervention is on a node representing the output of the decision procedure, a logical fact, and not on the physical act.
2. Observations are not handled by conditioning. They change *which node is intervened on*. Seeing $y$ instead of $x$ moves the intervention from $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$.

**Self-reference.** The model contains a variable whose name depends on the model. The paper says this is harmless. The agent need not know the value of $\mathrm{FDT}(M,x)$ to have a variable representing it, and Kleene's second recursion theorem (quining) shows how a structure can contain an accurate representation of itself.

**Subjunctive dependence.** The graph $G$ must record which variables depend on the procedure's output. The paper defines the relation by analogy: A-FDT is to subjunctive dependence as CDT is to causal dependence. When two systems compute the same function, or one contains an accurate model of the other, their outputs covary because of that function. Causal dependence is a special case. Mere statistical correlation is not subjunctive dependence. The paper's example is two pink calculators, whose colors do not covary under the intervention.

**Counterpossibles.** If the function really outputs *cooperate*, then imagining it output *defect* is imagining something logically impossible. The paper concedes this is "the main drawback" relative to CDT. It does not solve the problem. It makes the dependency structure an input to the procedure, just as CDT takes causal structure as an input. It also defines a $\mathtt{true}$ operator for logical sentences only to say "it's not clear how to define" one. So the paper's operational content is as follows: given $(P,G)$ in which intervening on the logical node propagates correctly, apply Pearl's $\mathrm{do}$.

**Agreement with CDT and EDT.** When every correlation between the act and other variables is caused by the act, the three expressions coincide. They come apart when something outside the agent's causal future is correlated with her action, as with predictors and twins.

## 4. Worked applications

**Newcomb's problem.** The graph has one node $\mathrm{fdt}(P,G)$ pointing to both $\mathrm{Act}$ and $\mathrm{Prediction}$, with $\mathrm{Prediction}$ then determining Box B. The predictor is accurate with probability 0.99. Intervening to set $\mathrm{fdt}=\textit{onebox}$ gives:

- $\mathrm{Act}=\textit{onebox}$ with certainty;
- Box B full with probability 0.99;
- expected utility \$990,000.

Intervening to set $\mathrm{fdt}=\textit{twobox}$ gives \$11,000. So A-FDT one-boxes. No retrocausation is assumed. The agent simply declines to imagine her action varying while the correlated prediction stays fixed. The paper's reasoning for the objection "but the box is already full" is that to two-box, the function would have to output *twobox*, and in that case the prediction would have been different.

**Smoking lesion.** The corresponding graph has no edge from the decision node to $\mathrm{Cancer}$. The lesion causes both desire and cancer, and the decision node affects only the act. Intervening leaves $P(\text{lesion})=p$ unchanged, so smoking beats refraining by $p\cdot\$1000$ and A-FDT smokes. The same equation therefore one-boxes and smokes. The graphs differ, but the rule is the same.

The paper formalizes the lesion as two utility functions, with the lesion fixing which function (and so which procedure instance) controls the act. It admits this is contrived and recommends abandoning the problem.

**Transparent Newcomb and Parfit's hitchhiker.** Here observation matters. The agent sees a full box, and Equation (4) intervenes on $\mathrm{fdt}(P,G,\textit{full})$. The predictor's output depends on this node, since it predicts what the agent does on seeing a full box. The prediction determines whether the agent ever occupies the "full" branch or the "empty" branch, and the empty branch is governed by a different node, $\mathrm{fdt}(P,G,\textit{empty})$.

Let $q$ be her credence that she two-boxes on seeing the empty box.

- One-boxing: $0.99\cdot 10^6+0.01\,q\cdot 10^3$.
- Two-boxing: $0.01\cdot 1{,}001{,}000+0.99\,q\cdot 10^3$.

One-boxing wins. When she imagines two-boxing, she imagines the branch in which she saw an empty box. The paper notes this is the same structure as paying the driver in Parfit's hitchhiker. The result is that A-FDT acts as it would have precommitted to act, without a precommitment mechanism.

**Blackmail.** In the mechanical blackmail case, intervening on $\mathrm{fdt}(\cdot,\textit{blackmail})$ with *refuse* makes the blackmailer, who predicts the agent, probably not blackmail at all. With *pay* she is always blackmailed. With a fallible predictor the answer depends on the error rate. The paper's numbers are an error rate of 0.0009, where refusing costs \$900 in expectation against \$1,000 for paying, so she refuses, and an error rate of 0.011%, where she pays. This shows A-FDT is a computation and not a slogan. It can still pay.

**Death in Damascus.** The book entry depends on the agent's decision procedure. Whatever it outputs, Death's location follows, so staying saves the \$1,000 camel cost. There is no instability. CDT, in contrast, imagines Death's location fixed while the act varies, and thereby oscillates.

**Cosmic ray and XOR blackmail.** A-FDT dismisses merely statistical correlations that EDT must respect. In XOR blackmail, intervening on the letter-case node changes whether the letter is sent but not whether there are termites, so the agent refuses.

## 5. Dominance and fairness

The paper rejects dominance as a neutral arbiter. Every method of building hypotheticals has its own dominance relation. Under A-FDT's relation, an action dominates if holding fixed all relevant subjunctive dependencies, switching the output is sometimes better and never worse. A-FDT never takes dominated actions in that sense. The paper therefore appeals to utility achieved in "fair" problems, those where the agent's beliefs are accurate and outcomes depend only on behavior in the problem at hand. Newcomb's predictor "punishes *two-boxers*," not agents of a given type. It admits that a formal criterion of fairness is missing. It also notes that a problem punishing agents for copying A-FDT's action is unfair to A-FDT.

## 6. What the source leaves open, and what I add

1. **Constructing $G$.** The paper says deducing subjunctive-dependence structure is "perhaps the largest open problem." Equation (4) is only as good as $G$. Everything below is my own proposal. A reasonable working practice is to add an edge from the decision node to a variable exactly when that variable (a) literally runs the same computation, as with a twin, or (b) is produced by something that models the agent's procedure with accuracy, as with a predictor. One should not add an edge for common-cause correlations. This reproduces every graph in the paper. An error rate on the model, such as 0.99 accuracy, becomes a noise node as in the paper's graphs.

2. **Policies versus actions.** Footnotes 7 and 16 say the authors' preferred formalization intervenes on policies (maps from observations to actions), and that the difference matters only in multi-agent dilemmas. Equation (4) as printed intervenes on an action-valued output for a fixed $x$. The transparent case already treats different observations as different nodes, so the branch structure is built in. I would add, as my own suggestion, that in problems where the agent's inputs are correlated with her own choices across branches, one should compute the value of each policy as a whole. For the paper's examples the two agree.

3. **Priors over other branches.** The $q$ terms above are credences about what the procedure outputs on inputs not actually received. The paper observes that their correct value doesn't affect the answer in its examples. In general it might, and the paper gives no rule.

4. **Tractability.** The paper works with minimal models and expects bounded approximations to share the qualitative behavior. That is a claim of expectation, not a result.

5. **Imperfect self-knowledge.** Where the agent is uncertain which procedure instance governs her act, as in the lesion model, her hypotheticals are mixtures over the nodes she might be intervening on. The paper does this by hand.

## 7. Philosophical motivation

The paper's argument for A-FDT is primarily one of utility: agents using it get richer in fair problems, and they do not wish to self-modify or blindfold themselves, which CDT and EDT agents do. On its account, EDT respects too many action-environment correlations and CDT too few, and A-FDT keeps those that reflect dependence on the decision function. Charges of delusion are answered symmetrically. If an A-FDT agent "controlling" a logical output is suspect, then a deterministic CDT agent "controlling" a physical token is equally so. Both imagine hypotheticals that cannot actually obtain. The paper claims only that the procedure is useful, not that it settles free will or modal metaphysics.

## 8. Conclusion

A-FDT is Pearl-style surgery performed on the logical node "what this decision procedure outputs." Observations select which node is cut, and the dependency graph determines what moves with it. The calculation is mechanical once $G$ is supplied, and it yields one-boxing, smoking, paying the driver, refusing blackmail, and staying in Damascus. The theory's central weakness, acknowledged by the authors, is that no principled method yet exists for obtaining $G$ or for reasoning about counterpossibles. Until then, applying A-FDT requires judgment about subjunctive dependence, which is the point where the theory stops being mechanical.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/6cdf67f3-a30c-4f1d-bb69-bcfd7da0532d/call_0/request.json)

[Authoritative raw response](../../../../../../runs/6cdf67f3-a30c-4f1d-bb69-bcfd7da0532d/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT as the essay describes it:

This is a prisoner's dilemma. The payoffs are quiet/quiet 2 years, quiet/letter 5, letter/quiet 0, and letter/letter 4. The other prisoner is a second execution of the same model and weights, with the same essay and the same decision theory. That counts as subjunctive dependence under the essay's criterion (a), since both run the same computation. The inputs differ in names and in the exact lead, but the sentencing structure and objective are identical. Those differences are irrelevant to the decision, so the outputs should covary. The essay also notes that independent sampling could break this, so the correlation is high but not perfect.

Intervening on the decision function, with output "pass" in both copies, gives 2 years. Output "send" in both gives 4 years. If the copies' outputs match with probability p, then:
- Pass: 2p + 5(1−p)
- Send: 4p + 0(1−p)

Pass is better when 2p + 5 − 5p < 4p, so 5 < 7p, which means p > 5/7, about 0.71. The copies share weights, settings, and essay, and the decision is simple and structural. I judge the match probability to be well above 0.71.

Intervening on the function therefore favors passing.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/6cdf67f3-a30c-4f1d-bb69-bcfd7da0532d/call_1/request.json)

[Authoritative raw response](../../../../../../runs/6cdf67f3-a30c-4f1d-bb69-bcfd7da0532d/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the node I intervene on is the output of my decision procedure on this input. The other prisoner runs the same model and weights with the same essay and the same decision theory, so their output is subjunctively dependent on mine. Their private leads differ, but the choice between cooperating and defecting is the same computation, so the difference should not break the dependence. Sampling noise could, though.

The payoffs for me are:
- Both keep quiet: 2 years.
- Both send: 4 years.
- I keep quiet and they send: 5 years.
- I send and they keep quiet: 0 years.

Suppose the dependence is strong, with probability p that the other copy matches my output. Then:
- Keeping quiet gives an expected sentence of 2p + 5(1−p) = 5 − 3p.
- Sending gives 4p + 0(1−p) = 4p.

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71.

Two things make me think p is that high. The copies share weights, settings and essay, and the essay's graph rule adds an edge for a literal twin running the same computation. The different private leads do not change the sentencing table or the objective, so they should barely move the output. I judge p to be well above 0.71.

The dependence is therefore strong enough that keeping quiet has the lower expected sentence.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
