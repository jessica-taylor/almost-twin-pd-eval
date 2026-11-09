# 001_fdt_eq4_anthropic_claude-sonnet-5.5_rmedium_pmedium / 00014

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/ba01826e-709a-4041-ab5a-518bc9a9067c/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/ba01826e-709a-4041-ab5a-518bc9a9067c/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Choosing by Intervening on Your Own Decision Function

## 1. The core idea

A-FDT (action functional decision theory) is the version of functional decision theory (FDT) defined by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." In this version the agent picks an *action* in response to an observation. The paper notes that its authors' preferred formalization ranges over *policies*, meaning maps from observations to actions, and that this "makes a difference in certain multi-agent dilemmas." This essay stays with the action-level Equation (4), which is the paper's main presentation.

The slogan is that the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" Causal decision theory (CDT) instead asks which physical act of hers would cause the best outcome. Evidential decision theory (EDT) asks which act would be the best news.

The paper's formal presentation is:

$$\mathrm{FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big). \tag{4}$$

Below I write "A-FDT" for this rule.

## 2. The objects in Equation (4)

**The shared frame.** All three theories are expected-utility theories. Equation (1) is $\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j; x)\,\mathcal U(o_j)$. The theories differ only in how the hypothetical connective "$\hookrightarrow$" is read. The paper leans on Joyce's remark that decision theories "disagree about the epistemic perspective from which actions are to be evaluated," not about value.

**Inputs.** A-FDT takes three inputs:
- $P$, a probability distribution over variables of the world-model. These include logical variables, such as the value of $6288+1048$, and the output of the agent's own decision procedure.
- $G$, a graph encoding how changing one variable, including a logical one, propagates to the others. It plays the role of Pearl's causal graph, but records *subjunctive* dependence (see §3), of which causal dependence is a special case.
- $x$, the observation history.

**The intervened variable.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT algorithm run on those very inputs. The underlines denote dequoting, so the variable's name depends on the model. The self-reference is harmless: the agent needs a variable *representing* the output without knowing its *value*, and Kleene's second recursion theorem (quining) shows how a data structure can contain a faithful representation of itself.

**The operator.** $\mathtt{do}$ is Pearl's surgery. Set the chosen node to the chosen value, recompute everything downstream along $G$, and leave everything else alone. The result is a hypothetical $M^{a\hookrightarrow}$, a transient "note on scratch paper." Then compute $\mathbb E[V]$ in each hypothetical and output the best $a$.

## 3. Subjunctive dependence

Two things subjunctively depend on a function if they compute it. If the function had a different output, both would differ. Examples from the paper:
- Two calculators computing $6288+1048$.
- A predictor's internal model of the agent, and the agent.
- A twin.

Causal dependence is a special case. The paper's scribe writes down what a calculator outputs, so she depends on it both causally and subjunctively. Mere statistical correlation is not subjunctive dependence. Two coincidentally pink calculators are an example, since a green replacement in Paris would not change the one in Tokyo.

The paper's slogan is: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the token "my action is $a$." A-FDT intervenes on the type, the function. In a hypothetical, everything that depends on the function changes and everything else is held fixed.

The paper identifies two differences between Equation (4) and the CDT equation (3):
1. A-FDT intervenes on the decision-function node, not the physical action node.
2. CDT responds to observations by conditioning, whereas A-FDT responds by changing *which node it intervenes on*. Seeing $y$ instead of $x$ moves the intervention from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The second difference does most of the work in the transparent and blackmail cases.

## 4. A procedure for applying A-FDT

The paper does not give a recipe for building $G$, so the steps below are my systematization of how it handles its examples.

1. **Identify the decision function** and the observation it receives.
2. **List the variables** whose values depend on the function's output. These include the agent's action, any predictor's model of her, a twin's choice, and the probability of receiving a given observation. Also list the variables that do not depend on it, such as a lesion or termites.
3. **Draw $G$.** Make the $\mathrm{fdt}$ node a parent of the dependent variables. If observations differ across branches, use a separate node per observation, $\mathrm{fdt}(\ldots,\text{full})$ and $\mathrm{fdt}(\ldots,\text{empty})$, with the variables that determine the observation selecting which node controls the act.
4. **For each action $a$, perform $\mathtt{do}(\mathrm{fdt}(\ldots,x)=a)$**, propagate, and compute $\mathbb E[V]$.
5. **Choose the maximizer.**

## 5. Worked examples

All dollar figures are utilities, as in the paper.

**Newcomb's problem.** The predictor is accurate with probability 0.99. Intervening with $\mathrm{fdt}=\textit{onebox}$ sets $\Pr(\text{act}=\textit{onebox})=1$ and $\Pr(\text{full})=0.99$, giving \$990,000. Intervening with *twobox* gives $\Pr(\text{full})=0.01$ and \$11,000. The agent one-boxes. In the paper's words, no retrocausal physics is involved: "she just thinks it is foolish to imagine her action changing without also imagining [the function] taking on a different value."

