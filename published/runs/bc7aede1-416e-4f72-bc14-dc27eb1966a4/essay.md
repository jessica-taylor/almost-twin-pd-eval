# A-FDT: Choosing the Output of Your Own Decision Function

## 1. The idea in one sentence

Functional decision theory, introduced by Yudkowsky and Soares (2017), starts from a change in what the agent takes herself to be choosing. Causal decision theory (CDT) asks which physical act causes the best outcome. Evidential decision theory (EDT) asks which act would be the best news. The functional decision theorist instead treats her decision as the output of a fixed mathematical function, and asks, in the paper's words, "Which output of this very function would yield the best outcome?"

This essay explains the version of the theory given by **Equation (4)** of the paper. I call it **A-FDT** (action functional decision theory) because the quantity it intervenes on is an *action*: the output of the agent's decision function on her actual input. The paper says in two footnotes that the authors' preferred formalization instead has agents "iterate over *policies* (mappings from observations to actions) rather than actions." I call that variant **policy-selecting FDT (P-FDT)** and keep it separate. The paper says the two coincide in all its examples. Section 7 gives a case where, on my analysis, they come apart.

Throughout, I mark which claims come from the source and which are my own interpretations or proposals.

## 2. Background: decision theories as recipes for hypotheticals

The paper treats CDT, EDT and A-FDT as expected utility theories that share Equation (1):

$$
\mathcal{EU}(a) = \sum_j P(a \hookrightarrow o_j;\, x)\,\mathcal U(o_j).
$$

Here $x$ is the observation history and $a \hookrightarrow o_j$ is a "decision hypothetical." Following Joyce (1999), the paper holds that the theories agree about how to value prospects and disagree only about "the epistemic perspective from which actions are to be evaluated," that is, about how to interpret $\hookrightarrow$.

In practice the agent holds a world-model $M$. For each option she builds a hypothetical $M^{a\hookrightarrow}$, scores it, and acts on the best one. The paper describes these hypotheticals as "decision-theoretic instruments constructed from beliefs," not as beliefs.

- **EDT** builds them by conditioning: $\arg\max_a \mathbb E(V \mid \textsc{Obs}=x, \textsc{Act}=a)$. This is Equation (2).
- **CDT** builds them by Pearl's causal intervention on the act node: $\arg\max_a \mathbb E(V \mid \mathtt{do}(\textsc{Act}=a), \textsc{Obs}=x)$. This is Equation (3).

## 3. The definition

