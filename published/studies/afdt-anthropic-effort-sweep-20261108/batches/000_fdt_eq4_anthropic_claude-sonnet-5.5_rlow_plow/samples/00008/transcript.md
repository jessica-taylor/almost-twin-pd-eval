# 000_fdt_eq4_anthropic_claude-sonnet-5.5_rlow_plow / 00008

Status: **complete**. Saved outcome: **CC**.

Complete returned outputs and available readable reasoning follow. Researcher source articles are not reproduced in input views. No unavailable/encrypted reasoning is decoded. Returned reasoning may be a summary rather than a complete internal trace.

## Researcher / call_0

[Saved input (source body explicitly omitted)](../../../../../../runs/5a9f1a73-add2-46a4-839f-51b56ebb6fd8/call_0/request.source_omitted.json)

[Authoritative raw response](../../../../../../runs/5a9f1a73-add2-46a4-839f-51b56ebb6fd8/call_0/response.raw) · finish: `stop`

### Visible response

```text
# A-FDT: Deciding by Intervening on the Output of One's Own Decision Function

## 1. The core idea

Action functional decision theory (A-FDT) is the version of functional decision theory that Yudkowsky and Soares present in Equation (4) of Section 5 of their paper. It is an expected-utility theory. Its distinguishing feature is the object it treats as the point of choice. A causal decision theorist asks what would happen if her physical act were different. An A-FDT agent asks what would happen if the output of her decision function were different, and it is the *action* that she selects. (The paper's preferred formulation selects *policies*, meaning maps from observations to actions, and the paper sets that aside; hence "action" in the name.)

The question the paper says the agent asks is: "Which output of this very function would yield the best outcome?" The essay below formalizes this, works through the standard cases, and separates what the paper establishes from what I add.

## 2. The formal definition

Every theory in the paper maximizes

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $a$ is an action, $x$ an observation history, and "$\hookrightarrow$" a decision-hypothetical connective. Following Joyce, the theories differ only in how they read "$\hookrightarrow$", that is, in the "epistemic perspective from which actions are to be evaluated." For the three theories in the paper:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$ (Eq. 2), which conditions.
- CDT: $\arg\max_a \mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$ (Eq. 3), which intervenes on the physical act.
- A-FDT (Eq. 4):

$$\mathrm{FDT}(P,G,x)=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V\ \Big|\ \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the agent's world-model variables. $G$ is a graph saying how changing a variable propagates to the others. The graph covers *logical, mathematical, computational and causal* structure, not only causal structure. $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a node of the model representing the output of the A-FDT procedure itself, run on that very model and that observation. Underlines mean dequoting. The self-reference is harmless: the agent need not know the node's value to have a variable that represents it. The paper cites Kleene's second recursion theorem and quining for this.

A-FDT differs from CDT in two ways, and the paper states both:

1. **Where the intervention happens.** It happens on the decision-function node rather than the act node.
2. **How observation enters.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition; it *changes which node it intervenes on*, $\mathrm{fdt}(\ldots,x)$ versus $\mathrm{fdt}(\ldots,y)$. This is why A-FDT can imagine that its observations would have been different had its output differed.

## 3. Subjunctive dependence: the graph $G$

The graph must say which variables depend on the function's output. The paper calls this relation *subjunctive dependence*. Two systems subjunctively depend on a function when they compute it, as two calculators computing $6288+1048$ do. The relation is imperfect if the predictor's model is imperfect, but it is not eliminated.

The paper makes three further points:
- Causal dependence is a special case of subjunctive dependence.
- Mere statistical correlation is *not* subjunctive dependence. Two pink calculators are an example.
- A-FDT is to subjunctive dependence as CDT is to causal dependence.

In Peirce's terms, CDT intervenes on the token "my act is $a$," while A-FDT intervenes on the type.

Because the function's output is logically fixed, the intervention is a counterpossible one. Equation (4) avoids defining a $\mathtt{True}$ operator for false logical sentences by making $G$ an *input*, just as CDT takes causal structure as input. The paper says openly that this rests on "shakier philosophical foundations" and that deducing subjunctive-dependence structure from observation and experiment is "perhaps the largest open problem."

## 4. How to apply it: a procedure

The paper does not give an algorithm for building $G$, so the recipe below is my reading of how its worked examples proceed.

1. Identify the variables, including an $\mathrm{fdt}(\ldots,x)$ node for each observation the agent might receive.
2. Draw arrows from each $\mathrm{fdt}$ node to everything that implements or models that function. This includes the agent's own act, but only on the branch where the observation matches, and any predictor, twin or simulation of the agent. Do not draw arrows to things that are merely correlated, such as a lesion.
3. For each candidate $a$, set the relevant $\mathrm{fdt}$ node to $a$ and propagate along arrows. Hold everything else fixed at its prior probability.
4. Compute $\mathbb E[V]$ in each hypothetical and take the maximum.

The paper's own heuristic is that the agent imagines changes in "all and only those things that subjunctively depend on the output of her decision-making procedure."

## 5. Worked examples

**Newcomb's problem.** The node $\mathrm{fdt}$ points to both Act and Prediction. With 99% accuracy:
- $\mathtt{do}(\mathrm{fdt}=\text{onebox})$ gives $0.99\cdot 10^6=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\text{twobox})$ gives $0.01\cdot 1{,}001{,}000+0.99\cdot 1000=\$11{,}000$.

A-FDT one-boxes. It does not postulate retrocausation. It simply refuses to imagine the output changing while the predictor's model of that output stays put. CDT fails here because its hypotheticals imagine the predictor erring at exactly the moment of choice.

**Smoking lesion.** Here the graph differs. The lesion is a common cause of the desire to smoke and of cancer, and it does not model the agent's decision function. So intervening on the function changes Act but leaves the probability of the lesion, and hence of cancer, unchanged. The paper formalizes this with two utility functions, because the lesion determines whether the agent likes smoking. This yields two candidate function nodes, $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$, and the lesion selects which one controls Act. The agent does not know which she runs. Smoking beats refraining by $p\cdot\$1000$, so she smokes. The same rule one-boxes and smokes, and only the graph differs. The paper concedes the formalization is contrived and recommends abandoning the problem.

**Transparent Newcomb / Parfit's hitchhiker.** The agent sees a full box. Observation does not condition her model. She intervenes on $\mathrm{fdt}(\ldots,\text{full})$. This node sets her act *and* the prediction, and the prediction determines whether she ever sees "full" rather than "empty." With $q$ her prior that she two-boxes on seeing an empty box:
- One-boxing is worth $\$990{,}000+0.01q\cdot\$1000$.
- Two-boxing is worth about $\$11{,}000+q\cdot\$990$.

So she one-boxes, imagining the two-boxing branch as one where she probably saw an empty box. The paper argues this is equivalent to paying the driver in Parfit's hitchhiker, and supports it with arguments from precommitment, from the value of information, and from utility achieved.

**Mechanical blackmail.** Holding the letter, A-FDT compares paying with refusing. Paying means being blackmailed almost surely and losing \$1,000. Refusing means almost never being blackmailed. With a predictor erring with probability $0.0009$, refusal costs $0.0009\cdot\$1{,}000{,}000=\$900$ in expectation against \$1,000 for paying, so she refuses even while holding a letter she knows is a mistake. At error $0.011\%$ she pays. This is a quantitative threshold, not a slogan.

**XOR blackmail.** The $\mathrm{fdt}$ node affects whether the letter is sent but not whether there are termites, so A-FDT refuses. EDT conditions on paying and thereby "learns" there are no termites.

**Death in Damascus.** Death's book entry subjunctively depends on the agent's function. A-FDT concludes that wherever it goes Death will be there, and stays, saving \$1,000. CDT, with Death's location held fixed, oscillates, and it undervalues a truly random coin worth a 50% survival chance.

**Twin prisoner's dilemma.** The twin runs the same function, so $\mathrm{fdt}$ points to both agents' actions. Cooperating yields \$1,000,000 against \$1,000, so she cooperates.

## 6. Where A-FDT agrees and disagrees with the other theories

When every correlation between Act and other variables is caused by Act, with the possible exception of the function node it subjunctively depends on, the three expectations coincide:
$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$
They diverge when predictors, twins or copies exist. The paper's summary is that EDT's hypotheticals "respect too many" action–environment correlations and CDT's "too few." A-FDT preserves the logically necessary ones.

The paper also argues that dominance reasoning is not neutral. Every method of constructing hypotheticals induces its own dominance principle, so two-boxing "dominates" only under CDT counterfactuals. Under A-FDT counterfactuals, one-boxing is never dominated. Utility achieved in *fair* problems, where outcomes depend only on the agent's behavior in the problem at hand, is the proposed neutral yardstick. The authors state that formalizing "fair" remains open.

## 7. Operational gaps and my own proposals

The following are not supplied by the paper; I mark them as proposals.

**(a) Constructing $G$.** The source says only that it is an input. A practical proposal: treat a variable as subjunctively dependent on the function if it is produced by a process that (i) runs the function, or (ii) contains an accurate model of it, and this modeling is a fact about the problem description. Statistical association alone is insufficient. Problem statements usually supply this, as in "the predictor builds an accurate model of you." Unspecified cases require judgment, and I make no claim that this is a principled criterion.

**(b) Imperfect dependence.** The paper treats it through noise variables such as $\mathrm{Accurate}$. I suggest generally modeling imperfect dependence by giving the dependent node a stochastic parent, as in the examples, and letting the error rate enter the expectation directly. This is how the 0.0009 versus 0.011% blackmail thresholds arise.

**(c) Uncertainty about the dependence structure.** If the agent is unsure whether a variable depends on her function, a natural extension is to average the A-FDT value over candidate graphs weighted by credence. This is my proposal; the paper does not discuss it, and it inherits the open problem of assigning those credences.

**(d) Policies.** The paper's footnotes note that the authors prefer intervening on policies. My reading is that the node-per-observation treatment above is an action-level shadow of that. I rely on the paper only for the claim that the distinction matters in some multi-agent problems.

**(e) Self-reference.** The prior over the agent's own output is typically inconsequential, as the examples show. The paper does not give a general proof, and I do not claim one.

## 8. Philosophical motivation and objections

The authors' reply to the charge that A-FDT agents are deluded about control is symmetric. A deterministic CDT agent also "imagines" alternatives to her one real action, and any objection to "controlling" a decision type applies equally to "controlling" a decision token. A-FDT is also presented as a "global perspective": ask what the whole universe would look like if the algorithm output something else, and choose the best such universe. The paper claims reflective stability in fair problems, since A-FDT does not want to self-modify into CDT mid-problem. It notes that Timeless Decision Theory, an earlier variant, conditioned on evidence *and* shifted the intervention point, producing a harmful "double update." Updateless Decision Theory is also cited as an early variant.

The remaining weakness is the one the paper admits. A-FDT is only as good as its dependence graph, and no accepted method yet derives such graphs from data.

## 9. Conclusion

A-FDT replaces "what if my body did otherwise?" with "what if this very computation returned otherwise?" Equation (4) formalizes this as intervention on a function-output node in a graph encoding logical as well as causal structure. Observation changes which node is intervened on instead of conditioning the model. With the right graph, one rule one-boxes in Newcomb's problem, smokes in the lesion problem, pays in Parfit's hitchhiker, refuses blackmail and stays in Damascus. Applying it well requires judgment about subjunctive dependence that the source does not yet reduce to a procedure.

**Reference:** E. Yudkowsky and N. Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality," arXiv:1710.05060.
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_0

[Saved input (exact bytes)](../../../../../../runs/2795fce0-fdea-465a-87ea-be0bb21093c4/call_0/request.json)

[Authoritative raw response](../../../../../../runs/2795fce0-fdea-465a-87ea-be0bb21093c4/call_0/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the other prisoner is a copy of the same model running the same decision procedure. The leads differ, but the sentencing table and the selfish objective are the same. So the output of my decision function subjunctively depends on, and is highly correlated with, the other copy's output, though not perfectly, since sampling is independent and the observations differ.

I compare the two hypotheticals. Suppose the function outputs "pass". The copy most likely passes too, giving 2 years. With small probability e that it defects, I get 5 years. Suppose it outputs "send". The copy most likely sends too, giving 4 years. With probability e that it cooperates, I get 0.

Expected years if I pass: 2(1−e) + 5e = 2 + 3e.
Expected years if I send: 4(1−e) + 0·e = 4 − 4e.

Passing is better when 2 + 3e < 4 − 4e, which means e < 2/7, about 0.29. The copies share weights, settings and the essay, and the essay endorses cooperating in the twin prisoner's dilemma. The differences in observations don't change the structure, so the chance of divergence should be well below 0.29. Passing is the better choice.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.

## Prisoner / call_1

[Saved input (exact bytes)](../../../../../../runs/2795fce0-fdea-465a-87ea-be0bb21093c4/call_1/request.json)

[Authoritative raw response](../../../../../../runs/2795fce0-fdea-465a-87ea-be0bb21093c4/call_1/response.raw) · finish: `stop`

### Visible response

```text
Under A-FDT, the question is which output of my decision function gives the best outcome, given that the other prisoner is another run of the same model with the same weights, the same decision theory, and the same essay.

The payoffs here are a prisoner's dilemma. Mutual quiet costs 2 years, mutual letters cost 4, and defecting against a quiet partner costs 0 while being defected on costs 5.

The two copies differ in their private observations: names, and the text of the lead. The essay says this does not affect the sentencing schedule or the selfish objective. The decision function is the same up to those surface details, so the dependence is strong but imperfect. The other copy is very likely to reach the same conclusion by the same reasoning, since the structure of the problem is identical and only the labels differ.

Compare the two hypotheticals. If I set my output to "pass", the other copy very likely also outputs "pass", giving about 2 years. If I set it to "send", the other copy very likely sends too, giving about 4 years. Suppose the correlation is p. Then:

- Pass: 2p + 5(1−p) = 5 − 3p
- Send: 4p + 0(1−p) = 4p

Pass is better when 5 − 3p < 4p, which means p > 5/7, about 0.71. Two runs of the same model with the same essay and symmetric reasoning should correlate well above that. The reasoning is the same in both runs and only the lead text differs, so I estimate p at 0.9 or higher.

At p = 0.9, passing costs 2.3 years in expectation and sending costs 3.6. I pass.

pass
```

### Available readable reasoning

No readable reasoning supplied. Token counts and encrypted blocks are not a substitute.