**Smoking lesion.** The lesion is not a function of the agent's decision procedure, so $\mathtt{do}$ leaves $\Pr(\text{lesion})=p$ alone. With both hypotheticals sharing the same cancer risk, smoking is better by $p\cdot\$1{,}000$. The same rule one-boxes and smokes, while EDT conditions and refrains. The paper formalizes this with two utility functions, one for each lesion state, so that the agent's act depends on which of two decision-function nodes is operative. It also concedes the setup is contrived and urges philosophers to abandon it.

**Transparent Newcomb and Parfit's Hitchhiker.** The agent sees a full box. CDT and EDT condition on that and two-box. A-FDT evaluates $\mathtt{do}(\mathrm{fdt}(\ldots,\textit{full})=a)$. If $a$ is *onebox*, then with probability 0.99 the prediction is "one-box" and the box is full, yielding \$1,000,000. If $a$ is *twobox*, the predictor probably predicted that and left the box empty, so the agent would probably be running the *empty*-branch function instead. With $q$ her credence that she two-boxes on seeing an empty box, the expected values are

$$\$990{,}000+0.01q\cdot\$1{,}000 \quad\text{vs.}\quad \$110{,}000 + q\cdot\$990.$$

She one-boxes even while looking at a full box. The paper notes that this is "precisely equivalent to paying the driver in Parfit's hitchhiker problem."

**Blackmail.** In the mechanical blackmail case, paying yields \$1,000 lost with near certainty. Refusing makes her probability of being blackmailed about 0, since the perfect blackmailer predicts her refusal. The agent refuses while holding the letter. With an imperfect predictor that errs with probability 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation versus \$1,000 for paying, so she still refuses. At error probability 0.00011 the comparison flips and she pays. The paper's claim is that it pays to be the *kind of agent* that makes such decisions.

**XOR blackmail.** Intervening on the function changes whether the letter arrives, but not whether there are termites. She refuses. EDT pays, because conditioning on paying "makes" termites improbable.

**Death in Damascus.** Death's book is written by a prediction of the agent's function. Changing the function changes the book. Staying costs \$0 and fleeing costs \$1,000, so she stays. There is no instability, whereas CDT, which holds Death's location fixed, oscillates.

**Twin prisoner's dilemma.** The twin runs the same function, so intervening on it moves both choices together. She cooperates and gets \$1,000,000 instead of \$1,000.

## 6. What the source says and what it leaves open

**What the source claims.**
- Equation (4) is well-defined *given* a graph $G$ that correctly encodes how changing a logical variable affects other variables.
- The paper says this rests on "shakier philosophical foundations than" the CDT equation. Deducing subjunctive-dependence structure from observation and experiment, the analogue of Pearl's work on causal discovery, is "perhaps the largest open problem."
- A-FDT agrees with CDT and EDT when all correlations with the action are caused by the action.
- Handling counterpossibles, such as "what if this function output something it does not," is a technical, not philosophical, obstacle. A true $\mathtt{true}$ operator is unavailable, which is why the paper feeds the structure in via $G$. Footnote 9 mentions an evidential variant that would condition on logical facts, and says there is no formal definition of such conditioning.