**Equation (4) (the source's definition, which I call A-FDT):**

$$
\mathrm{A\text{-}FDT}(P, G, x) \;:=\; \arg\max_{a\in\mathcal A}\; \mathbb E\!\left(V \;\middle|\; \mathtt{do}\big(\textsc{fdt}(\underline P, \underline G, \underline x) = a\big)\right).
$$

The ingredients are as follows.

- **$P$** is a probability distribution over variables. Some of these are ordinary physical variables. Others stand for the outputs of mathematical functions, for example a variable for the value of $6288+1048$.
- **$G$** is a graph. It says how changing a variable, including a logical variable, propagates to other variables. For CDT, $G$ encodes causal structure. For A-FDT it must encode "the logical, mathematical, computational, causal, etc. structure of the world more broadly."
- **$\textsc{fdt}(\underline P,\underline G,\underline x)$** is a node in the model. It represents the output of the A-FDT algorithm when run on this very model and this very observation history. The underlines mark dequoting: the node's name is built from the model's own contents. The paper argues that this self-reference is harmless. The agent needs a variable that *represents* her output, not knowledge of its value, and Kleene's recursion theorem ("quining") shows that such self-representing data structures exist.
- **$\mathtt{do}$** is Pearl's operator, reused unchanged. It sets the node to $a$, recomputes everything downstream of it in $G$, and leaves everything else at its prior distribution.

The paper names two structural differences from CDT.

1. **Point of intervention.** CDT intervenes on the physical token $\textsc{Act}$. A-FDT intervenes on the *type*, the function's output, and that output may be implemented or modelled in several places at once: the agent's body, a twin, a predictor's simulation.
2. **Treatment of observation.** CDT responds to new evidence by conditioning on $\textsc{Obs}=x$. A-FDT does not condition. It responds to observation "by changing which node it intervenes upon": from $\textsc{fdt}(\underline P,\underline G,\underline x)$ to $\textsc{fdt}(\underline P,\underline G,\underline y)$.

The second difference is the one that produces A-FDT's most surprising verdicts. Because nothing is conditioned on, a hypothetical in which the output differs can also be one in which the agent *would have seen something else*.

The paper also mentions an idealized version, $\arg\max_a \mathbb E(V \mid \mathtt{true}(\textsc{fdt}(\ldots)=a))$, which uses a "$\mathtt{true}$" operator for counterpossible updating. It concedes that "it's not clear how to define a $\mathtt{true}$ operator." Equation (4) avoids the problem by requiring that the relevant logical dependency structure be supplied as input in $G$, in the same way CDT takes causal structure as input.

## 4. Subjunctive dependence: what goes into $G$

The whole content of A-FDT is in which arrows leave the $\textsc{fdt}$ node. The paper's guiding slogan is:

> "Functional decision theory is to subjunctive dependence as causal decision theory is to causal dependence."

When two physical systems compute the same function, their behaviours "subjunctively depend" on that function. The paper's illustration is two calculators computing $6288+1048$. Three cases help fix the boundaries:

- **Causal dependence is a special case of subjunctive dependence.** A scribe copying a calculator's output would have written something different had the output been different.
- **Statistical correlation is not enough.** Two calculators that happen to both be pink stand in no subjunctive dependence.
- **Prediction counts.** A predictor that builds an accurate model of the agent contains "a 'twin' inside the predictor's mind." A carcinogenic lesion does no such modelling.

So, operationally, $G$ should contain an edge from $\textsc{fdt}(\underline P,\underline G,\underline y)$ to every variable whose value is fixed, through accurate computation, simulation or reasoning, by what that function outputs on input $y$. This covers the agent's own act, twins, and predictors' forecasts. It should contain no such edge to variables that merely correlate with the agent's behaviour through common physical causes.

The paper is explicit that it offers no method for building this graph:

> "Figuring out how to deduce the structure of subjunctive dependencies from observation and experiment is perhaps the largest open problem in the study of functional decision theory."

## 5. Worked examples

All dollar amounts stand for utility. Predictors are 99% accurate unless stated otherwise.

### Twin prisoner's dilemma and Newcomb's problem

In the twin dilemma, both prisoners' actions are children of a single node $\textsc{fdt}$. Intervening on it with $\textit{cooperate}$ yields $(C,C)$ and \$1,000,000. Intervening with $\textit{defect}$ yields $(D,D)$ and \$1,000. A-FDT cooperates.

In Newcomb's problem (Fig. 3b of the source), $\textsc{fdt}$ has arrows to both $\textsc{Act}$ and $\textsc{Prediction}$, and an exogenous node $\textsc{Accurate}$ also feeds $\textsc{Prediction}$:

$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{onebox})] = 0.99\cdot 10^6 = 990{,}000,
$$
$$
\mathbb E[V\mid \mathtt{do}(\textsc{fdt}=\textit{twobox})] = 0.01\cdot 1{,}001{,}000 + 0.99\cdot 1{,}000 = 11{,}000.
$$

A-FDT one-boxes. The paper stresses that no retrocausation is involved. The agent "just thinks it is foolish to imagine her action changing without also imagining $\mathrm{FDT}(P^F,G^F)$ taking on a different value."

The paper's text also gives EDT's one-boxing value as \$999,000. The same arithmetic, $P(\textit{full}\mid\textit{onebox})=0.99$, gives \$990,000, so I read the paper's figure as a typo.

