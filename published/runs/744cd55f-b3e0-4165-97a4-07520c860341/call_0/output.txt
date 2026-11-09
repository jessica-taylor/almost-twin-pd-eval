# A-FDT: Choosing by Intervening on Your Decision Function

## 1. The core idea

Action functional decision theory (A-FDT) is the version of functional decision theory that Yudkowsky and Soares present as Equation (4) of Section 5:

$$\text{A-FDT}(P,G,x) := \arg\max_{a\in\mathcal A}\ \mathbb E\big(V \mid \mathtt{do}(\mathrm{fdt}(\underline P,\underline G,\underline x)=a)\big).$$

I use "A-FDT" for this equation, in which the argument ranges over actions. The paper's footnotes say its authors prefer a policy-based version, and I mention that only in passing.

Three ingredients define the rule:

- **Inputs.** $P$ is a probability distribution over the variables of the agent's world-model. $G$ is a graph saying how changing one variable changes the others. $x$ is the observation history.
- **The intervention node.** It is $\mathrm{fdt}(\underline P,\underline G,\underline x)$, a variable in the model standing for the output of the A-FDT procedure itself, run on this model and these observations. Underlines mean dequoting: the variable's name is built from the values of $P$, $G$, $x$.
- **The operator.** $\mathtt{do}$ is Pearl's surgery operator. It sets the chosen variable to $a$, recomputes everything downstream of it in $G$, and leaves the rest alone.

Section 5's other equations share the same skeleton. All three theories, EDT, CDT and A-FDT, maximize $\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;x)\,\mathcal U(o_j)$. They differ only in how they read the connective $\hookrightarrow$, which Joyce called the "epistemic perspective":

- EDT conditions: $\mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$.
- CDT intervenes on the physical act: $\mathbb E(V\mid \mathtt{do}(\mathrm{Act}=a),\mathrm{Obs}=x)$.
- A-FDT intervenes on the logical fact about what its own decision function outputs.

The paper's slogan is "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence." CDT intervenes on the token "my action is $a$". A-FDT intervenes on the type.

## 2. Two differences from CDT

The paper names exactly two differences between Equations (3) and (4).

1. **Where the surgery happens.** CDT cuts at $\mathrm{Act}$. A-FDT cuts at the node for the function's output. Anything that computes or models that function lies downstream of the cut. This includes the agent's own body, a twin, and a predictor's internal model of the agent. All of these move together when the hypothetical output changes.
2. **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It changes which node it intervenes on, $\mathrm{fdt}(\underline P,\underline G,\underline x)$ for the $x$ actually seen. Other observation values correspond to other nodes, such as $\mathrm{fdt}(\ldots,\textit{empty})$ versus $\mathrm{fdt}(\ldots,\textit{full})$. A hypothetical output can therefore change which observation the agent would have received. This is the sense in which A-FDT "entertain[s] the hypothesis that, if their action were different, they might have *made different observations*."

Because it never conditions on observations, A-FDT is "updateless", a property the paper's footnote ties to Wei Dai's Updateless Decision Theory.

Subjunctive dependence is the relation that licenses the surgery. Two physical systems depend subjunctively on a function when they compute it, however accurately. Causal dependence is a special case: a scribe copying a calculator's output would write something different if the output were different. Mere statistical correlation is not subjunctive dependence: two coincidentally pink calculators do not covary under intervention. In the limiting case of a perfect model, the model's output and the agent's output are logically locked together, like two working calculators computing $6288+1048$. Imperfect models weaken the lock without removing it.

## 3. Counterpossibles, and what the paper leaves open

If the function outputs *onebox* on this input, it does so of logical necessity. Intervening to make it output *twobox* is therefore a counterpossible, in the way that "if Fermat's last theorem were false" is. The paper considers a "true" operator on logical sentences that would handle this directly, and says: "Unfortunately, it's not clear how to define a $\True$ operator. Fortunately, we don't have to." The workaround is to require that $G$ be given as input. It must encode how changing the logical variable changes everything else, just as CDT takes its causal graph as input.

This is the main open problem the source states, and it is worth being explicit about what it means:

