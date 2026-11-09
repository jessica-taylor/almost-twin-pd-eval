# A-FDT: Choosing by Intervening on One's Own Decision Function

## 1. The idea

A-FDT (action functional decision theory) is the theory defined by Equation (4) of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality." The paper calls the theory FDT. I use "A-FDT" throughout for the version of the theory that selects an *action* given in Equation (4), and I use that name for it consistently. The paper's footnotes 7 and 16 say the authors' preferred formalization selects *policies* (maps from observations to actions) instead. I call that variant policy-selecting FDT, and I do not develop it here. The paper says the difference matters only in some multi-agent dilemmas.

The central principle is quoted from the paper: treat one's decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" CDT asks which physical act causes the best outcome. EDT asks which act would be the best news. A-FDT asks what the world would look like if this very decision function returned a different output.

## 2. The formal definition

All three theories maximize expected utility,

$$\mathcal{EU}(a)=\sum_j P(a \hookrightarrow o_j;\,x)\,\mathcal U(o_j)$$

(Equation (1)). They differ only in how they read the connective "$\hookrightarrow$". Joyce's representation theorem treats that reading as a free parameter, "the epistemic perspective from which actions are to be evaluated."

With $V:=\mathcal U(\mathrm{Outcome})$, the paper gives:

- EDT: $\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a)$
- CDT: $\arg\max_a \mathbb E(V\mid do(\mathrm{Act}=a),\mathrm{Obs}=x)$
- **A-FDT (Equation (4))**:

