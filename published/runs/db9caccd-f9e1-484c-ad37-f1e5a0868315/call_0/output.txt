# A-FDT: Choosing by Intervening on Your Own Decision Function

## 1. The idea

A-FDT is the decision procedure defined by Equation (4), Section 5 of Yudkowsky and Soares, "Functional Decision Theory: A New Theory of Instrumental Rationality". It is an expected-utility theory that differs from causal decision theory (CDT) and evidential decision theory (EDT) in one place only: how it builds the hypothetical scenario used to evaluate an action.

The source's slogan is that the agent treats her decision "as the output of a fixed mathematical function that answers the question, 'Which output of this very function would yield the best outcome?'" A CDT agent asks which physical act of hers causes the best outcome. An EDT agent asks which act would be the best news. The A-FDT agent asks what the world would look like if the function she is computing returned a different value.

Terminology note: the paper calls the theory FDT. I use A-FDT for the procedure of Equation (4) and name other theories explicitly.

## 2. The formal definition

All three theories maximize

$$\mathcal{EU}(a)=\sum_j P(a\hookrightarrow o_j;\,x)\,\mathcal U(o_j),$$

where $a$ is an action, $x$ an observation history, and "$\hookrightarrow$" a decision-hypothetical connective. Following Joyce, the theories differ only in the epistemic perspective, meaning how "$\hookrightarrow$" is read. EDT reads it as conditioning:

$$\mathrm{EDT}(P,x)=\arg\max_a \mathbb E(V\mid \mathrm{Obs}=x,\mathrm{Act}=a).$$

CDT reads it as Pearl's intervention on a causal graph $G$:

$$\mathrm{CDT}(P,G,x)=\arg\max_a \mathbb E(V\mid \mathrm{do}(\mathrm{Act}=a),\mathrm{Obs}=x).$$

A-FDT, Equation (4), is

$$\mathrm{FDT}(P,G,x)\;:=\;\arg\max_{a\in\mathcal A}\;\mathbb E\Big(V\;\Big|\;\mathrm{do}\big(\mathrm{fdt}(\underline P,\underline G,\underline x)=a\big)\Big).$$

Here $P$ is a probability distribution containing variables for outputs of mathematical functions. $G$ is a graph describing how changing such a logical variable propagates to the other variables. The variable $\mathrm{fdt}(\underline P,\underline G,\underline x)$ stands for the output of the A-FDT procedure itself on those inputs. The underlines denote dequoting, so the variable's name depends on its inputs.

The source states two differences from CDT:

1. **Where the surgery happens.** CDT intervenes on a node for the physical action. A-FDT intervenes on a node for the output of its decision function. This is the type/token contrast: CDT intervenes on the token "my action is $a$", A-FDT on the type.
2. **How observation is handled.** CDT conditions on $\mathrm{Obs}=x$. A-FDT does not condition. It switches which node it intervenes on, moving from $\mathrm{fdt}(\underline P,\underline G,\underline x)$ to $\mathrm{fdt}(\underline P,\underline G,\underline y)$ when the observation changes from $x$ to $y$.

The self-reference is harmless. The agent need not know the value of $\mathrm{fdt}(P,G,x)$ to hold a variable representing it, and Kleene's recursion theorem (quining) shows such self-representing structures can be built.

## 3. Subjunctive dependence

What the graph $G$ must encode is subjunctive dependence. Two systems subjunctively depend on a function when they compute it. Examples are two calculators evaluating $6288+1048$, a twin, or a predictor holding an accurate model of the agent. Causal dependence is a special case: a scribe copying a calculator's display depends on it both causally and subjunctively. Mere statistical correlation does not count. Two calculators that happen to both be pink are not subjunctively linked, because a green purchase in Paris would not recolor Tokyo's.

The slogan is: A-FDT is to subjunctive dependence as CDT is to causal dependence. The A-FDT agent imagines her function's output changing, imagines everything subjunctively downstream changing with it, and holds everything else fixed. If $G$ has only causal arrows and the action has no subjunctive links beyond causal ones, the three theories coincide:

$$\mathbb E[V\mid a]=\mathbb E[V\mid \mathrm{do}(a)]=\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}=a)].$$

They come apart when events correlate with the action without being caused by it, for instance when predictors are present.

## 4. Worked applications

**Newcomb.** A-FDT's graph has the function node $\mathrm{fdt}(P,G)$ pointing to both $\mathrm{Act}$ and $\mathrm{Prediction}$. With predictor accuracy 0.99:

- $\mathrm{do}(\mathrm{fdt}=\text{onebox})$ gives $0.99\cdot\$1{,}000{,}000=\$990{,}000$.
- $\mathrm{do}(\mathrm{fdt}=\text{twobox})$ gives $0.01\cdot\$1{,}001{,}000+0.99\cdot\$1{,}000\approx\$11{,}000$.

So A-FDT one-boxes. No retrocausation is assumed. She simply does not imagine the action changing while a good predictor's output stays fixed.

**Smoking lesion.** The graph differs. The function node feeds $\mathrm{Act}$ but not $\mathrm{Cancer}$, which depends on the lesion. Intervening on the function leaves the lesion probability $p$ unchanged, so smoking gains $p\cdot\$1{,}000$ and she smokes. One rule yields one-boxing in the first case and smoking in the second. The only input that changes is $G$.