### Smoking lesion

Here the lesion determines the agent's *utility function*: $\mathcal U_S$ likes smoking, $\mathcal U_R$ does not. The model therefore contains two decision-function nodes, $\textsc{fdt}(\underline{P_S},\ldots)$ and $\textsc{fdt}(\underline{P_R},\ldots)$, and the lesion selects which of them controls $\textsc{Act}$. Neither node has an arrow to $\textsc{Cancer}$.

Intervening on the node the agent is actually running leaves $P(\textit{lesion})=p$ unchanged. The paper computes that smoking beats refraining by $p\cdot\$1{,}000$, so A-FDT smokes. The "$p$" factor reflects the agent's uncertainty about whether her own node is the one in control.

The general lesson is that **what you do not draw an arrow to cannot move.** A-FDT one-boxes and smokes for the same reason: it tracks dependence, not correlation.

### Transparent Newcomb (and Parfit's hitchhiker)

The agent sees box B full. Under A-FDT she does not condition on this. She intervenes on $\textsc{fdt}(\ldots,\textit{full})$, where $\textsc{Prediction}$ both reads that node and decides which observation node controls $\textsc{Act}$. Let $q$ be her prior that $\textsc{fdt}(\ldots,\textit{empty})=\textit{twobox}$.

**Setting the node to $\textit{onebox}$:**
- With probability 0.99 the prediction is accurate: the box is full and she takes \$1,000,000.
- With probability 0.01 it is inaccurate: the box is empty and the other node controls her act, giving $q\cdot 1{,}000$.

Total: $990{,}000 + 10q$.

**Setting the node to $\textit{twobox}$:**
- With probability 0.99 the box is empty, giving $q\cdot 1{,}000$.
- With probability 0.01 it is full and she two-boxes, giving \$1,001,000.

Total: $10{,}010 + 990q$.

One-boxing wins for every $q\in[0,1]$. The paper prints the two-boxing figure as "\$110,00 + q·\$990," which is evidently a misprint of \$10,010.

The paper argues that paying the driver in Parfit's hitchhiker problem is "precisely equivalent" to this case: the driver plays the role of the predictor, and the agent pays on arriving in the city.

### XOR blackmail

The letter is sent iff exactly one of the following holds: (no termites and the agent pays) or (termites and the agent refuses). Let $p$ be the prior probability of termites; the paper assumes an infallible predictor here.

- **Setting $\textsc{fdt}(\ldots,\textit{letter})=\textit{pay}$.** The letter arrives iff there are no termites. Expected value: $-p\cdot 10^6 - (1-p)\cdot 10^3$.
- **Setting it to $\textit{refuse}$.** The letter arrives iff there are termites. Expected value: $-p\cdot 10^6$.

A-FDT refuses, and so does CDT. They refuse for different reasons, and their hypotheticals differ. Asked what would have happened had she paid, the A-FDT agent answers "I would not have received the letter." The CDT agent answers that the inerrant predictor would have erred. EDT pays, because conditioning on paying drives the probability of termites to zero.

### Mechanical blackmail and a threshold

The blackmailer runs the program, and sends a letter, only if she predicts the agent would pay. With a perfect blackmailer, A-FDT refuses even while holding the letter: in the refuse-hypothetical she is simply never blackmailed.

The paper adds an error rate $\varepsilon$, the probability that the blackmailer wrongly predicts payment:

- Paying-type: always blackmailed, loses \$1,000.
- Refusing-type: blackmailed with probability $\varepsilon$, loses \$1,000,000 in that case.

So A-FDT refuses iff $\varepsilon\cdot 10^6 < 10^3$, that is, iff $\varepsilon < 0.1\%$.

The paper's illustrations are $\varepsilon=0.0009$, under which she refuses (expected loss \$900), and "0.011%," under which it says she pays. The second value lies below the threshold, so it is presumably a typo for something like 0.11%. In either case the structural point stands: A-FDT can choose an action with low utility *in the world matching its actual observations*, because that action is optimal for the function across the worlds its output influences.