$$\mathrm{FDT}(P,G,x):=\arg\max_{a\in\mathcal A}\ \mathbb E\Big(V \;\Big|\; do\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

The inputs are:

- $P$, a probability distribution over the agent's world-model variables, including variables for the outputs of mathematical functions. One example is a variable for $6288+1048$, with most of its mass on $7336$.
- $G$, a graph encoding how changing a logical variable propagates to other variables. This is the "subjunctive dependence" structure.
- $x$, the observation history.

The underlined arguments are dequoted names. The node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ represents what the A-FDT procedure outputs on these very inputs. This is self-reference by quining (Kleene's recursion theorem). The agent does not need to know the value of the node in order to have a variable for it.

The paper notes two differences from CDT.

1. The intervention is on the decision-function node, not the physical-act node.
2. Observation does not condition the distribution. It changes *which* node is intervened on: from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$.

The intervention uses Pearl's $do$ operator. Downstream variables according to $G$ are recomputed, and everything else is held fixed. Here "downstream" includes anything that subjunctively depends on the function's output, such as a predictor's model of the agent, a twin, or the agent's own later acts. An ideal operator $\mathtt{true}(\mathrm{fdt}(\cdot)=a)$ on logical sentences would be better, but the paper says "it's not clear how to define" it. Equation (4) avoids the problem by requiring the dependency structure as an *input*, just as CDT requires causal structure.

## 3. Subjunctive dependence

Two systems subjunctively depend on a function when both compute it. Examples are two calculators computing $6288+1048$, or a predictor's accurate model of an agent. Causal dependence is a special case. Mere statistical correlation is not subjunctive dependence: two pink calculators do not depend on each other's color. In sketch form:

- *Predictor-like* things depend on the function's output. The lesion and the cosmic ray do not.
- The paper says the dependence weakens but is not eliminated when prediction is imperfect. In the Newcomb network the strength is carried by the $\mathrm{Accurate}$ variable (0.99).

Evaluating $do(\mathrm{fdt}=a)$ for an $a$ the function does not in fact output is a counterpossible. The paper admits that lacking a theory of counterpossibles is "the main drawback of FDT relative to CDT at this time." It argues the difficulty is technical, not philosophical. Humans reason under logical uncertainty, and the agent needs only specific questions such as how a predictor's output would change.

## 4. Applying A-FDT: a recipe

This is a summary of the procedure the paper's examples follow.

1. Build $P$ and $G$. Include a node $F_x=\mathrm{fdt}(\underline P,\underline G,\underline x)$ for each observation $x$ that could arise.
2. Draw arrows from $F_x$ to every variable that implements or models the agent's decision when it receives $x$: the act, predictions, twins' acts.
3. For each action $a$, set $F_{x_{\text{actual}}}=a$ by $do$. Propagate, with other nodes keeping their priors.
4. Compute $\mathbb E[V]$ and take the argmax.

Step 2 is the part the paper leaves open. Wherever I fill in $G$ below, I am supplying it by reading the problem statement.

## 5. Worked examples (all from the paper)

**Newcomb's problem.** The nodes are $F$, $\mathrm{Act}$, $\mathrm{Prediction}$ and $\mathrm{Accurate}$, with $P(\text{accurate})=0.99$. Intervening with $F=\textit{onebox}$ gives $\mathrm{Act}=\textit{onebox}$ and box B full with probability 0.99. The expected utility is \$990,000. Intervening with $F=\textit{twobox}$ gives \$11,000. A-FDT one-boxes. No retrocausation is assumed. It would be foolish to imagine the act changing while the predictor's model of the function stays fixed.

**Smoking lesion.** Here $G$ is different. The $\mathrm{Lesion}$ node causes both the act and the cancer, but the decision function causes only the act. The agent does not know whether she runs $\mathrm{fdt}(P_S,G)$ (lesion, enjoys smoking) or $\mathrm{fdt}(P_R,G)$. Intervening on $\mathrm{fdt}(P_S,G)$ leaves $P(\text{lesion})=p$ unchanged. Smoking then beats refraining by $p\cdot\$1{,}000$, so she smokes. The same equation one-boxes and smokes, because only the graph differs. The paper also calls this problem contrived and "badly confused."

**Transparent Newcomb and Parfit's hitchhiker.** With a full box observed, A-FDT intervenes on $F_{\text{full}}$. The box's contents depend on the prediction of $F_{\text{full}}$, and the act is set by $F_{\text{full}}$ only if the box is full. Otherwise it is set by $F_{\text{empty}}$. One-boxing gives $\$990{,}000+0.01q\cdot\$1{,}000$. Two-boxing gives $\$11{,}000+q\cdot\$990$ (the paper's printed "\$110,00" looks like a typo for \$11,000). So she one-boxes even while looking at a full box. In imagining two-boxing she imagines seeing an empty box. The paper says this is equivalent to paying the driver in Parfit's problem.

**Blackmail.** With $F_{\text{letter}}$ set to *pay*, the blackmailer sends the letter with probability about 1 and she loses \$1,000. With $F_{\text{letter}}$ set to *refuse*, she is blackmailed with probability about 0. If a predictor errs with probability $\epsilon$, refusing costs $\epsilon\cdot\$1{,}000{,}000$ in expectation, and paying costs \$1,000 (taking the paper's setup where the loss if blackmailed and refusing is \$1,000,000). This is how the paper gets its 0.0009 versus 0.00011 thresholds. In XOR blackmail the intervention does not change the termite node, so she refuses. EDT conditions on the good-news letter and pays.

**Death in Damascus.** Death's location depends on the prediction, which depends on the function. Every hypothetical is therefore self-consistent: wherever she goes, Death goes. She stays and saves \$1,000, with none of CDT's instability.

## 6. Why the construction is what it is

- Compared with EDT, A-FDT respects too few correlations in the right way. It breaks merely statistical ones (cosmic ray, lesion, XOR letter) and so does not "manage the news."
- Compared with CDT, it keeps logical correlations. CDT's hypotheticals have perfect predictors err "exactly when Carl makes his current decision."
- The paper's dominance discussion: every method of constructing hypotheticals induces its own dominance principle. A-FDT never takes an action dominated in its own sense. Dominance therefore cannot adjudicate between theories, and utility achieved does.
- Fairness: the paper says a problem is fair when the outcome depends only on the agent's behavior in the problem at hand, so Newcomb's predictor "punishes *two-boxers*," not rational agents. No formal definition of fairness is given.

## 7. What is open, and what I add

The paper itself marks two gaps.

**(a) Where $G$ comes from.** This is "perhaps the largest open problem." The $do$ operator is only as good as the graph. An A-FDT user must therefore judge from a problem's description which processes compute, or accurately model, the decision function. A practical heuristic that matches every example in the paper (this is my proposal, not a claim of the source): add an arrow from $F_x$ to a variable $Z$ iff $Z$'s value would change if the agent's algorithm, on input $x$, were replaced by another algorithm with a different output and Z's source ran the same inference unchanged. A lesion fails that test, and a predictor passes it.

**(b) Consistency of the self-referential node.** The paper says the self-reference is harmless but gives no algorithm for ensuring priors over $F_x$ are well behaved. In the examples the priors on non-intervened nodes (the $q$ values) turn out not to matter. I would add that this is a property of those examples, not a theorem.

**Observations versus policies.** The paper's treatment of observation (switching which $F_x$ is intervened on) means each observation gets its own node. When one observation's occurrence depends on another observation's output (full box versus empty box), the nodes interact, and it can matter whether the agent is choosing an action or a whole observation-to-action map. Footnote 7 says the policy version is the authors' preferred one. My practical advice is that if a problem has multiple agents running the same function on different inputs, check whether the policy version changes the answer.

**Tractability.** The paper evaluates only the simplest accurate models and expects bounded agents to approximate A-FDT with analogous strengths and weaknesses.

## 8. Further consequences (stated by the paper)

A-FDT gives non-negative value to information. It needs no ratification or costly precommitment, because it "always acts as it would have precommitted to act." It is reflectively stable in fair problems. It supports coordination: the voting-booth case (ten agents, \$1,000 cost, \$1,000,000 prize) leads A-FDT agents to vote, since their decisions are not subjunctively independent. Intertemporal self-coordination also follows, as with gym attendance.

## 9. Conclusion

A-FDT is CDT with a different intervention point. Instead of surgery on a physical-act node with Bayesian conditioning on observations, it does surgery on the node $\mathrm{fdt}(\underline P,\underline G,\underline x)$ and lets observation select the node. Given a dependency graph, Equation (4) is an algorithm. The paper's main claim is that this gets the right balance between EDT's respect for too many correlations and CDT's respect for too few. The unsolved problem, which any user must face, is where the dependency graph comes from.