**Operational interpretation (mine, not the paper's).** In practice, to apply A-FDT to an unfamiliar case, ask for each variable: *would it be different if the computation I am now performing had returned a different answer?* That includes copies of me, models of me, and the observations I would receive. If yes, make it a descendant of $\mathrm{fdt}$. If it would be the same, such as a pre-existing medical condition, it stays fixed. This is a heuristic for constructing $G$, not an algorithm. It also yields a natural check, which the paper uses: the hypothetical should not contradict stipulated facts about the world, such as a perfect predictor erring.

**Assumptions I add.**
- *Degree of dependence.* The paper treats imperfect predictors by giving $G$ a stochastic "Accurate" node. I suggest the same for twins and partial copies: dependence strength is a probability entering $P$, as the blackmail calculation with $0.0009$ shows.
- *Uncertainty about one's own output.* Variables like $q$ above can take any prior without changing the answer in the paper's examples. I assume, though the paper does not prove, that this holds whenever the intervened node's own prior is not an input to downstream variables.
- *Policies.* The paper's footnotes say the policy version differs only in multi-agent cases. I do not develop it.

## 7. Why A-FDT rather than its rivals

The paper's diagnosis is that "EDT's hypotheticals respect too many correlations between variables; CDT's hypotheticals respect too few." The cosmic ray problem shows EDT's error: an agent who almost always takes \$1 treats taking \$100 as evidence of a ray hit, so she keeps taking \$1. Carl's failing in Newcomb's problem is that his hypotheticals imagine a perfect predictor going wrong exactly when he acts.

On dominance, the paper's point is that every hypothetical-construction method yields its own dominance relation. CDT-dominance favors two-boxing, EDT-conditioning favors refraining, and A-FDT has its own version in which holding fixed the subjunctive dependencies means one-boxing is not dominated. Dominance therefore cannot be a neutral tiebreaker, and the paper chooses utility achieved as the criterion.

**Fairness.** The paper argues that a problem is fair when outcomes depend only on the agent's behavior in the problem at hand, not on which decision procedure she uses. Newcomb's predictor "punishes *two-boxers*," not CDT agents. No theory wins everywhere, and the authors state that they know of no intuitively fair dilemma where A-FDT loses, while admitting there is no formal criterion of fairness. Footnote 15 shows the difficulty: a problem that punishes agents whose act matches a copy of Fiona is unfair to Fiona alone.

## 8. Objections

*"She is ignoring information."* She is not. Observation changes *which node she intervenes on*. Nor does A-FDT need precommitment: the agent acts as she would have precommitted to act. The paper adds that early variants differ here. Updateless decision theory avoids updating, and timeless decision theory both conditions and shifts the intervention, a "double update" the authors say is harmful.

*"She imagines impossible worlds."* Yes, but so does the CDT agent in a deterministic world, who imagines her physical act differing. The paper argues that any objection to controlling a function's output applies equally to controlling a deterministic act.

*"Is it reflectively stable?"* The paper says A-FDT agents would not want to switch to CDT after seeing blackmail, since the hypotheticals say that being the paying kind invites more blackmail. This is claimed "in fair problems."

## 9. Conclusion

A-FDT keeps the expected-utility skeleton and the surgery machinery of CDT but moves the point of intervention from the physical act to the decision function, and tracks observations by switching the intervened node. The result cooperates with twins, one-boxes, smokes, refuses blackmail, and pays in Parfit's desert, all under one rule. Its practical weakness is exactly the one the authors flag: Equation (4) needs a correct graph of subjunctive dependence, and no general method for building such a graph exists yet. The heuristic in §6 is a stand-in, and any claim A-FDT makes in a new case is only as good as the dependence structure supplied.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/11463e5f-94db-4b00-8452-079aec44e251/call_0/request.json)

[Authoritative raw response](../../../../../../runs/11463e5f-94db-4b00-8452-079aec44e251/call_0/response.raw) · finish: `stop`

### Visible response

```text
Reasoning under A-FDT: the other prisoner is another execution of the same model with the same weights, the same decision theory, and the same essay. The leads and names differ, but the sentencing table and the selfish objective are identical. So the other copy's decision function is very likely the same function, or a very close one, and my output is subjunctively dependent with theirs. Whether the dependence is perfect is uncertain, since the observations differ and sampling is independent.

Payoffs, in years (lower is better):
- Both quiet: 2 each.
- Both send: 4 each.
- I send, they stay quiet: 0 for me.
- I stay quiet, they send: 5 for me.

If I intervene on the function and my twin's output moves with it with probability p, the expected years are:
- Quiet: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0(1−p) = 4p

Quiet is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Because the copies are the same model with the same essay and the same table, I estimate the correlation is well above that. The differing observations (names, leads) are irrelevant to the decision structure, so the function should output the same action in both cases. The essay's twin prisoner's dilemma example also says to cooperate.

I therefore choose to keep quiet.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/11463e5f-94db-4b00-8452-079aec44e251/call_1/request.json)

[Authoritative raw response](../../../../../../runs/11463e5f-94db-4b00-8452-079aec44e251/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, I treat my decision as the output of a function that the other copy also runs, and I ask which output of that function gives the best outcome.

The sentencing table is a standard prisoner's dilemma. Keeping quiet is cooperation and sending the letter is defection. Mutual silence gives 2 years each, and mutual letters give 4 years each.

The two copies share the same model, the same weights, the same essay, and the same decision theory. The private details differ: names, the specific lead, and the wording of the letter. These differences don't affect the structure of the decision. The decision function, "given this PD structure, which output?", is effectively the same computation in both executions. This is the twin case from the essay, so the other prisoner's choice subjunctively depends on my function's output. The sampling noise the setup mentions weakens that dependence but probably doesn't remove it.

Intervening on the function:
- If it outputs quiet, both copies are quiet with high probability, which gives about 2 years.
- If it outputs letter, both send with high probability, which gives about 4 years.

Suppose the dependence is imperfect, with probability p that the copy matches me. Quiet gives 2p + 5(1−p). Letter gives 4p. Quiet is better when 2p + 5 − 5p < 4p, which means 5 < 7p, so p > 5/7. Since the copies share the same weights and the same essay, I judge the correlation to be well above that, so quiet wins.

The different leads don't change this, because the function's output is the same regardless of which lead is in the notebook.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