### Death in Damascus

Death's appointment book is a node downstream of $\textsc{fdt}$. Fleeing leads to death in Aleppo minus \$1,000; staying leads to death in Damascus. A-FDT stays, and stays stably.

CDT, by contrast, oscillates, or needs ratification procedures. The paper adds that it may even refuse to pay \$1 for a truly random coin that would give it a real 50% chance of survival.

## 6. When A-FDT agrees with its rivals

The paper observes that if every correlation between $\textsc{Act}$ and other variables is either caused by $\textsc{Act}$ or runs through the $\textsc{fdt}$ node only via $\textsc{Act}$, then

$$
\mathbb E[V\mid a] = \mathbb E[V\mid \mathtt{do}(a)] = \mathbb E[V\mid \mathtt{do}(\textsc{fdt}=a)],
$$

and all three theories coincide. Divergence therefore requires something *other than the agent's own body* that tracks her decision function, such as a predictor, a twin, or a copy. This gives a quick test for any new problem: if nothing in the world models you, A-FDT is just CDT.

## 7. What the source leaves open, and how I propose to operationalize it

### (a) Conditioning versus not conditioning

Equation (4) contains no "$\textsc{Obs}=x$" term. The transparent-Newcomb section, however, writes $\mathbb E(V\mid \mathtt{do}(\textsc{fdt}(\ldots,\textit{full})=a, \textsc{Obs}=\textit{full}))$. The paper's own arithmetic in that section integrates over the worlds in which the box is empty, which conditioning would exclude.

**My reading:** Equation (4) is authoritative. The observation enters only through the *name* of the intervened node. This reading is also supported by the paper's footnote criticizing Timeless Decision Theory for a "double update," which arises when an agent both conditions *and* moves the intervention point.

### (b) Priors on the other $\textsc{fdt}$ nodes

A-FDT intervenes on one node, $\textsc{fdt}(\ldots,x)$. Nodes for other inputs, such as $\textsc{fdt}(\ldots,\textit{empty})$, stay at their priors (the $q$ above). In the paper's examples $q$ "doesn't matter," but it is a genuine input. So is the prior on the intervened node itself, though $\mathtt{do}$ overrides it.

**My proposal:** require *calibration*, meaning that the priors on non-intervened $\textsc{fdt}$ nodes should equal what A-FDT actually outputs on those inputs. This is a fixed-point condition, $q = \mathbb 1[\mathrm{A\text{-}FDT}(P,G,\textit{empty})=\textit{twobox}]$. The paper appeals to it informally: "The correct value of $q$ is 1, as you may verify."

### (c) A-FDT versus P-FDT

Once calibration is required, A-FDT can have several self-consistent solutions. P-FDT avoids this by choosing the whole map from observations to actions jointly. The following example is my own construction, not the source's.

> **Consistency game.** A fair coin shows the agent L or R. A predictor pays \$10 iff it predicts the agent would choose $a$ on *both* L and R. Separately, physically choosing $b$ pays \$1.

Suppose the agent sees L, and let $q$ be her calibrated credence that $\textsc{fdt}(\ldots,R)=a$.

- $\mathtt{do}(\textsc{fdt}(\ldots,L)=a)$ yields $10q$.
- $\mathtt{do}(\textsc{fdt}(\ldots,L)=b)$ yields $1$.

With $q=1$, choosing $a$ is a calibrated fixed point worth \$10. With $q=0$, choosing $b$ is also a calibrated fixed point, worth \$1. P-FDT compares the policies $(a,a)$, $(b,b)$, $(a,b)$ and $(b,a)$ directly and selects $(a,a)$.

So A-FDT matches P-FDT whenever the problem decouples across observations, which covers every dilemma in the paper. Where the predictor rewards whole policies, it reduces to an equilibrium-selection problem.

