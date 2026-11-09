# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The core idea

Standard expected-utility theories agree that an agent should pick the action maximizing

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $a\hookrightarrow o_j$ is a "decision hypothetical". They differ over how to read the connective $\hookrightarrow$. Evidential theory reads it as conditioning. Causal theory reads it as a causal intervention on the physical act. A-FDT, the theory I discuss here under the name used in this assignment (Yudkowsky and Soares call it functional decision theory), reads it as an intervention on the output of the agent's own decision function.

The source gives the formal presentation as Equation (4), Section 5:

$$\mathrm{A\text{-}FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; \mathtt{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution over the variables of the agent's world-model. $G$ is a graph encoding how changing a variable propagates to the others, including logical and computational dependencies as well as causal ones. $x$ is the observation history. $V=\mathcal U(\text{Outcome})$. The underlines denote dequoting, so $\mathrm{fdt}(\underline P,\underline G,\underline x)$ is a variable in the model that names the output of the very algorithm being run, on exactly these inputs.

## 2. Reading the equation

The formula has four moving parts.

1. **The intervened variable is a logical fact.** The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for "what this algorithm outputs on this input". Under the source's CDT counterpart, Equation (3), one intervenes on the physical act $\mathrm{Act}$ instead. The source states the analogy this way: "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

2. **Surgery, not conditioning.** $\mathtt{do}$ is Pearl's operator. Set the node to $a$, recompute every node downstream of it according to $G$, and leave everything else untouched. Downstream of the node are the agent's own act, which is the usual case, but also anything that subjunctively depends on the function, such as a predictor's model of the agent or a twin running the same code. Variables that merely correlate with the act, such as a common-cause lesion, are not downstream and are left alone.

3. **Observations change which node is intervened on.** A CDT agent handles observation by conditioning, $\mathrm{Obs}=x$. An A-FDT agent does not condition on it. It intervenes on $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the observation $x$ it actually has. The source says that when observations change, A-FDT "changes from intervening on the variable $\mathrm{fdt}(P,G,x)$ to $\mathrm{fdt}(P,G,y)$ instead." This is why A-FDT behaves in an "updateless" way. In its hypotheticals, a different output may correspond to a world in which it saw something different.

4. **Self-reference is harmless.** The model names a variable depending on the model itself. The source appeals to Kleene's second recursion theorem ("quining"). The agent need not know the value of its output to have a variable representing it.

The source also notes (footnotes 7 and 16) that its preferred formalization intervenes on a *policy*, a map from observations to actions, and that this matters only in some multi-agent problems. I follow the source in using actions with a fixed observation. It follows from the policy remark, though, that the transparent-box and blackmail calculations below are best read as comparing policy-level hypotheticals.

## 3. Subjunctive dependence

The graph $G$ must encode **subjunctive dependence**. Two systems subjunctively depend on a function when they compute it, so that if the function's output were different, both their behaviors would differ. The source gives three clarifications:

- Causal dependence is a special case. A scribe copying a calculator's display depends on it both causally and subjunctively.
- Mere statistical correlation is not subjunctive dependence. Two pink calculators are correlated in color, but changing one would not change the other.
- Imperfect predictors give weakened but non-zero dependence, as with two calculators one of which might suffer a cosmic-ray error.

Evaluating the hypotheticals requires reasoning about counterpossibles, since the function's output is in fact fixed. The source concedes this is "the main drawback" of the theory. It argues the difficulty is technical and not philosophical, because humans reason under logical uncertainty ("the twin prime conjecture is false") without trouble.

## 4. What the source leaves open

The paper is explicit that Equation (4) "rests on shakier philosophical foundations" than the CDT equation. The graph $G$ is an *input*, just as causal structure is an input to CDT. The source gives no method for learning subjunctive structure from observation, and calls this "perhaps the largest open problem". It also supplies no formal $\mathtt{true}(\cdot)$ operator, which is why it uses $\mathtt{do}$ on a graph instead. Nor does it give a formal fairness criterion.

My own proposal, labelled as such, is an operational rule for building $G$ in practice. For each variable $Z$ in the problem, ask: *is $Z$ produced by something that computes, or accurately models, the same function as my decision procedure, on the relevant input?* If so, make $Z$ a descendant of the fdt node. Otherwise, treat it as downstream of the fdt node only through the ordinary causal route, via the agent's own act. Predictors, twins, and copies get the first treatment. Lesions, weather, and coincidental correlates get the second. The rule is useful but incomplete. It leaves open partial models, adversaries who respond to the agent's *theory* and not merely its output, and cases where it is unclear whether a simulation is accurate enough to count.

## 5. Worked applications

**Newcomb's problem.** The model has $\mathrm{fdt}\to \mathrm{Act}$ and $\mathrm{fdt}\to\mathrm{Prediction}\to\text{Box B}$, with a noise variable giving 99% accuracy.

- $\mathtt{do}(\mathrm{fdt}=\text{onebox})$ gives Act = onebox and Box B full with probability 0.99, so $\mathbb E[V]=\$990{,}000$.
- $\mathtt{do}(\mathrm{fdt}=\text{twobox})$ gives Box B full with probability 0.01, so $\mathbb E[V]=\$11{,}000$.

A-FDT one-boxes. No retrocausation is assumed, only that the predictor's model and the agent are two instances of one function. Carl, the CDT agent, cuts the link to the prediction and gains $1,000 in each branch, so he two-boxes.

**Smoking lesion.** Here the lesion is not computing the agent's function. The dependence graph has the fdt node feeding Act, while Lesion and Cancer sit outside it. Intervening on the fdt node does not move $P(\text{lesion})$, so smoking wins by $p\cdot\$1{,}000$. The source's formalization requires care: the lesion changes the agent's *utility function*, so there are two possible functions (one run by lesion-havers, one by non-havers). The agent does not know which she is running, and Act depends on the Lesion variable to select between them. The same rule gives one-boxing in Newcomb and smoking here, with no ratification.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees a full Box B. A-FDT intervenes on $\mathrm{fdt}(\cdot,\text{full})$. Setting it to *twobox* changes the prediction, so in that hypothetical the box was probably empty and a different node, $\mathrm{fdt}(\cdot,\text{empty})$, would be controlling the act. With $q$ the agent's credence that she two-boxes on seeing an empty box:

- onebox: $\approx \$990{,}000+0.01q\cdot\$1{,}000$
- twobox: $\approx \$11{,}000+q\cdot\$990$

So A-FDT leaves the $1,000. The source notes this is structurally the same as paying the driver in Parfit's hitchhiker. The 99% accurate lie detector plays the predictor's role.

**Blackmail.** In the mechanical blackmail case, the agent holds the letter. Hypothetically refusing means the blackmailer would have predicted refusal and never sent it; paying means always being blackmailed. With a blackmailer whose false-positive rate is 0.0009, refusing costs $0.0009\times\$1{,}000{,}000=\$900$ in expectation against a certain $1,000 for paying, so refusal wins even though this agent knows the letter exists. If the error rate rises to 0.011%, the source says she pays, because then the numbers favour paying. In XOR blackmail, A-FDT refuses for a different reason than CDT: changing the fdt output changes whether the letter appears but not whether the house has termites.

**Death in Damascus.** The book entry subjunctively depends on the agent's function. Fleeing yields Death in Aleppo, and staying yields Death in Damascus. So A-FDT stays and saves $1,000. It has no instability loop, because it never imagines changing its choice while Death's location stays fixed. CDT's trouble is that it does imagine that, and this leads to a ratified mixed strategy that even undervalues a $1 truly random coin (which the source says would give a 50% chance of survival).

**Common-cause cases with interventions.** In the cosmic-ray problem (take $1 or $100, where a rare ray flips the choice and costs $1,000 to check up), A-FDT, like CDT, intervenes without inheriting the spurious correlation, and takes the $100. EDT takes the $1.

## 6. Relation to the other two theories

The source's picture is that EDT's hypotheticals respect too many correlations and CDT's respect too few. Where every correlation between act and world is causal from the act (aside from possible dependence on the fdt node), all three agree:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathtt{do}(a)]=\mathbb E[V\mid \mathtt{do}(\mathrm{fdt}=a)].$$

They split only where something other than the act's causal descendants tracks the act, that is, predictors and replicas.

The source also stresses an analogy with CDT. Both theories are expected-utility theories in Joyce's framework, differing only in the "epistemic perspective", meaning the constraints on the hypothetical probabilities. A-FDT is thus not a rival account of value.

## 7. Justification and criticism

The source's main argument is **utility achieved**: a predictor can see that CDT and EDT agents two-box in the transparent box, so they mostly see empty boxes. Supporting arguments are that A-FDT behaves as if it had precommitted (so it needs no costly binding), that it does not assign negative value to information, and that it endorses its own continued use. The source also denies that dominance is a neutral arbiter, since every method of building hypotheticals induces its own dominance notion.

Fairness is its answer to the charge that Newcomb problems merely reward a predisposition. A problem is called "fair" roughly when payoffs depend on the agent's *behavior* in the problem, not on which decision procedure produced it. Newcomb's predictor "punishes two-boxers", not CDT as such. The source admits that no formal criterion exists, and its footnote 15 shows the difficulty: a game that punishes copying Fiona's action is unfair to her.

Some caveats are my own assessment and not claims of the source:

- A-FDT's verdicts are only as good as $G$. Misspecified subjunctive structure can make the theory behave arbitrarily, for example by crediting a weak predictor with too much dependence.
- The "global perspective" in which she imagines never having been blackmailed involves hypotheticals that are acknowledged to be impossible. The source defends this by parity with the CDT agent's imagined act-changes in a deterministic world. A critic may still find the transparent-box verdict hard to accept as *rational* even if it is *lucrative*.
- The empirical test cases are hand-picked. The source says it knows of no fair dilemma where the theory loses, which is a claim about absence of counterexamples and not a proof.

## 8. A procedure for unfamiliar cases

Following Equation (4), with my operational additions noted:

1. Build the world-model $P$ and variables, including the observation $x$ and utility $V$.
2. Identify the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the observation you actually have.
3. *(My addition.)* Draw arrows from it to every variable produced by something that computes or accurately models this function, including your own act at each observation-node that would run it.
4. Do not draw arrows to mere correlates.
5. For each action $a$, compute $\mathbb E[V\mid\mathtt{do}(\mathrm{fdt}=a)]$, allowing observation-nodes other than the actual one to be reached in the hypothetical.
6. Output the argmax.

Group cases follow the same pattern. In the ten-person vote ($1,000 to enter, $1,000,000 if all ten vote), the others' choices depend on the same function, so voting beats not voting. The gym case treats one's later selves as running the same function and so skipping today is hypothetically skipping always.

## 9. Conclusion

A-FDT, as defined by Equation (4), keeps the form of causal decision theory (expected utility under interventions) but moves the point of intervention from the physical act to the output of the agent's own decision function, and responds to observations by changing which output-node it intervenes on, not by conditioning. This one change yields one-boxing in Newcomb, smoking in the lesion problem, paying in Parfit's hitchhiker, refusing blackmail, and staying put in Damascus, all from a single rule. The cost is that the rule needs a dependence graph, and the source offers no principled way to learn it. Specifying and justifying the graph, and formalizing fairness, are the open problems on which the theory's wider claims depend.