- **Stated by the source.** Equation (4) works given an accurate $G$. How to learn or deduce the subjunctive-dependence structure from observation and experiment is "perhaps the largest open problem."
- **What A-FDT therefore is.** It is a decision procedure relative to a dependency model, not a way of discovering dependencies. Its quality is bounded by the quality of $G$.
- **The source's gestures toward heuristics.** The paper notes that the agent needs only narrow counterpossible judgments, such as "how would this predictor's prediction change if the algorithm had a different output?". It also observes that humans do this tolerably well.

Self-reference is handled by quining (Kleene's recursion theorem). The agent need not know the value of the output to have a variable representing it.

## 4. A practical recipe (my gloss on the source)

To apply A-FDT to an unfamiliar case:

1. **List the variables** and mark which are, or are modeled on, copies of the decision function. These include twins, predictors, simulators and the agent's own later selves. Mark which merely correlate with it, such as common-cause biological traits.
2. **Draw the intervention node(s).** Make one node per possible observation, $\mathrm{fdt}(\cdot,\cdot,x_i)$. Draw arrows from each node to everything that computes it. Add a selector variable that determines which node actually controls the act. This is how the paper draws the transparent Newcomb and blackmail graphs.
3. **For each action $a$, perform $\mathtt{do}(\mathrm{fdt}(\ldots,x)=a)$.** Propagate downstream, including to observations that vary with $a$, and compute $\mathbb E[V]$. Variables that are not downstream keep their prior probabilities.
4. **Output the argmax.**

For hypothetical outputs at nodes other than the actual one, the agent's beliefs about what it would do there enter as priors. The paper shows that these generally do not affect the answer, e.g. $q$ in its examples.

## 5. Worked examples

**Newcomb's problem.** A-FDT intervenes on $\mathrm{fdt}(P,G)$, which feeds both $\mathrm{Act}$ and $\mathrm{Prediction}$. The predictor is accurate with probability 0.99.

- *Onebox*: $0.99\cdot 1{,}000{,}000=\$990{,}000$.
- *Twobox*: $0.01\cdot 1{,}001{,}000+0.99\cdot 1{,}000=\$11{,}000$.

So A-FDT one-boxes. No retrocausation is asserted, and the agent does not claim a signal travels backwards. She simply declines to imagine her output changing without the output of the predictor's model changing. The dominance argument for two-boxing, in the paper's words, "is merely a restatement of CDT's method for assessing an agent's options". It is like asking us to imagine a calculator outputting 3159 while holding fixed that $6288+1048=7336$. A-FDT has its own dominance notion, in which relevant subjunctive dependencies are held fixed, and under that notion it never takes a dominated action.

**Smoking lesion.** The same equation gives a different answer because $G$ is different. The lesion is not a computation of the agent's decision function, so $\mathrm{Cancer}$ is not downstream of the intervention node. The paper formalizes the problem with two utility functions, one for each lesion state. The agent cannot introspect which function she runs, so there are two nodes $\mathrm{fdt}(P_S,G)$ and $\mathrm{fdt}(P_R,G)$. Intervening on the node she actually occupies leaves the probability $p$ of the lesion unchanged. Smoking then beats refraining by exactly $p\cdot\$1{,}000$ in her computation, so she smokes. A-FDT thus one-boxes and smokes with one rule, where CDT and EDT cannot. The paper also admits the problem is contrived: it asks the agent to choose under ignorance of her own preferences, and the EDT agent's model is inaccurate if the agent lives among EDT agents. It recommends abandoning the problem.

**Transparent Newcomb and Parfit's hitchhiker.** Suppose the agent sees a full box. Her graph has one node for "see full" and one for "see empty", with the prediction selecting which node controls the act. For $a=$ *onebox* at the "full" node:

- With probability 0.99, the prediction is accurate, the box is full, and she gets $1{,}000{,}000$.
- Otherwise she is in the empty-box world, and her expected payoff there is $q\cdot 1000$.

So $EU(\textit{onebox})=990{,}000+0.01q\cdot1000$. For *twobox*, $EU = 0.01\cdot 1{,}001{,}000+0.99q\cdot 1000$, which is much smaller. A-FDT leaves the box. When she imagines two-boxing she imagines a world in which she probably saw an empty box. Parfit's hitchhiker has the same structure, so A-FDT pays the driver. The paper argues this is "precisely equivalent," so intuitions that treat the two cases differently look like framing effects. Its supporting arguments are:

- Precommitment would be endorsed by CDT and EDT agents alike.
- A-FDT has no negative value of information.
- Above all, the argument from utility: the agents this rule produces end up richer.

**Blackmail.** In the mechanical blackmail case, a perfect predictor runs the damaging program only if she predicts payment.

- Hypothesizing *pay*: she is blackmailed with probability about 1 and loses $1{,}000$.
- Hypothesizing *refuse*: she is never blackmailed.

So she refuses, even holding the letter. With an imperfect blackmailer erring with probability $0.0009$, refusing costs $0.0009\cdot 1{,}000{,}000=\$900$ in expectation versus $\$1{,}000$ for paying, so she still refuses. If the error rate is $0.011\%$, the expected loss from refusing is $\$110$ and she pays. In XOR blackmail she refuses, because the infestation node is not downstream of the function while the letter's arrival is. Compare EDT, which pays because paying is "good news" about termites, and CDT, whose hypothetical has the predictor erring exactly when she acts.

**Death in Damascus.** A-FDT sees Death's book as depending on the decision function. Wherever she goes, Death is there, so she stays and saves the $1{,}000$. CDT oscillates, because its hypotheticals keep Death's location fixed while its own action varies.

## 6. Why the paper claims this is right

- **Utility achieved.** The justifying criterion is expected utility measured from outside. The paper reports that A-FDT does well in each of the cases above, while CDT and EDT each fail somewhere.
- **EDT respects too many correlations** and CDT "too few." A-FDT is meant to preserve exactly the subjunctive dependencies.
- **Reflective stability.** A-FDT acts as it would have precommitted to act, so it has no reason to self-modify in fair problems.
- **Fairness.** Newcomb's predictor "punishes *two-boxers*", not decision procedures. Penalizing an agent for the algorithm she runs, as opposed to the action she outputs, is unfair to any theory. The paper has no formal criterion of fairness, and it flags a hard case: a problem that punishes agents whose action matches a copy of A-FDT's action.
- **Control.** The charge that A-FDT agents believe they "control" mathematics is answered by parity. A deterministic CDT agent equally lacks control over her physical act, and both theories rely on imagined variation.

## 7. Where extra assumptions are required

The following are not fixed by the paper. They are my proposals.

1. **Building $G$.** A usable heuristic: add an arrow from the intervention node to a variable only if that variable's value is produced by running, or modeling by simulation or proof, this very algorithm on this input. Merely correlated traits get no arrow. The paper's treatment of lesion versus predictor exemplifies this.
2. **Imperfect prediction.** Model the predictor as a noisy copy: with probability $\epsilon$ the dependence is broken. The paper's examples with a 0.99 accuracy variable do exactly this.
3. **Multiple copies.** When several agents run the same function (voting, coordination, one's own future selves), the single node feeds all of them. The paper uses this for the voting and gym examples. Whether copies in different circumstances count as "the same function" depends on whether relevant differences exist, which needs case-by-case judgment.
4. **Policy versus action.** The paper's footnotes say the authors prefer intervening on a policy, a map from observations to actions. In the single-agent examples I worked through, the observation-indexed nodes behave like a policy, but I have not shown that the two always coincide. The source says they diverge only in multi-agent dilemmas.

## 8. Conclusion

A-FDT is an expected-utility rule whose only departure from CDT is where it cuts the model. It cuts at the output of its own decision function and lets observation select which cut applies. Given a faithful dependency graph, it one-boxes, smokes, pays the hitchhiker, refuses blackmail and stays in Damascus. The theory's hard part is the graph. Until subjunctive dependencies can be inferred as principledly as Pearl's causal structure, A-FDT is a precise procedure resting on an input that is still supplied by judgment.