**Transparent Newcomb and Parfit's hitchhiker.** Observing a full box does not lead A-FDT to condition on it. She intervenes on $\mathrm{fdt}(P,G,\text{full})$. This node feeds both her action when she sees a full box and the predictor's prediction, which determines whether she sees a full box at all. Writing $q$ for her credence that she two-boxes on seeing an empty box, the source computes:

- one-boxing: $\$990{,}000+0.01\,q\cdot\$1{,}000$;
- two-boxing: $\approx\$11{,}000+q\cdot\$990$.

She one-boxes, even while looking at a full box. When she imagines two-boxing she imagines having seen an empty box. Paying the driver in the hitchhiker case is the same structure.

**Blackmail.** In the mechanical blackmail case, $\mathrm{do}(\mathrm{fdt}(\cdot,\text{blackmail})=\text{pay})$ makes blackmail near-certain and costs \$1,000. $\mathrm{do}(\cdot=\text{refuse})$ makes blackmail near-nonexistent. She refuses, even holding the letter. With a blackmailer error rate of 0.0009, refusing costs \$900 in expectation versus \$1,000 for paying, so she refuses. At 0.011% she pays, because the comparison reverses. Thresholds like this fall out of the expected-utility calculation. In XOR blackmail she refuses because the function node does not affect termite infestation.

**Death in Damascus.** A-FDT imagines Death's book changing along with her decision, so no instability arises. She stays and saves the \$1,000.

## 5. Why the construction is principled

CDT hypotheticals can describe a perfect predictor erring exactly when the agent decides. EDT hypotheticals keep merely statistical correlations, which leads to "news management". In the cosmic ray problem EDT takes \$1 for fear of the hospital bill. A-FDT breaks statistical correlations but preserves dependencies that track the same computation. The source's summary is that EDT respects too many action–environment correlations and CDT too few.

On dominance, the source argues that every way of building hypotheticals induces its own dominance notion. Two-boxing dominates only under CDT counterfactuals. Under A-FDT counterfactuals, A-FDT never takes a dominated action. Dominance is therefore not a neutral arbiter, and the source appeals to utility achieved instead.

On fairness, the source treats a problem as "fair" if it rewards or punishes only behavior in the problem, not the decision procedure. Newcomb's predictor "punishes *two-boxers*", not CDT as such. The source has no formal criterion of fairness and says so.

## 6. What the source leaves open, and my proposals

**The graph $G$ is an input.** The source states plainly that deducing subjunctive-dependence structure from observation is "perhaps the largest open problem". It gives no analogue of Pearl's methods for learning causal structure. It also defines the intended $\mathrm{true}(\cdot)$ operator over counterpossibles as unavailable ("it's not clear how to define a $\mathrm{true}$ operator") and bypasses it by assuming $G$ is supplied. So, strictly, A-FDT is only as determinate as the modeler's $G$.

**An operational heuristic of my own, not the source's.** To draw $G$ for a new problem, I suggest asking, for each variable: does something compute (or accurately model) my decision procedure on this input, so that it would differ if my procedure's output differed? If yes, add an arrow from the function node to it. Otherwise treat it as causally downstream only or independent. This reproduces the source's graphs: predictors and twins get arrows, lesions do not. The heuristic inherits the source's gap, because predictor reliability must be modeled by hand.

**Observations and policies.** The source's footnotes say its preferred formalization intervenes on policies (maps from observations to actions), which matters in multi-agent cases. Equation (4) as written uses per-observation nodes. For single-agent problems the two agree in the source's examples. My recommendation is that when a decision includes observation-dependent branches, you evaluate whole policies by intervening on the function's output across all inputs, then read off the action for your actual input. This is my reading, not a claim of the source.

**Stochastic and imperfect dependence.** The source handles imperfect predictors with an "Accurate" noise variable that flips the prediction, rather than by weakening the dependence itself. I follow this: put the unreliability in explicit stochastic nodes on the arrows leaving $\mathrm{fdt}$.

**Self-uncertainty.** The probabilities $q$ of how she would act in other branches turned out not to matter in the source's examples, because they enter both options equally or are fixed by the correct answer. The source does not claim this in general.

**Reflective stability.** The source claims A-FDT is "reflectively stable in fair problems" and needs no precommitment, since she acts as she would have precommitted. This is an argued claim, not a proof.

## 7. A recipe

1. Build $P$ with outcome variables and utility $V$.
2. Identify the function node(s) $\mathrm{fdt}(\cdot,\cdot,x)$ for each observation, and add arrows to everything that computes or models the decision procedure, including your own action.
3. For each action, compute $\mathbb E[V\mid \mathrm{do}(\mathrm{fdt}(\cdot,x)=a)]$, letting the intervention propagate along those arrows, including to whether observation $x$ occurs.
4. Take the argmax.

## 8. Conclusion

A-FDT keeps the expected-utility skeleton and Pearl's surgery, but relocates the surgery from the physical act to the decision function's output, and replaces conditioning on observation with a change of intervention node. The result one-boxes, smokes, pays the driver, refuses blackmail, and stays in Damascus. The source's own caveat stands: the theory's verdicts depend on a subjunctive-dependence graph that nobody yet knows how to learn in general.