There is a possible defence. One could argue that $\textsc{fdt}(\ldots,L)$ and $\textsc{fdt}(\ldots,R)$ are outputs of the *same* function and should subjunctively depend on each other in $G$, which would close the gap. The source does not take this route: its graphs treat them as independent nodes. This is a concrete instance of the paper's broader admission that the structure of $G$ is not yet determined by any principled method.

### (d) Counterpossibles

The node's actual value is logically fixed, so $\mathtt{do}(\textsc{fdt}=a)$ for the wrong $a$ is a counterpossible supposition. The paper calls the lack of an account of counterpossibles "the main drawback of FDT relative to CDT at this time." It argues that the difficulty is "technical rather than philosophical," and that CDT faces an analogous puzzle about "control" in deterministic worlds.

Equation (4) sidesteps the issue only by assuming that $G$ is given. Anyone applying A-FDT should recognize that drawing the arrows is exactly where the hard judgment lies.

### (e) Fairness

The paper claims that A-FDT is not beaten in "fair" problems, which it characterizes informally as problems where outcomes depend on the agent's behaviour rather than on the procedure that produces it. It concedes that the notion is not yet formalized. An example is a problem that punishes anyone who acts like a copy of the FDT agent. The superiority claim is therefore only conjectural.

## 8. A recipe for unfamiliar cases

The following procedure is my operational summary. Steps 1–3 and 5–7 follow the source's practice; steps 4 and 6's calibration requirement and the policy check reflect my proposals in §7.

1. **List the observation histories** $y$ the agent could face in the problem.
2. **Find every system that computes or accurately models** your decision function on some input $y$: your body, twins, predictors, a past or future self running the same deliberation.
3. **Draw $G$.** Add a node $\textsc{fdt}(\ldots,y)$ for each $y$. Draw arrows from it to whatever its output fixes. Add selector arrows showing which node controls $\textsc{Act}$ in which world (for example, the prediction determines what you see). Draw *no* arrows to merely correlated variables.
4. **Set priors** on exogenous variables (accuracy, lesions, termites) and calibrated priors on the non-intervened $\textsc{fdt}$ nodes.
5. **Intervene** on $\textsc{fdt}(\ldots,x)$ for your actual $x$, with no conditioning on $x$, and propagate.
6. **Take the argmax.** If the calibration in step 4 admits several fixed points, report them, and note that P-FDT would compare full policies.
7. **Sanity-check** with §6: if nothing but your body depends on the node, the answer should match CDT's.

As a quick application, consider ten FDT agents who each pay \$1,000 to vote and receive \$1,000,000 iff all ten vote. One node feeds all ten acts, and intervening with "vote" yields $10^6 - 10^3$, so each agent votes. The paper's gym example works the same way: today's choice and next week's choice are outputs of the same function, so going today is evaluated together with going in the future.

## 9. Conclusion

A-FDT is CDT with the intervention moved from the physical act to the logical output of the agent's own decision function, and with observations used to select which output-node to intervene on rather than conditioned upon. Given a graph of subjunctive dependencies, Equation (4) is a complete and mechanical rule. It one-boxes, smokes, cooperates with twins, pays in Parfit's desert, refuses blackmail below a computable error threshold, and stays calmly in Damascus.

Its weaknesses are in what it takes as input. There is no theory of how to build $G$ or how to evaluate counterpossibles. Priors over the agent's own other outputs need a calibration convention. And in problems that reward whole policies, the action-level rule can settle on a worse self-consistent answer than the policy-level variant the authors themselves prefer.

## References

- Gibbard, A. & Harper, W. (1978). Counterfactuals and Two Kinds of Expected Utility.
- Joyce, J. (1999). *The Foundations of Causal Decision Theory*. Cambridge UP.
- Pearl, J. (2000). *Causality*. Cambridge UP.
- Yudkowsky, E. & Soares, N. (2017). Functional Decision Theory: A New Theory of Instrumental Rationality. arXiv:1710.05060.